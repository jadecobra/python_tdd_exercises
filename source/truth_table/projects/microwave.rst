.. meta::
  :description: Build a safety-critical Microwave control system using Python and Test Driven Development (TDD). This hands-on project tutorial guides beginners through managing four boolean inputs—door sensors, timers, start buttons, and "too hot" failsafes—using truth tables. Master the professional Red-Green-Refactor cycle, learn to debug complex "SyntaxError" and "TypeError" messages, and use modern tools like uv and pytest-watcher to create verified, robust software logic.
  :keywords: Jacob Itegboje, Python microwave logic tutorial, TDD for beginners project, safety-critical software Python, building a microwave controller code, Python boolean truth table examples, Converse Non-Implication implementation, door sensor safety logic, microwave failsafe code, SyntaxError parameter without a default, TypeError got an unexpected keyword argument, Red Green Refactor Python guide, uv project management, pytest-watcher automated testing, logical negation NOT tutorial, logical disjunction OR example, refactoring nested if statements Python, hardware logic modeling, Python control systems for beginners, truth table to Python code translation

.. include:: ../../links.rst

.. _microwave:

#################################################################################
Microwave
#################################################################################

I want to make a **Microwave** that heats up food when I push a button.

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :linenos:
  :caption: microwave/tests/test_microwave.py
  :lines: 1-23

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 25
  :caption: microwave/tests/test_microwave.py
  :lines: 25-41

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 43
  :caption: microwave/tests/test_microwave.py
  :lines: 43-59

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 61
  :caption: microwave/tests/test_microwave.py
  :lines: 61-77

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 79
  :caption: microwave/tests/test_microwave.py
  :lines: 79-95

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 97
  :caption: microwave/tests/test_microwave.py
  :lines: 97-113

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 115
  :caption: microwave/tests/test_microwave.py
  :lines: 115-131

.. literalinclude:: ../../code/microwave/test_microwave.py
  :language: python
  :lineno-start: 133
  :caption: microwave/tests/test_microwave.py
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

      * I change the name of the project to ``microwave`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/microwave/make_tdd/makePythonTddMicrowave.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 5, 12, 20

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``microwave`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``

      * I change the name of the project to ``microwave`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/microwave/make_tdd/makePythonTddMicrowave.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 4, 11, 19

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``microwave`` project

        .. code-block:: python
          :emphasize-lines: 1

          .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES =========================
    _____________ TestMicrowave.test_failure __________________

    self = <tests.test_microwave.TestMicrowave testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_microwave.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_microwave.py::TestMicrowave::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_microwave.py:7`` to open it
* I change :green:`True` to :red:`False` in ``test_microwave.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestMicrowave(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertFalse(False)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then `change directory`_ to ``microwave``

  .. code-block:: python
    :emphasize-lines: 1

    cd microwave

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

----

I want the **Microwave** to :green:`HEAT UP` only when the start button is :green:`pressed`. I get this :ref:`truth table`

==================  =============
start button        output
==================  =============
:green:`pressed`    :green:`True`
:red:`NOT pressed`  :red:`False`
==================  =============

Where :green:`True` means the **Microwave** will :green:`HEAT UP`, and :red:`False` means it stays :red:`OFF`.

----

*********************************************************************************
test_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change :ref:`test_failure` to :ref:`test_pressed_start` with an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed`

  ==================  =============
  start button        output
  ==================  =============
  :green:`pressed`    :green:`True`
  ==================  =============

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-8

    class TestMicrowave(unittest.TestCase):

        def test_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    pressed_start=True,
                )
            )


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because I do not have a definition for ``src`` in this file_.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.microwave
    import unittest


    class TestMicrowave(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.microwave'
                    has no attribute 'microwave'

  because ``microwave.py`` in the ``src`` folder_ does not have anything named ``microwave`` in it.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``microwave.py`` from the ``src`` folder_

* I delete all the text in the file_ then add a :ref:`function<what is a function?>` named ``microwave`` to ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def microwave():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: microwave() got
               an unexpected keyword argument 'pressed_start'

  because the test :ref:`called<how to call a function with input>` the ``microwave`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``pressed_start``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_microwave.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add ``pressed_start`` to the :ref:`function definition<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(pressed_start):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  the ``microwave`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I change the :ref:`return statement<the return statement>` to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def microwave(pressed_start):
        return True

  the test passes. The ``microwave`` :ref:`function<what is a function?>` always returns :green:`True`.

  .. code-block:: python

    microwave(pressed_start=True ) -> True

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_pressed_start'

----

*********************************************************************************
test_not_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed`

  ==================  =============
  start button        output
  ==================  =============
  :red:`NOT pressed`  :red:`False`
  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-13

        def test_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    pressed_start=True,
                )
            )

        def test_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    pressed_start=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``microwave`` :ref:`function<what is a function?>` always returns :green:`True` and this :ref:`assertion<what is an assertion?>` expects :red:`False`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I make the :ref:`function<what is a function?>` return its input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def microwave(pressed_start):
        return pressed_start

  the test passes.

  .. code-block:: python

    microwave(pressed_start=True ) -> True
    microwave(pressed_start=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_not_pressed_start'

----

I want the **Microwave** to :green:`HEAT UP` only when the **Microwave** door is :green:`closed` AND the start button is :green:`pressed`. The inputs to the **Microwave** will then be

* is the **Microwave** door closed?
* was the start button pressed?

and I get this :ref:`truth table`

=============== ==================  =============
door            start button        output
=============== ==================  =============
:green:`closed` :green:`pressed`    :green:`True`
:green:`closed` :red:`NOT pressed`  :red:`False`
:red:`open`     :green:`pressed`    :red:`False`
:red:`open`     :red:`NOT pressed`  :red:`False`
=============== ==================  =============

Where :green:`True` means the **Microwave** will :green:`HEAT UP`, and :red:`False` means it stays :red:`OFF`.

----

*********************************************************************************
test_open_door_not_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the start button is :red:`NOT pressed`, in ``test_microwave.py``

  =============== ==================  =============
  door            start button        output
  =============== ==================  =============
  :red:`open`     :red:`NOT pressed`  :red:`False`
  =============== ==================  =============

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-14

        def test_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    pressed_start=False,
                )
            )

        def test_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    pressed_start=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: microwave() got
               an unexpected keyword argument 'closed_door

  because the test :ref:`called<how to call a function with input>` the ``microwave`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``closed_door``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``closed_door`` to the :ref:`function signature<how to make a function that takes input>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(closed_door, pressed_start):
        return pressed_start

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_not_pressed_start - TypeError:
        microwave() missing
            1 required positional argument: 'closed_door'
    FAILED ...test_pressed_start - TypeError:
        microwave() missing
            1 required positional argument: 'closed_door'

