.. meta::
  :description: Build a real-world Traffic Light using truth tables and Test-Driven Development in Python. Learn how boolean logic controls physical systems like traffic signals.
  :keywords: Jacob Itegboje, python truth table, Traffic Light python, tdd python, real world boolean logic, state machine truth table, pumping python

.. include:: ../../links.rst

.. _traffic_light:

#################################################################################
Traffic Light
#################################################################################

----

I use the :ref:`truth table` to build a **Traffic Light** that changes color based on a timer, if the inputs are

* what color is the light now?
* is the timer done?

Here is the truth table for the traffic light

================  ==============  =================
current light     timer done      show
================  ==============  =================
:red:`RED`        :green:`yes`    :green:`GREEN`
:red:`RED`        :red:`no`       :red:`RED`
:yellow:`YELLOW`  :green:`yes`    :red:`RED`
:yellow:`YELLOW`  :red:`no`       :yellow:`YELLOW`
:green:`GREEN`    :green:`yes`    :yellow:`YELLOW`
:green:`GREEN`    :red:`no`       :green:`GREEN`
================  ==============  =================

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have at the end of this chapter

.. literalinclude:: ../../code/truth_table/tests/test_traffic_light.py
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

* I name this project ``traffic_light``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir traffic_light

  the terminal_ goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd traffic_light

  the terminal_ shows I am in the ``traffic_light`` folder_

  .. code-block:: shell

    .../pumping_python/traffic_light

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

        touch src/traffic_light.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/traffic_light.py

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

        touch tests/test_traffic_light.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_traffic_light.py

  the terminal_ goes back to the command line

* I open ``test_traffic_light.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_traffic_light.py

    `Visual Studio Code`_ opens ``test_traffic_light.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestTrafficLight(unittest.TestCase):

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

* I setup the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `traffic-light-controller`

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

  the terminal shows it installed the `Python packages`_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    ____________________ TestTrafficLight.test_failure _______________________

    self = <tests.test_traffic_light.TestTrafficLight testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_traffic_light.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_traffic_light.py::TestTrafficLight::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestTrafficLight(unittest.TestCase):

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
test_traffic_light_when_red
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_traffic_light_when_red``

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestTrafficLight(unittest.TestCase):

      def test_traffic_light_when_red(self):(self):
          my_expectation = 'GREEN'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=True,
          )
          self.assertEqual(reality, my_expectation)


    # Exceptions seen
    # AssertionError

the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

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

    import src.traffic_light
    import unittest

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.traffic_light' has no attribute 'show'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``traffic_light.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def show():
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: show() got an unexpected keyword argument 'current_light'

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add the :ref:`keyword argument<test_functions_w_keyword_arguments>` to the :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(current_light):
        return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: show() got an unexpected keyword argument 'timer_done'

* I add ``timer_done`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(current_light, timer_done):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'GREEN'

* I change the `return statement`_ to give the test what it expects

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(current_light, timer_done):
        return 'GREEN'

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` for when the current light is :red:`RED` and the timer has not expired, in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-14

        def test_traffic_light_when_red(self):
            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

* I add an :ref:`if statement<if statements>` to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def show(current_light, timer_done):
        if not timer_done:
            return 'RED'
        return 'GREEN'

  the test passes

----

