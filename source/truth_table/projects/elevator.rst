:orphan:

.. meta::
  :description: Build a safety-critical elevator control system from scratch using Python and Test Driven Development (TDD). This project-based tutorial teaches beginners how to manage multiple boolean inputs—including door sensors, floor requests, weight limits, and emergency stop buttons—to create robust, failsafe logic. Master the professional Red-Green-Refactor cycle using modern tools like uv, unittest, and pytest-watcher.
  :keywords: Jacob Itegboje, Python elevator logic project, safety-critical systems tutorial, TDD for beginners, building failsafes in Python, multiple boolean conditions example, elevator simulation code, Python unittest tutorial, uv package manager guide, pytest-watcher automated testing, Red Green Refactor Python project, debugging NameError and TypeError, logical conjunction tutorial, translating truth tables to code, weight limit failsafe logic, emergency stop button code, software engineering projects for beginners, Python boolean logic practice, building a controller in Python, robust software development

.. include:: ../../links.rst

.. _elevator:

#################################################################################
Elevator
#################################################################################

I want to make an **Elevator Controller** that will :green:`MOVE` to a floor when I push a button for the floor.

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :linenos:
  :caption: truth_table/tests/test_elevator.py
  :lines: 1-23

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 25
  :caption: truth_table/tests/test_elevator.py
  :lines: 25-41

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 43
  :caption: truth_table/tests/test_elevator.py
  :lines: 43-59

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 61
  :caption: truth_table/tests/test_elevator.py
  :lines: 61-77

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 79
  :caption: truth_table/tests/test_elevator.py
  :lines: 79-95

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 97
  :caption: truth_table/tests/test_elevator.py
  :lines: 97-113

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 115
  :caption: truth_table/tests/test_elevator.py
  :lines: 115-131

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :lineno-start: 133
  :caption: truth_table/tests/test_elevator.py
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

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``

* I name this project ``controller``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I change the name of the project to ``controller`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/elevator/make_tdd/makePythonTddElevator.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 5, 12, 20

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``controller`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I change the name of the project to ``controller`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/elevator/make_tdd/makePythonTddElevator.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 4, 11, 19

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``controller`` project

        .. code-block:: python
          :emphasize-lines: 1

          .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES =========================
    ______________ TestElevator.test_failure __________________

    self = <tests.test_elevator.TestElevator testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_elevator.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_elevator.py::TestElevator::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_elevator.py:7`` to open it
* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>` in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestElevator(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertTrue(True)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then `change directory`_ to ``controller``

  .. code-block:: python
    :emphasize-lines: 1

    cd elevator

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

----

I want the **Elevator** to :green:`MOVE` only when the button for a floor is :green:`pushed`. I get this :ref:`truth table`

==================  =============
floor button        output
==================  =============
:green:`pushed`     :green:`True`
:red:`NOT pushed`   :red:`False`
==================  =============

Where :green:`True` means the **Elevator** will :green:`MOVE` up or down to the floor number that is :green:`pushed`, and :red:`False` means it does :red:`NOT MOVE`.

----

*********************************************************************************
test_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change :ref:`test_failure` to :ref:`test_number_pushed` with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :green:`pushed`

  ==================  =============
  floor button        output
  ==================  =============
  :green:`pushed`     :green:`True`
  ==================  =============

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-8

    class TestElevator(unittest.TestCase):

        def test_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
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

    import src.elevator
    import unittest


    class TestElevator(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.elevator'
                    has no attribute 'elevator'

  because ``elevator.py`` in the ``src`` folder_ does not have anything named ``controller`` in it.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``elevator.py`` from the ``src`` folder_

* I delete all the text in the file_ then add a :ref:`function<what is a function?>` named ``controller`` to ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def controller():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: elevator() got
               an unexpected keyword argument 'number_pushed'

  because the test :ref:`called<how to call a function with input>` the ``controller`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``number_pushed``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add ``number_pushed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def controller(number_pushed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  the ``controller`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I change the :ref:`return statement<the return statement>` to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def controller(number_pushed):
        return True

  the test passes. The ``controller`` :ref:`function<what is a function?>` always returns :green:`True`, it does not care about the inputs. Is this :ref:`Tautology?<test_tautology>`

  .. code-block:: python

    elevator(number_pushed=True ) -> True

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_number_pushed'

----

*********************************************************************************
test_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :red:`NOT pushed`

  ==================  =============
  floor button        output
  ==================  =============
  :red:`NOT pushed`   :red:`False`
  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-13

        def test_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                )
            )

        def test_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``controller`` :ref:`function<what is a function?>` always returns :green:`True` and this :ref:`assertion<what is an assertion?>` expects :red:`False`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I make the :ref:`function<what is a function?>` return its input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def controller(number_pushed):
        return number_pushed

  the test passes.

  .. code-block:: python

    elevator(number_pushed=True ) -> True
    elevator(number_pushed=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_number_not_pushed'

I want the **Elevator** to :green:`MOVE` only when the button for a floor is :green:`pushed` AND the doors are :green:`closed`. I do not want anything or anyone falling out of the **Elevator** while it is :green:`MOVING`. The inputs to the **Elevator Controller** will then be

* was the number for a floor pushed?
* are the doors closed?

Which gives me this :ref:`truth table`

=================  ==================  =============
floor button       doors               output
=================  ==================  =============
:green:`pushed`    :green:`closed`     :green:`True`
:green:`pushed`    :red:`open`         :red:`False`
:red:`NOT pushed`  :green:`closed`     :red:`False`
:red:`NOT pushed`  :red:`open`         :red:`False`
=================  ==================  =============

----

*********************************************************************************
test_doors_closed_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add ``doors_closed`` with a value to the :ref:`call<how to call a function with input>` to the ``controller`` :ref:`function<what is a function?>` from :ref:`test_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed`

  =================  ==================  =============
  floor button       doors               output
  =================  ==================  =============
  :green:`pushed`    :green:`closed`     :green:`True`
  =================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                )
            )

        def test_number_not_pushed(self):

  .. code-block:: python

    TypeError: elevator() got
               an unexpected keyword argument 'doors_closed'

  because the test :ref:`called<how to call a function with input>` the ``controller`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``doors_closed``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``doors_closed`` to the :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def controller(number_pushed, doors_closed):
        return number_pushed

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: elevator() missing
               1 required positional argument: 'doors_closed'

  because the :ref:`assertion<what is an assertion?>` in :ref:`test_number_not_pushed` :ref:`calls<how to call a function with input>` the ``controller`` :ref:`function<what is a function?>` with one argument (``number_pushed``) and I just changed the :ref:`function<what is a function?>` to make it take two required arguments (``number_pushed`` and ``doors_closed``). I have to make ``doors_closed`` a :ref:`choice<test_optional_arguments>`.

* I add a :ref:`default value<test_optional_arguments>` for ``doors_closed`` to make it a :ref:`choice<test_optional_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def controller(number_pushed, doors_closed=False):
        return number_pushed

  the test passes.

  .. code-block:: python

    elevator(number_pushed=True , doors_closed=True ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of :ref:`test_number_pushed` to :ref:`test_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_doors_closed_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_doors_closed_number_pushed'

----

*********************************************************************************
test_doors_open_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test named :ref:`test_doors_open_number_pushed` with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open`

  =================  ==================  =============
  floor button       doors               output
  =================  ==================  =============
  :green:`pushed`    :red:`open`         :red:`False`
  =================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-15

        def test_doors_closed_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                )
            )

        def test_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                )
            )

        def test_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``controller`` :ref:`function<what is a function?>` returns the value of the ``number_pushed`` parameter.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to the ``controller`` :ref:`function<what is a function?>` in ``elevator.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def controller(number_pushed, doors_closed=False):
      if not doors_closed:
          return False
      return number_pushed

