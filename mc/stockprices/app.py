import numpy as np
from flask import Flask, render_template, request, redirect, url_for, make_response
from mc.stockprices.config import messages, app_config
from mc.stockprices.quandl.manager import PlottingManager, TableManager

app = Flask(__name__)
tm = TableManager(table=app_config["table"], apikey=app_config["apy_key"])
pm = PlottingManager()

@app.route('/prices/<ticker>/trend', methods=['POST'])
def price_trend(ticker=None):
    if request.method == 'POST':
        if ticker is None:
            return make_response(render_template('prices.html', error=messages.errors.ticker_not_found))
        else:
            to_date_cfg = app_config["to_date"]
            to_date_parsed = np.datetime64(to_date_cfg, 'D'),
            to_date = "{}".format(to_date_cfg)
            from_date_parsed = to_date_parsed[0] - app_config["days_back"]
            from_date = "{}".format(str(from_date_parsed)[:10])
            ticker_model = tm.retrieve_ticker(ticker=ticker, from_date=from_date, to_date=to_date,
                                              columns=app_config["columns"])
            script, div = pm.plot(ticker=ticker_model)
            return render_template("prices.html", script=script, div=div)
    else:
        redirect(url_for("prices"))

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/')
def index():
  return redirect(url_for("prices"))

@app.route('/version')
def version():
  return 'Quandl Stock Prices v. 1.0'

if __name__ == '__main__':
  app.run(port=8080)