*********************************************************************************
test_traffic_light_when_yellow
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test for when the traffic light is red, to ``test_traffic_light.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 16-22

      def test_traffic_light_when_red(self):
          my_expectation = 'GREEN'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'RED'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_traffic_light_when_yellow(self):
          my_expectation = 'RED'
          reality = src.traffic_light.show(
              current_light='YELLOW',
              timer_done=True,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'GREEN' != 'RED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``traffic_light.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-4

  def show(current_light, timer_done):
      if current_light == 'YELLOW':
          if timer_done:
              return 'RED'
      if not timer_done:
          return 'RED'
      return 'GREEN'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>` to ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9-14

        def test_traffic_light_when_yellow(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'YELLOW'

* I add an :ref:`if statement<if statements>` to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def show(current_light, timer_done):
        if current_light == 'YELLOW':
            if timer_done:
                return 'RED'
            else:
                return 'YELLOW'
        if not timer_done:
            return 'RED'
        return 'GREEN'

  the test passes

----

*********************************************************************************
test_traffic_light_when_green
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for when the traffic light is green, to ``test_traffic_light.py``

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 16-22

      def test_traffic_light_when_yellow(self):
          my_expectation = 'RED'
          reality = src.traffic_light.show(
              current_light='YELLOW',
              timer_done=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'YELLOW'
          reality = src.traffic_light.show(
              current_light='YELLOW',
              timer_done=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_traffic_light_when_green(self):
          my_expectation = 'YELLOW'
          reality = src.traffic_light.show(
              current_light='GREEN',
              timer_done=True,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'GREEN' != 'YELLOW'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``traffic_light.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-4

  def show(current_light, timer_done):
      if current_light == 'GREEN':
          if timer_done:
              return 'YELLOW'
      if current_light == 'YELLOW':
          if timer_done:
              return 'RED'
          else:
              return 'YELLOW'
      if not timer_done:
          return 'RED'
      return 'GREEN'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 9-14

        def test_traffic_light_when_green(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'YELLOW'

* I add an :ref:`if statement<if statements>` to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def show(current_light, timer_done):
        if current_light == 'GREEN':
            if timer_done:
                return 'YELLOW'
            else:
                return 'GREEN'
        if current_light == 'YELLOW':
            if timer_done:
                return 'RED'
            else:
                return 'YELLOW'
        if not timer_done:
            return 'RED'
        return 'GREEN'

  the test passes

* I add :ref:`variables<what is a variable?>` for the colors to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if current_light == 'GREEN':
            if timer_done:
                return 'YELLOW'
            else:
                return 'GREEN'
        if current_light == 'YELLOW':
            if timer_done:
                return 'RED'
            else:
                return 'YELLOW'
        if not timer_done:
            return 'RED'
        return 'GREEN'

* I use the new :ref:`variables<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 7-8, 10-13, 15-16, 18-19, 21-24

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        # if current_light == 'GREEN':
        if current_light == green:
            if timer_done:
                # return 'YELLOW'
                return yellow
            else:
                # return 'GREEN'
                return green
        # if current_light == 'YELLOW':
        if current_light == yellow:
            if timer_done:
                # return 'RED'
                return red
            else:
                # return 'YELLOW'
                return yellow
        if not timer_done:
            # return 'RED'
            return red
        # return 'GREEN'
        return green

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if current_light == green:
            if timer_done:
                return yellow
            else:
                return green
        if current_light == yellow:
            if timer_done:
                return red
            else:
                return yellow
        if not timer_done:
            return red
        return green

* I add a new :ref:`if statement<if statements>` for it the timer because it controls the traffic lights

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-10

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green
        if current_light == green:
            if timer_done:
                return yellow
            else:
                return green
        if current_light == yellow:
            if timer_done:
                return red
            else:
                return yellow
        if not timer_done:
            return red
        return green

  the test is still green

* I add an :ref:`else clause<if statements>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green
        else:
            return current_light

        if current_light == green:
            if timer_done:
                return yellow
            else:
                return green
        if current_light == yellow:
            if timer_done:
                return red
            else:
                return yellow
        if not timer_done:
            return red
        return green

  still green

* I remove the other :ref:`if statements`

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green
        else:
            return current_light

  green

* I add a :ref:`variable<what is a variable?>` for the next light

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green
        else:
            return current_light

* I use the new :ref:`variable<what is a variable?>` in each :ref:`condition<if statements>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7, 10, 13, 16

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
                return yellow
            if current_light == yellow:
                next_light = red
                return red
            if current_light == red:
                next_light = green
                return green
        else:
            next_light = current_light
            return current_light

  the test is still green

* I add a `return statement`_ for the :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
                return yellow
            if current_light == yellow:
                next_light = red
                return red
            if current_light == red:
                next_light = green
                return green
        else:
            next_light = current_light
            return current_light

        return next_light

* I remove the other `return statements`_

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == yellow:
                next_light = red
            if current_light == red:
                next_light = green
        else:
            next_light = current_light

        return next_light

  still green

* I remove the :ref:`if statement<if statements>` for when the light is ``'YELLOW'`` because I no longer need it

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                next_light = green
        else:
            next_light = current_light

        return next_light

  the test is still green

----

*********************************************************************************
test_traffic_light_when_red_w_walk_button
*********************************************************************************

----

I want to add a button for people to push when they want to cross the street, the inputs for the traffic light will now be

* what color is the light now?
* is the timer done?
* did the person push the walk button?

and the truth table when the traffic light is :red:`RED` is

================  ==============  ==============  =================
current light     timer done      walk button     show
================  ==============  ==============  =================
:red:`RED`        :green:`yes`    :green:`yes`    :red:`RED`
:red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN`
:red:`RED`        :red:`no`       :green:`yes`    :red:`RED`
:red:`RED`        :red:`no`       :red:`no`       :red:`RED`
================  ==============  ==============  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add ``walk_button`` to the call to ``src.traffic_light.show`` in the first :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_red` in ``test_traffic_light.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6

      def test_traffic_light_when_red(self):
          my_expectation = 'GREEN'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=True,
              walk_button=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'RED'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_traffic_light_when_yellow(self):

the terminal_ shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: show() got an unexpected keyword argument 'walk_button'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`keyword argument<test_functions_w_keyword_arguments>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(current_light, timer_done, walk_button):

  the terminal_ shows 3 failures with :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_traffic_light_when_green - TypeError: show() missing 1 required positional arg...
    FAILED ...test_traffic_light_when_red - TypeError: show() missing 1 required positional arg...
    FAILED ...test_traffic_light_when_yellow - TypeError: show() missing 1 required positional arg...

* I add a :ref:`default<test_functions_w_default_arguments>` value for the new :ref:`keyword argument<test_functions_w_keyword_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def show(
            current_light, timer_done,
            walk_button=False,
        ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the expectation for when the light is :red:`RED`, the timer is done and the walk button is pushed

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_traffic_light_when_red(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

* I add an :ref:`if statement with an else clause<if statements>` to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 12-15

    def show(
            current_light, timer_done,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        return next_light

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is done and the walk button has not been pushed, to :ref:`test_traffic_light_when_red` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-16

        def test_traffic_light_when_red(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_traffic_light_when_yellow(self):

  the test is still green

* I change the expectation to make sure the test works

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            my_expectation = 'BOOM'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'BOOM'

* I change the expectation back

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

  the test is green again

* I add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is done and the walk button is pressed

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 18-24

        def test_traffic_light_when_red(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_traffic_light_when_yellow(self):

  the test is still green

* I add a :ref:`variable<what is a variable?>` for ``'RED'``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_traffic_light_when_red(self):
            red = 'RED'

            my_expectation = 'RED'

* I use the :ref:`variable<what is a variable?>` to remove repetition

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines:

        def test_traffic_light_when_red(self):
            red = 'RED'

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

        def test_traffic_light_when_yellow(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_traffic_light_when_red(self):
            red = 'RED'

            reality = src.traffic_light.show(
                current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light=red,
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light=red,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show(
                current_light=red,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, red)

* I add a default value for the ``current_light`` :ref:`keyword argument<test_functions_w_keyword_arguments>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(
            current_light='RED', timer_done,
            walk_button=False,
        ):

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  :ref:`I cannot put a parameter that does NOT have a default value after a parameter that has a default value<test_functions_w_positional_and_keyword_arguments>`

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a default value for ``timer_done`` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):

  the test is green again

* I change the name of :ref:`test_traffic_light_when_red` to :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_traffic_light_when_red_w_walk_button(self):
            red = 'RED'

* I remove the ``current_light`` parameter from the call to ``src.traffic_light.show`` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 7

        def test_traffic_light_when_red_w_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, red)

        def test_traffic_light_when_yellow(self):

  the test is still green

----

*********************************************************************************
test_traffic_light_when_yellow_w_walk_button
*********************************************************************************

The truth table when the traffic light is :yellow:`YELLOW` with the push button is

================  ==============  ==============  =================
current light     timer done      walk button     show
================  ==============  ==============  =================
:yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED`
:yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED`
:yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`no`       :red:`no`       :yellow:`YELLOW`
================  ==============  ==============  =================

* I add ``walk_button`` to the call to ``src.traffic_light.show`` in the first :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_yellow` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6

          def test_traffic_light_when_yellow(self):
              my_expectation = 'RED'
              reality = src.traffic_light.show(
                  current_light='YELLOW',
                  timer_done=True,
                  walk_button=True,
              )
              self.assertEqual(reality, my_expectation)

              my_expectation = 'YELLOW'
              reality = src.traffic_light.show(
                  current_light='YELLOW',
                  timer_done=False,
              )
              self.assertEqual(reality, my_expectation)

          def test_traffic_light_when_green(self):

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is done and the walk button is NOT pushed

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 10-16

        def test_traffic_light_when_yellow(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_traffic_light_when_green(self):

  still green

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is NOT done and the walk button is pushed

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 6

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is NOT done and the walk button is NOT pushed

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 9-15

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_traffic_light_when_green(self):

  still green

* I change the name of the test from :ref:`test_traffic_light_when_yellow` to :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 7

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, red)

        def test_traffic_light_when_yellow_w_walk_button(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

* I add a :ref:`variable<what is a variable?>` for :yellow:`YELLOW`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

        def test_traffic_light_when_yellow_w_walk_button(self):
            yellow = 'YELLOW'

            my_expectation = 'RED'

* I use the new :ref:`variable<what is a variable?>` to remove repetition

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6-7, 15-16, 22, 24-25, 29-30, 32, 34-35, 39-40

        def test_traffic_light_when_yellow_w_walk_button(self):
            yellow = 'YELLOW'

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

        def test_traffic_light_when_green(self):

  the test is still green

* I add a :ref:`variable<what is a variable?>` for :red:`RED`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

        def test_traffic_light_when_yellow_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

* I use the new :ref:`variable<what is a variable?>` to remove repetition

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 4, 11-12, 14, 21-22

        def test_traffic_light_when_yellow_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

        def test_traffic_light_when_green(self):

  still green

* I remove the comments

  .. code-block:: python
    :lineno-start: 35

        def test_traffic_light_when_yellow_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, yellow)

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, yellow)

        def test_traffic_light_when_green(self):

* I make :ref:`global variables<what is a variable?>` for the colors at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW = 'RED', 'YELLOW'


    class TestTrafficLight(unittest.TestCase):

* I use the :red:`RED` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 8-9, 22-23, 29-30

        def test_traffic_light_when_red_w_walk_button(self):
            # red = 'RED'

            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

        def test_traffic_light_when_yellow_w_walk_button(self)

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    import src.traffic_light
    import unittest


    RED, YELLOW = 'RED', 'YELLOW'


    class TestTrafficLight(unittest.TestCase):

        def test_traffic_light_when_red_w_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, RED)

        def test_traffic_light_when_yellow_w_walk_button(self)

* I use the :RED:`RED` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 9-10, 17-18

        def test_traffic_light_when_yellow_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

  still green

* I use the :yellow:`YELLOW` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2, 5-6, 14-15, 23-24, 28-29, 32-33, 37-38

      def test_traffic_light_when_yellow_w_walk_button(self):
          # red, yellow = 'RED', 'YELLOW'

          reality = src.traffic_light.show(
              # current_light=yellow,
              current_light=YELLOW,
              timer_done=True,
              walk_button=True,
          )
          # self.assertEqual(reality, red)
          self.assertEqual(reality, RED)

          reality = src.traffic_light.show(
              # current_light=yellow,
              current_light=YELLOW,
              timer_done=True,
              walk_button=False,
          )
          # self.assertEqual(reality, red)
          self.assertEqual(reality, RED)

          reality = src.traffic_light.show(
              # current_light=yellow,
              current_light=YELLOW,
              timer_done=False,
              walk_button=True,
          )
          # self.assertEqual(reality, yellow)
          self.assertEqual(reality, YELLOW)

          reality = src.traffic_light.show(
              # current_light=yellow,
              current_light=YELLOW,
              timer_done=False,
              walk_button=False,
          )
          # self.assertEqual(reality, yellow)
          self.assertEqual(reality, YELLOW)

  green

* I remove the comments

  .. code-block:: python
    :lineno-start: 36

        def test_traffic_light_when_yellow_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, YELLOW)

        def test_traffic_light_when_green(self):

----

*********************************************************************************
test_traffic_light_when_green_w_walk_button
*********************************************************************************

The truth table when the traffic light is :green:`GREEN` with the push button is

================  ==============  ==============  =================
current light     timer done      walk button     show
================  ==============  ==============  =================
:green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW`
:green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW`
:green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN`
:green:`GREEN`    :red:`no`       :red:`no`       :green:`GREEN`
================  ==============  ==============  =================

* I add ``walk_button`` to the call to ``src.traffic_light.show`` in the first :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_green` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 6

        def test_traffic_light_when_green(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN`, the timer is done and the walk button is NOT pushed

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 10-16

        def test_traffic_light_when_green(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN`, the timer is NOT done and the walk button is pushed

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 5

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN`, the timer is NOT done and the walk button is NOT pushed

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 9-15

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I add a :ref:`global variable<what is a variable?>` for :green:`GREEN`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'


    class TestTrafficLight(unittest.TestCase):

* I use the :green:`GREEN` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1, 6-7

            # my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_traffic_light_when_red_w_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False
            )
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, RED)

        def test_traffic_light_when_yellow_w_walk_button

* I change the name of :ref:`test_traffic_light_when_green` to :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start:
    :emphasize-lines: 8

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, YELLOW)

        def test_traffic_light_when_green_w_walk_button(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

* I use the :green:`GREEN` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-5, 13-14, 20, 22-23, 27-28, 30, 32-33, 37-38

        def test_traffic_light_when_green_w_walk_button(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

            # my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

  still green

* I use the :yellow:`YELLOW` :ref:`global variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2, 9-10, 12, 19-20

        def test_traffic_light_when_green_w_walk_button(self):
            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, YELLOW)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, YELLOW)

  green

* I remove the comments

  .. code-block:: python
    :lineno-start: 64

        def test_traffic_light_when_green_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, GREEN)

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I can remove the ``reality`` :ref:`variable<what is a variable?>` since it is only used once for each :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-13, 19-26, 32-39, 45-52

        def test_traffic_light_when_red_w_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, RED)
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False
                ),
                GREEN
            )

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, RED)
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.show(
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, RED)
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=False,
                ),
                RED
            )

