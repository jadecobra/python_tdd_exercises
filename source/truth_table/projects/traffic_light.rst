.. meta::
  :description: Build a real-world Traffic Light using truth tables and Test-Driven Development in Python. Learn how boolean logic controls physical systems like traffic signals.
  :keywords: Jacob Itegboje, python truth table, Traffic Light python, tdd python, real world boolean logic, state machine truth table, pumping python

.. include:: ../../links.rst

.. _traffic_light:

#################################################################################
Traffic Light
#################################################################################

----

I want to make a **Traffic Light** that changes color based on a timer. If the inputs are

* what color is the light now?
* is the timer done?

then this is the :ref:`truth table` I get

=====================  ===================  =================
current light (first)  timer done (second)  show (output)
=====================  ===================  =================
:red:`RED`             :green:`yes`         :green:`GREEN`
:red:`RED`             :red:`no`            :red:`RED`
:yellow:`YELLOW`       :green:`yes`         :red:`RED`
:yellow:`YELLOW`       :red:`no`            :yellow:`YELLOW`
:green:`GREEN`         :green:`yes`         :yellow:`YELLOW`
:green:`GREEN`         :red:`no`            :green:`GREEN`
=====================  ===================  =================

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

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

  the terminal_ is my friend, and shows I am in the ``traffic_light`` folder_

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

* I set up the project with uv_

  .. code-block:: python
    :emphasize-lines: 1

    uv init

  the terminal_ shows

  .. code-block:: shell

    Initialized project `traffic-light`

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

I change ``test_failure`` to ``test_traffic_light_when_red``, then add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED` and the timer is done

================  ==============  =================
current light     timer done      show
================  ==============  =================
:red:`RED`        :green:`yes`    :green:`GREEN`
================  ==============  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestTrafficLight(unittest.TestCase):

      def test_traffic_light_when_red(self):
          my_expectation = 'GREEN'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=True,
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

    import src.traffic_light
    import unittest


    class TestTrafficLight(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: show() got an unexpected keyword argument 'current_light'

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5
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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: show() got an unexpected keyword argument 'timer_done'

* I add ``timer_done`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(current_light, timer_done):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'GREEN'

* I change the `return statement`_ to give the test what it expects

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(current_light, timer_done):
        return 'GREEN'

  the test passes. The ``show`` :ref:`function<what is a function?>` always returns :green:`GREEN`, it does not care about the inputs. Is this :ref:`Contradiction<test_contradiction>` or :ref:`Tautology<test_tautology>`?

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the current light is :red:`RED` and the timer is NOT done, in ``test_traffic_light.py``

  ================  ==============  =================
  current light     timer done      show
  ================  ==============  =================
  :red:`RED`        :green:`yes`    :green:`GREEN`
  :red:`RED`        :red:`no`       :red:`RED`
  ================  ==============  =================

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

  the test passes. The ``show`` :ref:`function<what is a function?>` returns

  * :green:`GREEN` if the timer is done
  * :red:`RED` if the timer is NOT done

----

*********************************************************************************
test_traffic_light_when_yellow
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the traffic light is :yellow:`YELLOW` and the timer is done, to ``test_traffic_light.py``

================  ==============  =================
current light     timer done      show
================  ==============  =================
:red:`RED`        :green:`yes`    :green:`GREEN`
:red:`RED`        :red:`no`       :red:`RED`
:yellow:`YELLOW`  :green:`yes`    :red:`RED`
================  ==============  =================

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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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
  :emphasize-lines: 4-5

  def show(current_light, timer_done):
      if not timer_done:
          return 'RED'
      if current_light == 'YELLOW':
          return 'RED'
      return 'GREEN'

the test passes.

The ``show`` :ref:`function<what is a function?>` returns

