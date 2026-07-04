import unittest


class TestUnittest(unittest.TestCase):

    def test_attributes_and_methods_of_unittest(self):
        reality = dir(unittest)
        my_expectation = [
            'BaseTestSuite', 'FunctionTestCase',
            'IsolatedAsyncioTestCase', 'SkipTest',
            'TestCase', 'TestLoader', 'TestProgram',
            'TestResult', 'TestSuite', 'TextTestResult',
            'TextTestRunner', '__all__', '__builtins__',
            '__cached__', '__dir__', '__doc__',
            '__file__', '__getattr__', '__loader__',
            '__name__', '__package__', '__path__',
            '__spec__', '__unittest', 'addModuleCleanup',
            'case', 'defaultTestLoader', 'doModuleCleanups',
            'enterModuleContext', 'expectedFailure',
            'installHandler', 'loader', 'main',
            'registerResult', 'removeHandler', 'removeResult',
            'result', 'runner', 'signals', 'skip', 'skipIf',
            'skipUnless', 'suite', 'util'
        ]
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_attributes_and_methods_of_unittest_testcase(self):
        reality = dir(unittest.TestCase)
        my_expectation = [
            '__call__', '__class__', '__delattr__',
            '__dict__', '__dir__', '__doc__', '__eq__',
            '__firstlineno__', '__format__', '__ge__',
            '__getattribute__', '__getstate__', '__gt__',
            '__hash__', '__init__', '__init_subclass__',
            '__le__', '__lt__', '__module__', '__ne__',
            '__new__', '__reduce__', '__reduce_ex__',
            '__repr__', '__setattr__', '__sizeof__',
            '__static_attributes__', '__str__',
            '__subclasshook__', '__weakref__',
            '_addDuration', '_addExpectedFailure',
            '_addUnexpectedSuccess', '_assertNotWarns',
            '_baseAssertEqual', '_callCleanup',
            '_callSetUp', '_callTearDown', '_callTestMethod',
            '_diffThreshold', '_formatMessage',
            '_getAssertEqualityFunc', '_tail_type_check',
            '_truncateMessage', 'addClassCleanup',
            'addCleanup', 'addTypeEqualityFunc',
            'assertAlmostEqual', 'assertCountEqual',
            'assertDictEqual', 'assertEndsWith',
            'assertEqual', 'assertFalse', 'assertGreater',
            'assertGreaterEqual', 'assertHasAttr',
            'assertIn', 'assertIs', 'assertIsInstance',
            'assertIsNone', 'assertIsNot',
            'assertIsNotNone', 'assertIsSubclass',
            'assertLess', 'assertLessEqual',
            'assertListEqual', 'assertLogs',
            'assertMultiLineEqual', 'assertNoLogs',
            'assertNotAlmostEqual', 'assertNotEndsWith',
            'assertNotEqual', 'assertNotHasAttr',
            'assertNotIn', 'assertNotIsInstance',
            'assertNotIsSubclass', 'assertNotRegex',
            'assertNotStartsWith', 'assertRaises',
            'assertRaisesRegex', 'assertRegex',
            'assertSequenceEqual', 'assertSetEqual',
            'assertStartsWith', 'assertTrue',
            'assertTupleEqual', 'assertWarns',
            'assertWarnsRegex', 'countTestCases',
            'debug', 'defaultTestResult',
            'doClassCleanups', 'doCleanups',
            'enterClassContext', 'enterContext', 'fail',
            'failureException', 'id', 'longMessage',
            'maxDiff', 'run', 'setUp', 'setUpClass',
            'shortDescription', 'skipTest', 'subTest',
            'tearDown', 'tearDownClass'
        ]
        assert reality == my_expectation
        self.assertEqual(reality, my_expectation)

    def test_assert_is_not(self):
        assert None is not False
        self.assertIsNot(None, False)

    def test_assert_is(self):
        assert False is False
        self.assertIs(False, False)

    def test_assert_not_equal(self):
        assert True != 0
        self.assertNotEqual(True, 0)

    def test_assert_equal(self):
        assert 0.0 == 0.0
        self.assertEqual(0.0, 0.0)

    def test_assert_not_is_instance(self):
        assert not isinstance(
            unittest.TestCase, unittest.TestCase
        )
        self.assertNotIsInstance(
            unittest.TestCase, unittest.TestCase
        )

    def test_assert_is_instance(self):
        a_class = unittest.TestCase
        an_instance = a_class()

        assert isinstance(an_instance, a_class)
        self.assertIsInstance(
            an_instance, a_class
        )
        self.assertIsInstance(
            self, unittest.TestCase
        )

    def test_assert_not_is_subclass(self):
        assert not issubclass(
            unittest.TestCase, list
        )
        self.assertNotIsSubclass(
            unittest.TestCase, dict
        )

    def test_assert_is_subclass(self):
        assert issubclass(unittest.TestCase, object)
        self.assertIsSubclass(
            unittest.TestCase, object
        )
        self.assertIsSubclass(
            TestUnittest, unittest.TestCase
        )


# Exceptions seen
# AssertionError
# NameError
# TypeError
# AttributeError