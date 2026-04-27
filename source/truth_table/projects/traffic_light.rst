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
current light (first)  timer (second)       show (output)
=====================  ===================  =================
:red:`RED`             :green:`done`        :green:`GREEN`
:red:`RED`             :red:`NOT done`      :red:`RED`
:yellow:`YELLOW`       :green:`done`        :red:`RED`
:yellow:`YELLOW`       :red:`NOT done`      :yellow:`YELLOW`
:green:`GREEN`         :green:`done`        :yellow:`YELLOW`
:green:`GREEN`         :red:`NOT done`      :green:`GREEN`
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
test_red_traffic_light
*********************************************************************************

The :ref:`truth table` for if the Traffic Light is :red:`RED` is

================  ===============  ================
current light     timer            show
================  ===============  ================
:red:`RED`        :green:`done`    :green:`GREEN`
:red:`RED`        :red:`NOT done`  :red:`RED`
================  ===============  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_red_traffic_light``, then add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED` and the timer is :green:`done`

================  ==============  =================
current light     timer done      show
================  ==============  =================
:red:`RED`        :green:`done`   :green:`GREEN`
================  ==============  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestTrafficLight(unittest.TestCase):

      def test_red_traffic_light(self):
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

  the ``show`` :ref:`function<what is a function?>` always returns :ref:`None<what is None?>` and the test expects ``'GREEN'``

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

* I add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED` and the timer is :red:`NOT done`, in ``test_traffic_light.py``

  ================  ===============  ================
  current light     timer            show
  ================  ===============  ================
  :red:`RED`        :green:`done`    :green:`GREEN`
  :red:`RED`        :red:`NOT done`  :red:`RED`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-14

        def test_red_traffic_light(self):
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

* I add an :ref:`if statement<if statements>` for this case, to ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def show(current_light, timer_done):
        if timer_done == False:
            return 'RED'
        return 'GREEN'

  the test passes

* I use bool_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def show(current_light, timer_done):
        # if timer_done == False:
        if bool(timer_done) == False:
            return 'RED'
        return 'GREEN'

  the test is still green

* I use :ref:`logical_negation (NOT)<test_logical_negation>` to write the statement in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def show(current_light, timer_done):
        # if timer_done == False:
        # if bool(timer_done) == False:
        if not bool(timer_done) == True:
            return 'RED'
        return 'GREEN'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def show(current_light, timer_done):
        # if timer_done == False:
        # if bool(timer_done) == False:
        # if not bool(timer_done) == True:
        if not bool(timer_done):
            return 'RED'
        return 'GREEN'

  green

* I remove bool_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def show(current_light, timer_done):
        # if timer_done == False:
        # if bool(timer_done) == False:
        # if not bool(timer_done) == True:
        # if not bool(timer_done):
        if not timer_done:
            return 'RED'
        return 'GREEN'

  still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(current_light, timer_done):
        if not timer_done:
            return 'RED'
        return 'GREEN'

  If the current Traffic Light is :red:`RED`, the ``show`` :ref:`function<what is a function?>` returns

  * :green:`GREEN` if the timer is :green:`done`
  * :red:`RED` if the timer is :red:`NOT done`

----

*********************************************************************************
test_yellow_traffic_light
*********************************************************************************

The :ref:`truth table` for if the Traffic Light is :yellow:`YELLOW` is

================  ===============  ================
current light     timer            show
================  ===============  ================
:yellow:`YELLOW`  :green:`done`    :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
================  ===============  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the traffic light is :yellow:`YELLOW` and the timer is :green:`done`, to ``test_traffic_light.py``

================  ===============  ================
current light     timer            show
================  ===============  ================
:yellow:`YELLOW`  :green:`done`    :red:`RED`
================  ===============  ================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 16-22

      def test_red_traffic_light(self):
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

      def test_yellow_traffic_light(self):
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
  :emphasize-lines: 5-6

  def show(current_light, timer_done):
      if not timer_done:
          return 'RED'

      if current_light == 'YELLOW':
          return 'RED'

      return 'GREEN'

the test passes.

The ``show`` :ref:`function<what is a function?>`

* returns :red:`RED` if the timer is :red:`NOT done`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

  - returns :red:`RED` if the current light is :yellow:`YELLOW`

* returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW` and the timer is :red:`NOT done`, to :ref:`test_yellow_traffic_light` in ``test_traffic_light.py``

  ================  ===============  ================
  current light     timer            show
  ================  ===============  ================
  :yellow:`YELLOW`  :green:`done`    :red:`RED`
  :yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9-14

        def test_yellow_traffic_light(self):
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

The ``show`` :ref:`function<what is a function?>`

* returns :yellow:`YELLOW` if the timer is :red:`NOT done` AND the current light is :yellow:`YELLOW`
* returns :red:`RED` if the timer is :red:`NOT done` AND the current light is NOT :yellow:`YELLOW`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

  - returns :red:`RED` if the current light is :yellow:`YELLOW`

* returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`

----

*********************************************************************************
test_green_traffic_light
*********************************************************************************

The :ref:`truth table` for if the Traffic Light is :green:`GREEN` is

================  ===============  ================
current light     timer            show
================  ===============  ================
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`GREEN`
================  ===============  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the traffic light is :green:`GREEN` and the timer is :green:`done`, to ``test_traffic_light.py``

================  ===============  ================
current light     timer            show
================  ===============  ================
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
================  ===============  ================

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 16-22

      def test_yellow_traffic_light(self):
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

      def test_green_traffic_light(self):
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
  :emphasize-lines: 10-11

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

The ``show`` :ref:`function<what is a function?>`

