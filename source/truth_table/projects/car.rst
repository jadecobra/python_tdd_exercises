.. meta::
  :description: Build a safety-critical car logic system in Python using truth tables and TDD. This beginner tutorial teaches how to manage multiple boolean inputs—door status, timers, and too_hot failsafes—while writing clean, verified code.
  :keywords: Python car logic project, safety-critical systems python tutorial, TDD python car example, how to code a car in python, python multiple boolean inputs tutorial, red green refactor examples, python truth table practice, learn Converse NonImplication python, uv python project management, pytest-watcher logic testing, Jacob Itegboje

.. include:: ../../links.rst

.. _car:

#################################################################################
Car
#################################################################################

I want to make a **Car** that can be turned on with the push of a button, if the inputs are

* is the key close?
* was the start button pushed?

this is the :ref:`truth table` I get

==============  =================  =================
key             start button       output
==============  =================  =================
:green:`close`  :green:`pushed`    :green:`ON`
:green:`close`  :red:`NOT pushed`  :red:`OFF`
:red:`far`      :green:`pushed`    :red:`OFF`
:red:`far`      :red:`NOT pushed`  :red:`OFF`
==============  =================  =================

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_car.py
  :language: python
  :linenos:

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`truth table: Binary Operations 5`

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``car``
* I open a terminal_
* I use uv_ to make a directory_ for the project

  .. code-block:: python
    :emphasize-lines: 1

    uv init car

  the terminal_ shows

  .. code-block:: shell

    Initialized project `car` at `.../pumping_python/car`

  then goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd car

  the terminal_ shows I am in the ``car`` folder_

  .. code-block:: shell

    .../pumping_python/car

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

        touch src/car.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/car.py

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

        touch tests/test_car.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_car.py

  the terminal_ goes back to the command line

* I open ``test_car.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_car.py

    `Visual Studio Code`_ opens ``test_car.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestCar(unittest.TestCase):

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
    │   └── car.py
    ├── tests
    │   ├── __init__.py
    │   └── test_car.py
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

    ================================ FAILURES ================================
    _________________________ TestCar.test_failure ___________________________

    self = <tests.test_car.TestCar testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_car.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_car.py::TestCar::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

  because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` have 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors then try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_car.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestCar(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_starter_w_key_close
*********************************************************************************

The :ref:`truth table` for when the key is :green:`close` to the starter is

==============  =================  =================
key             start button       output
==============  =================  =================
:green:`close`  :green:`pushed`    :green:`ON`
:green:`close`  :red:`NOT pushed`  :red:`OFF`
==============  =================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_starter_w_key_close``, then add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close` and the start button is :green:`pushed`