* I add a :ref:`default value<test_optional_arguments>` for ``closed_door``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(closed_door=False, pressed_start):
        return pressed_start

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_microwave.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a :ref:`default value<test_optional_arguments>` for ``pressed_start``, in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def microwave(closed_door=False, pressed_start=False):
        return pressed_start

  the test passes.

  .. code-block:: python

    microwave(closed_door=False, pressed_start=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'add test_open_door_not_pressed_start'

----

*********************************************************************************
test_open_door_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the start button is :green:`pressed`, in ``test_microwave.py``

  =============== ==================  =============
  door            start button        output
  =============== ==================  =============
  :red:`open`     :green:`pressed`    :red:`False`
  =============== ==================  =============

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-14

        def test_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    pressed_start=False,
                )
            )

        def test_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    pressed_start=True,
                )
            )

        def test_open_door_not_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for ``closed_door`` to the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def microwave(closed_door=False, pressed_start=False):
        if not closed_door:
            return False
        return pressed_start

  the test passes.

  .. code-block:: python

    microwave(closed_door=False, pressed_start=True ) -> False
    microwave(closed_door=False, pressed_start=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'add test_open_door_pressed_start'

----

*********************************************************************************
test_closed_door_not_pressed_start
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add a value for the ``closed_door`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_not_pressed_start` for if the **Microwave** door is :green:`closed` AND the start button is :red:`NOT pressed`

  =============== ==================  =============
  door            start button        output
  =============== ==================  =============
  :green:`closed` :red:`NOT pressed`  :red:`False`
  =============== ==================  =============

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

        def test_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    pressed_start=False,
                )
            )

        def test_closed_door_pressed_start(self):

  the test is still green.

  .. code-block:: python

    microwave(closed_door=True , pressed_start=False) -> False
    microwave(closed_door=False, pressed_start=True ) -> False
    microwave(closed_door=False, pressed_start=False) -> False

* I change the name of the test from :ref:`test_not_pressed_start` to :ref:`test_closed_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8

        def test_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    pressed_start=True,
                )
            )

        def test_closed_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    pressed_start=False,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'add test_closed_door_not_pressed_start'

----

*********************************************************************************
test_closed_door_pressed_start
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add a value for the ``closed_door`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_pressed_start` for if the **Microwave** door is :green:`closed` AND the start button is :green:`pressed`

  =============== ==================  =============
  door            start button        output
  =============== ==================  =============
  :red:`open`     :green:`pressed`    :red:`False`
  =============== ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=True,
                    pressed_start=True,
                )
            )

        def test_closed_door_not_pressed_start(self):

  the test is still green.

  .. code-block:: python

    microwave(closed_door=True , pressed_start=True ) -> True
    microwave(closed_door=True , pressed_start=False) -> False
    microwave(closed_door=False, pressed_start=True ) -> False
    microwave(closed_door=False, pressed_start=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'add test_closed_door_pressed_start'

----

When the ``microwave`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`, it checks if the door is :green:`closed`

* if the door is :red:`open` it returns :red:`False`

  .. code-block:: shell

    microwave(closed_door=False, pressed_start=True ) -> False
    └── def microwave(closed_door=False, pressed_start=False):
        └── if not closed_door:
            └── return False
            return pressed_start

  .. code-block:: shell

    microwave(closed_door=False, pressed_start=False) -> False
    └── def microwave(closed_door=False, pressed_start=False):
        └── if not closed_door:
            └── return False
            return pressed_start

* if the door is :green:`closed` it returns the value of ``pressed_start``

  - if the door is :green:`closed` AND the start button is :red:`NOT pressed` it returns :red:`False`

    .. code-block:: shell

      microwave(closed_door=True , pressed_start=False) -> False
      └── def microwave(closed_door=False, pressed_start=False):
          ├── if not closed_door:
          │       return False
          └── return pressed_start
              return False

  - if the door is :green:`closed` AND the start button is :green:`pressed` it returns :green:`True`

    .. code-block:: shell

      microwave(closed_door=True , pressed_start=True ) -> True
      └── def microwave(closed_door=False, pressed_start=False):
          ├── if not closed_door:
          │       return False
          └── return pressed_start
              return True

So far, the :ref:`truth table` for the **Microwave** is

=============== ==================  =============
door            start button        output
=============== ==================  =============
:green:`closed` :green:`pressed`    :green:`True`
:green:`closed` :red:`NOT pressed`  :red:`False`
:red:`open`     :green:`pressed`    :red:`False`
:red:`open`     :red:`NOT pressed`  :red:`False`
=============== ==================  =============

I want the **Microwave** to only heat up food when the door is :green:`closed` AND the timer is :green:`set` AND the start button is :green:`pressed`. The inputs for the **Microwave** will then be

* is the **Microwave** door closed?
* is the **Microwave** timer set?
* was the start button pressed?

----

*********************************************************************************
test_set_timer_closed_door_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add ``set_timer`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_closed_door_pressed_start`, for if the **Microwave** door is :green:`closed` AND the timer is :green:`set` AND the start button is :green:`pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :green:`closed` :green:`set`    :green:`pressed`    :green:`True`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_closed_door_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_closed_door_not_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: microwave() got
               an unexpected keyword argument 'set_timer'

  because the test :ref:`called<how to call a function with input>` the ``microwave`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``set_timer``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``set_timer`` to the :ref:`function signature<how to make a function that takes input>` in ``microwave.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 1-4

  def microwave(
          closed_door=False, pressed_start=False,
          set_timer=False,
      ):
      if not closed_door:
          return False
      return pressed_start

the test passes.

.. code-block:: python

  microwave(
      closed_door=True, set_timer=True,
      pressed_start=True
  ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_closed_door_pressed_start` to :ref:`test_set_timer_closed_door_pressed_start`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestMicrowave(unittest.TestCase):

        def test_set_timer_closed_door_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=True,
                    pressed_start=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_set_timer_closed_door_pressed_start'