the test passes.

.. code-block:: python

  elevator(number_pushed=True , doors_closed=True ) -> True
  elevator(number_pushed=True , doors_closed=False) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the **Elevator** to only check if the doors are :green:`closed` if the button for a floor is :green:`pushed`. I change the :ref:`if statement<if statements>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3, 5-6

    def controller(number_pushed, doors_closed=False):
        # if not doors_closed:
        if not number_pushed:
            return False
        # return number_pushed
        return doors_closed

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def controller(number_pushed, doors_closed=False):
        if not number_pushed:
            return False
        return doors_closed

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_doors_open_number_pushed'

If the button for a floor is :green:`pushed`, the **Elevator** only :green:`MOVES` when the doors are :green:`closed`.

----

*********************************************************************************
test_doors_closed_number_not_pushed
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add ``doors_closed`` with a value to the :ref:`call<how to call a function with input>` to the ``controller`` :ref:`function<what is a function?>` from :ref:`test_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed`

  =================  ==================  =============
  floor button       doors               output
  =================  ==================  =============
  :red:`NOT pushed`  :green:`closed`     :red:`False`
  =================  ==================  =============

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                )
            )


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    elevator(number_pushed=True , doors_closed=True ) -> True
    elevator(number_pushed=True , doors_closed=False) -> False
    elevator(number_pushed=False, doors_closed=True ) -> False

* I change the name of :ref:`test_number_not_pushed` to :ref:`test_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9

        def test_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                )
            )

        def test_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                )
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_doors_closed_number_not_pushed'

----

