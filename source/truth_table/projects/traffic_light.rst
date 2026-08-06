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

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :linenos:
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 1-9

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 12
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 12-30

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 32
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 32-48

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 50
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 50-66

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 68
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 68-84

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 86
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 86-102

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 104
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 104-

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
:green:`GREEN`    :red:`NOT done`  :green:`GREEN`
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
:yellow:`YELLOW`  :green:`done`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`RED`
:red:`RED`        :green:`done`    :green:`GREEN`
================  ===============  ================

----

*********************************************************************************
test_green_light_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change :ref:`test_failure` to :ref:`test_green_light_timer_not_done`, then add an :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :red:`NOT done`

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :green:`GREEN`    :red:`NOT done`  :green:`GREEN`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-10

    class TestTrafficLight(unittest.TestCase):

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light='GREEN',
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
                    has no attribute 'control'

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

* I delete all the text in the file_ then add a :ref:`function<what is a function?>` to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def control():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got
               an unexpected keyword argument 'timer_done'

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

* I add ``timer_done`` to the :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(timer_done):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got an
               unexpected keyword argument 'current_light'

* I add ``current_light`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(timer_done, current_light):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'GREEN'

* I change the :ref:`return statement<the return statement>` to give the test what it expects

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(timer_done, current_light):
        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='GREEN' , timer_done=False) -> 'GREEN'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_green_light_timer_not_done'

----

*********************************************************************************
test_green_light_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :green:`done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :green:`GREEN`    :green:`done`    :yellow:`YELLOW`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-17

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light='GREEN',
                ),
                'GREEN'
            )

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light='GREEN',
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

* I add an :ref:`if statement<if statements>` for this case, to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def control(timer_done, current_light):
        if timer_done:
            return 'YELLOW'

        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='GREEN' , timer_done=False) -> 'GREEN'
    control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a global :ref:`variable<what is a variable?>` for ``'GREEN'`` to ``tests/test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    GREEN = 'GREEN'


    class TestTrafficLight(unittest.TestCase):

        def test_green_light_timer_not_done(self):

* I use the new :ref:`variable<what is a variable?>` for ``'GREEN'`` in :ref:`test_green_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 5-6, 8-9

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    # current_light='GREEN',
                    current_light=GREEN,
                ),
                # 'GREEN'
                GREEN
            )

        def test_green_light_timer_done(self):

  the test is still green.

* I remove the commented lines from :ref:`test_green_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 10

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=GREEN,
                ),
                GREEN
            )

        def test_green_light_timer_done(self):

* I use the new :ref:`variable<what is a variable?>` for ``'GREEN'`` in :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 5-6

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    # current_light='GREEN',
                    current_light=GREEN,
                ),
                'YELLOW'
            )


    # Exceptions seen

  still green.

* I remove the commented lines from :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 19

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=GREEN,
                ),
                'YELLOW'
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_green_light_timer_done'

----

*********************************************************************************
test_yellow_light_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Traffic Light** is :yellow:`YELLOW` AND the timer is :red:`NOT done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 10-17

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=GREEN,
                ),
                'YELLOW'
            )

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light='YELLOW',
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

* I add an :ref:`if statement<if statements>` for if the current light is :yellow:`YELLOW` to ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def control(timer_done, current_light):
        if timer_done:
            return 'YELLOW'

        if current_light == 'YELLOW':
            return current_light

        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='GREEN' , timer_done=False) -> 'GREEN'
    control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'
    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`global variable<what is a variable?>` for ``'YELLOW'`` to ``tests/test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    GREEN, YELLOW = 'GREEN', 'YELLOW'


    class TestTrafficLight(unittest.TestCase):

* I use the new :ref:`variable<what is a variable?>` for ``'YELLOW'`` in :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 7-8

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=GREEN,
                ),
                # 'YELLOW'
                YELLOW
            )

        def test_yellow_light_timer_not_done(self):

  the test is still green.

* I remove the commented line from :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 19

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=GREEN,
                ),
                YELLOW
            )

        def test_yellow_light_timer_not_done(self):

* I use the new :ref:`variable<what is a variable?>` for ``'YELLOW'`` in :ref:`test_yellow_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-6, 8-9

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    # current_light='YELLOW',
                    current_light=YELLOW,
                ),
                # 'YELLOW'
                YELLOW
            )


    # Exceptions seen

  still green.

* I remove the commented lines from :ref:`test_yellow_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 28

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=YELLOW,
                ),
                YELLOW
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'add test_yellow_light_timer_not_done'

----

*********************************************************************************
test_yellow_light_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the light is :yellow:`YELLOW` AND the timer is :green:`done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :yellow:`YELLOW`  :green:`done`    :red:`RED`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 10-17

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=YELLOW,
                ),
                YELLOW
            )

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=YELLOW,
                ),
                'RED'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != 'RED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for if the timer is :green:`done` AND the light is :yellow:`YELLOW`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def control(timer_done, current_light):
        if timer_done:
            if current_light == 'YELLOW':
                return 'RED'
            return 'YELLOW'

        if current_light == 'YELLOW':
            return current_light

        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='GREEN' , timer_done=False) -> 'GREEN'
    control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'
    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
    control(current_light='YELLOW', timer_done=True ) -> 'RED'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_yellow_light_timer_done'

----

*********************************************************************************
test_red_light_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Traffic Light** is :red:`RED` AND the timer is :red:`NOT done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :red:`RED`        :red:`NOT done`  :red:`RED`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 10-17

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=YELLOW,
                ),
                'RED'
            )

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light='RED'
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

I add an :ref:`if statement<if statements>` to ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 3-4

      if current_light == 'YELLOW':
          return current_light
      if current_light == 'RED':
          return current_light

      return 'GREEN'

the test passes.

.. code-block:: python

  control(current_light='GREEN' , timer_done=False) -> 'GREEN'
  control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'
  control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
  control(current_light='YELLOW', timer_done=True ) -> 'RED'
  control(current_light='RED'   , timer_done=False) -> 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`global variable<what is a variable?>` for ``'RED'`` to ``tests/test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.traffic_light
    import unittest


    GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'


    class TestTrafficLight(unittest.TestCase):

* I use the :ref:`variable<what is a variable?>` for ``'RED'`` in :ref:`test_yellow_light_timer_done`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 7-8

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=YELLOW,
                ),
                # 'RED'
                RED
            )

        def test_red_light_timer_not_done(self):

  the test is still green.

* I remove the commented line from :ref:`test_yellow_light_timer_done`

  .. code-block:: python
    :lineno-start: 37

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=YELLOW,
                ),
                RED
            )

        def test_red_light_timer_not_done(self):

* I use the :ref:`variable<what is a variable?>` for ``'RED'`` in :ref:`test_red_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5-6, 8-9

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    # current_light='RED'
                    current_light=RED,
                ),
                # 'RED'
                RED
            )


    # Exceptions seen

  still green.

