.. meta::
  :description: Build a state-controlled **Traffic Light** system using Python and Test Driven Development (TDD). This hands-on project tutorial teaches beginners how to manage transitions between RED, YELLOW, and GREEN states based on timers and walk-button inputs. Master the Red-Green-Refactor cycle, learn to implement robust failsafes with function default arguments, and debug complex Python SyntaxErrors in a professional development environment.
  :keywords: Jacob Itegboje, Python **Traffic Light** project, state machine logic tutorial, TDD for beginners Python, building a traffic signal in code, Python truth table to code translation, Python function default arguments examples, Red Green Refactor tutorial, uv project management Python, pytest-watcher automated testing, debugging SyntaxError parameter order, TypeError unexpected keyword argument, sequential logic in programming, Python conditional statements project, building a controller in Python, software engineering logic gates, logic-based state transitions, programming automation for beginners, unittest **Traffic Light** example, Python boolean logic practice

.. include:: ../../links.rst

.. _traffic_light:

#################################################################################
Traffic Light
#################################################################################

----

I want to make a **Traffic Light** that changes color.

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :linenos:
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 1-23

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 25
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 25-41

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 43
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 43-59

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 61
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 61-77

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 79
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 79-95

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 97
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 97-113

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 115
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 115-131

.. literalinclude:: ../../code/traffic_light/tests/test_traffic_light.py
  :language: python
  :lineno-start: 133
  :caption: traffic_light/tests/tests/test_traffic_light.py
  :lines: 133-

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I open ``makePythonTdd.sh``

      * I change the name of the project to ``traffic_light`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/traffic_light/make_tdd/makePythonTddTrafficLight.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 10, 18

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``traffic_light`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``

      * I change the name of the project to ``traffic_light`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/traffic_light/make_tdd/makePythonTddTrafficLight.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 9, 17

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``traffic_light`` project

        .. code-block:: python
          :emphasize-lines: 1

          .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES =========================
    ___________ TestTrafficLight.test_failure _________________

    self = <tests.test_traffic_light.TestTrafficLight testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/tests/test_traffic_light.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/tests/test_traffic_light.py::TestTrafficLight::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/tests/test_traffic_light.py:7`` to open it
* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>` in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestTrafficLight(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertTrue(True)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then `change directory`_ to ``traffic_light``

  .. code-block:: python
    :emphasize-lines: 1

    cd traffic_light

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

----

I want the **Traffic Light** to change color based on a timer. If the inputs are

* what color is the light now?
* is the timer done?

then I get this :ref:`truth table`

================  ===============  ================
current light     timer            output
================  ===============  ================
:red:`RED`        :green:`done`    :green:`GREEN`
:red:`RED`        :red:`NOT done`  :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`GREEN`
================  ===============  ================

----

*********************************************************************************
test_red_light_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change :ref:`test_failure` to :ref:`test_red_light_timer_done`, then add an :ref:`assertion<what is an assertion?>` for if the light is :red:`RED` AND the timer is :green:`done`

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :red:`RED`        :green:`done`    :green:`GREEN`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-10

    class TestTrafficLight(unittest.TestCase):

        def test_red_light(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='RED',
                    timer_done=True,
                ),
                'GREEN'
            )


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

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.traffic_light
    import unittest


    class TestTrafficLight(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.traffic_light'
                    has no attribute 'show'

  because ``traffic_light/__init__.py`` in the ``src`` folder_ does not have anything named ``control`` in it

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``traffic_light/__init__.py`` from the ``src`` folder_

* I add a :ref:`function<what is a function?>` to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def control():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got
               an unexpected keyword argument 'current_light'

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add ``current_light`` to the :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(current_light):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got an
               unexpected keyword argument 'timer_done'

* I add ``timer_done`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(current_light, timer_done):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'GREEN'

* I change the :ref:`return statement<the return statement>` to give the test what it expects

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(current_light, timer_done):
        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='RED'   , timer_done=True ) -> 'GREEN'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_red_light_timer_done'

----

*********************************************************************************
test_red_light_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the light is :red:`RED` AND the timer is :red:`NOT done`, in ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :red:`RED`        :red:`NOT done`  :red:`RED`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-17

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='RED',
                    timer_done=True,
                ),
                'GREEN'
            )

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='RED',
                    timer_done=False,
                ),
                'RED'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for this case, to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def control(current_light, timer_done):
        if not timer_done:
            return 'RED'

        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='RED'   , timer_done=True ) -> 'GREEN'
    control(current_light='RED'   , timer_done=False) -> 'RED'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_red_light_timer_not_done'

----

*********************************************************************************
test_yellow_light_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Traffic Light** is :yellow:`YELLOW` AND the timer is :green:`done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :yellow:`YELLOW`  :green:`done`    :red:`RED`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10-17

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='RED',
                    timer_done=False,
                ),
                'RED'
            )

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='YELLOW',
                    timer_done=True,
                ),
                'RED'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

      def control(current_light, timer_done):
          if not timer_done:
              return 'RED'

          if current_light == 'YELLOW':
              return 'RED'

          return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='RED'   , timer_done=True ) -> 'GREEN'
    control(current_light='RED'   , timer_done=False) -> 'RED'
    control(current_light='YELLOW', timer_done=True ) -> 'RED'

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'add test_yellow_light_timer_done'

----

*********************************************************************************
test_yellow_light_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done`, in ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-17

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='YELLOW',
                    timer_done=True,
                ),
                'RED'
            )

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='YELLOW',
                    timer_done=False,
                ),
                'YELLOW'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'YELLOW'

* I add an :ref:`if statement<if statements>` to the one for if the timer is :red:`NOT done`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def control(current_light, timer_done):
        if not timer_done:
            if current_light == 'YELLOW':
                return 'YELLOW'
            return 'RED'

        if current_light == 'YELLOW':
            return 'RED'

        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='RED'   , timer_done=True ) -> 'GREEN'
    control(current_light='RED'   , timer_done=False) -> 'RED'
    control(current_light='YELLOW', timer_done=True ) -> 'RED'
    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_yellow_light_timer_not_done'

----

*********************************************************************************
test_green_light_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Traffic Light** is :green:`GREEN` AND the timer is :green:`done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :green:`GREEN`    :green:`done`    :yellow:`YELLOW`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10-17

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='YELLOW',
                    timer_done=False,
                ),
                'YELLOW'
            )

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='GREEN',
                    timer_done=True,
                ),
                'YELLOW'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'YELLOW'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    def control(current_light, timer_done):
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

  .. code-block:: python

    control(current_light='RED'   , timer_done=True ) -> 'GREEN'
    control(current_light='RED'   , timer_done=False) -> 'RED'
    control(current_light='YELLOW', timer_done=True ) -> 'RED'
    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
    control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_green_light_timer_done'

----