*********************************************************************************
test_doors_open_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add :ref:`test_doors_open_number_not_pushed` with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open`, in ``test_elevator.py``

  =================  ==================  =============
  floor button       doors               output
  =================  ==================  =============
  :red:`NOT pushed`  :red:`open`         :red:`False`
  =================  ==================  =============

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 9-15

        def test_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                )
            )

        def test_doors_open_number_not_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
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

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_doors_open_number_not_pushed`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2

        def test_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                )
            )


    # Exceptions seen

  the test passes.

  .. code-block:: python

    elevator(number_pushed=True , doors_closed=True ) -> True
    elevator(number_pushed=True , doors_closed=False) -> False
    elevator(number_pushed=False, doors_closed=True ) -> False
    elevator(number_pushed=False, doors_closed=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_doors_open_number_not_pushed'

When the ``controller`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`, it checks if the button for a floor is :red:`NOT pushed`

* If the button for a floor is :red:`NOT pushed` it returns :red:`False`

  .. code-block:: shell

    elevator(number_pushed=False, doors_closed=False) -> False
    └── def controller(number_pushed, doors_closed=False):
        └── if not number_pushed:
            └── return False
            return doors_closed

  .. code-block:: shell

    elevator(number_pushed=False, doors_closed=True ) -> False
    └── def controller(number_pushed, doors_closed=False):
        └── if not number_pushed:
            └── return False
            return doors_closed

* If the button for a floor is :green:`pushed` it returns the value of ``doors_closed``

  - if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open`, it returns :red:`False`

    .. code-block:: shell

      elevator(number_pushed=False, doors_closed=True ) -> False
      └── def controller(number_pushed, doors_closed=False):
          ├── if not number_pushed:
          │      return False
          └── return doors_closed
              return False

  - if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed`, it returns :green:`True`

    .. code-block:: shell

      elevator(number_pushed=True , doors_closed=True ) -> True
      └── def controller(number_pushed, doors_closed=False):
          ├── if not number_pushed:
          │      return False
          └── return doors_closed
              return True

So far, the :ref:`truth table` for the **Elevator** is

=================  ==================  =============
floor button       doors               output
=================  ==================  =============
:green:`pushed`    :green:`closed`     :green:`True`
:green:`pushed`    :red:`open`         :red:`False`
:red:`NOT pushed`  :green:`closed`     :red:`False`
:red:`NOT pushed`  :red:`open`         :red:`False`
=================  ==================  =============

I want to add a failsafe to the **Elevator Controller** so it will :red:`NOT MOVE` if the total weight of the **Elevator** when occupied is :green:`above` a certain number, the inputs to the Controller will then be

* was the number for a floor pushed?
* are the doors closed?
* is the **Elevator** above the weight limit?

Which gives me this :ref:`truth table`

=================  ===============  ============== =============
floor button       doors            weight limit   output
=================  ===============  ============== =============
:green:`pushed`    :green:`closed`  :green:`above` :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :green:`True`
:green:`pushed`    :red:`open`      :green:`above` :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :red:`False`
=================  ===============  ============== =============

=================  ===============  ============== =============
floor button       doors            weight limit   output
=================  ===============  ============== =============
:red:`NOT pushed`  :green:`closed`  :green:`above` :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`False`
:red:`NOT pushed`  :red:`open`      :green:`above` :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :red:`False`
=================  ===============  ============== =============

----

*********************************************************************************
test_above_weight_doors_open_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add ``above_weight`` to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from :ref:`test_doors_open_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :red:`NOT pushed`  :red:`open`      :green:`above` :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 5

        def test_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: elevator() got
               an unexpected keyword argument 'above_weight'

  because the test :ref:`called<how to call a function with input>` the ``controller`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``above_weight``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``above_weight`` to the :ref:`function signature<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def controller(
        number_pushed, doors_closed=False,
        above_weight,
    ):
        if not number_pushed:
            return False
        return doors_closed

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a :ref:`default value<test_optional_arguments>` to make ``above_weight`` a choice, in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False,
    ):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True
    ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_doors_open_number_not_pushed` to :ref:`test_above_weight_doors_open_number_not_pushed`, in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 9

        def test_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                )
            )

        def test_above_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_weight_doors_open_number_not_pushed'

----

*********************************************************************************
test_below_weight_doors_open_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 10-17

        def test_above_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                )
            )

        def test_below_weight_doors_open_number_not_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the ``controller`` :ref:`function<what is a function?>` returned :red:`False` and this :ref:`assertion<what is an assertion?>` expects :green:`True`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_open_number_not_pushed`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 2

        def test_below_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=False,
                )
            )


    # Exceptions seen

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_weight_doors_open_number_not_pushed'

----

*********************************************************************************
test_above_weight_doors_closed_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``above_weight`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from :ref:`test_doors_closed_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :red:`NOT pushed`  :green:`closed`  :green:`above` :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

        def test_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                )
            )

        def test_above_weight_doors_open_number_not_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False
    ) -> False

* I change the name of the test from :ref:`test_doors_closed_number_not_pushed` to :ref:`test_above_weight_doors_closed_number_not_pushed`, in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 9

        def test_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_weight_doors_closed_number_not_pushed'

----

*********************************************************************************
test_below_weight_doors_closed_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 10-17

        def test_above_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                )
            )

        def test_below_weight_doors_closed_number_not_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                )
            )

        def test_above_weight_doors_open_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

        def test_below_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                )
            )

        def test_above_weight_doors_open_number_not_pushed(self):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=False
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_weight_doors_closed_number_not_pushed'

----

*********************************************************************************
test_above_weight_doors_open_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``above_weight`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from :ref:`test_doors_open_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :green:`pushed`    :red:`open`      :green:`above` :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6

        def test_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True
    ) -> False

* I change the name of the test from :ref:`test_doors_open_number_pushed` to :ref:`test_above_weight_doors_open_number_pushed`, in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9

        def test_doors_closed_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_weight_doors_open_number_pushed'

----

*********************************************************************************
test_below_weight_doors_open_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :green:`pushed`    :red:`open`      :red:`below`   :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 10-17

        def test_above_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                )
            )

        def test_below_weight_doors_open_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the ``controller`` :ref:`function<what is a function?>` returns :red:`False` and this :ref:`assertion<what is an assertion?>` expects :green:`True`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 2

        def test_below_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=False
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_weight_doors_open_number_pushed'

----

*********************************************************************************
test_above_weight_doors_closed_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``above_weight`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from :ref:`test_doors_closed_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :green:`pushed`    :green:`closed`  :green:`above` :red:`False`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_doors_closed_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the test is still green.

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

* I add an :ref:`if statement<if statements>` for ``above_weight`` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False,
    ):
        if not number_pushed:
            return False
        if above_weight:
            return False
        return doors_closed

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=False
    ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_doors_closed_number_pushed` to :ref:`test_above_weight_doors_closed_number_pushed`, in ``test_elevator.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_above_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_weight_doors_closed_number_pushed'