----

*************************************************************************************
test_set_timer_closed_door_not_pressed_start
*************************************************************************************

* I go back to the terminal_ where the tests are running
* I add a value for ``set_timer`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_closed_door_not_pressed_start` for if the **Microwave** door is :green:`closed` AND the timer is :green:`set` AND the start button is :red:`NOT pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :green:`closed` :green:`set`    :red:`NOT pressed`  :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5

        def test_closed_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=True,
                    pressed_start=False,
                )
            )

        def test_open_door_pressed_start(self):

  the test is still green.

  .. code-block:: python

    microwave(
        closed_door=True, set_timer=True,
        pressed_start=True
    ) -> True
    microwave(
        closed_door=True, set_timer=True,
        pressed_start=False
    ) -> False

* I change the name of the test from :ref:`test_closed_door_not_pressed_start` to :ref:`test_set_timer_closed_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10

        def test_set_timer_closed_door_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_set_timer_closed_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=True,
                    pressed_start=False,
                )
            )

* I add a git_ commit message in the other terminal

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_set_timer_closed_door_not_pressed_start'

----

*********************************************************************************
test_not_set_timer_closed_door_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :green:`closed` AND the timer is :red:`NOT set` AND the start button is :green:`pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :green:`closed` :red:`NOT set`  :green:`pressed`    :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10-17

        def test_set_timer_closed_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=True,
                    pressed_start=False,
                )
            )

        def test_not_set_timer_closed_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=False,
                    pressed_start=True,
                )
            )

        def test_open_door_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for ``set_timer`` to the :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

      def microwave(
              closed_door=False, pressed_start=False,
              set_timer=False,
          ):
          if not closed_door:
              return False
          if not set_timer:
              return False
          return pressed_start

  the test passes.

  .. code-block:: python

    microwave(
        closed_door=True, set_timer=True,
        pressed_start=True
    ) -> True
    microwave(
        closed_door=True, set_timer=True,
        pressed_start=False
    ) -> False
    microwave(
        closed_door=True, set_timer=False,
        pressed_start=True
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_not_set_timer_closed_door_pressed_start'

----

*********************************************************************************
test_not_set_timer_closed_door_not_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :green:`closed` AND the timer is :red:`NOT set` AND the start button is :red:`NOT pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :green:`closed` :red:`NOT set`  :red:`NOT pressed`  :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-17

        def test_not_set_timer_closed_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=False,
                    pressed_start=True,
                )
            )

        def test_not_set_timer_closed_door_not_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=False,
                    pressed_start=False,
                )
            )

        def test_open_door_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_not_set_timer_closed_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

        def test_not_set_timer_closed_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=False,
                    pressed_start=False,
                )
            )

        def test_open_door_pressed_start(self):

  the test passes.

  .. code-block:: python

    microwave(
        closed_door=True, set_timer=True,
        pressed_start=True
    ) -> True
    microwave(
        closed_door=True, set_timer=True,
        pressed_start=False
    ) -> False
    microwave(
        closed_door=True, set_timer=False,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=True, set_timer=False,
        pressed_start=False
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_not_set_timer_closed_door_not_pressed_start'

----

*********************************************************************************
test_set_timer_open_door_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add ``set_timer`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_open_door_pressed_start`, for if the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :green:`pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :red:`open`     :green:`set`    :green:`pressed`    :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5

        def test_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_open_door_not_pressed_start(self):

  the test is still green.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=True
    ) -> False

* I change the name of the test from :ref:`test_open_door_pressed_start` to :ref:`test_set_timer_open_door_pressed_start`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10

        def test_not_set_timer_closed_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=True,
                    set_timer=False,
                    pressed_start=False,
                )
            )

        def test_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_open_door_not_pressed_start(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_set_timer_open_door_pressed_start'

----

*************************************************************************************
test_set_timer_open_door_not_pressed_start
*************************************************************************************

* I go back to the terminal_ where the tests are running
* I add a value for ``set_timer`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_open_door_not_pressed_start` for if the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :red:`NOT pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :red:`open`     :green:`set`    :red:`NOT pressed`  :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 5

        def test_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                )
            )


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False

