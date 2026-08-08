.. meta::
  :description: Build a two-direction **Traffic Light** controller with Python TDD (Red-Green-Refactor). Start from a single light and timer truth table (GREEN/YELLOW/RED stay-or-advance), then grow to parallel and cross lights with a ``red_phase`` of ``'cross'`` or ``'parallel'``, hold-on-timer-not-done behavior, and an all-RED failsafe for invalid or unsafe color pairs (for example GREEN+GREEN or junk like ``'BAP'``/``'POW'``). Debug NameError, AttributeError, TypeError (unexpected keyword argument), and AssertionError while extracting helpers ``is_not_safe``, ``is_not_light``, ``triggers_failsafe``, and ``next_light``, plus module-level color constants and optional ``red_phase`` defaults. Jacob Itegboje, Pumping Python — uv project setup, pytest-watcher, unittest ``assertEqual``.
  :keywords: Jacob Itegboje, Pumping Python, Traffic Light TDD, red_phase cross parallel, timer_done, next_light, triggers_failsafe, is_not_safe, is_not_light, failsafe RED RED, truth table project, Red Green Refactor, function default arguments, TypeError unexpected keyword argument, AttributeError module has no attribute control, NameError src not defined, AssertionError tuples differ, unittest assertEqual, uv makePythonTdd, pytest-watcher, sequential state machine Python

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
  :lines: 1-30

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 32
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 32-52

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 54
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 54-74

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 76
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 76-96

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 98
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 98-118

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 120
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 120-140

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 142
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 142-160

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 161
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 161-178

.. literalinclude:: ../../code/traffic_light/test_traffic_light.py
  :language: python
  :lineno-start: 179
  :caption: traffic_light/tests/test_traffic_light.py
  :lines: 179-

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

    tests/test_traffic_light.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_traffic_light.py::TestTrafficLight::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_traffic_light.py:7`` to open it
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

    git commit -am 'refactor if statements'

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

The **Traffic Light** has to make sure that there is never a case where cars move through the intersection at the same time to avoid accidents. The following cases must never happen

================  ================
parallel          cross
================  ================
:green:`GREEN`    :green:`GREEN`
:green:`GREEN`    :yellow:`YELLOW`
:yellow:`YELLOW`  :yellow:`YELLOW`
:yellow:`YELLOW`  :green:`GREEN`
================  ================

The outputs will be the lights for Parallel and Cross Traffic which gives me this :ref:`truth table`

================  ================  =============== =================== =================
current           current                           next                next
parallel          cross             timer           parallel            cross
================  ================  =============== =================== =================
:green:`GREEN`    :red:`RED`        :red:`NOT done` :green:`GREEN`      :red:`RED`
:green:`GREEN`    :red:`RED`        :green:`done`   :yellow:`YELLOW`    :red:`RED`
:yellow:`YELLOW`  :red:`RED`        :red:`NOT done` :yellow:`YELLOW`    :red:`RED`
:yellow:`YELLOW`  :red:`RED`        :green:`done`   safety :red:`RED`   safety :red:`RED`
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
:red:`RED`        :yellow:`YELLOW`  :green:`done`   safety :red:`RED`   safety :red:`RED`
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