----

*********************************************************************************
test_below_weight_doors_closed_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a test with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` the **Elevator** is :red:`below` the weight limit

  =================  ===============  ============== =============
  floor button       doors            weight limit   output
  =================  ===============  ============== =============
  :green:`pushed`    :green:`closed`  :red:`below`   :green:`True`
  =================  ===============  ============== =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-17

        def test_above_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                )
            )

        def test_below_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``controller`` :ref:`function<what is a function?>` returns :green:`True` and this :ref:`assertion<what is an assertion?>` expects :red:`False`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>` in :ref:`test_below_weight_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 2

        def test_below_weight_doors_closed_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=False
    ) -> True
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True
    ) -> False
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=False
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_weight_doors_closed_number_pushed'

When the ``controller`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`, it checks if the button for a floor is :red:`NOT pushed`

* If the button for a floor is :red:`NOT pushed` it returns :red:`False`

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            return doors_closed

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=False
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            return doors_closed

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            return doors_closed

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            return doors_closed

* If the button for a floor is :green:`pushed` it checks if the total weight of the **Elevator** is :green:`above` the weight limit

  - if the total weight of the **Elevator** is :green:`above` the weight limit, it returns :red:`False`

    .. code-block:: shell

      elevator(
          number_pushed=True, doors_closed=True,
          above_weight=True
      ) -> False
      └── def controller(
              number_pushed, doors_closed=False,
              above_weight=False,
          ):
          ├── if not number_pushed:
          │       return False
          └── if above_weight:
              └── return False
              return doors_closed

    .. code-block:: shell

      elevator(
          number_pushed=True, doors_closed=False,
          above_weight=True
      ) -> False
      └── def controller(
              number_pushed, doors_closed=False,
              above_weight=False,
          ):
          ├── if not number_pushed:
          │       return False
          └── if above_weight:
              └── return False
              return doors_closed

  - if the total weight of the **Elevator** is :red:`below` the weight limit, it returns the value of ``doors_closed``

    - if the button for a floor is :green:`pushed` AND the total weight of the **Elevator** is :red:`below` the weight limit AND the **Elevator** doors are :red:`open`, it returns :red:`False`

      .. code-block:: shell

        elevator(
            number_pushed=True, doors_closed=False,
            above_weight=False
        ) -> False
        └── def controller(
                number_pushed, doors_closed=False,
                above_weight=False,
            ):
            ├── if not number_pushed:
            │       return False
            ├── if above_weight:
            │       return False
            └── return doors_closed
                return False

    - if the button for a floor is :green:`pushed` AND the total weight of the **Elevator** is :red:`below` the weight limit AND the **Elevator** doors are :green:`closed`, it returns :green:`True`

      .. code-block:: shell

        elevator(
            number_pushed=True, doors_closed=True,
            above_weight=False
        ) -> True
        └── def controller(
                number_pushed, doors_closed=False,
                above_weight=False,
            ):
            ├── if not number_pushed:
            │       return False
            ├── if above_weight:
            │       return False
            └── return doors_closed
                return True

The :ref:`truth table` for the **Elevator** is

=================  ===============  ============== =============
floor button       doors            weight limit   output
=================  ===============  ============== =============
:green:`pushed`    :green:`closed`  :green:`above` :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :green:`True`
:green:`pushed`    :red:`open`      :green:`above` :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :red:`False`
=================  ===============  ============== =============

=================  ===============  ============== =============
floor button       doors            weight limit   output
=================  ===============  ============== =============
:red:`NOT pushed`  :green:`closed`  :green:`above` :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`False`
:red:`NOT pushed`  :red:`open`      :green:`above` :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :red:`False`
=================  ===============  ============== =============

I want to make sure the **Elevator** can be stopped with a button in an emergency. The inputs to the Controller will then be

* was the number for a floor pushed?
* are the doors closed?
* is the **Elevator** above the weight limit?
* was the emergency button pushed?

----

*********************************************************************************
test_emergency_w_above_weight_doors_closed_number_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
:green:`pushed`    :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add ``emergency`` to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_above_weight_doors_closed_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7

        def test_above_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                    emergency=True,
                )
            )

        def test_below_weight_doors_closed_number_pushed(self):

  the terminal shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: elevator() got
               an unexpected keyword argument 'emergency'

  because the test :ref:`called<how to call a function with input>` the ``controller`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``emergency``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``emergency`` to the ``controller`` :ref:`function signature<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, elevator,
    ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a :ref:`default value<test_optional_arguments>` for the ``emergency`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, elevator=False,
    ):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_above_weight_doors_closed_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-17

        def test_above_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_below_weight_doors_closed_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the :ref:`function<what is a function?>` returns :red:`False` and this :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_above_weight_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10

          def test_above_weight_doors_closed_number_pushed(self):
              self.assertFalse(
                  src.elevator.controller(
                      number_pushed=True,
                      doors_closed=True,
                      above_weight=True,
                      emergency=True,
                  )
              )
              self.assertFalse(
                  src.elevator.controller(
                      number_pushed=True,
                      doors_closed=True,
                      above_weight=True,
                      emergency=False,
                  )
              )

          def test_below_weight_doors_closed_number_pushed(self):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=False,
    ) -> False