* I change the name of the test from :ref:`test_open_door_not_pressed_start` to :ref:`test_set_timer_open_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10

        def test_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                )
            )

* I add a git_ commit message in the other terminal

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_set_timer_open_door_not_pressed_start'

----

*********************************************************************************
test_not_set_timer_open_door_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :green:`pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :red:`open`     :red:`NOT set`  :green:`pressed`    :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10-17

        def test_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                )
            )

        def test_not_set_timer_open_door_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_not_set_timer_open_door_pressed_start`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

        def test_not_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                )
            )


    # Exceptions seen

  the test passes.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_not_set_timer_open_door_pressed_start'

----

*********************************************************************************
test_not_set_timer_open_door_not_pressed_start
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :red:`NOT pressed`

  =============== ==============  ==================  =============
  door            timer           start button        output
  =============== ==============  ==================  =============
  :red:`open`     :red:`NOT set`  :red:`NOT pressed`  :red:`False`
  =============== ==============  ==================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10-17

        def test_not_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                )
            )

        def test_not_set_timer_open_door_not_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_not_set_timer_open_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2

        def test_not_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                )
            )


    # Exceptions seen

  the test passes.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=False
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_not_set_timer_open_door_not_pressed_start'

----

When the ``microwave`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`, it checks if the **Microwave** door is :green:`closed`

* If the **Microwave** door is :red:`open`, it returns :red:`False`

  .. code-block:: shell

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=True
    ) -> False
    └── def microwave(
                closed_door=False, pressed_start=False,
                set_timer=False,
            ):
            └── if not closed_door:
                └── return False
                if not set_timer:
                    return False
                return pressed_start

  .. code-block:: shell

    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False
    └── def microwave(
                closed_door=False, pressed_start=False,
                set_timer=False,
            ):
            └── if not closed_door:
                └── return False
                if not set_timer:
                    return False
                return pressed_start

  .. code-block:: shell

    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True
    ) -> False
    └── def microwave(
                closed_door=False, pressed_start=False,
                set_timer=False,
            ):
            └── if not closed_door:
                └── return False
                if not set_timer:
                    return False
                return pressed_start

  .. code-block:: shell

    microwave(
        closed_door=False, set_timer=False,
        pressed_start=False
    ) -> False
    └── def microwave(
                closed_door=False, pressed_start=False,
                set_timer=False,
            ):
            └── if not closed_door:
                └── return False
                if not set_timer:
                    return False
                return pressed_start

* If the **Microwave** door is :green:`closed`, it checks if the timer is :green:`set`

  - If the timer is :red:`NOT set`, it returns :red:`False`

    .. code-block:: shell

      microwave(
          closed_door=True, set_timer=False,
          pressed_start=True
      ) -> False
      └── def microwave(
                  closed_door=False, pressed_start=False,
                  set_timer=False,
              ):
              ├── if not closed_door:
              │       return False
              └── if not set_timer:
                  └── return False
                  return pressed_start

    .. code-block:: shell

      microwave(
          closed_door=True, set_timer=False,
          pressed_start=False
      ) -> False
      └── def microwave(
                  closed_door=False, pressed_start=False,
                  set_timer=False,
              ):
              ├── if not closed_door:
              │       return False
              └── if not set_timer:
                  └── return False
                  return pressed_start

  - If the timer is :green:`set`, it returns the value of ``pressed_start``

    * If the start button is :red:`NOT pressed`, it returns :red:`False`

      .. code-block:: shell

        microwave(
            closed_door=True, set_timer=True,
            pressed_start=False
        ) -> False
        └── def microwave(
                    closed_door=False, pressed_start=False,
                    set_timer=False,
                ):
                ├── if not closed_door:
                │       return False
                ├── if not set_timer:
                │       return False
                └── return pressed_start
                    return False

    * If the **Microwave** door is :green:`closed` AND the timer is :green:`set` and the start button is :green:`pressed`, it returns :green:`True`

      .. code-block:: shell

        microwave(
            closed_door=True, set_timer=True,
            pressed_start=True
        ) -> True
        └── def microwave(
                    closed_door=False, pressed_start=False,
                    set_timer=False,
                ):
                ├── if not closed_door:
                │       return False
                ├── if not set_timer:
                │       return False
                └── return pressed_start
                    return True

The :ref:`truth table` for the **Microwave** is

=============== ==============  ==================  =============
door            timer           start button        output
=============== ==============  ==================  =============
:green:`closed` :green:`set`    :green:`pressed`    :green:`True`
:green:`closed` :green:`set`    :red:`NOT pressed`  :red:`False`
:green:`closed` :red:`NOT set`  :green:`pressed`    :red:`False`
:green:`closed` :red:`NOT set`  :red:`NOT pressed`  :red:`False`
=============== ==============  ==================  =============

=============== ==============  ==================  =============
door            timer           start button        output
=============== ==============  ==================  =============
:red:`open`     :green:`set`    :green:`pressed`    :red:`False`
:red:`open`     :green:`set`    :red:`NOT pressed`  :red:`False`
:red:`open`     :red:`NOT set`  :green:`pressed`    :red:`False`
:red:`open`     :red:`NOT set`  :red:`NOT pressed`  :red:`False`
=============== ==============  ==================  =============

I want to add a failsafe to stop the **Microwave** if it gets :green:`too hot`. It will only heat up food when the door is :green:`closed` AND the timer is :green:`set` AND the start button is :green:`pressed` and it is :red:`NOT too hot`. The inputs for the **Microwave** will then be

* is the **Microwave** door closed?
* is the timer set?
* was the start button pressed?
* is the microwave too hot?

----

*********************************************************************************
test_too_hot_w_not_set_timer_open_door_not_pressed_start
*********************************************************************************

The :ref:`truth table` when the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :red:`NOT pressed` is

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:red:`open`     :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`False`
:red:`open`     :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for ``too_hot`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_not_set_timer_open_door_not_pressed_start` for if the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :red:`NOT pressed` AND the **Microwave** temperature is :red:`NOT too hot`

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 7

        def test_not_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                    too_hot=False,
                )
            )


    # Exceptions seen

  the terminal shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: microwave() got
               an unexpected keyword argument 'too_hot'

  because the test :ref:`called<how to call a function with input>` the ``microwave`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``too_hot``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``too_hot`` to the ``microwave`` :ref:`function definition<how to make a function that takes input>` in ``microwave.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 3

  def microwave(
          closed_door=False, pressed_start=False,
          set_timer=False, too_hot=False,
      ):