* I change the :ref:`default value<test_optional_arguments>` for ``current_light`` to :ref:`None<what is None?>`

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
* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_red_light_timer_done` for if the current parallel light is :red:`RED` AND the current cross light is :red:`RED` AND the timer is :green:`done`

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
  - if the current parallel light is :red:`RED` AND the cross light is :red:`RED` AND the timer is :green:`done` which returns the next parallel light as :red:`RED` and the next cross light as :green:`GREEN`
  - the current lights are the same in both cases but the output is different

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

        def test_parallel_yellow_cross_red_timer_done(self):
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

  ==========  ================  ================  =============== =================== =================
  red         current           current                           next                next
  phase       parallel          cross             timer           parallel            cross
  ==========  ================  ================  =============== =================== =================
  'cross'     :yellow:`YELLOW`  :red:`RED`        :red:`NOT done` :yellow:`YELLOW`    :red:`RED`
  ==========  ================  ================  =============== =================== =================

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

      def test_parallel_yellow_cross_red_timer_done(self):

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
  ) -> 'YELLOW', 'RED'
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

        def test_parallel_yellow_cross_red_timer_done(self):

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

        def test_parallel_yellow_cross_red_timer_done(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_parallel_yellow_cross_red_timer_not_done'

----

*********************************************************************************
test_parallel_green_cross_red_timer_done
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add values for ``current_parallel``, ``current_cross`` and ``red_phase`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_green_light_timer_done` for if ``'cross'`` traffic is in the :red:`RED` phase AND the current parallel light is :green:`GREEN` AND the current cross light is :red:`RED` AND the timer is :green:`done`

  ==========  ================  ================  =============== =================== =================
  red         current           current                           next                next
  phase       parallel          cross             timer           parallel            cross
  ==========  ================  ================  =============== =================== =================
  'cross'     :green:`GREEN`    :red:`RED`        :green:`done`   :yellow:`YELLOW`    :red:`RED`
  ==========  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-6, 8, 10-11

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=GREEN,
                    current_cross=RED,
                    timer_done=True,
                    # current_light=GREEN,
                ),
                # YELLOW
                (YELLOW, RED)
            )

        def test_parallel_yellow_cross_red_timer_not_done(self):

  the test is still green.

  .. code-block:: python

    control(
        current_parallel='GREEN' , current_cross='RED',
        timer_done=True, red_phase='cross'
    ) -> 'YELLOW', 'RED'
    control(
        current_parallel='YELLOW' , current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'YELLOW', 'RED'
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

* I remove the commented lines from :ref:`test_green_light_timer_done`

  .. code-block:: python
    :lineno-start: 19

        def test_green_light_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=GREEN,
                    current_cross=RED,
                    timer_done=True,
                ),
                (YELLOW, RED)
            )

        def test_parallel_yellow_cross_red_timer_not_done(self):

* I change the name of the test from :ref:`test_green_light_timer_done` to :ref:`test_parallel_green_cross_red_timer_done`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 10

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    timer_done=False,
                    current_light=GREEN,
                ),
                GREEN
            )

        def test_parallel_green_cross_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=GREEN,
                    current_cross=RED,
                    timer_done=True,
                ),
                (YELLOW, RED)
            )

        def test_parallel_yellow_cross_red_timer_not_done(self):

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
* I add values for ``current_parallel``, ``current_cross`` and ``red_phase`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_green_light_timer_not_done` for if ``'cross'`` traffic is in the :red:`RED` phase AND the current parallel light is :green:`GREEN` AND the current cross light is :red:`RED` AND the timer is :red:`NOT done`

  ==========  ================  ================  =============== =================== =================
  red         current           current                           next                next
  phase       parallel          cross             timer           parallel            cross
  ==========  ================  ================  =============== =================== =================
  'cross'     :green:`GREEN`    :red:`RED`        :red:`NOT done` :green:`GREEN`      :red:`RED`
  ==========  ================  ================  =============== =================== =================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4-6, 8, 10-11

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=GREEN,
                    current_cross=RED,
                    timer_done=False,
                    # current_light=GREEN,
                ),
                # GREEN
                (GREEN, RED)
            )

        def test_parallel_green_cross_red_timer_done(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != ('GREEN', 'RED')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if the current parallel light is :green:`GREEN` AND the current cross light is :red:`RED` to ``if not timer_done:`` in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 5-6

      if not timer_done:
          if current_light:
              return current_light

          if current_parallel == green and current_cross == red:
              return green, red
          if current_parallel == yellow and current_cross == red:
              return yellow, red
          if current_parallel == red:
              return current_parallel, current_cross

      if timer_done:

the test passes.

.. code-block:: python

  control(
      current_parallel='GREEN' , current_cross='RED',
      timer_done=False, red_phase='cross'
  ) -> 'GREEN', 'RED'
  control(
      current_parallel='GREEN' , current_cross='RED',
      timer_done=True, red_phase='cross'
  ) -> 'YELLOW', 'RED'
  control(
      current_parallel='YELLOW' , current_cross='RED',
      timer_done=False, red_phase='cross'
  ) -> 'YELLOW', 'RED'
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

* I remove the commented lines from :ref:`test_green_light_timer_not_done`

  .. code-block:: python
    :lineno-start: 10

        def test_green_light_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=GREEN,
                    current_cross=RED,
                    timer_done=False,
                ),
                (GREEN, RED)
            )

        def test_parallel_green_cross_red_timer_done(self):

* I change the name of the test from :ref:`test_green_light_timer_not_done` to :ref:`test_parallel_green_cross_red_timer_not_done`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestTrafficLight(unittest.TestCase):

        def test_parallel_green_cross_red_timer_not_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='cross',
                    current_parallel=GREEN,
                    current_cross=RED,
                    timer_done=False,
                ),
                (GREEN, RED)
            )

* I remove the :ref:`if statements` for the ``current_light`` parameter since they are no longer used, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 7

        if not timer_done:
            if current_parallel == green and current_cross == red:
                return green, red
            if current_parallel == yellow and current_cross == red:
                return yellow, red
            if current_parallel == red:
                return current_parallel, current_cross

        if timer_done:
            if red_phase == 'cross':
                if current_parallel == green:
                    return yellow, red
                if current_parallel == yellow:
                    return red, red
                if current_parallel == red:
                    return red, green
            if current_parallel == red:
                if current_cross == green:
                    return red, yellow
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

  the tests are still green.

* I remove the ``current_light`` parameter from the parentheses of the :ref:`function definition<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        if not timer_done:

* The three :ref:`if statements` in ``if not timer_done:`` all return the current parallel light and the current cross light. I write one :ref:`return statement<the return statement>` for all of them

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 2

        if not timer_done:
            return current_parallel, current_cross
            if current_parallel == green and current_cross == red:
                return green, red
            if current_parallel == yellow and current_cross == red:
                return yellow, red
            if current_parallel == red:
                return current_parallel, current_cross

        if timer_done:

  the tests are still green.

* I change ``if current_parallel == red`` to ``if red_phase == 'parallel':`` for if the timer is :green:`done` AND the current parallel light is :red:`RED` since it is for when ``parallel`` traffic is in the :red:`RED` phase

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9

        if timer_done:
            if red_phase == 'cross':
                if current_parallel == green:
                    return yellow, red
                if current_parallel == yellow:
                    return red, red
                if current_parallel == red:
                    return red, green
            # if current_parallel == red:
            if red_phase == 'parallel':
                if current_cross == green:
                    return red, yellow
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

  green.

* I remove the :ref:`if statements` from ``if not timer_done:`` and the commented line since they are no longer used

  .. code-block:: python
    :linenos:

    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not timer_done:
            return current_parallel, current_cross

        if timer_done:
            if red_phase == 'cross':
                if current_parallel == green:
                    return yellow, red
                if current_parallel == yellow:
                    return red, red
                if current_parallel == red:
                    return red, green
            if red_phase == 'parallel':
                if current_cross == green:
                    return red, yellow
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_parallel_green_cross_red_timer_not_done'

----

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the timer is :red:`NOT done`

* If the timer is :red:`NOT done`, it returns the values of ``current_parallel`` and ``current_cross``, which means it does not change the parallel or cross lights, it keeps them the same

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='GREEN',
        timer_done=False, red_phase='parallel'
    ) -> 'RED', 'GREEN'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'          , 'GREEN'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='YELLOW',
        timer_done=False, red_phase='parallel'
    ) -> 'RED', 'YELLOW'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'YELLOW'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='RED',
        timer_done=False, red_phase='parallel'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'RED'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='GREEN', current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'GREEN', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'GREEN'         , 'RED'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='YELLOW', current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'YELLOW', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'YELLOW'        , 'RED'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'RED'
                if timer_done:

* If the timer is :green:`done`, it checks if ``cross`` traffic is in the :red:`RED` phase

  - If ``cross`` traffic is in the :red:`RED` phase, it checks the value of ``current_parallel``

    * If the current parallel light is :green:`GREEN`, it returns ``YELLOW, RED``, which means the next parallel light will be :yellow:`YELLOW` and the cross light will remain :red:`RED` because it is still in the :red:`RED` phase

      .. code-block:: shell

        control(
            current_parallel='GREEN', current_cross='RED',
            timer_done=True, red_phase='cross'
        ) -> 'YELLOW', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── if red_phase == 'cross':
                        └── if current_parallel == green:
                            └── return yellow, red
                            if current_parallel == yellow:
                                return red, red
                            if current_parallel == red:
                                return red, green
                        if red_phase == 'parallel':

    * If the current parallel light is :yellow:`YELLOW`, it returns ``RED, RED``, which means there will be no traffic in the intersection, the parallel and cross lights will both be :red:`RED`

      .. code-block:: shell

        control(
            current_parallel='YELLOW', current_cross='RED',
            timer_done=True, red_phase='cross'
        ) -> 'RED', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── if red_phase == 'cross':
                        ├── if current_parallel == green:
                        │       return yellow, red
                        └── if current_parallel == yellow:
                            └── return red, red
                            if current_parallel == red:
                                return red, green
                        if red_phase == 'parallel':

    * If the current parallel light is :red:`RED`, it returns ``RED, GREEN``, which means the parallel light will stay :red:`RED` since it is now in the :red:`RED` phase and the next cross light will be :green:`GREEN`

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='RED',
            timer_done=True, red_phase='cross'
        ) -> 'RED', 'GREEN'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── if red_phase == 'cross':
                        ├── if current_parallel == green:
                        │       return yellow, red
                        ├── if current_parallel == yellow:
                        │       return red, red
                        └── if current_parallel == red:
                            └── return red, green
                        if red_phase == 'parallel':

    * If ``cross`` traffic is not in the :red:`RED` phase, it checks if ``parallel`` traffic is in the :red:`RED` phase

  - If ``parallel`` traffic is in the :red:`RED` phase, it checks the value of ``current_cross``

    * If the current cross light is :green:`GREEN`, it returns ``RED, YELLOW``, which means the parallel light will remain :red:`RED` because it is still in the :red:`RED` phase and the next cross light will be :yellow:`YELLOW`

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='GREEN',
            timer_done=True, red_phase='parallel'
        ) -> 'RED', 'YELLOW'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    ├── if red_phase == 'cross':
                    │       ...
                    └── if red_phase == 'parallel':
                        └── if current_cross == green:
                            └── return red, yellow
                            if current_cross == yellow:
                                return red, red
                            if current_cross == red:
                                return green, red


    * If the current parallel light is :yellow:`YELLOW`, it returns ``RED, RED``, which means there will be no traffic in the intersection, the parallel and cross lights will both be :red:`RED`

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='YELLOW',
            timer_done=True, red_phase='parallel'
        ) -> 'RED', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    ├── if red_phase == 'cross':
                    │       ...
                    └── if red_phase == 'parallel':
                        ├── if current_cross == green:
                        │       return red, yellow
                        └── if current_cross == yellow:
                            └── return red, red
                            if current_cross == red:
                                return green, red

    * If the current cross light is :red:`RED`, it returns ``GREEN, RED``, which means the next parallel light will be :green:`GREEN` and the cross light will stay :red:`RED` since it is now in the :red:`RED` phase

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='RED',
            timer_done=True, red_phase='parallel'
        ) -> 'GREEN', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    ├── if red_phase == 'cross':
                    │       ...
                    └── if red_phase == 'parallel':
                        ├── if current_cross == green:
                        │       return red, yellow
                        ├── if current_cross == yellow:
                        │       return red, red
                        └── if current_cross == red:
                            └── return green, red

* If none of the above :ref:`conditions<if statements>` are met it returns :ref:`None<what is None?>`

  .. code-block:: shell

    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── red, yellow, green = 'RED', 'YELLOW', 'GREEN'
            ├── if not timer_done:
            │       return current_parallel, current_cross
            └── if timer_done:
                ├── if red_phase == 'cross':
                │       ...
                ├── if red_phase == 'parallel':
                │       ...

----

*********************************************************************************
test_failsafe
*********************************************************************************

The **Traffic Light** has to make sure that there is never a case where cars move through the intersection at the same time to avoid accidents. The following cases must never happen

================  ================
parallel          cross
================  ================
:green:`GREEN`    :green:`GREEN`
:green:`GREEN`    :yellow:`YELLOW`
:yellow:`YELLOW`  :yellow:`YELLOW`
:yellow:`YELLOW`  :green:`GREEN`
================  ================