* I remove the ``reality`` :ref:`variable<what is a variable?>` and the comments from :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 10

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False
                ),
                GREEN
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=False,
                ),
                RED
            )

        def test_traffic_light_when_yellow_w_walk_button(self):

* I do the same thing in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7-15, 22-30, 37-45, 52-60

        def test_traffic_light_when_yellow_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, RED)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, RED)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                RED
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW
            )

* I remove the ``reality`` :ref:`variable<what is a variable?>` and comments from :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 43

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW
            )

        def test_traffic_light_when_green_w_walk_button

* I can also do it with :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 7-15, 22-30, 37-45, 52-60

        def test_traffic_light_when_green_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                GREEN
            )

* I remove the ``reality`` :ref:`variable<what is a variable?>` and comments from :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :linenos:

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                YELLOW
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                GREEN
            )


    # Exceptions seen

  all the tests are still green

----

*************************************************************************************
test_traffic_light_w_walk_sign
*************************************************************************************

I want the traffic light to show ``WALK`` or ``NO WALK`` when a person can walk. This means the :ref:`truth table` for the Traffic Light is

================  ==============  ==============  =================================
current light     timer done      walk button     show
================  ==============  ==============  =================================
:red:`RED`        :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
:red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :red:`no`       :green:`yes`    :red:`RED` + :green:`WALK`
:red:`RED`        :red:`no`       :red:`no`       :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`no`       :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :red:`no`       :green:`GREEN` + :red:`NO WALK`
================  ==============  ==============  =================================