the test passes.

.. code-block:: python

  microwave(
      closed_door=False, set_timer=False,
      pressed_start=False, too_hot=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :red:`NOT pressed` AND the **Microwave** temperature is :green:`too hot`, in ``test_microwave.py``

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2-9

        def test_not_set_timer_open_door_not_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                    too_hot=True,
                )
            )
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                    too_hot=False,
                )
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_not_set_timer_open_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2

        def test_not_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                    too_hot=True,
                )
            )

  the test passes.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=False,
        pressed_start=False, too_hot=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=False, too_hot=False
    ) -> False

* I change the name of the test from :ref:`test_not_set_timer_open_door_not_pressed_start` to :ref:`test_too_hot_w_not_set_timer_open_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10

        def test_not_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=False,
                    too_hot=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_too_hot_w_not_set_timer_open_door_not_pressed_start'

----

*********************************************************************************
test_too_hot_w_not_set_timer_open_door_pressed_start
*********************************************************************************

The :ref:`truth table` when the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :green:`pressed` is

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:red:`open`     :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`False`
:red:`open`     :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for ``too_hot`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_not_set_timer_open_door_pressed_start` for if the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :green:`pressed` AND the **Microwave** temperature is :red:`NOT too hot`

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 7

        def test_not_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                    too_hot=False,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_not_pressed_start(self):

  the test is still green.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=False,
        pressed_start=True, too_hot=False
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=False, too_hot=True
    ) -> False
    microwave(
        closed_door=False, set_timer=False,
        pressed_start=False, too_hot=False
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the timer is :red:`NOT set` AND the start button is :green:`pressed` AND the **Microwave** temperature is :green:`too hot`, in ``test_microwave.py``

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-9

        def test_not_set_timer_open_door_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                    too_hot=True,
                )
            )
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                    too_hot=False,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_not_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_not_set_timer_open_door_pressed_start`

.. code-block:: python
  :lineno-start: 70
  :emphasize-lines: 2

      def test_not_set_timer_open_door_pressed_start(self):
          self.assertFalse(
              src.microwave.microwave(
                  closed_door=False,
                  set_timer=False,
                  pressed_start=True,
                  too_hot=True,
              )
          )

the test passes.