*********************************************************************************
test_green_light_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :red:`NOT done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :green:`GREEN`    :red:`NOT done`  :green:`GREEN`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10-17

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='GREEN',
                    timer_done=True,
                ),
                'YELLOW'
            )

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light='GREEN',
                    timer_done=False,
                ),
                'GREEN'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'GREEN'

* I add an :ref:`if statement<if statements>` to the one for if the timer is :red:`NOT done` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def control(current_light, timer_done):
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

  the test passes.

  .. code-block:: python

    control(current_light='RED'   , timer_done=True ) -> 'GREEN'
    control(current_light='RED'   , timer_done=False) -> 'RED'
    control(current_light='YELLOW', timer_done=True ) -> 'RED'
    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
    control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'
    control(current_light='GREEN' , timer_done=False) -> 'GREEN'

* I add a git_ commit message in the other terminal_

  .. code-block::
    :emphasize-lines: 1

    git commit -am 'add test_green_light_timer_not_done'

----

*********************************************************************************
refactor control if statements
*********************************************************************************

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :green:`done`

* If the timer is :red:`NOT done`

  - it returns :yellow:`YELLOW` if the current light is :yellow:`YELLOW`
  - it returns :green:`GREEN` if the current light is :green:`GREEN`
  - it returns :red:`RED` if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

* If the timer is :green:`done`

  - it returns :red:`RED` if the current light is :yellow:`YELLOW`
  - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
  - it returns :green:`GREEN` if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

----

* I go back to the terminal_ where the tests are running
* I add an :ref:`if statement<if statements>` for if the timer is :red:`NOT done` AND the light is :red:`RED`, to make it clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def control(current_light, timer_done):
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

  the test is still green. The ``control`` :ref:`function<what is a function?>` returns the current light when the timer is :red:`NOT done`

* I add a :ref:`return statement<the return statement>` to return the current light when the timer is :red:`NOT done`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def control(current_light, timer_done):
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

  still green.

* I remove the other :ref:`if statements<if statements>` from the one for if the timer is :red:`NOT done` (lines 4-9) because they are no longer used

  .. code-block:: python
    :linenos:

    def control(current_light, timer_done):
        if not timer_done:
            return current_light

        if current_light == 'YELLOW':
            return 'RED'

        if current_light == 'GREEN':
            return 'YELLOW'

        return 'GREEN'

* I add :ref:`variables<what is a variable?>` for the colors to use them to remove the repetition of ``'YELLOW'`` and ``'GREEN'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(current_light, timer_done):
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

    def control(current_light, timer_done):
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

  the test is still green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def control(current_light, timer_done):
        yellow, green = 'YELLOW', 'GREEN'

        if not timer_done:
            return current_light

        if current_light == yellow:
            return 'RED'

        if current_light == green:
            return yellow

        return green

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit 'refactor control if statements'

----

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :green:`done`

* if the timer is :red:`NOT done` it returns the value of ``current_light``

  .. code-block:: shell

    control(current_light='RED'   , timer_done=False) -> 'RED'
    └── def control(current_light, timer_done):
        ├── yellow, green = 'YELLOW', 'GREEN'
        └── if not timer_done:
            └── return current_light
                return 'RED'
            if current_light == yellow:
                return 'RED'
            if current_light == green:
                return yellow
            return green

  .. code-block:: shell

    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
    └── def control(current_light, timer_done):
        ├── yellow, green = 'YELLOW', 'GREEN'
        └── if not timer_done:
            └── return current_light
                return 'YELLOW'
            if current_light == yellow:
                return 'RED'
            if current_light == green:
                return yellow
            return green

  .. code-block:: shell

    control(current_light='GREEN' , timer_done=False) -> 'YELLOW'
    └── def control(current_light, timer_done):
        ├── yellow, green = 'YELLOW', 'GREEN'
        └── if not timer_done:
            └── return current_light
                return 'GREEN'
            if current_light == yellow:
                return 'RED'
            if current_light == green:
                return yellow
            return green

* If the timer is :green:`done` it checks the value of ``current_light``

  - If the current light is :yellow:`YELLOW` it returns :red:`RED`

    .. code-block:: shell

      control(current_light='YELLOW', timer_done=True ) -> 'RED'
      └── def control(current_light, timer_done):
          ├── yellow, green = 'YELLOW', 'GREEN'
          ├── if not timer_done:
          │       return current_light
          └── if current_light == yellow:
              └── return 'RED'
              if current_light == green:
                  return yellow
              return green

  - If the current light is :green:`GREEN` it returns :yellow:`YELLOW`

    .. code-block:: shell

      control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'
      └── def control(current_light, timer_done):
          ├── yellow, green = 'YELLOW', 'GREEN'
          ├── if not timer_done:
          │       return current_light
          ├── if current_light == yellow:
          │       return 'RED'
          └── if current_light == green:
              └── return yellow
              return green

  - If the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN` it returns :green:`GREEN`

    .. code-block:: shell

      control(current_light='RED'   , timer_done=True ) -> 'GREEN'
      └── def control(current_light, timer_done):
          ├── yellow, green = 'YELLOW', 'GREEN'
          ├── if not timer_done:
          │       return current_light
          ├── if current_light == yellow:
          │       return 'RED'
          ├── if current_light == green:
          │       return yellow
          └── return green

----

*********************************************************************************
extract global variables
*********************************************************************************

* I add :ref:`global variables<what is a variable?>` for :red:`'RED'`, :yellow:`'YELLOW'` and :green:`'GREEN'` ``tests/test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'


    class TestTrafficLight(unittest.TestCase):

* I use the :ref:`variables<what is a variable?>` for :red:`'RED'` and :green:`'GREEN'` in :ref:`test_red_light_timer_done`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4-5, 8-9

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    # current_light='RED',
                    current_light=RED,
                    timer_done=True,
                ),
                # 'GREEN'
                GREEN
            )

        def test_red_light_timer_not_done(self):

  the test is still green.

* I remove the commented lines from :ref:`test_red_light_timer_done`

  .. code-block:: python
    :lineno-start: 10

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                ),
                GREEN
            )

        def test_red_light_timer_not_done(self):

* I use the :ref:`variable<what is a variable?>` for :red:`'RED'` in :ref:`test_red_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-5, 8-9

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    # current_light='RED',
                    current_light=RED,
                    timer_done=False,
                ),
                # 'RED'
                RED
            )

        def test_yellow_light_timer_done(self):

  still green.

* I remove the commented lines from :ref:`test_red_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 19

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                ),
                RED
            )

        def test_yellow_light_timer_done(self):

* I use the :ref:`variables<what is a variable?>` for :yellow:`'YELLOW'` and :red:`'RED'` in :ref:`test_yellow_light_timer_done`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4-5, 8-9

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    # current_light='YELLOW',
                    current_light=YELLOW,
                    timer_done=True,
                ),
                # 'RED'
                RED
            )

        def test_yellow_light_timer_not_done(self):

  green.

* I remove the commented lines from :ref:`test_yellow_light_timer_done`

  .. code-block:: python
    :lineno-start: 28

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                ),
                RED
            )

        def test_yellow_light_timer_not_done(self):

* I use the :ref:`variable<what is a variable?>` for :yellow:`'YELLOW'` in :ref:`test_yellow_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-5, 8-9

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    # current_light='YELLOW',
                    current_light=YELLOW,
                    timer_done=False,
                ),
                # 'YELLOW'
                YELLOW
            )

        def test_green_light_timer_done(self):

  still green.

* I remove the commented lines from :ref:`test_yellow_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 37

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                ),
                YELLOW
            )

        def test_green_light_timer_done(self):

* I use the :ref:`variables<what is a variable?>` for :green:`'GREEN'` and :yellow:`'YELLOW'` in :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-5, 8-9

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    # current_light='GREEN',
                    current_light=GREEN,
                    timer_done=True,
                ),
                # 'YELLOW'
                YELLOW
            )

        def test_green_light_timer_not_done(self):

  the test is still green.

* I remove the commented lines from :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 46

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                ),
                YELLOW
            )

        def test_green_light_timer_not_done(self):

* I use the :ref:`variable<what is a variable?>` for :green:`'GREEN'` in :ref:`test_green_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 4-5, 8-9

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    # current_light='GREEN',
                    current_light=GREEN,
                    timer_done=False,
                ),
                # 'GREEN'
                GREEN
            )


    # Exceptions seen

  still green.

* I remove the commented lines from :ref:`test_green_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 55

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                ),
                GREEN
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract global variables'

----

The :ref:`truth table` for the **Traffic Light** is

================  ===============  ================
current light     timer            output
================  ===============  ================
:red:`RED`        :green:`done`    :green:`GREEN`
:red:`RED`        :red:`NOT done`  :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`GREEN`
================  ===============  ================

I want to add a walk button for a person to push when they want to cross the street. The inputs for the **Traffic Light** will then be

* what color is the light now?
* is the timer done?
* was the walk button pushed?

----

*********************************************************************************
test_green_light_timer_not_done_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :green:`GREEN` AND the timer is :red:`NOT done` is

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_green_light_timer_not_done` for if the current light is :green:`GREEN` AND the timer is :red:`NOT done` AND the walk button is :red:`NOT pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 9-16

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                ),
                GREEN
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                GREEN
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got
               an unexpected keyword argument 'walk_button'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``walk_button`` to the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(current_light, timer_done, walk_button):

  the terminal_ is my friend, and shows 3 failures with :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_green_light - TypeError:
        control() missing 1 required positional argument: 'walk_button'
    FAILED ...test_red_light - TypeError:
        control() missing 1 required positional argument: 'walk_button'
    FAILED ...test_yellow_light - TypeError:
        control() missing 1 required positional argument: 'walk_button'

  because all the other :ref:`assertions<what is an assertion?>` :ref:`call<how to call a function with input>` the ``control`` :ref:`function<what is a function?>` with two arguments and I changed the :ref:`function signature<how to make a function that takes input>` to make it expect three.

