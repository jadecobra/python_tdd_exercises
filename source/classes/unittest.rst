.. meta::
  :description: Step-by-step Python TDD tutorial for beginners explaining why everything in Python inherits from the base 'object' class. Learn how to use isinstance() and issubclass() in unittest, and understand the difference between subunittest and instances. Verify that None, bool, int, float, str, tuple, list, set, and dict are all children of object. Learn to inspect built-in unittest with dir(object) and understand the inherited dunder methods. Resolve common beginner bugs: TypeError: issubclass() arg 1 must be a class, NameError: name 'src' is not defined, AttributeError: module has no attribute, and NameError: name 'E' is not defined.
  :keywords: Jacob Itegboje, Pumping Python, python inheritance tutorial for beginners, everything in python is an object, why does all python unittest inherit from object, is None an instance of object, is bool a subclass of object python, is int a subclass of object python, is float a subclass of object python, is str a subclass of object python, is list a subclass of object python, is tuple a subclass of object python, is set a subclass of object python, is dict a subclass of object python, difference between subclass and instance python, python isinstance vs issubclass tutorial, unittest assertIsInstance, unittest assertNotIsInstance, unittest assertIsSubclass, unittest assertNotIsSubclass, how to use dir on object class python, dunder methods of object class python, python object __init__ dunder, python object __str__ dunder, python object __repr__ dunder, TypeError issubclass arg 1 must be a class, NameError name src is not defined, AttributeError module unittest has no attribute, AssertionError assert not True, NameError name E is not defined pytest, python test driven development unittest object, class vs instance parentheses python, learning python dunder class doc init repr str

.. include:: ../links.rst

.. _isinstance: https://docs.python.org/3/library/functions.html#isinstance
.. _isinstance built-in function: isinstance_
.. _assertNotIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance
.. _unittest.TestCase.assertNotIsInstance: assertNotIsInstance_
.. _assertNotIsInstance method: assertNotIsInstance_
.. _assertIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance
.. _unittest.TestCase.assertIsInstance: assertIsInstance_
.. _assertIsInstance method: assertIsInstance_
.. _issubclass: https://docs.python.org/3/library/functions.html#issubclass
.. _issubclass built-in function: issubclass_
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
.. _TestCase class: `unittest.TestCase`_

#################################################################################
another way to write tests
#################################################################################

I used unittest_ in :ref:`how to make a Python test driven development environment manually` yp run tests manually before I learned to :ref:`run them automatically<how to run tests automatically>` with `pytest-watcher`_.

The unittest_ :ref:`library<what is a module?>` is part of `The Python Standard Library`_ and can also be used to write tests. You can think of it as a toolbox with different tools I can use to test code.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_unittest.py
  :language: python
  :linenos:

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

* I change ``test_failure`` to :ref:`test_attributes_and_methods_of_unittest` in ``test_classes.py``

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
        assert ['BaseTestSui...tLoader', ...] == []
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