* I remove the commented line from :ref:`test_red_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 46

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=RED,
                ),
                RED
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_red_light_timer_not_done'

----

*********************************************************************************
test_red_light_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the light is :green:`GREEN` AND the timer is :green:`done`, to ``tests/test_traffic_light.py``

  ================  ===============  ================
  current light     timer            output
  ================  ===============  ================
  :red:`RED`        :green:`done`    :green:`GREEN`
  ================  ===============  ================

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 10-17

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=RED,
                ),
                RED
            )

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != 'GREEN'

* I add an :ref:`if statement<if statements>` for if the timer is :green:`done` AND the current light is :red:`RED` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def control(timer_done, current_light):
        if timer_done:
            if current_light == 'YELLOW':
                return 'RED'
            if current_light == 'RED':
                return 'GREEN'
            return 'YELLOW'

        if current_light == 'YELLOW':
            return current_light
        if current_light == 'RED':
            return current_light

        return 'GREEN'

  the test passes.

  .. code-block:: python

    control(current_light='GREEN' , timer_done=False) -> 'GREEN'
    control(current_light='GREEN' , timer_done=True ) -> 'YELLOW'
    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
    control(current_light='YELLOW', timer_done=True ) -> 'RED'
    control(current_light='RED'   , timer_done=False) -> 'RED'
    control(current_light='RED'   , timer_done=True ) -> 'GREEN'

* I add a git_ commit message in the other terminal_

  .. code-block::
    :emphasize-lines: 1

    git commit -am 'add test_green_light_timer_not_done'

----

*********************************************************************************
refactor if statements
*********************************************************************************

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :green:`done`

* If the timer is :green:`done`, it checks the color of the current light

  - If the current light is :yellow:`YELLOW`, it returns :red:`RED`
  - If the current light is :red:`RED`, it returns :green:`GREEN`
  - If none of the above :ref:`conditions<if statements>` are met, it returns :yellow:`YELLOW`

* If none of the above :ref:`conditions<if statements>` are met, it checks the color of the current light

  - If the current light is :yellow:`YELLOW`, it returns :yellow:`YELLOW`
  - If the current light is :red:`RED`, it returns :red:`RED`
  - If none of the above :ref:`conditions<if statements>` are met, it returns :green:`GREEN`

* I go back to the terminal_ where the tests are running
* I add an :ref:`if statement<if statements>` for if the timer is :green:`done` AND the light is :green:`GREEN`, to make it clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def control(timer_done, current_light):
        if timer_done:
            if current_light == 'GREEN':
                return 'YELLOW'
            if current_light == 'YELLOW':
                return 'RED'
            if current_light == 'RED':
                return 'GREEN'
            # return 'YELLOW'

  the tests are still green.

* I add an :ref:`if statement<if statements>` for if the timer is :red:`NOT done` to be clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-14

    def control(timer_done, current_light):
        if timer_done:
            if current_light == 'GREEN':
                return 'YELLOW'
            if current_light == 'YELLOW':
                return 'RED'
            if current_light == 'RED':
                return 'GREEN'
            # return 'YELLOW'
        if not timer_done:
            if current_light == 'YELLOW':
                return current_light
            if current_light == 'RED':
                return current_light

        return 'GREEN'

  still green.

* I add an :ref:`if statement<if statements>` for if the timer is :red:`NOT done` and the light is :green:`GREEN`, to make it clearer

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-3, 9

        if not timer_done:
            if current_light == 'GREEN':
                return current_light
            if current_light == 'YELLOW':
                return current_light
            if current_light == 'RED':
                return current_light

        # return 'GREEN'

  The ``control`` :ref:`function<what is a function?>` returns the current light in every case where the timer is :red:`NOT done`

* I add a :ref:`return statement<the return statement>` to return the current light if the timer is :red:`NOT done`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2

        if not timer_done:
            return current_light
            if current_light == 'GREEN':
                return current_light
            if current_light == 'YELLOW':
                return current_light
            if current_light == 'RED':
                return current_light

        # return 'GREEN'

  green.

* I remove the commented lines and the other :ref:`if statements<if statements>` from the :ref:`else block<if statements>` because they are no longer used

  .. code-block:: python
    :linenos:

    def control(timer_done, current_light):
        if timer_done:
            if current_light == 'GREEN':
                return 'YELLOW'
            if current_light == 'YELLOW':
                return 'RED'
            if current_light == 'RED':
                return 'GREEN'
        if not timer_done:
            return current_light

  still green.

* I move the :ref:`if statement<if statements>` for if the timer is :red:`NOT done` to the top to make the :ref:`function<what is a function?>` return a value quicker before it checks the lights

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def control(timer_done, current_light):
        if not timer_done:
            return current_light
        if timer_done:
            if current_light == 'GREEN':
                return 'YELLOW'
            if current_light == 'YELLOW':
                return 'RED'
            if current_light == 'RED':
                return 'GREEN'

* I add :ref:`variables<what is a variable?>` for ``'RED'``, ``'YELLOW'`` and ``'GREEN'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(timer_done, current_light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        if not timer_done:

* I use the new :ref:`variables<what is a variable?>` for ``'RED'``, ``'YELLOW'`` and ``'GREEN'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-17

    def control(timer_done, current_light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        if not timer_done:
            return current_light
        if timer_done:
            # if current_light == 'GREEN':
            if current_light == green:
                # return 'YELLOW'
                return yellow
            # if current_light == 'YELLOW':
            if current_light == yellow:
                # return 'RED'
                return red
            # if current_light == 'RED':
            if current_light == red:
                # return 'GREEN'
                return green

  still green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def control(timer_done, current_light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        if not timer_done:
            return current_light
        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit 'refactor if statements'

----

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :red:`NOT done`

* If the timer is :red:`NOT done` it returns the value of ``current_light``

  .. code-block:: shell

    control(current_light='GREEN', timer_done=False) -> 'GREEN'
    └── def control(timer_done, current_light):
        ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        └── if not timer_done:
            └── return current_light
                return 'GREEN'
            if timer_done:
                if current_light == green:
                    return yellow
                if current_light == yellow:
                    return red
                if current_light == red:
                    return green

  .. code-block:: shell

    control(current_light='YELLOW', timer_done=False) -> 'YELLOW'
    └── def control(timer_done, current_light):
        ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        └── if not timer_done:
            └── return current_light
                return 'YELLOW'
            if timer_done:
                if current_light == green:
                    return yellow
                if current_light == yellow:
                    return red
                if current_light == red:
                    return green

  .. code-block:: shell

    control(current_light='RED', timer_done=False) -> 'RED'
    └── def control(timer_done, current_light):
        ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        └── if not timer_done:
            └── return current_light
                return 'RED'
            if timer_done:
                if current_light == green:
                    return yellow
                if current_light == yellow:
                    return red
                if current_light == red:
                    return green

* If the timer is :green:`done` it checks the value of ``current_light``

  - If the current light is :green:`GREEN` it returns :yellow:`YELLOW`

    .. code-block:: shell

      control(current_light='GREEN', timer_done=True ) -> 'YELLOW'
      └── def control(timer_done, current_light):
          ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
          ├── if not timer_done:
          │      return current_light
          └── if timer_done:
              └── if current_light == green:
                  └── return yellow
                  if current_light == yellow:
                      return red
                  if current_light == red:
                      return green

  - If the current light is :yellow:`YELLOW` it returns :red:`RED`

    .. code-block:: shell

      control(current_light='YELLOW', timer_done=True ) -> 'RED'
      └── def control(timer_done, current_light):
          ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
          ├── if not timer_done:
          │      return current_light
          └── if timer_done:
              ├── if current_light == green:
              │       return yellow
              └── if current_light == yellow:
                  └── return red
                  if current_light == red:
                      return green

  - If the current light is :red:`RED` it returns :green:`GREEN`

    .. code-block:: shell

      control(current_light='RED', timer_done=True ) -> 'GREEN'
      └── def control(timer_done, current_light):
          ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
          ├── if not timer_done:
          │      return current_light
          └── if timer_done:
              ├── if current_light == green:
              │       return yellow
              ├── if current_light == yellow:
              │       return red
              └── if current_light == red:
                  └── return green

* If none of the above :ref:`conditions<if statements>` are met it :ref:`returns None because ...<test_making_a_function_w_return_none>`.

  .. code-block:: shell

    def control(timer_done, current_light):
    ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
    ├── if not timer_done:
    │      return current_light
    └── if timer_done:
        ├── if current_light == green:
        │       return yellow
        ├── if current_light == yellow:
        │       return red
        ├── if current_light == red:
        │       return green

----

The :ref:`truth table` for the **Traffic Light** is

================  ===============  ================
current light     timer            output
================  ===============  ================
:green:`GREEN`    :red:`NOT done`  :green:`GREEN`
:green:`GREEN`    :green:`done`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :yellow:`YELLOW`
:yellow:`YELLOW`  :green:`done`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`RED`
:red:`RED`        :green:`done`    :green:`GREEN`
================  ===============  ================

This only shows one set of lights for traffic in one direction, which is not needed if the street has no cross traffic, it is not yet a real **Traffic Light**.

I want the ``control`` :ref:`function<what is a function?>` to show what happens in front of me (parallel) and what happens for the traffic crossing the street if the light is :red:`RED` for me, it has to consider traffic in both directions

* what traffic phase is this (cross, parallel or both)?

  - what is the light for me (parallel)?
  - what is the light for them (cross)?
* is the timer done?

The outputs will be the lights for Parallel and Cross Traffic which gives me this :ref:`truth table`. The **Traffic Light** has to make sure that there is never a case where cars move through the intersection at the same time to avoid accidents. The following cases must never happen

================  ================
parallel          cross
================  ================
:green:`GREEN`    :green:`GREEN`
:green:`GREEN`    :yellow:`YELLOW`
:yellow:`YELLOW`  :yellow:`YELLOW`
:yellow:`YELLOW`  :green:`GREEN`
================  ================

That leaves me with this :ref:`truth table`

================  ================  =============== =================== =================
current           current                           next                next
parallel          cross             timer           parallel            cross
================  ================  =============== =================== =================
:green:`GREEN`    :red:`RED`        :red:`NOT done` :green:`GREEN`      :red:`RED`
:green:`GREEN`    :red:`RED`        :green:`done`   :yellow:`YELLOW`    :red:`RED`
:yellow:`YELLOW`  :red:`RED`        :red:`NOT done` :yellow:`YELLOW`    :red:`RED`
:yellow:`YELLOW`  :red:`RED`        :green:`done`   :red:`RED`          :red:`RED`
:red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
:red:`RED`        :red:`RED`        :green:`done`   :red:`RED`          :green:`GREEN`
================  ================  =============== =================== =================

================  ================  =============== =================== =================
current           current                           next                next
parallel          cross             timer           parallel            cross
================  ================  =============== =================== =================
:red:`RED`        :green:`GREEN`    :red:`NOT done` :red:`RED`          :green:`GREEN`
:red:`RED`        :green:`GREEN`    :green:`done`   :red:`RED`          :yellow:`YELLOW`
:red:`RED`        :yellow:`YELLOW`  :red:`NOT done` :red:`RED`          :yellow:`YELLOW`
:red:`RED`        :yellow:`YELLOW`  :green:`done`   :red:`RED`          :red:`RED`
:red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
:red:`RED`        :red:`RED`        :green:`done`   :green:`GREEN`      :red:`RED`
================  ================  =============== =================== =================

Where ``parallel`` is the light in front of me, and ``cross`` is the light for traffic crossing the street. The all :red:`RED` row (Safety State) makes sure that there are no cars moving through the intersection at the same time to avoid accidents

----

*********************************************************************************
test_cross_red_parallel_red_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :red:`RED` AND the current cross light is :red:`RED` AND the timer is :green:`done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :red:`RED`        :green:`done`   :green:`GREEN`      :red:`RED`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_cross_red_parallel_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=True,
                ),
                (GREEN, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got
               an unexpected keyword argument 'current_parallel'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``current_parallel`` to the :ref:`function definition<how to make a function that takes input>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def control(timer_done, current_light, current_parallel):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_cross_red_parallel_red_timer_done -
        TypeError: control() got an
            unexpected keyword argument 'current_cross'
    FAILED ...test_green_light_timer_done -
        TypeError: control() missing
            1 required positional argument: 'current_parallel'
    FAILED ...test_green_light_timer_not_done -
        TypeError: control() missing
            1 required positional argument: 'current_parallel'
    FAILED ...test_red_light_timer_done -
         ypeError: control() missing
            1 required positional argument: 'current_parallel'
    FAILED ...test_red_light_timer_not_done -
         TypeError: control() missing
            1 required positional argument: 'current_parallel'
    FAILED ...test_yellow_light_timer_done -
        TypeError: control() missing
            1 required positional argument: 'current_parallel'
    FAILED ...test_yellow_light_timer_not_done -
         TypeError: control() missing
            1 required positional argument: 'current_parallel'

* I add a :ref:`default value<test_optional_arguments>` for the ``current_parallel`` parameter

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def control(
            timer_done, current_light,
            current_parallel='RED',
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got
               an unexpected keyword argument 'current_cross'

* I add ``current_cross`` to the :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def control(
            timer_done, current_light,
            current_parallel='RED', current_cross='RED',
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

     TypeError: control() missing
                1 required positional argument: 'current_light'

* I add a :ref:`default value<test_optional_arguments>` for ``current_light`` to the :ref:`function signature<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(
            timer_done, current_light='RED,
            current_parallel='RED', current_cross='RED',
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'RED')

* I add an :ref:`if statement<if statements>` to ``if timer_done:`` for if the current parallel light is :red:`RED` AND the current cross light is :red:`RED`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 8-9

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green
            if current_parallel == red and current_cross == red:
                return green, red

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` because the :ref:`function<what is a function?>` returns :red:`RED` if the timer is :green:`done` AND ``current_light`` is :red:`RED` and the :ref:`default value<test_optional_arguments>` for ``current_light`` in this :ref:`assertion<what is an assertion?>` is :red:`RED`.

* I change the :ref:`default value` for ``current_light`` to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def control(
            timer_done, current_light=None,
            current_parallel='RED', current_cross='RED',
        ):

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED' , current_cross='RED',
        timer_done=True
    ) -> 'GREEN', 'RED'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_cross_red_parallel_red_timer_done'

----

*********************************************************************************
test_cross_red_parallel_red_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :red:`RED` AND the current cross light is :red:`RED` AND the timer is :red:`NOT done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_cross_red_parallel_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=False,
                ),
                (RED, RED)
            )

        def test_cross_red_parallel_red_timer_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'RED')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :red:`RED` to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3

        if not timer_done:
            if current_parallel == red and current_cross == red:
                return red, red
            return current_light
        if timer_done:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_green_light_timer_not_done -
        AssertionError: ('RED', 'RED') != 'GREEN'
    FAILED ...test_red_light_timer_not_done -
        AssertionError: ('RED', 'RED') != 'RED'
    FAILED ...test_yellow_light_timer_not_done -
        AssertionError: ('RED', 'RED') != 'YELLOW'

  because those :ref:`assertions<what is an assertion?>` use the :ref:`default values<test_optional_arguments>` for ``current_parallel`` and ``cross_parallel``

* I add an :ref:`if statements` for if the timer is :red:`NOT done` and the ``current_light`` is :ref:`grouped as True<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2-3

        if not timer_done:
            if current_light:
                return current_light
            if current_parallel == red and current_cross == red:
                return red, red
            # return current_light
        if timer_done:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED' , current_cross='RED',
        timer_done=False
    ) -> 'RED', 'RED'
    control(
        current_parallel='RED' , current_cross='RED',
        timer_done=True
    ) -> 'GREEN', 'RED'

* I remove the commented line

  .. code-block:: python
    :lineno-start: 6

        if not timer_done:
            if current_light:
                return current_light
            if current_parallel == red and current_cross == red:
                return red, red

        if timer_done:

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_cross_red_parallel_red_timer_not_done'

----

*********************************************************************************
test_cross_yellow_parallel_red_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :red:`RED` AND the current cross light is :yellow:`YELLOW` AND the timer is :green:`done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :yellow:`YELLOW`  :green:`done`   :red:`RED`          :red:`RED`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_cross_yellow_parallel_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=YELLOW,
                    timer_done=True,
                ),
                (RED, RED)
            )

        def test_cross_red_parallel_red_timer_not_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'RED')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :yellow:`YELLOW` to ``if timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 12
  :emphasize-lines: 8-9

      if timer_done:
          if current_light == green:
              return yellow
          if current_light == yellow:
              return red
          if current_light == red:
              return green
          if current_parallel == red and current_cross == yellow:
              return red, red
          if current_parallel == red and current_cross == red:
              return green, red

the test passes.

