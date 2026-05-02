.. meta::
  :description: Learn Python and Test-Driven Development (TDD) by building a safety-critical car ignition system. This beginner project uses truth tables to manage multiple boolean inputs—proximity keys, brake pedals, and transmission park failsafes—while teaching the Red-Green-Refactor cycle using uv, pytest-watcher, and common Python exceptions.
  :keywords: Python car ignition logic tutorial, TDD car starter project, truth table to python code, multiple boolean inputs python example, red green refactor for beginners, uv python project management, pytest-watcher automated testing, proximity key ignition logic, brake pedal safety check code, transmission in park failsafe, troubleshooting TypeError in python tests, AssertionError vs AttributeError python, Jacob Itegboje

.. include:: ../../links.rst

.. _car:

#################################################################################
Car
#################################################################################

I want to make a **Car** that can be turned on with the push of a button, if the inputs are

* is the key close to the starter?
* was the start button pressed?

this is the :ref:`truth table` I get for the Car Starter

==============  ==================  =================
key             start button        output
==============  ==================  =================
:green:`close`  :green:`pressed`    :green:`ON`
:green:`close`  :red:`NOT pressed`  :red:`OFF`
:red:`far`      :green:`pressed`    :red:`OFF`
:red:`far`      :red:`NOT pressed`  :red:`OFF`
==============  ==================  =================

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

    ======================== FAILURES ========================
    _________________ TestCar.test_failure ___________________

    self = <tests.test_car.TestCar testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_car.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_car.py::TestCar::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

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
test_key_close
*********************************************************************************

The :ref:`truth table` for when the key is :green:`close` to the starter is

==============  ==================  =================
key             start button        output
==============  ==================  =================
:green:`close`  :green:`pressed`    :green:`ON`
:green:`close`  :red:`NOT pressed`  :red:`OFF`
==============  ==================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_key_close``, then add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close` and the start button is :green:`pressed`

==============  ==================  =================
key             start button        output
==============  ==================  =================
:green:`close`  :green:`pressed`    :green:`ON`
==============  ==================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestCar(unittest.TestCase):

      def test_key_close(self):
          my_expectation = 'ON'
          reality = src.car.starter(
              key_is_close=True,
              start_is_pressed=True,
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

  .. admonition:: If you get :ref:`ModuleNotFoundError<what is a module?>`

    .. code-block:: python

      ModuleNotFoundError: No module named 'src'

    check if you have ``__init__.py`` in the ``tests`` folder_ with underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

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

  because the test called the ``starter`` :ref:`function<what is a function?>` with 2 keyword arguments (``key_is_close`` and ``start_is_pressed``) and this definition only allows calls with 0 arguments

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

    TypeError: starter() got an unexpected keyword argument 'start_is_pressed'

  because the test called the ``starter`` :ref:`function<what is a function?>` with 2 keyword arguments (``key_is_close`` and ``start_is_pressed``) and this definition only allows calls with 1 input

* I add ``start_is_pressed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def starter(key_is_close, start_is_pressed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'ON'

  the ``starter`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the test expects :green:`'ON'`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def starter(key_is_close, start_is_pressed):
        return 'ON'

  the test passes. The ``starter`` :ref:`function<what is a function?>` always returns :green:`ON`, it does not care about the inputs. Is this :ref:`Tautology?<test_tautology>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close` and the start button is :red:`NOT pressed`, in ``test_car.py``

  ==============  ==================  =================
  key             start               output
  ==============  ==================  =================
  :green:`close`  :green:`pressed`    :green:`ON`
  :green:`close`  :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-14

        def test_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=False,
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

    def starter(key_is_close, start_is_pressed):
        if start_is_pressed == False:
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def starter(key_is_close, start_is_pressed):
        # if start_is_pressed == False:
        if not start_is_pressed == True:
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def starter(key_is_close, start_is_pressed):
        # if start_is_pressed == False:
        # if not start_is_pressed == True:
        if not start_is_pressed:
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(key_is_close, start_is_pressed):
        if not start_is_pressed:
            return 'OFF'

        return 'ON'

  this is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the start button is :red:`NOT pressed`
  - it returns :green:`'ON'` if the above condition is not met

