.. orphan::

.. meta::
  :description: Build a safety-critical elevator logic system in Python using truth tables and TDD. This beginner tutorial teaches how to manage multiple boolean inputs—door status, timers, and too_hot failsafes—while writing clean, verified code.
  :doorswords: Python elevator logic project, safety-critical systems python tutorial, TDD python elevator example, how to code a elevator in python, python multiple boolean inputs tutorial, red green refactor examples, python truth table practice, learn Converse NonImplication python, uv python project management, pytest-watcher logic testing, Jacob Itegboje

.. include:: ../../links.rst

.. _elevator:

#################################################################################
Elevator
#################################################################################

I want to make an **Elevator** that goes up and down when I push a button, if the inputs are

* are the doors clear?
* was the number for a floor pushed?

this is the :ref:`truth table` I get for the Elevator Starter

================  ==================  =================
doors             floor number        output
================  ==================  =================
:green:`clear`    :green:`pressed`    :green:`ON`
:green:`clear`    :red:`NOT pressed`  :red:`OFF`
:red:`NOT clear`  :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :red:`NOT pressed`  :red:`OFF`
================  ==================  =================

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_elevator.py
  :language: python
  :linenos:

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`truth table: Binary Operations 5`

----

*********************************************************************************
number the project
*********************************************************************************

* I name this project ``elevator``
* I open a terminal_
* I use uv_ to make a directory_ for the project

  .. code-block:: python
    :emphasize-lines: 1

    uv init elevator

  the terminal_ shows

  .. code-block:: shell

    Initialized project `elevator` at `.../pumping_python/elevator`

  then goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd elevator

  the terminal_ shows I am in the ``elevator`` folder_

  .. code-block:: shell

    .../pumping_python/elevator

* I remove ``main.py`` from the project because I do not use it

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I make a directory_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` to hold the source code in the ``src`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch src/elevator.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/elevator.py

  the terminal_ goes back to the command line

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I make the ``tests`` directory_ a `Python package`_

  .. DANGER:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

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

  the terminal_ goes back to the command line

* I make a :ref:`Python file<what is a module?>` for the tests in the ``tests`` directory_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/test_elevator.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_elevator.py

  the terminal_ goes back to the command line

