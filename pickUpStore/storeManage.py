# -*- coding: utf-8 -*-

import unittest
from commonBase.commonMethod import comMethod

class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('end')

    def test_add(self):
        """Test method add(a, b)"""
        print('add')
        self.assertEqual(3, 1+2)
        self.assertNotEqual(3, 2+2)

    def test_minus(self):
        """Test method minus(a, b)"""
        print('--')
        self.assertEqual(1, 3-2)

    def test_multi(self):
        """Test method multi(a, b)"""
        print('*')
        self.assertEqual(6,2*3)

    def test_divide(self):
        """Test method divide(a, b)"""
        print('/')
        self.assertEqual(2, 2/1)
        self.assertEqual(2.5,5/2)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)