* returns :yellow:`YELLOW` if the timer is :red:`NOT done` AND the current light is :yellow:`YELLOW`
* returns :red:`RED` if the timer is :red:`NOT done` AND the current light is NOT :yellow:`YELLOW`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

  - returns :red:`RED` if the current light is :yellow:`YELLOW`

* checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

  - returns :yellow:`YELLOW` if the current light is :green:`GREEN`

* returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`
* returns :green:`GREEN` if none of the other conditions are met (this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN` and the timer is :red:`NOT done`, to ``test_traffic_light.py``

  ================  ===============  ================
  current light     timer            show
  ================  ===============  ================
  :green:`GREEN`    :green:`done`    :yellow:`YELLOW`
  :green:`GREEN`    :red:`NOT done`  :green:`GREEN`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 9-14

        def test_green_traffic_light(self):
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

* I add an :ref:`if statement<if statements>` to the one for when the timer is :red:`NOT done` in ``traffic_light.py``

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

  the test passes. The ``show`` :ref:`function<what is a function?>`

  * returns :yellow:`YELLOW` if the timer is :red:`NOT done` AND the current light is :yellow:`YELLOW`
  * returns :green:`GREEN` if the timer is :red:`NOT done` AND the current light is :green:`GREEN`
  * returns :red:`RED` if the timer is :red:`NOT done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN` (this covers the case where the timer is :red:`NOT done` AND the current light is :red:`RED`)
  * checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

    - returns :red:`RED` if the current light is :yellow:`YELLOW`

  * checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

    - returns :yellow:`YELLOW` if the current light is :green:`GREEN`

  * returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`
  * returns :green:`GREEN` if none of the other conditions are met (this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)


* I add an :ref:`if statement<if statements>` for when the timer is :red:`NOT done` and the light is :red:`RED`, to be clearer

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

  the test is still green. The ``show`` :ref:`function<what is a function?>` returns the current light when the timer is :red:`NOT done`

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

* I remove the other :ref:`if statements<if statements>` from the one for when the timer is :red:`NOT done` (lines 4-9) because they are no longer used

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

* I add :ref:`variables<what is a variable?>` for the colors to use to remove the repetition of ``'YELLOW'`` and ``'GREEN'``

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

* I use the new :ref:`variables<what is a variable?>` to remove the repetition of ``'YELLOW'`` and ``'GREEN'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 11-14, 16-17

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

The ``show`` :ref:`function<what is a function?>`

* returns the current light if the timer is :red:`NOT done`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

  - returns :red:`RED` if the current light is :yellow:`YELLOW`

* checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

  - returns :yellow:`YELLOW` if the current light is :green:`GREEN`

* returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`
* returns :green:`GREEN` if none of the other conditions are met (this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)

----

*********************************************************************************
test_red_traffic_light_w_walk_button
*********************************************************************************

----

So far, the :ref:`truth table` for the Traffic Light is

================  ===============  ================
current light     timer            show
================  ===============  ================
:red:`RED`        :green:`done`    :green:`GREEN`
:red:`RED`        :red:`NOT done`  :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`GREEN`
================  ===============  ================

I want to add a walk button for a person to push when they want to cross the street, the inputs for the traffic light will then be

* did the person push the walk button?
* what color is the light now?
* is the timer done?

and the :ref:`truth table` for if the Traffic Light is :red:`RED` is

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
================  ===============  =================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` for when the current light is :red:`RED`, the timer is :green:`done` and the walk button is :green:`pushed`, to :ref:`test_red_traffic_light` in ``test_traffic_light.py``

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
================  ===============  =================  =================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 2-8

      def test_red_traffic_light(self):
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
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'RED'
          reality = src.traffic_light.show(
              current_light='RED',
              timer_done=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_yellow_traffic_light(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: show() got an unexpected keyword argument 'walk_button'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`keyword argument<test_functions_w_keyword_arguments>` to the ``show`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def show(current_light, timer_done, walk_button):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light

        if current_light == yellow:
            return 'RED'

        if current_light == green:
            return 'YELLOW'

        return green

  the terminal_ is my friend, and shows 3 failures with :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_green_traffic_light - TypeError: show() missing 1 required positional arg...
    FAILED ...test_red_traffic_light - TypeError: show() missing 1 required positional arg...
    FAILED ...test_yellow_traffic_light - TypeError: show() missing 1 required positional arg...

  because all the other tests call the ``show`` :ref:`function<what is a function?>` with two arguments and I changed the :ref:`function signature<what is a function?>` to make it expect three. I need to make the third argument a choice.