* I open ``test_elevator.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_elevator.py

    `Visual Studio Code`_ opens ``test_elevator.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestElevator(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed the `Python packages`_

* I use tree_ to look at the structure of the project

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── README.md
    ├── pyproject.toml
    ├── requirements.txt
    ├── src
    │   └── elevator.py
    ├── tests
    │   ├── __init__.py
    │   └── test_elevator.py
    └── uv.lock

  if you do not see ``uv.lock`` in your tree, do not worry, run the tests next

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ======================== FAILURES ========================
    _________________ TestElevator.test_failure ___________________

    self = <tests.test_elevator.TestElevator testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_elevator.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_elevator.py::TestElevator::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` have 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors then try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_elevator.py``

  .. code-block:: python
    :lineno-number: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestElevator(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-number: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_doors_close
*********************************************************************************

The :ref:`truth table` for when the doors are :green:`clear` to the numberer is

================  ==================  =================
doors             floor number        output
================  ==================  =================
:green:`clear`    :green:`pressed`    :green:`ON`
:green:`clear`    :red:`NOT pressed`  :red:`OFF`
================  ==================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_doors_close``, then add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear` and the number button is :green:`pressed`

================  ==================  =================
doors             floor number        output
================  ==================  =================
:green:`clear`    :green:`pressed`    :green:`ON`
================  ==================  =================

.. code-block:: python
  :lineno-number: 4
  :emphasize-lines: 3-9

  class TestElevator(unittest.TestCase):

      def test_doors_close(self):
          my_expectation = 'ON'
          reality = src.elevator.numberer(
              doors_clear=True,
              number_pushed=True,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen
  # AssertionError

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'src' is not defined

because I do not have a definition for ``src`` in this file_

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-number: 15
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.elevator
    import unittest


    class TestElevator(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.elevator' has no attribute 'numberer'

  because ``elevator.py`` in the ``src`` folder_ does not have anything named ``numberer`` in it

  .. admonition:: If you get :ref:`ModuleNotFoundError<what is a module?>`

    .. code-block:: python

      ModuleNotFoundError: No module named 'src'

    check if you have ``__init__.py`` in the ``tests`` folder_ with underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-number: 16
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``elevator.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` named ``numberer`` to ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def numberer():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: numberer() got an unexpected doorsword argument 'doors_clear'

  because the test called the ``numberer`` :ref:`function<what is a function?>` with 2 doorsword arguments (``doors_clear`` and ``number_pushed``) and this definition only allows calls with 0 arguments

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_elevator.py``

  .. code-block:: python
    :lineno-number: 16
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add the :ref:`doorsword argument<test_functions_w_doorsword_arguments>` to the :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def numberer(doors_clear):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: numberer() got an unexpected doorsword argument 'number_pushed'

  because the test called the ``numberer`` :ref:`function<what is a function?>` with 2 doorsword arguments (``doors_clear`` and ``number_pushed``) and this definition only allows calls with 1 input

* I add ``number_pushed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def numberer(doors_clear, number_pushed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'ON'

  the ``numberer`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the test expects :green:`'ON'`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def numberer(doors_clear, number_pushed):
        return 'ON'

  the test passes. The ``numberer`` :ref:`function<what is a function?>` always returns :green:`ON`, it does not elevatore about the inputs. Is this :ref:`Tautology?<test_tautology>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear` and the number button is :red:`NOT pressed`, in ``test_elevator.py``

  ================  ==================  =================
  doors             floor number        output
  ================  ==================  =================
  :green:`clear`    :green:`pressed`    :green:`ON`
  :green:`clear`    :red:`NOT pressed`  :red:`OFF`
  ================  ==================  =================

  .. code-block:: python
    :lineno-number: 7
    :emphasize-lines: 9-14

        def test_doors_close(self):
            my_expectation = 'ON'
            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'
            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ON' != 'OFF'

  because the ``numberer`` :ref:`function<what is a function?>` returns :green:`'ON'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``numberer`` :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def numberer(doors_clear, number_pushed):
        if number_pushed == False:
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def numberer(doors_clear, number_pushed):
        # if number_pushed == False:
        if not number_pushed == True:
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def numberer(doors_clear, number_pushed):
        # if number_pushed == False:
        # if not number_pushed == True:
        if not number_pushed:
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def numberer(doors_clear, number_pushed):
        if not number_pushed:
            return 'OFF'

        return 'ON'

  this is what happens when the ``numberer`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the number button is :red:`NOT pressed`
  - it returns :green:`'ON'` if the above condition is not met

----

*********************************************************************************
test_doors_far
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT clear` from the numberer is

==============  ==================  ==========
doors             floor number        output
==============  ==================  ==========
:red:`NOT clear`  :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==========

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer and the number button is :green:`pressed`, in ``test_elevator.py``

==============  ==================  ==========
doors             floor number        output
==============  ==================  ==========
:red:`NOT clear`  :green:`pressed`    :red:`OFF`
==============  ==================  ==========

.. code-block:: python
  :lineno-number: 15
  :emphasize-lines: 8-14

            my_expectation = 'OFF'
            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_doors_far(self):
            my_expectation = 'OFF'
            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'ON' != 'OFF'

because the ``numberer`` :ref:`function<what is a function?>` returns :green:`'ON'` and the test expects :red:`'OFF'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``elevator.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def numberer(doors_clear, number_pushed):
      if doors_clear == False:
          return 'OFF'

      if not number_pushed:
          return 'OFF'

      return 'ON'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the new :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def numberer(doors_clear, number_pushed):
        # if doors_clear == False:
        if not doors_clear == True:
            return 'OFF'

        if not number_pushed:
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def numberer(doors_clear, number_pushed):
        # if doors_clear == False:
        # if not doors_clear == True:
        if not doors_clear:
            return 'OFF'

        if not number_pushed:
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the two :ref:`if statements` together because they both return the same thing (``'OFF'``)

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 7-8

    def numberer(doors_clear, number_pushed):
        # if doors_clear == False:
        # if not doors_clear == True:
        # if not doors_clear:
        #     return 'OFF'

        # if not number_pushed:
        if not doors_clear or not number_pushed:
            return 'OFF'

        return 'ON'

  the test is still green

* I rewrite the statement in terms of :ref:`Logical Negation (NOT)<test_logical_negation>` because it happens two times

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-12

    def numberer(doors_clear, number_pushed):
        # if doors_clear == False:
        # if not doors_clear == True:
        # if not doors_clear:
        #     return 'OFF'
        # if not number_pushed:
        # if not doors_clear or not number_pushed:
        if (
            (not doors_clear)
            (not and)
            (not number_pushed)
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_elevator.py``

  .. code-block:: python
    :lineno-number: 31
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I "factor" out the :ref:`nots<test_logical_negation>` in the ``numberer`` :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-13

    def numberer(doors_clear, number_pushed):
        # if doors_clear == False:
        # if not doors_clear == True:
        # if not doors_clear:
        #     return 'OFF'
        # if not number_pushed:
        # if not doors_clear or not number_pushed:
        # if (
        #     (not doors_clear)
        #     (not and)
        #     (not number_pushed)
        # ):
        if not (doors_clear and number_pushed):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def numberer(doors_clear, number_pushed):
        if not (doors_clear and number_pushed):
            return 'OFF'

        return 'ON'

  this is what happens when the ``numberer`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the doors are :red:`NOT clear` from the numberer OR the number button is :red:`NOT pressed`
  - it returns :green:`'ON'` if the above conditions are not met

  is this :ref:`Logical Conjunction?<test_logical_conjunction>`

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer and the number button is :red:`NOT pressed` to :ref:`test_doors_far` in ``test_elevator.py``

  ==============  ==================  ==========
  doors             floor number        output
  ==============  ==================  ==========
  :red:`NOT clear`  :green:`pressed`    :red:`OFF`
  :red:`NOT clear`  :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  ==========

  .. code-block:: python
    :lineno-number: 22
    :emphasize-lines: 9-13

        def test_doors_far(self):
            my_expectation = 'OFF'
            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

  - I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (:red:`'OFF'`)

* I make a :ref:`global variable<what is a variable?>` to remove repetition from the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.elevator
    import unittest


    OFF = 'OFF'


    class TestElevator(unittest.TestCase):

  this way all the tests can use the same :ref:`global variable<what is a variable?>` and I do not have to make one for each test

* I use the new :ref:`global variable<what is a variable?>` to remove ``'OFF'`` from :ref:`test_doors_close`

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 9, 14-15

        def test_doors_close(self):
            my_expectation = 'ON'
            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'OFF'
            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-number: 10

        def test_doors_close(self):
            my_expectation = 'ON'
            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.elevator.numberer(
                doors_clear=True,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far(self):

* I use the new :ref:`global variable<what is a variable?>` to remove ``'OFF'`` from :ref:`test_doors_far`

  .. code-block:: python
    :lineno-number: 24
    :emphasize-lines: 2, 7-8, 14-15

        def test_doors_far(self):
            # my_expectation = 'OFF'
            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)


    # Exceptions seen

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-number: 24

        def test_doors_far(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.elevator.numberer(
                doors_clear=False,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

----

*********************************************************************************
test_doors_close_weight limit_pressed
*********************************************************************************

So far, the :ref:`truth table` for the elevator numberer is

================  ==================  =================
doors             floor number        output
================  ==================  =================
:green:`clear`    :green:`pressed`    :green:`ON`
:green:`clear`    :red:`NOT pressed`  :red:`OFF`
:red:`NOT clear`  :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :red:`NOT pressed`  :red:`OFF`
================  ==================  =================

I want the elevator to number only when the weight limit pedal is pressed, the inputs for the elevator will then be

* are the doors clear?
* is it above the weight limit?
* was the number for a floor pushed?

and the :ref:`truth table` for when the doors are :green:`clear` and the weight limit is being :green:`pressed`, is:

==============  ==================  ==================  ===========
doors           weight limit        floor number        output
==============  ==================  ==================  ===========
:green:`clear`  :green:`above`      :green:`pressed`    :green:`ON`
:green:`clear`  :green:`above`      :red:`NOT pressed`  :red:`OFF`
================  ==================  ==================  ===========

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``above_weight_limit`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_doors_close`, for when the doors are :green:`clear`, the weight limit is being :green:`pressed` and the number button is :green:`pressed`

==============  ==================  ==================  ===========
doors           weight limit        floor number        output
==============  ==================  ==================  ===========
:green:`clear`  :green:`above`      :green:`pressed`    :green:`ON`
================  ==================  ==================  ===========


.. code-block:: python
  :lineno-number: 7
  :emphasize-lines: 5

      def test_doors_close(self):
          my_expectation = 'ON'
          reality = src.elevator.numberer(
              doors_clear=True,
              above_weight_limit=True,
              number_pushed=True,
          )
          self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: shell

  TypeError: numberer() got an unexpected doorsword argument 'above_weight_limit'. Did you mean 'number_pushed'?

because the test called the ``numberer`` :ref:`function<what is a function?>` with 3 doorsword arguments (``doors_clear``, ``above_weight_limit`` and ``number_pushed``) and the :ref:`function<what is a function?>` only allows calls with 2 arguments (``doors_clear`` and ``number_pushed``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``above_weight_limit`` to the :ref:`function signature<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit,
        ):
        if not (doors_clear and number_pushed):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_doors_close - TypeError: numberer() missing 1 required positional argument: 'above_weight_limit'
    FAILED ...test_doors_far - TypeError: numberer() missing 1 required positional argument: 'above_weight_limit'

  because the tests call the ``numberer`` :ref:`function<what is a function?>` with 2 arguments (``doors_clear`` and ``number_pushed``) and I just changed the :ref:`function signature<what is a function?>` to make it take 3 required arguments (``doors_clear``, ``number_pushed`` and ``above_weight_limit``). I have to make ``above_weight_limit`` a choice.

* I add a :ref:`default value<test_functions_w_default_arguments>` to make ``above_weight_limit`` a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):

  the test passes because

  .. code-block:: python

    src.elevator.numberer(
        doors_clear=True,
        number_pushed=False,
    )

  is now the same as

  .. code-block:: python

    src.elevator.numberer(
        doors_clear=True,
        number_pushed=False,
        above_weight_limit=False,
    )

  a :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``above_weight_limit`` to the next :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is being :green:`pressed` and the number button is :red:`NOT pressed`

  ================  ==================  ==================  ===========
  doors           weight limit        floor number        output
  ================  ==================  ==================  ===========
  :green:`clear`  :green:`above`      :green:`pressed`    :green:`ON`
  :green:`clear`  :green:`above`      :red:`NOT pressed`  :red:`OFF`
  ================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 7
    :emphasize-lines: 12

        def test_doors_close(self):
            my_expectation = 'ON'
            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=True,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=True,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far(self):

  the test is still green

* I change the name of the test from :ref:`test_doors_close` to :ref:`test_doors_close_weight limit_pressed`

  .. code-block:: python
    :lineno-number: 5
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_doors_close_weight limit_pressed(self):
            my_expectation = 'OFF'

----

*********************************************************************************
test_doors_close_weight limit_not_pressed
*********************************************************************************

The :ref:`truth table` for when the doors are :green:`clear` and the weight limit is :red:`NOT pressed` is

==============  ==================  ==================  ===========
doors           weight limit        floor number        output
==============  ==================  ==================  ===========
:green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
:green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`OFF`
================  ==================  ==================  ===========

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is :red:`NOT pressed` and the number button is :green:`pressed`

  ================  ==================  ==================  ===========
  doors           weight limit        floor number        output
  ================  ==================  ==================  ===========
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
  ================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 19
    :emphasize-lines: 8-14

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=True,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_close_weight limit_not_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ON' != 'OFF'

  because the ``numberer`` :ref:`function<what is a function?>` returned :green:`'ON'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``numberer`` :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        if above_weight_limit == False:
            return 'OFF'

        if not (doors_clear and number_pushed):
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the new :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        # if above_weight_limit == False:
        if not above_weight_limit == True:
            return 'OFF'

        if not (doors_clear and number_pushed):
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        # if above_weight_limit == False:
        # if not above_weight_limit == True:
        if not above_weight_limit:
            return 'OFF'

        if not (doors_clear and number_pushed):
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjunction<test_logical_disjunction>` to put the two :ref:`if statements` together because they return the same thing

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-15

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        # if above_weight_limit == False:
        # if not above_weight_limit == True:
        # if not above_weight_limit:
        #     return 'OFF'

        # if not (doors_clear and number_pushed):
        if (
            not (doors_clear and number_pushed)
            or
            not above_weight_limit
        ):
            return 'OFF'

        return 'ON'

  green

* I write the statement in terms of :ref:`NOT<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-20

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        # if above_weight_limit == False:
        # if not above_weight_limit == True:
        # if not above_weight_limit:
        #     return 'OFF'

        # if not (doors_clear and number_pushed):
        # if (
        #     not (doors_clear and number_pushed)
        #     or
        #     not above_weight_limit
        # ):
        if (
            (not (doors_clear and number_pushed))
            (not and)
            (not above_weight_limit)
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I "factor" out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-25

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        # if above_weight_limit == False:
        # if not above_weight_limit == True:
        # if not above_weight_limit:
        #     return 'OFF'

        # if not (doors_clear and number_pushed):
        # if (
        #     not (doors_clear and number_pushed)
        #     or
        #     not above_weight_limit
        # ):
        # if (
        #     (not (doors_clear and number_pushed))
        #     (not and)
        #     (not above_weight_limit)
        # ):
        if not (
            (doors_clear and number_pushed)
            and
            (above_weight_limit)
        ):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False,
        ):
        if not (
            doors_clear
            and number_pushed
            and above_weight_limit
        ):
            return 'OFF'

        return 'ON'

  this is what happens when the ``numberer`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the doors are :red:`NOT clear` from the numberer OR the number button is :red:`NOT pressed` OR the weight limit is :red:`NOT pressed`
  - it returns :green:`'ON'` if none of the conditions are met

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is :red:`NOT pressed` and the number button is :red:`NOT pressed`, in :ref:`test_doors_close_weight limit_not_pressed` in ``test_elevator.py``

  ================  ==================  ==================  ===========
  doors           weight limit        floor number        output
  ================  ==================  ==================  ===========
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
  :green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`OFF`
  ================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 26
    :emphasize-lines: 9-14

        def test_doors_close_weight limit_not_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far(self):

  the test is still green

----

*********************************************************************************
test_doors_far_weight limit_pressed
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT clear` from the numberer and the weight limit is being :green:`pressed`, is:

================  ==================  ==================  ===========
doors             weight limit        floor number        output
================  ==================  ==================  ===========
:red:`NOT clear`  :green:`above`      :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :green:`above`      :red:`NOT pressed`  :red:`OFF`
==================  ==================  ==================  ===========

* I add a value for the ``above_weight_limit`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_doors_close` for the case where the doors are :red:`NOT clear` from the numberer, the weight limit is being :green:`pressed` and the number button is :green:`pressed`

  ==================  ==================  ==================  ===========
  doors             weight limit        floor number        output
  ==================  ==================  ==================  ===========
  :red:`NOT clear`  :green:`above`      :green:`pressed`    :red:`OFF`
  ==================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 34
    :emphasize-lines: 11

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

  the test is still green

* I add a value for ``above_weight_limit`` to the next :ref:`assertion<what is an assertion?>`, for when the doors are :red:`NOT clear` from the numberer, the weight limit is being :green:`pressed` and the number button is :red:`NOT pressed`

  ==================  ==================  ==================  ===========
  doors             weight limit        floor number        output
  ==================  ==================  ==================  ===========
  :red:`NOT clear`  :green:`above`      :green:`pressed`    :red:`OFF`
  :red:`NOT clear`  :green:`above`      :red:`NOT pressed`  :red:`OFF`
  ==================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 40
    :emphasize-lines: 11

        def test_doors_far(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green

* I change the name of the test from :ref:`test_doors_far` to :ref:`test_doors_far_weight limit_pressed`

  .. code-block:: python
    :lineno-number: 34
    :emphasize-lines: 8

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far_weight limit_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

----

*********************************************************************************
test_doors_far_weight limit_not_pressed
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT clear` from the numberer and the weight limit is :red:`NOT pressed` is

================  ==================  ==================  ===========
doors             weight limit        floor number        output
================  ==================  ==================  ===========
:red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`OFF`
==================  ==================  ==================  ===========

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is :red:`NOT pressed` and the number button is :green:`pressed`

  ==================  ==================  ==================  ===========
  doors             weight limit        floor number        output
  ==================  ==================  ==================  ===========
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
  ==================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 48
    :emphasize-lines: 8-14

            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_doors_far_weight limit_not_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=False,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is :red:`NOT pressed` and the number button is :red:`NOT pressed`

  ==================  ==================  ==================  ===========
  doors             weight limit        floor number        output
  ==================  ==================  ==================  ===========
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`OFF`
  ==================  ==================  ==================  ===========

  .. code-block:: python
    :lineno-number: 56
    :emphasize-lines: 9-14

        def test_doors_far_weight limit_not_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=False,
                number_pushed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=False,
                number_pushed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green

* I call the ``numberer`` :ref:`function<what is a function?>` directly in :ref:`test_doors_far_weight limit_not_pressed`, I do not need the ``reality`` :ref:`variable<what is a variable?>` because it is only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-number: 56
    :emphasize-lines: 7-15, 22-30

        def test_doors_far_weight limit_not_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=False,
                number_pushed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                ),
                OFF
            )

            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=False,
                number_pushed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                OFF
            )

  the test is still green

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-number: 56

        def test_doors_far_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                OFF
            )


    # Exceptions seen