this shows that the Traffic Light only shows :green:`WALK` when the light is :red:`RED`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the expectation of the first :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 7

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'RED' != ('RED', 'WALK')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the `return statement`_ in the ``show`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        return next_light, 'WALK'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_traffic_light_when_green_w_walk_button - AssertionError: ('YELLOW', 'WALK') != 'YELLOW'
    FAILED ...test_traffic_light_when_red_w_walk_button - AssertionError: ('GREEN', 'WALK') != 'GREEN'
    FAILED ...test_traffic_light_when_yellow_w_walk_button - AssertionError: ('RED', 'WALK') != 'RED'

  my solution broke all the tests

* I remove ``WALK`` from the `return statement`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1

        return next_light

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I make a copy of the ``show`` :ref:`function<what is a function?>` and paste it below, then change the name to ``show_walk``, this way I keep what works while I try a new solution

  .. code-block:: python
    :linenos:
    :emphasize-lines: 22-41

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        return next_light


    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        return next_light

* I change the call to the ``show`` :ref:`function<what is a function?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change the `return statement`_ of the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 19

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        return next_light, 'WALK'

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the expectation of the second :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 16

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I change the call in the :ref:`assertion<what is an assertion?>` from ``show`` to ``show_walk``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12-13

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=False
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('GREEN', 'WALK') != ('GREEN', 'NO WALK')

