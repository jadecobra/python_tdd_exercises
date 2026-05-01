.. meta::
  :description: Build a safety-critical Microwave logic system in Python using truth tables and TDD. This beginner tutorial teaches how to manage multiple boolean inputs—door status, timers, and too_hot failsafes—while writing clean, verified code.
  :keywords: Python microwave logic project, safety-critical systems python tutorial, TDD python microwave example, how to code a microwave in python, python multiple boolean inputs tutorial, red green refactor examples, python truth table practice, learn Converse NonImplication python, uv python project management, pytest-watcher logic testing, Jacob Itegboje

.. include:: ../../links.rst

.. _microwave:

#################################################################################
Microwave
#################################################################################

I want to make a **Microwave** that heats up food, if the inputs are

* is the door open?
* was the start button pushed?

this is the :ref:`truth table` I get

==================  =================  =================
door                start button       output
==================  =================  =================
:green:`open`       :green:`pushed`    :red:`OFF`
:green:`open`       :red:`NOT pushed`  :red:`OFF`
:red:`closed`       :green:`pushed`    :green:`HEATING`
:red:`closed`       :red:`NOT pushed`  :red:`OFF`
==================  =================  =================

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_microwave.py
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

* I name this project ``microwave``
* I open a terminal_
* I use uv_ to make a directory_ for the project

  .. code-block:: python
    :emphasize-lines: 1

    uv init microwave

  the terminal_ shows

  .. code-block:: shell

    Initialized project `microwave` at `.../pumping_python/microwave`

  then goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd microwave

  the terminal_ shows I am in the ``microwave`` folder_

  .. code-block:: shell

    .../pumping_python/microwave

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

        touch src/microwave.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/microwave.py

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

        touch tests/test_microwave.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_microwave.py

  the terminal_ goes back to the command line

* I open ``test_microwave.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_microwave.py

    `Visual Studio Code`_ opens ``test_microwave.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestMicrowave(unittest.TestCase):

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
    │   └── microwave.py
    ├── tests
    │   ├── __init__.py
    │   └── test_microwave.py
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
    ______________________ TestMicrowave.test_failure ________________________

    self = <tests.test_microwave.TestMicrowave testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_microwave.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_microwave.py::TestMicrowave::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

  because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` have 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors then try to run ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_microwave.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestMicrowave(unittest.TestCase):

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
test_open_door
*********************************************************************************

The :ref:`truth table` for if the door is :green:`open` is

==================  =================  =================
door                start button       output
==================  =================  =================
:green:`open`       :green:`pushed`    :red:`OFF`
:green:`open`       :red:`NOT pushed`  :red:`OFF`
==================  =================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_open_door``, then add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open` and the start button is :green:`pushed`

