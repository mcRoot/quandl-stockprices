import numpy as np
from flask import Flask, render_template, request, redirect, url_for, make_response
from mc.stockprices.config import messages, app_config
from mc.stockprices.quandl.manager import PlottingManager, TableManager

app = Flask(__name__)
tm = TableManager(table=app_config["table"], apikey=app_config["apy_key"])
pm = PlottingManager()

@app.route('/prices/<ticker>/trend', methods=['POST', 'GET'])
def price_trend(ticker=None):
    if request.method == 'POST':
        if ticker is None:
            return make_response(render_template('prices.html', error=messages["errors"]["ticker_not_found"]))
        else:
            ticker = ticker.upper()
            script = None
            div = None
            error_message = None
            chart_title = ""

            to_date = request.form["to"]
            from_date = request.form["from"]

            measure_list = []
            for c in app_config["supported_charts"]:
                if (request.form.get(c)):
                    measure_list.append(c)

            try:
                ticker_model = tm.retrieve_ticker(ticker=ticker, from_date=from_date, to_date=to_date,
                                                  columns=app_config["columns"])
                script, div = pm.plot(ticker=ticker_model, measures=measure_list)
                chart_title = messages["info"]["chart"].format(ticker, from_date, to_date)
            except ValueError as e:
                error_message = messages["errors"][str(e)].format(ticker)
            except ConnectionError as ce:
                code = ce.__getattribute__("code")
                message = ce.__getattribute__("message")
                error_message = messages["errors"][str(ce)].format(code, message)

            return render_template("prices.html", ticker=ticker, script=script, div=div, measures=measure_list,
                                   chart_error=error_message, chart_title=chart_title, max_date=app_config["max_date"],
                                   start_date=from_date, end_date=to_date)
    else:
        return redirect(url_for("prices"))

@app.route('/prices')
def prices():
    return render_template('prices.html', measures=app_config["default_measures"], ticker="",
                           start_date=app_config["from_date"], end_date=app_config["to_date"],
                           max_date=app_config["max_date"])

@app.route('/')
def index():
  return redirect(url_for("prices"))

@app.route('/version')
def version():
  return 'Quandl Stock Prices v. 1.0'

if __name__ == '__main__':
  app.run(port=8080)
