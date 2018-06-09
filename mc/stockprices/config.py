import os


messages = {
    "errors": {
        "ticker_not_found": "You must specify a valid ticker.",
        "no_data_found": "No data was found for the specified ticker code '{}'."
    },
    "info": {
        "chart": "<strong>{}</strong> Price Trend from <strong>{}</strong> to <strong>{}</strong>"
    }
}

app_config = {
    "apy_key": os.environ.get('QUANDL_KEY', 'APY_KEY_HERE'),
    "table": "WIKI/PRICES",
    "to_date": '2018-03-27',#datetime.datetime.now().strftime("%Y-%m-%d"),
    "max_date": '2018-03-27',
    "from_date": '2018-02-20',
    "columns": ["date", "close", "open", "high", "low"],
    "supported_charts": ["close", "open", "high", "low"],
    "default_measures": ["close"]
}