* I change the name of the test from :ref:`test_above_weight_doors_closed_number_pushed` to :ref:`test_emergency_w_above_weight_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_emergency_w_above_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_above_weight_doors_closed_number_pushed'

----

*********************************************************************************
test_emergency_w_below_weight_doors_closed_number_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :red:`NOT pushed`  :green:`True`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_below_weight_doors_closed_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

        def test_below_weight_doors_closed_number_pushed(self):
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the test is still green.

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

        def test_below_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` for the ``emergency`` parameter to the :ref:`function definition<how to make a function that takes input>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-10

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, emergency=False,
    ):
        if not number_pushed:
            return False
        if above_weight:
            return False
        if emergency:
            return False
        return doors_closed

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=False,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=False, emergency=True,
    ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the :ref:`function<what is a function?>` to check if the **Elevator** doors are :green:`closed` before it checks if the emergency button is :green:`pushed`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 9-10, 12-15

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, emergency=False,
    ):
        if not number_pushed:
            return False
        if above_weight:
            return False
        # if emergency:
        if not doors_closed:
            return False
        # return doors_closed
        if emergency:
            return False
        return True

* I remove the commented lines from :ref:`test_below_weight_doors_closed_number_pushed`

  .. code-block:: python
    :linenos:

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, emergency=False,
    ):
        if not number_pushed:
            return False
        if above_weight:
            return False
        if not doors_closed:
            return False
        if emergency:
            return False
        return True

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_below_weight_doors_closed_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :green:`closed`  :red:`below`   :red:`NOT pushed`  :green:`True`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-17

        def test_below_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` returns :green:`True` and this :ref:`assertion<what is an assertion?>` expects :red:`False`.

* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>` in :ref:`test_below_weight_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10

        def test_below_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_above_weight_doors_open_number_pushed(self):

  the test passes.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=True, emergency=False,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=False, emergency=True,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=True,
        above_weight=False, emergency=False,
    ) -> True

* I change the name of the test from :ref:`test_below_weight_doors_closed_number_pushed` to :ref:`test_emergency_w_below_weight_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10

            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_emergency_w_below_weight_doors_closed_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_below_weight_doors_closed_number_pushed'

----

*********************************************************************************
test_emergency_w_above_weight_doors_open_number_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :red:`open`      :green:`above` :green:`pushed`    :red:`False`
:green:`pushed`    :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_above_weight_doors_open_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :red:`open`      :green:`above` :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

        def test_above_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                    emergency=True,
                )
            )

        def test_below_weight_doors_open_number_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True, emergency=True,
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_above_weight_doors_open_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10-17

        def test_above_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_below_weight_doors_open_number_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_above_weight_doors_open_number_pushed`

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 10

      def test_above_weight_doors_open_number_pushed(self):
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=True,
                  doors_closed=False,
                  above_weight=True,
                  emergency=True,
              )
          )
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=True,
                  doors_closed=False,
                  above_weight=True,
                  emergency=False,
              )
          )

      def test_below_weight_doors_open_number_pushed(self):

the test passes.

