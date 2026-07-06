.. meta::
  :description: Another way to write tests in Python TDD: use the unittest.TestCase class (from the standard library) and its built-in assert methods as alternatives to bare `assert` statements. Step-by-step RED/GREEN/REFACTOR on the "unittest" project (uv init, mkdir tests, pytest-watcher): inspect dir(unittest) and dir(unittest.TestCase), demonstrate two ways for each of assertIsNot ("X is not Y"), assertIs, assertNotEqual, assertEqual, assertNotIsInstance / isinstance, assertIsInstance, assertNotIsSubclass / issubclass, assertIsSubclass. Covers calling on the class, on an instance, refactoring through TOOLBOX class attr and @staticmethod to self. methods inside TestCase subclass. Exact errors reproduced: "unexpectedly identical: None", "assert False is True", TypeError missing arguments for assertIsNot(), AssertionError from dir lists. Part of Jacob Itegboje Pumping Python TDD series for beginners.
  :keywords: Jacob Itegboje, Pumping Python, another way to write tests, unittest.TestCase, unittest assert methods, assertIsNot, assertIs, assertNotEqual, assertEqual, assertNotIsInstance, assertIsInstance, assertNotIsSubclass, assertIsSubclass, two ways to test, bare assert vs self.assert, dir(unittest), TestCase dir, unexpectedly identical: None, uv init unittest pytest-watcher, TestCase subclass, TOOLBOX refactor, self. methods, python TDD unittest, standard library testing, is vs == vs assertIs, isinstance issubclass unittest, python beginner unittest tutorial

.. include:: ../links.rst

.. _unittest.TestCase: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase
.. _TestCase: https://docs.python.org/3/library/unittest.html#unittest.TestCase
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _unittest module: unittest_
.. _assertNotIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance
.. _unittest.TestCase.assertNotIsInstance: assertNotIsInstance_
.. _assertNotIsInstance method: assertNotIsInstance_
.. _assertIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance
.. _unittest.TestCase.assertIsInstance: assertIsInstance_
.. _assertIsInstance method: assertIsInstance_
.. _assertNotIsSubclass: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsSubclass
.. _assertNotIsSubclass method: assertNotIsSubclass_
.. _unittest.TestCase.assertNotIsSubclass: assertNotIsSubclass_
.. _assertIsSubclass: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsSubclass
.. _assertIsSubclass method: assertIsSubclass_
.. _unittest.TestCase.assertIsSubclass: assertIsSubclass_
.. _assert method: https://docs.python.org/3/library/unittest.html#assert-methods
.. _assert methods: `assert method`_
.. _unittest.TestCase.assertEqual: assertEqual_
.. _unittest.TestCase.assertNotEqual: assertNotEqual_
.. _assertEqual: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual
.. _assertEqual method: assertEqual_
.. _assertNotEqual: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual
.. _assertIs: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs
.. _assertIs method: assertIs_
.. _unittest.TestCase.assertIs: assertIs_
.. _assertIsNot: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot
.. _assertIsNot method: assertIsNot_
.. _unittest.TestCase.assertIsNot: assertIsNot_
.. _assertNotEqual method: assertNotEqual_
.. _unittest.TestCase class: `unittest.TestCase`_
.. _TestCase class: `unittest.TestCase`_
.. _click here to see the source code for unittest: https://github.com/python/cpython/blob/3.14/Lib/unittest/__init__.py

#################################################################################
another way to write tests
#################################################################################

I used unittest_ in :ref:`how to make a Python test driven development environment manually` to run tests manually before I learned to :ref:`run them automatically<how to run tests automatically>` with `pytest-watcher`_.

The unittest_ :ref:`library<what is a module?>` is part of `The Python Standard Library`_ and can also be used to write tests. You can think of it as a toolbox with different tools I can use to test code.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/tests/test_unittest.py
  :language: python
  :linenos:

*********************************************************************************
Questions about unittest
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`What are two ways to test if something is not something else?<test_assert_is_not>`
* :ref:`What are two ways to test if something is something?<test_assert_is>`
* :ref:`What are two ways to test if two things are not equal?<test_assert_not_equal>`
* :ref:`What are two ways to test if two things are equal?<test_assert_equal>`
* :ref:`What are two ways to test if something is not an instance<test_assert_not_is_instance>`
* :ref:`What are two ways to test if something is an instance<test_assert_is_instance>`
* :ref:`What are two ways to test if something is not a subclass<test_assert_not_is_subclass>`
* :ref:`What are two ways to test if something is a subclass<test_assert_is_subclass>`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``unittest``
* I open a terminal_
* I `change directory`_ to the ``unittest`` folder_ in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd unittest

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: unittest

* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init unittest

  the terminal_ shows

  .. code-block:: shell

    Initialized project `unittest`
    at `.../pumping_python/unittest`

* I `change directory`_ to ``unittest``

  .. code-block:: python
    :emphasize-lines: 1

    cd unittest

  the terminal_ shows I am in the ``unittest`` folder_

  .. code-block:: python

    .../pumping_python/unittest

* I `make a directory`_ for the tests

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

* I use the `mv program`_ to change the name of ``main.py`` to ``test_unittest.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py tests/test_unittest.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py tests/test_unittest.py

* I open ``test_unittest.py``

* I delete the text in the file_ then add :ref:`the first failing test<test_failure>` to ``test_unittest.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_failure():
        assert False is True

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 6, 8, 10

    ======================== FAILURES ========================
    ______________________ test_failure ______________________

        def test_failure():
    >       assert False is True
    E       assert False is True

    test_unittest.py:2: AssertionError
    ================ short test summary info =================
    FAILED test_unittest.py::test_failure - assert False is True
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`.

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    and try ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_unittest.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6
    :emphasize-text: AssertionError

    def test_failure():
        assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_failure():
        # assert False is True
        assert False is False


    # Exceptions seen
    # AssertionError

  the test passes.


----

*********************************************************************************
test_attributes_and_methods_of_unittest
*********************************************************************************

I want to see what comes with the `unittest module`_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change ``test_failure`` to :ref:`test_attributes_and_methods_of_unittest` in ``test_unittest.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def test_attributes_and_methods_of_unittest():
        reality = dir(unittest)
        my_expectation = []
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'unittest' is not defined.
                Did you forget to import 'unittest'?

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for `unittest`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import unittest


    def test_attributes_and_methods_of_unittest():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError:
              assert ['BaseTestSui...tLoader', ...]
           == []
    E
    E         Left contains 44 more items,
              first extra item: 'BaseTestSuite'
    E         Use -v to get more diff

* I click in the terminal_ where the tests are running then press :kbd:`v` on the keyboard for `pytest-watcher`_ to show me more of the difference between ``reality`` and ``my_expectation`` and it shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E         ...Full output truncated (44 lines hidden),
                 use '-vv' to show

* I press :kbd:`w` on the keyboard in the terminal_ where the tests are running, to show the menu for `pytest-watcher`_ and it shows

  .. code-block:: python
    :emphasize-lines: 2, 10

    [pytest-watcher]
    Current runner args: [-v]

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

* I press :kbd:`c` on the keyboard to change runner args, and the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 7, 14

    [pytest-watcher]
    Current runner args: []

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

    Enter new runner args: -vv

* I press :kbd:`-+v+v` on the keyboard then press :kbd:`enter` to show the full difference, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with the full :ref:`list<what is a list?>`.

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-19
    :emphasize-text: TestCase

    def test_attributes_and_methods_of_unittest():
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


    # Exceptions seen

  the test passes because when ``import unittest`` runs, Python_ brings in an :ref:`object (everything in Python is an object)<what is a class?>` for the `unittest module`_ from `The Python Standard Library`_ so I can use it in ``test_unittest.py`` as ``unittest``.

  This means that there is a file_ or folder_ on the computer named ``unittest`` that got added when I installed Python_.

  .. caution:: Your list of attributes and methods may be different depending on your Python version

* I open a new terminal_ then make sure I am in the ``classes`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd classes

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attributes_and_methods_of_unittest'

----

*********************************************************************************
test_attributes_and_methods_of_unittest_testcase
*********************************************************************************