.. code-block:: python

  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=True
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=False
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=True
  ) -> 'GREEN', 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* Two of the :ref:`if statements` in ``if timer_done:`` are for if the current parallel light is :red:`RED`. I change them to remove repetition of ``if current_parallel == red``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 8-16

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green
            # if current_parallel == red and current_cross == yellow:
            #     return red, red
            # if current_parallel == red and current_cross == red:
            #     return green, red
            if current_parallel == red:
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

  the tests are still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 12

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if current_parallel == red:
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_cross_yellow_parallel_red_timer_done'

----

*********************************************************************************
test_cross_yellow_parallel_red_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :red:`RED` AND the current cross light is :yellow:`YELLOW` AND the timer is :red:`NOT done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :yellow:`YELLOW`  :red:`NOT done` :red:`RED`          :yellow:`YELLOW`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_cross_yellow_parallel_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=YELLOW,
                    timer_done=False,
                ),
                (RED, YELLOW)
            )

        def test_cross_yellow_parallel_red_timer_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'YELLOW')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :yellow:`YELLOW` to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 4-5

      if not timer_done:
          if current_light:
              return current_light
          if current_parallel == red and current_cross == yellow:
              return red, yellow
          if current_parallel == red and current_cross == red:
              return red, red

      if timer_done:

the test passes.

.. code-block:: python

  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=False
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=True
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=False
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=True
  ) -> 'GREEN', 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* Two of the :ref:`if statements` in ``if not timer_done:`` are also for if the current parallel light is :red:`RED`. I change them to remove repetition of ``if current_parallel == red``

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 3-12

        if not timer_done:
            if current_light:
                return current_light
            # if current_parallel == red and current_cross == yellow:
            #     return red, yellow
            # if current_parallel == red and current_cross == red:
            #     return red, red
            if current_parallel == red:
                if current_cross == yellow:
                    return red, yellow
                if current_cross == red:
                    return red, red

        if timer_done:

  the tests are still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 6

        if not timer_done:
            if current_light:
                return current_light

            if current_parallel == red:
                if current_cross == yellow:
                    return red, yellow
                if current_cross == red:
                    return red, red

        if timer_done:

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_cross_yellow_parallel_red_timer_not_done'

----

*********************************************************************************
test_cross_green_parallel_red_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :red:`RED` AND the current cross light is :green:`GREEN` AND the timer is :green:`done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :green:`GREEN`    :green:`done`   :red:`RED`          :yellow:`YELLOW`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_cross_green_parallel_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=GREEN,
                    timer_done=True,
                ),
                (RED, YELLOW)
            )

        def test_cross_yellow_parallel_red_timer_not_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'YELLOW')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :green:`GREEN` to ``if timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 10-11

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if current_parallel == red:
                if current_cross == green:
                    return red, yellow
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

the test passes.

.. code-block:: python

  control(
      current_parallel='RED' , current_cross='GREEN',
      timer_done=True
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=False
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=True
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=False
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=True
  ) -> 'GREEN', 'RED'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_cross_green_parallel_red_timer_done'

----

*********************************************************************************
test_cross_green_parallel_red_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :red:`RED` AND the current cross light is :green:`GREEN` AND the timer is :red:`NOT done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :green:`GREEN`    :red:`NOT done` :red:`RED`          :green:`GREEN`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_cross_green_parallel_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=GREEN,
                    timer_done=False,
                ),
                (RED, GREEN)
            )

        def test_cross_green_parallel_red_timer_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'GREEN')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :green:`GREEN` to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 6-7

      if not timer_done:
          if current_light:
              return current_light

          if current_parallel == red:
              if current_cross == green:
                  return red, green
              if current_cross == yellow:
                  return red, yellow
              if current_cross == red:
                  return red, red

      if timer_done:

the test passes.

.. code-block:: python

  control(
      current_parallel='RED' , current_cross='GREEN',
      timer_done=False
  ) -> 'RED', 'GREEN'
  control(
      current_parallel='RED' , current_cross='GREEN',
      timer_done=True
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=False
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_cross='YELLOW',
      timer_done=True
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=False
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=True
  ) -> 'GREEN', 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* The three :ref:`if statements` in ``if not timer_done:`` for if the current parallel light is :red:`RED` all return the current parallel light and the current cross light. I write one :ref:`return statement<the return statement>` for all of them

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        if not timer_done:
            if current_light:
                return current_light

            if current_parallel == red:
                return current_parallel, current_cross
                if current_cross == green:
                    return red, green
                if current_cross == yellow:
                    return red, yellow
                if current_cross == red:
                    return red, red

        if timer_done:

  the tests are still green.

* I remove the :ref:`if statements` for the other cases since they are no longer used

  .. code-block:: python
    :lineno-start: 6

        if not timer_done:
            if current_light:
                return current_light

            if current_parallel == red:
                return current_parallel, current_cross

        if timer_done:

  still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_cross_green_parallel_red_timer_not_done'

----

*********************************************************************************
test_parallel_red_cross_red_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_not_done` for if the current parallel light is :red:`RED` AND the current cross light is :red:`RED` AND the timer is :green:`done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :red:`RED`        :green:`done`   :red:`RED`          :green:`GREEN`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 4-5, 7, 9-10

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=True,
                    # current_light=RED,
                ),
                # GREEN
                (RED, GREEN)
            )

        def test_cross_green_parallel_red_timer_not_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('GREEN', 'RED') != ('RED', 'GREEN')

  because the ``control`` :ref:`function<what is a function?>` cannot tell the difference between

  - if the current parallel light is :red:`RED` AND the cross light is :red:`RED` AND the timer is :green:`done` which returns the next parallel light as :green:`GREEN` and the next cross light as :red:`RED`, and
  - if the current parallel light is :red:`RED` AND the cross light is :red:`RED` AND the timer is :green:`done` which gives returns the next parallel light as :red:`RED` and the next cross light as :green:`GREEN`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :red:`RED`        :green:`done`   :green:`GREEN`      :red:`RED`
  :red:`RED`        :red:`RED`        :green:`done`   :red:`RED`          :green:`GREEN`
  ================  ================  =============== =================== =================

  I need a way for the :ref:`function<what is a function?>` to know the difference. When I look at the overall table I see that the phases that come right before these two states are the safety state which is also the same for both

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
  :red:`RED`        :red:`RED`        :green:`done`   :green:`GREEN`      :red:`RED`
  :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
  :red:`RED`        :red:`RED`        :green:`done`   :red:`RED`          :green:`GREEN`
  ================  ================  =============== =================== =================

  The difference between them is in the phase before the safety phase

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :yellow:`YELLOW`  :red:`RED`        :green:`done`   :red:`RED`          :red:`RED`
  :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
  :red:`RED`        :red:`RED`        :green:`done`   :green:`GREEN`      :red:`RED`
  ================  ================  =============== =================== =================

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :yellow:`YELLOW`  :green:`done`   :red:`RED`          :red:`RED`
  :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
  :red:`RED`        :red:`RED`        :green:`done`   :red:`RED`          :green:`GREEN`
  ================  ================  =============== =================== =================

  The ``control`` :ref:`function<what is a function?>` needs to know that it is a sequence based on whether the parallel or cross traffic is in a :red:`RED` state

  - if it is in the :red:`RED` state for cross traffic AND the current parallel light is :red:`RED` AND the cross light is :red:`RED` AND the timer is :green:`done` it should keep the parallel light :red:`RED` and turn the next cross light :green:`GREEN`
  - if it is in the :red:`RED` state for parallel traffic AND the current parallel light is :red:`RED` AND the cross light is :red:`RED` AND the timer is :green:`done` it should turn the next parallel light :green:`GREEN` and keep the next cross light :red:`RED`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``red_phase`` to the :ref:`call<how to call a function with input>` ``control`` :ref:`function<what is a function?>` in the :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_done`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 4

      def test_red_light_timer_done(self):
          self.assertEqual(
              src.traffic_light.control(
                  red_phase='cross',
                  current_parallel=RED,
                  current_cross=RED,
                  timer_done=True,
                  # current_light=RED,
              ),
              # GREEN
              (RED, GREEN)
          )

      def test_cross_green_parallel_red_timer_not_done(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: control() got an
               unexpected keyword argument 'red_phase'

* I add ``red_phase`` with a :ref:`default value<test_optional_arguments>` for the other tests, to the :ref:`function definition<how to make a function that takes input>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    def control(
            timer_done, current_light=None,
            current_parallel='RED', current_cross='RED',
            red_phase='parallel',
        ):

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I add an :ref:`if statement<if statements>` to ``if timer_done:`` for if the **Traffic Light** is currently in the :red:`RED` phase for cross traffic AND the current parallel light is :red:`RED` AND the current cross light is :red:`RED`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 9-11

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if red_phase == 'cross':
                if current_parallel == red and current_cross == red:
                    return red, green

            if current_parallel == red:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED' , current_cross='RED',
        timer_done=True, red_phase='cross'
    ) -> 'RED', 'GREEN'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_red_light_timer_done` in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 55

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=True,
                ),
                (RED, GREEN)
            )

        def test_cross_green_parallel_red_timer_not_done(self):