.. code-block:: python

  elevator(
      number_pushed=True, doors_closed=False,
      above_weight=True, emergency=True,
  ) -> False
  elevator(
      number_pushed=True, doors_closed=False,
      above_weight=True, emergency=False,
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_above_weight_doors_open_number_pushed` to :ref:`test_emergency_w_above_weight_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10

            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=True,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_emergency_w_above_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_above_weight_doors_open_number_pushed'

----

*********************************************************************************
test_emergency_w_below_weight_doors_open_number_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_below_weight_doors_open_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 7

        def test_below_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True, emergency=True,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=True, emergency=False,
    ) -> False
    elevator(
        number_pushed=True, doors_closed=False,
        above_weight=False, emergency=True,
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_below_weight_doors_open_number_pushed` for if the button for a floor is :green:`pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :green:`pushed`    :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10-17

        def test_below_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_above_weight_doors_closed_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_open_number_pushed`

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 10

      def test_below_weight_doors_open_number_pushed(self):
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=True,
                  doors_closed=False,
                  above_weight=False,
                  emergency=True,
              )
          )
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=True,
                  doors_closed=False,
                  above_weight=False,
                  emergency=False,
              )
          )

      def test_above_weight_doors_closed_number_not_pushed(self):

the test passes.

.. code-block:: python

  elevator(
      number_pushed=True, doors_closed=False,
      above_weight=True, emergency=True,
  ) -> False
  elevator(
      number_pushed=True, doors_closed=False,
      above_weight=True, emergency=False,
  ) -> False
  elevator(
      number_pushed=True, doors_closed=False,
      above_weight=False, emergency=True,
  ) -> False
  elevator(
      number_pushed=True, doors_closed=False,
      above_weight=False, emergency=False,
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_below_weight_doors_open_number_pushed` to :ref:`test_emergency_w_below_weight_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10

            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_emergency_w_below_weight_doors_open_number_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_below_weight_doors_open_number_pushed'

----

*********************************************************************************
test_emergency_w_above_weight_doors_closed_number_not_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
:red:`NOT pushed`  :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_above_weight_doors_closed_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 7

        def test_above_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                    emergency=True,
                )
            )

        def test_below_weight_doors_closed_number_not_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_above_weight_doors_closed_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 10-17

        def test_above_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_below_weight_doors_closed_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_above_weight_doors_closed_number_not_pushed`

.. code-block:: python
  :lineno-start: 79
  :emphasize-lines: 10

      def test_above_weight_doors_closed_number_not_pushed(self):
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=True,
                  above_weight=True,
                  emergency=True,
              )
          )
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=True,
                  above_weight=True,
                  emergency=False,
              )
          )

      def test_below_weight_doors_closed_number_not_pushed(self):

the test passes.

.. code-block:: python

  elevator(
      number_pushed=False, doors_closed=True,
      above_weight=True, emergency=True,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=True,
      above_weight=True, emergency=False,
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_above_weight_doors_closed_number_not_pushed` to :ref:`test_emergency_w_above_weight_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 10

            self.assertFalse(
                src.elevator.controller(
                    number_pushed=True,
                    doors_closed=False,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_emergency_w_above_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_above_weight_doors_closed_number_not_pushed'

----

*********************************************************************************
test_emergency_w_below_weight_doors_closed_number_not_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_below_weight_doors_closed_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 7

        def test_below_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )

        def test_above_weight_doors_open_number_not_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False
    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True, emergency=False,
    ) -> False
    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=False, emergency=True,
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_below_weight_doors_closed_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :green:`closed` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`NOT pushed`  :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 10-17

        def test_below_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_above_weight_doors_open_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_closed_number_not_pushed`

.. code-block:: python
  :lineno-start: 97
  :emphasize-lines: 10

      def test_below_weight_doors_closed_number_not_pushed(self):
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=True,
                  above_weight=False,
                  emergency=True,
              )
          )
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=True,
                  above_weight=False,
                  emergency=False,
              )
          )

      def test_above_weight_doors_open_number_not_pushed(self):

the test passes.

.. code-block:: python

  elevator(
      number_pushed=False, doors_closed=True,
      above_weight=True, emergency=True,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=True,
      above_weight=True, emergency=False,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=True,
      above_weight=False, emergency=True,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=True,
      above_weight=False, emergency=False,
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_below_weight_doors_closed_number_not_pushed` to :ref:`test_emergency_w_below_weight_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 10

            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_emergency_w_below_weight_doors_closed_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_below_weight_doors_closed_number_not_pushed'

----

*********************************************************************************
test_emergency_w_above_weight_doors_open_number_not_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :red:`open`      :green:`above` :green:`pushed`    :red:`False`
:red:`NOT pushed`  :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to ``src.elevator.controller`` from the :ref:`assertion<what is an assertion?>` of :ref:`test_above_weight_doors_open_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :red:`open`      :green:`above` :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 7

        def test_above_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                    emergency=True,
                )
            )

        def test_below_weight_doors_open_number_not_pushed(self):

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True, emergency=True,
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_above_weight_doors_open_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :green:`above` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 115
    :emphasize-lines: 10-17

        def test_above_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_below_weight_doors_open_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_above_weight_doors_open_number_not_pushed`

.. code-block:: python
  :lineno-start: 115
  :emphasize-lines: 10

      def test_above_weight_doors_open_number_not_pushed(self):
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=False,
                  above_weight=True,
                  emergency=True,
              )
          )
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=False,
                  above_weight=True,
                  emergency=False,
              )
          )

      def test_below_weight_doors_open_number_not_pushed(self):

the test passes.

.. code-block:: python

  elevator(
      number_pushed=False, doors_closed=False,
      above_weight=True, emergency=True,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=False,
      above_weight=True, emergency=False,
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_above_weight_doors_open_number_not_pushed` to :ref:`test_emergency_w_above_weight_doors_open_number_not_pushed`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 10

            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=True,
                    above_weight=False,
                    emergency=False,
                )
            )

        def test_emergency_w_above_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_above_weight_doors_open_number_not_pushed'

----