* I could add the ``walk_button`` parameter to every call to the ``show`` :ref:`function<what is a function?>` in every test or add a :ref:`default value<test_functions_w_default_arguments>` for the new :ref:`keyword argument<test_functions_w_keyword_arguments>` to make it a choice, NOT a requirement. I make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def show(
            current_light, timer_done,
            walk_button=False,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

  yes!

* I add an :ref:`if statement<if statements>` for ``walk_button``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-17

    def show(
            current_light, timer_done,
            walk_button=False
        ):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light

        if current_light == yellow:
            return 'RED'

        if current_light == green:
            return 'YELLOW'

        if walk_button == True:
            return 'RED'

        return green

  the test passes

  .. TIP:: Because I set a :ref:`default value<test_functions_w_default_arguments>` for the new :ref:`keyword argument<test_functions_w_keyword_arguments>` to make it a choice, NOT a requirement, this call to the ``show`` :ref:`function<what is a function?>`

    .. code-block:: python

      src.traffic_light.show(
          current_light='RED',
          timer_done=True,
      )

    is now the same as

    .. code-block:: python

      src.traffic_light.show(
          current_light='RED',
          timer_done=True,
          walk_button=False,
      )

    If I call the ``show`` :ref:`function<what is a function?>` without giving a value for the ``walk_button`` parameter, it will use the :ref:`default value (False)<test_functions_w_default_arguments>` for the ``walk_button``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add bool_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1-2

        # if walk_button == True:
        if bool(walk_button) == True:
            return 'RED'

        return green

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-3

        # if walk_button == True:
        # if bool(walk_button) == True:
        if bool(walk_button):
            return 'RED'

        return green

  still green

* I remove bool_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-4

        # if walk_button == True:
        # if bool(walk_button) == True:
        # if bool(walk_button):
        if walk_button:
            return 'RED'

  green

* I add a :ref:`variable<what is a variable?>` for :red:`RED`, to use to remove repetition of ``'RED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def show(
            current_light, timer_done,
            walk_button=False
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:

* I use the :ref:`variable<what is a variable?>` to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12, 21-22

    def show(
            current_light, timer_done,
            walk_button=False
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light

        if current_light == yellow:
            # return 'RED'
            return red

        if current_light == green:
            return 'YELLOW'

        # if walk_button == True:
        # if bool(walk_button) == True:
        # if bool(walk_button):
        if walk_button:
            # return 'RED'
            return red

        return green

  still green

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def show(
            current_light, timer_done,
            walk_button=False
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

* I do not need to do anything to the :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is :green:`done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  ================  ===============  =================  =================

  because

  .. code-block:: python

    src.traffic_light.show(
        current_light='RED',
        timer_done=True,
    )

  is now the same as

  .. code-block:: python

    src.traffic_light.show(
        current_light='RED',
        timer_done=True,
        walk_button=False,
    )

  because the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  :red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 21

        def test_red_traffic_light(self):
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
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_yellow_traffic_light(self):

  green

* I change the expectation to make sure the test works

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

            my_expectation = 'BOOM'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'BOOM'

* I change the expectation back

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_yellow_traffic_light(self):

  the test is green again

* I add an :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is :red:`NOT done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  :red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
  :red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 25-29

        def test_red_traffic_light(self):
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
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='RED',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_yellow_traffic_light(self):

  green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'RED'``)
  * I do not need to provide a value for the ``walk_button`` parameter because

    .. code-block:: python

      src.traffic_light.show(
          current_light='RED',
          timer_done=False,
      )

    is the same as

    .. code-block:: python

      src.traffic_light.show(
          current_light='RED',
          timer_done=False,
          walk_button=False,
      )

    because the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'RED'`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_red_traffic_light(self):
            red = 'RED'

            my_expectation = 'RED'

* I use the ``red`` :ref:`variable<what is a variable?>` to remove the repetition of ``'RED'`` and ``my_expectation`` when its value is ``'RED'``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4, 6-7, 11-12, 16-17, 22, 24-25, 29-30, 33-34, 37-38

        def test_red_traffic_light(self):
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

            reality = src.traffic_light.show(
                # current_light='RED',
                current_light=red,
                timer_done=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

        def test_yellow_traffic_light(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_red_traffic_light(self):
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
            )
            self.assertEqual(reality, red)

        def test_yellow_traffic_light(self):

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``current_light`` :ref:`keyword argument<test_functions_w_keyword_arguments>` in ``traffic_light.py`` as a fail safe so that the light is always :red:`RED` if no value is given

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
    :lineno-start: 68
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

  because

  - the :ref:`default value<test_functions_w_default_arguments>` for ``current_light`` is :red:`'RED'`
  - the :ref:`default value<test_functions_w_default_arguments>` for ``timer_done`` is :ref:`False<test_what_is_false>`
  - the :ref:`default value<test_functions_w_default_arguments>` for ``walk_button`` is :ref:`False<test_what_is_false>`

* I change the name of :ref:`test_red_traffic_light` to :ref:`test_red_traffic_light_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_red_traffic_light_w_walk_button(self):
            red = 'RED'

* I remove the ``current_light`` parameter from the calls to ``src.traffic_light.show`` in :ref:`test_red_traffic_light_w_walk_button` in ``test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5, 13, 19, 26

        def test_red_traffic_light_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.show(
                # current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                # current_light=red,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                # current_light=red,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show(
                # current_light=red,
                timer_done=False,
            )
            self.assertEqual(reality, red)

        def test_yellow_traffic_light(self):

  the test is still green

* I remove the ``timer_done`` parameter when it is :ref:`False<test_what_is_false>` from :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 20, 27

        def test_red_traffic_light_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.show(
                # current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                # current_light=red,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                # current_light=red,
                # timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show(
                # current_light=red,
                # timer_done=False,
            )
            self.assertEqual(reality, red)

        def test_yellow_traffic_light(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_red_traffic_light_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.show()
            self.assertEqual(reality, red)

        def test_yellow_traffic_light(self):

  green

.. admonition:: REMINDER

  The ``show`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

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

  * returns the current light if the timer is :red:`NOT done`
  * checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

    - returns :red:`RED` if the current light is :yellow:`YELLOW`

  * checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

    - returns :yellow:`YELLOW` if the current light is :green:`GREEN`

  * checks if the walk button is :green:`pushed` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`, this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)

    - returns :red:`RED` if the walk button is :green:`pushed`

  * returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`
  * returns :green:`GREEN` if none of the other conditions are met (this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)

----

*********************************************************************************
test_yellow_traffic_light_w_walk_button
*********************************************************************************

The :ref:`truth table` for if the Traffic Light is :yellow:`YELLOW` with the walk button is

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  =================

* I add ``walk_button`` to the call to ``src.traffic_light.show`` for when the light is :yellow:`YELLOW`, the timer is :green:`done` and the walk button is :green:`pushed`, in the first :ref:`assertion<what is an assertion?>` of :ref:`test_yellow_traffic_light` in ``test_traffic_light.py``

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6

        def test_yellow_traffic_light(self):
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

        def test_green_traffic_light(self):

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is :green:`done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 10-14

        def test_yellow_traffic_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

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

        def test_green_traffic_light(self):

  still green

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'RED'``)
  * I do not need to give a value for the ``walk_button`` parameter because

    .. code-block:: python

      src.traffic_light.show(
          current_light='YELLOW',
          timer_done=True,
      )

    is the same as

    .. code-block:: python

      src.traffic_light.show(
          current_light='YELLOW',
          timer_done=True,
          walk_button=False,
      )

    the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>`, for when the light is :yellow:`YELLOW`, the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  :yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 20

        def test_yellow_traffic_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_green_traffic_light(self):

  green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is :red:`NOT done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  :yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
  :yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 24-27

        def test_yellow_traffic_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='YELLOW',
            )
            self.assertEqual(reality, my_expectation)

        def test_green_traffic_light(self):

  still green

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'YELLOW'``)
  * I do not need to give a value for the ``walk_button`` and ``timer_done`` parameters because

    .. code-block:: python

      src.traffic_light.show(
          current_light='YELLOW',
      )

    is the same as

    .. code-block:: python

      src.traffic_light.show(
          current_light='YELLOW',
          timer_done=False,
          walk_button=False,
      )

    - the :ref:`default value<test_functions_w_default_arguments>` for the ``timer_done`` parameter is :ref:`False<test_what_is_false>`
    - the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I change the name of the test from :ref:`test_yellow_traffic_light` to :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4

            reality = src.traffic_light.show()
            self.assertEqual(reality, red)

        def test_yellow_traffic_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.show(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'YELLOW'`` from the test

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_yellow_traffic_light_w_walk_button(self):
            yellow = 'YELLOW'

            my_expectation = 'RED'

* I use the new :ref:`variable<what is a variable?>` to remove repetition of ``'YELLOW'`` and the ``my_expectation`` :ref:`variable<what is a variable?>` when its value is ``'YELLOW'``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6-7, 14-15, 20, 22-23, 27-28, 31-32, 34-35, 39-40

        def test_yellow_traffic_light_w_walk_button(self):
            yellow = 'YELLOW'

            my_expectation = 'RED'
            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
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

            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

        def test_green_traffic_light(self):

  the test is still green

* I add a :ref:`variable<what is a variable?>` for :red:`RED` (a repetition of the :ref:`variable<what is a variable?>` in :ref:`test_red_traffic_light_w_walk_button`, oh boy)

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_yellow_traffic_light_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            my_expectation = 'RED'

* I use the new :ref:`variable<what is a variable?>` to remove repetition, such irony (I use a repetition to remove a repetition)

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4, 11-12, 19-20

        def test_yellow_traffic_light_w_walk_button(self):
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

            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

  still green

* I make a :ref:`global variable<what is a variable?>` to use to remove repetition of ``'RED'`` from :ref:`test_yellow_traffic_light_w_walk_button` and :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED = 'RED'


    class TestTrafficLight(unittest.TestCase):

* I use the ``RED`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 8-9, 20-21, 24-25

        def test_red_traffic_light_walk_button(self):
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
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show()
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

        def test_yellow_traffic_light_w_walk_button(self):

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_red_traffic_light_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show()
            self.assertEqual(reality, RED)

        def test_yellow_traffic_light_w_walk_button(self):

* I use the ``RED`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2-3, 13-14, 22-23

        def test_yellow_traffic_light_w_walk_button(self):
            # red, yellow = 'RED', 'YELLOW'
            yellow = 'YELLOW'

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

            reality = src.traffic_light.show(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 31

        def test_yellow_traffic_light_w_walk_button(self):
            yellow = 'YELLOW'

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                current_light=yellow,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, yellow)

            reality = src.traffic_light.show(
                current_light=yellow,
            )
            self.assertEqual(reality, yellow)

        def test_green_traffic_light(self):

----

*********************************************************************************
test_green_traffic_light_w_walk_button
*********************************************************************************

The :ref:`truth table` for if the Traffic Light is :green:`GREEN` with the walk button is

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  =================

* I add ``walk_button`` to the call to ``src.traffic_light.show`` for when the light is :green:`GREEN`, the timer is :green:`done` and the walk button is :green:`pushed`, in the first :ref:`assertion<what is an assertion?>` of :ref:`test_green_traffic_light` in ``test_traffic_light.py``

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 6

        def test_green_traffic_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN`, the timer is :green:`done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 10-14

        def test_green_traffic_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

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

  still green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'YELLOW'``)
  * I do not need to give a value for the ``walk_button`` parameter because

    .. code-block:: python

      src.traffic_light.show(
          current_light='GREEN',
          timer_done=True,
      )

    is the same as

    .. code-block:: python

      src.traffic_light.show(
          current_light='GREEN',
          timer_done=True,
          walk_button=False,
      )

    the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN`, the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  :green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 20

        def test_green_traffic_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green

* I add an :ref:`assertion<what is an assertion?>` for when the light is :green:`GREEN`, the timer is :red:`NOT done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        show
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  :green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
  :green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 24-27

        def test_green_traffic_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                current_light='GREEN',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'GREEN'``)
  * I do not need to give a value for the ``walk_button`` and ``timer_done`` parameters because

    .. code-block:: python

      src.traffic_light.show(
          current_light='GREEN',
      )

    is the same as

    .. code-block:: python

      src.traffic_light.show(
          current_light='GREEN',
          timer_done=False,
          walk_button=False,
      )

    - the :ref:`default value<test_functions_w_default_arguments>` for the ``timer_done`` parameter is :ref:`False<test_what_is_false>`
    - the :ref:`default value<test_functions_w_default_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I change the name of the test from :ref:`test_green_traffic_light` to :ref:`test_green_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 6

            reality = src.traffic_light.show(
                current_light=yellow,
            )
            self.assertEqual(reality, yellow)

        def test_green_traffic_light_w_walk_button(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

* I add a :ref:`global variable<what is a variable?>` to use to remove repetition of ``'YELLOW'`` from :ref:`test_green_traffic_light_w_walk_button` and :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW = 'RED', 'YELLOW'


    class TestTrafficLight(unittest.TestCase):

* I use the ``YELLOW`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2, 5-6, 13-14, 20-21, 25-26, 29-30, 32-33

        def test_yellow_traffic_light_w_walk_button(self):
            # yellow = 'YELLOW'

            reality = src.traffic_light.show(
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=True,
            )
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
            )
            # self.assertEqual(reality, yellow)
            self.assertEqual(reality, YELLOW)

        def test_green_traffic_light_w_walk_button(self):

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 31

        def test_yellow_traffic_light_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
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
            )
            self.assertEqual(reality, YELLOW)

        def test_green_traffic_light_w_walk_button(self):

* I add a :ref:`global variable<what is a variable?>` to use to remove repetition of ``'GREEN'`` from :ref:`test_green_traffic_light_w_walk_button` and :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'


    class TestTrafficLight(unittest.TestCase):

* I use the ``GREEN`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8, 12-13

        def test_red_traffic_light_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            # my_expectation = 'GREEN'
            reality = src.traffic_light.show(
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.show(
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show()
            self.assertEqual(reality, RED)

        def test_yellow_traffic_light_w_walk_button(self):

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_red_traffic_light_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show(
                timer_done=True,
            )
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.show(
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.show()
            self.assertEqual(reality, RED)

        def test_yellow_traffic_light_w_walk_button(self):

* I use the :green:`GREEN` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_green_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4-5, 12-13, 18, 20-21, 25-26, 29-30, 32-33

        def test_green_traffic_light_w_walk_button(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
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

            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

  still green

* I use the :yellow:`YELLOW` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_green_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2, 9-10, 17-18

        def test_green_traffic_light_w_walk_button(self):
            # my_expectation = 'YELLOW'
            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.show(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, YELLOW)

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 56

        def test_green_traffic_light_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
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
            )
            self.assertEqual(reality, GREEN)


    # Exceptions seen

* I want to remove the ``reality`` :ref:`variable<what is a variable?>`, because it is only used once for each :ref:`assertion<what is an assertion?>`, I can make the call to ``src.traffic_light.show`` directly, in :ref:`test_green_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7-11, 18-22, 29-33, 38-42

        def test_green_traffic_light_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                reality,
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                reality,
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                reality,
                GREEN
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                reality,
                GREEN
            )

* I remove the ``reality`` :ref:`variable<what is a variable?>` from the :ref:`assertions<what is an assertion?>` :ref:`test_green_traffic_light_w_walk_button`, I no longer need it to be a middle man

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 9-14, 24-28, 39-44, 53-56

        def test_green_traffic_light_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                # reality,
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
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
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
                # reality,
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN
            )

            reality = src.traffic_light.show(
                current_light=GREEN,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    current_light=GREEN,
                ),
                GREEN
            )


    # Exceptions seen

  green

* I remove the commented lines and ``reality`` :ref:`variable<what is a variable?>` from :ref:`test_green_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56

        def test_green_traffic_light_w_walk_button(self):
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
                ),
                GREEN
            )


    # Exceptions seen

  still green

* I do the same thing with :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-10, 16-19, 26-29, 34-37

        def test_yellow_traffic_light_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(
                reality,
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
            )
            self.assertEqual(
                reality,
                YELLOW
            )

        def test_green_traffic_light_w_walk_button(self):

* I call the ``show`` :ref:`function<what is a function?>` directly in the :ref:`assertions<what is an assertion?>` in :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8-13, 22-26, 36-41, 49-52

        def test_yellow_traffic_light_w_walk_button(self):
            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                # reality,
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
            )
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                ),
                RED
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )

            reality = src.traffic_light.show(
                current_light=YELLOW,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    current_light=YELLOW,
                ),
                YELLOW
            )

        def test_green_traffic_light_w_walk_button(self):

  the test is still green

