from commonBase.envData import commonData
import unittest

class TestUserFunc(unittest.TestCase):
    params = None

    @classmethod
    def setUpClass(cls):
        if cls.params:
            print(f"接收到的参数: {cls.params}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("第一次结束后操作")

    def test_01(self):
        print("这是case1")
        r=2
        self.assertEqual(2,r,"判断相等")

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(myunitest("test_01"))
    unittest.TextTestRunner().run(suite)