* I add a :ref:`default value<test_optional_arguments>` for the new :ref:`keyword argument<test_keyword_arguments>` to make it a choice not a requirement

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def control(
            current_light, timer_done,
            walk_button=False,
        ):

  the test passes.

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=False,
        walk_button=False
    ) -> 'GREEN'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``walk_button`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_green_light_timer_not_done` for if the current light is :green:`GREEN` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 6

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                GREEN
            )


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=False,
        walk_button=True
    ) -> 'GREEN'
    control(
        current_light='GREEN', timer_done=False,
        walk_button=False
    ) -> 'GREEN'

* I change the name of the test from :ref:`test_green_light_timer_not_done` to :ref:`test_green_light_timer_not_done_walk_button`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 10

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                ),
                YELLOW
            )

        def test_green_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_green_light_timer_not_done_walk_button'

----

*********************************************************************************
test_green_light_timer_done_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :green:`GREEN` AND the timer is :green:`done` is

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_green_light_timer_done` for if the current light is :green:`GREEN` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 9-16

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                ),
                YELLOW
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                RED
            )

        def test_green_light_timer_not_done_walk_button(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != 'RED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :yellow:`YELLOW` to :red:`RED` in the :ref:`test_green_light_timer_done`

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 7

          self.assertEqual(
              src.traffic_light.control(
                  current_light=GREEN,
                  timer_done=True,
                  walk_button=False,
              ),
              YELLOW
          )

      def test_green_light_timer_not_done_walk_button(self):

the test passes.

.. code-block:: python

  control(
      current_light='GREEN', timer_done=True,
      walk_button=False
  ) -> 'YELLOW'
  control(
      current_light='GREEN', timer_done=False,
      walk_button=True
  ) -> 'GREEN'
  control(
      current_light='GREEN', timer_done=False,
      walk_button=False
  ) -> 'GREEN'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``walk_button`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_green_light_timer_done` for if the current light is :green:`GREEN` AND the timer is :green:`done` AND the walk button is :green:`pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 6

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                YELLOW
            )

        def test_green_light_timer_not_done_walk_button(self):

  the test is still green.

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=True,
        walk_button=True
    ) -> 'YELLOW'
    control(
        current_light='GREEN', timer_done=True,
        walk_button=False
    ) -> 'YELLOW'
    control(
        current_light='GREEN', timer_done=False,
        walk_button=True
    ) -> 'GREEN'
    control(
        current_light='GREEN', timer_done=False,
        walk_button=False
    ) -> 'GREEN'

* I change the name of the test from :ref:`test_green_light_timer_done` to :ref:`test_green_light_timer_done_walk_button`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 10

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                ),
                YELLOW
            )

        def test_green_light_timer_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_green_light_timer_done_walk_button'

----

*********************************************************************************
test_yellow_light_timer_not_done_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :yellow:`YELLOW` AND the timer is :red:`NOT done` is

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_yellow_light_timer_not_done` for if the current light is :yellow:`YELLOW` AND the timer is :red:`NOT done` AND the walk button is :red:`NOT pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 9-16

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                ),
                YELLOW
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                RED
            )

        def test_green_light_timer_done_walk_button(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != 'RED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :red:`RED` to :yellow:`YELLOW` in :ref:`test_yellow_light_timer_not_done`

.. code-block:: python
  :lineno-start: 45
  :emphasize-lines: 7

          self.assertEqual(
              src.traffic_light.control(
                  current_light=YELLOW,
                  timer_done=False,
                  walk_button=False,
              ),
              YELLOW
          )

      def test_green_light_timer_done_walk_button(self):

the test passes.

.. code-block:: python

  control(
      current_light='YELLOW', timer_done=False,
      walk_button=False
  ) -> 'YELLOW'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``walk_button`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_yellow_light_timer_not_done` for if the current light is :yellow:`YELLOW` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW
            )

        def test_green_light_timer_done_walk_button(self):

  the test is still green.

  .. code-block:: python

    control(
        current_light='YELLOW', timer_done=False,
        walk_button=True
    ) -> 'YELLOW'
    control(
        current_light='YELLOW', timer_done=False,
        walk_button=False
    ) -> 'YELLOW'

* I change the name of the test from :ref:`test_yellow_light_timer_not_done` to :ref:`test_yellow_light_timer_not_done_walk_button`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 10

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                ),
                RED
            )

        def test_yellow_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_yellow_light_timer_not_done_walk_button'

----

*********************************************************************************
test_yellow_light_timer_done_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :yellow:`YELLOW` AND the timer is :green:`done` is

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
================  ===============  =================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_yellow_light_timer_done` for if the current light is :yellow:`YELLOW` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 9-16

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                ),
                RED
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                GREEN
            )

        def test_yellow_light_timer_not_done_walk_button(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'GREEN'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :green:`GREEN` to :red:`RED` in the :ref:`test_yellow_light_timer_done`

.. code-block:: python
  :lineno-start: 36
  :emphasize-lines: 7

          self.assertEqual(
              src.traffic_light.control(
                  current_light=YELLOW,
                  timer_done=True,
                  walk_button=False,
              ),
              RED
          )

      def test_yellow_light_timer_not_done_walk_button(self):

the test passes.

.. code-block:: python

  control(
      current_light='YELLOW', timer_done=True,
      walk_button=False
  ) -> 'RED'
  control(
      current_light='YELLOW', timer_done=False,
      walk_button=True
  ) -> 'YELLOW'
  control(
      current_light='YELLOW', timer_done=False,
      walk_button=False
  ) -> 'YELLOW'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``walk_button`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_yellow_light_timer_done` for if the current light is :yellow:`YELLOW` AND the timer is :green:`done` AND the walk button is :green:`pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                RED
            )

        def test_yellow_light_timer_not_done_walk_button(self):

  the test is still green.

  .. code-block:: python

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=True
    ) -> 'RED'
    control(
        current_light='YELLOW', timer_done=True,
        walk_button=False
    ) -> 'RED'
    control(
        current_light='YELLOW', timer_done=False,
        walk_button=True
    ) -> 'YELLOW'
    control(
        current_light='YELLOW', timer_done=False,
        walk_button=False
    ) -> 'YELLOW'

* I change the name of the test from :ref:`test_yellow_light_timer_done` to :ref:`test_yellow_light_timer_done_walk_button`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 10

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                ),
                RED
            )

        def test_yellow_light_timer_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_yellow_light_timer_done_walk_button'