* I do the same thing in :ref:`test_doors_far_weight limit_pressed`

  .. code-block:: python
    :lineno-number: 41
    :emphasize-lines: 7-15, 22-30

        def test_doors_far_weight limit_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                    src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                ),
                OFF
            )

            reality = src.elevator.numberer(
                doors_clear=False,
                above_weight_limit=True,
                number_pushed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_not_pressed(self):

  still green

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_doors_far_weight limit_pressed`

  .. code-block:: python
    :lineno-number: 41

        def test_doors_far_weight limit_pressed(self):
            self.assertEqual(
                    src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_not_pressed(self):

* on to :ref:`test_doors_close_weight limit_not_pressed`

  .. code-block:: python
    :lineno-number: 26
    :emphasize-lines: 7-15, 22-30

        def test_doors_close_weight limit_not_pressed(self):
            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                ),
                OFF
            )

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=False,
                number_pushed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_pressed(self):

  green

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_doors_close_weight limit_not_pressed`

  .. code-block:: python
    :lineno-number: 26

        def test_doors_close_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_pressed(self):

* I call the ``numberer`` :ref:`function<what is a function?>` directly in :ref:`test_doors_close_weight limit_pressed`

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 8-16, 23-31

        def test_doors_close_weight limit_pressed(self):
            my_expectation = 'ON'
            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=True,
                number_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                ),
                'ON'
            )

            reality = src.elevator.numberer(
                doors_clear=True,
                above_weight_limit=True,
                number_pushed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_close_weight limit_not_pressed(self):

  still green

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_doors_close_weight limit_pressed`

  .. code-block:: python
    :lineno-number: 10

        def test_doors_close_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_close_weight limit_not_pressed(self):

----

*********************************************************************************
test_doors_close_weight limit_pressed_w_emergency
*********************************************************************************

the :ref:`truth table` for the elevator numberer is

==============  ==================  ==================  ===========
doors           weight limit        floor number        output
==============  ==================  ==================  ===========
:green:`clear`  :green:`above`      :green:`pressed`    :green:`ON`
:green:`clear`  :green:`above`      :red:`NOT pressed`  :red:`OFF`
:green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
:green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

================  ==================  ==================  ===========
doors             weight limit        floor number        output
================  ==================  ==================  ===========
:red:`NOT clear`  :green:`above`      :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :green:`above`      :red:`NOT pressed`  :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`OFF`
================  ==================  ==================  ===========

I want to make sure the elevator is emergency before it can number, so it does not immediately move when it is turned on (that would be a problem). The inputs will then be

* are the doors clear?
* is it above the weight limit?
* was the number for a floor pushed?
* emergency stop?

and the :ref:`truth table` for when the doors are :green:`clear` and the weight limit is being :green:`pressed`, is:

==============  ==================  ==================  ====================  ================
doors           weight limit      floor number        emergency             output
==============  ==================  ==================  ====================  ================
:green:`clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :green:`ON`
:green:`clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:green:`clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:green:`clear`  :green:`above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
==============  ==================  ==================  ====================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``emergency`` to the :ref:`assertion<what is an assertion?>` for the case where the doors are :green:`clear`, the weight limit is being :green:`pressed`, the number button is :green:`pressed` and the elevator emergency is :green:`emergency`, to :ref:`test_doors_close_weight limit_pressed`

==============  ==================  ==================  ====================  ================
doors           weight limit      floor number        emergency             output
==============  ==================  ==================  ====================  ================
:green:`clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :green:`ON`
==============  ==================  ==================  ====================  ================

.. code-block:: python
  :lineno-number: 10
  :emphasize-lines: 7

        def test_doors_close_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                'ON'
            )

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: numberer() got an unexpected doorsword argument 'emergency'

