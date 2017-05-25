# coding=utf-8

import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print "init by SetUp..."

    def tearDown(self):
        print "end by TearDown..."

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    # unittest.main()
    # 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    # 生成测试报告
    print ("testsRun: %s" % test_result.testsRun)
    print ("failures: %s " % len(test_result.failures))
    print ("error: %s" % len(test_result.errors))
    print ("skipped: %s" % len(test_result.skipped))
