.. meta::
  :description: Build a real-world Microwave using truth tables and Test-Driven Development in Python. Learn how boolean logic controls physical systems like Microwaves.
  :keywords: Jacob Itegboje, python truth table, Microwave python, tdd python, real world boolean logic, state machine truth table, pumping python

.. include:: ../../links.rst

.. _microwave:

#################################################################################
Microwave
#################################################################################

I want to make a **Microwave** that heats up food or stays off, if the inputs are

* is the door open?
* has the start button been pushed?

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
* I make a directory_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir microwave

  the terminal_ goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd microwave

  the terminal_ shows I am in the ``microwave`` folder_

  .. code-block:: shell

    .../pumping_python/microwave

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

* I make a requirements file_ for the `Python packages`_ I need, in the terminal_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

  the terminal_ goes back to the command line

* I set up the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `microwave`

  then goes back to the command line

* I remove ``main.py`` from the project because I do not use it

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed the `Python packages`_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

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

  .. admonition:: if the terminal_ shows

    .. code-block:: shell

      error: Failed to spawn: `pytest-watcher`
      Caused by: No such file or directory (os error 2)

    then add `pytest-watcher`_ to the ``requirements.txt`` file_

    .. code-block:: python
      :emphasize-lines: 1

      echo "pytest-watcher" >> requirements.txt

    run

    .. code-block:: python
      :emphasize-lines: 1

      uv add --requirement requirements.txt

    then

    .. code-block:: python
      :emphasize-lines: 1
      :emphasize-text: .

      uv run pytest-watcher . --now

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
test_door_open
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_door_open``, then add an :ref:`assertion<what is an assertion?>` for when the door is :green:`open` and the start button is :green:`pushed`