* I add an :ref:`if statement<if statements>` for ``walk_button``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-17

    def control(
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

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1-2

        # if walk_button == True:
        if bool(walk_button) == True:
            return 'RED'

        return green

  the test is still green.



----

*********************************************************************************
test_red_light_w_walk_button
*********************************************************************************

----

The :ref:`truth table` for if the **Traffic Light** is :red:`RED` is

================  ===============  =================  =================
current light     timer            walk button        output
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

I add an :ref:`assertion<what is an assertion?>` for if the current light is :red:`RED` AND the timer is :green:`done` and the walk button is :green:`pushed`, to :ref:`test_red_light` in ``tests/test_traffic_light.py``

================  ===============  =================  =================
current light     timer            walk button        output
================  ===============  =================  =================
:red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
================  ===============  =================  =================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 2-8

      def test_red_light(self):
          my_expectation = 'RED'
          reality = src.traffic_light.control(
              current_light='RED',
              timer_done=True,
              walk_button=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'GREEN'
          reality = src.traffic_light.control(
              current_light='RED',
              timer_done=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'RED'
          reality = src.traffic_light.control(
              current_light='RED',
              timer_done=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_yellow_light(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: control() got
             an unexpected keyword argument 'walk_button'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``walk_button`` to the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(current_light, timer_done, walk_button):
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

    FAILED ...test_green_light - TypeError:
        control() missing 1 required positional argument
    FAILED ...test_red_light - TypeError:
        control() missing 1 required positional argument
    FAILED ...test_yellow_light - TypeError:
        control() missing 1 required positional argument

  because all the other tests :ref:`call<how to call a function with input>` the ``control`` :ref:`function<what is a function?>` with two arguments and I changed the :ref:`function signature<what is a function?>` to make it expect three. I need to make the third argument a choice.

* I could add the ``walk_button`` parameter to every :ref:`call<how to call a function with input>` to the ``control`` :ref:`function<what is a function?>` in every test or add a :ref:`default value<test_optional_arguments>` for the new :ref:`keyword argument<test_keyword_arguments>` to make it a choice, NOT a requirement. I make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def control(
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

    def control(
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

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1-2

        # if walk_button == True:
        if bool(walk_button) == True:
            return 'RED'

        return green

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2-3

        # if walk_button == True:
        # if bool(walk_button) == True:
        if bool(walk_button):
            return 'RED'

        return green

  still green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-4

        # if walk_button == True:
        # if bool(walk_button) == True:
        # if bool(walk_button):
        if walk_button:
            return 'RED'

  green because ``if bool(something) == True`` is the same as ``if something``

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def control(
            current_light, timer_done,
            walk_button=False
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'RED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-12, 21-22

    def control(
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

  still green.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def control(
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

  When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done` it returns the current light
  * if the timer is :green:`done`

    - it returns :red:`RED` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns :red:`RED` if the walk button is :green:`pushed`
      * it returns :green:`GREEN` if the walk button is :red:`NOT pushed`

* I do not need to do anything to the :ref:`assertion<what is an assertion?>` for if the light is :red:`RED` AND the timer is :green:`done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  ================  ===============  =================  =================

  because

  .. code-block:: python

    src.traffic_light.control(
        current_light='RED',
        timer_done=True,
    )

  is now the same as

  .. code-block:: python

    src.traffic_light.control(
        current_light='RED',
        timer_done=True,
        walk_button=False,
    )

  since the :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`. :ref:`A function uses the default value for a parameter when it is :ref:`called<how to call a function with input>` without the parameter<test_optional_arguments>`.

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for if the light is :red:`RED` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  :red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 21

        def test_red_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_yellow_light(self):

  green.

* I change the expectation to make sure the test works

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

            my_expectation = 'BOOM'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'BOOM'

  because the ``control`` :ref:`function<what is a function?>` returned ``'RED'`` and the :ref:`assertion<what is an assertion?>` expects ``'BOOM'``

* I change the expectation back

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1

            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_yellow_light(self):

  the test is green again

* I add an :ref:`assertion<what is an assertion?>` for if the light is :red:`RED` AND the timer is :red:`NOT done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  :red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
  :red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 25-29

        def test_red_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='RED',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_yellow_light(self):

  green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'RED'``)
  * I do not need to provide a value for the ``walk_button`` parameter because

    .. code-block:: python

      src.traffic_light.control(
          current_light='RED',
          timer_done=False,
      )

    is the same as

    .. code-block:: python

      src.traffic_light.control(
          current_light='RED',
          timer_done=False,
          walk_button=False,
      )

    since the :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`. :ref:`A function uses the default value for a parameter when it is :ref:`called<how to call a function with input>` without the parameter<test_optional_arguments>`.

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_red_light(self):
            red = 'RED'

            my_expectation = 'RED'

* I use the ``red`` :ref:`local variable<what is a variable?>` to remove the repetition of ``'RED'`` and ``my_expectation`` when its value is ``'RED'``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4, 6-7, 11-12, 16-17, 22, 24-25, 29-30, 33-34, 37-38

        def test_red_light(self):
            red = 'RED'

            # my_expectation = 'RED'
            reality = src.traffic_light.control(
                # current_light='RED',
                current_light=red,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                # current_light='RED',
                current_light=red,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'RED'
            reality = src.traffic_light.control(
                # current_light='RED',
                current_light=red,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            reality = src.traffic_light.control(
                # current_light='RED',
                current_light=red,
                timer_done=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

        def test_yellow_light(self):

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_red_light(self):
            red = 'RED'

            reality = src.traffic_light.control(
                current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                current_light=red,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light=red,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.control(
                current_light=red,
                timer_done=False,
            )
            self.assertEqual(reality, red)

        def test_yellow_light(self):

* I add a :ref:`default value<test_optional_arguments>` for the ``current_light`` :ref:`keyword argument<test_keyword_arguments>` to the ``control`` :ref:`function<what is a function?>` ``src/traffic_light/__init__.py`` as a fail safe so that the light is always :red:`RED` if no value is given

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(
            current_light='RED', timer_done,
            walk_button=False,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``tests/test_traffic_light.py``

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

* I add a :ref:`default value<test_optional_arguments>` for ``timer_done`` to the ``control`` :ref:`function<what is a function?>` ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(
        current_light='RED', timer_done=False,
        walk_button=False,
    ):

  the test is green again. All the arguments in the :ref:`function<what is a function?>` are now choices, which means

  .. code-block:: python

    src.traffic_light.control()

  is the same as

  .. code-block:: python

    src.traffic_light.control(
        current_light='RED',
        timer_done=False,
        walk_button=False,
    )

  because

  - the :ref:`default value<test_optional_arguments>` for ``current_light`` is ``'RED'``
  - the :ref:`default value<test_optional_arguments>` for ``timer_done`` is :ref:`False<test_what_is_false>`
  - the :ref:`default value<test_optional_arguments>` for ``walk_button`` is :ref:`False<test_what_is_false>`
  - :ref:`A function uses the default value for a parameter when it is :ref:`called<how to call a function with input>` without the parameter<test_optional_arguments>`

* I change the name of :ref:`test_red_light` to :ref:`test_red_light_w_walk_button` in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_red_light_w_walk_button(self):
            red = 'RED'

* I remove the ``current_light`` parameter from the calls to ``src.traffic_light.show`` in :ref:`test_red_light_w_walk_button` in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5, 13, 19, 26

        def test_red_light_w_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.control(
                # current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                # current_light=red,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                # current_light=red,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.control(
                # current_light=red,
                timer_done=False,
            )
            self.assertEqual(reality, red)

        def test_yellow_light(self):

  the test is still green.

* I remove the ``timer_done`` parameter when it is :ref:`False<test_what_is_false>` from :ref:`test_red_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 20, 27

        def test_red_light_w_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.control(
                # current_light=red,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                # current_light=red,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                # current_light=red,
                # timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.control(
                # current_light=red,
                # timer_done=False,
            )
            self.assertEqual(reality, red)

        def test_yellow_light(self):

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_red_light_w_walk_button(self):
            red = 'RED'

            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, red)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                walk_button=True,
            )
            self.assertEqual(reality, red)

            reality = src.traffic_light.control()
            self.assertEqual(reality, red)

        def test_yellow_light(self):

  green.

.. admonition:: REMINDER

  When the ``control`` :ref:`function<what is a function?>` is called

  .. code-block:: python
    :linenos:

    def control(
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

  * if the timer is :red:`NOT done` it returns the current light
  * if the timer is :green:`done`

    - it returns :red:`RED` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns :red:`RED` if the walk button is :green:`pushed`
      * it returns :green:`GREEN` if the walk button is :red:`NOT pushed`

----

*********************************************************************************
test_yellow_light_w_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :yellow:`YELLOW` with the walk button is

================  ===============  =================  =================
current light     timer            walk button        output
================  ===============  =================  =================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  =================

* I add ``walk_button`` to the :ref:`call<how to call a function with input>` to ``src.traffic_light.show`` for if the light is :yellow:`YELLOW` AND the timer is :green:`done` and the walk button is :green:`pushed`, in the first :ref:`assertion<what is an assertion?>` of :ref:`test_yellow_light` in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6

        def test_yellow_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_green_light(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the light is :yellow:`YELLOW` AND the timer is :green:`done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 10-14

        def test_yellow_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_green_light(self):

  still green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'RED'``)
  * I do not need to give a value for the ``walk_button`` parameter because

    .. code-block:: python

      src.traffic_light.control(
          current_light='YELLOW',
          timer_done=True,
      )

    is the same as

    .. code-block:: python

      src.traffic_light.control(
          current_light='YELLOW',
          timer_done=True,
          walk_button=False,
      )

    the :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`. :ref:`A function uses the default value for a parameter when it is :ref:`called<how to call a function with input>` without the parameter<test_optional_arguments>`.

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>`, for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  :yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 20

        def test_yellow_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_green_light(self):

  green.

* I add an :ref:`assertion<what is an assertion?>` for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
  :yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
  :yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 24-27

        def test_yellow_light(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='YELLOW',
            )
            self.assertEqual(reality, my_expectation)

        def test_green_light(self):

  still green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'YELLOW'``)
  * I do not need to give a value for the ``walk_button`` and ``timer_done`` parameters because

    .. code-block:: python

      src.traffic_light.control(
          current_light='YELLOW',
      )

    is the same as

    .. code-block:: python

      src.traffic_light.control(
          current_light='YELLOW',
          timer_done=False,
          walk_button=False,
      )

    - the :ref:`default value<test_optional_arguments>` for the ``timer_done`` parameter is :ref:`False<test_what_is_false>`
    - the :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`
    - :ref:`A function uses the default value for a parameter when it is :ref:`called<how to call a function with input>` without the parameter<test_optional_arguments>`

* I change the name of the test from :ref:`test_yellow_light` to :ref:`test_yellow_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 4

            reality = src.traffic_light.control()
            self.assertEqual(reality, red)

        def test_yellow_light_w_walk_button(self):
            my_expectation = 'RED'
            reality = src.traffic_light.control(
                current_light='YELLOW',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_yellow_light_w_walk_button(self):
            yellow = 'YELLOW'

            my_expectation = 'RED'

* I use the new :ref:`variable<what is a variable?>` to remove repetition of ``'YELLOW'`` and the ``my_expectation`` :ref:`variable<what is a variable?>` when its value is ``'YELLOW'``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6-7, 14-15, 20, 22-23, 27-28, 31-32, 34-35, 39-40

        def test_yellow_light_w_walk_button(self):
            yellow = 'YELLOW'

            my_expectation = 'RED'
            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, yellow)

        def test_green_light(self):

  the test is still green.

* I add a :ref:`variable<what is a variable?>` for :red:`RED` (a repetition of the :ref:`variable<what is a variable?>` in :ref:`test_red_light_w_walk_button`, oh boy)

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2

        def test_yellow_light_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            my_expectation = 'RED'

* I use the new :ref:`variable<what is a variable?>` to remove repetition, such irony (I use a repetition to remove a repetition)

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4, 11-12, 19-20

        def test_yellow_light_w_walk_button(self):
            red, yellow = 'RED', 'YELLOW'

            # my_expectation = 'RED'
            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, red)

  still green.

* I make a :ref:`global variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED = 'RED'


    class TestTrafficLight(unittest.TestCase):

* I use the ``RED`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_red_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2, 8-9, 20-21, 24-25

        def test_red_light_w_walk_button(self):
            # red = 'RED'

            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                walk_button=True,
            )
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control()
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

        def test_yellow_light_w_walk_button(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_red_light_w_walk_button(self):
            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control()
            self.assertEqual(reality, RED)

        def test_yellow_light_w_walk_button(self):

* I use the ``RED`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_yellow_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2-3, 13-14, 22-23

        def test_yellow_light_w_walk_button(self):
            # red, yellow = 'RED', 'YELLOW'
            yellow = 'YELLOW'

            # my_expectation = 'RED'
            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                # current_light='YELLOW',
                current_light=yellow,
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, red)
            self.assertEqual(reality, RED)

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 31

        def test_yellow_light_w_walk_button(self):
            yellow = 'YELLOW'

            reality = src.traffic_light.control(
                current_light=yellow,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                current_light=yellow,
                timer_done=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                current_light=yellow,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, yellow)

            reality = src.traffic_light.control(
                current_light=yellow,
            )
            self.assertEqual(reality, yellow)

        def test_green_light(self):

----

*********************************************************************************
test_green_light_w_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :green:`GREEN` with the walk button is

================  ===============  =================  =================
current light     timer            walk button        output
================  ===============  =================  =================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  =================

* I add ``walk_button`` to the :ref:`call<how to call a function with input>` to ``src.traffic_light.show`` for if the light is :green:`GREEN` AND the timer is :green:`done` and the walk button is :green:`pushed`, in the first :ref:`assertion<what is an assertion?>` of :ref:`test_green_light` in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 6

        def test_green_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :green:`done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 10-14

        def test_green_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=False,
            )
            self.assertEqual(reality, my_expectation)

  still green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'YELLOW'``)
  * I do not need to give a value for the ``walk_button`` parameter because

    .. code-block:: python

      src.traffic_light.control(
          current_light='GREEN',
          timer_done=True,
      )

    is the same as

    .. code-block:: python

      src.traffic_light.control(
          current_light='GREEN',
          timer_done=True,
          walk_button=False,
      )

    the :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`

* I add ``walk_button`` to the third :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  :green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 20

        def test_green_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green.

* I add an :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :red:`NOT done` and the walk button is :red:`NOT pushed`

  ================  ===============  =================  =================
  current light     timer            walk button        output
  ================  ===============  =================  =================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
  :green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
  :green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
  ================  ===============  =================  =================

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 24-27

        def test_green_light(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                current_light='GREEN',
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green.

  * I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (``'GREEN'``)
  * I do not need to give a value for the ``walk_button`` and ``timer_done`` parameters because

    .. code-block:: python

      src.traffic_light.control(
          current_light='GREEN',
      )

    is the same as

    .. code-block:: python

      src.traffic_light.control(
          current_light='GREEN',
          timer_done=False,
          walk_button=False,
      )

    - the :ref:`default value<test_optional_arguments>` for the ``timer_done`` parameter is :ref:`False<test_what_is_false>`
    - the :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter is :ref:`False<test_what_is_false>`
    - :ref:`A function uses the default value for a parameter when it is :ref:`called<how to call a function with input>` without the parameter<test_optional_arguments>`

* I change the name of the test from :ref:`test_green_light` to :ref:`test_green_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 6

            reality = src.traffic_light.control(
                current_light=yellow,
            )
            self.assertEqual(reality, yellow)

        def test_green_light_w_walk_button(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                current_light='GREEN',
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

* I add a :ref:`global variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW = 'RED', 'YELLOW'


    class TestTrafficLight(unittest.TestCase):

* I use the ``YELLOW`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_yellow_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2, 5-6, 13-14, 20-21, 25-26, 29-30, 32-33

        def test_yellow_light_w_walk_button(self):
            # yellow = 'YELLOW'

            reality = src.traffic_light.control(
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                # current_light=yellow,
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, yellow)
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.control(
                # current_light=yellow,
                current_light=YELLOW,
            )
            # self.assertEqual(reality, yellow)
            self.assertEqual(reality, YELLOW)

        def test_green_light_w_walk_button(self):

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 31

        def test_yellow_light_w_walk_button(self):
            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.control(
                current_light=YELLOW,
            )
            self.assertEqual(reality, YELLOW)

        def test_green_light_w_walk_button(self):

* I add a :ref:`global variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'


    class TestTrafficLight(unittest.TestCase):

* I use the ``GREEN`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_red_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8, 12-13

        def test_red_light_w_walk_button(self):
            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            # my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.control(
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control()
            self.assertEqual(reality, RED)

        def test_yellow_light_w_walk_button(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_red_light_w_walk_button(self):
            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control(
                timer_done=True,
            )
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.control(
                walk_button=True,
            )
            self.assertEqual(reality, RED)

            reality = src.traffic_light.control()
            self.assertEqual(reality, RED)

        def test_yellow_light_w_walk_button(self):

* I use the :green:`GREEN` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_green_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4-5, 12-13, 18, 20-21, 25-26, 29-30, 32-33

        def test_green_light_w_walk_button(self):
            my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.traffic_light.control(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'GREEN'
            reality = src.traffic_light.control(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.control(
                # current_light='GREEN',
                current_light=GREEN,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, GREEN)

  still green.

* I use the :yellow:`YELLOW` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_green_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2, 9-10, 17-18

        def test_green_light_w_walk_button(self):
            # my_expectation = 'YELLOW'
            reality = src.traffic_light.control(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.control(
                # current_light='GREEN',
                current_light=GREEN,
                timer_done=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, YELLOW)

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 56

        def test_green_light_w_walk_button(self):
            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
            )
            self.assertEqual(reality, YELLOW)

            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(reality, GREEN)

            reality = src.traffic_light.control(
                current_light=GREEN,
            )
            self.assertEqual(reality, GREEN)


    # Exceptions seen

* I want to remove the ``reality`` :ref:`variable<what is a variable?>`, because it is only used once for each :ref:`assertion<what is an assertion?>`, I can make the :ref:`call<how to call a function with input>` to ``src.traffic_light.show`` directly, in :ref:`test_green_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7-11, 18-22, 29-33, 38-42

        def test_green_light_w_walk_button(self):
            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                reality,
                YELLOW
            )

            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                reality,
                YELLOW
            )

            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                reality,
                green.
            )

            reality = src.traffic_light.control(
                current_light=GREEN,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                reality,
                green.
            )

* I remove the ``reality`` :ref:`variable<what is a variable?>` from the :ref:`assertions<what is an assertion?>` :ref:`test_green_light_w_walk_button`, I no longer need it to be a middle man

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 9-14, 24-28, 39-44, 53-56

        def test_green_light_w_walk_button(self):
            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
                walk_button=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW
            )

            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=True,
            )
            # self.assertEqual(reality, YELLOW)
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                ),
                YELLOW
            )

            reality = src.traffic_light.control(
                current_light=GREEN,
                timer_done=False,
                walk_button=True,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                green.
            )

            reality = src.traffic_light.control(
                current_light=GREEN,
            )
            # self.assertEqual(reality, GREEN)
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=GREEN,
                ),
                green.
            )

  green.

