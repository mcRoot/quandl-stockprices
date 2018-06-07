from mc.stockprices.quandl.client import QuandlClient
from mc.stockprices.quandl.model import Ticker
from bokeh.plotting import figure
from bokeh.embed import components

class TableManager:

    def __init__(self, table=None, apikey=None):
        if (table is None or apikey is None):
            raise ValueError("Missing one or more required params")
        self.table = table
        self.apy_key = apikey
        self.client = QuandlClient()

    def retrieve_ticker(self, ticker=None, from_date=None, to_date=None, columns=None):
        try:
            data = self.client.connect_to_table(table=self.table, ticker=ticker, from_date=from_date,
                                                to_date=to_date, columns=columns, apikey=self.apy_key)
            return Ticker(name=ticker, data=data, columns=columns)
        except:
            raise

class PlottingManager:

    def __init__(self, text_color="gray", line_color="navy"):
        self.text_color = text_color
        self.line_color = line_color

    def plot(self, ticker=None):
        if ticker is None:
            raise ValueError("Ticker to plot is mandatory")

        data = ticker.data
        start_date = data.index.values[0]
        end_date =  data.index.values[len(data.index.values) - 1]
        num_days = end_date - start_date
        columns = data.columns.values

        p = figure(title="{} Price Trend from {} to {}".format(ticker.name,
                                                                            str(start_date)[:10], str(end_date)[:10]),
                   x_axis_label="Date", y_axis_label="Price ($)", x_axis_type="datetime")

        p.title.text_color = self.text_color

        p.xaxis.axis_line_color = self.text_color
        p.yaxis.axis_line_color = self.text_color

        p.xaxis.axis_label_text_color = self.text_color
        p.yaxis.axis_label_text_color = self.text_color

        p.xaxis.major_label_text_color = self.text_color
        p.yaxis.major_label_text_color = self.text_color

        p.line(data.index, data["close"], line_color=self.line_color,
               line_width=1, alpha=0.5)

        return components(p)