It should be :red:`RED` for both ``cross`` and ``parallel`` traffic for any of the above cases and for any cases that are outside the safe cases, for example a power failure.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test for the safety state in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 12-21

        def test_cross_red_parallel_red_timer_done(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='parallel',
                    current_parallel=RED,
                    current_cross=RED,
                    timer_done=True,
                ),
                (GREEN, RED)
            )

        def test_failsafe(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel='BAP',
                    current_cross=RED,
                    timer_done=False,
                ),
                (RED, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('BAP', 'RED') != ('RED', 'RED')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for if ``current_parallel`` is NOT :green:`GREEN` or :yellow:`YELLOW` or :red:`RED`, in ``src/traffic_light/__init__.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 3-8

        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not (
            current_parallel == green
            or current_parallel == yellow
            or current_parallel == red
        ):
            return red, red

        if not timer_done:

the test passes.

.. code-block:: python

  control(
      current_parallel='BAP', current_cross='RED',
      timer_done=False, red_phase='BOOM'
  ) -> 'RED', 'RED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for if ``current_cross`` is NOT :green:`GREEN` or :yellow:`YELLOW` or :red:`RED` to :ref:`test_failsafe` in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 142
    :emphasize-lines: 11-19

        def test_failsafe(self):
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel='BAP',
                    current_cross=RED,
                    timer_done=False,
                ),
                (RED, RED)
            )
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel='BAP',
                    current_cross='POW',
                    timer_done=False,
                ),
                (RED, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('RED', 'POW') != ('RED', 'RED')

* I add an :ref:`if statement<if statements>` for if ``current_cross`` is NOT :green:`GREEN` or :yellow:`YELLOW` or :red:`RED` to :ref:`test_failsafe` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-13

        if not (
            current_parallel == green
            or current_parallel == yellow
            or current_parallel == red
        ):
            return red, red

        if not (
            current_cross == green
            or current_cross == yellow
            or current_cross == red
        ):
            return red, red

        if not timer_done:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED', current_cross='POW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='BAP', current_cross='RED',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_failsafe` for if both lights are :green:`GREEN`, in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 152
    :emphasize-lines: 10-18

            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=RED,
                    current_cross='POW',
                    timer_done=False,
                ),
                (RED, RED)
            )
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=GREEN,
                    current_cross=GREEN,
                    timer_done=False,
                ),
                (RED, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('GREEN', 'GREEN') != ('RED', 'RED')

* I add an :ref:`if statement<if statements>` for if both lights are :green:`GREEN`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-9

        if not (
            current_cross == green
            or current_cross == yellow
            or current_cross == red
        ):
            return red, red

        if current_parallel == current_cross == green:
            return red, red

        if not timer_done:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED', current_cross='POW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='BAP', current_cross='RED',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_failsafe` for if the parallel lights are :green:`GREEN` AND the cross lights are :yellow:`YELLOW`, in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 161
    :emphasize-lines: 10-18

            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=GREEN,
                    current_cross=GREEN,
                    timer_done=False,
                ),
                (RED, RED)
            )
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=GREEN,
                    current_cross=YELLOW,
                    timer_done=False,
                ),
                (RED, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('GREEN', 'YELLOW') != ('RED', 'RED')

* I add an :ref:`if statement<if statements>` for if the parallel lights are :green:`GREEN` AND the cross lights are :yellow:`YELLOW`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-4

        if current_parallel == current_cross == green:
            return red, red
        if current_parallel == green and current_cross == yellow:
            return red, red

        if not timer_done:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED', current_cross='POW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='BAP', current_cross='RED',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='YELLOW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_failsafe` for if the parallel lights are :yellow:`YELLOW` AND the cross lights are :green:`GREEN`, in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 170
    :emphasize-lines: 10-18

            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=GREEN,
                    current_cross=YELLOW,
                    timer_done=False,
                ),
                (RED, RED)
            )
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=YELLOW,
                    current_cross=GREEN,
                    timer_done=False,
                ),
                (RED, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('YELLOW', 'GREEN') != ('RED', 'RED')

* I add an :ref:`if statement<if statements>` for if the parallel lights are :yellow:`YELLOW` AND the cross lights are :green:`GREEN`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

        if current_parallel == current_cross == green:
            return red, red
        if current_parallel == green and current_cross == yellow:
            return red, red
        if current_parallel == yellow and current_cross == green:
            return red, red

        if not timer_done:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED', current_cross='POW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='BAP', current_cross='RED',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='YELLOW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='YELLOW', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_failsafe` for if both lights are :yellow:`YELLOW`, in ``tests/test_traffic_light.py``

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 10-18

            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=YELLOW,
                    current_cross=GREEN,
                    timer_done=False,
                ),
                (RED, RED)
            )
            self.assertEqual(
                src.traffic_light.control(
                    red_phase='BOOM',
                    current_parallel=YELLOW,
                    current_cross=YELLOW,
                    timer_done=False,
                ),
                (RED, RED)
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Tuples differ: ('YELLOW', 'YELLOW') != ('RED', 'RED')

* I add an :ref:`if statement<if statements>` for if both lights are :yellow:`YELLOW`, in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 7-8

        if current_parallel == current_cross == green:
            return red, red
        if current_parallel == green and current_cross == yellow:
            return red, red
        if current_parallel == yellow and current_cross == green:
            return red, red
        if current_parallel == current_cross == yellow:
            return red, red

        if not timer_done:

  the test passes.

  .. code-block:: python

    control(
        current_parallel='RED', current_cross='POW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='BAP', current_cross='RED',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='GREEN', current_cross='YELLOW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='YELLOW', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    control(
        current_parallel='YELLOW', current_cross='YELLOW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'

----

* I add an :ref:`if statement<if statements>` for if the parallel lights and cross lights are the same AND are not equal to :red:`RED`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1-2, 8-9

        # if current_parallel == current_cross == green:
        if current_parallel == current_cross != red:
            return red, red
        if current_parallel == green and current_cross == yellow:
            return red, red
        if current_parallel == yellow and current_cross == green:
            return red, red
        # if current_parallel == current_cross == yellow:
        #     return red, red

        if not timer_done:

  the tests are still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 14

        if not (
            current_cross == green
            or current_cross == yellow
            or current_cross == red
        ):
            return red, red

        if current_parallel == current_cross != red:
            return red, red
        if current_parallel == green and current_cross == yellow:
            return red, red
        if current_parallel == yellow and current_cross == green:
            return red, red

        if not timer_done:

* I add a :ref:`return statement<the return statement>` with the safety state as what the ``control`` :ref:`function<what is a function?>` returns by default

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 9

            if red_phase == 'parallel':
                if current_cross == green:
                    return red, yellow
                if current_cross == yellow:
                    return red, red
                if current_cross == red:
                    return green, red

        return red, red

  still green.

* I remove ``if current_cross == yellow:`` from ``if red_phase == 'parallel':`` since it returns the safety state

  .. code-block:: python
    :lineno-start: 39

            if red_phase == 'parallel':
                if current_cross == green:
                    return red, yellow
                if current_cross == red:
                    return green, red

        return red, red

  green.

* I remove ``if current_parallel == yellow:`` from ``if red_phase == 'cross':`` since it returns the safety state

  .. code-block:: python
    :lineno-start: 31

        if timer_done:
            if red_phase == 'cross':
                if current_parallel == green:
                    return yellow, red
                if current_parallel == red:
                    return red, green
            if red_phase == 'parallel':

  still green.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_failsafe'

----

*********************************************************************************
extract is_not_safe function
*********************************************************************************

* I add a :ref:`function<what is a function?>` to check for when both lights allow traffic at the same time

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-8

    def is_not_safe(parallel, cross):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        if parallel == cross != red:
            return True
        if parallel == green and cross == yellow:
            return True
        if parallel == yellow and cross == green:
            return True


    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'


* I add a :ref:`call<how to call a function with input>` to the :ref:`is_not_safe function<extract is_not_safe function>` for the :ref:`if statements` that check if the lights allow traffic both ways

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 17-25

        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if not (
            current_parallel == green
            or current_parallel == yellow
            or current_parallel == red
        ):
            return red, red

        if not (
            current_cross == green
            or current_cross == yellow
            or current_cross == red
        ):
            return red, red

        if is_not_safe(current_parallel, current_cross):
            return red, red
        if current_parallel == current_cross != red:
        # if current_parallel == current_cross != red:
        #     return red, red
        # if current_parallel == green and current_cross == yellow:
        #     return red, red
        # if current_parallel == yellow and current_cross == green:
        #     return red, red

        if not timer_done:

  the tests are still green.

* I remove the other :ref:`if statements` for the :ref:`if statements` that check if the lights allow traffic both ways, because they are no longer needed.

  .. code-block:: python
    :lineno-start: 31

        if is_not_safe(current_parallel, current_cross):
            return red, red

        if not timer_done:
            return current_parallel, current_cross

* I write a :ref:`conditional expression<conditional expressions>` for the :ref:`if statements` in the :ref:`is_not_safe function<extract is_not_safe function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-7

    def is_not_safe(parallel, cross):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return (
            (parallel == cross != red)
            or (parallel == green and cross == yellow)
            or (parallel == yellow and cross == green)
        )
        if parallel == cross != red:
            return True
        if parallel == green and cross == yellow:
            return True
        if parallel == yellow and cross == green:
            return True



    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):

  still green.

* I remove the other :ref:`if statements` because they are no longer used

  .. code-block:: python
    :linenos:

    def is_not_safe(parallel, cross):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return (
            (parallel == cross != red)
            or (parallel == green and cross == yellow)
            or (parallel == yellow and cross == green)
        )



    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract is_not_safe function'

----

*********************************************************************************
extract is_not_light function
*********************************************************************************

----

* I add a :ref:`function<what is a function?>` to check if the value of a light is :green:`GREEN` or :yellow:`YELLOW` or :red:`RED`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-15

    def is_not_safe(parallel, cross):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return (
            (parallel == cross != red)
            or (parallel == green and cross == yellow)
            or (parallel == yellow and cross == green)
        )


    def is_not_light(light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        if not (
            light == green or light == yellow or light == red
        ):
            return True


    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):

* I add a :ref:`call<how to call a function with input>` to the :ref:`is_not_light function<extract is_not_light function>` for the :ref:`if statements` that check if ``current_parallel`` is :green:`GREEN` or :yellow:`YELLOW` or :red:`RED`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 7-14

    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if is_not_light(current_parallel):
            return red, red
        # if not (
        #     current_parallel == green
        #     or current_parallel == yellow
        #     or current_parallel == red
        # ):
        #     return red, red

  green.

* I add a :ref:`call<how to call a function with input>` to the :ref:`is_not_light function<extract is_not_light function>` for the :ref:`if statements` that check if ``current_cross`` is :green:`GREEN` or :yellow:`YELLOW` or :red:`RED`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3-10

        #     return red, red

        if is_not_light(current_cross):
            return red, red
        # if not (
        #     current_cross == green
        #     or current_cross == yellow
        #     or current_cross == red
        # ):
        #     return red, red

        if is_not_safe(current_parallel, current_cross):

  green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 18

    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if is_not_light(current_parallel):
            return red, red
        if is_not_light(current_cross):
            return red, red
        if is_not_safe(current_parallel, current_cross):
            return red, red

        if not timer_done:
            return current_parallel, current_cross

        if timer_done:
            if red_phase == 'cross':
                if current_parallel == green:
                    return yellow, red
                if current_parallel == red:
                    return red, green
            if red_phase == 'parallel':
                if current_cross == green:
                    return red, yellow
                if current_cross == red:
                    return green, red

        return red, red

* I add a :ref:`conditional expression<conditional expressions>` to the :ref:`is_not_light function<extract is_not_light function>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-5

    def is_not_light(light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return not (
            light == green or light == yellow or light == red
        )
        if not (
            light == green or light == yellow or light == red
        ):
            return True

  still green.

* I remove the :ref:`if statement<if statements>` from the :ref:`is_not_light function<extract is_not_light function>`

  .. code-block:: python
    :lineno-start: 10

    def is_not_light(light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return not (
            light == green or light == yellow or light == red
        )


    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'extract is_not_light function'

----

*********************************************************************************
extract triggers_failsafe function
*********************************************************************************

* I add a :ref:`function<what is a function?>` for the three :ref:`functions` which trigger the fail safe

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8-12

    def is_not_light(light):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return not (
            light == green or light == yellow or light == red
        )


    def triggers_failsafe(parallel, cross):
        return (
            is_not_light(parallel) or is_not_light(cross)
            or is_not_safe(parallel, cross)
        )


    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):

* I add a :ref:`call<how to call a function with input>` to the :ref:`triggers_failsafe function<extract triggers_failsafe function>` from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-14

    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if triggers_failsafe(current_parallel, current_cross):
            return red, red
        # if is_not_light(current_parallel):
        #     return red, red
        # if is_not_light(current_cross):
        #     return red, red
        # if is_not_safe(current_parallel, current_cross):
        #     return red, red

        if not timer_done:

  the tests are still green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 24

    def control(
            timer_done, red_phase='parallel',
            current_parallel='RED', current_cross='RED',
        ):
        red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if triggers_failsafe(current_parallel, current_cross):
            return red, red

        if not timer_done:
            return current_parallel, current_cross

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract triggers_failsafe function'

----

*********************************************************************************
extract global variables for lights
*********************************************************************************

* I add :ref:`global variables<what is a variable?>` for :green:`GREEN`, :yellow:`YELLOW` and :red:`RED`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'


    def is_not_safe(parallel, cross):

* I use the :ref:`variables<what is a variable?>` for :green:`GREEN`, :yellow:`YELLOW` and :red:`RED` in the :ref:`is_not_safe function<extract is_not_safe function>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2, 4-9

    def is_not_safe(parallel, cross):
        # red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return (
            # (parallel == cross != red)
            (parallel == cross != RED)
            # or (parallel == green and cross == yellow)
            or (parallel == GREEN and cross == YELLOW)
            # or (parallel == yellow and cross == green)
            or (parallel == YELLOW and cross == GREEN)
        )

  still green.

* I remove the commented lines from the :ref:`is_not_safe function<extract is_not_safe function>`

  .. code-block:: python
    :lineno-start: 4

    def is_not_safe(parallel, cross):
        return (
            (parallel == cross != RED)
            or (parallel == GREEN and cross == YELLOW)
            or (parallel == YELLOW and cross == GREEN)
        )


    def is_not_light(light):

* I use the :ref:`variables<what is a variable?>` for :green:`GREEN`, :yellow:`YELLOW` and :red:`RED` in the :ref:`is_not_light function<extract is_not_light function>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2, 4-6

    def is_not_light(light):
        # red, yellow, green = 'RED', 'YELLOW', 'GREEN'
        return not (
            # light == green or light == yellow or light == red
            light == GREEN or light == YELLOW or light == RED
        )


    def triggers_failsafe(parallel, cross):

  green.

* I remove the commented lines from the :ref:`is_not_light function<extract is_not_light function>`

  .. code-block:: python
    :lineno-start: 12

    def is_not_light(light):
        return not (
            light == GREEN or light == YELLOW or light == RED
        )


    def triggers_failsafe(parallel, cross):

* I use the :ref:`variables<what is a variable?>` for :green:`GREEN`, :yellow:`YELLOW` and :red:`RED` in the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3, 6, 9-10

    def control(
            timer_done, red_phase='parallel',
            # current_parallel='RED', current_cross='RED',
            current_parallel=RED, current_cross=RED,
        ):
        # red, yellow, green = 'RED', 'YELLOW', 'GREEN'

        if triggers_failsafe(current_parallel, current_cross):
            # return red, red
            return RED, RED

        if not timer_done:
            return current_parallel, current_cross

        if timer_done:

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-10, 12-19, 21-22

        if timer_done:
            if red_phase == 'cross':
                # if current_parallel == green:
                if current_parallel == GREEN:
                    # return yellow, red
                    return YELLOW, RED
                # if current_parallel == red:
                if current_parallel == RED:
                    # return red, green
                    return RED, GREEN
            if red_phase == 'parallel':
                # if current_cross == green:
                if current_cross == GREEN:
                    # return red, yellow
                    return RED, YELLOW
                # if current_cross == red:
                if current_cross == RED:
                    # return green, red
                    return GREEN, RED

        # return red, red
        return RED, RED

  still green.

* I remove the commented lines from the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 25

    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):
        if triggers_failsafe(current_parallel, current_cross):
            return RED, RED

        if not timer_done:
            return current_parallel, current_cross

        if timer_done:
            if red_phase == 'cross':
                if current_parallel == GREEN:
                    return YELLOW, RED
                if current_parallel == RED:
                    return RED, GREEN
            if red_phase == 'parallel':
                if current_cross == GREEN:
                    return RED, YELLOW
                if current_cross == RED:
                    return GREEN, RED

        return RED, RED

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'extract global variables for lights'

----

*********************************************************************************
extract next_light function
*********************************************************************************

* I add a :ref:`function<what is a function?>` for when the timer is :green:`done` and none of the fail safes are triggered

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8-19

    def triggers_failsafe(parallel, cross):
        return (
            is_not_light(parallel) or is_not_light(cross)
            or is_not_safe(parallel, cross)
        )


    def next_light(red_phase, parallel, cross):
        if red_phase == 'cross':
            if parallel == GREEN:
                return YELLOW, RED
            if parallel == RED:
                return RED, GREEN
        if red_phase == 'parallel':
            if cross == GREEN:
                return RED, YELLOW
            if cross == RED:
                return GREEN, RED
        return RED, RED


    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):

* I add a :ref:`call<how to call a function with input>` to the :ref:`next_light function<extract next_light function>` from ``if timer_done:`` in the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 12-14

    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):
        if triggers_failsafe(current_parallel, current_cross):
            return RED, RED

        if not timer_done:
            return current_parallel, current_cross

        if timer_done:
            return next_light(
                red_phase, current_parallel, current_cross
            )
            if red_phase == 'cross':

  the tests are still green.

* I remove the other statements in the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 39

    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):
        if triggers_failsafe(current_parallel, current_cross):
            return RED, RED

        if not timer_done:
            return current_parallel, current_cross

        if timer_done:
            return next_light(
                red_phase, current_parallel, current_cross
            )

        return RED, RED

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'extract next_light function'