==============  =================  =================
key             start button       output
==============  =================  =================
:green:`close`  :green:`pushed`    :green:`ON`
==============  =================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestCar(unittest.TestCase):

      def test_starter_w_key_close(self):
          my_expectation = 'ON'
          reality = src.car.starter(
              key_is_close=True,
              start_is_pushed=True,
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
    :lineno-start: 15
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.car
    import unittest


    class TestCar(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.car' has no attribute 'starter'

  because ``car.py`` in the ``src`` folder_ does not have anything named ``starter`` in it

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``car.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` named ``starter`` to ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def starter():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: starter() got an unexpected keyword argument 'key_is_close'

  because the test called the ``starter`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only allows calls with 0 arguments

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_car.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add the :ref:`keyword argument<test_functions_w_keyword_arguments>` to the :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def starter(key_is_close):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: starter() got an unexpected keyword argument 'start_is_pushed'

  because the test called the ``starter`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only allows calls with 1 input

* I add ``start_is_pushed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def starter(key_is_close, start_is_pushed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'ON'

  the ``starter`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the test expects :green:`'ON'`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def starter(key_is_close, start_is_pushed):
        return 'ON'

  the test passes. The ``car`` :ref:`function<what is a function?>` always returns :green:`ON`, it does not care about the inputs. Is this :ref:`Tautology?<test_tautology>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close` and the start button is :red:`NOT pushed`, in ``test_car.py``

  ==============  =================  =================
  key             start button       output
  ==============  =================  =================
  :green:`close`  :green:`pushed`    :green:`ON`
  :green:`close`  :red:`NOT pushed`  :red:`OFF`
  ==============  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-14

        def test_starter_w_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ON' != 'OFF'

  because the ``starter`` :ref:`function<what is a function?>` returns :green:`'ON'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``starter`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def starter(key_is_close, start_is_pushed):
        if start_is_pushed == False:
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def starter(key_is_close, start_is_pushed):
        # if start_is_pushed == False:
        if not start_is_pushed == True:
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def starter(key_is_close, start_is_pushed):
        # if start_is_pushed == False:
        # if not start_is_pushed == True:
        if not start_is_pushed:
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(key_is_close, start_is_pushed):
        if not start_is_pushed:
            return 'OFF'

        return 'ON'

  this is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the start button is :red:`NOT pushed`
  - it returns :green:`'ON'` if the above condition is not met

----

*********************************************************************************
test_car_w_key_far
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter is

==============  =================  =================
key             start button       output
==============  =================  =================
:red:`far`      :green:`pushed`    :red:`OFF`
:red:`far`      :red:`NOT pushed`  :red:`OFF`
==============  =================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter and the start button is :green:`pushed`

==================  =================  =================
door                start button       output
==================  =================  =================
:red:`closed`       :green:`pushed`    :green:`HEATING`
==================  =================  =================

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 8-14

            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'ON' != 'OFF'

because the ``starter`` :ref:`function<what is a function?>` returns :green:`'ON'` and the test expects :red:`'OFF'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``car.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def starter(key_is_close, start_is_pushed):
    if key_is_close == False:
        return 'OFF'
    if not start_is_pushed:
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

    def starter(key_is_close, start_is_pushed):
        # if key_is_close == False:
        if not key_is_close == True:
            return 'OFF'
        if not start_is_pushed:
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def starter(key_is_close, start_is_pushed):
        # if key_is_close == False:
        # if not key_is_close == True:
        if not key_is_close:
            return 'OFF'
        if not start_is_pushed:
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjuncion (OR)<test_logical_disjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-7

    def starter(key_is_close, start_is_pushed):
        # if key_is_close == False:
        # if not key_is_close == True:
        # if not key_is_close:
        #     return 'OFF'
        # if not start_is_pushed:
        if not key_is_close or not start_is_pushed:
            return 'OFF'

        return 'ON'

  the test is still green

* I rewrite the statement in terms of :ref:`Logical Negation (NOT)<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-12

    def starter(key_is_close, start_is_pushed):
        # if key_is_close == False:
        # if not key_is_close == True:
        # if not key_is_close:
        #     return 'OFF'
        # if not start_is_pushed:
        # if not key_is_close or not start_is_pushed:
        if (
            (not key_is_close)
            (not and)
            (not start_is_pushed)
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I "factor" out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-13

    def starter(key_is_close, start_is_pushed):
        # if key_is_close == False:
        # if not key_is_close == True:
        # if not key_is_close:
        #     return 'OFF'
        # if not start_is_pushed:
        # if not key_is_close or not start_is_pushed:
        # if (
        #     (not key_is_close)
        #     (not and)
        #     (not start_is_pushed)
        # ):
        if not (key_is_close and start_is_pushed):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(key_is_close, start_is_pushed):
        if not (key_is_close and start_is_pushed):
            return 'OFF'

        return 'ON'

  this is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the key is :red:`far` from the starter AND the start button is :green:`pushed`
  - it returns :green:`'ON'` if the condition is not met

  is this :ref:`Logical Conjunction?<test_logical_conjunction>`

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter and the start button is :red:`NOT pushed` to :ref:`test_starter_w_key_close` in ``test_car.py``

  ==================  =================  =================
  door                start button       output
  ==================  =================  =================
  :red:`closed`       :green:`pushed`    :green:`HEATING`
  :red:`closed`       :red:`NOT pushed`  :red:`OFF`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9-13

        def test_starter_w_key_close(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

  - I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (:red:`'OFF'`)

* I make a :ref:`global variable<what is a variable?>` to remove repetition from the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.car
    import unittest


    OFF = 'OFF'


    class TestCar(unittest.TestCase):

* I use the new :ref:`global variable<what is a variable?>` to remove ``'OFF'`` from :ref:`test_starter_w_key_close`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 9, 14-15

        def test_starter_w_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_starter_w_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_starter_w_key_close(self):

* I use the new :ref:`global variable<what is a variable?>` to remove ``'OFF'`` from :ref:`test_starter_w_key_close`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2, 7-8, 14-15

        def test_starter_w_key_close(self):
            # my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)


    # Exceptions seen

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 24

        def test_starter_w_key_close(self):
            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

----

*********************************************************************************
test_starter_w_key_close_timer_set
*********************************************************************************

So far, the :ref:`truth table` for the car is

==============  =================  =================
key             start button       output
==============  =================  =================
:green:`close`  :green:`pushed`    :green:`ON`
:green:`close`  :red:`NOT pushed`  :red:`OFF`
:red:`far`      :green:`pushed`    :red:`OFF`
:red:`far`      :red:`NOT pushed`  :red:`OFF`
==============  =================  =================

I want the car to start only when the brake pedal is pressed, the inputs for the car will then be

* is the key close?
* is the brake being pressed?
* was the start button pushed?

and the :ref:`truth table` for when the key is :green:`close` and the the brake is being :green:`pressed`, will be

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`close`  :green:`set`    :green:`pushed`    :red:`OFF`
:green:`close`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ===========

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``timer_is_set`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_starter_w_key_close`, for when the key is :green:`close`, the the brake is being :green:`pressed` and the start button is :green:`pushed`

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`close`  :green:`set`    :green:`pushed`    :red:`OFF`
=============  ==============  =================  ===========

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6

      def test_starter_w_key_close(self):
          my_expectation = 'OFF'

          reality = src.car.starter(
              key_is_close=True,
              timer_is_set=True,
              start_is_pushed=True,
          )
          self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: starter() got an unexpected keyword argument 'timer_is_set'

because the test called the ``starter`` :ref:`function<what is a function?>` with 3 keyword arguments (``key_is_close``, ``timer_is_set`` and ``start_is_pushed``) and the :ref:`function<what is a function?>` only allows calls with 2 arguments (``key_is_close`` and ``start_is_pushed``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``timer_is_set`` to the :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set,
        ):
        if not key_is_close and start_is_pushed:
            return 'OFF'
        return 'OFF'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_starter_w_key_close - TypeError: starter() missing 1 required positional argument:...
    FAILED ...test_starter_w_key_close - TypeError: starter() missing 1 required positional argument:...

  because the tests call the ``starter`` :ref:`function<what is a function?>` with 2 arguments (``key_is_close`` and ``start_is_pushed``) and I just changed the :ref:`function signature<what is a function?>` to make it take 3 required arguments (``key_is_close``, ``start_is_pushed`` and ``timer_is_set``). I have to make ``timer_is_set`` a choice.

* I add a :ref:`default value<test_functions_w_default_arguments>` to make ``timer_is_set`` a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False,
        ):

  the test passes because

  .. code-block:: python

    src.car.starter(
        key_is_close=True,
        start_is_pushed=False,
    )

  is now the same as

  .. code-block:: python

    src.car.starter(
        key_is_close=True,
        start_is_pushed=False,
        timer_is_set=False,
    )

  a :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``timer_is_set`` to the next :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is being :green:`pressed` and the start button is :red:`NOT pushed`

  =============  ==============  =================  ===========
  door           timer           start button       output
  =============  ==============  =================  ===========
  :green:`close`  :green:`set`    :green:`pushed`    :red:`OFF`
  :green:`close`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  ===========

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 13

        def test_starter_w_key_close(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close(self):

  the test is still green

* I change the name of the test from :ref:`test_starter_w_key_close` to :ref:`test_starter_w_key_close_timer_set`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'

----

*********************************************************************************
test_starter_w_key_close_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the key is :green:`close` and the the brake is :red:`NOT pressed` is

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`close`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:green:`close`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ===========

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is :red:`NOT pressed` and the start button is :green:`pushed`

  =============  ==============  =================  ===========
  door           timer           start button       output
  =============  ==============  =================  ===========
  :green:`close`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
  =============  ==============  =================  ===========

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8-9, 11-16

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is :red:`NOT pressed` and the start button is :red:`NOT pushed`

  =============  ==============  =================  ===========
  door           timer           start button       output
  =============  ==============  =================  ===========
  :green:`close`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
  :green:`close`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  ===========

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 11-16

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close(self):

  green

----

*********************************************************************************
test_starter_w_key_close_timer_set
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and is the the brake is being :green:`pressed`

=============  ==============  =================  ================
door           timer           start button       output
=============  ==============  =================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ================

* I add a value for the ``timer_is_set`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_starter_w_key_close` for the case where the key is :red:`far` from the starter, the the brake is being :green:`pressed` and the start button is :green:`pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
  =============  ==============  =================  =============

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

        def test_starter_w_key_close(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I do not need to add a value for ``timer_is_set`` to the next :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is being :green:`pressed` and the start button is :red:`NOT pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  =============

  because

  .. code-block:: python

    src.car.starter(
        key_is_close=False,
        start_is_pushed=False,
    )

  is the same as

  .. code-block:: python

    src.car.starter(
        key_is_close=False,
        start_is_pushed=False,
        timer_is_set=False,
    )

  the :ref:`default value<test_functions_w_default_arguments>` for ``timer_is_set`` is :ref:`False<test_what_is_false>`

* I change the name of the test from :ref:`test_starter_w_key_close` to :ref:`test_starter_w_key_close_timer_set`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 8

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_starter_w_key_close_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the the brake is :red:`NOT pressed` is

=============  ==============  =================  ================
door           timer           start button       output
=============  ==============  =================  ================
:red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ================
----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is :red:`NOT pressed` and the start button is :green:`pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
  =============  ==============  =================  =============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7-8, 10-15

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'OFF' != 'OFF'

  because the ``starter`` :ref:`function<what is a function?>` returns :red:`'OFF'` and the test expects :red:`'OFF'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`if statement<if statements>` to the ``starter`` :ref:`function<what is a function?>` in ``car.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def starter(
          key_is_close, start_is_pushed,
          timer_is_set=False
      ):
      if timer_is_set == False:
          return 'OFF'
      if not key_is_close and start_is_pushed:
          return 'OFF'
      return 'OFF'

the test passes


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        if bool(timer_is_set) == False:
            return 'OFF'
        if not key_is_close and start_is_pushed:
            return 'OFF'
        return 'OFF'

  the test is still green

* I use :ref:`Logical Negation(NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        # if bool(timer_is_set) == False:
        if not bool(timer_is_set) == True:
            return 'OFF'
        if not key_is_close and start_is_pushed:
            return 'OFF'
        return 'OFF'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        # if bool(timer_is_set) == False:
        # if not bool(timer_is_set) == True:
        if not bool(timer_is_set):
            return 'OFF'
        if not key_is_close and start_is_pushed:
            return 'OFF'
        return 'OFF'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        # if bool(timer_is_set) == False:
        # if not bool(timer_is_set) == True:
        # if not bool(timer_is_set):
        if not timer_is_set:
            return 'OFF'
        if not key_is_close and start_is_pushed:
            return 'OFF'
        return 'OFF'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False,
        ):
        if not timer_is_set:
            return 'OFF'
        if not key_is_close and start_is_pushed:
            return 'OFF'
        return 'OFF'

  This is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the the brake is :red:`NOT pressed`
  - if the the brake is being :green:`pressed`

    * it returns :red:`'OFF'` if the key is :red:`far` from the starter AND the start button is :green:`pushed`
  - it returns :red:`'OFF'` if none of the conditions are met

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is :red:`NOT pressed` and the start button is :red:`NOT pushed`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 11-16

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

* I add another clause to the :ref:`if statement<if statements>` for when the the brake is being :green:`pressed`, in the ``starter`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False
        ):
        if not timer_is_set:
            return 'OFF'
        if (
            not key_is_close
            and start_is_pushed
            and timer_is_set
        ):
            return 'OFF'
        return 'OFF'

  the test is still green

* I remove the :ref:`if statement<if statements>` for when the the brake is :red:`NOT pressed` because I do not need it anymore

  .. code-block:: python
    :linenos:

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False
        ):
        if (
            not key_is_close
            and start_is_pushed
            and timer_is_set
        ):
            return 'OFF'
        return 'OFF'

  still green. This is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the key is :red:`far` from the starter AND the start button is :green:`pushed` AND the the brake is being :green:`pressed`
  - it returns :red:`'OFF'` in every other case

----

*********************************************************************************
test_too_hot_open_door_timer_set
*********************************************************************************

the :ref:`truth table` for the car is

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`close`  :green:`set`    :green:`pushed`    :red:`OFF`
:green:`close`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
:green:`close`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:green:`close`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ===========

=============  ==============  =================  ================
door           timer           start button       output
=============  ==============  =================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
:red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ================

I want to add a failsafe to stop the car if it gets too hot. The inputs will then be

* is the key close?
* is the brake being pressed?
* was the start button pushed?
* is the car too hot?

and the :ref:`truth table` for when the key is :green:`close` and the the brake is being :green:`pressed` will be

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`close`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`close`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`close`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`close`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``too_hot`` to the :ref:`assertion<what is an assertion?>` for the case where the key is :green:`close`, the the brake is being :green:`pressed`, the start button is :green:`pushed` and the car temperature is :green:`too hot`, to :ref:`test_starter_w_key_close_timer_set` in ``test_car.py``

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`close`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
=============  ==============  =================  ==================  ================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 8

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: starter() got an unexpected keyword argument 'too_hot'

because the test called the ``starter`` :ref:`function<what is a function?>` with 4 keyword arguments (``key_is_close``, ``timer_is_set``, ``start_is_pushed`` and ``too_hot``) and the definition only allows calls with 2 required arguments (``key_is_close`` and ``start_is_pushed``) and 1 optional argument (``timer_is_set``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``too_hot`` to the ``car`` :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False, too_hot,
        ):
        if not key_is_close and start_is_pushed and timer_is_set:
            return 'OFF'
        return 'OFF'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``too_hot`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def starter(
            key_is_close, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is being :green:`pressed`, the start button is :green:`pushed` and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`close`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 12-18

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add a value for the ``too_hot`` parameter in the next :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is being :green:`pressed`, the start button is :red:`NOT pushed` and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`close`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`close`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 24

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_not_set(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is being :green:`pressed`, the start button is :red:`NOT pushed` and the car temperature is  :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`close`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`close`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  :green:`close`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 28-34

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_not_set(self):

  green

* I change the name of the test from :ref:`test_starter_w_key_close_timer_set` to :ref:`test_too_hot_open_door_timer_set`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_too_hot_open_door_timer_set(self):
            my_expectation = 'OFF'

* I add a :ref:`global variable<what is a variable?>` for :red:`'OFF'`. I want to use it to remove repetition from the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.car
    import unittest


    OFF = 'OFF'


    class TestCar(unittest.TestCase):

        def test_too_hot_open_door_timer_set(self):

* I use the :ref:`global variable<what is a variable?>` for ``my_expectation`` in :ref:`test_too_hot_open_door_timer_set`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 10-11, 19-20, 28-29, 37-38

        def test_too_hot_open_door_timer_set(self):
            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I remove the ``reality`` :ref:`variables<what is a variable?>`, I do not need them because they are called only once in every :ref:`assertion<what is an assertion?>`, I can call the ``starter`` :ref:`function<what is a function?>` directly without the middle man

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 11-20, 29-38, 46-56, 65-74

        def test_too_hot_open_door_timer_set(self):
            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 10

        def test_too_hot_open_door_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_starter_w_key_close_timer_not_set(self):

----

*********************************************************************************
test_too_hot_open_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the key is :green:`close` and the the brake is :red:`NOT pressed` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`close`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`close`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`close`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`close`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_starter_w_key_close_timer_not_set` for when the key is :green:`close`, the the brake is :red:`NOT pressed`, the start button is :green:`pushed` and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is :red:`NOT pressed`, the start button is :green:`pushed` and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`close`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-18

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_set(self):

  the test is still green

* I add a value for ``too_hot`` to the next :ref:`assertion<what is an assertion?>`, for when the key is :green:`close`, the the brake is :red:`NOT pressed`, the start button is :red:`NOT pushed` and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`close`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`close`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 24

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_set(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the the brake is :red:`NOT pressed`, the start button is :red:`NOT pushed` and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`close`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`close`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`close`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  :green:`close`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 28-34

        def test_starter_w_key_close_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_starter_w_key_close_timer_set(self):

  green

* I change the name of the test from :ref:`test_starter_w_key_close_timer_not_set` to :ref:`test_too_hot_open_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_open_door_timer_not_set(self):
            my_expectation = 'OFF'

* I use the ``OFF`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_too_hot_open_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2, 10-11, 19-20, 28-29, 37-38

        def test_too_hot_open_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I call the ``starter`` :ref:`function<what is a function?>` directly in the :ref:`assertion<what is an assertion?>` because I only use the ``reality`` :ref:`variable<what is a variable?>` once for each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 11-19, 28-36, 45-53, 62-70

        def test_too_hot_open_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 51

        def test_too_hot_open_door_timer_not_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_starter_w_key_close_timer_set(self):

----

*********************************************************************************
test_too_hot_closed_door_timer_set
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the the brake is being :green:`pressed` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I use the ``OFF`` :ref:`global variable<what is a variable?>` for ``my_expectation`` when the value is :red:`'OFF'` in :ref:`test_starter_w_key_close_timer_set`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 10, 16-17

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  the test is still green

* I call the ``starter`` :ref:`function<what is a function?>` directly without the ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 8-15, 24-30

        def test_starter_w_key_close_timer_set(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                ),
                'OFF'
            )

            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    start_is_pushed=False,
                ),
                OFF
            )

  still green