* I add a ``walk`` :ref:`variable<what is a variable?>` to the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 7

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:

* I use the ``walk`` :ref:`variable<what is a variable?>` in the :ref:`if statement<if statements>` for when the light is :red:`RED`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light, walk = red, 'WALK'
                else:
                    next_light = green
        else:
            next_light = current_light

* I use the ``walk`` :ref:`variable<what is a variable?>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 20

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light, walk = red, 'WALK'
                else:
                    next_light = green
        else:
            next_light = current_light

        return next_light, walk

  the test passes

* I change the third :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 21-22, 26

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=False
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('RED', 'NO WALK') != ('RED', 'WALK')

* I add an :ref:`if statement<if statements>` for it to the :ref:`else clause<if statements>` in the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 19-20

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light, walk = red, 'WALK'
                else:
                    next_light = green
        else:
            next_light = current_light
            if current_light == red:
                walk = 'WALK'

        return next_light, walk

  the test passes

* I change the last :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 10

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=False
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=False,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_traffic_light_when_yellow_w_walk_button(self):

  the test is still green

----

* I change the first :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-4, 9

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('RED', 'NO WALK') != ('RED', 'WALK')

* I add an :ref:`if statement<if statements>` to the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 22-23

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light, walk = red, 'WALK'
                else:
                    next_light = green
        else:
            next_light = current_light
            if current_light == red:
                walk = 'WALK'

        if next_light == red:
            walk = 'WALK'

        return next_light, walk

  the test passes. I forgot that from the :ref:`truth table` of the Traffic Light, it only shows :green:`WALK` when the light is :red:`RED`

* I comment out the last two statements I added

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 14-15, 20-21

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    # next_light, walk = red, 'WALK'
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light
            # if current_light == red:
            #     walk = 'WALK'

        if next_light == red:
            walk = 'WALK'

        return next_light, walk

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        if next_light == red:
            walk = 'WALK'

        return next_light, walk

  still green

* I change the second :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_yellow_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 13-14, 19

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

  the test is still green

* I change the third :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 23-24, 29

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

  still green

* I change the last :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 33-34, 39

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

  the test is still green

* I have used ``NO WALK`` and ``WALK`` enough times, that I add :ref:`global variables<what is a variable?>` for them

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'
    WALK = (RED, 'WALK')
    NO_WALK = 'NO WALK'


    class TestTrafficLight(unittest.TestCase):

* I use the new :ref:`variables<what is a variable?>` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 8-9, 18-19, 28-29, 38-39

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=True,
                    walk_button=False
                ),
                # (GREEN, 'NO WALK')
                (GREEN, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=False,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    timer_done=False,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

  still green

* I use them in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 9-11, 20-21, 31-32, 42-43

    def test_traffic_light_when_yellow_w_walk_button(self):
        self.assertEqual(
            # src.traffic_light.show(
            src.traffic_light.show_walk(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            ),
            # (RED, 'WALK')
            WALK
        )

        self.assertEqual(
            # src.traffic_light.show(
            src.traffic_light.show_walk(
                current_light=YELLOW,
                timer_done=True,
                walk_button=False,
            ),
            # (RED, 'WALK')
            WALK
        )

        self.assertEqual(
            # src.traffic_light.show(
            src.traffic_light.show_walk(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            ),
            # (YELLOW, 'NO WALK')
            (YELLOW, NO_WALK)
        )

        self.assertEqual(
            # src.traffic_light.show(
            src.traffic_light.show_walk(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            ),
            # (YELLOW, 'NO WALK')
            (YELLOW, NO_WALK)
        )

----

* I change the first :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 3-4, 9

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, NO_WALK)
            )

  the test is still green

* I change the second :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 13-14, 19

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, NO_WALK)
            )

  still green

* I change the third :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 23-24, 29

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, NO_WALK)
            )

* I change the last :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 33-34, 39

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, NO_WALK)
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                (GREEN, NO_WALK)
            )

  still green

----

* I remove the ``show`` :ref:`function<what is a function?>` from ``traffic_light.py`` since it is no longer used

  .. code-block:: python
    :linenos:

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        if next_light == red:
            walk = 'WALK'

        return next_light, walk

* Since my new solution works, I right click on the name ``show_walk`` and select ``Rename Symbol`` (`Visual Studio Code`_) to change the name to ``show`` and all tests are still green

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):


### REFACTOR ``show``


* I add 2 :ref:`global variables<what is a variable?>` to ``test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-9

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'
    NO_WALK = 'NO WALK'
    WALK = (RED, 'WALK')
    YELLOW_NO_WALK = (YELLOW, NO_WALK)
    GREEN_NO_WALK = (GREEN, NO_WALK)


    class TestTrafficLight(unittest.TestCase):

* I use ``GREEN_NO_WALK`` for ``(GREEN, NO_WALK)`` in the second :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines:

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False
                ),
                # (GREEN, 'NO WALK')
                # (GREEN, NO_WALK)
                GREEN_NO_WALK
            )

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False
                ),
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=False,
                ),
                WALK
            )

        def test_traffic_light_when_yellow_w_walk_button(self):

* I use ``YELLOW_NO_WALK`` for ``(YELLOW, NO_WALK)`` in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 32-33, 44-45

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                # (YELLOW, NO_WALK)
                YELLOW_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                # (YELLOW, 'NO WALK')
                # (YELLOW, NO_WALK)
                YELLOW_NO_WALK
            )

  still green

* I remove the commented lines from :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 47

        def test_traffic_light_when_yellow_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW_NO_WALK
            )

        def test_traffic_light_when_green_w_walk_button(self):

* I use ``YELLOW_NO_WALK`` for ``(YELLOW, NO_WALK)`` in :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 9-10, 20-21

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, NO_WALK)
                YELLOW_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                # (YELLOW, NO_WALK)
                YELLOW_NO_WALK
            )

  green

* I use ``GREEN_NO_WALK`` for ``(GREEN, NO_WALK)``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 31-32, 42-43

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, NO_WALK)
                YELLOW_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                # (YELLOW, NO_WALK)
                YELLOW_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                # (GREEN, NO_WALK)
                GREEN_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                # (GREEN, NO_WALK)
                GREEN_NO_WALK
            )


    # Exceptions seen

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 84

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                GREEN_NO_WALK
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

----

* I add a :ref:`conditional expression<conditional expressions>` at the top of the `show` :ref:`function<what is a function?>` with an :ref:`if statement<if statements>` for when the timer is NOT done

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-14

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if not timer_done:
            return current_light, (
                'WALK'
                if current_light == red
                else 'NO WALK'
            )

        if timer_done:

  green

* I add an :ref:`if statement<if statements>` for when the light is :green:`GREEN`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-17

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if not timer_done:
            return current_light, (
                'WALK'
                if current_light == red
                else 'NO WALK'
            )

        if current_light == green:
            return yellow, 'NO WALK'

        if timer_done:

  still green

* I add an :ref:`if statement<if statements>` for when the light is :red:`RED`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 18-23

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if not timer_done:
            return current_light, (
                'WALK'
                if current_light == red
                else 'NO WALK'
            )

        if current_light == green:
            return yellow, 'NO WALK'
        if current_light == red:
            return (
                (red, 'WALK')
                if walk_button
                else (green, 'NO WALK')
            )

        if timer_done:

  the test is still green

* I add a `return statement`_ for the default case which covers when the light is :yellow:`YELLOW`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 25

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if not timer_done:
            return current_light, (
                'WALK'
                if current_light == red
                else 'NO WALK'
            )

        if current_light == green:
            return yellow, 'NO WALK'
        if current_light == red:
            return (
                (red, 'WALK')
                if walk_button
                else (green, 'NO WALK')
            )

        return (red, 'WALK')

        if timer_done:
            if current_light == green:
                next_light = yellow
            if current_light == red:
                if walk_button:
                    next_light = red
                else:
                    next_light = green
        else:
            next_light = current_light

        if next_light == red:
            walk = 'WALK'

        return next_light, walk

  still green

* I remove the other statements

  .. code-block:: python
    :linenos:

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'NO WALK'

        if not timer_done:
            return current_light, (
                'WALK'
                if current_light == red
                else 'NO WALK'
            )

        if current_light == green:
            return yellow, 'NO WALK'
        if current_light == red:
            return (
                (red, 'WALK')
                if walk_button
                else (green, 'NO WALK')
            )

        return (red, 'WALK')

* I change the value of the ``walk`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'WALK'

        if not timer_done:

* I use it to remove repetition in the statements

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12, 21-22, 27-28

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        next_light = red
        walk = 'WALK'

        if not timer_done:
            return current_light, (
                # 'WALK'
                walk
                if current_light == red
                else 'NO WALK'
            )

        if current_light == green:
            return yellow, 'NO WALK'
        if current_light == red:
            return (
                # (red, 'WALK')
                (red, walk)
                if walk_button
                else (green, 'NO WALK')
            )

        # return (red, 'WALK')
        return (red, walk)

  green

* I change the ``next_light`` :ref:`variable<what is a variable?>` to ``no_walk``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        no_walk = 'NO WALK'
        walk = 'WALK'

        if not timer_done:

* I use it to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19-20, 26-27

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        no_walk = 'NO WALK'
        walk = 'WALK'

        if not timer_done:
            return current_light, (
                # 'WALK'
                walk
                if current_light == red
                # else 'NO WALK'
                else no_walk
            )

        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk
        if current_light == red:
            return (
                # (red, 'WALK')
                (red, walk)
                if walk_button
                # else (green, 'NO WALK')
                else (green, no_walk)
            )

        # return (red, 'WALK')
        return (red, walk)

  still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        no_walk = 'NO WALK'
        walk = 'WALK'

        if not timer_done:
            return current_light, (
                walk
                if current_light == red
                else no_walk
            )

        if current_light == green:
            return yellow, no_walk
        if current_light == red:
            return (
                (red, walk)
                if walk_button
                else (green, no_walk)
            )

        return (red, walk)

----

*************************************************************************************
review
*************************************************************************************

I ran tests for a Traffic Light that has a timer and a button for people to push when they want to walk. If the inputs are

* what color is the light now?
* is the timer done?
* did the person push the walk button?

then this is the :ref:`truth table` for the Traffic Light

================  ==============  ==============  =================================
current light     timer done      walk button     show
================  ==============  ==============  =================================
:red:`RED`        :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
:red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :red:`no`       :green:`yes`    :red:`RED` + :green:`WALK`
:red:`RED`        :red:`no`       :red:`no`       :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`no`       :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :red:`no`       :green:`GREEN` + :red:`NO WALK`
================  ==============  ==============  =================================

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Traffic Light: tests and solutions>`

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