import numpy as np
import datetime
import os
import json

env_data = {}

with open('env-config.json') as json_data_file:
    env_data = json.load(json_data_file)

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
    "apy_key": os.environ.get('QUANDL_KEY', env_data["quandl"]["api_key"]),
    "table": "WIKI/PRICES",
    "to_date": '2018-03-27',#datetime.datetime.now().strftime("%Y-%m-%d"),
    "max_date": '2018-03-27',
    "from_date": '2018-02-20',
    "columns": ["date", "close", "open", "high", "low"],
    "supported_charts": ["close", "open", "high", "low"],
    "default_measures": ["close"]
}