.. code-block:: python

  microwave(
      closed_door=False, set_timer=False,
      pressed_start=True, too_hot=True
  ) -> False
  microwave(
      closed_door=False, set_timer=False,
      pressed_start=True, too_hot=False
  ) -> False
  microwave(
      closed_door=False, set_timer=False,
      pressed_start=False, too_hot=True
  ) -> False
  microwave(
      closed_door=False, set_timer=False,
      pressed_start=False, too_hot=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_not_set_timer_open_door_pressed_start` to :ref:`test_too_hot_w_not_set_timer_open_door_pressed_start`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10

        def test_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=False,
                    pressed_start=True,
                    too_hot=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_too_hot_w_not_set_timer_open_door_pressed_start'

----

*********************************************************************************
test_too_hot_w_set_timer_open_door_not_pressed_start
*********************************************************************************

The :ref:`truth table` when the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :red:`NOT pressed` is

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:red:`open`     :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`False`
:red:`open`     :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for ``too_hot`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_set_timer_open_door_not_pressed_start` for if the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :red:`NOT pressed` AND the **Microwave** temperature is :red:`NOT too hot`

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7

        def test_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=False,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_pressed_start(self):

  the test is still green.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=False, too_hot=False
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :red:`NOT pressed` AND the **Microwave** temperature is :green:`too hot`, in ``test_microwave.py``

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-9

        def test_set_timer_open_door_not_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=True,
                )
            )
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=False,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_set_timer_open_door_not_pressed_start`

.. code-block:: python
  :lineno-start: 52
  :emphasize-lines: 2

      def test_set_timer_open_door_not_pressed_start(self):
          self.assertFalse(
              src.microwave.microwave(
                  closed_door=False,
                  set_timer=True,
                  pressed_start=False,
                  too_hot=True,
              )
          )

the test passes.

.. code-block:: python

  microwave(
      closed_door=False, set_timer=True,
      pressed_start=False, too_hot=True
  ) -> False
  microwave(
      closed_door=False, set_timer=True,
      pressed_start=False, too_hot=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_set_timer_open_door_not_pressed_start` to :ref:`test_too_hot_w_set_timer_open_door_not_pressed_start`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10

        def test_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_too_hot_w_set_timer_open_door_not_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_too_hot_w_set_timer_open_door_not_pressed_start'

----

*********************************************************************************
test_too_hot_w_set_timer_open_door_pressed_start
*********************************************************************************

The :ref:`truth table` when the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :green:`pressed` is

=============== ==============  ==================  ==================  =============
door            timer           start button        too hot             output
=============== ==============  ==================  ==================  =============
:red:`open`     :green:`set`    :green:`pressed`    :green:`too hot`    :red:`False`
:red:`open`     :green:`set`    :green:`pressed`    :red:`NOT too hot`  :red:`False`
=============== ==============  ==================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for ``too_hot`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_set_timer_open_door_pressed_start` for if the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :green:`pressed` AND the **Microwave** temperature is :red:`NOT too hot`

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :green:`set`    :green:`pressed`    :red:`NOT too hot`  :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

        def test_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=True,
                    too_hot=False,
                )
            )

        def test_too_hot_w_set_timer_open_door_not_pressed_start

  the test is still green.

  .. code-block:: python

    microwave(
        closed_door=False, set_timer=True,
        pressed_start=False, too_hot=True
    ) -> False
    microwave(
        closed_door=False, set_timer=True,
        pressed_start=False, too_hot=False
    ) -> False
    microwave(
        closed_door=False, set_timer=True,
        pressed_start=False, too_hot=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the **Microwave** door is :red:`open` AND the timer is :green:`set` AND the start button is :green:`pressed` AND the **Microwave** temperature is :green:`too hot`, in ``test_microwave.py``

  =============== ==============  ==================  ==================  =============
  door            timer           start button        too hot             output
  =============== ==============  ==================  ==================  =============
  :red:`open`     :green:`set`    :green:`pressed`    :green:`too hot`    :red:`False`
  =============== ==============  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-9

        def test_set_timer_open_door_pressed_start(self):
            self.assertTrue(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=True,
                )
            )
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=False,
                )
            )

        def test_too_hot_w_not_set_timer_open_door_pressed_start(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_set_timer_open_door_pressed_start`

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 2

      def test_set_timer_open_door_pressed_start(self):
          self.assertFalse(
              src.microwave.microwave(
                  closed_door=False,
                  set_timer=True,
                  pressed_start=False,
                  too_hot=True,
              )
          )

the test passes.

.. code-block:: python

  microwave(
      closed_door=False, set_timer=True,
      pressed_start=False, too_hot=True
  ) -> False
  microwave(
      closed_door=False, set_timer=True,
      pressed_start=False, too_hot=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_set_timer_open_door_pressed_start` to :ref:`test_too_hot_w_set_timer_open_door_pressed_start`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10

        def test_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=True,
                )
            )

        def test_too_hot_w_set_timer_open_door_pressed_start(self):
            self.assertFalse(
                src.microwave.microwave(
                    closed_door=False,
                    set_timer=True,
                    pressed_start=False,
                    too_hot=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_too_hot_w_set_timer_open_door_pressed_start'

----BOOM----


* I add a value for the ``too_hot`` parameter in the next :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :red:`open` AND the timer is :green:`set`, the start button is :red:`NOT pressed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`open`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
  :red:`open`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  :red:`open`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 24

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green.

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :red:`open` AND the timer is :green:`set`, the start button is :red:`NOT pressed` and the microwave temperature is  :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`open`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
  :red:`open`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  :red:`open`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  :red:`open`  :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 28-34

        def test_open_door_timer_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_open_door_timer_not_set(self):

  green.

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
                set_timer=True,
                start_is_pressed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

  still green.

* I remove the ``reality`` :ref:`variables<what is a variable?>`, I do not need them because they are called only once in every :ref:`assertion<what is an assertion?>`, I can call the ``microwave`` :ref:`function<what is a function?>` directly without the middle man

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 11-20, 29-38, 47-56, 65-74

        def test_too_hot_open_door_timer_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=True,
                start_is_pressed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=False,
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
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_open_door_timer_not_set(self):

----

*********************************************************************************
test_too_hot_open_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the **Microwave** door is :red:`open` and the timer is :red:`NOT set` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`open`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
:red:`open`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
:red:`open`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:red:`open`  :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_open_door_timer_not_set` for when the **Microwave** door is :red:`open` AND the timer is :red:`NOT set`, the start button is :green:`pressed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`open`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green.

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :red:`open` AND the timer is :red:`NOT set`, the start button is :green:`pressed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`open`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  :red:`open`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-18

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green.

* I add a value for ``too_hot`` to the next :ref:`assertion<what is an assertion?>`, for when the **Microwave** door is :red:`open` AND the timer is :red:`NOT set`, the start button is :red:`NOT pressed` and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`open`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  :red:`open`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  :red:`open`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 24

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

  still green.

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :red:`open` AND the timer is :red:`NOT set`, the start button is :red:`NOT pressed` and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :red:`open`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  :red:`open`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  :red:`open`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  :red:`open`  :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 28-34

        def test_open_door_timer_not_set(self):
            my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_closed_door_timer_set(self):

  green.

* I change the name of the test from :ref:`test_open_door_timer_not_set` to :ref:`test_too_hot_open_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=True,
                    start_is_pressed=False,
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
                set_timer=False,
                start_is_pressed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

        def test_closed_door_timer_set(self):

  still green.

* I call the ``microwave`` :ref:`function<what is a function?>` directly in the :ref:`assertions<what is an assertion?>` because I only use the ``reality`` :ref:`variable<what is a variable?>` once for each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 11-19, 28-36, 45-53, 62-70

        def test_too_hot_open_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=True,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=True,
                set_timer=False,
                start_is_pressed=False,
                too_hot=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_closed_door_timer_set(self):

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 51

        def test_too_hot_open_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_closed_door_timer_set(self):

----

*********************************************************************************
test_too_hot_closed_door_timer_set
*********************************************************************************

The :ref:`truth table` for when the **Microwave** door is :green:`closed` and the timer is :green:`set` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`closed`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
:green:`closed`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :green:`HEATING`
:green:`closed`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:green:`closed`  :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I use the ``OFF`` :ref:`global variable<what is a variable?>` for ``my_expectation`` when the value is :red:`'OFF'` in :ref:`test_closed_door_timer_set`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 10, 17-18

        def test_closed_door_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=True,
                start_is_pressed=True,
            )
            self.assertEqual(reality, my_expectation)

            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

        def test_closed_door_timer_not_set(self):

  the test is still green.

* I call the ``microwave`` :ref:`function<what is a function?>` directly without the ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 8-15, 25-32

        def test_closed_door_timer_set(self):
            my_expectation = 'HEATING'
            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=True,
                start_is_pressed=True,
            )
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                ),
                'HEATING'
            )

            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  still green.