* I remove the commented lines and :ref:`variables<what is a variable?>` that are not used anymore

  .. code-block:: python
    :lineno-start: 92

        def test_starter_w_key_close_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                ),
                'OFF'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    start_is_pushed=False,
                ),
                OFF
            )

        def test_starter_w_key_close_timer_not_set(self):

* I add a value for the ``too_hot`` and ``timer_is_set`` parameters in the second :ref:`assertion<what is an assertion?>`, for when the key is :red:`far` from the starter, the the brake is being :green:`pressed`, the start button is :green:`pushed`, and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 14, 16

        def test_starter_w_key_close_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                ),
                'OFF'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

  green

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>`, for when the key is :red:`far` from the starter, the the brake is being :green:`pressed`, the start button is :green:`pushed` and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 7

        def test_starter_w_key_close_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'OFF'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is being :green:`pressed`, the start button is :red:`NOT pushed`, and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 22-30

        def test_starter_w_key_close_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'OFF'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is being :green:`pressed`, the start button is :red:`NOT pushed`, and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 32-40

        def test_starter_w_key_close_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'OFF'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_starter_w_key_close_timer_not_set(self):

  the test is still green

* I change the name of the test from :ref:`test_starter_w_key_close_timer_set` to :ref:`test_too_hot_closed_door_timer_set`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_closed_door_timer_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'OFF'
            )

----

*********************************************************************************
test_too_hot_closed_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the the brake is :red:`NOT pressed` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I use the ``OFF`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_starter_w_key_close_timer_not_set`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 2, 9-10, 17-18

        def test_starter_w_key_close_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I call the ``starter`` :ref:`function<what is a function?>` directly in the :ref:`assertion<what is an assertion?>`, I do not need the ``reality`` :ref:`variables<what is a variable?>` because they are only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 10-17, 25-32

        def test_starter_w_key_close_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )

* I remove the commented lines and :ref:`variables<what is a variable?>` that are not used

  .. code-block:: python
    :lineno-start: 133

        def test_starter_w_key_close_timer_not_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )


    # Exceptions seen

* I change the name of the test from :ref:`test_starter_w_key_close_timer_not_set` to :ref:`test_too_hot_closed_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 11

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_too_hot_closed_door_timer_not_set`, for when the key is :red:`far` from the starter, the the brake is :red:`NOT pressed`, the start button is :green:`pushed`, and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 7

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is :red:`NOT pressed`, the start button is :green:`pushed`, and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 12-20

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )

  still green

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the key is :red:`far` from the starter, the the brake is :red:`NOT pressed`, the start button is :red:`NOT pushed`, and the car temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 22-30

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

  green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the the brake is :red:`NOT pressed`, the start button is :red:`NOT pushed`, and the car temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 32-40

          def test_too_hot_closed_door_timer_not_set(self):
              self.assertEqual(
                  src.car.starter(
                      key_is_close=False,
                      timer_is_set=False,
                      start_is_pushed=True,
                      too_hot=True,
                  ),
                  OFF
              )

              self.assertEqual(
                  src.car.starter(
                      key_is_close=False,
                      timer_is_set=False,
                      start_is_pushed=True,
                      too_hot=False,
                  ),
                  OFF
              )

              self.assertEqual(
                  src.car.starter(
                      key_is_close=False,
                      timer_is_set=False,
                      start_is_pushed=False,
                      too_hot=True,
                  ),
                  OFF
              )

              self.assertEqual(
                  src.car.starter(
                      key_is_close=False,
                      timer_is_set=False,
                      start_is_pushed=False,
                      too_hot=False,
                  ),
                  OFF
              )


      # Exceptions seen

  all the tests are still green

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_car.py`` and ``car.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``car``

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

I ran tests for a car with these inputs:

* is the key close?
* is the brake being pressed?
* was the start button pushed?
* is the car too hot?

the inputs gave me this :ref:`truth table`

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`close`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`close`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`close`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`close`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`close`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`close`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`close`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`close`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

the only time this car heats food is when the door is :green:`closed`, the the brake is being :green:`pressed`, the start button is :green:`pushed` and the car temperature is :red:`NOT too hot`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<car: tests and solutions>`

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