* I change the name of the test from :ref:`test_red_light_timer_done` to :ref:`test_parallel_red_cross_red_timer_done`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 10

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=RED,
                ),
                RED
            )

        def test_parallel_red_cross_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=True,
                ),
                (RED, GREEN)
            )

        def test_cross_green_parallel_red_timer_not_done(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_red_cross_red_timer_done'

----

*********************************************************************************
test_parallel_red_cross_red_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add values for ``current_parallel``, ``current_cross`` and ``red_phase`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_not_done` for if ``'cross'`` traffic is in the :red:`RED` phase AND the current parallel light is :red:`RED` AND the current cross light is :red:`RED` AND the timer is :red:`NOT done`

  ==========  ================  ================  =============== =================== =================
  red         current           current                           next                next
  phase       parallel          cross             timer           parallel            cross
  ==========  ================  ================  =============== =================== =================
  'cross'     :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
  ==========  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-6, 8, 10-11

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=False,
                    # current_light=RED,
                ),
                # RED
                (RED, RED)
            )

        def test_parallel_red_cross_red_timer_done(self):

  the test is still green.

  .. code-block:: python

    control(
        current_parallel='RED' , current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'RED', 'RED'
    control(
        current_parallel='RED' , current_cross='RED',
        timer_done=True, red_phase='cross'
    ) -> 'RED', 'GREEN'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I remove the commented lines from :ref:`test_red_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 46

      def test_red_light_timer_not_done(self):
          self.assertEqual(
              src.traffic_light.control(
                  red_phase='cross',
                  current_parallel=RED,
                  current_cross=RED,
                  timer_done=False,
              ),
              (RED, RED)
          )

      def test_parallel_red_cross_red_timer_done(self):

* I change the name of the test from :ref:`test_red_light_timer_not_done` to :ref:`test_parallel_red_cross_red_timer_not_done`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 10

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=YELLOW,
                ),
                RED
            )

        def test_parallel_red_cross_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=False,
                ),
                (RED, RED)
            )

        def test_parallel_red_cross_red_timer_done(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_red_cross_red_timer_not_done'

----

*********************************************************************************
test_parallel_yellow_cross_red_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add values for ``current_parallel``, ``current_cross`` and ``red_phase`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_yellow_light_timer_done` for if ``'cross'`` traffic is in the :red:`RED` phase AND the current parallel light is :yellow:`YELLOW` AND the current cross light is :red:`RED` AND the timer is :green:`done`

  ==========  ================  ================  =============== =================== =================
  red         current           current                           next                next
  phase       parallel          cross             timer           parallel            cross
  ==========  ================  ================  =============== =================== =================
  'cross'     :yellow:`YELLOW`  :red:`RED`        :green:`done`   :red:`RED`          :red:`RED`
  ==========  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4-6, 8, 10-11

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=YELLOW,
                    current_cross=RED,
                    timer_done=True,
                    # current_light=YELLOW,
                ),
                # RED
                (RED, RED)
            )

        def test_parallel_red_cross_red_timer_not_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'RED')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :yellow:`YELLOW` AND the current cross light is :red:`RED` to ``if timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 13-14

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if red_phase == 'cross':
                if current_parallel == red and current_cross == red:
                    return red, green

            if current_parallel == yellow and current_cross == red:
                return red, red

            if current_parallel == red:

the test passes.

.. code-block:: python

  control(
      current_parallel='YELLOW' , current_cross='RED',
      timer_done=True, red_phase='cross'
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=False, red_phase='cross'
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=True, red_phase='cross'
  ) -> 'RED', 'GREEN'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* Two of the :ref:`if statements` in ``if timer_done:`` are for if the current cross light is :red:`RED` which is when ``cross`` traffic is in the :red:`RED` phase. I change them to remove repetition of ``if current_cross == red``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 9-18

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if red_phase == 'cross':
            #     if current_parallel == red and current_cross == red:
            #         return red, green

            # if current_parallel == yellow and current_cross == red:
            #     return red, red
                if current_parallel == yellow:
                    return red, red
                if current_parallel == red:
                    return red, green

            if current_parallel == red:

  the tests are still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if red_phase == 'cross':
                if current_parallel == yellow:
                    return red, red
                if current_parallel == red:
                    return red, green

            if current_parallel == red:

* I remove the commented lines from :ref:`test_yellow_light_timer_done`

  .. code-block:: python
    :lineno-start: 37

        def test_yellow_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=YELLOW,
                    current_cross=RED,
                    timer_done=True,
                ),
                (RED, RED)
            )

        def test_parallel_red_cross_red_timer_not_done(self):

* I change the name of the test from :ref:`test_yellow_light_timer_done` to :ref:`test_parallel_yellow_cross_red_timer_done`

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 10

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=YELLOW,
                ),
                YELLOW
            )

        def test_parallel_yellow_cross_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=YELLOW,
                    current_cross=RED,
                    timer_done=True,
                ),
                (RED, RED)
            )

        def test_parallel_red_cross_red_timer_not_done(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_yellow_cross_red_timer_done'

----

*********************************************************************************
test_parallel_yellow_cross_red_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add values for ``current_parallel``, ``current_cross`` and ``red_phase`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_yellow_light_timer_not_done` for if ``'cross'`` traffic is in the :red:`RED` phase AND the current parallel light is :yellow:`YELLOW` AND the current cross light is :red:`RED` AND the timer is :red:`NOT done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  'cross'     :yellow:`YELLOW`  :red:`RED`        :red:`NOT done` :yellow:`YELLOW`    :red:`RED`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 4-6, 8, 10-11

      def test_yellow_light_timer_not_done(self):
          self.assertEqual(
              src.traffic_light.control(
                  red_phase='cross',
                  current_parallel=YELLOW,
                  current_cross=RED,
                  timer_done=False,
                  # current_light=YELLOW,
              ),
              # YELLOW
              (YELLOW, RED)
          )

      def test_parallel_yellow_cross_red_light_timer_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('YELLOW', 'RED')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :yellow:`YELLOW` AND the current cross light is :red:`RED` to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 5-6

        if not timer_done:
            if current_light:
                return current_light

            if current_parallel == yellow and current_cross == red:
                return yellow, red
            if current_parallel == red:
                return current_parallel, current_cross

        if timer_done:

the test passes.

.. code-block:: python

  control(
      current_parallel='YELLOW' , current_cross='RED',
      timer_done=False, red_phase='cross'
  ) -> 'RED', 'RED'
  control(
      current_parallel='YELLOW' , current_cross='RED',
      timer_done=True, red_phase='cross'
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=False, red_phase='cross'
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_cross='RED',
      timer_done=True, red_phase='cross'
  ) -> 'RED', 'GREEN'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from :ref:`test_yellow_light_timer_not_done` in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 28

        def test_yellow_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=YELLOW,
                    current_cross=RED,
                    timer_done=False,
                ),
                (YELLOW, RED)
            )

        def test_parallel_yellow_cross_red_light_timer_done(self):

* I change the name of the test from :ref:`test_yellow_light_timer_not_done` to :ref:`test_parallel_yellow_cross_red_timer_not_done`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 10

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=GREEN,
                ),
                YELLOW
            )

        def test_parallel_yellow_cross_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=YELLOW,
                    current_cross=RED,
                    timer_done=False,
                ),
                (YELLOW, RED)
            )

        def test_parallel_yellow_cross_red_light_timer_done(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_yellow_cross_red_timer_not_done'

----

*********************************************************************************
test_parallel_green_cross_red_timer_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :green:`GREEN` AND the current cross light is :red:`RED` AND the timer is :green:`done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :green:`GREEN`    :green:`done`   :red:`RED`          :yellow:`YELLOW`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_parallel_green_cross_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_parallel=GREEN,
                    timer_done=True,
                ),
                (RED, YELLOW)
            )

        def test_parallel_yellow_cross_red_timer_not_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'YELLOW')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :green:`GREEN` to ``if timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 10-11

        if timer_done:
            if current_light == green:
                return yellow
            if current_light == yellow:
                return red
            if current_light == red:
                return green

            if current_parallel == red:
                if current_parallel == green:
                    return red, yellow
                if current_parallel == yellow:
                    return red, red
                if current_parallel == red:
                    return green, red

the test passes.

.. code-block:: python

  control(
      current_parallel='RED' , current_parallel='GREEN',
      timer_done=True
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_parallel='YELLOW',
      timer_done=False
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_parallel='YELLOW',
      timer_done=True
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_parallel='RED',
      timer_done=False
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_parallel='RED',
      timer_done=True
  ) -> 'GREEN', 'RED'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_green_cross_red_timer_done'

----

*********************************************************************************
test_parallel_green_cross_red_timer_not_done
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the current parallel light is :green:`GREEN` AND the current cross light is :red:`RED` AND the timer is :red:`NOT done`

  ================  ================  =============== =================== =================
  current           current                           next                next
  parallel          cross             timer           parallel            cross
  ================  ================  =============== =================== =================
  :red:`RED`        :green:`GREEN`    :red:`NOT done` :red:`RED`          :green:`GREEN`
  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10-18

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=True,
                    current_light=RED,
                ),
                GREEN
            )

        def test_parallel_green_cross_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_parallel=RED,
                    current_parallel=GREEN,
                    timer_done=False,
                ),
                (RED, GREEN)
            )

        def test_parallel_green_cross_red_timer_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('RED', 'GREEN')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :red:`RED` AND the current cross light is :green:`GREEN` to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 6-7

      if not timer_done:
          if current_light:
              return current_light

          if current_parallel == red:
              if current_parallel == green:
                  return red, green
              if current_parallel == yellow:
                  return red, yellow
              if current_parallel == red:
                  return red, red

      if timer_done:

the test passes.

.. code-block:: python

  control(
      current_parallel='RED' , current_parallel='GREEN',
      timer_done=False
  ) -> 'RED', 'GREEN'
  control(
      current_parallel='RED' , current_parallel='GREEN',
      timer_done=True
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_parallel='YELLOW',
      timer_done=False
  ) -> 'RED', 'YELLOW'
  control(
      current_parallel='RED' , current_parallel='YELLOW',
      timer_done=True
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_parallel='RED',
      timer_done=False
  ) -> 'RED', 'RED'
  control(
      current_parallel='RED' , current_parallel='RED',
      timer_done=True
  ) -> 'GREEN', 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* The three :ref:`if statements` in ``if not timer_done:`` for if the current parallel light is :red:`RED` all return the current parallel light and the current cross light. I write one :ref:`return statement<the return statement>` for all of them

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 6

        if not timer_done:
            if current_light:
                return current_light

            if current_parallel == red:
                return current_parallel, current_parallel
                if current_parallel == green:
                    return red, green
                if current_parallel == yellow:
                    return red, yellow
                if current_parallel == red:
                    return red, red

        if timer_done:

  the tests are still green.

* I remove the :ref:`if statements` for the other cases since they are no longer used

  .. code-block:: python
    :lineno-start: 6

        if not timer_done:
            if current_light:
                return current_light

            if current_parallel == red:
                return current_parallel, current_parallel

        if timer_done:

  still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_green_cross_red_timer_not_done'


####
BOOM BOOM BAP
####

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_green_light_timer_done -
        TypeError: control() missing 1
                   required positional argument: 'walk_button'
    FAILED ...test_green_light_timer_not_done -
        TypeError: control() missing 1
                   required positional argument: 'walk_button'
    FAILED ...test_red_light_timer_done -
        TypeError: control() missing 1
                   required positional argument: 'walk_button'
    FAILED ...test_red_light_timer_not_done -
        TypeError: control() missing 1
                   required positional argument: 'walk_button'
    FAILED ...test_yellow_light_timer_done -
        TypeError: control() missing 1
                   required positional argument: 'walk_button'
    FAILED ...test_yellow_light_timer_not_done -
        TypeError: control() missing 1
                   required positional argument: 'walk_button'

  because all the other :ref:`assertions<what is an assertion?>` :ref:`call<how to call a function with input>` the ``control`` :ref:`function<what is a function?>` with two arguments and I changed the :ref:`function signature<how to make a function that takes input>` to make it expect three.

* I add a :ref:`default value<test_optional_arguments>` for the ``walk_button`` parameter, to make it a choice not a requirement

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

I change :red:`RED` to :yellow:`YELLOW` in the :ref:`test_green_light_timer_done`

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

----

*********************************************************************************
test_red_light_timer_not_done_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :red:`RED` AND the timer is :red:`NOT done` is

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
================  ===============  =================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_red_light_timer_not_done` for if the current light is :red:`RED` AND the timer is :red:`NOT done` AND the walk button is :red:`NOT pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 9-16

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                ),
                RED
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW
            )

        def test_yellow_light_timer_done_walk_button(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'RED' != 'YELLOW'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :yellow:`YELLOW` to :red:`RED` in :ref:`test_red_light_timer_not_done`

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 7

          self.assertEqual(
              src.traffic_light.control(
                  current_light=RED,
                  timer_done=False,
                  walk_button=False,
              ),
              RED
          )

      def test_yellow_light_timer_done_walk_button(self):

the test passes.

.. code-block:: python

  control(
      current_light='RED', timer_done=False,
      walk_button=False
  ) -> 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a value for ``walk_button`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_not_done` for if the current light is :red:`RED` AND the timer is :red:`NOT done` and the walk button is :green:`pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 6

        def test_red_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                RED
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                RED
            )

        def test_yellow_light_timer_done_walk_button(self):

  the test is still green.

  .. code-block:: python

    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> 'RED'
    control(
        current_light='RED', timer_done=False,
        walk_button=False
    ) -> 'RED'

* I change the name of the test from :ref:`test_red_light_timer_not_done` to :ref:`test_red_light_timer_not_done_walk_button`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 10

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                ),
                GREEN
            )

        def test_red_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                RED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_red_light_timer_not_done_walk_button'

----

*********************************************************************************
test_red_light_timer_done_walk_button
*********************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :red:`RED` AND the timer is :green:`done` is

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:red:`RED`        :green:`done`    :green:`pushed`    :green:`GREEN`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for ``walk_button`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_done` for if the current light is :red:`RED` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                GREEN
            )

        def test_red_light_timer_not_done_walk_button(self):

  the test is still green.

  .. code-block:: python

    control(
        current_light='RED', timer_done=True,
        walk_button=False
    ) -> 'GREEN'
    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> 'RED'
    control(
        current_light='RED', timer_done=False,
        walk_button=False
    ) -> 'RED'