* I remove the ``reality`` :ref:`variable<what is a variable?>` and comments from :ref:`test_yellow_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 30

        def test_yellow_traffic_light_w_walk_button(self):
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
                ),
                YELLOW
            )

        def test_green_traffic_light_w_walk_button(self):

* I also do it in :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-9, 14-17, 22-25, 28-31

        def test_red_traffic_light_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.show(
                timer_done=True,
            )
            self.assertEqual(
                reality,
                GREEN
            )

            reality = src.traffic_light.show(
                walk_button=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.show()
            self.assertEqual(
                reality,
                RED
            )

        def test_yellow_traffic_light_w_walk_button(self):

* I call the ``show`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7-11, 19-22, 30-33, 39-40

        def test_red_traffic_light_walk_button(self):
            reality = src.traffic_light.show(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.show(
                timer_done=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    timer_done=True,
                ),
                GREEN
            )

            reality = src.traffic_light.show(
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.show(
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.show()
            self.assertEqual(
                # reality,
                src.traffic_light.show(),
                RED
            )

        def test_yellow_traffic_light_w_walk_button(self):

  still green

* I remove the ``reality`` :ref:`variable<what is a variable?>` and the comments from :ref:`test_red_traffic_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10

        def test_red_traffic_light_walk_button(self):
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
                ),
                GREEN
            )

            self.assertEqual(
                src.traffic_light.show(
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.show(),
                RED
            )

        def test_yellow_traffic_light_w_walk_button(self):

.. admonition:: REMINDER

  .. code-block:: python
    :linenos:

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

  the ``show`` :ref:`function<what is a function?>`

  * returns the current light if the timer is :red:`NOT done`
  * checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

    - returns :red:`RED` if the current light is :yellow:`YELLOW`

  * checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

    - returns :yellow:`YELLOW` if the current light is :green:`GREEN`

  * checks if the walk button is :green:`pushed` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`, this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)

    - returns :red:`RED` if the walk button is :green:`pushed`

  * returns :green:`GREEN` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`
  * returns :green:`GREEN` if none of the other conditions are met (this includes the case where the timer is :green:`done` AND the current light is :red:`RED`)

----

*************************************************************************************
test_red_traffic_light_w_walk
*************************************************************************************

The inputs for the traffic light up till now are

* did the person push the walk button?
* what color is the light now?
* is the timer done?

which gives this :ref:`truth table`

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
================  ===============  =================  =================

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  =================

================  ===============  =================  =================
current light     timer            walk button        show
================  ===============  =================  =================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  =================

I want the traffic light to show ``WALK`` or ``NO WALK`` when a person can walk. This means the :ref:`truth table` for if the Traffic Light is :red:`RED` with the walk sign is

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`RED` + :green:`WALK`
================  =============== ================= =================================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add the value for the ``current_light`` parameter in the call to the ``show`` :ref:`function<what is a function?>` for when the light is :red:`RED`, the timer is :green:`done` and the walk button is :green:`pushed`, to be clearer, then I change the expectation of the first :ref:`assertion<what is an assertion?>` in :ref:`test_red_traffic_light_w_walk_button`

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
================  =============== ================= =================================

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 7

      def test_red_traffic_light_w_walk_button(self):
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

I change the `return statement`_ for this case ``show`` :ref:`function<what is a function?>` in ``traffic_light.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 17

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
          return 'YELLOW'

      if walk_button:
          return red, 'WALK'

      return green

the test passes. The ``show`` :ref:`function<what is a function?>`

* returns the current light if the timer is :red:`NOT done`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

    - returns :red:`RED` if the current light is :yellow:`YELLOW`
* checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

    - returns :yellow:`YELLOW` if the current light is :green:`GREEN`
* checks if the walk button is :green:`pushed` (this only happens if the timer is :green:`done` AND the current light is :red:`RED`)
    - returns``'RED', 'WALK'`` if the walk button is :green:`pushed`
* returns :green:`GREEN` if the timer is :green:`done` AND the current light is :red:`RED` (this only happens if the walk button is :red:`NOT pushed`)

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add values for the other parameters, to be clearer for when the light is :red:`RED`, the timer is :green:`done`, and the walk button is :green:`pushed`, then I change the expectation of the second :ref:`assertion<what is an assertion?>` in :ref:`test_red_traffic_light_w_walk_button` in ``test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 13, 15, 17

        def test_red_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I add ``'NO WALK'`` to the `return statement`_ for this case in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19

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
            return red, 'WALK'

        return green, 'NO WALK'

  the test passes

* I change the third :ref:`assertion<what is an assertion?>` for when the light is :red:`RED`, the timer is :red:`NOT done`, and the walk button is :green:`pushed`, in :ref:`test_red_traffic_light_w_walk_button` in ``test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  :red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 22-23, 26

        def test_red_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I add an :ref:`if statement<if statements>` for this case to the one for when the timer is :red:`NOT done`, in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            return current_light

        if current_light == yellow:
            return red

        if current_light == green:
            return yellow

        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('RED', 'WALK') != 'RED'

  this time for the next :ref:`assertion<what is an assertion?>`

* I add values for the other parameters in the next :ref:`assertion<what is an assertion?>`, to be clearer for the case where the light is :red:`RED`, the timer is :red:`NOT done`, and the walk button is :red:`NOT pushed`,  in :ref:`test_red_traffic_light_w_walk_button` in ``test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  :red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 30-35

        def test_red_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_yellow_traffic_light_w_walk_button(self):

  the test passes

* I change the name of :ref:`test_red_traffic_light_w_walk_button` to :ref:`test_red_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_red_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

The ``show`` :ref:`function<what is a function?>`

* returns ``'RED', 'WALK'`` if the timer is :red:`NOT done` AND the current light is :red:`RED`
* returns the current light if the timer is :red:`NOT done` AND the current light is NOT :red:`RED`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)

    - returns :red:`RED` if the current light is :yellow:`YELLOW`
* checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

    - returns :yellow:`YELLOW` if the current light is :green:`GREEN`
* checks if the walk button is :green:`pushed` (this only happens if the timer is :green:`done` AND the current light is :red:`RED`)
    - returns``'RED', 'WALK'`` if the walk button is :green:`pushed`
* returns ``'GREEN', 'NO WALK'`` if the timer is :green:`done` AND the current light is :red:`RED` (this only happens if the walk button is :red:`NOT pushed`)

----

*************************************************************************************
test_yellow_traffic_light_w_walk
*************************************************************************************

The :ref:`truth table` for if the Traffic Light is :yellow:`YELLOW` with the walk sign is

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= =================================

* I change the expectation of the first :ref:`assertion<what is an assertion?>` for when the light is :yellow:`YELLOW`, the timer is :green:`done` and the walk button is :green:`pushed`, in :ref:`test_yellow_traffic_light_w_walk_button`

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 8

        def test_yellow_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I add ``'WALK'`` to the :ref:`if statement<if statements>` for this case, in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 22

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            return current_light

        if current_light == yellow:
            return red, 'WALK'

        if current_light == green:
            return yellow

        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('RED', 'WALK') != 'RED'

  I have to make the same change to the expectation of the next :ref:`assertion<what is an assertion?>`