One of the names in the list of :ref:`attributes and methods of unittest<test_attributes_and_methods_of_unittest>` is ``TestCase``, this is the :ref:`class (toolbox)<what is a class?>` that contains the things I will use to write tests for code.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for the :ref:`attributes and methods of TestCase<test_attributes_and_methods_of_unittest_testcase>`

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 4-7

      assert reality == my_expectation


  def test_attributes_and_methods_of_unittest_testcase():
      reality = dir(unittest.TestCase)
      my_expectation = []
      assert reality == my_expectation


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  E       AssertionError: assert
            ['__call__', ...__doc__', ...] == []
  E
  E         Left contains 108 more items,
            first extra item: '__call__'
  E         Use -v to get more diff

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I click in the terminal_ where the tests are running then press :kbd:`v` on the keyboard for `pytest-watcher`_ to show me more of the difference between ``reality`` and ``my_expectation`` and it shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E         ...Full output truncated (108 lines hidden),
                 use '-vv' to show

* I press :kbd:`w` on the keyboard in the terminal_ where the tests are running, to show the menu for `pytest-watcher`_ and it shows

  .. code-block:: python
    :emphasize-lines: 2, 10

    [pytest-watcher]
    Current runner args: [-v]

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

* I press :kbd:`c` on the keyboard to change runner args, and the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 7, 14

    [pytest-watcher]
    Current runner args: []

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

    Enter new runner args: -vv

* I press :kbd:`-+v+v` on the keyboard then press :kbd:`enter` to show the full difference, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with the entire :ref:`list<what is a list?>`.

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-48
    :emphasize-text: assertIsNot assertIs assertIsInstance assertNotIsInstance assertIsSubclass assertNotIsSubclass assertEqual assertNotEqual

    def test_attributes_and_methods_of_unittest_testcase():
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


    # Exceptions seen

  - The test passes.
  - The :ref:`__init__ method<the constructor method>` is in the :ref:`list of attributes and methods<test_attributes_and_methods_of_unittest_testcase>` because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I see names that begin with ``assert`` and look like some of the :ref:`assertions<what is an assertion?>` I have written so far.

  ===================== ===============================
  assertIsNot_          ``assert X is not Y``
  assertIs_             ``assert X is Y``
  assertNotEqual_       ``assert X != Y``
  assertEqual_          ``assert X == Y``
  assertNotIsInstance_  ``assert not isinstance(X, Y)``
  assertIsInstance_     ``assert isinstance(X, Y)``
  assertNotIsSubclass_  ``assert not issubclass(X, Y)``
  assertIsSubclass_     ``assert issubclass(X, Y)``
  ===================== ===============================

* I type these names below the test as a TODO list to test what I can do with them

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4-11

    assert reality == my_expectation


    'assertIsNot'
    'assertIs'
    'assertNotEqual'
    'assertEqual'
    'assertNotIsInstance'
    'assertIsInstance'
    'assertNotIsSubclass'
    'assertIsSubclass'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attributes_and_methods_of_unittest_testcase'

----

*********************************************************************************
test_assert_is_not
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for assertIsNot_

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4-5

        assert reality == my_expectation


    def test_assert_is_not():
        unittest.TestCase.assertIsNot()


    'assertIsNot'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

     TypeError: TestCase.assertIsNot() missing
                3 required positional arguments:
                'self', 'expr1', and 'expr2'

  - because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.
  - The :ref:`definition<how to make a function that takes input>` of the `assertIsNot method`_  of the `TestCase class`_  of the unittest_ library (``unittest.TestCase.assertIsNot``) has two required :ref:`positional arguments<test_positional_arguments>`. I imagine Python_ follows this path when `unittest.TestCase.assertIsNot`_ is called

    .. code-block:: shell

      unittest
      └── class TestCase:
          └── def assertIsNot(self, expr1, expr2):
              └── return something

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 7
    :emphasize-text: TypeError

    'assertIsSubclass'


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the call to use :ref:`an instance<how to test if something is an instance>` instead of a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 2-3

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        unittest.TestCase().assertIsNot()


    'assertIsNot'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertIsNot() missing
               2 required positional arguments:
               'expr1' and 'expr2'

  I no longer need to provide ``self`` because it is the :ref:`instance of the class<how to test if something is an instance>` (``unittest.TestCase()``)

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertIsNot`_

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 3-4

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        # unittest.TestCase().assertIsNot()
        unittest.TestCase().assertIsNot(None, None)


    'assertIsNot'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: unexpectedly identical: None

  because :ref:`None is None<what is None?>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 4-5

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        # unittest.TestCase().assertIsNot()
        # unittest.TestCase().assertIsNot(None, None)
        unittest.TestCase().assertIsNot(None, False)


    'assertIsNot'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to compare it with the `assertIsNot method`_

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        # unittest.TestCase().assertIsNot()
        # unittest.TestCase().assertIsNot(None, None)
        assert None is not None
        unittest.TestCase().assertIsNot(None, False)


    'assertIsNot'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None is not None

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5-6

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        # unittest.TestCase().assertIsNot()
        # unittest.TestCase().assertIsNot(None, None)
        # assert None is not None
        assert None is not False
        unittest.TestCase().assertIsNot(None, False)


    'assertIsNot'
    'assertIs'

  the test passes.

* I remove assertIsNot_ from the TODO list

  .. code-block:: python
    :lineno-start: 84

        unittest.TestCase().assertIsNot(None, False)


    'assertIs'
    'assertNotEqual'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_is_not'

I imagine Python_ follows this path when `unittest.TestCase.assertIsNot`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertIsNot(self, expr1, expr2):
          └── assert expr1 is not expr2

Compare the error message for ``assertIsNot(None, None)`` with the one for ``assert None is not None``

.. code-block:: python

  AssertionError: unexpectedly identical: None

vs

.. code-block:: python

  assert None is not None

Which do you like better?

----

*********************************************************************************
test_assert_is
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for the `assertIs method`_

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 10-11

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        # unittest.TestCase().assertIsNot()
        # unittest.TestCase().assertIsNot(None, None)
        # assert None is not None
        assert None is not False
        unittest.TestCase().assertIsNot(None, False)


    def test_assert_is():
        assert False is True


    'assertIs'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert False is True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 87
  :emphasize-lines: 2-3

  def test_assert_is():
      # assert False is True
      assert False is False


  'assertIs'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the `assertIs method`_

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 4

    def test_assert_is():
        # assert False is True
        assert False is False
        unittest.TestCase.assertIs()


    'assertIs'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertIs() missing
               3 required positional arguments:
               'self', 'expr1', and 'expr2'

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I change the :ref:`call<how to call a function with input>` to use :ref:`an instance<how to test if something is an instance>` instead of a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 4-5

    def test_assert_is():
        # assert False is True
        assert False is False
        # unittest.TestCase.assertIs()
        unittest.TestCase().assertIs()


    'assertIs'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertIs() missing
               2 required positional arguments:
               'expr1' and 'expr2'

  I no longer need to provide ``self`` because it is the :ref:`instance of the class<how to test if something is an instance>` (``unittest.TestCase()``)

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertIs`_

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 5-6

    def test_assert_is():
        # assert False is True
        assert False is False
        # unittest.TestCase.assertIs()
        # unittest.TestCase().assertIs()
        unittest.TestCase().assertIs(False, True)


    'assertIs'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not True

  because :ref:`False is not True<test_assertion_error_w_false>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 6-7

    def test_assert_is():
        # assert False is True
        assert False is False
        # unittest.TestCase.assertIs()
        # unittest.TestCase().assertIs()
        # unittest.TestCase().assertIs(False, True)
        unittest.TestCase().assertIs(False, False)


    'assertIs'
    'assertNotEqual'

  the test passes.

* I remove assertIs_ from the TODO list

  .. code-block:: python
    :lineno-start: 93

        unittest.TestCase().assertIs(False, False)


    'assertNotEqual'
    'assertEqual'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_is'

I imagine Python_ follows this path when `unittest.TestCase.assertIs`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertIs(self, expr1, expr2):
          └── assert expr1 is expr2

Compare the error message for ``assertIs(False, True)`` with the one for ``assert False is True``

.. code-block:: python

  AssertionError: False is not True

vs

.. code-block:: python

  E       assert False is True

----

*********************************************************************************
test_assert_not_equal
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for assertNotEqual_

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 10-11

    def test_assert_is():
        # assert False is True
        assert False is False
        # unittest.TestCase.assertIs()
        # unittest.TestCase().assertIs()
        # unittest.TestCase().assertIs(False, True)
        unittest.TestCase().assertIs(False, False)


    def test_assert_not_equal():
        unittest.TestCase().assertNotEqual()


    'assertNotEqual'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertNotEqual() missing
               2 required positional arguments:
               'first', and 'second'

  the :ref:`definition<how to make a function that takes input>` of the `assertNotEqual method`_  of the `TestCase class`_  of the unittest_ library (``unittest.TestCase.assertNotEqual``) has two required :ref:`positional arguments<test_positional_arguments>` (``first`` and ``second``).

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertNotEqual`_

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 2-3

    def test_assert_not_equal():
        # unittest.TestCase().assertNotEqual()
        unittest.TestCase().assertNotEqual(True, True)


    'assertNotEqual'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True == True

  because :ref:`True is True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3-4

    def test_assert_not_equal():
        # unittest.TestCase().assertNotEqual()
        # unittest.TestCase().assertNotEqual(True, True)
        unittest.TestCase().assertNotEqual(True, 0)


    'assertNotEqual'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to compare it with the `assertNotEqual method`_

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 4

    def test_assert_not_equal():
        # unittest.TestCase().assertNotEqual()
        # unittest.TestCase().assertNotEqual(True, True)
        assert True != True
        unittest.TestCase().assertNotEqual(True, 0)


    'assertNotEqual'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert True != True

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 4-5

    def test_assert_not_equal():
        # unittest.TestCase().assertNotEqual()
        # unittest.TestCase().assertNotEqual(True, True)
        # assert True != True
        assert True != 0
        unittest.TestCase().assertNotEqual(True, 0)


    'assertNotEqual'
    'assertEqual'

  the test passes.

* I remove assertNotEqual_ from the TODO list

  .. code-block:: python
    :lineno-start: 101

        unittest.TestCase().assertNotEqual(True, 0)


    'assertEqual'
    'assertNotIsInstance'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_not_equal'

I imagine Python_ follows this path when `unittest.TestCase.assertNotEqual`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertNotEqual(self, first, second):
          └── assert first != second

Compare the error message for ``assertNotEqual(True, True)`` with the one for ``assert True != True``

.. code-block:: python

  AssertionError: True == True

vs

.. code-block:: python

  E       assert True != True

----

*********************************************************************************
test_assert_equal
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 9-10

    def test_assert_not_equal():
        # unittest.TestCase().assertNotEqual()
        # unittest.TestCase().assertNotEqual(True, True)
        # assert True != True
        assert True != 0
        unittest.TestCase().assertNotEqual(True, 0)


    def test_assert_equal():
        assert 0.0 == '0.0'


    'assertEqual'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert 0.0 == '0.0'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 104
  :emphasize-lines: 2-3

  def test_assert_equal():
      # assert 0.0 == '0.0'
      assert 0.0 == 0.0


  'assertEqual'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`call<how to call a function with input>` to the `assertEqual method`_

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 4

    def test_assert_equal():
        # assert 0.0 == '0.0'
        assert 0.0 == 0.0
        unittest.TestCase().assertEqual(0.0, '0.0')


    'assertEqual'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 0.0 != '0.0'

  because a float_ is not a string_.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 4-5

    def test_assert_equal():
        # assert 0.0 == '0.0'
        assert 0.0 == 0.0
        # unittest.TestCase().assertEqual(0.0, '0.0')
        unittest.TestCase().assertEqual(0.0, 0.0)


    'assertEqual'
    'assertNotIsInstance'

  the test passes.

* I remove the commented lines and assertEqual_ from the TODO list

  .. code-block:: python
    :lineno-start: 108

        unittest.TestCase().assertEqual(0.0, 0.0)


    'assertNotIsInstance'
    'assertIsInstance'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_equal'

I imagine Python_ follows this path when `unittest.TestCase.assertEqual`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertEqual(self, first, second):
          └── assert first is second

Compare the error message for ``assertEqual(0.0, '0.0')`` with the one for ``assert 0.0 == '0.0'``

.. code-block:: python

  AssertionError: 0.0 != '0.0'

vs

.. code-block:: python

  AssertionError: assert 0.0 == '0.0'

----

*********************************************************************************
test_assert_not_is_instance
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for the `assertNotIsInstance method`_

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 8-9

    def test_assert_equal():
        # assert 0.0 == '0.0'
        assert 0.0 == 0.0
        # unittest.TestCase().assertEqual(0.0, '0.0')
        unittest.TestCase().assertEqual(0.0, 0.0)


    def test_assert_not_is_instance():
        unittest.TestCase.assertNotIsInstance()


    'assertNotIsInstance'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertNotIsInstance() missing
               3 required positional arguments:
               'self', 'obj', and 'cls'

  - The :ref:`definition<how to make a function that takes input>` of the `assertNotIsInstance method`_  of the `TestCase class`_  of the unittest_ library (``unittest.TestCase.assertIsNot``) has three required :ref:`positional arguments<test_positional_arguments>` (``self``, ``obj`` and ``cls``)
  - A :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.
  - ``obj`` is for the :ref:`instance<how to test if something is an instance>` being tested.
  - ``cls`` is for the :ref:`class<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to use :ref:`an instance<how to test if something is an instance>` instead of a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 2-3

    def test_assert_not_is_instance():
        # unittest.TestCase.assertNotIsInstance()
        unittest.TestCase().assertNotIsInstance()


    'assertNotIsInstance'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertNotIsInstance()
               missing 2 required positional arguments:
               'obj' and 'cls'

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertNotIsInstance`_

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 4-6

    def test_assert_not_is_instance():
        # unittest.TestCase.assertNotIsInstance()
        # unittest.TestCase().assertNotIsInstance()
        unittest.TestCase().assertNotIsInstance(
            unittest.TestCase(), unittest.TestCase
        )


    'assertNotIsInstance'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <unittest.case.TestCase testMethod=runTest>
        is an instance of
        <class 'unittest.case.TestCase'>

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 5-6

    def test_assert_not_is_instance():
        # unittest.TestCase.assertNotIsInstance()
        # unittest.TestCase().assertNotIsInstance()
        unittest.TestCase().assertNotIsInstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )


    'assertNotIsInstance'

  the test passes because a :ref:`class<what is a class?>` is not an :ref:`instance<how to test if something is an instance>` of itself.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to compare it with the `assertNotIsInstance method`_

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 4-6

    def test_assert_not_is_instance():
        # unittest.TestCase.assertNotIsInstance()
        # unittest.TestCase().assertNotIsInstance()
        assert not isinstance(
            unittest.TestCase(), unittest.TestCase
        )
        unittest.TestCase().assertNotIsInstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )


    'assertNotIsInstance'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert not True

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 5-6

    def test_assert_not_is_instance():
        # unittest.TestCase.assertNotIsInstance()
        # unittest.TestCase().assertNotIsInstance()
        assert not isinstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )
        unittest.TestCase().assertNotIsInstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )


    'assertNotIsInstance'
    'assertIsInstance'

  the test passes.

