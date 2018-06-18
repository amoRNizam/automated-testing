import unittest
import PriceSitilink, ikor

testLoad = unittest.TestLoader()
tc1 = testLoad.loadTestsFromModule(PriceSitilink)
tc2 = testLoad.loadTestsFromModule(ikor)

tc = unittest.TestSuite([tc1, tc2])
#runner = unittest.TextTestRunner(verbosity=2)
#runner.run(suites)
runner = unittest.TextTestRunner(verbosity=2)
testResult = runner.run(tc)
print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)