* I change the second :ref:`assertion<what is an assertion?>` which is for when the light is :yellow:`YELLOW`, the timer is :green:`done` and the walk button is :red:`NOT pushed`, in :ref:`test_yellow_traffic_light_w_walk_button` in ``test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 15, 17

        def test_yellow_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

  the test passes

* I change the third :ref:`assertion<what is an assertion?>`, which is for when the light is :yellow:`YELLOW`, the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 23-24, 29

        def test_yellow_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != ('YELLOW', 'NO WALK')

* I add an :ref:`if statement<if statements>` to the one for when the timer is :red:`NOT done` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light

        if current_light == yellow:
            return red, 'WALK'

        if current_light == green:
            return yellow

        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('YELLOW', 'NO WALK') != 'YELLOW'

  I have to make the same change to the next :ref:`assertion<what is an assertion?>` in the test

* I change the last :ref:`assertion<what is an assertion?>`, which is for when the light is :yellow:`YELLOW`, the timer is :red:`NOT done`, and the walk button is :red:`NOT pushed`, in :ref:`test_yellow_traffic_light_w_walk_button` in ``test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 32-33, 35

        def test_yellow_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

        def test_green_traffic_light_w_walk_button(self):

  the test passes

* I change the name of the test from :ref:`test_green_traffic_light_w_walk_button` to :ref:`test_green_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_green_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

The ``show`` :ref:`function<what is a function?>`

* returns ``'RED', 'WALK'`` if the timer is :red:`NOT done` AND the current light is :red:`RED`
* returns ``'YELLOW', 'WALK'`` if the timer is :red:`NOT done` AND the current light is :red:`YELLOW`
* returns the current light if the timer is :red:`NOT done` AND the current light is NOT :red:`RED` AND the current light is NOT :yellow:`YELLOW`
* checks if the current light is :yellow:`YELLOW` (this only happens if the timer is :green:`done`)
    - returns``'RED', 'WALK'`` if the current light is :yellow:`YELLOW`
* checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW`)

    - returns :yellow:`YELLOW` if the current light is :green:`GREEN`