* :red:`RED` if the timer is done and the current light is :yellow:`YELLOW`
* :red:`RED` if the timer is NOT done
* :green:`GREEN` if the timer is done and the current light is NOT :yellow:`YELLOW` and if none of the conditions are met

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW` and the timer is NOT done to ``test_traffic_light.py``

  ================  ==============  =================
  current light     timer done      show
  ================  ==============  =================
  :red:`RED`        :green:`yes`    :green:`GREEN`
  :red:`RED`        :red:`no`       :red:`RED`
  :yellow:`YELLOW`  :green:`yes`    :red:`RED`
  :yellow:`YELLOW`  :red:`no`       :yellow:`YELLOW`
  ================  ==============  =================

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'YELLOW'

* I add an :ref:`if statement<if statements>` to the one for when the timer is NOT done, in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def show(current_light, timer_done):
        if not timer_done:
            if current_light == 'YELLOW':
                return 'YELLOW'
            return 'RED'
        if current_light == 'YELLOW':
            return 'RED'
        return 'GREEN'

  the test passes.

The ``show`` :ref:`function<what is a function?>` returns

* :red:`RED` if the timer is done and the current light is :yellow:`YELLOW`
* :red:`RED` if the timer is NOT done and the current light is NOT :yellow:`YELLOW`
* :yellow:`YELLOW` if the timer is NOT done and the current light is :yellow:`YELLOW`
* :green:`GREEN` if the timer is done and the current light is NOT :yellow:`YELLOW` and if none of the conditions are met

----

*********************************************************************************
test_traffic_light_when_green
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the traffic light is :green:`GREEN` and the timer is done, to ``test_traffic_light.py``

================  ==============  =================
current light     timer done      show
================  ==============  =================
:red:`RED`        :green:`yes`    :green:`GREEN`
:red:`RED`        :red:`no`       :red:`RED`
:yellow:`YELLOW`  :green:`yes`    :red:`RED`
:yellow:`YELLOW`  :red:`no`       :yellow:`YELLOW`
:green:`GREEN`    :green:`yes`    :yellow:`YELLOW`
================  ==============  =================

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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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
  :emphasize-lines: 8-9

  def show(current_light, timer_done):
      if not timer_done:
          if current_light == 'YELLOW':
              return 'YELLOW'
          return 'RED'
      if current_light == 'YELLOW':
          return 'RED'
      if current_light == 'GREEN':
          return 'YELLOW'
      return 'GREEN'

the test passes.

The ``show`` :ref:`function<what is a function?>` returns

* :yellow:`YELLOW` if the timer is done and the current light is :green:`GREEN`
* :red:`RED` if the timer is done and the current light is :yellow:`YELLOW`
* :red:`RED` if the timer is NOT done and the current light is NOT :yellow:`YELLOW`
* :yellow:`YELLOW` if the timer is NOT done and the current light is :yellow:`YELLOW`
* :green:`GREEN` if the timer is done and the current light is NOT :yellow:`YELLOW` and is NOT :green:`GREEN` and if none of the other conditions are met

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN` and the timer is NOT done, to ``test_traffic_light.py``

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'GREEN'

* I add an :ref:`if statement<if statements>` to the one for when the timer is NOT done in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def show(current_light, timer_done):
        if not timer_done:
            if current_light == 'YELLOW':
                return 'YELLOW'
            if current_light == 'GREEN':
                return 'GREEN'
            return 'RED'
        if current_light == 'YELLOW':
            return 'RED'
        if current_light == 'GREEN':
            return 'YELLOW'
        return 'GREEN'

  the test passes. The ``show`` :ref:`function<what is a function?>` returns

  * :yellow:`YELLOW` if the timer is NOT done and the current light is :yellow:`YELLOW`
  * :green:`GREEN` if the timer is NOT done and the current light is :green:`GREEN`
  * :red:`RED` if the timer is NOT done and the current light is NOT :yellow:`YELLOW`
  * :red:`RED` if the timer is done and the current light is :yellow:`YELLOW`
  * :yellow:`YELLOW` if the timer is done and the current light is :green:`GREEN`
  * :green:`GREEN` if the timer is done and the current light is :red:`RED` or if none of the conditions are met

* I add an :ref:`if statement<if statements>` for when the timer is NOT done and the light is :red:`RED`, to be clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def show(current_light, timer_done):
        if not timer_done:
            if current_light == 'YELLOW':
                return 'YELLOW'
            if current_light == 'GREEN':
                return 'GREEN'
            if current_light == 'RED':
                return 'RED'
        if current_light == 'YELLOW':
            return 'RED'
        if current_light == 'GREEN':
            return 'YELLOW'
        return 'GREEN'

  the test is still green. The ``show`` :ref:`function<what is a function?>` returns the current light when the timer is NOT done