*********************************************************************************
test_emergency_w_below_weight_doors_open_number_not_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit, is

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running.
* I add a value for the ``emergency`` parameter to the :ref:`call<how to call a function with input>` to the ``controller`` :ref:`function<what is a function?>` from the :ref:`assertion<what is an assertion?>` of :ref:`test_below_weight_doors_open_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :green:`pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7

        def test_below_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True, emergency=True,
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True, emergency=False,
    ) -> False
    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False, emergency=True,
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_below_weight_doors_open_number_not_pushed` for if the button for a floor is :red:`NOT pushed` AND the **Elevator** doors are :red:`open` AND the **Elevator** is :red:`below` the weight limit AND the emergency button is :red:`NOT pushed`

  =================  ===============  ============== =================  =============
  floor button       doors            weight limit   emergency button   output
  =================  ===============  ============== =================  =============
  :red:`NOT pushed`  :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
  =================  ===============  ============== =================  =============

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 10-17

        def test_below_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )
            self.assertTrue(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the ``controller`` :ref:`function<what is a function?>` returned :red:`False` and this :ref:`assertion<what is a function?>` expects :green:`True`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_below_weight_doors_open_number_not_pushed`

.. code-block:: python
  :lineno-start: 133
  :emphasize-lines: 10

      def test_below_weight_doors_open_number_not_pushed(self):
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=False,
                  above_weight=False,
                  emergency=True,
              )
          )
          self.assertFalse(
              src.elevator.controller(
                  number_pushed=False,
                  doors_closed=False,
                  above_weight=False,
                  emergency=True,
              )
          )


  # Exceptions seen

the test passes.

