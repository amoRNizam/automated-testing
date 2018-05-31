import unittest
import BrowserInteractions

BrowserInteractionsTestSuite = unittest.TestSuite()
BrowserInteractionsTestSuite.addTest(unittest.makeSuite(BrowserInteractions.BrowserInteractions))
# calcTestSuite.addTest(unittest.makeSuite(test-1.CalcExTests))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(BrowserInteractionsTestSuite)