* I remove the commented lines and ``reality`` :ref:`variable<what is a variable?>` from :ref:`test_green_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 56

        def test_green_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                ),
                YELLOW
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                green.
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                ),
                green.
            )


    # Exceptions seen

  still green.

* I do the same thing with :ref:`test_yellow_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-10, 16-19, 26-29, 34-37

        def test_yellow_light_w_walk_button(self):
            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(
                reality,
                YELLOW
            )

            reality = src.traffic_light.control(
                current_light=YELLOW,
            )
            self.assertEqual(
                reality,
                YELLOW
            )

        def test_green_light_w_walk_button(self):

* I :ref:`call<how to call a function with input>` the ``control`` :ref:`function<what is a function?>` directly in the :ref:`assertions<what is an assertion?>` in :ref:`test_yellow_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8-13, 22-26, 36-41, 49-52

        def test_yellow_light_w_walk_button(self):
            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                ),
                RED
            )

            reality = src.traffic_light.control(
                current_light=YELLOW,
                timer_done=False,
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )

            reality = src.traffic_light.control(
                current_light=YELLOW,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    current_light=YELLOW,
                ),
                YELLOW
            )

        def test_green_light_w_walk_button(self):

  the test is still green.

* I remove the ``reality`` :ref:`variable<what is a variable?>` and comments from :ref:`test_yellow_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 30

        def test_yellow_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                ),
                YELLOW
            )

        def test_green_light_w_walk_button(self):