* I remove assertNotIsInstance_ from the TODO list

  .. code-block:: python
    :lineno-start: 118

        unittest.TestCase().assertNotIsInstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )


    'assertIsInstance'
    'assertNotIsSubclass'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_not_is_instance'

I imagine Python_ follows this path when `unittest.TestCase.assertNotIsInstance`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertNotIsInstance(self, obj, cls):
          └── assert not isinstance(obj, cls)

Compare the error message for ``unittest.TestCase().assertNotIsInstance(unittest.TestCase(), unittest.TestCase)`` with the one for ``assert not isinstance(unittest.TestCase(), unittest.TestCase)``

.. code-block:: shell

  AssertionError:
      <unittest.case.TestCase testMethod=runTest>
      is an instance of
      <class 'unittest.case.TestCase'>

vs

.. code-block:: python

  AssertionError: assert not True

----

*********************************************************************************
test_assert_is_instance
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for `assertIsInstance`_

  .. code-block:: python
    :lineno-start: 118
    :emphasize-lines: 7-8

        unittest.TestCase().assertNotIsInstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )


    def test_assert_is_instance():
        unittest.TestCase.assertIsInstance()


    'assertIsInstance'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertIsInstance() missing
               3 required positional arguments:
               'self', 'obj', and 'cls'

  - A :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.
  - ``obj`` is for the :ref:`instance<how to test if something is an instance>` being tested.
  - ``cls`` is for the :ref:`class<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`call<how to call a function with input>` to use :ref:`an instance<how to test if something is an instance>` instead of a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 2-3

    def test_assert_is_instance():
        # unittest.TestCase.assertIsInstance()
        unittest.TestCase().assertIsInstance()


    'assertIsInstance'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertIsInstance()
               missing 2 required positional arguments:
               'obj' and 'cls'

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertIsInstance`_

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 3-6

    def test_assert_is_instance():
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        unittest.TestCase().assertIsInstance(
            unittest.TestCase, unittest.TestCase
        )


    'assertIsInstance'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'unittest.case.TestCase'>
        is not an instance of
        <class 'unittest.case.TestCase'>

  because a :ref:`class<what is a class?>` is not an :ref:`instance<how to test if something is an instance>` of itself.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 5-6

    def test_assert_is_instance():
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            unittest.TestCase(), unittest.TestCase
        )


    'assertIsInstance'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to compare it with the `assertIsInstance method`_

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 4-6

    def test_assert_is_instance():
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        assert isinstance(
            unittest.TestCase, unittest.TestCase
        )
        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            unittest.TestCase(), unittest.TestCase
        )


    'assertIsInstance'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 5-6

    def test_assert_is_instance():
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        assert isinstance(
            # unittest.TestCase, unittest.TestCase
            unittest.TestCase(), unittest.TestCase
        )
        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            unittest.TestCase(), unittest.TestCase
        )


    'assertIsInstance'

  the test passes.