because the test called the ``numberer`` :ref:`function<what is a function?>` with 4 doorsword arguments (``doors_clear``, ``above_weight_limit``, ``number_pushed`` and ``emergency``) and the definition only allows calls with 2 required arguments (``doors_clear`` and ``number_pushed``) and 1 optional argument (``above_weight_limit``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``emergency`` to the ``numberer`` :ref:`function signature<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False, emergency,
        ):
        if not (
            doors_clear
            and number_pushed
            and above_weight_limit
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_doorsword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``emergency`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def numberer(
        doors_clear, number_pushed,
        above_weight_limit=False, emergency=False,
    ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is being :green:`pressed`, the number button is :green:`pressed` and the elevator emergency is :red:`NOT emergency`

  ==============  ==================  ==================  ====================  ================
  doors           weight limit      floor number        emergency             output
  ==============  ==================  ==================  ====================  ================
  :green:`clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :green:`ON`
  :green:`clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  ==============  ==================  ==================  ====================  ================

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 12-20

        def test_doors_close_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                ),
                OFF
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ON' != 'OFF'

  because the ``numberer`` :ref:`function<what is a function?>` returns :green:`'ON'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``numberer`` :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        if emergency == False:
            return 'OFF'

        if not (
            doors_clear
            and number_pushed
            and above_weight_limit
        ):
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-number: 5
    :emphasize-lines: 1-2

        # if emergency == False:
        if not emergency == True:
            return 'OFF'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-number: 5
    :emphasize-lines: 2-3

        # if emergency == False:
        # if not emergency == True:
        if not emergency:
            return 'OFF'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the two :ref:`if statements` together because they both return :red:`'OFF'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-21

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        # if emergency == False:
        # if not emergency == True:
        # if not emergency:
        #     return 'OFF'

        # if not (
        #     doors_clear
        #     and number_pushed
        #     and above_weight_limit
        # ):
        if (
            not (
                doors_clear
                and number_pushed
                and above_weight_limit
            ) or not emergency
        ):
            return 'OFF'

        return 'ON'

  that is one long confusing statement

* I write the new :ref:`if statement<if statements>` in terms of :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 6-21

        # if not (
        #     doors_clear
        #     and number_pushed
        #     and above_weight_limit
        # ):
        # if (
        #     not (
        #         doors_clear
        #         and number_pushed
        #         and above_weight_limit
        #     ) or not emergency
        # ):
        if (
            (not (
                doors_clear
                and number_pushed
                and above_weight_limit
            ))
            (not and)
            (not emergency)
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I factor out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 13-30

        # if not (
        #     doors_clear
        #     and number_pushed
        #     and above_weight_limit
        # ):
        # if (
        #     not (
        #         doors_clear
        #         and number_pushed
        #         and above_weight_limit
        #     ) or not emergency
        # ):
        # if (
        #     (not (
        #         doors_clear
        #         and number_pushed
        #         and above_weight_limit
        #     ))
        #     (not and)
        #     (not emergency)
        # ):
        if not (
            (
                doors_clear
                and number_pushed
                and above_weight_limit
            )
            and
            emergency
        ):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def numberer(
            doors_clear, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        if not (
            doors_clear
            and number_pushed
            and above_weight_limit
            and emergency
        ):
            return 'OFF'

        return 'ON'

  this is what happens when the ``numberer`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the doors are :red:`NOT clear` from the numberer OR the number button is :red:`NOT pressed` OR the weight limit is :red:`NOT pressed` OR the elevator emergency is :red:`NOT emergency`
  - it returns :green:`'ON'` if none of the conditions are met

* I add a value for the ``emergency`` parameter in the next :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is being :green:`pressed`, the number button is :red:`NOT pressed` and the elevator emergency is :green:`emergency`, in :ref:`test_doors_close_weight limit_pressed` in ``test_elevator.py``

  ==============  ==================  ==================  ====================  ================
  doors           weight limit      floor number        emergency             output
  ==============  ==================  ==================  ====================  ================
  :green:`clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :green:`ON`
  :green:`clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :green:`clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  ==============  ==================  ==================  ====================  ================

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 27

        def test_doors_close_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

        def test_doors_close_weight limit_not_pressed(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is being :green:`pressed`, the number button is :red:`NOT pressed` and the elevator emergency is  :red:`NOT emergency`

  ==============  ==================  ==================  ====================  ================
  doors           weight limit      floor number        emergency             output
  ==============  ==================  ==================  ====================  ================
  :green:`clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :green:`ON`
  :green:`clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :green:`clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  :green:`clear`  :green:`above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
  ==============  ==================  ==================  ====================  ================

  .. code-block:: python
    :lineno-number: 10
    :emphasize-lines: 32-40

        def test_doors_close_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )

        def test_doors_close_weight limit_not_pressed(self):

  green

* I change the name of the test from :ref:`test_doors_close_weight limit_pressed` to :ref:`test_doors_close_weight limit_pressed_w_emergency`

  .. code-block:: python
    :lineno-number: 8
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_doors_close_weight limit_pressed_w_emergency(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                'ON'
            )

----

*********************************************************************************
test_doors_close_weight limit_not_pressed_w_emergency
*********************************************************************************

The :ref:`truth table` for when the doors are :green:`clear` and the weight limit is :red:`NOT pressed` is

================  ==================  ==================  ====================  ==========
doors           weight limit        floor number        emergency             output
================  ==================  ==================  ====================  ==========
:green:`clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
:green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
================  ==================  ==================  ====================  ==========

* I add a value for the ``emergency`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_doors_close_weight limit_not_pressed` for when the doors are :green:`clear`, the weight limit is :red:`NOT pressed`, the number button is :green:`pressed` and the elevator emergency is :green:`emergency`

  ================  ==================  ==================  ====================  ==========
  doors           weight limit        floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 51
    :emphasize-lines: 7

        def test_doors_close_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is :red:`NOT pressed`, the number button is :green:`pressed` and the elevator emergency is :red:`NOT emergency`

  ================  ==================  ==================  ====================  ==========
  doors           weight limit        floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 51
    :emphasize-lines: 12-20

        def test_doors_close_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_pressed(self):

  the test is still green

* I add a value for ``emergency`` to the next :ref:`assertion<what is an assertion?>`, for when the doors are :green:`clear`, the weight limit is :red:`NOT pressed`, the number button is :red:`NOT pressed` and the elevator emergency is :green:`emergency`

  ================  ==================  ==================  ====================  ==========
  doors           weight limit        floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 51
    :emphasize-lines: 27

        def test_doors_close_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

        def test_doors_far_weight limit_pressed(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :green:`clear`, the weight limit is :red:`NOT pressed`, the number button is :red:`NOT pressed` and the elevator emergency is :red:`NOT emergency`

  ================  ==================  ==================  ====================  ==========
  doors           weight limit        floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  :green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 51
    :emphasize-lines: 32-40

        def test_doors_close_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_pressed(self):

  green

* I change the name of the test from :ref:`test_doors_close_weight limit_not_pressed` to :ref:`test_doors_close_weight limit_not_pressed_w_emergency`

  .. code-block:: python
    :lineno-number: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )

        def test_doors_close_weight limit_not_pressed_w_emergency(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

----

*********************************************************************************
test_doors_far_weight limit_pressed_w_emergency
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT clear` from the numberer and the weight limit is being :green:`pressed` is

================  ==================  ==================  ====================  ==========
doors             weight limit      floor number        emergency             output
================  ==================  ==================  ====================  ==========
:red:`NOT clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
================  ==================  ==================  ====================  ==========

* I add a value for the ``emergency`` parameter in the first :ref:`assertion<what is an assertion?>` of :ref:`test_doors_far_weight limit_pressed`, for when the doors are :red:`NOT clear` from the numberer, the weight limit is being :green:`pressed`, the number button is :green:`pressed`, and the elevator emergency is :green:`emergency`

  ================  ==================  ==================  ====================  ==========
  doors             weight limit      floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 92
    :emphasize-lines: 7

        def test_doors_far_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is being :green:`pressed`, the number button is :green:`pressed` and the elevator emergency is :red:`NOT emergency`

  ================  ==================  ==================  ====================  ==========
  doors             weight limit      floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 92
    :emphasize-lines: 12-20

        def test_doors_far_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_not_pressed(self):

  still green

* I add a value for the ``emergency`` parameter to the next :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is being :green:`pressed`, the number button is :red:`NOT pressed`, and the elevator emergency is :green:`emergency`

  ================  ==================  ==================  ====================  ==========
  doors             weight limit      floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 92
    :emphasize-lines: 27

        def test_doors_far_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

        def test_doors_far_weight limit_not_pressed(self):

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is being :green:`pressed`, the number button is :red:`NOT pressed`, and the elevator emergency is :red:`NOT emergency`

  ================  ==================  ==================  ====================  ==========
  doors             weight limit      floor number        emergency             output
  ================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
  ================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 92
    :emphasize-lines: 32-40

        def test_doors_far_weight limit_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_not_pressed(self):

  still green

* I change the name of the test from :ref:`test_doors_far_weight limit_pressed` to :ref:`test_doors_far_weight limit_pressed_w_emergency`

  .. code-block:: python
    :lineno-number: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=True,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_pressed_w_emergency(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

----

*********************************************************************************
test_doors_far_weight limit_not_pressed_w_emergency
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT clear` from the numberer and the weight limit is :red:`NOT pressed` is

==================  ==================  ==================  ====================  ==========
doors             weight limit        floor number        emergency             output
==================  ==================  ==================  ====================  ==========
:red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
==================  ==================  ==================  ====================  ==========

* I add a value for the ``emergency`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_doors_far_weight limit_not_pressed`, for when the doors are :red:`NOT clear` from the numberer, the weight limit is :red:`NOT pressed`, the number button is :green:`pressed`, and the elevator emergency is :green:`emergency`

  ==================  ==================  ==================  ====================  ==========
  doors             weight limit        floor number        emergency             output
  ==================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  ==================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 133
    :emphasize-lines: 7

        def test_doors_far_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is :red:`NOT pressed`, the number button is :green:`pressed`, and the elevator emergency is :red:`NOT emergency`

  ==================  ==================  ==================  ====================  ==========
  doors             weight limit        floor number        emergency             output
  ==================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  ==================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 133
    :emphasize-lines: 12-20

        def test_doors_far_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                OFF
            )


    # Exceptions seen

  still green

* I add a value for the ``emergency`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the doors are :red:`NOT clear` from the numberer, the weight limit is :red:`NOT pressed`, the number button is :red:`NOT pressed`, and the elevator emergency is :green:`emergency`

  ==================  ==================  ==================  ====================  ==========
  doors             weight limit        floor number        emergency             output
  ==================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  ==================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 133
    :emphasize-lines: 27

        def test_doors_far_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

  green

* I add an :ref:`assertion<what is an assertion?>` for when the doors are :red:`NOT clear` from the numberer, the weight limit is :red:`NOT pressed`, the number button is :red:`NOT pressed`, and the elevator emergency is :red:`NOT emergency`

  ==================  ==================  ==================  ====================  ==========
  doors             weight limit        floor number        emergency             output
  ==================  ==================  ==================  ====================  ==========
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
  :red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
  ==================  ==================  ==================  ====================  ==========

  .. code-block:: python
    :lineno-number: 133
    :emphasize-lines: 32-40

        def test_doors_far_weight limit_not_pressed(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=True,
                ),
                OFF
            )

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )


    # Exceptions seen

  all the tests are still green

* I change the name of the test from :ref:`test_doors_far_weight limit_not_pressed` to :ref:`test_doors_far_weight limit_not_pressed_w_emergency`

  .. code-block:: python
    :lineno-number: 123
    :emphasize-lines: 11

            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=False,
                ),
                OFF
            )

        def test_doors_far_weight limit_not_pressed_w_emergency(self):
            self.assertEqual(
                src.elevator.numberer(
                    doors_clear=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                OFF
            )

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_elevator.py`` and ``elevator.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the doorsboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``elevator``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*************************************************************************************
review
*************************************************************************************

I ran tests for a elevator with these inputs:

* are the doors clear?
* is it above the weight limit?
* was the number for a floor pushed?
* is the elevator emergency?

the inputs gave me this :ref:`truth table`

==============  ==================  ==================  ====================  ================
doors           weight limit      floor number        emergency             output
==============  ==================  ==================  ====================  ================
:green:`clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :green:`ON`
:green:`clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:green:`clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:green:`clear`  :green:`above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
==============  ==================  ==================  ====================  ================

================  ==================  ==================  ====================  ==========
doors           weight limit        floor number        emergency             output
================  ==================  ==================  ====================  ==========
:green:`clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
:green:`clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:green:`clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
================  ==================  ==================  ====================  ==========

================  ==================  ==================  ====================  ==========
doors             weight limit      floor number        emergency             output
================  ==================  ==================  ====================  ==========
:red:`NOT clear`  :green:`above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :green:`above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :green:`above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
================  ==================  ==================  ====================  ==========

==================  ==================  ==================  ====================  ==========
doors             weight limit        floor number        emergency             output
==================  ==================  ==================  ====================  ==========
:red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :green:`pressed`    :red:`NOT emergency`  :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :green:`emergency`    :red:`OFF`
:red:`NOT clear`  :red:`NOT above`    :red:`NOT pressed`  :red:`NOT emergency`  :red:`OFF`
==================  ==================  ==================  ====================  ==========

the only time I can number this elevator is when the doors are :green:`clear` to the numberer, the weight limit is being :green:`pressed`, the number button is :green:`pressed` and the elevator emergency is :green:`emergency`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<elevator: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you now know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`

:ref:`Would you like to test making a calculator?<how to make a calculator>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->