* checks if the walk button is :green:`pushed` (this only happens if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is NOT :red:`GREEN`)
    - returns``'RED', 'WALK'`` if the walk button is :green:`pushed`
* returns ``'GREEN', 'NO WALK'`` if the timer is :green:`done` AND the current light is NOT :yellow:`YELLOW` AND the current light is not :green:`GREEN` (this only happens if the walk button is :red:`NOT pushed`)

----

*************************************************************************************
test_green_traffic_light_w_walk
*************************************************************************************

The :ref:`truth table` for if the Traffic Light is :green:`GREEN` with the walk sign is

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
================  =============== ================= =================================

* I change the expectation of the first :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN`, the timer is :green:`done`, and the walk button is :green:`pushed`, in :ref:`test_green_traffic_light_w_walk_button`

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 8

        def test_green_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
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
    :emphasize-lines: 18

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light

        if current_light == yellow:
            return red, 'WALK'

        if current_light == green:
            return yellow, 'NO WALK'

        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('YELLOW', 'NO WALK') != 'YELLOW'

  I have to make the same change to the next :ref:`assertion<what is an assertion?>`

* I change the second :ref:`assertion<what is an assertion?>`, which is for when the light is :green:`GREEN`, the time is :green:`done`, and the walk button is :red:`NOT pushed` in :ref:`test_green_traffic_light_w_walk_button` in ``test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 17

        def test_green_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

  the test passes

* I change the third :ref:`assertion<what is an assertion?>`, which is for when the light is :green:`GREEN`, the timer is :red:`NOT done`, and the walk button is :green:`pushed`

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 26

        def test_green_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I add an :ref:`if statement<if statements>` to the one for when the timer is NOT done in the ``show`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 12

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            if current_light == yellow:
                return current_light, 'NO WALK'
            return current_light, 'NO WALK'

        if current_light == yellow:
            return red, 'WALK'

        if current_light == green:
            return yellow, 'NO WALK'

        if walk_button:
            return red, 'WALK'

        return green, 'NO WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('GREEN', 'NO WALK') != 'GREEN'

  I have to make the same change in the next :ref:`assertion<what is an assertion?>`

* I change the last :ref:`assertion<what is an assertion?>`, which is for when the light is :green:`GREEN`, the timer is :red:`NOT done`, and the walk button is :red:`NOT pushed`

  ================  =============== ================= =================================
  current light     timer           walk button       show
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
  :green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 35

        def test_green_traffic_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )


    # Exceptions seen

  the test passes

* I change the name of the test from :ref:`test_green_traffic_light_w_walk_button` to :ref:`test_green_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

        def test_green_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

----

* I add more :ref:`global variables<what is a variable?>` to ``test_traffic_light.py`` to use to remove repetition from the tests

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

* I use the ``GREEN_NO_WALK`` :ref:`variable<what is a variable?>` for ``(GREEN, 'NO WALK')`` in the second :ref:`assertion<what is an assertion?>` of :ref:`test_red_traffic_light_w_walk`


  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 17-18

        def test_red_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

  the test is still green

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` in :ref:`test_red_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-9, 28-29, 38-39

        def test_red_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

        def test_green_traffic_light_w_walk(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

        def test_red_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                WALK
            )

        def test_green_traffic_light_w_walk(self):

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` in :ref:`test_yellow_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8-9, 18-19

        def test_green_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

  green

* I use the ``YELLOW_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(YELLOW, 'NO WALK')`` in :ref:`test_yellow_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 28-29, 38-39

        def test_green_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

  still green

* I remove the commented lines from :ref:`test_yellow_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 51

        def test_green_traffic_light_w_walk(self):
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

        def test_green_traffic_light_w_walk(self):

* I use the ``YELLOW_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(YELLOW, 'NO WALK')`` in :ref:`test_green_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 8-9, 18-19

        def test_green_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

  green