* I add an :ref:`assertion<what is an assertion?>` for if the current light is :red:`RED` AND the timer is :green:`done` AND the walk button is :green:`pushed`

  ================  ===============  =================  ================
  current light     timer            walk button        output
  ================  ===============  =================  ================
  :red:`RED`        :green:`done`    :green:`pushed`    :green:`GREEN`
  ================  ===============  =================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-9

        def test_red_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                GREEN
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                GREEN
            )

        def test_red_light_timer_not_done_walk_button(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`if statement<if statements>` for the ``walk_button`` parameter in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-17

    def control(
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

  the test passes.

  .. code-block:: python

    control(
        current_light='RED', timer_done=True,
        walk_button=True
    ) -> 'GREEN'
    control(
        current_light='RED', timer_done=True,
        walk_button=False
    ) -> 'GREEN'
    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> 'RED'
    control(
        current_light='RED', timer_done=False,
        walk_button=False
    ) -> 'RED'

* I add a :ref:`variable<what is a variable?>` for :red:`'RED'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def control(
            current_light, timer_done,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:

* I use the :ref:`variable<what is a variable?>` for :red:`'RED'` in the :ref:`if statements`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6, 12-13

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

  the test is still green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def control(
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

* I change the name of the test from :ref:`test_red_light_timer_done` to :ref:`test_red_light_timer_done_walk_button`, in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_red_light_timer_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                RED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_red_light_timer_done_walk_button'

----

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :red:`NOT done`

* If the timer is :red:`NOT done` it returns the value of ``current_light``

  .. code-block:: shell

    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> 'RED'
    └── def control(
                current_light, timer_done,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_light
                    return 'RED'
                if current_light == yellow:
                    return red
                if current_light == green:
                    return yellow
                if walk_button:
                    return red
                return green

  .. code-block:: shell

    control(
        current_light='RED', timer_done=False,
        walk_button=False
    ) -> 'RED'
    └── def control(
                current_light, timer_done,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_light
                    return 'RED'
                if current_light == yellow:
                    return red
                if current_light == green:
                    return yellow
                if walk_button:
                    return red
                return green

  .. code-block:: shell

    control(
        current_light='YELLOW', timer_done=False,
        walk_button=True
    ) -> 'YELLOW'
    └── def control(
                current_light, timer_done,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_light
                    return 'YELLOW'
                if current_light == yellow:
                    return red
                if current_light == green:
                    return yellow
                if walk_button:
                    return red
                return green

  .. code-block:: shell

    control(
        current_light='YELLOW', timer_done=False,
        walk_button=False
    ) -> 'YELLOW'
    └── def control(
                current_light, timer_done,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_light
                    return 'YELLOW'
                if current_light == yellow:
                    return red
                if current_light == green:
                    return yellow
                if walk_button:
                    return red
                return green

  .. code-block:: shell

    control(
        current_light='GREEN', timer_done=False,
        walk_button=True
    ) -> 'GREEN'
    └── def control(
                current_light, timer_done,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_light
                    return 'GREEN'
                if current_light == yellow:
                    return red
                if current_light == green:
                    return yellow
                if walk_button:
                    return red
                return green

  .. code-block:: shell

    control(
        current_light='GREEN', timer_done=False,
        walk_button=False
    ) -> 'GREEN'
    └── def control(
                current_light, timer_done,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_light
                    return 'GREEN'
                if current_light == yellow:
                    return red
                if current_light == green:
                    return yellow
                if walk_button:
                    return red
                return green

* If the timer is :green:`done` it checks the value of ``current_light``

  - If the current light is :yellow:`YELLOW` it returns :red:`RED`

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=True,
          walk_button=True
      ) -> 'RED'
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       return current_light
              └── if current_light == yellow:
                  └── return red
                  if current_light == green:
                      return yellow
                  if walk_button:
                      return red
                  return green

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=True,
          walk_button=False
      ) -> 'RED'
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       return current_light
              └── if current_light == yellow:
                  └── return red
                  if current_light == green:
                      return yellow
                  if walk_button:
                      return red
                  return green

  - If the current light is :green:`GREEN` it returns :yellow:`YELLOW`

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=True,
          walk_button=True
      ) -> 'YELLOW'
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       return current_light
              ├── if current_light == yellow:
              │       return red
              └── if current_light == green:
                  └── return yellow
                  if walk_button:
                      return red
                  return green

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=True,
          walk_button=False
      ) -> 'YELLOW'
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       return current_light
              ├── if current_light == yellow:
              │       return red
              └── if current_light == green:
                  └── return yellow
                  if walk_button:
                      return red
                  return green

  - If the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN` it checks if the walk button was :green:`pushed`

    * If the walk button was :red:`NOT pushed` it returns :green:`green`

      .. code-block:: shell

        control(
            current_light='RED', timer_done=True,
            walk_button=True
        ) -> 'RED'
        └── def control(
                    current_light, timer_done,
                    walk_button=False,
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_light
                ├── if current_light == yellow:
                │       return red
                ├── if current_light == green:
                │       return yellow
                ├── if walk_button:
                │       return red
                └── return green

    * If the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN` AND the walk button is :green:`pushed` it returns :red:`RED`

      .. code-block:: shell

        control(
            current_light='RED', timer_done=True,
            walk_button=False
        ) -> 'GREEN'
        └── def control(
                    current_light, timer_done,
                    walk_button=False,
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_light
                ├── if current_light == yellow:
                │       return red
                ├── if current_light == green:
                │       return yellow
                └── if walk_button:
                    └── return red
                    return green

The inputs for the **Traffic Light** up till now are

* what color is the light now?
* is the timer done?
* was the walk button pushed?

which gives this :ref:`truth table`

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:red:`RED`        :green:`done`    :green:`pushed`    :red:`RED`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN`
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED`
================  ===============  =================  ================

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED`
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW`
================  ===============  =================  ================

================  ===============  =================  ================
current light     timer            walk button        output
================  ===============  =================  ================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW`
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN`
================  ===============  =================  ================

I want the **Traffic Light** to show ``WALK`` when a person can cross the street or ``DONT WALK`` when a person can NOT cross the street.

----

*************************************************************************************
test_red_light_timer_done_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :red:`RED` AND the timer is :green:`done` is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:red:`RED`        :green:`done`    :green:`pushed`    :green:`GREEN` + :red:`DONT WALK`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN` + :red:`DONT WALK`
================  ===============  =================  =================================

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the expectation of the first :ref:`assertion<what is an assertion?>` to ``(RED, 'WALK')`` in :ref:`test_red_light_timer_done_walk_button` for if the current light is :red:`RED` AND the timer is :green:`done` AND the walk button is :green:`pushed`

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :red:`RED`        :green:`done`    :green:`pushed`    :green:`GREEN` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8

        def test_red_light_timer_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (GREEN, 'DONT WALK')
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
          return red, 'WALK'

      return green

the test passes.

.. code-block:: python

  control(
      current_light='RED', timer_done=True,
      walk_button=True
  ) -> ('RED', 'WALK')

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the expectation of the second :ref:`assertion<what is an assertion?>` to ``(GREEN, 'DONT WALK')`` in :ref:`test_red_light_timer_done_walk_button` for if the current light is :red:`RED` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`, in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 16

        def test_red_light_timer_done_walk_button(self):
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
                (GREEN, 'DONT WALK')
            )

        def test_red_light_timer_not_done_walk_button(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'DONT WALK')

* I add ``'DONT WALK'`` to the :ref:`return statement<the return statement>` for this case in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 19

    def control(
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
            return red, 'WALK'

        return green, 'DONT WALK'

  the test passes.

  .. code-block:: python

    control(
        current_light='RED', timer_done=True,
        walk_button=True
    ) -> ('RED', 'WALK')
    control(
        current_light='RED', timer_done=True,
        walk_button=False
    ) -> ('GREEN', 'DONT WALK')

* I change the name of the test from :ref:`test_red_light_timer_done_walk_button` to :ref:`test_red_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_red_light_timer_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_red_light_timer_done_w_walk'

----

*************************************************************************************
test_red_light_timer_not_done_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :red:`RED` AND the timer is :red:`NOT done` is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED` + :green:`WALK`
================  ===============  =================  =================================

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the expectation of the first :ref:`assertion<what is an assertion?>` to ``(RED, 'WALK')`` in :ref:`test_red_light_timer_not_done` for if the light is :red:`RED` AND the timer is :red:`NOT done` AND the walk button is :green:`pushed`

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED` + :green:`WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 8

        def test_red_light_timer_not_done_walk_button(self):
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

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for this case to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def control(
            current_light, timer_done,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            return current_light

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('RED', 'WALK') != 'RED'

  this time for the next :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_not_done_walk_button`.

  .. code-block:: python

    control(
        current_light='RED', timer_done=True,
        walk_button=True
    ) -> ('RED', 'WALK')
    control(
        current_light='RED', timer_done=True,
        walk_button=False
    ) -> ('GREEN', 'DONT WALK')
    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> ('RED', 'WALK')

* I change the expectation of the second :ref:`assertion<what is an assertion?>` to ``(RED, 'WALK')`` in :ref:`test_red_light_timer_not_done_walk_button` for if the light is :red:`RED` AND the timer is :red:`NOT done` AND the walk button is :red:`NOT pushed`,  in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED` + :green:`WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 16

        def test_red_light_timer_not_done_walk_button(self):
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

        def test_yellow_light_timer_done_walk_button(self):

  the test passes.

  .. code-block:: python

    control(
        current_light='RED', timer_done=True,
        walk_button=True
    ) -> ('RED', 'WALK')
    control(
        current_light='RED', timer_done=True,
        walk_button=False
    ) -> ('GREEN', 'DONT WALK')
    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> ('RED', 'WALK')
    control(
        current_light='RED', timer_done=False,
        walk_button=False
    ) -> ('RED', 'WALK')

* I change the name of the test from :ref:`test_red_light_timer_not_done_walk_button` to :ref:`test_red_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=True,
                    walk_button=False,
                ),
                (GREEN, 'DONT WALK')
            )

        def test_red_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_red_light_timer_not_done_w_walk'

----

*************************************************************************************
test_yellow_light_timer_done_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :yellow:`YELLOW` AND the timer is :green:`done` is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED` + :green:`WALK`
================  ===============  =================  =================================

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the expectation of the first :ref:`assertion<what is an assertion?>` to ``(RED, 'WALK')`` in :ref:`test_yellow_light_timer_done_walk_button` for if the current light is :yellow:`YELLOW` AND the timer is :green:`done` AND the walk button is :green:`pushed`

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED` + :green:`WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 8

        def test_yellow_light_timer_done_walk_button(self):
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

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`return statement<the return statement>` for ``if current_light == yellow:`` in the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

        if current_light == yellow:
            return red, 'WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('RED', 'WALK') != 'RED'

  for the second :ref:`assertion<what is an assertion?>` in :ref:`test_yellow_light_timer_done_walk_button`

  .. code-block:: python

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=True
    ) -> ('RED', 'WALK')

* I change the expectation of the second :ref:`assertion<what is an assertion?>` to ``(RED, 'WALK')`` in :ref:`test_yellow_light_timer_done_walk_button` for if the current light is :yellow:`YELLOW` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`, in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED` + :green:`WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 16

        def test_yellow_light_timer_done_walk_button(self):
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

        def test_yellow_light_timer_not_done_walk_button(self):

  the test passes.

  .. code-block:: python

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=True
    ) -> 'RED', 'WALK'
    control(
        current_light='YELLOW', timer_done=True,
        walk_button=False
    ) -> 'GREEN', 'DONT WALK'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_yellow_light_timer_done_walk_button` to :ref:`test_yellow_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=RED,
                    timer_done=False,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_yellow_light_timer_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=True,
                ),
                (RED, 'WALK')
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_yellow_light_timer_done_w_walk'

----

*************************************************************************************
test_yellow_light_timer_not_done_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :yellow:`YELLOW` AND the timer is :red:`NOT done` is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW` + :red:`DONT WALK`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW` + :red:`DONT WALK`
================  ===============  =================  =================================

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the expectation of the first :ref:`assertion<what is an assertion?>` to ``(YELLOW, 'DONT WALK')`` in :ref:`test_yellow_light_timer_not_done` for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done` AND the walk button is :green:`pushed`

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 8

        def test_yellow_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'DONT WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != ('YELLOW', 'DONT WALK')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for this case to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-5

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            if current_light == yellow:
                return current_light, 'DONT WALK'
            return current_light

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('YELLOW', 'DONT WALK') != 'YELLOW'

  for the second :ref:`assertion<what is an assertion?>` in :ref:`test_yellow_light_timer_not_done_walk_button`.

  .. code-block:: python

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=True
    ) -> 'RED', 'WALK'
    control(
        current_light='YELLOW', timer_done=True,
        walk_button=False
    ) -> 'GREEN', 'DONT WALK'
    control(
        current_light='YELLOW', timer_done=False,
        walk_button=True
    ) -> 'RED', 'WALK'

* I change the expectation of the second :ref:`assertion<what is an assertion?>` to ``(YELLOW, 'DONT WALK')`` in :ref:`test_yellow_light_timer_not_done_walk_button` for if the light is :yellow:`YELLOW` AND the timer is :red:`NOT done` AND the walk button is :red:`NOT pushed`,  in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 16

        def test_yellow_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'DONT WALK')
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'DONT WALK')
            )

        def test_green_light_timer_done_walk_button(self):

  the test passes.

  .. code-block:: python

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=True
    ) -> 'RED', 'WALK'
    control(
        current_light='YELLOW', timer_done=True,
        walk_button=False
    ) -> 'GREEN', 'DONT WALK'
    control(
        current_light='YELLOW', timer_done=False,
        walk_button=True
    ) -> 'RED', 'WALK'
    control(
        current_light='YELLOW', timer_done=False,
        walk_button=False
    ) -> 'RED', 'WALK'

