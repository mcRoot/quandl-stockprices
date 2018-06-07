import unittest
from mc.stockprices.quandl.client import QuandlClient
import mc.tests.test_config as test_config

class QuandlClientTestCase(unittest.TestCase):

    def test_connect_table(self):
        c = QuandlClient()
        data = c.connect_to_table(table="WIKI/PRICES",ticker="FB",from_date='2018-03-01', to_date="2018-03-03",
                                  columns=['date', 'ticker', 'close'], apikey=test_config.apy_key)
        self.assertIsNotNone(data)