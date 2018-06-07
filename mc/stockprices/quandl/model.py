import pandas as pd
import numpy as np


class Ticker:

    def __init__(self, name=None, data=np.array([]), columns=[]):
        if name is None:
            raise ValueError("Ticker name cannot be undefined")
        if "date" not in columns:
            raise ValueError("Date column is mandatory")
        if data.shape[0] == 0:
            raise ValueError("no_data_found")
        self.name = name
        self.data = pd.DataFrame(data, columns=columns)
        self._clean_data()

    def _clean_data(self):
        self.data = self.data.dropna()
        self.data["date_parsed"] = self.data["date"].astype('datetime64[D]')
        self.data.drop(columns=["date"], inplace=True)
        self.data.set_index("date_parsed", inplace=True)

    def __str__(self):
        return "name: {}, columns: {}, rows: {}".format(self.name, self.data.columns.values, self.data.shape[0])

    def __len__(self):
        return self.data.shape[0]

    def __iter__(self):
        for x in self.data.values:
            yield x