* I use the ``GREEN_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(GREEN, 'NO WALK')`` in :ref:`test_green_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 28-29, 38-39

        def test_green_traffic_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.show(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

  still green

* I remove the commented lines from :ref:`test_green_traffic_light_w_walk`

  .. code-block:: python
    :lineno-start: 88

        def test_green_traffic_light_w_walk(self):
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
                    walk_button=True,
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

----

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I add :ref:`variables<what is a variable?>` for ``'WALK'`` and ``'NO WALK'`` to the ``show`` :ref:`function<what is a function?>` in ``traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

* I use the new :ref:`variables<what is a variable?>` to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11, 13-14, 15-16, 18-19, 21-22, 24-25, 27-28

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

        if not timer_done:
            if current_light == red:
                # return current_light, 'WALK'
                return walk
            if current_light == yellow:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            # return current_light, 'NO WALK'
            return current_light, no_walk

        if current_light == yellow:
            # return red, 'WALK'
            return walk

        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk

        if walk_button:
            # return red, 'WALK'
            return walk

        # return green, 'NO WALK'
        return green, no_walk

  the tests are still green

* I write a new :ref:`if statement with an else clause<if statements>`, that covers the 3 cases when the timer is :red:`NOT done`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-5

        if not timer_done:
            if current_light != red:
                return current_light, no_walk
            else:
                return walk
            if current_light == red:
                # return current_light, 'WALK'
                return walk
            if current_light == yellow:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            # return current_light, 'NO WALK'
            return current_light, no_walk

  still green

* I write out the :ref:`if statements<if statements>` for when the light is :red:`RED` and the timer is :green:`done`, to be clearer

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1, 3, 5-9, 12

        # if walk_button:
            # return red, 'WALK'
            # return walk

        if current_light == red:
            if not walk_button:
                return green, no_walk
            else:
                return walk

        # return green, 'NO WALK'
        # return green, no_walk

  green

* the ``walk`` :ref:`variable<what is a variable?>` which is ``'RED', 'WALK'``, happens 3 times in the :ref:`function<what is a function?>`, I add a `return statement`_ to make it the default state of the light

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3

        # return green, 'NO WALK'
        # return green, no_walk
        return walk

  still green. This means if no :ref:`conditions<if statements>` are met, the light stays :red:`RED` and shows ``'WALK'``

* I no longer need the :ref:`if statement<if statements>` for :yellow:`YELLOW` because it returns the default state (``'RED', 'WALK'``) when the timer is :green:`done`. I comment it out

  .. code-block:: python
    :linenos:
    :emphasize-lines: 23, 25

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

        if not timer_done:
            if current_light != red:
                return current_light, no_walk
            else:
                return walk
            if current_light == red:
                # return current_light, 'WALK'
                return walk
            if current_light == yellow:
                # return current_light, 'NO WALK'
                return current_light, no_walk
            # return current_light, 'NO WALK'
            return current_light, no_walk

        # if current_light == yellow:
            # return red, 'WALK'
            # return walk

        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk

  green. Why does this work?

* I remove the commented lines and the other :ref:`if statements<if statements>` from the one for when the timer is :red:`NOT done`

  .. code-block:: python
    :linenos:

    def show(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

        if not timer_done:
            if current_light != red:
                return current_light, no_walk
            else:
                return walk

        if current_light == green:
            return yellow, no_walk

        if current_light == red:
            if not walk_button:
                return green, no_walk
            else:
                return walk

        return walk

  The ``show`` :ref:`function<what is a function?>`

  - checks if the timer is :red:`NOT done`

    * returns the current light and ``'NO WALK'`` if the timer is :red:`NOT done` AND the current light is NOT :red:`RED`
    * returns ``'RED', 'WALK'`` if the timer is :red:`NOT done` AND the current light is :red:`RED`

  - checks if the current light is :green:`GREEN` (this only happens if the timer is :green:`done`)
    - returns``'YELLOW', 'NO WALK'`` if the current light is :green:`GREEN`
  - checks if the current light is :red:`RED` (this only happens if the timer is :green:`done`)

    * returns ``'GREEN', 'NO WALK'`` if the timer is :green:`done` AND the walk button is :red:`NOT pushed`
    * returns ``'RED', 'WALK'`` if the timer is :green:`done` AND the walk button is :green:`pushed`

  - returns ``'RED', 'WALK'`` if none of the conditions in the :ref:`function<what is a function?>` are met

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

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`RED` + :green:`WALK`
================  =============== ================= =================================

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= =================================

================  =============== ================= =================================
current light     timer           walk button       show
================  =============== ================= =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
================  =============== ================= =================================

The Traffic Light only shows ``'WALK'`` when the light is :red:`RED`.

What if there is an emergency vehicle? If the Traffic Light changes based on the emergency vehicle, its inputs would be

* what color is the light now?
* is the timer done?
* did the person push the walk button?
* is there an emergency vehicle?

and the :ref:`truth table` would be

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             show
================  =============== ================= ====================  =================================
:red:`RED`        :green:`done`   :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :green:`done`   :green:`pushed`   :red:`NOT emergency`  :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :green:`GREEN` + :red:`NO WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             show
================  =============== ================= ====================  =================================
:red:`RED`        :red:`NOT done` :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :red:`RED` + :green:`WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             show
================  =============== ================= ====================  =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`NOT emergency`  :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :red:`RED` + :green:`WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             show
================  =============== ================= ====================  =================================
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             show
================  =============== ================= ====================  =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :green:`emergency`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :green:`pushed`   :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :green:`emergency`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             show
================  =============== ================= ====================  =================================
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`emergency`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :green:`GREEN` + :red:`NO WALK`
================  =============== ================= ====================  =================================

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Traffic Light: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`

:ref:`Would you like to test making an Automatic Teller Machine?<Automatic Teller Machine>`

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