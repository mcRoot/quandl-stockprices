import unittest
from mc.stockprices.quandl.manager import TableManager, PlottingManager
import mc.tests.test_config as test_config


class ModelTestCase(unittest.TestCase):

    def test_TableManager(self):
        tm = TableManager(table="WIKI/PRICES", apikey=test_config.apy_key)
        fb = tm.retrieve_ticker(ticker="FB", from_date='2018-03-01', to_date="2018-03-03", columns=['date', 'ticker', 'close'])
        self.assertEqual("FB", fb.name)
        self.assertGreater(len(fb), 0)
        count = 0
        for i in fb:
            count += 1
        self.assertEqual(len(fb), count)

    def test_PlottingManager(self):
        tm = TableManager(table="WIKI/PRICES", apikey=test_config.apy_key)
        pm = PlottingManager()
        fb = tm.retrieve_ticker(ticker="FB", from_date='2018-03-01', to_date="2018-03-03", columns=['date', 'ticker', 'close'])
        self.assertEqual("FB", fb.name)
        script, div = pm.plot(fb)
        print(script + "\n" + div)