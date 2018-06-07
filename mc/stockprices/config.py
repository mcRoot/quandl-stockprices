import numpy as np
import datetime

messages = {
    "errors": {
        "ticker_not_found": "You must specify a valid ticker.",
        "no_data_found": "No data was found for the specified ticker code '{}'."
    }
}

app_config = {
    "apy_key": "v_fSkbj2m-Mw1wxb4GNq",
    "table": "WIKI/PRICES",
    "to_date": '2018-03-27',#datetime.datetime.now().strftime("%Y-%m-%d"),
    "days_back": 30,
    "columns": ["date", "close", "open", "high", "low"]
}