* I add :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 2-3

    def test_assert_is_instance():
        a_class = unittest.TestCase
        an_instance = a_class()
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        assert isinstance(
            # unittest.TestCase, unittest.TestCase
            unittest.TestCase(), unittest.TestCase
        )
        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            unittest.TestCase(), unittest.TestCase
        )


    'assertIsInstance'
    'assertNotIsSubclass'

* I use the :ref:`variables<what is a variable?>` to remove repetition of ``unittest.TestCase`` and ``unittest.TestCase()``

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 8-9, 13-14

    def test_assert_is_instance():
        a_class = unittest.TestCase
        an_instance = a_class()
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        assert isinstance(
            # unittest.TestCase, unittest.TestCase
            # unittest.TestCase(), unittest.TestCase
            an_instance, a_class
        )
        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            # unittest.TestCase(), unittest.TestCase
            an_instance, a_class
        )


    'assertIsInstance'

  the test is still green.

* I remove assertIsInstance_ from the TODO list

  .. code-block:: python
    :lineno-start: 134

        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            # unittest.TestCase(), unittest.TestCase
            an_instance, a_class
        )


    'assertNotIsSubclass'
    'assertIsSubclass'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_is_instance'

I imagine Python_ follows this path when `unittest.TestCase.assertIsInstance`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertIsInstance(self, obj, cls):
          └── assert not isinstance(obj, cls)

Compare the error message for ``unittest.TestCase().assertIsInstance(unittest.TestCase, unittest.TestCase)`` with the one for ``assert isinstance(unittest.TestCase, unittest.TestCase)``

.. code-block:: shell

  AssertionError:
      <class 'unittest.case.TestCase'>
      is not an instance of
      <class 'unittest.case.TestCase'>

vs

.. code-block:: python

  AssertionError: assert False

----

*********************************************************************************
test_assert_not_is_subclass
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for `assertNotIsSubclass`_

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 8-9

        unittest.TestCase().assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            # unittest.TestCase(), unittest.TestCase
            an_instance, a_class
        )


    def test_assert_not_is_subclass():
        unittest.TestCase().assertNotIsSubclass()


    'assertNotIsSubclass'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertNotIsSubclass() missing
               2 required positional arguments:
               'cls', and 'superclass'

  - ``cls`` is for the :ref:`subclass<how to test if something is a subclass>` being tested.
  - ``superclass`` is for the :ref:`parent class<what is a class?>` of the :ref:`subclass<how to test if something is a subclass>` being tested.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertNotIsSubclass`_

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 3-5

    def test_assert_not_is_subclass():
        # unittest.TestCase().assertNotIsSubclass()
        unittest.TestCase().assertNotIsSubclass(
            unittest.TestCase(), object
        )


    'assertNotIsSubclass'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <unittest.case.TestCase testMethod=runTest>
        is not a class

  because :ref:`an instance is not a class<instance vs subclass>`.

* I change the :ref:`assertion<what is an assertion?>` to use a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 4-5

    def test_assert_not_is_subclass():
        # unittest.TestCase().assertNotIsSubclass()
        unittest.TestCase().assertNotIsSubclass(
            # unittest.TestCase(), object
            unittest.TestCase, object
        )


    'assertNotIsSubclass'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'unittest.case.TestCase'>
        is a subclass of <class 'object'>

  because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 5-6

    def test_assert_not_is_subclass():
        # unittest.TestCase().assertNotIsSubclass()
        unittest.TestCase().assertNotIsSubclass(
            # unittest.TestCase(), object
            # unittest.TestCase, object
            unittest.TestCase, dict
        )


    'assertNotIsSubclass'

  the test passes because the `unittest.TestCase class`_ is not a :ref:`subclass<how to test if something is a subclass>` of the :ref:`dict class (the class for dictionaries)<what is a dictionary?>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to compare it with the `assertNotIsSubclass method`_

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 3-5

    def test_assert_not_is_subclass():
        # unittest.TestCase().assertNotIsSubclass()
        assert not issubclass(
            unittest.TestCase, object
        )
        unittest.TestCase().assertNotIsSubclass(
            # unittest.TestCase(), object
            # unittest.TestCase, object
            unittest.TestCase, dict
        )


    'assertNotIsSubclass'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert not True

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 141
    :emphasize-lines: 4-5

    def test_assert_not_is_subclass():
        # unittest.TestCase().assertNotIsSubclass()
        assert not issubclass(
            # unittest.TestCase, object
            unittest.TestCase, list
        )
        unittest.TestCase().assertNotIsSubclass(
            # unittest.TestCase(), object
            # unittest.TestCase, object
            unittest.TestCase, dict
        )


    'assertNotIsSubclass'
    'assertIsSubclass'

  the test passes because the `unittest.TestCase class`_ is not a :ref:`subclass<how to test if something is a subclass>` of the :ref:`list class (the class for lists)<what is a list?>`.

* I remove assertNotIsSubclass_ from the TODO list

  .. code-block:: python
    :lineno-start: 147

        unittest.TestCase().assertNotIsSubclass(
            # unittest.TestCase(), object
            # unittest.TestCase, object
            unittest.TestCase, dict
        )


    'assertIsSubclass'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_not_is_subclass'

I imagine Python_ follows this path when `unittest.TestCase.assertNotIsSubclass`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertNotIsSubclass(self, cls, superclass):
          └── assert not issubclass(cls, superclass)

Compare the error message for ``unittest.TestCase().assertNotIsSubclass(unittest.TestCase, object)`` with the one for ``assert not issubclass(unittest.TestCase, object)``

.. code-block:: shell

  AssertionError:
      <class 'unittest.case.TestCase'>
      is a subclass of <class 'object'>

vs

.. code-block:: python

  AssertionError: assert not True

----

*********************************************************************************
test_assert_is_subclass
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for the `assertIsSubclass method`_

  .. code-block:: python
    :lineno-start: 147
    :emphasize-lines: 8-9

        unittest.TestCase().assertNotIsSubclass(
            # unittest.TestCase(), object
            # unittest.TestCase, object
            unittest.TestCase, dict
        )


    def test_assert_is_subclass():
        assert issubclass(unittest.TestCase(), set)


    'assertIsSubclass'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`instance<how to test if something is an instance>` to a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 2-3

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        assert issubclass(unittest.TestCase, set)


    'assertIsSubclass'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 3-4

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)


    'assertIsSubclass'

  the test passes.

* I add a call to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 5

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)
        unittest.TestCase.assertIsSubclass()


    'assertIsSubclass'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertIsSubclass()
               missing 3 required positional arguments:
               'self', 'cls', and 'superclass'

  - A :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.
  - ``cls`` is for the :ref:`subclass<how to test if something is a subclass>` being tested
  - ``superclass`` is for the :ref:`parent class<what is a class?>` of the :ref:`subclass<how to test if something is a subclass>` being tested.

* I change the :ref:`call<how to call a function with input>` to use :ref:`an instance<how to test if something is an instance>` instead of a :ref:`class<what is a class?>`, then add two things to the parentheses

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 5-8

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)
        # unittest.TestCase.assertIsSubclass()
        unittest.TestCase().assertIsSubclass(
            unittest.TestCase(), set
        )


    'assertIsSubclass'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError:
        <unittest.case.TestCase testMethod=runTest>
        is not a class

  because :ref:`an instance is not a class<instance vs subclass>`.