==================  =================  =================
door                start button       output
==================  =================  =================
:green:`open`       :green:`start`     :red:`OFF`
==================  =================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-4, 6-10

  class TestMicrowave(unittest.TestCase):

      def test_door_open(self):
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

    import src.microwave
    import unittest


    class TestMicrowave(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.microwave' has no attribute 'microwave'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
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

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_microwave.py``

  .. code-block:: python
    :lineno-start: 16
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

* I add ``start_is_pushed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(door_is_open, start_is_pushed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'OFF'

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

        def test_door_open(self):
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
test_door_closed
*********************************************************************************

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

        def test_door_closed(self):
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

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``microwave.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def microwave(door_is_open, start_is_pushed):
      if not door_is_open and start_is_pushed:
          return 'HEATING'
      return 'OFF'

the test passes. Is this :ref:`Converse NonImplication?<test_converse_non_implication>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed` and the start button is :red:`NOT pushed` to :ref:`test_door_closed` in ``test_microwave.py``

  ==================  =================  =================
  door                start button       output
  ==================  =================  =================
  :red:`closed`       :green:`pushed`    :green:`HEATING`
  :red:`closed`       :red:`NOT pushed`  :red:`OFF`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9, 11-15

        def test_door_closed(self):
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
test_door_open_and_timer_set
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

I want it to only HEATING up food when the timer is set, the inputs for the microwave will then be

* is the door open?
* is the timer set?
* has the start button been pushed?

and the :ref:`truth table` will be

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``timer_is_set`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_door_open`, for when the door is :green:`open`, the timer is :green:`set` and the start button is :green:`pushed`

=============  ==============  =================  ===========
door           timer           start button       output
=============  ==============  =================  ===========
:green:`open`  :green:`set`    :green:`pushed`    :red:`OFF`
=============  ==============  =================  ===========

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6

      def test_door_open(self):
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

    FAILED ...test_microwave_w - TypeError: microwave() missing 1 required positional argument:...
    FAILED ...test_door_open - TypeError: microwave() missing 1 required positional argument:...

  because the other :ref:`assertions<what is an assertion?>` call the ``microwave`` :ref:`function<what is a function?>` with 2 arguments and I just changed the :ref:`function signature<what is a function?>` to make it take 3 required arguments

* I add a :ref:`default value<test_functions_w_default_arguments>` to make ``timer_is_set`` a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False,
        ):

  the test passes because this

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

  because ``timer_is_set`` has a :ref:`default value<test_functions_w_default_arguments>`

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

        def test_door_open(self):
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

        def test_microwave_w(self):

  the test is still green

* I change the name of the test from :ref:`test_door_open` to :ref:`test_door_open_and_timer_set`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestMicrowave(unittest.TestCase):

        def test_door_open_and_timer_set(self):
            my_expectation = 'OFF'

----

*********************************************************************************
test_door_open_and_timer_not_set
*********************************************************************************

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

        def test_door_open_and_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_door_closed(self):

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

        def test_door_open_and_timer_not_set(self):
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

        def test_door_closed(self):

  green

----

*********************************************************************************
test_door_closed_and_timer_set
*********************************************************************************

* I add a value for the ``timer_is_set`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_door_closed` for the case where the door is :red:`closed`, the timer is :green:`set` and the start button is :green:`pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
  =============  ==============  =================  =============

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

        def test_door_closed(self):
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

* I do not need to add a value for ``timer_is_set`` to the next :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :green:`set` and the start button is :red:`NOT pushed`

  =============  ==============  =================  =============
  door           timer           start button       output
  =============  ==============  =================  =============
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :red:`OFF`
  =============  ==============  =================  =============

  because

  .. code-block:: python

    src.microwave.microwave(
        door_is_open=False,
        start_is_pushed=False,
    )

  is the same as

  .. code-block:: python

    src.microwave.microwave(
        door_is_open=False,
        start_is_pushed=False,
        timer_is_set=False,
    )

  the :ref:`default value<test_functions_w_default_arguments>` for ``timer_is_set`` is :ref:`False<test_what_is_false>`

* I change the name of the test from :ref:`test_door_closed` to :ref:`test_door_closed_and_timer_set`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 8

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_door_closed_and_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_door_closed_and_timer_not_set
*********************************************************************************

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
    :emphasize-lines: 7-8, 10-15

            reality = src.microwave.microwave(
                door_is_open=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_door_closed_and_timer_not_set(self):
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
          timer_is_set=False,
      ):
      if not timer_is_set:
          return 'OFF'
      if not door_is_open and start_is_pushed:
          return 'HEATING'
      return 'OFF'

the test passes. The Microwave returns

* :red:`OFF` if the timer is :red:`NOT set`
* :green:`HEATING` if the door is :red:`closed` and the start button is :green:`pushed`, which only happens if the timer is :green:`set`
* :red:`OFF` if none of the conditions are met

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :red:`NOT set` and the start button is :red:`NOT pushed`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 11-16

        def test_door_closed_and_timer_not_set(self):
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
    :emphasize-lines: 7

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False,
        ):
        if not timer_is_set:
            return 'OFF'
        if not door_is_open and start_is_pushed and timer_is_set:
            return 'HEATING'
        return 'OFF'

  the test is still green

* I remove the :ref:`if statement<if statements>` for when the timer is :red:`NOT set` because I do not need it anymore

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False,
        ):
        if not door_is_open and start_is_pushed and timer_is_set:
            return 'HEATING'
        return 'OFF'

  still green. The Microwave returns

  - ``'HEATING'`` if the door is :red:`closed`, the timer is :green:`set` and the start button is :green:`pushed`
  - ``'OFF'`` in every other case

----

*********************************************************************************
test_door_open_timer_set_w_overheating
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
* has the start button been pushed?
* is the microwave too hot?

and the :ref:`truth table` will be

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

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

test_door_open_timer_set_and_overheating

I add a value for ``overheating`` to the :ref:`assertion<what is an assertion?>` for the case where the door is :green:`open`, the timer is :green:`set`, the start button is :green:`pushed` and the microwave temperature is :green:`too hot`, to :ref:`test_door_open_and_timer_set` in ``test_microwave.py``

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`open`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
=============  ==============  =================  ==================  ================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 8

        def test_door_open_and_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: microwave() got an unexpected keyword argument 'overheating'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``overheating`` to the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, overheating,
        ):
        if not door_is_open and start_is_pushed and timer_is_set:
            return 'HEATING'
        return 'OFF'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`I cannot put a parameter that does NOT have a default value after a parameter that has a default value<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``overheating`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def microwave(
            door_is_open, start_is_pushed,
            timer_is_set=False, overheating=False,
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

        def test_door_open_and_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add a value for the ``overheating`` parameter in the next :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :green:`set`, the start button is :red:`NOT pushed` and the microwave temperature is :green:`too hot`

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

        def test_door_open_and_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True
            )
            self.assertEqual(reality, my_expectation)

        def test_door_open_and_timer_not_set(self):

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
    :emphasize-lines: 28-33

        def test_door_open_and_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False,
            )

        def test_door_open_and_timer_not_set(self):

  green

* I change the name of the test from :ref:`test_door_open_and_timer_set` to :ref:`test_door_open_timer_set_w_overheating`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestMicrowave(unittest.TestCase):

        def test_door_open_timer_set_w_overheating(self):
            my_expectation = 'OFF'

* I add a :ref:`global variable<what is a variable?>` for ``'OFF'``. I want to use it to remove repetition from the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.microwave
    import unittest


    OFF = 'OFF'


    class TestMicrowave(unittest.TestCase):

        def test_door_open_timer_set_w_overheating(self):

* I use the :ref:`global variable<what is a variable?>` for ``my_expectation`` in :ref:`test_door_open_timer_set_w_overheating`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 10-11, 19-20, 28-29, 37-38

        def test_door_open_timer_set_w_overheating(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

        def test_door_open_and_timer_not_set(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_door_open_timer_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

        def test_door_open_and_timer_not_set(self):

----

*********************************************************************************
test_door_open_timer_not_set_w_overheating
*********************************************************************************

* I add a value for the ``overheating`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_door_open_and_timer_not_set` for when the door is :green:`open`, the timer is :red:`NOT set`, the start button is :green:`pushed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8

        def test_door_open_and_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
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
    :lineno-start: 43
    :emphasize-lines: 12-18

        def test_door_open_and_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_door_closed_and_timer_set(self):

  the test is still green

* I add a value for ``overheating`` to the next :ref:`assertion<what is an assertion?>` for when the door is :green:`open`, the timer is :red:`NOT set`, the start button is :red:`NOT pushed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`open`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :green:`open`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :green:`open`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 20-26

        def test_door_open_and_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True
            )
            self.assertEqual(reality, my_expectation)

        def test_door_closed_and_timer_set(self):

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
    :lineno-start: 43
    :emphasize-lines: 28-34

        def test_door_open_and_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_door_closed_and_timer_set(self):

  green

* I change the name of the test from :ref:`test_door_open_and_timer_not_set` to :ref:`test_door_open_timer_not_set_w_overheating`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 9

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

        def test_door_open_timer_not_set_w_overheating(self):
            my_expectation = 'OFF'

* I use the ``OFF`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_door_open_timer_not_set_w_overheating`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2, 10-11, 19-20, 28-29, 37-38

        def test_door_open_timer_not_set_w_overheating(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 43

        def test_door_open_timer_not_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_set(self):

----

*********************************************************************************
test_door_closed_timer_set_w_overheating
*********************************************************************************

* I use the ``OFF`` :ref:`global variable<what is a variable?>` for ``my_expectation`` when the value is ``'OFF'`` in :ref:`test_door_closed_and_timer_set`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 10, 16-17

        def test_door_closed_and_timer_set(self):
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
                start_is_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_not_set(self):

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 76

        def test_door_closed_and_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_not_set(self):

* I add a value for the ``overheating`` and ``timer_is_set`` parameters in the second :ref:`assertion<what is an assertion?>`, for when the door is :red:`closed`, the timer is :green:`set`, the start button is :green:`pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 12, 14

        def test_door_closed_and_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_not_set(self):

  still green

* I add a value for the ``overheating`` parameter to the first :ref:`assertion<what is an assertion?>`, for when the door is :red:`closed`, the timer is :green:`set`, the start button is :green:`pushed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 7

        def test_door_closed_and_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_not_set(self):

  green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :green:`set`, the start button is :red:`NOT pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :green:`set`    :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :green:`set`    :green:`pushed`    :red:`NOT too hot`  :green:`HEATING`
  :red:`closed`  :green:`set`    :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 19-25

        def test_door_closed_and_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_not_set(self):

  still green

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
    :lineno-start: 76
    :emphasize-lines: 27-33

        def test_door_closed_and_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_and_timer_not_set(self):

  the test is still green

* I change the name of the test from :ref:`test_door_closed_and_timer_set` to :ref:`test_door_closed_timer_set_w_overheating`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 9

            reality = src.microwave.microwave(
                door_is_open=True,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_timer_set_w_overheating(self):
            my_expectation = 'HEATING'

----

*********************************************************************************
test_door_closed_timer_not_set_w_overheating
*********************************************************************************

* I use the ``OFF`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_door_closed_and_timer_not_set`

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 2, 9-10, 17-18

        def test_door_closed_and_timer_not_set(self):
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


    # Exceptions seen

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 110

        def test_door_closed_and_timer_not_set(self):
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

* I change the name of the test from :ref:`test_door_closed_and_timer_not_set` to :ref:`test_door_closed_timer_not_set_w_overheating`

  .. code-block:: python
    :lineno-start: 102
    :emphasize-lines: 9

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=True,
                start_is_pushed=False,
                overheating=False
            )
            self.assertEqual(reality, OFF)

        def test_door_closed_timer_not_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
            )
            self.assertEqual(reality, OFF)