----

*********************************************************************************
test_key_far
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter is

==============  ==================  ==========
key             start               output
==============  ==================  ==========
:red:`far`      :green:`pressed`    :red:`OFF`
:red:`far`      :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==========

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter and the start button is :green:`pressed`, in ``test_car.py``

==============  ==================  ==========
key             start               output
==============  ==================  ==========
:red:`far`      :green:`pressed`    :red:`OFF`
==============  ==================  ==========

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 8-14

            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_key_far(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=True,
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

  def starter(key_is_close, start_is_pressed):
      if key_is_close == False:
          return 'OFF'

      if not start_is_pressed:
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

    def starter(key_is_close, start_is_pressed):
        # if key_is_close == False:
        if not key_is_close == True:
            return 'OFF'

        if not start_is_pressed:
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def starter(key_is_close, start_is_pressed):
        # if key_is_close == False:
        # if not key_is_close == True:
        if not key_is_close:
            return 'OFF'

        if not start_is_pressed:
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the two :ref:`if statements` together because they both return the same thing (``'OFF'``)

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 7-8

    def starter(key_is_close, start_is_pressed):
        # if key_is_close == False:
        # if not key_is_close == True:
        # if not key_is_close:
        #     return 'OFF'

        # if not start_is_pressed:
        if not key_is_close or not start_is_pressed:
            return 'OFF'

        return 'ON'

  the test is still green

* I rewrite the statement in terms of :ref:`Logical Negation (NOT)<test_logical_negation>` because it happens two times

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-12

    def starter(key_is_close, start_is_pressed):
        # if key_is_close == False:
        # if not key_is_close == True:
        # if not key_is_close:
        #     return 'OFF'
        # if not start_is_pressed:
        # if not key_is_close or not start_is_pressed:
        if (
            (not key_is_close)
            (not and)
            (not start_is_pressed)
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_car.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I "factor" out the :ref:`nots<test_logical_negation>` in the ``starter`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-13

    def starter(key_is_close, start_is_pressed):
        # if key_is_close == False:
        # if not key_is_close == True:
        # if not key_is_close:
        #     return 'OFF'
        # if not start_is_pressed:
        # if not key_is_close or not start_is_pressed:
        # if (
        #     (not key_is_close)
        #     (not and)
        #     (not start_is_pressed)
        # ):
        if not (key_is_close and start_is_pressed):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(key_is_close, start_is_pressed):
        if not (key_is_close and start_is_pressed):
            return 'OFF'

        return 'ON'

  this is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the key is :red:`far` from the starter OR the start button is :red:`NOT pressed`
  - it returns :green:`'ON'` if the above conditions are not met

  is this :ref:`Logical Conjunction?<test_logical_conjunction>`

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter and the start button is :red:`NOT pressed` to :ref:`test_key_far` in ``test_car.py``

  ==============  ==================  ==========
  key             start               output
  ==============  ==================  ==========
  :red:`far`      :green:`pressed`    :red:`OFF`
  :red:`far`      :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  ==========

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9-13

        def test_key_far(self):
            my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=False,
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

  this way all the tests can use the same :ref:`global variable<what is a variable?>` and I do not have to make one for each test

* I use the new :ref:`global variable<what is a variable?>` to remove ``'OFF'`` from :ref:`test_key_close`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 9, 14-15

        def test_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_far(self):

* I use the new :ref:`global variable<what is a variable?>` to remove ``'OFF'`` from :ref:`test_key_far`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2, 7-8, 14-15

        def test_key_far(self):
            # my_expectation = 'OFF'
            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)


    # Exceptions seen

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 24

        def test_key_far(self):
            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

----

*********************************************************************************
test_key_close_brake_pressed
*********************************************************************************

So far, the :ref:`truth table` for the car starter is

==============  ==================  =================
key             start button        output
==============  ==================  =================
:green:`close`  :green:`pressed`    :green:`ON`
:green:`close`  :red:`NOT pressed`  :red:`OFF`
:red:`far`      :green:`pressed`    :red:`OFF`
:red:`far`      :red:`NOT pressed`  :red:`OFF`
==============  ==================  =================

I want the car to start only when the brake pedal is pressed, the inputs for the car will then be

* is the key close to the starter?
* is the brake being pressed?
* was the start button pressed?

and the :ref:`truth table` for when the key is :green:`close` and the brake is being :green:`pressed`, is:

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:green:`close`  :green:`pressed`    :green:`pressed`    :green:`ON`
:green:`close`  :green:`pressed`    :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``brake_is_pressed`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_key_close`, for when the key is :green:`close`, the brake is being :green:`pressed` and the start button is :green:`pressed`

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:green:`close`  :green:`pressed`    :green:`pressed`    :green:`ON`
==============  ==================  ==================  ===========


.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 5

      def test_key_close(self):
          my_expectation = 'ON'
          reality = src.car.starter(
              key_is_close=True,
              brake_is_pressed=True,
              start_is_pressed=True,
          )
          self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: shell

  TypeError: starter() got an unexpected keyword argument 'brake_is_pressed'. Did you mean 'start_is_pressed'?

because the test called the ``starter`` :ref:`function<what is a function?>` with 3 keyword arguments (``key_is_close``, ``brake_is_pressed`` and ``start_is_pressed``) and the :ref:`function<what is a function?>` only allows calls with 2 arguments (``key_is_close`` and ``start_is_pressed``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``brake_is_pressed`` to the :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed,
        ):
        if not (key_is_close and start_is_pressed):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_key_close - TypeError: starter() missing 1 required positional argument: 'brake_is_pressed'
    FAILED ...test_key_far - TypeError: starter() missing 1 required positional argument: 'brake_is_pressed'

  because the tests call the ``starter`` :ref:`function<what is a function?>` with 2 arguments (``key_is_close`` and ``start_is_pressed``) and I just changed the :ref:`function signature<what is a function?>` to make it take 3 required arguments (``key_is_close``, ``start_is_pressed`` and ``brake_is_pressed``). I have to make ``brake_is_pressed`` a choice.

* I add a :ref:`default value<test_functions_w_default_arguments>` to make ``brake_is_pressed`` a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):

  the test passes because

  .. code-block:: python

    src.car.starter(
        key_is_close=True,
        start_is_pressed=False,
    )

  is now the same as

  .. code-block:: python

    src.car.starter(
        key_is_close=True,
        start_is_pressed=False,
        brake_is_pressed=False,
    )

  a :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``brake_is_pressed`` to the next :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is being :green:`pressed` and the start button is :red:`NOT pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :green:`close`  :green:`pressed`    :green:`pressed`    :green:`ON`
  :green:`close`  :green:`pressed`    :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 12

        def test_key_close(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_far(self):

  the test is still green

* I change the name of the test from :ref:`test_key_close` to :ref:`test_key_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_key_close_brake_pressed(self):
            my_expectation = 'OFF'

----

*********************************************************************************
test_key_close_brake_not_pressed
*********************************************************************************

The :ref:`truth table` for when the key is :green:`close` and the brake is :red:`NOT pressed` is

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is :red:`NOT pressed` and the start button is :green:`pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8-14

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_close_brake_not_pressed(self):
            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

        def test_key_far(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ON' != 'OFF'

  because the ``starter`` :ref:`function<what is a function?>` returned :green:`'ON'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``starter`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        if brake_is_pressed == False:
            return 'OFF'

        if not (key_is_close and start_is_pressed):
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the new :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        # if brake_is_pressed == False:
        if not brake_is_pressed == True:
            return 'OFF'

        if not (key_is_close and start_is_pressed):
            return 'OFF'

        return 'ON'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        # if brake_is_pressed == False:
        # if not brake_is_pressed == True:
        if not brake_is_pressed:
            return 'OFF'

        if not (key_is_close and start_is_pressed):
            return 'OFF'

        return 'ON'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjunction<test_logical_disjunction>` to put the two :ref:`if statements` together because they return the same thing

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-15

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        # if brake_is_pressed == False:
        # if not brake_is_pressed == True:
        # if not brake_is_pressed:
        #     return 'OFF'

        # if not (key_is_close and start_is_pressed):
        if (
            not (key_is_close and start_is_pressed)
            or
            not brake_is_pressed
        ):
            return 'OFF'

        return 'ON'

  green

* I write the statement in terms of :ref:`NOT<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-20

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        # if brake_is_pressed == False:
        # if not brake_is_pressed == True:
        # if not brake_is_pressed:
        #     return 'OFF'

        # if not (key_is_close and start_is_pressed):
        # if (
        #     not (key_is_close and start_is_pressed)
        #     or
        #     not brake_is_pressed
        # ):
        if (
            (not (key_is_close and start_is_pressed))
            (not and)
            (not brake_is_pressed)
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

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        # if brake_is_pressed == False:
        # if not brake_is_pressed == True:
        # if not brake_is_pressed:
        #     return 'OFF'

        # if not (key_is_close and start_is_pressed):
        # if (
        #     not (key_is_close and start_is_pressed)
        #     or
        #     not brake_is_pressed
        # ):
        # if (
        #     (not (key_is_close and start_is_pressed))
        #     (not and)
        #     (not brake_is_pressed)
        # ):
        if not (
            (key_is_close and start_is_pressed)
            and
            (brake_is_pressed)
        ):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False,
        ):
        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
        ):
            return 'OFF'

        return 'ON'

  this is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the key is :red:`far` from the starter OR the start button is :red:`NOT pressed` OR the brake is :red:`NOT pressed`
  - it returns :green:`'ON'` if none of the conditions are met

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is :red:`NOT pressed` and the start button is :red:`NOT pressed`, in :ref:`test_key_close_brake_not_pressed` in ``test_car.py``

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 9-14

        def test_key_close_brake_not_pressed(self):
            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_far(self):

  the test is still green

----

*********************************************************************************
test_key_far_brake_pressed
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the brake is being :green:`pressed`, is:

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:red:`far`      :green:`pressed`    :green:`pressed`    :red:`OFF`
:red:`far`      :green:`pressed`    :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

* I add a value for the ``brake_is_pressed`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_key_close` for the case where the key is :red:`far` from the starter, the brake is being :green:`pressed` and the start button is :green:`pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :red:`far`      :green:`pressed`    :green:`pressed`    :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 11

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_far(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

  the test is still green

* I add a value for ``brake_is_pressed`` to the next :ref:`assertion<what is an assertion?>`, for when the key is :red:`far` from the starter, the brake is being :green:`pressed` and the start button is :red:`NOT pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :red:`far`      :green:`pressed`    :green:`pressed`    :red:`OFF`
  :red:`far`      :green:`pressed`    :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 11

        def test_key_far(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green

* I change the name of the test from :ref:`test_key_far` to :ref:`test_key_far_brake_pressed`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 8

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_far_brake_pressed(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

----

*********************************************************************************
test_key_far_brake_not_pressed
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the brake is :red:`NOT pressed` is

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:red:`far`      :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
:red:`far`      :red:`NOT pressed`  :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is :red:`NOT pressed` and the start button is :green:`pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :red:`far`      :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 8-14

            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)

        def test_key_far_brake_not_pressed(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is :red:`NOT pressed` and the start button is :red:`NOT pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :red:`far`      :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
  :red:`far`      :red:`NOT pressed`  :red:`NOT pressed`  :red:`OFF`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 9-14

        def test_key_far_brake_not_pressed(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green

* I call the ``starter`` :ref:`function<what is a function?>` directly in :ref:`test_key_far_brake_not_pressed`, I do not need the ``reality`` :ref:`variable<what is a variable?>` because it is only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7-15, 22-30

        def test_key_far_brake_not_pressed(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

  the test is still green

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 56

        def test_key_far_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )


    # Exceptions seen

* I do the same thing in :ref:`test_key_far_brake_pressed`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 7-15, 22-30

        def test_key_far_brake_pressed(self):
            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                    src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_far_brake_not_pressed(self):

  still green

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_key_far_brake_pressed`

  .. code-block:: python
    :lineno-start: 41

        def test_key_far_brake_pressed(self):
            self.assertEqual(
                    src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_far_brake_not_pressed(self):

* on to :ref:`test_key_close_brake_not_pressed`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 7-15, 22-30

        def test_key_close_brake_not_pressed(self):
            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_far_brake_pressed(self):

  green

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_key_close_brake_not_pressed`

  .. code-block:: python
    :lineno-start: 26

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_far_brake_pressed(self):

* I call the ``starter`` :ref:`function<what is a function?>` directly in :ref:`test_key_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8-16, 23-31

        def test_key_close_brake_pressed(self):
            my_expectation = 'ON'
            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                'ON'
            )

            reality = src.car.starter(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

  still green

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_key_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 10

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

----

*********************************************************************************
test_key_close_brake_pressed_w_gear
*********************************************************************************

the :ref:`truth table` for the car starter is

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:green:`close`  :green:`pressed`    :green:`pressed`    :green:`ON`
:green:`close`  :green:`pressed`    :red:`NOT pressed`  :red:`OFF`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:red:`far`      :green:`pressed`    :green:`pressed`    :red:`OFF`
:red:`far`      :green:`pressed`    :red:`NOT pressed`  :red:`OFF`
:red:`far`      :red:`NOT pressed`  :green:`pressed`    :red:`OFF`
:red:`far`      :red:`NOT pressed`  :red:`NOT pressed`  :red:`OFF`
==============  ==================  ==================  ===========

I want to make sure the car is in park before it can start, so it does not immediately move when it is turned on (that would be a problem). The inputs will then be

* is the key close to the starter?
* is the brake being pressed?
* was the start button pressed?
* is the gear in park?

and the :ref:`truth table` for when the key is :green:`close` and the brake is being :green:`pressed`, is:

==============  ================  ==================  ==================  ================
key             brake             start button        gear                output
==============  ================  ==================  ==================  ================
:green:`close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`ON`
:green:`close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:green:`close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:green:`close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==============  ================  ==================  ==================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``in_park`` to the :ref:`assertion<what is an assertion?>` for the case where the key is :green:`close`, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :green:`in park`, to :ref:`test_key_close_brake_pressed`

==============  ================  ==================  ==================  ================
key             brake             start button        gear                output
==============  ================  ==================  ==================  ================
:green:`close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`ON`
==============  ================  ==================  ==================  ================

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 7

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                'ON'
            )

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: starter() got an unexpected keyword argument 'in_park'

because the test called the ``starter`` :ref:`function<what is a function?>` with 4 keyword arguments (``key_is_close``, ``brake_is_pressed``, ``start_is_pressed`` and ``in_park``) and the definition only allows calls with 2 required arguments (``key_is_close`` and ``start_is_pressed``) and 1 optional argument (``brake_is_pressed``)

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

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``in_park`` to the ``starter`` :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park,
        ):
        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``in_park`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def starter(
        key_is_close, start_is_pressed,
        brake_is_pressed=False, in_park=False,
    ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :red:`NOT in park`

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`ON`
  :green:`close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12-20

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ON' != 'OFF'

  because the ``starter`` :ref:`function<what is a function?>` returns :green:`'ON'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``starter`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park=False,
        ):
        if in_park == False:
            return 'OFF'

        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
        ):
            return 'OFF'

        return 'ON'

  the test passes

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

        # if in_park == False:
        if not in_park == True:
            return 'OFF'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

        # if in_park == False:
        # if not in_park == True:
        if not in_park:
            return 'OFF'

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the two :ref:`if statements` together because they both return :red:`'OFF'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-21

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park=False,
        ):
        # if in_park == False:
        # if not in_park == True:
        # if not in_park:
        #     return 'OFF'

        # if not (
        #     key_is_close
        #     and start_is_pressed
        #     and brake_is_pressed
        # ):
        if (
            not (
                key_is_close
                and start_is_pressed
                and brake_is_pressed
            ) or not in_park
        ):
            return 'OFF'

        return 'ON'

  that is one long confusing statement

* I write the new :ref:`if statement<if statements>` in terms of :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-21

        # if not (
        #     key_is_close
        #     and start_is_pressed
        #     and brake_is_pressed
        # ):
        # if (
        #     not (
        #         key_is_close
        #         and start_is_pressed
        #         and brake_is_pressed
        #     ) or not in_park
        # ):
        if (
            (not (
                key_is_close
                and start_is_pressed
                and brake_is_pressed
            ))
            (not and)
            (not in_park)
        ):
            return 'OFF'

        return 'ON'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I factor out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 13-30

        # if not (
        #     key_is_close
        #     and start_is_pressed
        #     and brake_is_pressed
        # ):
        # if (
        #     not (
        #         key_is_close
        #         and start_is_pressed
        #         and brake_is_pressed
        #     ) or not in_park
        # ):
        # if (
        #     (not (
        #         key_is_close
        #         and start_is_pressed
        #         and brake_is_pressed
        #     ))
        #     (not and)
        #     (not in_park)
        # ):
        if not (
            (
                key_is_close
                and start_is_pressed
                and brake_is_pressed
            )
            and
            in_park
        ):
            return 'OFF'

        return 'ON'

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def starter(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park=False,
        ):
        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
            and in_park
        ):
            return 'OFF'

        return 'ON'

  this is what happens when the ``starter`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the key is :red:`far` from the starter OR the start button is :red:`NOT pressed` OR the brake is :red:`NOT pressed` OR the car gear is :red:`NOT in park`
  - it returns :green:`'ON'` if none of the conditions are met

* I add a value for the ``in_park`` parameter in the next :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is being :green:`pressed`, the start button is :red:`NOT pressed` and the car gear is :green:`in park`, in :ref:`test_key_close_brake_pressed` in ``test_car.py``

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`ON`
  :green:`close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :green:`close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 27

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is being :green:`pressed`, the start button is :red:`NOT pressed` and the car gear is  :red:`NOT in park`

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`ON`
  :green:`close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :green:`close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  :green:`close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 32-40

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                'ON'
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

  green

* I change the name of the test from :ref:`test_key_close_brake_pressed` to :ref:`test_key_close_brake_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_key_close_brake_pressed_w_gear(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                'ON'
            )

----

*********************************************************************************
test_key_close_brake_not_pressed_w_gear
*********************************************************************************

The :ref:`truth table` for when the key is :green:`close` and the brake is :red:`NOT pressed` is

==============  ==================  ==================  ==================  ==========
key             brake               start               gear                output
==============  ==================  ==================  ==================  ==========
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==============  ==================  ==================  ==================  ==========

* I add a value for the ``in_park`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_key_close_brake_not_pressed` for when the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :green:`pressed` and the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 7

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :green:`pressed` and the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-20

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_far_brake_pressed(self):

  the test is still green

* I add a value for ``in_park`` to the next :ref:`assertion<what is an assertion?>`, for when the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed` and the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 27

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

        def test_key_far_brake_pressed(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed` and the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  :green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 32-40

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_far_brake_pressed(self):

  green

* I change the name of the test from :ref:`test_key_close_brake_not_pressed` to :ref:`test_key_close_brake_not_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed_w_gear(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

----

*********************************************************************************
test_key_far_brake_pressed_w_gear
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the brake is being :green:`pressed` is

==========  ================  ==================  ==================  ==========
key         brake             start               gear                output
==========  ================  ==================  ==================  ==========
:red:`far`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
:red:`far`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:red:`far`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:red:`far`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==========  ================  ==================  ==================  ==========

* I add a value for the ``in_park`` parameter in the first :ref:`assertion<what is an assertion?>` of :ref:`test_key_far_brake_pressed`, for when the key is :red:`far` from the starter, the brake is being :green:`pressed`, the start button is :green:`pressed`, and the car gear is :green:`in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`far`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 7

        def test_key_far_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :red:`NOT in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`far`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :red:`far`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 12-20

        def test_key_far_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_far_brake_not_pressed(self):

  still green

* I add a value for the ``in_park`` parameter to the next :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is being :green:`pressed`, the start button is :red:`NOT pressed`, and the car gear is :green:`in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`far`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :red:`far`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :red:`far`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 27

        def test_key_far_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

        def test_key_far_brake_not_pressed(self):

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is being :green:`pressed`, the start button is :red:`NOT pressed`, and the car gear is :red:`NOT in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`far`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :red:`far`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :red:`far`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  :red:`far`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 32-40

        def test_key_far_brake_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_far_brake_not_pressed(self):

  still green

* I change the name of the test from :ref:`test_key_far_brake_pressed` to :ref:`test_key_far_brake_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.car.starter(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_far_brake_pressed_w_gear(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

----

*********************************************************************************
test_key_far_brake_not_pressed_w_gear
*********************************************************************************

The :ref:`truth table` for when the key is :red:`far` from the starter and the brake is :red:`NOT pressed` is

==========  ==================  ==================  ==================  ==========
key         brake               start               gear                output
==========  ==================  ==================  ==================  ==========
:red:`far`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
:red:`far`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==========  ==================  ==================  ==================  ==========

* I add a value for the ``in_park`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_key_far_brake_not_pressed`, for when the key is :red:`far` from the starter, the brake is :red:`NOT pressed`, the start button is :green:`pressed`, and the car gear is :green:`in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7

        def test_key_far_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is :red:`NOT pressed`, the start button is :green:`pressed`, and the car gear is :red:`NOT in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 12-20

        def test_key_far_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )


    # Exceptions seen

  still green

* I add a value for the ``in_park`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the key is :red:`far` from the starter, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed`, and the car gear is :green:`in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 27

        def test_key_far_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

  green

* I add an :ref:`assertion<what is an assertion?>` for when the key is :red:`far` from the starter, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed`, and the car gear is :red:`NOT in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
  :red:`far`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
  :red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
  :red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 32-40

        def test_key_far_brake_not_pressed(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )


    # Exceptions seen

  all the tests are still green

* I change the name of the test from :ref:`test_key_far_brake_not_pressed` to :ref:`test_key_far_brake_not_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 11

            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_far_brake_not_pressed_w_gear(self):
            self.assertEqual(
                src.car.starter(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

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

* is the key close to the starter?
* is the brake being pressed?
* was the start button pressed?
* is the car in park?

the inputs gave me this :ref:`truth table`

==============  ================  ==================  ==================  ================
key             brake             start button        gear                output
==============  ================  ==================  ==================  ================
:green:`close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`ON`
:green:`close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:green:`close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:green:`close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==============  ================  ==================  ==================  ================

==============  ==================  ==================  ==================  ==========
key             brake               start               gear                output
==============  ==================  ==================  ==================  ==========
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==============  ==================  ==================  ==================  ==========

==========  ================  ==================  ==================  ==========
key         brake             start               gear                output
==========  ================  ==================  ==================  ==========
:red:`far`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
:red:`far`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:red:`far`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:red:`far`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==========  ================  ==================  ==================  ==========

==========  ==================  ==================  ==================  ==========
key         brake               start               gear                output
==========  ==================  ==================  ==================  ==========
:red:`far`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`OFF`
:red:`far`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`OFF`
:red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`OFF`
:red:`far`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`OFF`
==========  ==================  ==================  ==================  ==========

the only time I can start this car is when the key is :green:`close` to the starter, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :green:`in park`.

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