----

When the ``control`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it :ref:`calls<how to call a function with input>` the :ref:`triggers_failsafe function<extract triggers_failsafe function>` to check if the values of ``current_parallel`` or ``current_cross`` trigger the failsafe. The :ref:`triggers_failsafe function<extract triggers_failsafe function>` :ref:`calls<how to call a function with input>` the :ref:`is_not_light function<extract is_not_light function>` or :ref:`is_not_safe function<extract is_not_safe function>` to check the values of ``current_parallel`` and ``current_cross``

* If the failsafe is :green:`triggered`, it turns the parallel and cross lights :red:`RED`

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='POW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            └── if triggers_failsafe(current_parallel, current_cross):
                ├── def triggers_failsafe(parallel, cross):
                │   └── return (
                │       │   is_not_light(parallel)
                │       └── or is_not_light(cross)
                │           or is_not_safe(parallel, cross)
                │       )
                │       └── def is_not_light(light):
                │           └── return not (
                │                   light == GREEN or light == YELLOW
                │                   or light == RED
                │               )
                │               return True
                └── return RED, RED
                if not timer_done:

  .. code-block:: shell

    control(
        current_parallel='BAP', current_cross='RED',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            └── if triggers_failsafe(current_parallel, current_cross):
                ├── def triggers_failsafe(parallel, cross):
                │   └── return (
                │       └── is_not_light(parallel)
                │           or is_not_light(cross)
                │           or is_not_safe(parallel, cross)
                │       )
                │       └── def is_not_light(light):
                │           └── return not (
                │                   light == GREEN or light == YELLOW
                │                   or light == RED
                │               )
                │               return True
                └── return RED, RED
                if not timer_done:

  .. code-block:: shell

    control(
        current_parallel='GREEN', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            └── if triggers_failsafe(current_parallel, current_cross):
                ├── def triggers_failsafe(parallel, cross):
                │   └── return (
                │       │   is_not_light(parallel) or is_not_light(cross)
                │       └── or is_not_safe(parallel, cross)
                │       )
                │       └── def is_not_safe(parallel, cross):
                │           └── return (
                │               └── (parallel == cross != RED)
                │                   or (parallel == GREEN and cross == YELLOW)
                │                   or (parallel == YELLOW and cross == GREEN)
                │               )
                │               return True
                └── return RED, RED
                if not timer_done:

  .. code-block:: shell

    control(
        current_parallel='GREEN', current_cross='YELLOW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            └── if triggers_failsafe(current_parallel, current_cross):
                ├── def triggers_failsafe(parallel, cross):
                │   └── return (
                │       │   is_not_light(parallel) or is_not_light(cross)
                │       └── or is_not_safe(parallel, cross)
                │       )
                │       └── def is_not_safe(parallel, cross):
                │           └── return (
                │               │   (parallel == cross != RED)
                │               └── or (parallel == GREEN and cross == YELLOW)
                │                   or (parallel == YELLOW and cross == GREEN)
                │               )
                │               return True
                └── return RED, RED
                if not timer_done:

  .. code-block:: shell

    control(
        current_parallel='YELLOW', current_cross='GREEN',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            └── if triggers_failsafe(current_parallel, current_cross):
                ├── def triggers_failsafe(parallel, cross):
                │   └── return (
                │       │   is_not_light(parallel) or is_not_light(cross)
                │       └── or is_not_safe(parallel, cross)
                │       )
                │       └── def is_not_safe(parallel, cross):
                │           └── return (
                │               │   (parallel == cross != RED)
                │               │   or (parallel == GREEN and cross == YELLOW)
                │               └── or (parallel == YELLOW and cross == GREEN)
                │               )
                │               return True
                └── return RED, RED
                if not timer_done:

  .. code-block:: shell

    control(
        current_parallel='YELLOW', current_cross='YELLOW',
        timer_done=False, red_phase='BOOM'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            └── if triggers_failsafe(current_parallel, current_cross):
                ├── def triggers_failsafe(parallel, cross):
                │   └── return (
                │       │   is_not_light(parallel) or is_not_light(cross)
                │       └── or is_not_safe(parallel, cross)
                │       )
                │       └── def is_not_safe(parallel, cross):
                │           └── return (
                │               └── (parallel == cross != RED)
                │                   or (parallel == GREEN and cross == YELLOW)
                │                   or (parallel == YELLOW and cross == GREEN)
                │               )
                │               return True
                └── return RED, RED
                if not timer_done:

  If the failsafe is :red:`NOT triggered`, it checks if the timer is :red:`NOT done`

* If the timer is :red:`NOT done`, it returns the values of ``current_parallel`` and ``current_cross``, which means it does not change the parallel or cross lights, it keeps them the same

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='GREEN',
        timer_done=False, red_phase='parallel'
    ) -> 'RED', 'GREEN'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel=RED, current_cross=RED,
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'GREEN'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='YELLOW',
        timer_done=False, red_phase='parallel'
    ) -> 'RED', 'YELLOW'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'YELLOW'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='RED',
        timer_done=False, red_phase='parallel'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'RED'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='GREEN', current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'GREEN', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'GREEN'         , 'RED'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='YELLOW', current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'YELLOW', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'YELLOW'        , 'RED'
                if timer_done:

  .. code-block:: shell

    control(
        current_parallel='RED', current_cross='RED',
        timer_done=False, red_phase='cross'
    ) -> 'RED', 'RED'
    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            └── if not timer_done:
                └── return current_parallel, current_cross
                    return 'RED'           , 'RED'
                if timer_done:

* If the timer is :green:`done`, it :ref:`calls<how to call a function with input>` the :ref:`next_light function<extract next_light function>` which checks if ``cross`` traffic is in the :red:`RED` phase

  - If ``cross`` traffic is in the :red:`RED` phase, it checks the value of ``current_parallel``

    * If the current parallel light is :green:`GREEN`, it returns ``YELLOW, RED``, which means the next parallel light will be :yellow:`YELLOW` and the cross light will remain :red:`RED` because it is still in the :red:`RED` phase

      .. code-block:: shell

        control(
            current_parallel='GREEN', current_cross='RED',
            timer_done=True, red_phase='cross'
        ) -> 'YELLOW', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── if triggers_failsafe(current_parallel, current_cross):
                │       return RED, RED
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── return next_light(
                            red_phase, current_parallel, current_cross
                        )
                        └── def next_light(red_phase, parallel, cross):
                            └── if red_phase == 'cross':
                                └── if parallel == GREEN:
                                    └── return YELLOW, RED
                                    if parallel == RED:

    * If the current parallel light is :red:`RED`, it returns ``RED, GREEN``, which means the parallel light will stay :red:`RED` since it is now in the :red:`RED` phase and the next cross light will be :green:`GREEN`

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='RED',
            timer_done=True, red_phase='cross'
        ) -> 'RED', 'GREEN'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── if triggers_failsafe(current_parallel, current_cross):
                │       return RED, RED
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── return next_light(
                            red_phase, current_parallel, current_cross
                        )
                        └── def next_light(red_phase, parallel, cross):
                            └── if red_phase == 'cross':
                                ├── if parallel == GREEN:
                                │       return YELLOW, RED
                                └── if parallel == RED:
                                    └── return RED, GREEN
                                if red_phase == 'parallel':

    * If ``cross`` traffic is not in the :red:`RED` phase, it checks if ``parallel`` traffic is in the :red:`RED` phase

  - If ``parallel`` traffic is in the :red:`RED` phase, it checks the value of ``current_cross``

    * If the current cross light is :green:`GREEN`, it returns ``RED, YELLOW``, which means the parallel light will remain :red:`RED` because it is still in the :red:`RED` phase and the next cross light will be :yellow:`YELLOW`

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='GREEN',
            timer_done=True, red_phase='parallel'
        ) -> 'RED', 'YELLOW'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── if triggers_failsafe(current_parallel, current_cross):
                │       return RED, RED
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── return next_light(
                            red_phase, current_parallel, current_cross
                        )
                        └── def next_light(red_phase, parallel, cross):
                            ├── if red_phase == 'cross':
                            │       ...
                            └── if red_phase == 'parallel':
                                └── if cross == GREEN:
                                    └── return RED, YELLOW
                                    if cross == RED:

    * If the current cross light is :red:`RED`, it returns ``GREEN, RED``, which means the next parallel light will be :green:`GREEN` and the cross light will stay :red:`RED` since it is now in the :red:`RED` phase

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='RED',
            timer_done=True, red_phase='parallel'
        ) -> 'GREEN', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── if triggers_failsafe(current_parallel, current_cross):
                │       return RED, RED
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── return next_light(
                            red_phase, current_parallel, current_cross
                        )
                        └── def next_light(red_phase, parallel, cross):
                            ├── if red_phase == 'cross':
                            │       ...
                            └── if red_phase == 'parallel':
                                ├── if cross == GREEN:
                                │       return RED, YELLOW
                                └── if cross == RED:
                                    └── return GREEN, RED
                                return RED, RED

    * If none of the above :ref:`conditions<if statements>` are met, it returns ``RED, RED``, which means there will be no traffic in the intersection, the parallel and cross lights will both be :red:`RED`

      .. code-block:: shell

        control(
            current_parallel='YELLOW', current_cross='RED',
            timer_done=True, red_phase='cross'
        ) -> 'RED', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── if triggers_failsafe(current_parallel, current_cross):
                │       return RED, RED
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── return next_light(
                            red_phase, current_parallel, current_cross
                        )
                        └── def next_light(red_phase, parallel, cross):
                            └── if red_phase == 'cross':
                                ├── if parallel == GREEN:
                                │       return YELLOW, RED
                            ┌───┴── if parallel == RED:
                            │           return RED, GREEN
                            │   if red_phase == 'parallel':
                            │       if cross == GREEN:
                            │           return RED, YELLOW
                            │       if cross == RED:
                            │           return GREEN, RED
                            └── return RED, RED

      .. code-block:: shell

        control(
            current_parallel='RED', current_cross='YELLOW',
            timer_done=True, red_phase='parallel'
        ) -> 'RED', 'RED'
        └── def control(
                    timer_done, red_phase='parallel',
                    current_parallel='RED', current_cross='RED',
                ):
                ├── if triggers_failsafe(current_parallel, current_cross):
                │       return RED, RED
                ├── if not timer_done:
                │       return current_parallel, current_cross
                └── if timer_done:
                    └── return next_light(
                            red_phase, current_parallel, current_cross
                        )
                        └── def next_light(red_phase, parallel, cross):
                            ├── if red_phase == 'cross':
                            │       if parallel == GREEN:
                            │           return YELLOW, RED
                            │       if parallel == RED:
                            │           return RED, GREEN
                            └── if red_phase == 'parallel':
                                ├── if cross == GREEN:
                                │       return RED, YELLOW
                            ┌───┴── if cross == RED:
                            │           return GREEN, RED
                            └── return RED, RED

* If none of the above :ref:`conditions<if statements>` are met, it returns ``RED, RED``, which means there will be no traffic in the intersection, the parallel and cross lights will both be :red:`RED`

  .. code-block:: shell

    └── def control(
                timer_done, red_phase='parallel',
                current_parallel='RED', current_cross='RED',
            ):
            ├── if triggers_failsafe(current_parallel, current_cross):
            │       return RED, RED
            ├── if not timer_done:
            │       return current_parallel, current_cross
            ├── if timer_done:
            │       return next_light(
            │           red_phase, current_parallel, current_cross
            │        )
            └── return RED, RED

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

I ran tests for a **Traffic Light** that changes lights based on what :red:`RED` phase the traffic is in (``'cross'`` or ``'parallel'``) AND if a timer is :green:`done` or :red:`NOT done`

The outputs are the next lights for Parallel and Cross Traffic which gave me this :ref:`truth table`

==========  ================  ================  =============== =================== =================
red         current           current                           next                next
phase       parallel          cross             timer           parallel            cross
==========  ================  ================  =============== =================== =================
'cross'     :green:`GREEN`    :red:`RED`        :red:`NOT done` :green:`GREEN`      :red:`RED`
'cross'     :green:`GREEN`    :red:`RED`        :green:`done`   :yellow:`YELLOW`    :red:`RED`
'cross'     :yellow:`YELLOW`  :red:`RED`        :red:`NOT done` :yellow:`YELLOW`    :red:`RED`
'cross'     :yellow:`YELLOW`  :red:`RED`        :green:`done`   safety :red:`RED`   safety :red:`RED`
'cross'     :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
'cross'     :red:`RED`        :red:`RED`        :green:`done`   :red:`RED`          :green:`GREEN`
==========  ================  ================  =============== =================== =================


==========  ================  ================  =============== =================== =================
red         current           current                           next                next
phase       parallel          cross             timer           parallel            cross
==========  ================  ================  =============== =================== =================
'parallel'  :red:`RED`        :green:`GREEN`    :red:`NOT done` :red:`RED`          :green:`GREEN`
'parallel'  :red:`RED`        :green:`GREEN`    :green:`done`   :red:`RED`          :yellow:`YELLOW`
'parallel'  :red:`RED`        :yellow:`YELLOW`  :red:`NOT done` :red:`RED`          :yellow:`YELLOW`
'parallel'  :red:`RED`        :yellow:`YELLOW`  :green:`done`   safety :red:`RED`   safety :red:`RED`
'parallel'  :red:`RED`        :red:`RED`        :red:`NOT done` safety :red:`RED`   safety :red:`RED`
'parallel'  :red:`RED`        :red:`RED`        :green:`done`   :green:`GREEN`      :red:`RED`
==========  ================  ================  =============== =================== =================

It also makes sure that there is never a case where cars move through the intersection at the same time to avoid accidents.

What if the **Traffic Light** has a walk button and I push it?
What if the **Traffic Light** changes based on if there is an emergency vehicle?
What would the inputs be and what :ref:`truth table` do I get?

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