==================  =================  =================
door                start button       output
==================  =================  =================
:green:`open`       :green:`start`     :red:`OFF`
==================  =================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-4, 6-10

  class TestMicrowave(unittest.TestCase):

      def test_open_door(self):
          my_expectation = 'OFF'

          reality = src.microwave.microwave(
              door_is_open=True,
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
    :lineno-start: 16
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_ so that I can test ``microwave.py`` from the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.microwave
    import unittest


    class TestMicrowave(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.microwave' has no attribute 'microwave'

  because ``microwave.py`` in the ``src`` folder_ does not have anything named ``microwave`` in it

  .. admonition:: If you get :ref:`ModuleNotFoundError<what is a module?>`

    check if you have ``__init__.py`` in the ``tests`` folder_ with underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``microwave.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` named ``microwave`` to ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def microwave():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: microwave() got an unexpected keyword argument 'door_is_open'

  because the test called the ``microwave`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only allows calls with 0 arguments

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_microwave.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add the :ref:`keyword argument<test_functions_w_keyword_arguments>` to the :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(door_is_open):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: microwave() got an unexpected keyword argument 'start_is_pushed'

  because the test called the ``microwave`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only allows calls with 1 input

* I add ``start_is_pushed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(door_is_open, start_is_pushed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'OFF'

  the ``microwave`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the test expects :red:`'OFF'`

* I change the `return statement`_ to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def microwave(door_is_open, start_is_pushed):
        return 'OFF'

  the test passes. The ``microwave`` :ref:`function<what is a function?>` always returns :red:`OFF`, it does not care about the inputs. Is this :ref:`Contradiction?<test_contradiction>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open` and the start button is :red:`NOT pushed`, in ``test_microwave.py``

  ==================  =================  =================
  door                start button       output
  ==================  =================  =================
  :green:`open`       :green:`pushed`    :red:`OFF`
  :green:`open`       :red:`NOT pushed`  :red:`OFF`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-14

        def test_open_door(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

----

*********************************************************************************
test_closed_door
*********************************************************************************

The :ref:`truth table` for if the door is :red:`closed` is

==================  =================  =================
door                start button       output
==================  =================  =================
:red:`closed`       :green:`pushed`    :green:`HEATING`
:red:`closed`       :red:`NOT pushed`  :red:`OFF`
==================  =================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed` and the start button is :green:`pushed`

==================  =================  =================
door                start button       output
==================  =================  =================
:red:`closed`       :green:`pushed`    :green:`HEATING`
==================  =================  =================

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 7-13

            reality = src.microwave.microwave(
                door_is_open=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'OFF' != 'HEATING'

because the ``microwave`` :ref:`function<what is a function?>` returns :red:`'OFF'` and the test expects :green:`'HEATING'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``microwave.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-4

  def microwave(door_is_open, start_is_pushed):
      if door_is_open == False:
          if start_is_pushed == True:
              return 'HEATING'

      return 'OFF'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def microwave(door_is_open, start_is_pushed):
        # if door_is_open == False:
        if bool(door_is_open) == False:
            # if start_is_pushed == True:
            if bool(start_is_pushed) == True:
                return 'HEATING'

        return 'OFF'

  the test is still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the first :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def microwave(door_is_open, start_is_pushed):
        # if door_is_open == False:
        # if bool(door_is_open) == False:
        if not bool(door_is_open) == True:
            # if start_is_pushed == True:
            if bool(start_is_pushed) == True:
                return 'HEATING'
        return 'OFF'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 7-8

    def microwave(door_is_open, start_is_pushed):
        # if door_is_open == False:
        # if bool(door_is_open) == False:
        # if not bool(door_is_open) == True:
        if not bool(door_is_open):
            # if start_is_pushed == True:
            # if bool(start_is_pushed) == True:
            if bool(start_is_pushed):
                return 'HEATING'

        return 'OFF'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6, 9-10

    def microwave(door_is_open, start_is_pushed):
        # if door_is_open == False:
        # if bool(door_is_open) == False:
        # if not bool(door_is_open) == True:
        # if not bool(door_is_open):
        if not door_is_open:
            # if start_is_pushed == True:
            # if bool(start_is_pushed) == True:
            # if bool(start_is_pushed):
            if start_is_pushed:
                return 'HEATING'
        return 'OFF'

  still green, because

  - ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``
  - ``if bool(something) == True`` is the same as ``if something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6, 10-12

    def microwave(door_is_open, start_is_pushed):
        # if door_is_open == False:
        # if bool(door_is_open) == False:
        # if not bool(door_is_open) == True:
        # if not bool(door_is_open):
        # if not door_is_open:
            # if start_is_pushed == True:
            # if bool(start_is_pushed) == True:
            # if bool(start_is_pushed):
            # if start_is_pushed:
        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def microwave(door_is_open, start_is_pushed):
        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  This is what happens when the ``microwave`` :ref:`function<what is a function?>` is called

  - it returns :green:`'HEATING'` if the door is :red:`closed` AND the start button is :green:`pushed`
  - it returns :red:`'OFF'` if the condition is not met

  is this :ref:`Converse NonImplication?<test_converse_non_implication>`

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed` and the start button is :red:`NOT pushed` to :ref:`test_closed_door` in ``test_microwave.py``

  ==================  =================  =================
  door                start button       output
  ==================  =================  =================
  :red:`closed`       :green:`pushed`    :green:`HEATING`
  :red:`closed`       :red:`NOT pushed`  :red:`OFF`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9, 11-15

        def test_closed_door(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

----

*********************************************************************************
test_open_door_timer_set
*********************************************************************************

So far, the :ref:`truth table` for the Microwave is

==================  =================  =================
door                start button       output
==================  =================  =================
:green:`open`       :green:`pushed`    :red:`OFF`
:green:`open`       :red:`NOT pushed`  :red:`OFF`
:red:`closed`       :green:`pushed`    :green:`HEATING`
:red:`closed`       :red:`NOT pushed`  :red:`OFF`
==================  =================  =================

I want the microwave to only heat up food when the timer is set, the inputs for the microwave will then be

* is the door open?
* is the timer set?
* was the start button pushed?

and the :ref:`truth table` for when the door is :green:`open` and the timer is :green:`set`, will be

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`open`  :green:`set`    :green:`pushed`    :red:`OFF`
:green:`open`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ===========

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``timer_is_set`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_open_door`, for when the door is :green:`open`, the timer is :green:`set` and the start button is :green:`pushed`

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`open`  :green:`set`    :green:`pushed`    :red:`OFF`
=============  ==============  =================  ===========

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6

      def test_open_door(self):
          my_expectation = 'OFF'

          reality = src.microwave.microwave(
              door_is_open=True,
              timer_is_set=True,
              start_is_pushed=True,
          )
          self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: microwave() got an unexpected keyword argument 'timer_is_set'

because the test called the ``microwave`` :ref:`function<what is a function?>` with 3 keyword arguments (``door_is_open``, ``timer_is_set`` and ``start_is_pushed``) and the :ref:`function<what is a function?>` only allows calls with 2 arguments (``door_is_open`` and ``start_is_pushed``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``timer_is_set`` to the :ref:`function signature<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set,
        ):
        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_closed_door - TypeError: microwave() missing 1 required positional argument:...
    FAILED ...test_open_door - TypeError: microwave() missing 1 required positional argument:...

  because the tests call the ``microwave`` :ref:`function<what is a function?>` with 2 arguments (``door_is_open`` and ``start_is_pushed``) and I just changed the :ref:`function signature<what is a function?>` to make it take 3 required arguments (``door_is_open``, ``start_is_pushed`` and ``timer_is_set``). I have to make ``timer_is_set`` a choice.

* I add a :ref:`default value<test_functions_w_default_arguments>` to make ``timer_is_set`` a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False,
        ):

  the test passes because

  .. code-block:: python

    src.microwave.microwave(
        door_is_open=True,
        start_is_pushed=False,
    )

  is now the same as

  .. code-block:: python

    src.microwave.microwave(
        door_is_open=True,
        start_is_pushed=False,
        timer_is_set=False,
    )

  a :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``timer_is_set`` to the next :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :green:`set` and the start button is :red:`NOT pushed`

  =============  ==============  =================  ===========
  door           timer           start button       output
  =============  ==============  =================  ===========
  :green:`open`  :green:`set`    :green:`pushed`    :red:`OFF`
  :green:`open`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  ===========

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 13

        def test_open_door(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door(self):

  the test is still green

* I change the name of the test from :ref:`test_open_door` to :ref:`test_open_door_timer_set`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestMicrowave(unittest.TestCase):

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

----

*********************************************************************************
test_open_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the door is :green:`open` and the timer is :red:`NOT set` is

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`open`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:green:`open`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ===========

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :red:`NOT set` and the start button is :green:`pushed`

  =============  ==============  =================  ===========
  door           timer           start button       output
  =============  ==============  =================  ===========
  :green:`open`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
  =============  ==============  =================  ===========

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8-9, 11-16

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :red:`NOT set` and the start button is :red:`NOT pushed`

  =============  ==============  =================  ===========
  door           timer           start button       output
  =============  ==============  =================  ===========
  :green:`open`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
  :green:`open`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  ===========

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 11-16

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door(self):

  green

----

*********************************************************************************
test_closed_door_timer_set
*********************************************************************************

The :ref:`truth table` for when the door is :red:`closed` and the timer is :green:`set` is

=============  ==============  =================  ================
door           timer           start button       output
=============  ==============  =================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ================

* I add a value for the ``timer_is_set`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_closed_door` for the case where the door is :red:`closed`, the timer is :green:`set` and the start button is :green:`pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
  =============  ==============  =================  =============

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

        def test_closed_door(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add a value for ``timer_is_set`` to the next :ref:`assertion<what is an assertion?>`, for when the door is :red:`closed`, the timer is :green:`set` and the start button is :red:`NOT pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  =============

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 14

        def test_closed_door(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I change the name of the test from :ref:`test_closed_door` to :ref:`test_closed_door_timer_set`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 8

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_closed_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the door is :red:`closed` and the timer is :red:`NOT set` is

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

* I add a new test with an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :red:`NOT set` and the start button is :green:`pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
  =============  ==============  =================  =============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 8-9, 11-16

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'HEATING' != 'OFF'

  because the ``microwave`` :ref:`function<what is a function?>` returns :green:`'HEATING'` and the test expects :red:`'OFF'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a :ref:`if statement<if statements>` to the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def microwave(
          door_is_open, start_is_pushed,
          timer_is_set=False
      ):
      if timer_is_set == False:
          return 'OFF'

      if not door_is_open and start_is_pushed:
          return 'HEATING'

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

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        if bool(timer_is_set) == False:
            return 'OFF'

        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  the test is still green

* I use :ref:`Logical Negation(NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        # if bool(timer_is_set) == False:
        if not bool(timer_is_set) == True:
            return 'OFF'

        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        # if bool(timer_is_set) == False:
        # if not bool(timer_is_set) == True:
        if not bool(timer_is_set):
            return 'OFF'

        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False
        ):
        # if timer_is_set == False:
        # if bool(timer_is_set) == False:
        # if not bool(timer_is_set) == True:
        # if not bool(timer_is_set):
        if not timer_is_set:
            return 'OFF'
        if not door_is_open and start_is_pushed:
            return 'HEATING'
        return 'OFF'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False,
        ):
        if not timer_is_set:
            return 'OFF'

        if not door_is_open and start_is_pushed:
            return 'HEATING'

        return 'OFF'

  This is what happens when the ``microwave`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the timer is :red:`NOT set`
  - if the timer is :green:`set`

    * it returns :green:`'HEATING'` if the door is :red:`closed` AND the start button is :green:`pushed`
  - it returns :red:`'OFF'` if none of the conditions are met

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_closed_door_timer_not_set`, for when the door is :red:`closed`, the timer is :red:`NOT set` and the start button is :red:`NOT pushed`, in ``test_microwave.py``

  =============  ==============  =================  ================
  door           timer           start button       output
  =============  ==============  =================  ================
  :red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  ================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 11-16

        def test_closed_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

* I add another clause to the :ref:`if statement<if statements>` for when the timer is :green:`set`, in the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-12

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False,
        ):
        if not timer_is_set:
            return 'OFF'

        if (
            not door_is_open
            and start_is_pushed
            and timer_is_set
        ):
            return 'HEATING'

        return 'OFF'

  the test is still green

* I remove the :ref:`if statement<if statements>` for when the timer is :red:`NOT set` because I do not need it anymore

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False
        ):
        if (
            not door_is_open
            and start_is_pushed
            and timer_is_set
        ):
            return 'HEATING'

        return 'OFF'

  still green. This is what happens when the ``microwave`` :ref:`function<what is a function?>` is called

  - it returns :green:`'HEATING'` if the door is :red:`closed` AND the start button is :green:`pushed` AND the timer is :green:`set`
  - it returns :red:`'OFF'` in every other case

----

*********************************************************************************
test_too_hot_open_door_timer_set
*********************************************************************************

the :ref:`truth table` for the Microwave is

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`open`  :green:`set`    :green:`pushed`    :red:`OFF`
:green:`open`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
:green:`open`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:green:`open`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ===========

=============  ==============  =================  ================
door           timer           start button       output
=============  ==============  =================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
:red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`OFF`
=============  ==============  =================  ================

I want to add a failsafe to stop the Microwave if it gets too hot. The inputs will then be

* is the door open?
* is the timer set?
* was the start button pushed?
* is the microwave too hot?

and the :ref:`truth table` for when the door is :green:`open` and the timer is :green:`set` will be

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`open`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`open`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`open`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``too_hot`` to the :ref:`assertion<what is an assertion?>` for the case where the door is :green:`open`, the timer is :green:`set`, the start button is :green:`pushed` and the microwave temperature is :green:`too hot`, to :ref:`test_open_door_timer_set` in ``test_microwave.py``

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
=============  ==============  =================  ==================  ================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 8

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: microwave() got an unexpected keyword argument 'too_hot'

because the test called the ``microwave`` :ref:`function<what is a function?>` with 4 keyword arguments (``door_is_open``, ``timer_is_set``, ``start_is_pushed`` and ``too_hot``) and the definition only allows calls with 2 required arguments (``door_is_open`` and ``start_is_pushed``) and 1 optional argument (``timer_is_set``)

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``too_hot`` to the ``microwave`` :ref:`function signature<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot,
        ):
        if not door_is_open and start_is_pushed and timer_is_set:
            return 'HEATING'

        return 'OFF'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``too_hot`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :green:`set`, the start button is :green:`pushed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 12-18

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add a value for the ``too_hot`` parameter in the next :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :green:`set`, the start button is :red:`NOT pushed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`open`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 24

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :green:`set`, the start button is :red:`NOT pushed` and the microwave temperature is  :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`open`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  :green:`open`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 28-34

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_open_door_timer_not_set(self):

  green

* I change the name of the test from :ref:`test_open_door_timer_set` to :ref:`test_too_hot_open_door_timer_set`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestMicrowave(unittest.TestCase):

        def test_too_hot_open_door_timer_set(self):
            my_expectation = 'OFF'

* I add a :ref:`global variable<what is a variable?>` for :red:`'OFF'`. I want to use it to remove repetition from the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.microwave
    import unittest


    OFF = 'OFF'


    class TestMicrowave(unittest.TestCase):

        def test_too_hot_open_door_timer_set(self):

* I use the :ref:`global variable<what is a variable?>` for ``my_expectation`` in :ref:`test_too_hot_open_door_timer_set`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 10-11, 19-20, 28-29, 37-38

        def test_too_hot_open_door_timer_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I remove the ``reality`` :ref:`variables<what is a variable?>`, I do not need them because they are called only once in every :ref:`assertion<what is an assertion?>`, I can call the ``microwave`` :ref:`function<what is a function?>` directly without the middle man

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 11-20, 29-38, 46-56, 65-74

        def test_too_hot_open_door_timer_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
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
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_open_door_timer_not_set(self):

----

*********************************************************************************
test_too_hot_open_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the door is :green:`open` and the timer is :red:`NOT set` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`open`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`open`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`open`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_open_door_timer_not_set` for when the door is :green:`open`, the timer is :red:`NOT set`, the start button is :green:`pushed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :red:`NOT set`, the start button is :green:`pushed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-18

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add a value for ``too_hot`` to the next :ref:`assertion<what is an assertion?>`, for when the door is :green:`open`, the timer is :red:`NOT set`, the start button is :red:`NOT pushed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`open`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 24

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :red:`NOT set`, the start button is :red:`NOT pushed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`open`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  :green:`open`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 28-34

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door_timer_set(self):

  green

* I change the name of the test from :ref:`test_open_door_timer_not_set` to :ref:`test_too_hot_open_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
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

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I call the ``microwave`` :ref:`function<what is a function?>` directly in the :ref:`assertions<what is an assertion?>` because I only use the ``reality`` :ref:`variable<what is a variable?>` once for each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 11-19, 28-36, 45-53, 62-70

        def test_too_hot_open_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
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
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_closed_door_timer_set(self):

----

*********************************************************************************
test_too_hot_closed_door_timer_set
*********************************************************************************

The :ref:`truth table` for when the door is :red:`closed` and the timer is :green:`set` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I use the ``OFF`` :ref:`global variable<what is a variable?>` for ``my_expectation`` when the value is :red:`'OFF'` in :ref:`test_closed_door_timer_set`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 10, 17-18

        def test_closed_door_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

        def test_closed_door_timer_not_set(self):

  the test is still green

* I call the ``microwave`` :ref:`function<what is a function?>` directly without the ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 8-15, 25-32

        def test_closed_door_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                ),
                'HEATING'
            )

            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                ),
                OFF
            )

  still green

* I remove the commented lines and :ref:`variables<what is a variable?>` that are not used anymore

  .. code-block:: python
    :lineno-start: 92

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :green:`set`, the start button is :green:`pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-10

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'HEATING' != 'OFF'

  because the ``microwave`` :ref:`function<what is a function?>` returned :green:`'HEATING'` and the test expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        if too_hot == True:
            return 'OFF'

        if (
            not door_is_open
            and start_is_pushed
            and timer_is_set
        ):
            return 'HEATING'

        return 'OFF'

  the test passes

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        # if too_hot == True:
        if bool(too_hot) == True:
            return 'OFF'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        # if too_hot == True:
        # if bool(too_hot) == True:
        if bool(too_hot):
            return 'OFF'

  still green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        # if too_hot == True:
        # if bool(too_hot) == True:
        # if bool(too_hot):
        # if bool(too_hot):
        if too_hot:
            return 'OFF'

  green, because ``if bool(something) == True`` is the same as ``if something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        if too_hot:
            return 'OFF'

        if (
            not door_is_open
            and start_is_pushed
            and timer_is_set
        ):
            return 'HEATING'

        return 'OFF'

  this is what happens when the ``microwave`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the microwave temperature is :green:`too hot`
  - if the microwave temperature is :red:`NOT too hot`

    * it returns :green:`'HEATING'` if the door is :red:`closed` AND the start button is :green:`pushed` AND the timer is :green:`set`
  - it returns :red:`'OFF'` in every other case

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :green:`set`, the start button is :green:`pushed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 17

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                ),
                OFF
            )

  still green

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the door is :red:`closed`, the timer is :green:`set`, the start button is :red:`NOT pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 27

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :green:`set`, the start button is :red:`NOT pushed`, and the microwave temperature is :red:`NOT too hot`

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

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  still green

* I change the name of the test from :ref:`test_closed_door_timer_set` to :ref:`test_too_hot_closed_door_timer_set`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

----

*********************************************************************************
test_too_hot_closed_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the door is :red:`closed` and the timer is :red:`NOT set` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I use the ``OFF`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_closed_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 2, 9-10, 17-18

        def test_closed_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I call the ``microwave`` :ref:`function<what is a function?>` directly in the :ref:`assertion<what is an assertion?>`, I do not need the ``reality`` :ref:`variables<what is a variable?>` because they are only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 10-17, 25-32

        def test_closed_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )

* I remove the commented lines and :ref:`variables<what is a variable?>` that are not used

  .. code-block:: python
    :lineno-start: 133

        def test_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )


    # Exceptions seen

* I change the name of the test from :ref:`test_closed_door_timer_not_set` to :ref:`test_too_hot_closed_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 11

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                ),
                OFF
            )

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_too_hot_closed_door_timer_not_set`, for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :green:`pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :green:`pushed`, and the microwave temperature is :red:`NOT too hot`

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
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                ),
                OFF
            )

  still green

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :red:`NOT pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 27

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

  green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :red:`NOT pushed`, and the microwave temperature is :red:`NOT too hot`

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
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                    too_hot=False,
                ),
                OFF
            )


    # Exceptions seen

  all the tests are still green

* I add another :ref:`condition<if statements>` to the one that returns :green:`'HEATING'` in the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        if too_hot:
            return 'OFF'

        if (
            not door_is_open
            and start_is_pushed
            and timer_is_set
            and not too_hot
        ):
            return 'HEATING'

        return 'OFF'

  still green

* I remove the :ref:`if statement<if statements>` for when the microwave temperature is :green:`too hot` because I no longer need it

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        if (
            not door_is_open
            and start_is_pushed
            and timer_is_set
            and not too_hot
        ):
            return 'HEATING'

        return 'OFF'

  green. This is what happens when the ``microwave`` :ref:`function<what is a function?>` is called

  * it returns :green:`'HEATING'` if the door is :red:`closed` AND the start button is :green:`pushed` AND the timer is :green:`set` AND the microwave temperature is :red:`NOT too hot`
  * it returns :red:`'OFF'` in every other case

* I can also write the ``microwave`` :ref:`function<what is a function?>` with the negative cases first

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, too_hot=False,
        ):
        off = 'OFF'

        if too_hot:
            return off
        if not timer_is_set:
            return off
        if not start_is_pushed:
            return off
        if door_is_open:
            return off

        return 'HEATING'


  which do you like better?

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_microwave.py`` and ``microwave.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``microwave``

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

I ran tests for a Microwave with these inputs:

* is the door open?
* is the timer set?
* was the start button pushed?
* is the microwave too hot?

the inputs gave me this :ref:`truth table`

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`open`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`open`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`open`  :green:`set`    :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
:green:`open`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
:green:`open`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
:green:`open`  :red:`NOT set`  :red:`NOT pushed`  :red:`NOT too hot`  :red:`OFF`
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

the only time this Microwave heats food is when the door is :red:`closed`, the timer is :green:`set`, the start button is :green:`pushed` and the microwave temperature is :red:`NOT too hot`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Microwave: tests and solutions>`

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

:ref:`Would you like to test making a Car starter?<car>`

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