.. code-block:: python

  elevator(
      number_pushed=False, doors_closed=False,
      above_weight=True, emergency=True,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=False,
      above_weight=True, emergency=False,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=False,
      above_weight=False, emergency=True,
  ) -> False
  elevator(
      number_pushed=False, doors_closed=False,
      above_weight=False, emergency=False,
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_below_weight_doors_open_number_not_pushed` to :ref:`test_emergency_w_below_weight_doors_open_number_not_pushed`

  .. code-block:: python
    :lineno-start: 124
    :emphasize-lines: 10

            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=True,
                    emergency=False,
                )
            )

        def test_emergency_w_below_weight_doors_open_number_not_pushed(self):
            self.assertFalse(
                src.elevator.controller(
                    number_pushed=False,
                    doors_closed=False,
                    above_weight=False,
                    emergency=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_emergency_w_below_weight_doors_open_number_not_pushed'

-----

When the ``controller`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`, it checks if the button for a floor is :red:`NOT pushed`

* If the button for a floor is :red:`NOT pushed` it returns :red:`False`

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True, emergency=True,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=True, emergency=False,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=False, emergency=True,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=True,
        above_weight=False, emergency=False,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True, emergency=True,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=True, emergency=False,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False, emergency=True,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

  .. code-block:: shell

    elevator(
        number_pushed=False, doors_closed=False,
        above_weight=False, emergency=False,
    ) -> False
    └── def controller(
            number_pushed, doors_closed=False,
            above_weight=False, emergency=False,
        ):
        └── if not number_pushed:
            └── return False
            if above_weight:
                return False
            if not doors_closed:
                return False
            if emergency:
                return False
            return True

* If the button for a floor is :green:`pushed` it checks if the total weight of the **Elevator** is :green:`above` the weight limit

  - if the total weight of the **Elevator** is :green:`above` the weight limit, it returns :red:`False`

    .. code-block:: shell

      elevator(
          number_pushed=True, doors_closed=False,
          above_weight=True, emergency=True,
      ) -> False
      └── def controller(
              number_pushed, doors_closed=False,
              above_weight=False, emergency=False,
          ):
          ├── if not number_pushed:
          │       return False
          └── if above_weight:
              └── return False
              if not doors_closed:
                  return False
              if emergency:
                  return False
              return True

    .. code-block:: shell

      elevator(
          number_pushed=True, doors_closed=False,
          above_weight=True, emergency=False,
      ) -> False
      └── def controller(
              number_pushed, doors_closed=False,
              above_weight=False, emergency=False,
          ):
          ├── if not number_pushed:
          │       return False
          └── if above_weight:
              └── return False
              if not doors_closed:
                  return False
              if emergency:
                  return False
              return True

    .. code-block:: shell

      elevator(
          number_pushed=True, doors_closed=True,
          above_weight=True, emergency=True,
      ) -> False
      └── def controller(
              number_pushed, doors_closed=False,
              above_weight=False, emergency=False,
          ):
          ├── if not number_pushed:
          │       return False
          └── if above_weight:
              └── return False
              if not doors_closed:
                  return False
              if emergency:
                  return False
              return True

    .. code-block:: shell

      elevator(
          number_pushed=True, doors_closed=True,
          above_weight=True, emergency=False,
      ) -> False
      └── def controller(
              number_pushed, doors_closed=False,
              above_weight=False, emergency=False,
          ):
          ├── if not number_pushed:
          │       return False
          └── if above_weight:
              └── return False
              if not doors_closed:
                  return False
              if emergency:
                  return False
              return True

  - if the total weight of the **Elevator** is :red:`below` the weight limit, it checks if the **Elevator** doors are :green:`closed`

    - if the **Elevator** doors are :red:`open`, it returns :red:`False`

      .. code-block:: shell

        elevator(
            number_pushed=True, doors_closed=False,
            above_weight=False, emergency=True,
        ) -> False
        └── def controller(
                number_pushed, doors_closed=False,
                above_weight=False, emergency=False,
            ):
            ├── if not number_pushed:
            │       return False
            ├── if above_weight:
            │       return False
            └── if not doors_closed:
                └── return False
                if emergency:
                    return False
                return True

      .. code-block:: shell

        elevator(
            number_pushed=True, doors_closed=False,
            above_weight=False, emergency=False,
        ) -> False
        └── def controller(
                number_pushed, doors_closed=False,
                above_weight=False, emergency=False,
            ):
            ├── if not number_pushed:
            │       return False
            ├── if above_weight:
            │       return False
            └── if not doors_closed:
                └── return False
                if emergency:
                    return False
                return True

    - if the **Elevator** doors are :green:`closed`, it checks if the emergency button is :green:`pushed`

      * if the emergency button is :green:`pushed`, it returns :red:`False`

        .. code-block:: shell

          elevator(
              number_pushed=True, doors_closed=True,
              above_weight=False, emergency=True,
          ) -> False
          └── def controller(
                  number_pushed, doors_closed=False,
                  above_weight=False, emergency=False,
              ):
              ├── if not number_pushed:
              │       return False
              ├── if above_weight:
              │       return False
              ├── if not doors_closed:
              │       return False
              └── if emergency:
                  └── return False
                  return True

      * the button for a floor is :green:`pushed` AND the doors are :green:`closed` AND the **Elevator** is :red:`NOT above` the weight limit, and the emergency button is :red:`NOT pushed`, it returns :green:`True`

        .. code-block:: shell

          elevator(
              number_pushed=True, doors_closed=True,
              above_weight=False, emergency=False,
          ) -> True
          └── def controller(
                  number_pushed, doors_closed=False,
                  above_weight=False, emergency=False,
              ):
              ├── if not number_pushed:
              │       return False
              ├── if above_weight:
              │       return False
              ├── if not doors_closed:
              │       return False
              ├── if emergency:
              │       return False
              └── return True

----

*********************************************************************************
refactor controller
*********************************************************************************

* All the :ref:`if statements` in the ``controller`` :ref:`function<what is a function?>` return :red:`False` which means I can use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put them together

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-11

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, emergency=False,
    ):
        if (
            not number_pushed
            or above_weight
            or not doors_closed
            or emergency
        ):
            return False
        return True

  the tests are still green and this is a long statement.

* I put the two statements that have ``not`` together

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

        if (
            not number_pushed
            or not doors_closed
            or above_weight
            or emergency
        ):
            return False
        return True

  still green.

* I "factor" out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

        if (
            # not number_pushed
            # or not doors_closed
            not (number_pushed and doors_closed)
            or above_weight
            or emergency
        ):
            return False
        return True

  green.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def controller(
        number_pushed, doors_closed=False,
        above_weight=False, emergency=False,
    ):
        if (
            not (number_pushed and doors_closed)
            or above_weight
            or emergency
        ):
            return False
        return True

  Which do you like better? One :ref:`if statement<if statements>` to bind them all or many simple statements?

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'refactor controller'

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_elevator.py`` and ``elevator.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for an **Elevator Controller** with these inputs:

* was the number for a floor pushed?
* are the doors closed?
* is it above the weight limit?
* was the emergency button pushed?

The inputs gave me this :ref:`truth table`

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
:green:`pushed`    :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
:green:`pushed`    :green:`closed`  :red:`below`   :red:`NOT pushed`  :green:`True`
=================  ===============  ============== =================  =============

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:green:`pushed`    :red:`open`      :green:`above` :green:`pushed`    :red:`False`
:green:`pushed`    :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
:green:`pushed`    :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :green:`closed`  :green:`above` :green:`pushed`    :red:`False`
:red:`NOT pushed`  :green:`closed`  :green:`above` :red:`NOT pushed`  :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :green:`pushed`    :red:`False`
:red:`NOT pushed`  :green:`closed`  :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

=================  ===============  ============== =================  =============
floor button       doors            weight limit   emergency button   output
=================  ===============  ============== =================  =============
:red:`NOT pushed`  :red:`open`      :green:`above` :green:`pushed`    :red:`False`
:red:`NOT pushed`  :red:`open`      :green:`above` :red:`NOT pushed`  :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :green:`pushed`    :red:`False`
:red:`NOT pushed`  :red:`open`      :red:`below`   :red:`NOT pushed`  :red:`False`
=================  ===============  ============== =================  =============

The only time this elevator :green:`moves` up or down is when the button for a floor is :green:`pushed` AND the doors are :green:`closed` AND the **Elevator** is :red:`NOT above` the weight limit, and the emergency button is :red:`NOT pushed`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<elevator: tests and solutions>`

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
* :ref:`how to write programs that make decisions<truth table>`

:ref:`Would you like to test making a Microwave?<Microwave>`

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