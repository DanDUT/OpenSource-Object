#！/usr/bin/python
# coding: utf-8
import unittest
from testchart import testchart
#模块名（testchart.py） 函数变量/类(testchart)

class ChartTestCase(unittest.TestCase):
    def test_1(self):
        #self.assertEqual(真实行为，预期行为）
        self.assertEqual(testchart('daily'), 14)
    def test_2(self):
        self.assertEqual(testchart('weekly'),17)
    def test_3(self):
        self.assertEqual(testchart('monthly'),14)

if  __name__ == "__main__":
    unittest.main()