* I change the :ref:`instance<how to test if something is an instance>` to a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 7-8

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)
        # unittest.TestCase.assertIsSubclass()
        unittest.TestCase().assertIsSubclass(
            # unittest.TestCase(), set
            unittest.TestCase, set
        )


    'assertIsSubclass'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'unittest.case.TestCase'>
        is not a subclass of <class 'set'>

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 154
    :emphasize-lines: 8-9

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)
        # unittest.TestCase.assertIsSubclass()
        unittest.TestCase().assertIsSubclass(
            # unittest.TestCase(), set
            # unittest.TestCase, set
            unittest.TestCase, object
        )


    'assertIsSubclass'


    # Exceptions seen

  the test passes because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove assertIsSubclass_ from the TODO list

  .. code-block:: python
    :lineno-start: 154

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)
        # unittest.TestCase.assertIsSubclass()
        unittest.TestCase().assertIsSubclass(
            # unittest.TestCase(), set
            # unittest.TestCase, set
            unittest.TestCase, object
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_is_subclass'

I imagine Python_ follows this path when `unittest.TestCase.assertIsSubclass`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:
      └── def assertIsSubclass(self, cls, superclass):
          └── assert not issubclass(cls, superclass)

Compare the error message for ``unittest.TestCase().assertIsSubclass(unittest.TestCase, tuple)`` with the one for ``assert issubclass(unittest.TestCase, set)``

.. code-block:: shell

  AssertionError:
      <class 'unittest.case.TestCase'>
      is not a subclass of <class 'tuple'>

vs

.. code-block:: python

  AssertionError: assert False

Which of the error messages in this chapter do you like better?

----

*********************************************************************************
extract TOOLBOX variable
*********************************************************************************

I make an :ref:`instance<how to test if something is an instance>` of the `unittest.TestCase class`_ to use its `assert methods`_ in every test. I can use a :ref:`variable<what is a variable?>` to remove repetition of that process (``unittest.TestCase()``) from every test.

* I add a :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` at the top of the file_

  .. code-block:: python
    :linenos:

    import unittest


    TOOLBOX = unittest.TestCase()


    def test_attributes_and_methods_of_unittest():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 7-8

    def test_assert_is_not():
        # unittest.TestCase.assertIsNot()
        # unittest.TestCase().assertIsNot()
        # unittest.TestCase().assertIsNot(None, None)
        # assert None is not None
        assert None is not False
        # unittest.TestCase().assertIsNot(None, False)
        TOOLBOX.assertIsNot(None, False)


    def test_assert_is():

  the test is still green.

* I remove the commented lines from :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 81

    def test_assert_is_not():
        assert None is not False
        TOOLBOX.assertIsNot(None, False)


    def test_assert_is():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 7-8

    def test_assert_is():
        # assert False is True
        assert False is False
        # unittest.TestCase.assertIs()
        # unittest.TestCase().assertIs()
        # unittest.TestCase().assertIs(False, True)
        # unittest.TestCase().assertIs(False, False)
        TOOLBOX.assertIs(False, False)


    def test_assert_not_equal():

  still green.

* I remove the commented lines from :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 86

    def test_assert_is():
        assert False is False
        TOOLBOX.assertIs(False, False)


    def test_assert_not_equal():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 6-7

    def test_assert_not_equal():
        # unittest.TestCase().assertNotEqual()
        # unittest.TestCase().assertNotEqual(True, True)
        # assert True != True
        assert True != 0
        # unittest.TestCase().assertNotEqual(True, 0)
        TOOLBOX.assertNotEqual(True, 0)


    def test_assert_equal():

  green.

* I remove the commented lines from :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 91

    def test_assert_not_equal():
        assert True != 0
        TOOLBOX.assertNotEqual(True, 0)


    def test_assert_equal():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 5-6

    def test_assert_equal():
        # assert 0.0 == '0.0'
        assert 0.0 == 0.0
        # unittest.TestCase().assertEqual(0.0, '0.0')
        # unittest.TestCase().assertEqual(0.0, 0.0)
        TOOLBOX.assertEqual(0.0, 0.0)


    def test_assert_not_is_instance():

  still green.

* I remove the commented lines from :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 96

    def test_assert_equal():
        assert 0.0 == 0.0
        TOOLBOX.assertEqual(0.0, 0.0)


    def test_assert_not_is_instance():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 8-9

    def test_assert_not_is_instance():
        # unittest.TestCase.assertNotIsInstance()
        # unittest.TestCase().assertNotIsInstance()
        assert not isinstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )
        # unittest.TestCase().assertNotIsInstance(
        TOOLBOX.assertNotIsInstance(
            # unittest.TestCase(), unittest.TestCase
            unittest.TestCase, unittest.TestCase
        )


    def test_assert_is_instance():

  the test is still green.

* I remove the commented lines from :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 101

    def test_assert_not_is_instance():
        assert not isinstance(
            unittest.TestCase, unittest.TestCase
        )
        TOOLBOX.assertNotIsInstance(
            unittest.TestCase, unittest.TestCase
        )


    def test_assert_is_instance():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_is_instance`

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 11-12

    def test_assert_is_instance():
        a_class = unittest.TestCase
        an_instance = a_class()
        # unittest.TestCase.assertIsInstance()
        # unittest.TestCase().assertIsInstance()
        assert isinstance(
            # unittest.TestCase, unittest.TestCase
            # unittest.TestCase(), unittest.TestCase
            an_instance, a_class
        )
        # unittest.TestCase().assertIsInstance(
        TOOLBOX.assertIsInstance(
            # unittest.TestCase, unittest.TestCase
            # unittest.TestCase(), unittest.TestCase
            an_instance, a_class
        )


    def test_assert_not_is_subclass():

  still green.

* I remove the commented lines from :ref:`test_assert_is_instance`

  .. code-block:: python
    :lineno-start: 110

    def test_assert_is_instance():
        a_class = unittest.TestCase
        an_instance = a_class()

        assert isinstance(an_instance, a_class)
        TOOLBOX.assertIsInstance(
            an_instance, a_class
        )


    def test_assert_not_is_subclass():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 7-8

    def test_assert_not_is_subclass():
        # unittest.TestCase().assertNotIsSubclass()
        assert not issubclass(
            # unittest.TestCase, object
            unittest.TestCase, list
        )
        # unittest.TestCase().assertNotIsSubclass(
        TOOLBOX.assertNotIsSubclass(
            # unittest.TestCase(), object
            # unittest.TestCase, object
            unittest.TestCase, dict
        )


    def test_assert_is_subclass():

  green.

* I remove the commented lines from :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 120

    def test_assert_not_is_subclass():
        assert not issubclass(
            unittest.TestCase, list
        )
        TOOLBOX.assertNotIsSubclass(
            unittest.TestCase, dict
        )


    def test_assert_is_subclass():

* I use the :ref:`variable<what is a variable?>` for ``unittest.TestCase()`` in :ref:`test_assert_is_subclass`

  .. code-block:: python
    :lineno-start: 129
    :emphasize-lines: 6-7

    def test_assert_is_subclass():
        # assert issubclass(unittest.TestCase(), set)
        # assert issubclass(unittest.TestCase, set)
        assert issubclass(unittest.TestCase, object)
        # unittest.TestCase.assertIsSubclass()
        # unittest.TestCase().assertIsSubclass(
        TOOLBOX.assertIsSubclass(
            # unittest.TestCase(), set
            # unittest.TestCase, set
            unittest.TestCase, object
        )


    # Exceptions seen

  still green.

* I remove the commented lines from :ref:`test_assert_is_subclass`

  .. code-block:: python
    :lineno-start: 129

    def test_assert_is_subclass():
        assert issubclass(unittest.TestCase, object)
        TOOLBOX.assertIsSubclass(
            unittest.TestCase, object
        )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract TOOLBOX variable'


The ``unittest.TestCase()`` :ref:`instance<how to test if something is an instance>` is now made once then used in every test for its `assert methods`_.

The problem with this solution is that anyone reading it has to know what the ``TOOLBOX`` :ref:`variable<what is a variable?>` points to at the beginning of the file_ to understand why the :ref:`calls<how to call a function with input>` work.

----

*********************************************************************************
extract TestUnittest class
*********************************************************************************

I can put the test :ref:`functions<what is a function?>` together in a :ref:`class<what is a class?>` since they are related.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a :ref:`class<what is a class?>` named ``Unittest``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4, 6-7

    TOOLBOX = unittest.TestCase()


    class Unittest(object):

        def test_failure():
            TOOLBOX.assertEqual(True, False)


    def test_attributes_and_methods_of_unittest():

  this is a problem. I expect ``TOOLBOX.assertEqual(True, False)`` to fail since :ref:`True<test_what_is_true>` is not equal to :ref:`False<test_what_is_false>`

* I add ``Test`` to the name of the :ref:`class<what is a class?>`

  .. code-block::
    :lineno-start: 4
    :emphasize-lines: 4-5

    TOOLBOX = unittest.TestCase()


    # class Unittest(object):
    class TestUnittest(object):

        def test_failure():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestUnittest.test_failure() takes 0
               positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to ``test_failure`` since I can use it if I do not want to add ``self`` to the :ref:`method definition<how to make a function>`. This way I do not send more information than what the :ref:`method<what is a method?>` needs when it does not use anything in the :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

    # class Unittest(object):
    class TestUnittest(object):

        @staticmethod
        def test_failure():
            TOOLBOX.assertEqual(True, False)


    def test_attributes_and_methods_of_unittest():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

    # class Unittest(object):
    class TestUnittest(object):

        @staticmethod
        def test_failure():
            # TOOLBOX.assertEqual(True, False)
            TOOLBOX.assertEqual(True, True)


    def test_attributes_and_methods_of_unittest():


  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I move :ref:`test_attributes_and_methods_of_unittest` to replace ``test_failure`` As a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-23

    # class Unittest(object):
    class TestUnittest(object):

        def test_attributes_and_methods_of_unittest():
            reality = dir(unittest)
            my_expectation = [
                'BaseTestSuite', 'FunctionTestCase',
                'IsolatedAsyncioTestCase', 'SkipTest',
                ...

  .. caution:: Indentation matters in Python_. It is how it knows what blocks belong to what :ref:`function/method<what is a function?>`, :ref:`class<what is a class?>` or :ref:`module<what is a module?>` (Use 4 spaces)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_attributes_and_methods_of_unittest()
        takes 0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_attributes_and_methods_of_unittest`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

    # class Unittest(object):
    class TestUnittest(object):

        @staticmethod
        def test_attributes_and_methods_of_unittest():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the `assertNotEqual method`_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

            assert reality == my_expectation
            TOOLBOX.assertNotEqual(reality, my_expectation)


    def test_attributes_and_methods_of_unittest_testcase():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change assertNotEqual_ to assertEqual_

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # TOOLBOX.assertNotEqual(reality, my_expectation)
            TOOLBOX.assertEqual(reality, my_expectation)


    def test_attributes_and_methods_of_unittest_testcase():

  the test passes.

* I move :ref:`test_attributes_and_methods_of_unittest_testcase` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-50

            TOOLBOX.assertEqual(reality, my_expectation)

        def test_attributes_and_methods_of_unittest_testcase():
            reality = dir(unittest.TestCase)
            my_expectation = [
                '__call__', '__class__', '__delattr__',
                ...

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_attributes_and_methods_of_unittest_testcase()
        takes 0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_attributes_and_methods_of_unittest_testcase`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3

            TOOLBOX.assertEqual(reality, my_expectation)

        @staticmethod
        def test_attributes_and_methods_of_unittest_testcase():

  the test passes.

* I add a :ref:`call<how to call a function with input>` to the `assertNotEqual method`_

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2

            assert reality == my_expectation
            TOOLBOX.assertNotEqual(reality, my_expectation)


    def test_assert_is_not():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`.

* I change assertNotEqual_ to assertEqual_

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 2-3

            assert reality == my_expectation
            # TOOLBOX.assertNotEqual(reality, my_expectation)
            TOOLBOX.assertEqual(reality, my_expectation)


    def test_assert_is_not():

  the test passes.

* I indent (move with four spaces) :ref:`test_assert_is_not` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3-5

            TOOLBOX.assertEqual(reality, my_expectation)

        def test_assert_is_not():
            assert None is not False
            TOOLBOX.assertIsNot(None, False)


    def test_assert_is():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_is_not()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 3

            TOOLBOX.assertEqual(reality, my_expectation)

        @staticmethod
        def test_assert_is_not():

  the test passes.

* I move :ref:`test_assert_is` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3-5

            TOOLBOX.assertIsNot(None, False)

        def test_assert_is():
            assert False is False
            TOOLBOX.assertIs(False, False)


    def test_assert_not_equal():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_is()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 3

            TOOLBOX.assertIsNot(None, False)

        @staticmethod
        def test_assert_is():

  the test passes.

* I indent :ref:`test_assert_not_equal` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3-5

            TOOLBOX.assertIs(False, False)

        def test_assert_not_equal():
            assert True != 0
            TOOLBOX.assertNotEqual(True, 0)


    def test_assert_equal():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_not_equal()
        takes 0 positional arguments but 1 was given

  because ...

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3

            TOOLBOX.assertIs(False, False)

        @staticmethod
        def test_assert_not_equal():

  the test passes.

* I move :ref:`test_assert_equal` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3-5

            TOOLBOX.assertNotEqual(True, 0)

        def test_assert_equal():
            assert 0.0 == 0.0
            TOOLBOX.assertEqual(0.0, 0.0)


    def test_assert_not_is_instance():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_equal()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3

            TOOLBOX.assertNotEqual(True, 0)

        @staticmethod
        def test_assert_equal():

  the test passes.

* I move :ref:`test_assert_not_is_instance` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3-9

            TOOLBOX.assertEqual(0.0, 0.0)

        def test_assert_not_is_instance():
            assert not isinstance(
                unittest.TestCase, unittest.TestCase
            )
            TOOLBOX.assertNotIsInstance(
                unittest.TestCase, unittest.TestCase
            )


    def test_assert_is_instance():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_not_is_instance()
        takes 0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3

            TOOLBOX.assertEqual(0.0, 0.0)

        @staticmethod
        def test_assert_not_is_instance():

  the test passes.

* I move :ref:`test_assert_is_instance` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 6-7, 9-12

            TOOLBOX.assertNotIsInstance(
                unittest.TestCase, unittest.TestCase
            )

        def test_assert_is_instance():
            a_class = unittest.TestCase
            an_instance = a_class()

            assert isinstance(an_instance, a_class)
            TOOLBOX.assertIsInstance(
                an_instance, a_class
            )


    def test_assert_not_is_subclass():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_is_instance()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_is_instance`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5

            TOOLBOX.assertNotIsInstance(
                unittest.TestCase, unittest.TestCase
            )

        @staticmethod
        def test_assert_is_instance():

  the test passes.

* I move :ref:`test_assert_not_is_subclass` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 5-12

            TOOLBOX.assertIsInstance(
                an_instance, a_class
            )

        def test_assert_not_is_subclass():
            assert not issubclass(
                unittest.TestCase, list
            )
            TOOLBOX.assertNotIsSubclass(
                unittest.TestCase, dict
            )


    def test_assert_is_subclass():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_not_is_subclass()
        takes 0 positional arguments but 1 was given

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5

            TOOLBOX.assertIsInstance(
                an_instance, a_class
            )

        @staticmethod
        def test_assert_not_is_subclass():

  the test passes.

* I move :ref:`test_assert_is_subclass` to make it a :ref:`method<what is a method?>` of the :ref:`TestUnittest class<extract TestUnittest class>`

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 5-9

            TOOLBOX.assertNotIsSubclass(
                unittest.TestCase, dict
            )

        def test_assert_is_subclass():
            assert issubclass(unittest.TestCase, object)
            TOOLBOX.assertIsSubclass(
                unittest.TestCase, object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError:
        TestUnittest.test_assert_is_subclass()
        takes 0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to :ref:`test_assert_is_subclass`

  .. code-block:: python
    :lineno-start: 132
    :emphasize-lines: 5

            TOOLBOX.assertNotIsSubclass(
                unittest.TestCase, dict
            )

        @staticmethod
        def test_assert_is_subclass():

  the test passes.

----

* I add the ``TOOLBOX`` :ref:`variable<what is a variable?>` to :ref:`TestUnittest<extract TestUnittest class>` to make it a :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

    # class Unittest(object):
    class TestUnittest(object):

        TOOLBOX = unittest.TestCase()

        @staticmethod
        def test_attributes_and_methods_of_unittest():

* I use the new :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_attributes_and_methods_of_unittest`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4

            assert reality == my_expectation
            # TOOLBOX.assertNotEqual(reality, my_expectation)
            # TOOLBOX.assertEqual(reality, my_expectation)
            self.TOOLBOX.assertEqual(reality, my_expectation)

        @staticmethod
        def test_attributes_and_methods_of_unittest_testcase():

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses of :ref:`test_attributes_and_methods_of_unittest`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7-8

    # class Unittest(object):
    class TestUnittest(object):

        TOOLBOX = unittest.TestCase()

        @staticmethod
        # def test_attributes_and_methods_of_unittest():
        def test_attributes_and_methods_of_unittest(self):

  the terminal_ is my friend, and shows

  .. code-block:: python

    E       fixture 'self' not found

* I remove the :ref:`staticmethod decorator<what is the staticmethod decorator?>` since I am using ``self`` in the :ref:`test_attributes_and_methods_of_unittest`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

    # class Unittest(object):
    class TestUnittest(object):

        TOOLBOX = unittest.TestCase()

        # @staticmethod
        # def test_attributes_and_methods_of_unittest():
        def test_attributes_and_methods_of_unittest(self):
            reality = dir(unittest)

  the test is green again.

* I use the new :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_attributes_and_methods_of_unittest_testcase`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4

            assert reality == my_expectation
            # TOOLBOX.assertNotEqual(reality, my_expectation)
            # TOOLBOX.assertEqual(reality, my_expectation)
            self.TOOLBOX.assertEqual(reality, my_expectation)

        @staticmethod
        def test_assert_is_not():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_attributes_and_methods_of_unittest_testcase`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-5

            self.TOOLBOX.assertEqual(reality, my_expectation)

        # @staticmethod
        # def test_attributes_and_methods_of_unittest_testcase():
        def test_attributes_and_methods_of_unittest_testcase(self):
            reality = dir(unittest.TestCase)

  green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 4-5

        @staticmethod
        def test_assert_is_not():
            assert None is not False
            # TOOLBOX.assertIsNot(None, False)
            self.TOOLBOX.assertIsNot(None, False)

        @staticmethod
        def test_assert_is():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_is_not():
        def test_assert_is_not(self):

  the test is green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 4-5

        @staticmethod
        def test_assert_is():
            assert False is False
            # TOOLBOX.assertIs(False, False)
            self.TOOLBOX.assertIs(False, False)

        @staticmethod
        def test_assert_not_equal():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_is():
        def test_assert_is(self):

  green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 4-5

        @staticmethod
        def test_assert_not_equal():
            assert True != 0
            # TOOLBOX.assertNotEqual(True, 0)
            self.TOOLBOX.assertNotEqual(True, 0)

        @staticmethod
        def test_assert_equal():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_not_equal():
        def test_assert_not_equal(self):

  the test is green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 4-5

        @staticmethod
        def test_assert_equal():
            assert 0.0 == 0.0
            # TOOLBOX.assertEqual(0.0, 0.0)
            self.TOOLBOX.assertEqual(0.0, 0.0)

        @staticmethod
        def test_assert_not_is_instance():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_equal():
        def test_assert_equal(self):

  green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 6-7

        @staticmethod
        def test_assert_not_is_instance():
            assert not isinstance(
                unittest.TestCase, unittest.TestCase
            )
            # TOOLBOX.assertNotIsInstance(
            self.TOOLBOX.assertNotIsInstance(
                unittest.TestCase, unittest.TestCase
            )

        @staticmethod
        def test_assert_is_instance():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_not_is_instance():
        def test_assert_not_is_instance(self):

  the test is green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_is_instance`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7-8

        @staticmethod
        def test_assert_is_instance():
            a_class = unittest.TestCase
            an_instance = a_class()

            assert isinstance(an_instance, a_class)
            # TOOLBOX.assertIsInstance(
            self.TOOLBOX.assertIsInstance(
                an_instance, a_class
            )

        @staticmethod
        def test_assert_not_is_subclass():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_is_instance`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_is_instance():
        def test_assert_is_instance(self):

  the test is green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 6-7

        @staticmethod
        def test_assert_not_is_subclass():
            assert not issubclass(
                unittest.TestCase, list
            )
            # TOOLBOX.assertNotIsSubclass(
            self.TOOLBOX.assertNotIsSubclass(
                unittest.TestCase, dict
            )

        @staticmethod
        def test_assert_is_subclass():

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 145
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_not_is_subclass():
        def test_assert_not_is_subclass(self):

  the test is green again.

* I use the :ref:`class attribute<what is a class attribute?>` for ``TOOLBOX`` in :ref:`test_assert_is_subclass`

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 4-5

        @staticmethod
        def test_assert_is_subclass():
            assert issubclass(unittest.TestCase, object)
            # TOOLBOX.assertIsSubclass(
            self.TOOLBOX.assertIsSubclass(
                unittest.TestCase, object
            )


    # Exceptions seen

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses and comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>` for :ref:`test_assert_is_subclass`

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 1-3

        # @staticmethod
        # def test_assert_is_subclass():
        def test_assert_is_subclass(self):

  the test is green again.

* I remove the ``TOOLBOX`` :ref:`variable<what is a variable?>` because it is no longer used

  .. code-block:: python
    :linenos:

    import unittest


    # class Unittest(object):
    class TestUnittest(object):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract TestUnittest class'

----

*********************************************************************************
use unittest.TestCase
*********************************************************************************

I can use the `unittest.TestCase class`_ as a parent of the :ref:`TestUnittest class<extract TestUnittest class>` which will allow me to use ``self`` to access its :ref:`attributes and methods<test_attributes_and_methods_of_unittest_testcase>`.

It also means I will not need the ``TOOLBOX`` :ref:`class attribute<what is a class attribute?>` which points to an :ref:`instance<how to test if something is an instance>` of the `unittest.TestCase class`_.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.

* I change the :ref:`call<how to call a function with input>` to the `assertEqual method`_ in :ref:`test_attributes_and_methods_of_unittest`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4-5

            assert reality == my_expectation
            # TOOLBOX.assertNotEqual(reality, my_expectation)
            # TOOLBOX.assertEqual(reality, my_expectation)
            # self.TOOLBOX.assertEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

        # @staticmethod
        # def test_attributes_and_methods_of_unittest_testcase():
        def test_attributes_and_methods_of_unittest_testcase(self):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'TestUnittest' object
                    has no attribute 'assertEqual'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 165
    :emphasize-lines: 5
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add `unittest.TestCase`_ as the parent of the :ref:`TestUnittest class<extract TestUnittest class>` so that it can :ref:`have all the attributes and methods<everything is an object>` of `unittest.TestCase`_

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 2-3

  # class Unittest(object):
  # class TestUnittest(object):
  class TestUnittest(unittest.TestCase):

      TOOLBOX = unittest.TestCase()

      # @staticmethod
      # def test_attributes_and_methods_of_unittest():
      def test_attributes_and_methods_of_unittest(self):
          reality = dir(unittest)

the test passes because

* :ref:`TestUnittest<extract TestUnittest class>` is now a :ref:`subclass (child)<how to test if something is a subclass>` of the `unittest.TestCase class`_.
* :ref:`children inherit the attributes and methods of their parents<everything is an object>`.
* ``self`` is :ref:`TestUnittest()<extract TestUnittest class>` inside :ref:`TestUnittest<extract TestUnittest class>`.
* ``self`` has all the :ref:`attributes and methods of unittest.TestCase<test_attributes_and_methods_of_unittest_testcase>` because `unittest.TestCase`_ is the :ref:`parent class<what is a class?>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_attributes_and_methods_of_unittest` and :ref:`TestUnittest<extract TestUnittest class>`

  .. code-block:: python
    :linenos:

    import unittest


    class TestUnittest(unittest.TestCase):

        TOOLBOX = unittest.TestCase()

        def test_attributes_and_methods_of_unittest(self):
            reality = dir(unittest)
            my_expectation = [

  .. code-block:: python
    :lineno-start: 26

            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        # @staticmethod
        # def test_attributes_and_methods_of_unittest_testcase():
        def test_attributes_and_methods_of_unittest_testcase(self):

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_assert_is_subclass` to show that :ref:`TestUnittest<extract TestUnittest class>` is a :ref:`subclass<how to test if something is a subclass>` of the `unittest.TestCase class`_

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 10-12

        # @staticmethod
        # def test_assert_is_subclass():
        def test_assert_is_subclass(self):
            assert issubclass(unittest.TestCase, object)
            # TOOLBOX.assertIsSubclass(
            self.TOOLBOX.assertIsSubclass(
                unittest.TestCase, object
            )
            self.assertNotIsSubclass(
                TestUnittest, unittest.TestCase
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'tests.test_unittest.TestUnittest'>
        is a subclass of
        <class 'unittest.case.TestCase'>

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 9-10

        # @staticmethod
        # def test_assert_is_subclass():
        def test_assert_is_subclass(self):
            assert issubclass(unittest.TestCase, object)
            # TOOLBOX.assertIsSubclass(
            self.TOOLBOX.assertIsSubclass(
                unittest.TestCase, object
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                TestUnittest, unittest.TestCase
            )


    # Exceptions seen

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``self.TOOLBOX.assertIsSubclass``

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 6-7

        # @staticmethod
        # def test_assert_is_subclass():
        def test_assert_is_subclass(self):
            assert issubclass(unittest.TestCase, object)
            # TOOLBOX.assertIsSubclass(
            # self.TOOLBOX.assertIsSubclass(
            self.assertIsSubclass(
                unittest.TestCase, object
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                TestUnittest, unittest.TestCase
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_assert_is_subclass`

  .. code-block:: python
    :lineno-start: 148

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

* I change the :ref:`call<how to call a function with input>` to the `assertNotIsSubclass method`_ in :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 8-9

        # @staticmethod
        # def test_assert_not_is_subclass():
        def test_assert_not_is_subclass(self):
            assert not issubclass(
                unittest.TestCase, list
            )
            # TOOLBOX.assertNotIsSubclass(
            # self.TOOLBOX.assertNotIsSubclass(
            self.assertNotIsSubclass(
                unittest.TestCase, dict
            )

        def test_assert_is_subclass(self):

  still green.

* I remove the commented lines from :ref:`test_assert_not_is_subclass`

  .. code-block:: python
    :lineno-start: 137

        def test_assert_not_is_subclass(self):
            assert not issubclass(
                unittest.TestCase, list
            )
            self.assertNotIsSubclass(
                unittest.TestCase, dict
            )

        def test_assert_is_subclass(self):

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_assert_is_instance` to show that ``self`` in the :ref:`TestUnittest class<extract TestUnittest class>` is an :ref:`instance<how to test if something is an instance>` of the `unittest.TestCase class`_

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 13-15

        # @staticmethod
        # def test_assert_is_instance():
        def test_assert_is_instance(self):
            a_class = unittest.TestCase
            an_instance = a_class()

            assert isinstance(an_instance, a_class)
            # TOOLBOX.assertIsInstance(
            # self.TOOLBOX.assertIsInstance(
            self.TOOLBOX.assertIsInstance(
                an_instance, a_class
            )
            self.assertNotIsInstance(
                self, unittest.TestCase
            )

        def test_assert_not_is_subclass(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <
            tests.test_unittest.TestUnittest
            testMethod=test_assert_is_instance
        > is an instance of
        <class 'unittest.case.TestCase'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 13-14

        # @staticmethod
        # def test_assert_is_instance():
        def test_assert_is_instance(self):
            a_class = unittest.TestCase
            an_instance = a_class()

            assert isinstance(an_instance, a_class)
            # TOOLBOX.assertIsInstance(
            # self.TOOLBOX.assertIsInstance(
            self.TOOLBOX.assertIsInstance(
                an_instance, a_class
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                self, unittest.TestCase
            )

        def test_assert_not_is_subclass(self):

  the test passes.

* I change the :ref:`call<how to call a function with input>` to ``self.TOOLBOX.assertIsInstance``

  .. code-block:: python
    :lineno-start: 125
    :emphasize-lines: 10-11

    # @staticmethod
        # def test_assert_is_instance():
        def test_assert_is_instance(self):
            a_class = unittest.TestCase
            an_instance = a_class()

            assert isinstance(an_instance, a_class)
            # TOOLBOX.assertIsInstance(
            # self.TOOLBOX.assertIsInstance(
            # self.TOOLBOX.assertIsInstance(
            self.assertIsInstance(
                an_instance, a_class
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                self, unittest.TestCase
            )

        def test_assert_not_is_subclass(self):

* I remove the commented lines from :ref:`test_assert_is_instance`

  .. code-block:: python
    :lineno-start: 125

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

* I change the :ref:`call<how to call a function with input>` to the `assertNotIsInstance method`_ in :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 114
    :emphasize-lines: 8-9

        # @staticmethod
        # def test_assert_not_is_instance():
        def test_assert_not_is_instance(self):
            assert not isinstance(
                unittest.TestCase, unittest.TestCase
            )
            # TOOLBOX.assertNotIsInstance(
            # self.TOOLBOX.assertNotIsInstance(
            self.assertNotIsInstance(
                unittest.TestCase, unittest.TestCase
            )

        def test_assert_is_instance(self):

  the test is still green.

* I remove the commented lines from :ref:`test_assert_not_is_instance`

  .. code-block:: python
    :lineno-start: 114

        def test_assert_not_is_instance(self):
            assert not isinstance(
                unittest.TestCase, unittest.TestCase
            )
            self.assertNotIsInstance(
                unittest.TestCase, unittest.TestCase
            )

        def test_assert_is_instance(self):

* I change the :ref:`call<how to call a function with input>` to assertEqual in :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 6-7

        # @staticmethod
        # def test_assert_equal():
        def test_assert_equal(self):
            assert 0.0 == 0.0
            # TOOLBOX.assertEqual(0.0, 0.0)
            # self.TOOLBOX.assertEqual(0.0, 0.0)
            self.assertEqual(0.0, 0.0)

        def test_assert_not_is_instance(self):

  still green.

* I remove the commented lines from :ref:`test_assert_equal`

  .. code-block:: python
    :lineno-start: 107

        def test_assert_equal(self):
            assert 0.0 == 0.0
            self.assertEqual(0.0, 0.0)

        def test_assert_not_is_instance(self):

* I change the :ref:`call<how to call a function with input>` to the `assertNotEqual method`_ in :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 6-7

        # @staticmethod
        # def test_assert_not_equal():
        def test_assert_not_equal(self):
            assert True != 0
            # TOOLBOX.assertNotEqual(True, 0)
            # self.TOOLBOX.assertNotEqual(True, 0)
            self.assertNotEqual(True, 0)

        def test_assert_equal(self):

  still green.

* I remove the commented lines from :ref:`test_assert_not_equal`

  .. code-block:: python
    :lineno-start: 100

        def test_assert_not_equal(self):
            assert True != 0
            self.assertNotEqual(True, 0)

        def test_assert_equal(self):

* I change the :ref:`call<how to call a function with input>` to the `assertIs method`_ in :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 6-7

        # @staticmethod
        # def test_assert_is():
        def test_assert_is(self):
            assert False is False
            # TOOLBOX.assertIs(False, False)
            # self.TOOLBOX.assertIs(False, False)
            self.assertIs(False, False)

        def test_assert_not_equal(self):

  green.

* I remove the commented lines from :ref:`test_assert_is`

  .. code-block:: python
    :lineno-start: 93

        def test_assert_is(self):
            assert False is False
            self.assertIs(False, False)

        def test_assert_not_equal(self):

* I change the :ref:`call<how to call a function with input>` to the `assertIsNot method`_ in :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 6-7

        # @staticmethod
        # def test_assert_is_not():
        def test_assert_is_not(self):
            assert None is not False
            # TOOLBOX.assertIsNot(None, False)
            # self.TOOLBOX.assertIsNot(None, False)
            self.assertIsNot(None, False)

        def test_assert_is(self):

  the test is still green.

* I remove the commented lines from :ref:`test_assert_is_not`

  .. code-block:: python
    :lineno-start: 86

        def test_assert_is_not(self):
            assert None is not False
            self.assertIsNot(None, False)

        def test_assert_is(self):

* I change the :ref:`call<how to call a function with input>` to the `assertEqual method`_ in :ref:`test_attributes_and_methods_of_unittest_testcase`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 4-5

            assert reality == my_expectation
            # TOOLBOX.assertNotEqual(reality, my_expectation)
            # TOOLBOX.assertEqual(reality, my_expectation)
            # self.TOOLBOX.assertEqual(reality, my_expectation)
            self.assertEqual(reality, my_expectation)

        def test_assert_is_not(self):

  the test is still green.

* I remove the commented lines from :ref:`test_attributes_and_methods_of_unittest_testcase`

  .. code-block:: python
    :lineno-start: 27

            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_attributes_and_methods_of_unittest_testcase(self):
            reality = dir(unittest.TestCase)
            my_expectation = [

  .. code-block:: python
    :lineno-start: 78

            ]
            assert reality == my_expectation
            self.assertEqual(reality, my_expectation)

        def test_assert_is_not(self):

* I remove the ``TOOLBOX`` :ref:`class attribute<what is a class attribute?>` since it is no longer used

  .. code-block:: python
    :lineno-start: 4

    class TestUnittest(unittest.TestCase):

        def test_attributes_and_methods_of_unittest(self):

  all the tests are still passing.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'use unittest.TestCase'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_unittest.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``unittest``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I can write tests with the `unittest.TestCase class`_ which comes with `assert methods`_ I can use in place of basic :ref:`assert statements<what is an assertion?>`:

* :ref:`assertIsNot<test_assert_is_not>`
* :ref:`assertIs<test_assert_is>`
* :ref:`assertNotEqual<test_assert_not_equal>`
* :ref:`assertEqual<test_assert_equal>`
* :ref:`assertNotIsInstance<test_assert_not_is_instance>`
* :ref:`assertIsInstance<test_assert_is_instance>`
* :ref:`assertNotIsSubclass<test_assert_not_is_subclass>`
* :ref:`assertIsSubclass<test_assert_is_subclass>`


:ref:`How many questions can you answer about unittest?<questions about unittest>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

* :ref:`Do you want to see all the CODE I typed in this chapter?<another way to write tests: tests>`
* `click here to see the source code for unittest`_

----

*************************************************************************************
what is next?
*************************************************************************************

You now know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError?`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hi with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal functions>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`
* :ref:`how to use the unittest library<another way to write tests>`

:ref:`Would you like to use unittest with the assertion_error project?<AssertionError: use unittest>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->