* I remove the commented lines and :ref:`variables<what is a variable?>` that are not used anymore

  .. code-block:: python
    :lineno-start: 92

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :green:`closed` AND the timer is :green:`set`, the start button is :green:`pressed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-10

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'HEATING' != 'OFF'

  because the ``microwave`` :ref:`function<what is a function?>` returned :green:`'HEATING'` and the :ref:`assertion<what is an assertion?>` expects :red:`'OFF'`

* I add an :ref:`if statement<if statements>` to the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def microwave(
            door_is_open, start_is_pressed,
            set_timer=False, too_hot=False,
        ):
        if too_hot == True:
            return 'OFF'

        if not set_timer:
            return 'OFF'

        if door_is_open or not start_is_pressed:
            return 'OFF'
        else:
            return 'HEATING'

  the test passes.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

        # if too_hot == True:
        if too_hot:
            return 'OFF'

  the test is still green, because ``if something == True`` is the same as ``if something``

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the :ref:`if statement<if statements>` for when the microwave temperature is :green:`too hot` and the :ref:`if statement<if statements>` for when the timer is :red:`NOT set`, because they both return :red:`'OFF'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7, 9-10

    def microwave(
            door_is_open, start_is_pressed,
            set_timer=False, too_hot=False,
        ):
        # if too_hot == True:
        # if too_hot:
        #     return 'OFF'

        # if not set_timer:
        if too_hot or not set_timer:
            return 'OFF'

        if door_is_open or not start_is_pressed:
            return 'OFF'
        else:
            return 'HEATING'

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def microwave(
            door_is_open, start_is_pressed,
            set_timer=False, too_hot=False,
        ):
        if too_hot or not set_timer:
            return 'OFF'

        if door_is_open or not start_is_pressed:
            return 'OFF'
        else:
            return 'HEATING'

  this is what happens when the ``microwave`` :ref:`function<what is a function?>` is called

  - it returns :red:`'OFF'` if the microwave temperature is :green:`too hot` OR the timer is :red:`NOT set`, this means

    * it returns :red:`'OFF'` if the microwave temperature is :green:`too hot`
    * it returns :red:`'OFF'` if the timer is :red:`NOT set`

  - if the above :ref:`condition<if statements>` is NOT met

    * it returns :red:`'OFF'` if the **Microwave** door is :red:`open` OR if the start button is :red:`NOT pressed`, this means

      - it returns :red:`'OFF'` if the **Microwave** door is :red:`open`
      - it returns :red:`'OFF'` if the start button is :red:`NOT pressed`

    * it returns :green:`'HEATING'` if the **Microwave** door is :green:`closed` AND the start button is :green:`closed`

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :green:`closed` AND the timer is :green:`set`, the start button is :green:`pressed` and the microwave temperature is :red:`NOT too hot` in :ref:`test_closed_door_timer_set` in ``test_microwave.py``

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
  :green:`closed`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :green:`HEATING`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 17

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  the test is still green.

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the **Microwave** door is :green:`closed` AND the timer is :green:`set`, the start button is :red:`NOT pressed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
  :green:`closed`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :green:`HEATING`
  :green:`closed`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 27

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :green:`closed` AND the timer is :green:`set`, the start button is :red:`NOT pressed`, and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
  :green:`closed`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :green:`HEATING`
  :green:`closed`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  :green:`closed`  :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 32-40

        def test_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                'HEATING'
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_closed_door_timer_not_set(self):

  still green.

* I change the name of the test from :ref:`test_closed_door_timer_set` to :ref:`test_too_hot_closed_door_timer_set`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=True,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_closed_door_timer_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=True,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

----

*********************************************************************************
test_too_hot_closed_door_timer_not_set
*********************************************************************************

The :ref:`truth table` for when the **Microwave** door is :green:`closed` and the timer is :red:`NOT set` is

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`closed`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
:green:`closed`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
:green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

* I use the ``OFF`` :ref:`global variable<what is a variable?>` to remove repetition from :ref:`test_closed_door_timer_not_set`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 2, 9-10, 17-18

        def test_closed_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)

            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green.

* I call the ``microwave`` :ref:`function<what is a function?>` directly in the :ref:`assertion<what is an assertion?>`, I do not need the ``reality`` :ref:`variables<what is a variable?>` because they are only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 10-17, 25-32

        def test_closed_door_timer_not_set(self):
            # my_expectation = 'OFF'

            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.microwave.microwave(
                door_is_open=False,
                set_timer=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=False,
                ),
                OFF
            )


    # Exceptions seen

* I remove the commented lines and :ref:`variables<what is a variable?>` that are not used

  .. code-block:: python
    :lineno-start: 133

        def test_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=False,
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
                    set_timer=True,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                ),
                OFF
            )

* I add a value for the ``too_hot`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_too_hot_closed_door_timer_not_set`, for when the **Microwave** door is :green:`closed` AND the timer is :red:`NOT set`, the start button is :green:`pressed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :green:`closed` AND the timer is :red:`NOT set`, the start button is :green:`pressed`, and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 12-20

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=False,
                ),
                OFF
            )


    # Exceptions seen

  still green.

