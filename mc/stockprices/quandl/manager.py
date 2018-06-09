from mc.stockprices.quandl.client import QuandlClient
from mc.stockprices.quandl.model import Ticker
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import NumeralTickFormatter, Legend

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
        except ConnectionError as e:
            raise e

class PlottingManager:

    def __init__(self, text_color="gray", line_colors=["lightskyblue", "orange", "tan", "blue"]):
        self.text_color = text_color
        self.line_color = line_colors

    def plot(self, ticker=None, measures=[]):
        if ticker is None:
            raise ValueError("Ticker to plot is mandatory")

        data = ticker.data
        start_date = data.index.values[0]
        end_date =  data.index.values[len(data.index.values) - 1]
        num_days = end_date - start_date
        columns = data.columns.values

        p = figure(title="", sizing_mode="scale_width", x_axis_label="Date", y_axis_label="Price", x_axis_type="datetime")
        p.plot_width = 800
        p.plot_height = 550
        p.title.text_color = self.text_color

        p.xaxis.axis_line_color = self.text_color
        p.yaxis.axis_line_color = self.text_color

        p.xaxis.axis_label_text_color = self.text_color
        p.yaxis.axis_label_text_color = self.text_color

        p.xaxis.major_label_text_color = self.text_color
        p.yaxis.major_label_text_color = self.text_color

        p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
        legend_items = []

        if "close" in measures:
            r1 = p.line(data.index, data["close"], line_color=self.line_color[3],
                line_width=1, alpha=0.8)
            r2 = p.circle(data.index, data["close"], size=8, fill_color=None, line_color=self.line_color[3])
            legend_items.append(("close", [r1, r2]))

        if "open" in measures:
            r1 = p.line(data.index, data["open"], line_color=self.line_color[0],
                   line_width=1, alpha=0.8)
            r2 = p.triangle(data.index, data["open"], size=8, fill_color=None, line_color=self.line_color[0])
            legend_items.append(("open", [r1, r2]))


        if "high" in measures:
            r1 = p.line(data.index, data["high"], line_color=self.line_color[1],
                   line_width=1, alpha=0.8)
            r2 = p.diamond(data.index, data["high"], size=8, fill_color=None, line_color=self.line_color[1])
            legend_items.append(("high", [r1, r2]))


        if "low" in measures:
            r1 = p.line(data.index, data["low"], line_color=self.line_color[2],
                   line_width=1, alpha=0.8)
            r2 = p.square(data.index, data["low"], size=8, fill_color=None, line_color=self.line_color[2])
            legend_items.append(("low", [r1, r2]))

        legend = Legend(items=legend_items, location=(0, 15), orientation="horizontal", click_policy="hide")
        p.add_layout(legend, 'above')

        return components(p)