* I change the name of the test from :ref:`test_yellow_light_timer_not_done_walk_button` to :ref:`test_yellow_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=True,
                    walk_button=False,
                ),
                (RED, 'WALK')
            )

        def test_yellow_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                (YELLOW, 'DONT WALK')
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_yellow_light_timer_not_done_w_walk'

----

*************************************************************************************
test_green_light_timer_done_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :green:`GREEN` AND the timer is :green:`done` is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW` + :red:`DONT WALK`
================  ===============  =================  =================================

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the expectation of the first :ref:`assertion<what is an assertion?>` to ``(YELLOW, 'DONT WALK')`` in :ref:`test_green_light_timer_done_walk_button` for if the current light is :green:`GREEN` AND the timer is :green:`done` AND the walk button is :green:`pushed`

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 8

        def test_green_light_timer_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'DONT WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'YELLOW' != ('YELLOW', 'DONT WALK')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the :ref:`return statement<the return statement>` for ``if current_light == green:`` in the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

        if current_light == green:
            return yellow, 'DONT WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('RED', 'WALK') != 'RED'

  for the second :ref:`assertion<what is an assertion?>` in :ref:`test_green_light_timer_done_walk_button`

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=True,
        walk_button=True
    ) -> ('YELLOW', 'DONT WALK')

* I change the expectation of the second :ref:`assertion<what is an assertion?>` to ``(YELLOW, 'DONT WALK')`` in :ref:`test_green_light_timer_done_walk_button` for if the current light is :green:`GREEN` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`, in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 16

        def test_green_light_timer_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'DONT WALK')
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'DONT WALK')
            )

        def test_green_light_timer_not_done_walk_button(self):

  the test passes.

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=True,
        walk_button=True
    ) -> ('YELLOW', 'DONT WALK')
    control(
        current_light='GREEN', timer_done=True,
        walk_button=False
    ) -> ('YELLOW', 'DONT WALK')

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_green_light_timer_done_walk_button` to :ref:`test_green_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                (YELLOW, 'DONT WALK')
            )

        def test_green_light_timer_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                (YELLOW, 'DONT WALK')
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_green_light_timer_done_w_walk'

----

*************************************************************************************
test_green_light_timer_not_done_w_walk
*************************************************************************************

The :ref:`truth table` for if the **Traffic Light** is :green:`GREEN` AND the timer is :red:`NOT done` is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN` + :red:`DONT WALK`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN` + :red:`DONT WALK`
================  ===============  =================  =================================

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change the expectation of the first :ref:`assertion<what is an assertion?>` to ``(YELLOW, 'DONT WALK')`` in :ref:`test_green_light_timer_not_done` for if the light is :green:`GREEN` AND the timer is :red:`NOT done` AND the walk button is :green:`pushed`

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 8

        def test_green_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'DONT WALK')
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'GREEN' != ('GREEN', 'DONT WALK')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for this case to ``if not timer_done:``, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

        if not timer_done:
            if current_light == red:
                return current_light, 'WALK'
            if current_light == yellow:
                return current_light, 'DONT WALK'
            if current_light == green:
                return current_light, 'DONT WALK'

        if current_light == yellow:
            return red, 'WALK'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: ('GREEN', 'DONT WALK') != 'GREEN'

  for the second :ref:`assertion<what is an assertion?>` in :ref:`test_green_light_timer_not_done_walk_button`.

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=True,
        walk_button=True
    ) -> ('YELLOW', 'DONT WALK')
    control(
        current_light='GREEN', timer_done=True,
        walk_button=False
    ) -> ('YELLOW', 'DONT WALK')
    control(
        current_light='GREEN', timer_done=False,
        walk_button=True
    ) -> ('GREEN', 'DONT WALK')

* I change the expectation of the second :ref:`assertion<what is an assertion?>` to ``(GREEN, 'DONT WALK')`` in :ref:`test_green_light_timer_not_done_walk_button` for if the light is :green:`GREEN` AND the timer is :red:`NOT done` AND the walk button is :red:`NOT pushed`,  in ``tests/test_traffic_light.py``

  ================  ===============  =================  =================================
  current light     timer            walk button        output
  ================  ===============  =================  =================================
  :green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN` + :red:`DONT WALK`
  ================  ===============  =================  =================================

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 16

        def test_green_light_timer_not_done_walk_button(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'DONT WALK')
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                (GREEN, 'DONT WALK')
            )


    # Exceptions seen

  the test passes.

  .. code-block:: python

    control(
        current_light='GREEN', timer_done=True,
        walk_button=True
    ) -> ('YELLOW', 'DONT WALK')
    control(
        current_light='GREEN', timer_done=True,
        walk_button=False
    ) -> ('YELLOW', 'DONT WALK')
    control(
        current_light='GREEN', timer_done=False,
        walk_button=True
    ) -> ('GREEN', 'DONT WALK')
    control(
        current_light='GREEN', timer_done=False,
        walk_button=False
    ) -> ('GREEN', 'DONT WALK')

* I change the name of the test from :ref:`test_green_light_timer_not_done_walk_button` to :ref:`test_green_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 91
    :emphasize-lines: 10

            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                (YELLOW, 'DONT WALK')
            )

        def test_green_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                (GREEN, 'DONT WALK')
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_green_light_timer_not_done_w_walk'

----

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :red:`NOT done`

* If the timer is :red:`NOT done` it checks the value of the current light

  - If the current light is :red:`RED` it returns ``('RED', 'WALK')``

    .. code-block:: shell

      control(
          current_light='RED', timer_done=False,
          walk_button=True
      ) -> ('RED', 'WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              └── if not timer_done:
                  └── if current_light == red:
                      └── return current_light, 'WALK'
                          return 'RED'        , 'WALK'
                      if current_light == yellow:
                          return current_light, 'DONT WALK'
                      if current_light == green:
                          return current_light, 'DONT WALK'
                  if current_light == yellow:
                      return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

    .. code-block:: shell

      control(
          current_light='RED', timer_done=False,
          walk_button=False
      ) -> ('RED', 'WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              └── if not timer_done:
                  └── if current_light == red:
                      └── return current_light, 'WALK'
                          return 'RED'        , 'WALK'
                      if current_light == yellow:
                          return current_light, 'DONT WALK'
                      if current_light == green:
                          return current_light, 'DONT WALK'
                  if current_light == yellow:
                      return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

  - If the current light is :yellow:`YELLOW`, it returns ``('YELLOW', 'DONT WALK')``

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=False,
          walk_button=True
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              └── if not timer_done:
                  ├── if current_light == red:
                  │       return current_light, 'WALK'
                  └── if current_light == yellow:
                      └── return current_light, 'DONT WALK'
                          return 'YELLOW'     , 'DONT WALK'
                      if current_light == green:
                          return current_light, 'DONT WALK'
                  if current_light == yellow:
                      return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=False,
          walk_button=False
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              └── if not timer_done:
                  ├── if current_light == red:
                  │       return current_light, 'WALK'
                  └── if current_light == yellow:
                      └── return current_light, 'DONT WALK'
                          return 'YELLOW'     , 'DONT WALK'
                      if current_light == green:
                          return current_light, 'DONT WALK'
                  if current_light == yellow:
                      return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                    return green, 'DONT WALK'

  - If the current light is :green:`GREEN`, it returns ``('GREEN', 'DONT WALK')

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=False,
          walk_button=True
      ) -> ('GREEN', 'DONT WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              └── if not timer_done:
                  ├── if current_light == red:
                  │       return current_light, 'WALK'
                  ├── if current_light == yellow:
                  │       return current_light, 'DONT WALK'
                  └── if current_light == green:
                      └── return current_light, 'DONT WALK'
                          return 'GREEN'      , 'DONT WALK'
                  if current_light == yellow:
                      return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=False,
          walk_button=False
      ) -> ('GREEN', 'DONT WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              └── if not timer_done:
                  ├── if current_light == red:
                  │       return current_light, 'WALK'
                  ├── if current_light == yellow:
                  │       return current_light, 'DONT WALK'
                  └── if current_light == green:
                      └── return current_light, 'DONT WALK'
                          return 'GREEN'      , 'DONT WALK'
                  if current_light == yellow:
                      return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

  - If the timer is :red:`NOT done` AND the current light is NOT :red:`RED` or :yellow:`YELLOW` or :green:`GREEN` it moves the next statement ``if current_light == yellow:``

* If the timer is :green:`done` it checks the value of ``current_light``

  - If the current light is :yellow:`YELLOW` it returns ``('RED', 'WALK')``

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=True,
          walk_button=True
      ) -> ('RED', 'WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       if current_light == red:
              │          return current_light, 'WALK'
              │       if current_light == yellow:
              │           return current_light, 'DONT WALK'
              │       if current_light == green:
              │           return current_light, 'DONT WALK'
              └── if current_light == yellow:
                  └── return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=True,
          walk_button=False
      ) -> ('RED', 'WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       if current_light == red:
              │          return current_light, 'WALK'
              │       if current_light == yellow:
              │           return current_light, 'DONT WALK'
              │       if current_light == green:
              │           return current_light, 'DONT WALK'
              └── if current_light == yellow:
                  └── return red, 'WALK'
                  if current_light == green:
                      return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

  - If the current light is :green:`GREEN` it returns ``('YELLOW', 'DONT WALK')``

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=True,
          walk_button=True
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       if current_light == red:
              │          return current_light, 'WALK'
              │       if current_light == yellow:
              │           return current_light, 'DONT WALK'
              │       if current_light == green:
              │           return current_light, 'DONT WALK'
              ├── if current_light == yellow:
              │       return red, 'WALK'
              └── if current_light == green:
                  └── return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=True,
          walk_button=False
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light, timer_done,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── if not timer_done:
              │       if current_light == red:
              │          return current_light, 'WALK'
              │       if current_light == yellow:
              │           return current_light, 'DONT WALK'
              │       if current_light == green:
              │           return current_light, 'DONT WALK'
              ├── if current_light == yellow:
              │       return red, 'WALK'
              └── if current_light == green:
                  └── return yellow, 'DONT WALK'
                  if walk_button:
                      return red, 'WALK'
                  return green, 'DONT WALK'

  - If the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN` it checks if the walk button was :green:`pushed`

    * If the walk button was :red:`NOT pushed` it returns ``('GREEN', 'DONT WALK')``

      .. code-block:: shell

        control(
            current_light='RED', timer_done=True,
            walk_button=False
        ) -> ('GREEN', 'DONT WALK')
        └── def control(
                    current_light, timer_done,
                    walk_button=False,
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       if current_light == red:
                │          return current_light, 'WALK'
                │       if current_light == yellow:
                │           return current_light, 'DONT WALK'
                │       if current_light == green:
                │           return current_light, 'DONT WALK'
                ├── if current_light == yellow:
                │       return red, 'WALK'
                ├── if current_light == green:
                │       return yellow, 'DONT WALK'
                ├── if walk_button:
                │       return red, 'WALK'
                └── return green, 'DONT WALK'

    * If the current light is NOT :yellow:`YELLOW` AND the current light is NOT :green:`GREEN` AND the walk button is :green:`pushed` it returns ``('RED', 'WALK')``

      .. code-block:: shell

        control(
            current_light='RED', timer_done=True,
            walk_button=True
        ) -> ('RED', 'WALK')
        └── def control(
                    current_light, timer_done,
                    walk_button=False,
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       if current_light == red:
                │          return current_light, 'WALK'
                │       if current_light == yellow:
                │           return current_light, 'DONT WALK'
                │       if current_light == green:
                │           return current_light, 'DONT WALK'
                ├── if current_light == yellow:
                │       return red, 'WALK'
                ├── if current_light == green:
                │       return yellow, 'DONT WALK'
                └── if walk_button:
                    └── return red, 'WALK'
                    return green, 'DONT WALK'

----

*********************************************************************************
extract more global variables
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add more :ref:`global variables<what is a variable?>` to ``tests/test_traffic_light.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-9

    import src.traffic_light
    import unittest


    RED, YELLOW, GREEN = 'RED', 'YELLOW', 'GREEN'
    DONT_WALK = 'DONT WALK'
    WALK = (RED, 'WALK')
    YELLOW_DONT_WALK = (YELLOW, DONT_WALK)
    GREEN_DONT_WALK = (GREEN, DONT_WALK)


    class TestTrafficLight(unittest.TestCase):

* I use the ``GREEN_DONT_WALK`` :ref:`global variable<what is a variable?>` for ``(GREEN, 'DONT WALK')`` in :ref:`test_green_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 104
    :emphasize-lines: 8-9, 17-18

        def test_green_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                # (GREEN, 'DONT WALK')
                GREEN_DONT_WALK
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                # (GREEN, 'DONT WALK')
                GREEN_DONT_WALK
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_green_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 104

        def test_green_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=True,
                ),
                GREEN_DONT_WALK
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=False,
                    walk_button=False,
                ),
                GREEN_DONT_WALK
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I use the ``YELLOW_DONT_WALK`` :ref:`global variable<what is a variable?>` for ``(YELLOW, 'DONT WALK')`` in :ref:`test_green_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 8-9, 17-18

        def test_green_light_timer_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                # (YELLOW, 'DONT WALK')
                YELLOW_DONT_WALK
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                # (YELLOW, 'DONT WALK')
                YELLOW_DONT_WALK
            )

        def test_green_light_timer_not_done_w_walk(self):

  still green.

* I remove the commented lines from :ref:`test_green_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 86

        def test_green_light_timer_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=True,
                ),
                YELLOW_DONT_WALK
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=GREEN,
                    timer_done=True,
                    walk_button=False,
                ),
                YELLOW_DONT_WALK
            )

        def test_green_light_timer_not_done_w_walk(self):

* I use the ``YELLOW_DONT_WALK`` :ref:`global variable<what is a variable?>` for ``(YELLOW, 'DONT WALK')`` in :ref:`test_yellow_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 8-9, 17-18

        def test_yellow_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                # (YELLOW, 'DONT WALK')
                YELLOW_DONT_WALK
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                # (YELLOW, 'DONT WALK')
                YELLOW_DONT_WALK
            )

        def test_green_light_timer_done_w_walk(self):

  green.

