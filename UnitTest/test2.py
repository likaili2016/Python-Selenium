#coding=utf-8
from Count import Count
import unittest

class TestCount (unittest.TestCase):

    def setUp(self):
        self.j = Count(self, 5, 4)

    def test_add(self):
        self.add = self.j.add()
        self.assertEqual(self.add, 6)

    def tearDown(self):
        pass

if __name__  == '__main__':
    unittest.main()