* I also do it in :ref:`test_red_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-9, 14-17, 22-25, 28-31

        def test_red_light_w_walk_button(self):
            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.control(
                timer_done=True,
            )
            self.assertEqual(
                reality,
                green.
            )

            reality = src.traffic_light.control(
                walk_button=True,
            )
            self.assertEqual(
                reality,
                RED
            )

            reality = src.traffic_light.control()
            self.assertEqual(
                reality,
                RED
            )

* I :ref:`call<how to call a function with input>` the ``control`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7-11, 19-22, 30-33, 39-40

        def test_red_light_w_walk_button(self):
            reality = src.traffic_light.control(
                timer_done=True,
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.control(
                timer_done=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    timer_done=True,
                ),
                green.
            )

            reality = src.traffic_light.control(
                walk_button=True,
            )
            self.assertEqual(
                # reality,
                src.traffic_light.control(
                    walk_button=True,
                ),
                RED
            )

            reality = src.traffic_light.control()
            self.assertEqual(
                # reality,
                src.traffic_light.control(),
                RED
            )

  still green.

* I remove the ``reality`` :ref:`variable<what is a variable?>` and the comments from :ref:`test_red_light_w_walk_button`

  .. code-block:: python
    :lineno-start: 10

        def test_red_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                ),
                green.
            )

            self.assertEqual(
                src.traffic_light.control(
                    walk_button=True,
                ),
                RED
            )

            self.assertEqual(
                src.traffic_light.control(),
                RED
            )

        def test_yellow_light_w_walk_button(self):

