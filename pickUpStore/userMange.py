from commonBase.envData import commonData
import unittest

class myunitest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.auth=commonData.baseData.authorization.value
    @classmethod
    def tearDownClass(cls) -> None:
        print("第一次结束后操作")

    def test_01(self):
        print("这是case1")
        r=2
        self.assertEqual(2,r,"判断相等")

    def test_02(self):
        print("这是case2")

class my2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("第二次开始前准备")

    @classmethod
    def tearDownClass(cls) -> None:
        print("第二次结束后操作")
    def test_03(self):
        print("这是case03")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(myunitest("test_01"))
    suite.addTest(my2("test_03"))
    unittest.TextTestRunner().run(suite)