* I add a `return statement`_ to return the current light when the timer is NOT done

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def show(current_light, timer_done):
        if not timer_done:
            return current_light
            if current_light == 'YELLOW':
                return 'YELLOW'
            if current_light == 'GREEN':
                return 'GREEN'
            if current_light == 'RED':
                return 'RED'
        if current_light == 'YELLOW':
            return 'RED'
        if current_light == 'GREEN':
            return 'YELLOW'
        return 'GREEN'

  still green

* I remove the other :ref:`if statements<if statements>` from the one for when the timer is NOT done (lines 4-9)

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        if not timer_done:
            return current_light
        if current_light == 'YELLOW':
            return 'RED'
        if current_light == 'GREEN':
            return 'YELLOW'
        return 'GREEN'

* I add :ref:`variables<what is a variable?>` for the colors to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(current_light, timer_done):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == 'YELLOW':
            return 'RED'
        if current_light == 'GREEN':
            return 'YELLOW'
        return 'GREEN'

* I use the new :ref:`variables<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7, 9-14

    def show(current_light, timer_done):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        # if current_light == 'YELLOW':
        if current_light == yellow:
            return 'RED'
        # if current_light == 'GREEN':
        if current_light == green:
            # return 'YELLOW'
            return yellow
        # return 'GREEN'
        return green

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return 'RED'
        if current_light == green:
            return yellow
        return green

----

*********************************************************************************
test_traffic_light_when_red_w_walk_button
*********************************************************************************

----

So far, the :ref:`truth table` for the Traffic Light is

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

I want to add a walk button for a person to push when they want to cross the street, the inputs for the traffic light will then be

* did the person push the walk button?
* what color is the light now?
* is the timer done?

and the :ref:`truth table` for the cases where the traffic light is :red:`RED` is

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

================  ==============  ==============  =================
current light     timer done      walk button     show
================  ==============  ==============  =================
:red:`RED`        :green:`yes`    :green:`yes`    :red:`RED`
================  ==============  ==============  =================

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

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

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

  the terminal_ is my friend, and shows 3 failures with :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_traffic_light_when_green - TypeError: show() missing 1 required positional arg...
    FAILED ...test_traffic_light_when_red - TypeError: show() missing 1 required positional arg...
    FAILED ...test_traffic_light_when_yellow - TypeError: show() missing 1 required positional arg...

* I could add the ``walk_button`` parameter to every call to the ``show`` :ref:`function<what is a function?>` in every test or add a :ref:`default value<test_functions_w_default_arguments>` for the new :ref:`keyword argument<test_functions_w_keyword_arguments>` to make it a choice NOT a requirement. I make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def show(
            current_light, timer_done,
            walk_button=False,
        ):

  the test passes because

  .. code-block:: python

    src.traffic_light.show(
        current_light='RED',
        timer_done=False,
    )

  is now the same as

  .. code-block:: python

    src.traffic_light.show(
        current_light='RED',
        timer_done=False,
        walk_button=False,
    )

  because the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` is :ref:`False<test_what_is_false>`

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

* I add an :ref:`if statement<if statements>` to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13-14

    def show(
            current_light, timer_done,
            walk_button=False,
        ):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return 'RED'
        if current_light == green:
            return yellow
        if walk_button:
            return 'RED'
        return green

  the test passes