.. admonition:: REMINDER

  When the ``control`` :ref:`function<what is a function?>` is called

  .. code-block:: python
    :linenos:

    def control(
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

  * if the timer is :red:`NOT done` it returns the current light
  * if the timer is :green:`done`

    - it returns :red:`RED` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns :red:`RED` if the walk button is :green:`pushed`
      * it returns :green:`GREEN` if the walk button is :red:`NOT pushed`

----

*************************************************************************************
test_red_light_w_walk
*************************************************************************************

The inputs for the **Traffic Light** up till now are

* did the person push the walk button?
* what color is the light now?
* is the timer done?

which gives this :ref:`truth table`

================  ===============  =================  =================
current light     timer            walk button        output
================  ===============  =================  =================
:red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
================  ===============  =================  =================

================  ===============  =================  =================
current light     timer            walk button        output
================  ===============  =================  =================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  =================

================  ===============  =================  =================
current light     timer            walk button        output
================  ===============  =================  =================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  =================

I want the **Traffic Light** to show ``WALK`` when a person can cross the street or ``NO WALK`` when a person can NOT cross the street. This means the :ref:`truth table` for if the **Traffic Light** is :red:`RED` with the walk sign is

================  =============== ================= =================================
current light     timer           walk button       output
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

I add the value for the ``current_light`` parameter in the :ref:`call<how to call a function with input>` to the ``control`` :ref:`function<what is a function?>` for if the light is :red:`RED` AND the timer is :green:`done` and the walk button is :green:`pushed`, to make it clearer, then I change the expectation of the first :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_w_walk_button`

================  =============== ================= =================================
current light     timer           walk button       output
================  =============== ================= =================================
:red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
================  =============== ================= =================================

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4, 8

        def test_red_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
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

I change the :ref:`return statement<the return statement>` for this case, in the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 17

  def control(
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

the test passes. When the ``control`` :ref:`function<what is a function?>` is called

* if the timer is :red:`NOT done` it returns the current light
* if the timer is :green:`done`

  - it returns :red:`RED` if the current light is :yellow:`YELLOW`
  - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
  - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

    * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
    * it returns :green:`GREEN` if the walk button is :red:`NOT pushed`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add values for the other parameters, to make it clearer for if the light is :red:`RED` AND the timer is :green:`done`, and the walk button is :green:`pushed`, then I change the expectation of the second :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 13, 15, 17

        def test_red_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I add ``'NO WALK'`` to the :ref:`return statement<the return statement>` for this case in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19

    def control(
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

  the test passes. When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done` it returns the current light
  * if the timer is :green:`done`

    - it returns :red:`RED` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
      * it returns ``'GREEN', 'NO WALK'`` if the walk button is :red:`NOT pushed`

* I change the third :ref:`assertion<what is an assertion?>` for if the light is :red:`RED` AND the timer is :red:`NOT done`, and the walk button is :green:`pushed`, in :ref:`test_red_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  :red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 22-23, 26

        def test_red_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I add an :ref:`if statement<if statements>` for this case to the one for if the timer is :red:`NOT done`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def control(
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

* I add values for the other parameters in the next :ref:`assertion<what is an assertion?>`, to make it clearer for the case where the light is :red:`RED` AND the timer is :red:`NOT done`, and the walk button is :red:`NOT pushed`,  in :ref:`test_red_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  :red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
  :red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 30-35

        def test_red_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_yellow_light_w_walk_button(self):

  the test passes. When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done`

    - it returns ``'RED', 'WALK'`` if the current light is :red:`RED`
    - it returns the current light if the current light is NOT :red:`RED`

  * if the timer is :green:`done`

    - it returns :red:`RED` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
      * it returns ``'GREEN', 'NO WALK'`` if the walk button is :red:`NOT pushed`

* I change the name of the test from :ref:`test_red_light_w_walk_button` to :ref:`test_red_light_w_walk`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_red_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

----

*************************************************************************************
test_yellow_light_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :yellow:`YELLOW` with the walk sign is

================  =============== ================= =================================
current light     timer           walk button       output
================  =============== ================= =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= =================================

* I change the expectation of the first :ref:`assertion<what is an assertion?>` for if the light is :yellow:`YELLOW` AND the timer is :green:`done` and the walk button is :green:`pushed`, in :ref:`test_yellow_light_w_walk_button`

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 8

        def test_yellow_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != ('RED', 'WALK')

* I add ``'WALK'`` to the :ref:`if statement<if statements>` for this case, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13

    def control(
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

* I change the second :ref:`assertion<what is an assertion?>` which is for if the light is :yellow:`YELLOW` AND the timer is :green:`done` and the walk button is :red:`NOT pushed`, in :ref:`test_yellow_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 15, 17

        def test_yellow_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

  the test passes. When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done`

    - it returns ``'RED', 'WALK'`` if the current light is :red:`RED`
    - it returns the current light if the current light is NOT :red:`RED`

  * if the timer is :green:`done`

    - it returns ``'RED', 'WALK'`` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
      * it returns ``'GREEN', 'NO WALK'`` if the walk button is :red:`NOT pushed`

* I change the third :ref:`assertion<what is an assertion?>`, which is for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 26

        def test_yellow_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != ('YELLOW', 'NO WALK')

* I add an :ref:`if statement<if statements>` to the one for if the timer is :red:`NOT done` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11

    def control(
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

* I change the last :ref:`assertion<what is an assertion?>`, which is for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done`, and the walk button is :red:`NOT pushed`, in :ref:`test_yellow_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
  :yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 32-33, 35

        def test_yellow_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

        def test_green_light_w_walk_button(self):

  the test passes. When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done`

    - it returns ``'RED', 'WALK'`` if the current light is :red:`RED`
    - it returns ``'YELLOW', 'NO WALK'`` if the current light is :yellow:`YELLOW`
    - it returns the current light if the current light is NOT :red:`RED` AND NOT :yellow:`YELLOW`

  * if the timer is :green:`done`

    - it returns ``'RED', 'WALK'`` if the current light is :yellow:`YELLOW`
    - it returns :yellow:`YELLOW` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
      * it returns ``'GREEN', 'NO WALK'`` if the walk button is :red:`NOT pushed`

* I change the name of the test from :ref:`test_yellow_light_w_walk_button` to :ref:`test_yellow_light_w_walk`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_yellow_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

----

*************************************************************************************
test_green_light_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :green:`GREEN` with the walk sign is

================  =============== ================= =================================
current light     timer           walk button       output
================  =============== ================= =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
================  =============== ================= =================================

* I change the expectation of the first :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :green:`done`, and the walk button is :green:`pushed`, in :ref:`test_green_light_w_walk_button`

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 8

        def test_green_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != ('YELLOW', 'NO WALK')

* I add ``'NO WALK'`` to the :ref:`if statement<if statements>` for if the current light is :green:`GREEN`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 18

    def control(
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

* I change the second :ref:`assertion<what is an assertion?>`, which is for if the light is :green:`GREEN` AND the timer is :green:`done`, and the walk button is :red:`NOT pushed`, in :ref:`test_green_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 15, 17

        def test_green_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

  the test passes. When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done`

    - it returns ``'RED', 'WALK'`` if the current light is :red:`RED`
    - it returns ``'YELLOW', 'NO WALK'`` if the current light is :yellow:`YELLOW`
    - it returns the current light if the current light is NOT :red:`RED` AND NOT :yellow:`YELLOW`

  * if the timer is :green:`done`

    - it returns ``'RED', 'WALK'`` if the current light is :yellow:`YELLOW`
    - it returns ``'YELLOW', 'NO WALK'`` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
      * it returns ``'GREEN', 'NO WALK'`` if the walk button is :red:`NOT pushed`

* I change the third :ref:`assertion<what is an assertion?>`, which is for if the light is :green:`GREEN` AND the timer is :red:`NOT done`, and the walk button is :green:`pushed`

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 26

        def test_green_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'NO WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'NO WALK')

* I change the :ref:`return statement<the return statement>` of the :ref:`if statement<if statements>` for if the timer is :red:`NOT done` in the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 1
    :emphasize-lines: 12

    def control(
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

  the ``control`` :ref:`function<what is a function?>` now returns ``('GREEN', 'NO WALK')`` and the next :ref:`assertion<what is an assertion?>` expects ``'GREEN'``. I have to make the same change in the next :ref:`assertion<what is an assertion?>`

* I change the last :ref:`assertion<what is an assertion?>`, which is for if the light is :green:`GREEN` AND the timer is :red:`NOT done`, and the walk button is :red:`NOT pushed`, in :ref:`test_green_light_w_walk_button` in ``tests/test_traffic_light.py``

  ================  =============== ================= =================================
  current light     timer           walk button       output
  ================  =============== ================= =================================
  :green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
  :green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
  :green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
  ================  =============== ================= =================================

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 32-33, 35

        def test_green_light_w_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'NO WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                (GREEN, 'NO WALK')
            )


    # Exceptions seen

  the test passes. When the ``control`` :ref:`function<what is a function?>` is called

  * if the timer is :red:`NOT done`

    - it returns ``'RED', 'WALK'`` if the current light is :red:`RED`
    - it returns ``'YELLOW', 'NO WALK'`` if the current light is :yellow:`YELLOW`
    - it returns the current light, ``'NO WALK'`` if the current light is NOT :red:`RED` AND NOT :yellow:`YELLOW`

  * if the timer is :green:`done`

    - it returns ``'RED', 'WALK'`` if the current light is :yellow:`YELLOW`
    - it returns ``'YELLOW', 'NO WALK'`` if the current light is :green:`GREEN`
    - if the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN`

      * it returns ``'RED', 'WALK'`` if the walk button is :green:`pushed`
      * it returns ``'GREEN', 'NO WALK'`` if the walk button is :red:`NOT pushed`

* I change the name of the test from :ref:`test_green_light_w_walk_button` to :ref:`test_green_light_w_walk`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'NO WALK')
            )

        def test_green_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'NO WALK')
            )

----

* I add more :ref:`global variables<what is a variable?>` to ``tests/test_traffic_light.py`` to use them to remove repetition from the tests

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

* I use the ``GREEN_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(GREEN, 'NO WALK')`` in the second :ref:`assertion<what is an assertion?>` of :ref:`test_red_light_w_walk`


  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 17-18

        def test_red_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

  the test is still green.

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` in :ref:`test_red_light_w_walk`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-9, 28-29, 38-39

        def test_red_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

        def test_yellow_light_w_walk(self):

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

        def test_red_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                WALK
            )

        def test_yellow_light_w_walk(self):

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` in :ref:`test_yellow_light_w_walk`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8-9, 18-19

        def test_yellow_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

  green.

* I use the ``YELLOW_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(YELLOW, 'NO WALK')`` in :ref:`test_yellow_light_w_walk`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 28-29, 38-39

        def test_yellow_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                # (RED, 'WALK')
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

  still green.

* I remove the commented lines from :ref:`test_yellow_light_w_walk`

  .. code-block:: python
    :lineno-start: 51

        def test_yellow_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW_NO_WALK
            )

        def test_green_light_w_walk(self):

* I use the ``YELLOW_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(YELLOW, 'NO WALK')`` in :ref:`test_green_light_w_walk`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 8-9, 18-19

        def test_green_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

  green.

* I use the ``GREEN_NO_WALK`` :ref:`global variable<what is a variable?>` for ``(GREEN, 'NO WALK')`` in :ref:`test_green_light_w_walk`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 28-29, 38-39

        def test_green_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                # (YELLOW, 'NO WALK')
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                # (GREEN, 'NO WALK')
                GREEN_NO_WALK
            )

  still green.

* I remove the commented lines from :ref:`test_green_light_w_walk`

  .. code-block:: python
    :lineno-start: 88

        def test_green_light_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                YELLOW_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN_NO_WALK
            )

            self.assertEqual(
                src.traffic_light.control(
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

* I add :ref:`variables<what is a variable?>` for ``'WALK'`` and ``'NO WALK'`` to the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def control(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

* I use the new :ref:`variables<what is a variable?>` to remove repetition

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11, 14-17, 20-21, 24-25, 28-29, 31-32

    def control(
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

  the tests are still green.

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

  still green.

* I write out the :ref:`if statement<if statements>` for if the light is :red:`RED` AND the timer is :green:`done`, to make it clearer

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 9, 11, 14, 17-20

        if current_light == yellow:
            # return red, 'WALK'
            return walk

        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk

        # if walk_button:
            # return red, 'WALK'
            # return walk

        # return green, 'NO WALK'
        # return green, no_walk

        if current_light == red:
            if not walk_button:
                return green, no_walk
            else:
                return walk

  green.

* the ``walk`` :ref:`variable<what is a variable?>` which is ``'RED', 'WALK'``, happens 3 times in the :ref:`function<what is a function?>`, I add a :ref:`return statement<the return statement>` to make it the default state of the light

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7

        if current_light == red:
            if not walk_button:
                return green, no_walk
            else:
                return walk

        return walk

  still green. This means if none of the :ref:`conditions<if statements>` in the ``control`` :ref:`function<what is a function?>` are met, the light stays :red:`RED` and shows ``'WALK'``

* I no longer need the :ref:`else clause<if statements>` for when the walk button is :green:`pushed` because it returns the default state (``'RED', 'WALK'``) when the list is :red:`RED` AND the timer is :green:`done`. I comment it out

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5

        if current_light == red:
            if not walk_button:
                return green, no_walk
            # else:
                # return walk

        return walk

  the tests are still green.

* I rewrite the :ref:`if statement<if statements>` for if the current light is :red:`red` AND the timer is :green:`done` AND the walk button is :green:`pushed` with :ref:`Logical Conjunction(AND)<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 38

        # if current_light == red:
            # if not walk_button:
        if current_light == red and not walk_button:
                return green, no_walk
            # else:
                # return walk

        return walk

  still green.

* I no longer need the :ref:`if statement<if statements>` for :yellow:`YELLOW` because it returns the default state (``'RED', 'WALK'``) when the timer is :green:`done`. I comment it out

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 1, 3

        # if current_light == yellow:
            # return red, 'WALK'
            # return walk

        if current_light == green:
            # return yellow, 'NO WALK'
            return yellow, no_walk

        # if walk_button:
            # return red, 'WALK'
            # return walk

        # return green, 'NO WALK'
        # return green, no_walk

        if current_light == red:
            if not walk_button:
                return green, no_walk
            # else:
                # return walk

        return walk

  green. Why does this work?

* I add an :ref:`if statement<if statements>` for if the timer is :green:`done` to make it clearer

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5, 6, 8, 19

        # if current_light == yellow:
            # return red, 'WALK'
            # return walk

        if timer_done:
            if current_light == green:
            # return yellow, 'NO WALK'
                return yellow, no_walk

        # if walk_button:
            # return red, 'WALK'
            # return walk

        # return green, 'NO WALK'
        # return green, no_walk

        # if current_light == red:
            # if not walk_button:
            if current_light == red and not walk_button:
                return green, no_walk
            # else:
                # return walk

        return walk

  still green.

* I no longer need the :ref:`else clause<if statements>` for if the current light is NOT :red:`RED` AND the timer is :red:`NOT done` because it returns the default state (``'RED', 'WALK'``) . I comment it out and the other :ref:`if statements` below it to make sure they are not run

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-6, 8-9, 11, 13

        if not timer_done:
            if current_light != red:
                return current_light, no_walk
            # else:
            #     return walk
            # if current_light == red:
                # return current_light, 'WALK'
            #     return walk
            # if current_light == yellow:
                # return current_light, 'NO WALK'
                # return current_light, no_walk
            # return current_light, 'NO WALK'
            # return current_light, no_walk

        # if current_light == yellow:
            # return red, 'WALK'
            # return walk

  the tests are still green.

* I use  :ref:`Logical Conjunction(AND)<test_logical_conjunction>` to change the :ref:`if statement<if statements>` for if the current light is NOT :red:`red` AND the timer is :red:`NOT done`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-12

    def control(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

        # if not timer_done:
        #     if current_light != red:
        if not timer_done and current_light != red:
            return current_light, no_walk
            # else:

  still green.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def control(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        no_walk = 'NO WALK'

        if not timer_done and current_light != red:
            return current_light, no_walk

        if timer_done:
            if current_light == green:
                return yellow, no_walk
            if current_light == red and not walk_button:
                return green, no_walk

        return walk

When the ``control`` :ref:`function<what is a function?>` is called

* if the timer is :red:`NOT done`

  - it returns the current light, ``'NO WALK'`` if the current light is NOT :red:`RED`

* if the timer is :green:`done`

  - it returns ``'YELLOW', 'NO WALK'`` if the current light is :green:`GREEN`
  - it returns ``'GREEN', 'NO WALK'`` if the current light is :red:`RED` AND the walk button is :red:`NOT pushed`

* it returns ``'RED', 'WALK'`` if none of the above :ref:`conditions<if statements>` are met

The :ref:`function<what is a function?>` does not look like the :ref:`truth table` and makes every test pass. There is also a problem with the :ref:`if statement<if statements>` for if the timer is :green:`done` AND the current light is NOT :red:`RED`

.. code-block:: python

  if not timer_done and current_light != red:
      return current_light, no_walk

What does it return if I :ref:`call<how to call a function with input>` the ``control`` :ref:`function<what is a function?>` with a color that is NOT :red:`RED`, :yellow:`YELLOW` or :green:`GREEN`. There is one way to find out ...

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_traffic_light.py`` and ``src/traffic_light/__init__.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for a **Traffic Light** that has a timer and a button for people to push when they want to walk. If the inputs are

* what color is the light now?
* is the timer done?
* did the person push the walk button?

then this is the :ref:`truth table` for the Traffic Light

================  =============== ================= =================================
current light     timer           walk button       output
================  =============== ================= =================================
:red:`RED`        :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :green:`pushed`   :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`RED` + :green:`WALK`
================  =============== ================= =================================

================  =============== ================= =================================
current light     timer           walk button       output
================  =============== ================= =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= =================================

================  =============== ================= =================================
current light     timer           walk button       output
================  =============== ================= =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`GREEN` + :red:`NO WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`GREEN` + :red:`NO WALK`
================  =============== ================= =================================

The **Traffic Light** only shows ``'WALK'`` when the light is :red:`RED`.

What if there is an emergency vehicle? If the **Traffic Light** changes based on the emergency vehicle, its inputs would be

* what color is the light now?
* is the timer done?
* did the person push the walk button?
* is there an emergency vehicle?

and the :ref:`truth table` would be

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:red:`RED`        :green:`done`   :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :green:`done`   :green:`pushed`   :red:`NOT emergency`  :green:`GREEN` + :red:`NO WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :green:`GREEN` + :red:`NO WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:red:`RED`        :red:`NOT done` :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :red:`RED` + :green:`WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`NOT emergency`  :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :red:`RED` + :green:`WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`NO WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :green:`emergency`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :green:`pushed`   :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :green:`emergency`    :yellow:`YELLOW` + :red:`NO WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :yellow:`YELLOW` + :red:`NO WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
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

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`
* :ref:`I know how to write programs that make decisions<truth table>`

:ref:`Would you like to test making an Automated Teller Machine?<Automated Teller Machine>`

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