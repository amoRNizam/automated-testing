import unittest
import PriceSitilink

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(PriceSitilink)
#runner = unittest.TextTestRunner(verbosity=2)
#runner.run(suites)
runner = unittest.TextTestRunner(verbosity=1)
testResult = runner.run(suites)
print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)