* I add a :ref:`variable<what is a variable?>` for :red:`RED`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def show(
            current_light, timer_done,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:

* I use the :ref:`variable<what is a variable?>` to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11, 15-16

    def show(
            current_light, timer_done,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            # return 'RED'
            return red
        if current_light == green:
            return yellow
        if walk_button:
            # return 'RED'
            return red
        return green

  the test is green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(
            current_light, timer_done,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red
        return green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is done and the walk button has not been pushed, to :ref:`test_traffic_light_when_red` in ``test_traffic_light.py``

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :red:`RED`        :green:`yes`    :green:`yes`    :red:`RED`
  :red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN`
  ================  ==============  ==============  =================

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is NOT done and the walk button is pressed

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :red:`RED`        :green:`yes`    :green:`yes`    :red:`RED`
  :red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN`
  :red:`RED`        :red:`no`       :green:`yes`    :red:`RED`
  ================  ==============  ==============  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 22

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
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is NOT done and the walk button is not pressed

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :red:`RED`        :green:`yes`    :green:`yes`    :red:`RED`
  :red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN`
  :red:`RED`        :red:`no`       :green:`yes`    :red:`RED`
  :red:`RED`        :red:`no`       :red:`no`       :red:`RED`
  ================  ==============  ==============  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 26-32

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
                walk_button=False,
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

  green

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
    :emphasize-lines: 4-5, 7-8, 16-17, 23-24, 26-27, 33-34, 36-37

        def test_traffic_light_when_red(self):
            red = 'RED'

            # my_expectation = 'RED'
            my_expectation = red
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=True,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'RED'
            my_expectation = red
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'RED'
            my_expectation = red
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I use the :ref:`variable<what is a variable?>` for ``my_expectation`` when it is :red:`RED`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5, 12-13, 25, 32-33, 36, 43-44

        def test_traffic_light_when_red(self):
            red = 'RED'

            # my_expectation = 'RED'
            # my_expectation = red
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
                walk_button=False,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'RED'
            # my_expectation = red
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            # my_expectation = 'RED'
            # my_expectation = red
            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

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
                walk_button=False,
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

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``current_light`` :ref:`keyword argument<test_functions_w_keyword_arguments>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(
            current_light='RED', timer_done,
            walk_button=False,
        ):

  the terminal_ is my friend, and shows SyntaxError_

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

* I add a :ref:`default value<test_functions_w_default_arguments>` for ``timer_done`` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def show(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):

  the test is green again. All the arguments in the :ref:`function<what is a function?>` are now choices, which means

  .. code-block:: python

    src.traffic_light.show()

  is the same as

  .. code-block:: python

    src.traffic_light.show(
        current_light='RED',
        timer_done=False,
        walk_button=False,
    )

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
                walk_button=False,
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

The truth table when the traffic light is :yellow:`YELLOW` with the walk button is

================  ==============  ==============  =================
current light     timer done      walk button     show
================  ==============  ==============  =================
:yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED`
:yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED`
:yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`no`       :red:`no`       :yellow:`YELLOW`
================  ==============  ==============  =================

* I add ``walk_button`` to the call to ``src.traffic_light.show`` in the first :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_yellow` in ``test_traffic_light.py``

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED`
  ================  ==============  ==============  =================

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

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED`
  :yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED`
  ================  ==============  ==============  =================

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

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>`, for when the light is :yellow:`YELLOW`, the timer is NOT done and the walk button is pushed

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED`
  :yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED`
  :yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW`
  ================  ==============  ==============  =================

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 5

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is NOT done and the walk button is NOT pushed

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED`
  :yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED`
  :yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW`
  :yellow:`YELLOW`  :red:`no`       :red:`no`       :yellow:`YELLOW`
  ================  ==============  ==============  =================

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

  the test is still green

* I add a :ref:`variable<what is a variable?>` for :red:`RED` (a repetition)

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 2

        def test_traffic_light_when_yellow_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            my_expectation = 'RED'

* I use the new :ref:`variable<what is a variable?>` to remove repetition, such irony

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

  still green

* I make :ref:`global variables<what is a variable?>` for the colors at the top of the file_ since :red:`RED` is used in both :ref:`test_traffic_light_when_yellow_w_walk_button` and :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW = 'RED', 'YELLOW'


    class TestTrafficLight(unittest.TestCase):

* I use the :red:`RED` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 12-13, 23-24

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
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

  green

* I use the :yellow:`YELLOW` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7-8, 19-20, 31-32, 37-38, 43-44, 49-50

        def test_traffic_light_when_yellow_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            # my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=True,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, yellow)
            self.assertEqual(reality, YELLOW)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, yellow)
            self.assertEqual(reality, YELLOW)

  still green

* I remove the comments and the ``red`` and ``yellow`` :ref:`local variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 38

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

* I use the :red:`RED` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 8-9, 22-23, 29-30

        def test_traffic_light_when_red_w_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False,
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

  the test is still green

* I remove the commented lines and the ``red`` :ref:`local variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 10

        def test_traffic_light_when_red_w_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False,
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

        def test_traffic_light_when_yellow_w_walk_button(self):

----

*********************************************************************************
test_traffic_light_when_green_w_walk_button
*********************************************************************************

The truth table when the traffic light is :green:`GREEN` with the walk button is

================  ==============  ==============  =================
current light     timer done      walk button     show
================  ==============  ==============  =================
:green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW`
:green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW`
:green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN`
:green:`GREEN`    :red:`no`       :red:`no`       :green:`GREEN`
================  ==============  ==============  =================

* I add ``walk_button`` to the call to ``src.traffic_light.show`` in the first :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_green` in ``test_traffic_light.py``

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW`
  ================  ==============  ==============  =================

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

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW`
  ================  ==============  ==============  =================

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

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW`
  :green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN`
  ================  ==============  ==============  =================

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

  ================  ==============  ==============  =================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW`
  :green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN`
  :green:`GREEN`    :red:`no`       :red:`no`       :green:`GREEN`
  ================  ==============  ==============  =================

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

* I use the :green:`GREEN` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_traffic_light_when_green`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 4-5, 13-14, 20, 22-23, 27-28, 30, 32-33, 37-38

        def test_traffic_light_when_green(self):
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

  green

* I use the :yellow:`YELLOW` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_traffic_light_when_green`

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 2, 9-10, 12, 19-20

        def test_traffic_light_when_green(self):
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

  still green

* I change the name of the test from :ref:`test_traffic_light_when_green` to :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 8

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=False,
            )
            self.assertEqual(reality, YELLOW)

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

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 65

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


    # Exceptions seen

* I use the :green:`GREEN` :ref:`global variable<what is a variable?>` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 1, 6-7

            # my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=False,
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
                walk_button=False,
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

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I can remove the ``reality`` :ref:`variable<what is a variable?>`, since it is only used once for each :ref:`assertion<what is an assertion?>`, I can make the call to ``src.traffic_light.show`` directly, in :ref:`test_traffic_light_when_red_w_walk_button`

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
                walk_button=False,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False,
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
                    walk_button=False,
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

* I do the same thing with :ref:`test_traffic_light_when_yellow_w_walk_button`

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

        def test_traffic_light_when_green_w_walk_button(self):

* I also do it with :ref:`test_traffic_light_when_green_w_walk_button`

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
    :lineno-start: 80

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

================  ==============  ==============  =================================
current light     timer done      walk button     show
================  ==============  ==============  =================================
:red:`RED`        :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
================  ==============  ==============  =================================

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

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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
    :emphasize-lines: 15-16

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red

        return green, 'WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_traffic_light_when_green_w_walk_button - AssertionError: ('YELLOW', 'WALK') != 'YELLOW'
    FAILED ...test_traffic_light_when_red_w_walk_button - AssertionError: ('GREEN', 'WALK') != 'GREEN'
    FAILED ...test_traffic_light_when_yellow_w_walk_button - AssertionError: ('RED', 'WALK') != 'RED'

  my solution broke all the tests

* I remove ``WALK`` from the `return statement`_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1

        return green

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I make a copy of the ``show`` :ref:`function<what is a function?>` and paste it below, then change the name to ``show_walk``, this way I keep what works while I try a new solution

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19-23, 25-32, 34

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red

        return green


    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red

        return green

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

* I change the `return statement`_ for when the ``walk_button`` is pushed, in the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 14

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red, 'WALK'

        return green

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the expectation of the second :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :red:`RED`        :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN` + :red:`NO WALK`
  ================  ==============  ==============  =================================

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
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I change the call in the second :ref:`assertion<what is an assertion?>` from ``show`` to ``show_walk``

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I add ``'NO WALK'`` to the `return statement`_ of the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 16

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the third :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :red:`RED`        :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN` + :red:`NO WALK`
  :red:`RED`        :red:`no`       :green:`yes`    :red:`RED` + :green:`WALK`
  ================  ==============  ==============  =================================

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
                    walk_button=False,
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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I add ``'WALK'`` to the :ref:`if statement<if statements>` for when the timer is NOT done, in the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light, 'WALK'
        if current_light == yellow:
            return red
        if current_light == green:
            return yellow
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the last :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_red_w_walk_button` in ``test_traffic_light.py``

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :red:`RED`        :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`yes`    :red:`no`       :green:`GREEN` + :red:`NO WALK`
  :red:`RED`        :red:`no`       :green:`yes`    :red:`RED` + :green:`WALK`
  :red:`RED`        :red:`no`       :red:`no`       :red:`RED` + :green:`WALK`
  ================  ==============  ==============  =================================

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
                    walk_button=False,
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

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  ================  ==============  ==============  =================================

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I add ``'WALK'`` to the :ref:`if statement<if statements>` for when the current light is :yellow:`YELLOW`, in the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 10

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light, 'WALK'
        if current_light == yellow:
            return red, 'WALK'
        if current_light == green:
            return yellow
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the second :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_yellow_w_walk_button` in ``test_traffic_light.py``

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED` + :green:`WALK`
  ================  ==============  ==============  =================================

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

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
  ================  ==============  ==============  =================================

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('YELLOW', 'WALK') != ('YELLOW', 'NO WALK')

* I add an :ref:`if statement<if statements>` to the one for when the timer is not done, in the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8-9

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light, 'WALK'
        if current_light == yellow:
            return red, 'WALK'
        if current_light == green:
            return yellow
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the last :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_yellow_w_walk_button` in ``test_traffic_light.py``

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :red:`no`       :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
  :yellow:`YELLOW`  :red:`no`       :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
  ================  ==============  ==============  =================================

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

        def test_traffic_light_when_green_w_walk_button(self):

  the test is still green

----

* I change the first :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_when_green_w_walk_button`

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
  ================  ==============  ==============  =================================

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4, 9

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != ('YELLOW', 'NO WALK')

* I add ``'NO WALK'`` to the :ref:`if statement<if statements>` for when the current light is :green:`GREEN`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 14

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light, 'WALK'
        if current_light == yellow:
            return red, 'WALK'
        if current_light == green:
            return yellow, 'NO WALK'
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the second :ref:`assertion<what is an assertion?>`

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
  ================  ==============  ==============  =================================

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 13-14, 19

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

  the test is still green

* I change the third :ref:`assertion<what is an assertion?>`

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN` + :red:`NO WALK`
  ================  ==============  ==============  =================================

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 23-24, 29

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('GREEN', 'WALK') != ('GREEN', 'NO WALK')

* I add an :ref:`if statement<if statements>` to the one for when the timer is NOT done, in the ``show_walk`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 8-9

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == green:
                return current_light, 'NO WALK'
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light, 'WALK'
        if current_light == yellow:
            return red, 'WALK'
        if current_light == green:
            return yellow, 'NO WALK'
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the last :ref:`assertion<what is an assertion?>`

  ================  ==============  ==============  =================================
  current light     timer done      walk button     show
  ================  ==============  ==============  =================================
  :green:`GREEN`    :green:`yes`    :green:`yes`    :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`yes`    :red:`no`       :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :red:`no`       :green:`yes`    :green:`GREEN` + :red:`NO WALK`
  :green:`GREEN`    :red:`no`       :red:`no`       :green:`GREEN` + :red:`NO WALK`
  ================  ==============  ==============  =================================

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 33-34, 39

        def test_traffic_light_when_green_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show_walk(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )


    # Exceptions seen

  the test is still green

----

* I remove the ``show`` :ref:`function<what is a function?>` from ``traffic_light.py`` since it is no longer used

  .. code-block:: python
    :linenos:

    def show_walk(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):

* Since my new solution works, I right click on the name ``show_walk`` and select ``Rename Symbol`` (`Visual Studio Code`_) to change the name to ``show`` and all tests are still green

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == green:
                return current_light, 'NO WALK'
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light, 'WALK'
        if current_light == yellow:
            return red, 'WALK'
        if current_light == green:
            return yellow, 'NO WALK'
        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  green

  .. TIP:: ``Rename Symbol`` changes the name everywhere in the code that it is used or defined, including the tests

* I add more :ref:`global variables<what is a variable?>` to ``test_traffic_light.py``

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

* I use ``GREEN_NO_WALK`` for ``(GREEN, 'NO WALK')`` in the second :ref:`assertion<what is an assertion?>` of :ref:`test_traffic_light_when_red_w_walk_button`


  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-8

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

  the test is still green

* I use ``WALK`` for ``(RED, 'WALK')`` in :ref:`test_traffic_light_when_red_w_walk_button`

  .. NOTE:: ``Rename Symbol`` changes the names of the calls to ``src.traffic_light.show_walk`` to ``src.traffic_light.show`` in the tests

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-9, 28-29, 38-39

        def test_traffic_light_when_red_w_walk_button(self):
            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    timer_done=False,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

  still green

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
                    walk_button=False,
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

* I use ``WALK`` for ``(RED, 'WALK')`` in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 9-10, 20-21

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

  green

* I use ``YELLOW_NO_WALK`` for ``(YELLOW, 'NO WALK')`` in :ref:`test_traffic_light_when_yellow_w_walk_button`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 8-9, 19-20

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
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

* I use ``YELLOW_NO_WALK`` for ``(YELLOW, 'NO WALK')`` in :ref:`test_traffic_light_when_green_w_walk_button`

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
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

  green

* I use ``GREEN_NO_WALK`` for ``(GREEN, 'NO WALK')`` in :ref:`test_traffic_light_when_green_w_walk_button`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 8-9, 19-20

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

            self.assertEqual(
                # src.traffic_light.show(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

  still green

* I remove the commented lines from :ref:`test_traffic_light_when_green_w_walk_button`

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

* I add :ref:`variables<what is a variable?>` for ``'WALK'`` and ``'NO WALK'`` to the ``show`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

* I use the new :ref:`variables<what is a variable?>` to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11, 13-14, 15-16, 18-19, 21-22, 24-25, 27-28

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            if current_light == green:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            if current_light == yellow:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            # return current_light, 'WALK'
            return current_light, walk
        if current_light == yellow:
            # return red, 'WALK'
            return red, walk
        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk
        if walk_button:
            # return red, 'WALK'
            return red, walk

        # return green, 'NO WALK'
        return green, no_walk

  the tests are still green

* The :ref:`if statements<if statements>` for when the timer is NOT done all return the current light, I add a statement for :red:`RED` to be clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-17

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            if current_light == green:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            if current_light == yellow:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            # return current_light, 'WALK'
            if current_light == red:
                return current_light, walk
        if current_light == yellow:
            # return red, 'WALK'
            return red, walk
        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk
        if walk_button:
            # return red, 'WALK'
            return red, walk

        # return green, 'NO WALK'
        return green, no_walk

  the tests are still green

* I write a new :ref:`if statement with an else clause<if statements>`, that covers the 3 cases when the timer is NOT done

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-12

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            if current_light != red:
                return current_light, no_walk
            else:
                return current_light, walk

  still green

* I add a :ref:`conditional expression<conditional expressions>` for the new :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 2-5

        if not timer_done:
            return current_light, (
                no_walk if current_light != red
                else walk
            )
            if current_light != red:

  green

* I remove the other :ref:`if statements<if statements>` from the one for when the timer is NOT done, and the commented lines

  .. code-block:: python
    :linenos:

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            return current_light, (
                no_walk if current_light != red
                else walk
            )
        if current_light == yellow:
            return red, walk
        if current_light == green:
            return yellow, no_walk
        if walk_button:
            return red, walk

        return green, no_walk

* I write out the :ref:`if statements<if statements>` for when the light is :red:`RED` and the timer is done, to be clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-7, 9

        if current_light == red:
            if not walk_button:
                return green, no_walk
            else:
                return red, walk
        # if walk_button:
        #     return red, walk

        # return green, no_walk

  still green

* I add a :ref:`conditional expression<conditional expressions>` for the :ref:`if statement<if statements>` with ``walk_button``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

        if current_light == red:
            return (
                (green, no_walk) if not walk_button
                else (red, walk)
            )
            if not walk_button:
                return green, no_walk
            else:
                return red, walk
        # if walk_button:
        #     return red, walk

        # return green, no_walk

  the tests are still green

* I remove the other :ref:`if statements<if statements>` and commented lines below the new statement

  .. code-block:: python
    :linenos:

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            return current_light, (
                no_walk if current_light != red
                else walk
            )

        if current_light == yellow:
            return red, walk

        if current_light == green:
            return yellow, no_walk

        if current_light == red:
            return (
                (green, no_walk) if not walk_button
                else (red, walk)
            )

* ``(red, walk)`` happens 3 times in the :ref:`function<what is a function?>`, I add a `return statement`_ to make it the default state of the light

  .. code-block:: python
    :linenos:
    :emphasize-lines: 23

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            return current_light, (
                no_walk if current_light != red
                else walk
            )

        if current_light == yellow:
            return red, walk

        if current_light == green:
            return yellow, no_walk

        if current_light == red:
            return (
                (green, no_walk) if not walk_button
                else (red, walk)
            )

        return red, walk

  still green. This means if no :ref:`conditions<if statements>` are met, the light stays :red:`RED`

* I no longer need the :ref:`if statement<if statements>` for :yellow:`YELLOW` because it returns the default state. I comment it out

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14-15

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            return current_light, (
                no_walk if current_light != red
                else walk
            )

        # if current_light == yellow:
        #     return red, walk

        if current_light == green:
            return yellow, no_walk

  green. Why does this work?

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk, no_walk = 'WALK', 'NO WALK'

        if not timer_done:
            return current_light, (
                no_walk if current_light != red
                else walk
            )

        if current_light == green:
            return yellow, no_walk

        if current_light == red:
            return (
                (green, no_walk) if not walk_button
                else (red, walk)
            )

        return red, walk

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_traffic_light.py`` and ``traffic_light.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``traffic_light``

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

What if there is an emergency vehicle present and the Traffic Light changes based on that as well? The inputs would be

* what color is the light now?
* is the timer done?
* did the person push the walk button?
* is there an emergency vehicle?

and the :ref:`truth table` would be

================  ==============  ==============  ===========  =================================
current light     timer done      walk button     emergency    show
================  ==============  ==============  ===========  =================================
:red:`RED`        :green:`yes`    :green:`yes`    :red:`yes`   :red:`RED` + :red:`NO WALK`
:red:`RED`        :green:`yes`    :green:`yes`    :green:`no`  :red:`RED` + :green:`WALK`
:red:`RED`        :green:`yes`    :red:`no`       :red:`yes`   :red:`RED` + :red:`NO WALK`
:red:`RED`        :green:`yes`    :red:`no`       :green:`no`  :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :red:`no`       :green:`yes`    :red:`yes`   :red:`RED` + :red:`NO WALK`
:red:`RED`        :red:`no`       :green:`yes`    :green:`no`  :red:`RED` + :green:`WALK`
:red:`RED`        :red:`no`       :red:`no`       :red:`yes`   :red:`RED` + :red:`NO WALK`
:red:`RED`        :red:`no`       :red:`no`       :green:`no`  :red:`RED` + :green:`WALK`
================  ==============  ==============  ===========  =================================

================  ==============  ==============  ===========  =================================
current light     timer done      walk button     emergency    show
================  ==============  ==============  ===========  =================================
:yellow:`YELLOW`  :green:`yes`    :green:`yes`    :red:`yes`   :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :green:`yes`    :green:`yes`    :green:`no`  :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`yes`    :red:`no`       :red:`yes`   :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :green:`yes`    :red:`no`       :green:`no`  :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`no`       :green:`yes`    :red:`yes`   :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`no`       :green:`yes`    :green:`no`  :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`no`       :red:`no`       :red:`yes`   :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`no`       :red:`no`       :green:`no`  :yellow:`YELLOW` + :red:`NO WALK`
================  ==============  ==============  ===========  =================================

================  ==============  ==============  ===========  =================================
current light     timer done      walk button     emergency    show
================  ==============  ==============  ===========  =================================
:green:`GREEN`    :green:`yes`    :green:`yes`    :red:`yes`   :red:`RED` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :green:`yes`    :green:`no`  :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :red:`no`       :red:`yes`   :red:`RED` + :red:`NO WALK`
:green:`GREEN`    :green:`yes`    :red:`no`       :green:`no`  :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :green:`yes`    :red:`yes`   :red:`RED` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :green:`yes`    :green:`no`  :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :red:`no`       :red:`yes`   :red:`RED` + :red:`NO WALK`
:green:`GREEN`    :red:`no`       :red:`no`       :green:`no`  :green:`GREEN` + :red:`NO WALK`
================  ==============  ==============  ===========  =================================

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