* I remove the commented lines from :ref:`test_yellow_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 68

        def test_yellow_light_timer_not_done_w_walk(self):
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=True,
                ),
                YELLOW_DONT_WALK
            )
            self.assertEqual(
                src.traffic_light.control(
                    current_light=YELLOW,
                    timer_done=False,
                    walk_button=False,
                ),
                YELLOW_DONT_WALK
            )

        def test_green_light_timer_done_w_walk(self):

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` in :ref:`test_yellow_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 8-9, 17-18

        def test_yellow_light_timer_done_w_walk(self):
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

        def test_yellow_light_timer_not_done_w_walk(self):

  still green.

* I remove the commented lines from :ref:`test_yellow_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 50

        def test_yellow_light_timer_done_w_walk(self):
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

        def test_yellow_light_timer_not_done_w_walk(self):

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` in :ref:`test_red_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 8-9, 17-18

        def test_red_light_timer_not_done_w_walk(self):
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

        def test_yellow_light_timer_done_w_walk(self):

  the test is still green.

* I remove the commented lines from :ref:`test_red_light_timer_not_done_w_walk`

  .. code-block:: python
    :lineno-start: 32

        def test_red_light_timer_not_done_w_walk(self):
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

        def test_yellow_light_timer_done_w_walk(self):