* I add a value for the ``too_hot`` parameter to the next :ref:`assertion<what is an assertion?>`, for when the **Microwave** door is :green:`closed` AND the timer is :red:`NOT set`, the start button is :red:`NOT pressed`, and the microwave temperature is :green:`too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  :green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 27

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )


    # Exceptions seen

  green.

* I add an :ref:`assertion<what is an assertion?>` for when the **Microwave** door is :green:`closed` AND the timer is :red:`NOT set`, the start button is :red:`NOT pressed`, and the microwave temperature is :red:`NOT too hot`

  =============  ==============  =================  ==================  ================
  door           timer           start button       too hot             output
  =============  ==============  =================  ==================  ================
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
  :green:`closed`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
  :green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
  :green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
  =============  ==============  =================  ==================  ================

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 32-40

        def test_too_hot_closed_door_timer_not_set(self):
            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=True,
                    too_hot=False,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=True,
                ),
                OFF
            )

            self.assertEqual(
                src.microwave.microwave(
                    door_is_open=False,
                    set_timer=False,
                    start_is_pressed=False,
                    too_hot=False,
                ),
                OFF
            )


    # Exceptions seen

  all the tests are still green.

* The :ref:`condition<if statements>` of the ``microwave`` :ref:`function<what is a function?>` in ``microwave.py`` can be written with :ref:`Logical Conjunction (AND)<test_logical_conjunction>` for the one case where it returns :green:`'HEATING'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-10

    def microwave(
            door_is_open, start_is_pressed,
            set_timer=False, too_hot=False,
        ):
        if (
            not door_is_open
            and start_is_pressed
            and set_timer
            and not too_hot
        ):
            return 'HEATING'

        return 'OFF'

  or it could be written with the negative cases first

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5, 7-14

    def microwave(
            door_is_open, start_is_pressed,
            set_timer=False, too_hot=False,
        ):
        off = 'OFF'

        if too_hot:
            return off
        if not set_timer:
            return off
        if not start_is_pressed:
            return off
        if door_is_open:
            return off

        return 'HEATING'

  or it could be written with :ref:`Logical Disjunction (OR)<test_logical_disjunction>` for all the cases that return :red:`'OFF'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-10

    def microwave(
            door_is_open, start_is_pressed,
            set_timer=False, too_hot=False,
        ):
        if (
            too_hot
            or not set_timer
            or not start_is_pressed
            or door_is_open
        ):
            return 'OFF'

        return 'HEATING'

  which do you like better?

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_microwave.py`` and ``microwave.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for a Microwave with these inputs:

* is the **Microwave** door closed?
* is the timer set?
* was the start button pressed?
* is the microwave too hot?

the inputs gave me this :ref:`truth table`

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`open`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
:red:`open`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
:red:`open`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:red:`open`  :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:red:`open`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
:red:`open`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
:red:`open`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:red:`open`  :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`closed`  :green:`set`    :green:`pressed`    :green:`too hot`    :red:`OFF`
:green:`closed`  :green:`set`    :green:`pressed`    :red:`NOT too hot`  :green:`HEATING`
:green:`closed`  :green:`set`    :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:green:`closed`  :green:`set`    :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

=============  ==============  =================  ==================  ================
door           timer           start button       too hot             output
=============  ==============  =================  ==================  ================
:green:`closed`  :red:`NOT set`  :green:`pressed`    :green:`too hot`    :red:`OFF`
:green:`closed`  :red:`NOT set`  :green:`pressed`    :red:`NOT too hot`  :red:`OFF`
:green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :green:`too hot`    :red:`OFF`
:green:`closed`  :red:`NOT set`  :red:`NOT pressed`  :red:`NOT too hot`  :red:`OFF`
=============  ==============  =================  ==================  ================

the only time this Microwave heats food is when the **Microwave** door is :green:`closed` AND the timer is :green:`set`, the start button is :green:`pressed` and the microwave temperature is :red:`NOT too hot`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Microwave: tests and solutions>`

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

:ref:`Would you like to test making a Car starter?<car>`

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