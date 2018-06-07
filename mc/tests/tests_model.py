import unittest
from mc.stockprices.quandl.client import QuandlClient
from mc.stockprices.quandl.model import Ticker
import mc.tests.test_config as test_config


class ModelTestCase(unittest.TestCase):

    def test_Ticker(self):
        c = QuandlClient()
        data = c.connect_to_table(table="WIKI/PRICES", ticker="FB", from_date='2018-03-01', to_date="2018-03-03",
                                  columns=['date', 'ticker', 'close'], apikey=test_config.apy_key)
        fb = Ticker(name="FB", data=data, columns=["date", "ticker", "close"])
        self.assertEqual("FB", fb.name)
        self.assertGreater(len(fb), 0)
        count = 0
        for i in fb:
            count += 1
        self.assertEqual(len(fb), count)