* I open a new terminal_ then make sure I am in ``classes`` folder_

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

  E       AssertionError:
      assert ['__call__', ...__doc__', ...] == []
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
  assertNotIsSubClass_  ``assert not issubclass(X, Y)``
  assertIsSubClass_     ``assert issubclass(X, Y)``
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

  - because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance of a class>` takes the :ref:`instance of the class<how to test if something is an instance of a class>` (``self``) it belongs to as the first argument.
  - The :ref:`definition<how to make a function that takes input>` of the `assertIsNot method`_  of the `TestCase class`_  of the unittest_ library (``unittest.TestCase.assertIsNot``) has two required :ref:`positional arguments<test_positional_arguments>`. I imagine Python_ follows this path when `unittest.TestCase.assertIsNot`_ is called

    .. code-block:: shell

      unittest
      └── class TestCase:

              def assertIsNot(self, expr1, expr2):
                  return something

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

* I change the call to use :ref:`an instance<how to test if something is an instance of a class>` instead of a :ref:`class<what is a class?>`

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

  I no longer need to provide ``self`` because it is the :ref:`instance of the class<how to test if something is an instance of a class>` (``unittest.TestCase()``)

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

* I remove the commented lines and assertIsNot_ from the TODO list

  .. code-block:: python
    :lineno-start: 78

    def test_assert_is_not():
        assert None is not False
        unittest.TestCase().assertIsNot(None, False)


    'assertIs'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_is_not'

I imagine Python_ follows this path when `unittest.TestCase.assertIsNot`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:

          def assertIsNot(self, expr1, expr2):
              assert expr1 is not expr2

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
    :emphasize-lines: 6-7

    def test_assert_is_not():
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
  :lineno-start: 83
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
    :lineno-start: 83
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

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance of a class>` takes the :ref:`instance of the class<how to test if something is an instance of a class>` (``self``) it belongs to as the first argument.

* I change the call to use :ref:`an instance<how to test if something is an instance of a class>` instead of a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 83
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

  I no longer need to provide ``self`` because it is the :ref:`instance of the class<how to test if something is an instance of a class>` (``unittest.TestCase()``)

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertIs`_

  .. code-block:: python
    :lineno-start: 83
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
    :lineno-start: 83
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

* I remove the commented lines and assertIs_ from the TODO list

  .. code-block:: python
    :lineno-start: 83

    def test_assert_is():
        assert False is False
        unittest.TestCase().assertIs(False, False)


    'assertNotEqual'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_is'

I imagine Python_ follows this path when `unittest.TestCase.assertIs`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:

          def assertIs(self, expr1, expr2):
              assert expr1 is expr2

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
    :lineno-start: 83
    :emphasize-lines: 6-7

    def test_assert_is():
        assert False is False
        unittest.TestCase().assertIs(False, False)


    def test_assert_not_equal():
        unittest.TestCase().assertNotEqual()


    'assertNotEqual'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: TestCase.assertNotEqual() missing
               2 required positional arguments:
               'first', and 'second'

  the :ref:`definition<how to make a function that takes input>` of the `assertNotEqual method`_  of the `TestCase class`_  of the unittest_ library (``unittest.TestCase.assertNotEqual``) has two required :ref:`positional arguments<test_positional_arguments>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add two things to the :ref:`call<how to call a function with input>` to `unittest.TestCase.assertNotEqual`_

  .. code-block:: python
    :lineno-start: 88
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
    :lineno-start: 88
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
    :lineno-start: 88
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
    :lineno-start: 88
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

* I remove the commented lines and assertNotEqual_ from the TODO list

  .. code-block:: python
    :lineno-start: 88

    def test_assert_not_equal():
        assert True != 0
        unittest.TestCase().assertNotEqual(True, 0)


    'assertEqual'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_assert_not_equal'

I imagine Python_ follows this path when `unittest.TestCase.assertNotEqual`_ is called

.. code-block:: shell

  unittest
  └── class TestCase:

          def assertNotEqual(self, first, second):
              assert first != second

Compare the error message for ``assertNotEqual(None, None)`` with the one for ``assert None is not None``

.. code-block:: python

  AssertionError: unexpectedly identical: None

vs

.. code-block:: python

  assert None is not None


----

*********************************************************************************
review
*********************************************************************************

I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`
* :ref:`object<test_making_a_class_w_object>`

Everything in Python_ is an :ref:`object<everything is an object>`

* :ref:`None is an object<test_is_none_an_object>`
* :ref:`A boolean is an object<test_is_a_boolean_an_object>`
* :ref:`An integer is an object<test_is_an_integer_an_object>`
* :ref:`A float is an object<test_is_a_float_an_object>`
* :ref:`A string is an object<test_is_a_string_an_object>`
* :ref:`A tuple is an object<test_is_a_tuple_an_object>`
* :ref:`A list is an object<test_is_a_list_an_object>`
* :ref:`A set is an object<test_is_a_set_an_object>`
* :ref:`A dictionary is an object<test_is_a_dictionary_an_object>`
* :ref:`An instance is NOT a subclass<instance vs subclass>`

:ref:`How many questions can you answer about unittest?<questions about unittest>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_unittest.py`` and ``unittest.py`` in the :ref:`editor(s)<2 editors>`
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

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<unittest: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
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

:ref:`Would you like to use class attributes to remove repetition from the assertion_error project?<AssertionError 2: use class attributes>`

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