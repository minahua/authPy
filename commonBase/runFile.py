import unittest
from pickUpStore.storeManage import TestMathFunc
from pickUpStore.userMange import myunitest
from pickUpStore.userMange import my2

def runTest(env):
    suite1=unittest.TestLoader().loadTestsFromTestCase(TestMathFunc)
    suite2=unittest.TestLoader().loadTestsFromTestCase(myunitest)
    suite3=unittest.TestLoader().loadTestsFromTestCase(my2)
    suiteall=unittest.TestSuite([suite1,suite2,suite3])
    unittest.TextTestRunner().run(suiteall)

env=''
runTest(env)