* I add a value for the ``overheating`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_door_closed_timer_not_set_w_overheating`, for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :green:`pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 6

        def test_door_closed_timer_not_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, OFF)

  green

* I add an :ref:`assertion<what is an assertion?>` for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :green:`pushed`, and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 10-16

        def test_door_closed_timer_not_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green

* I add a value for the ``overheating`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the door is :red:`closed`, the timer is :red:`NOT set`, the start button is :red:`NOT pushed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :green:`too hot`    :red:`OFF`
  :red:`closed`  :red:`NOT set`  :green:`pushed`    :red:`NOT too hot`  :red:`OFF`
  :red:`closed`  :red:`NOT set`  :red:`NOT pushed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 18-24

        def test_door_closed_timer_not_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  the test is still green

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
    :lineno-start: 110
    :emphasize-lines: 26-32

        def test_door_closed_timer_not_set_w_overheating(self):
            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=True,
                overheating=False,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                timer_is_set=False,
                start_is_pushed=False,
                overheating=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green

* I use the call to the ``microwave`` :ref:`function<what is a function?>` directly in the :ref:`assertion<what is an assertion?>`. I do not need the ``reality`` :ref:`variable<what is a variable?>` because it is only used once in each one

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines:

        def test_door_closed_timer_not_set_w_overheating(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    overheating=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=True,
                    overheating=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                    overheating=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=False,
                    start_is_pushed=False,
                    overheating=False,
                ),
                OFF
            )


    # Exceptions seen

  green

