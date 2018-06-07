import requests
import numpy as np


class QuandlClient:

    def __init__(self):
        self.base_url = "https://www.quandl.com/api/v3/{path}";
        self.datatables_path = "datatables/{table_code}.{format}"

    def connect_to_table(self, table=None, format='json', ticker=None, from_date=None, to_date=None, columns=None,
                         apikey=None):
        data = None
        param_missing = table is None or format is None or ticker is None or apikey is None
        if param_missing:
            raise RuntimeError('Missing required parameters')
        else:
            payload = {}
            if ticker:
                payload["ticker"] = ticker
            if from_date:
                payload["date.gte"] = from_date
            if to_date:
                payload["date.lte"] = to_date
            if columns:
                payload["qopts.columns"] = ",".join(str(c) for c in columns)
            if apikey:
                payload["api_key"] = apikey

            datatable_path = self.datatables_path.format(table_code=table, format=format)
            r = requests.get(self.base_url.format(path=datatable_path), params=payload)
            self._check_statuscode(r.status_code)
            json_resp = r.json()
            data = np.array(json_resp["datatable"]["data"])
            next_page_id = json_resp["meta"]["next_cursor_id"]
            while next_page_id is not None:
                payload["qopts.cursor_id"] = next_page_id
                r = requests.get(self.base_url.format(path=datatable_path), params=payload)
                self._check_statuscode(r.status_code)
                json_resp = r.json()
                data = np.concatenate((data, np.array(json_resp["datatable"]["data"])))
                next_page_id = json_resp["meta"]["next_cursor_id"]

        return data

    def _check_statuscode(self, code):
        if (code >= 300):
            raise ConnectionError("Something went wrong on connecting to QUANDL - error code {}".format(code))