* I use the ``WALK`` :ref:`global variable<what is a variable?>` for ``(RED, 'WALK')`` and ``GREEN_DONT_WALK`` :ref:`global variable<what is a variable?>` for ``(GREEN, 'DONT WALK')`` in :ref:`test_red_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-9, 17-18

        def test_red_light_timer_done_w_walk(self):
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
                # (GREEN, 'DONT WALK')
                GREEN_DONT_WALK
            )

        def test_red_light_timer_not_done_w_walk(self):

  the test is still green.

* I remove the commented lines from :ref:`test_red_light_timer_done_w_walk`

  .. code-block:: python
    :lineno-start: 14

        def test_red_light_timer_done_w_walk(self):
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
                GREEN_DONT_WALK
            )

        def test_red_light_timer_not_done_w_walk(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract more global variables'

----

*********************************************************************************
refactor control function
*********************************************************************************

* I add :ref:`variables<what is a variable?>` for ``'WALK'`` and ``'DONT WALK'`` to the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def control(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        walk = (red, 'WALK')
        dont_walk = 'DONT WALK'

        if not timer_done:

* I use the new :ref:`variables<what is a variable?>` for their values

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3-4, 6-7, 9-10, 13-14, 17-18, 21-22, 24-25

        if not timer_done:
            if current_light == red:
                # return current_light, 'WALK'
                return walk
            if current_light == yellow:
                # return current_light, 'DONT WALK'
                return current_light, dont_walk
            if current_light == green:
                # return current_light, 'DONT WALK'
                return current_light, dont_walk

        if current_light == yellow:
            # return red, 'WALK'
            return walk

        if current_light == green:
            # return yellow, 'DONT WALK'
            return yellow, dont_walk

        if walk_button:
            # return red, 'WALK'
            return walk

        # return green, 'DONT WALK'
        return green, dont_walk

  the tests are still green.

* I add a new :ref:`if statement with an else clause<if statements>` to ``if not timer done:``, that covers the 3 cases if the timer is :red:`NOT done`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-5

        if not timer_done:
            if current_light != red:
                return current_light, dont_walk
            if timer_done:
                return walk
            if current_light == red:
                # return current_light, 'WALK'
                return walk
            if current_light == yellow:
                # return current_light, 'DONT WALK'
                return current_light, dont_walk
            if current_light == green:
                # return current_light, 'DONT WALK'
                return current_light, dont_walk

  still green.

* I write out the :ref:`if statement<if statements>` for if the light is :red:`RED` AND the timer is :green:`done` with the walk button, to make it clearer

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 1, 3, 6, 8-12

        # if walk_button:
            # return red, 'WALK'
            # return walk

        # return green, 'DONT WALK'
        # return green, dont_walk

        if current_light == red:
            if not walk_button:
                return green, dont_walk
            if timer_done:
                return walk

  green.

* the ``walk`` :ref:`variable<what is a variable?>` (``'RED', 'WALK'``), happens 3 times in the :ref:`function<what is a function?>`, I add a :ref:`return statement<the return statement>` to make it the default state of the light

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7

        if current_light == red:
            if not walk_button:
                return green, dont_walk
            if timer_done:
                return walk

        return walk

  still green. This means if none of the :ref:`conditions<if statements>` in the ``control`` :ref:`function<what is a function?>` are met, the light stays :red:`RED` and shows ``'WALK'``

* I no longer need the :ref:`else clause<if statements>` for if the walk button is :green:`pushed` because it returns the default state (``'RED', 'WALK'``) if the light is :red:`RED` AND the timer is :green:`done`. I comment it out

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 4-5

        if current_light == red:
            if not walk_button:
                return green, dont_walk
            # if timer_done:
            #     return walk

        return walk

  the tests are still green.

* I use :ref:`Logical Conjunction(AND)<test_logical_conjunction>` to rewrite the :ref:`if statement<if statements>` for if the current light is :red:`red` AND the timer is :green:`done` AND the walk button is :red:`NOT pushed`

  .. code-block:: python
    :lineno-start: 39

        # if current_light == red:
        #     if not walk_button:
        if current_light == red and not walk_button:
                return green, dont_walk
            # if timer_done:
            #     return walk

        return walk

  still green.

* I no longer need the :ref:`if statement<if statements>` for :yellow:`YELLOW` because it returns the default state (``'RED', 'WALK'``) if the timer is :green:`done`. I comment it out

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 1, 3

        # if current_light == yellow:
            # return red, 'WALK'
            # return walk

        if current_light == green:
            # return yellow, 'DONT WALK'
            return yellow, dont_walk


  green. Why does this work?

* I add an :ref:`if statement<if statements>` for if the timer is :green:`done` to make it clearer

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 5, 6, 8, 19

        # if current_light == yellow:
            # return red, 'WALK'
            # return walk

        if timer_done:
            if current_light == green:
            # return yellow, 'DONT WALK'
                return yellow, dont_walk

        # if walk_button:
            # return red, 'WALK'
            # return walk

        # return green, 'DONT WALK'
        # return green, dont_walk

        # if current_light == red:
        #     if not walk_button:
            if current_light == red and not walk_button:
                return green, dont_walk
            # if timer_done:
            #     return walk

        return walk

  still green.

* I no longer need the :ref:`else clause<if statements>` for if the current light is NOT :red:`RED` AND the timer is :red:`NOT done` because it returns the default state (``'RED', 'WALK'``) . I comment it out and the other :ref:`if statements` below it to make sure they are not run

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-6, 8-9, 11-12, 14

        if not timer_done:
            if current_light != red:
                return current_light, dont_walk
            # if timer_done:
            #     return walk
            # if current_light == red:
                # return current_light, 'WALK'
                # return walk
            # if current_light == yellow:
                # return current_light, 'DONT WALK'
                # return current_light, dont_walk
            # if current_light == green:
                # return current_light, 'DONT WALK'
                # return current_light, dont_walk

        # if current_light == yellow:

  the tests are still green.

* I use  :ref:`Logical Conjunction(AND)<test_logical_conjunction>` to change the :ref:`if statement<if statements>` for if the current light is NOT :red:`red` AND the timer is :red:`NOT done`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-4

        # if not timer_done:
            # if current_light != red:
        if not timer_done and current_light != red:
            return current_light, dont_walk
            # if timer_done:

  still green.

* I no longer need the ``walk`` :ref:`variable<what is a variable?>` since it is only used once for the default state (``'RED', 'WALK'``)

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        # walk = (red, 'WALK')
        dont_walk = 'DONT WALK'


  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 1-2

        # return walk
        return red, 'WALK'

  green.

* I add :ref:`default values<test_optional_arguments>` for the ``current_light`` and ``timer_done`` parameters

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def control(
            # current_light, timer_done,
            current_light='RED', timer_done=False,
            walk_button=False,
        ):

  still green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def control(
            current_light='RED', timer_done=False,
            walk_button=False,
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        dont_walk = 'DONT WALK'

        if not timer_done and current_light != red:
            return current_light, dont_walk

        if timer_done:
            if current_light == green:
                return yellow, dont_walk
            if current_light == red and not walk_button:
                return green, dont_walk

        return red, 'WALK'

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'refactor control function'

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* If the timer is :red:`NOT done` AND if the current light is NOT :red:`RED`

  * If the timer is :red:`NOT done` AND if the current light is NOT :red:`RED`, it returns the value of ``current_light`` AND ``DONT WALK``

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=False,
          walk_button=True
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light='RED', timer_done=False,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── dont_walk = 'DONT WALK'
              └── if not timer_done and current_light != red:
                  └── return current_light, dont_walk
                      return 'YELLOW'     , 'DONT WALK'
                  if timer_done:
                      if current_light == green:
                          return yellow, dont_walk
                      if current_light == red and not walk_button:
                          return green, dont_walk
                  return red, 'WALK'

    .. code-block:: shell

      control(
          current_light='YELLOW', timer_done=False,
          walk_button=False
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light='RED', timer_done=False,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── dont_walk = 'DONT WALK'
              └── if not timer_done and current_light != red:
                  └── return current_light, dont_walk
                      return 'YELLOW'     , 'DONT WALK'
                  if timer_done:
                      if current_light == green:
                          return yellow, dont_walk
                      if current_light == red and not walk_button:
                          return green, dont_walk
                  return red, 'WALK'

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=False,
          walk_button=True
      ) -> ('GREEN', 'DONT WALK')
      └── def control(
                  current_light='RED', timer_done=False,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── dont_walk = 'DONT WALK'
              └── if not timer_done and current_light != red:
                  └── return current_light, dont_walk
                      return 'GREEN'      , 'DONT WALK'
                  if timer_done:
                      if current_light == green:
                          return yellow, dont_walk
                      if current_light == red and not walk_button:
                          return green, dont_walk
                  return red, 'WALK'

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=False,
          walk_button=False
      ) -> ('GREEN', 'DONT WALK')
      └── def control(
                  current_light='RED', timer_done=False,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── dont_walk = 'DONT WALK'
              └── if not timer_done and current_light != red:
                  └── return current_light, dont_walk
                      return 'GREEN'      , 'DONT WALK'
                  if timer_done:
                      if current_light == green:
                          return yellow, dont_walk
                      if current_light == red and not walk_button:
                          return green, dont_walk
                  return red, 'WALK'

* If the timer is :green:`done` it checks if the current light is :green:`GREEN`

  - If the timer is :green:`done` AND the current light is :green:`GREEN`, it returns ``('YELLOW', 'DONT WALK')``

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=True,
          walk_button=True
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light='RED', timer_done=False,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── dont_walk = 'DONT WALK'
              ├── if not timer_done and current_light != red:
              │       return current_light, dont_walk
              └── if timer_done:
                  └── if current_light == green:
                      └── return yellow, dont_walk
                      if current_light == red and not walk_button:
                          return green, dont_walk
                  return red, 'WALK'

    .. code-block:: shell

      control(
          current_light='GREEN', timer_done=True,
          walk_button=False
      ) -> ('YELLOW', 'DONT WALK')
      └── def control(
                  current_light='RED', timer_done=False,
                  walk_button=False,
              ):
              ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
              ├── dont_walk = 'DONT WALK'
              ├── if not timer_done and current_light != red:
              │       return current_light, dont_walk
              └── if timer_done:
                  └── if current_light == green:
                      └── return yellow, dont_walk
                      if current_light == red and not walk_button:
                          return green, dont_walk
                  return red, 'WALK'

  - If the timer is :green:`done` AND the current light is NOT :green:`GREEN`, it checks if the current light is :red:`RED` AND if the walk button is :red:`NOT pushed`

    * If the timer is :green:`done` AND the current light is :red:`RED` AND the walk button is :red:`NOT pushed`, it returns ``('GREEN', 'DONT WALK')``

      .. code-block:: shell

        control(
            current_light='RED', timer_done=True,
            walk_button=False
        ) -> ('GREEN', 'DONT WALK')
        └── def control(
                    current_light='RED', timer_done=False,
                    walk_button=False,
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── dont_walk = 'DONT WALK'
                ├── if not timer_done and current_light != red:
                │       return current_light, dont_walk
                └── if timer_done:
                    ├── if current_light == green:
                    │       return yellow, dont_walk
                    └── if current_light == red and not walk_button:
                        └── return green, dont_walk
                    return red, 'WALK'

* If none of the above :ref:`conditions<if statements>` are met, it returns ``'RED', 'WALK'``

  .. code-block:: shell

    control(
        current_light='RED', timer_done=False,
        walk_button=True
    ) -> ('RED', 'WALK')
    └── def control(
                current_light='RED', timer_done=False,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            ├── dont_walk = 'DONT WALK'
            ├── if not timer_done and current_light != red:
            │       return current_light, dont_walk
            ├── if timer_done:
            │       if current_light == green:
            │           return yellow, dont_walk
            │       if current_light == red and not walk_button:
            │           return green, dont_walk
            └── return red, 'WALK'

  .. code-block:: shell

    control(
        current_light='RED', timer_done=False,
        walk_button=False
    ) -> ('RED', 'WALK')
    └── def control(
                current_light='RED', timer_done=False,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            ├── dont_walk = 'DONT WALK'
            ├── if not timer_done and current_light != red:
            │       return current_light, dont_walk
            ├── if timer_done:
            │       if current_light == green:
            │           return yellow, dont_walk
            │       if current_light == red and not walk_button:
            │           return green, dont_walk
            └── return red, 'WALK'

  .. code-block:: shell

    control(
        current_light='RED', timer_done=True,
        walk_button=True
    ) -> ('RED', 'WALK')
    └── def control(
                current_light='RED', timer_done=False,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            ├── dont_walk = 'DONT WALK'
            ├── if not timer_done and current_light != red:
            │       return current_light, dont_walk
            └── if timer_done:
                ├── if current_light == green:
                │       return yellow, dont_walk
            ┌───┴── if current_light == red and not walk_button:
            │           return green, dont_walk
            └── return red, 'WALK'

  .. code-block:: shell

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=True
    ) -> ('RED', 'WALK')
    └── def control(
                current_light='RED', timer_done=False,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            ├── dont_walk = 'DONT WALK'
            ├── if not timer_done and current_light != red:
            │       return current_light, dont_walk
            └── if timer_done:
                ├── if current_light == green:
                │       return yellow, dont_walk
            ┌───┴── if current_light == red and not walk_button:
            │           return green, dont_walk
            └── return red, 'WALK'

  .. code-block:: shell

    control(
        current_light='YELLOW', timer_done=True,
        walk_button=False
    ) -> ('RED', 'WALK')
    └── def control(
                current_light='RED', timer_done=False,
                walk_button=False,
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            ├── dont_walk = 'DONT WALK'
            ├── if not timer_done and current_light != red:
            │       return current_light, dont_walk
            └── if timer_done:
                ├── if current_light == green:
                │       return yellow, dont_walk
            ┌───┴── if current_light == red and not walk_button:
            │           return green, dont_walk
            └── return red, 'WALK'

There is a problem with the :ref:`if statement<if statements>` of the ``control`` :ref:`function<what is a function?>` for if the timer is :green:`done` AND the current light is NOT :red:`RED`

.. code-block:: python

  if not timer_done and current_light != red:
      return current_light, dont_walk

What does it return if I :ref:`call<how to call a function with input>` it with a color that is NOT :red:`RED`, :yellow:`YELLOW` or :green:`GREEN`. There is one way to find out ...

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

I ran tests for a **Traffic Light** that has a timer and a button for people to push when they want to :green:`WALK`. If the inputs are

* what color is the light now?
* is the timer done?
* did the person push the walk button?

then the :ref:`truth table` for the **Traffic Light** is

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:red:`RED`        :green:`done`    :green:`pushed`    :green:`GREEN` + :red:`DONT WALK`
:red:`RED`        :green:`done`    :red:`NOT pushed`  :green:`GREEN` + :red:`DONT WALK`
:red:`RED`        :red:`NOT done`  :green:`pushed`    :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done`  :red:`NOT pushed`  :red:`RED` + :green:`WALK`
================  ===============  =================  =================================

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:yellow:`YELLOW`  :green:`done`    :green:`pushed`    :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`    :red:`NOT pushed`  :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :red:`NOT done`  :green:`pushed`    :yellow:`YELLOW` + :red:`DONT WALK`
:yellow:`YELLOW`  :red:`NOT done`  :red:`NOT pushed`  :yellow:`YELLOW` + :red:`DONT WALK`
================  ===============  =================  =================================

================  ===============  =================  =================================
current light     timer            walk button        output
================  ===============  =================  =================================
:green:`GREEN`    :green:`done`    :green:`pushed`    :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :green:`done`    :red:`NOT pushed`  :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :red:`NOT done`  :green:`pushed`    :green:`GREEN` + :red:`DONT WALK`
:green:`GREEN`    :red:`NOT done`  :red:`NOT pushed`  :green:`GREEN` + :red:`DONT WALK`
================  ===============  =================  =================================

It only shows ``'WALK'`` if the light is :red:`RED`.

What if the **Traffic Light** changes based on if there is an emergency vehicle? The inputs would be

* what color is the light now?
* is the timer done?
* did the person push the walk button?
* is there an emergency vehicle?

and the :ref:`truth table` would be

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:red:`RED`        :green:`done`   :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:red:`RED`        :green:`done`   :green:`pushed`   :red:`NOT emergency`  :green:`GREEN` + :red:`DONT WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:red:`RED`        :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :green:`GREEN` + :red:`DONT WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:red:`RED`        :red:`NOT done` :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:red:`RED`        :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :red:`RED` + :green:`WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:red:`RED`        :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :red:`RED` + :green:`WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:yellow:`YELLOW`  :green:`done`   :green:`pushed`   :red:`NOT emergency`  :red:`RED` + :green:`WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:yellow:`YELLOW`  :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :red:`RED` + :green:`WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:yellow:`YELLOW`  :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :yellow:`YELLOW` + :red:`DONT WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :red:`RED` + :red:`DONT WALK`
:yellow:`YELLOW`  :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :yellow:`YELLOW` + :red:`DONT WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:green:`GREEN`    :green:`done`   :green:`pushed`   :green:`emergency`    :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :green:`done`   :green:`pushed`   :red:`NOT emergency`  :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :green:`emergency`    :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :green:`done`   :red:`NOT pushed` :red:`NOT emergency`  :yellow:`YELLOW` + :red:`DONT WALK`
================  =============== ================= ====================  =================================

================  =============== ================= ====================  =================================
current light     timer           walk button       emergency             output
================  =============== ================= ====================  =================================
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :green:`emergency`    :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :red:`NOT done` :green:`pushed`   :red:`NOT emergency`  :green:`GREEN` + :red:`DONT WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :green:`emergency`    :yellow:`YELLOW` + :red:`DONT WALK`
:green:`GREEN`    :red:`NOT done` :red:`NOT pushed` :red:`NOT emergency`  :green:`GREEN` + :red:`DONT WALK`
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