* I remove the ``reality`` :ref:`variable<what is a variable?>` from :ref:`test_door_closed_timer_set_w_overheating`

  .. code-block:: python
    :lineno-start: 76

        def test_door_closed_timer_set_w_overheating(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=True,
                    overheating=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    overheating=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    overheating=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    timer_is_set=True,
                    start_is_pushed=False,
                    overheating=False
                ),
                OFF
            )

        def test_door_closed_timer_not_set_w_overheating(self):

  still green

* I remove the ``reality`` :ref:`variable<what is a variable?>` from :ref:`test_door_open_timer_not_set_w_overheating`

  .. code-block:: python
    :lineno-start: 43

        def test_door_open_timer_not_set_w_overheating(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    overheating=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=True,
                    overheating=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    overheating=True
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=False,
                    start_is_pushed=False,
                    overheating=False,
                ),
                OFF
            )

        def test_door_closed_timer_set_w_overheating(self):

  the tests are still green

* I remove the ``reality`` :ref:`variable<what is a variable?>` from :ref:`test_door_open_timer_set_w_overheating`

  .. code-block:: python
    :lineno-start: 10

        def test_door_open_timer_set_w_overheating(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    overheating=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=True,
                    overheating=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    overheating=True
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    timer_is_set=True,
                    start_is_pushed=False,
                    overheating=False,
                ),
                OFF
            )

        def test_door_open_timer_not_set_w_overheating(self):

  all the tests are green

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_microwave.py`` and ``microwave.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``microwave``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ is my friend, and shows

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
* has the start button been pushed?
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