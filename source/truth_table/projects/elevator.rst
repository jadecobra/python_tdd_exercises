:orphan:

.. meta::
  :description: Build a safety-critical elevator control system from scratch using Python and Test Driven Development (TDD). This project-based tutorial teaches beginners how to manage multiple boolean inputs—including door sensors, floor requests, weight limits, and emergency stop buttons—to create robust, failsafe logic. Master the professional Red-Green-Refactor cycle using modern tools like uv, unittest, and pytest-watcher.
  :keywords: Jacob Itegboje, Python elevator logic project, safety-critical systems tutorial, TDD for beginners, building failsafes in Python, multiple boolean conditions example, elevator simulation code, Python unittest tutorial, uv package manager guide, pytest-watcher automated testing, Red Green Refactor Python project, debugging NameError and TypeError, logical conjunction tutorial, translating truth tables to code, weight limit failsafe logic, emergency stop button code, software engineering projects for beginners, Python boolean logic practice, building a controller in Python, robust software development

.. include:: ../../links.rst

.. _elevator:

#################################################################################
Elevator
#################################################################################

I want to make an **Elevator** that will :green:`True` to a floor when I push a button for the floor.

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/elevator/test_elevator.py
  :language: python
  :linenos:
  :caption: truth_table/tests/test_elevator.py

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

* I name this project ``elevator``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I change the name of the project to ``elevator`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/elevator/make_tdd/makePythonTddElevator.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 5, 12, 20

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``elevator`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I change the name of the project to ``elevator`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/elevator/make_tdd/makePythonTddElevator.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 4, 11, 19

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``elevator`` project

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

* I open a new terminal_ then `change directory`_ to ``elevator``

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
                src.elevator.elevator(
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

  because ``elevator.py`` in the ``src`` folder_ does not have anything named ``elevator`` in it.

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

* I delete all the text in the file_ then add a :ref:`function<what is a function?>` named ``elevator`` to ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def elevator():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: elevator() got
               an unexpected keyword argument 'number_pushed'

  because the test :ref:`called<how to call a function with input>` the ``elevator`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``number_pushed``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

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

    def elevator(number_pushed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  the ``elevator`` :ref:`function<what is a function?>` returned :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I change the :ref:`return statement<the return statement>` to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def elevator(number_pushed):
        return True

  the test passes. The ``elevator`` :ref:`function<what is a function?>` always returns :green:`True`, it does not care about the inputs. Is this :ref:`Tautology?<test_tautology>`

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
                src.elevator.elevator(
                    number_pushed=True,
                )
            )

        def test_number_not_pushed(self):
            self.assertFalse(
                src.elevator.elevator(
                    number_pushed=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``elevator`` :ref:`function<what is a function?>` always returns :green:`True` and this :ref:`assertion<what is an assertion?>` expects :red:`False`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I make the :ref:`function<what is a function?>` return its input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def elevator(number_pushed):
        return number_pushed

  the test passes.

  .. code-block:: python

    elevator(number_pushed=True ) -> True
    elevator(number_pushed=False) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_number_not_pushed'

I want the **Elevator** to :green:`MOVE` only when the button for a floor is :green:`pushed` AND the doors are :green:`closed`. I do not want anything or anyone falling out of the elevator while it is :green:`MOVING`. The inputs will then be

* was the number for a floor pushed?
* are the doors closed?

Which gives me this :ref:`truth table`

=================  ==================  =============
doors              floor button        output
=================  ==================  =============
:green:`closed`    :green:`pushed`     :green:`True`
:green:`closed`    :red:`NOT pushed`   :red:`False`
:red:`NOT closed`  :green:`pushed`     :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`False`
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
* I add ``doors_closed`` with a value to the :ref:`call<how to call a function with input>` to the ``elevator`` :ref:`function<what is a function?>` from :ref:`test_number_pushed` for if the button for a floor is :green:`pushed` AND the elevator doors are :green:`closed`

  =================  ==================  =============
  doors              floor button        output
  =================  ==================  =============
  :green:`closed`    :green:`pushed`     :green:`True`
  =================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_number_pushed(self):
            self.assertTrue(
                src.elevator.elevator(
                    number_pushed=True,
                    doors_closed=True,
                )
            )

        def test_number_not_pushed(self):

  .. code-block:: python

    TypeError: elevator() got
               an unexpected keyword argument 'doors_closed'

  because the test :ref:`called<how to call a function with input>` the ``elevator`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``doors_closed``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``doors_closed`` to the :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def elevator(number_pushed, doors_closed):
        return number_pushed

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: elevator() missing
               1 required positional argument: 'doors_closed'

  because the :ref:`assertion<what is an assertion?>` in :ref:`test_number_not_pushed` :ref:`calls<how to call a function with input>` the ``elevator`` :ref:`function<what is a function?>` with one argument (``number_pushed``) and I just changed the :ref:`function<what is a function?>` to make it take two required arguments (``number_pushed`` and ``doors_closed``). I have to make ``doors_closed`` a :ref:`choice<test_optional_arguments>`.

* I add a :ref:`default value<test_optional_arguments>` for ``doors_closed`` to make it a :ref:`choice<test_optional_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def elevator(number_pushed, doors_closed=False):
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
                src.elevator.elevator(
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
test_doors_closed_number_not_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test named :ref:`test_doors_closed_number_not_pushed` with an :ref:`assertion<what is an assertion?>` for if the button for a floor is :red:`NOT pushed` AND the elevator doors are :green:`closed`, in ``test_elevator.py``

================  ==================  =================
doors             floor button        output
================  ==================  =================
:green:`closed`    :red:`NOT pushed`   :red:`False`
================  ==================  =================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 9-15

      def test_doors_closed_number_pushed(self):
          my_expectation = 'MOVE'
          reality = src.elevator.elevator(
              doors_closed=True,
              number_pushed=True,
          )
          self.assertEqual(reality, my_expectation)

      def test_doors_closed_number_not_pushed(self):
          my_expectation = 'NOT MOVE'
          reality = src.elevator.elevator(
              doors_closed=True,
              number_pushed=False,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'MOVE' != 'NOT MOVE'

because the ``elevator`` :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`'NOT MOVE'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to the ``elevator`` :ref:`function<what is a function?>` in ``elevator.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def elevator(doors_closed, number_pushed):
      if number_pushed == False:
          return 'NOT MOVE'

      return 'MOVE'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def elevator(doors_closed, number_pushed):
        # if number_pushed == False:
        if bool(number_pushed) == False:
            return 'NOT MOVE'

        return 'MOVE'

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def elevator(doors_closed, number_pushed):
        # if number_pushed == False:
        # if bool(number_pushed) == False:
        if not bool(number_pushed) == True:
            return 'NOT MOVE'

        return 'MOVE'

  still green.

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def elevator(doors_closed, number_pushed):
        # if number_pushed == False:
        # if bool(number_pushed) == False:
        # if not bool(number_pushed) == True:
        if not bool(number_pushed):
            return 'NOT MOVE'

        return 'MOVE'

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def elevator(doors_closed, number_pushed):
        # if number_pushed == False:
        # if bool(number_pushed) == False:
        # if not bool(number_pushed) == True:
        # if not bool(number_pushed):
        if not number_pushed:
            return 'NOT MOVE'

        return 'MOVE'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def elevator(doors_closed, number_pushed):
        if not number_pushed:
            return 'NOT MOVE'

        return 'MOVE'

  this is what happens when the ``elevator`` :ref:`function<what is a function?>` is called

  - it returns :red:`'NOT MOVE'` if the button for the floor is :red:`NOT pushed`
  - it returns :green:`True` if the above :ref:`condition<if statements>` is NOT met

----

*********************************************************************************
test_doors_open_number_pushed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed` and the button for a floor is :green:`pushed`, in ``test_elevator.py``

================  ==================  =================
doors             floor button        output
================  ==================  =================
:red:`NOT closed`  :green:`pushed`     :red:`False`
================  ==================  =================

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 9-15

      def test_doors_closed_number_not_pushed(self):
          my_expectation = 'NOT MOVE'
          reality = src.elevator.elevator(
              doors_closed=True,
              number_pushed=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_doors_open_number_pushed(self):
          my_expectation = 'NOT MOVE'
          reality = src.elevator.elevator(
              doors_closed=False,
              number_pushed=True,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'MOVE' != 'NOT MOVE'

because the ``elevator`` :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`'NOT MOVE'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``elevator.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def elevator(doors_closed, number_pushed):
      if doors_closed == False:
          return 'NOT MOVE'

      if not number_pushed:
          return 'NOT MOVE'

      return 'MOVE'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def elevator(doors_closed, number_pushed):
        # if doors_closed == False:
        if bool(doors_closed) == False:
            return 'NOT MOVE'

        if not number_pushed:
            return 'NOT MOVE'

        return 'MOVE'

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the new :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def elevator(doors_closed, number_pushed):
    # if doors_closed == False:
    # if bool(doors_closed) == False:
    if not bool(doors_closed) == True:
        return 'NOT MOVE'

    if not number_pushed:
        return 'NOT MOVE'

    return 'MOVE'

  still green.

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def elevator(doors_closed, number_pushed):
        # if doors_closed == False:
        # if bool(doors_closed) == False:
        # if not bool(doors_closed) == True:
        if not bool(doors_closed):
            return 'NOT MOVE'

        if not number_pushed:
            return 'NOT MOVE'

        return 'MOVE'

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def elevator(doors_closed, number_pushed):
        # if doors_closed == False:
        # if bool(doors_closed) == False:
        # if not bool(doors_closed) == True:
        # if not bool(doors_closed):
        if not doors_closed:
            return 'NOT MOVE'

        if not number_pushed:
            return 'NOT MOVE'

        return 'MOVE'

  because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not bool(something)`` is the same as ``if not something``.

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def elevator(doors_closed, number_pushed):
        not_move = 'NOT MOVE'
        # if doors_closed == False:
        # if bool(doors_closed) == False:
        # if not bool(doors_closed) == True:

* I use the :ref:`variable<what is a variable?>` to remove repetition of :red:`'NOT MOVE'` from the :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9, 12-13

    def elevator(doors_closed, number_pushed):
        not_move = 'NOT MOVE'
        # if doors_closed == False:
        # if bool(doors_closed) == False:
        # if not bool(doors_closed) == True:
        # if not bool(doors_closed):
        if not doors_closed:
            # return 'NOT MOVE'
            return not_move

        if not number_pushed:
            # return 'NOT MOVE'
            return not_move

        return 'MOVE'

  still green.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def elevator(doors_closed, number_pushed):
        not_move = 'NOT MOVE'

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  this is what happens when the ``elevator`` :ref:`function<what is a function?>` is called

  - it returns :red:`'NOT MOVE'` if the button for the floor is :red:`NOT pushed`
  - it returns :red:`'NOT MOVE'` if the doors are :red:`NOT closed`
  - it returns :green:`True` if the above :ref:`conditions<if statements>` are NOT met

----

*********************************************************************************
test_doors_open_number_not_pushed
*********************************************************************************

----

I add a test with an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed` and the button for the floor is :red:`NOT pushed` to ``test_elevator.py``

================  ==================  =================
doors             floor button        output
================  ==================  =================
:red:`NOT closed`  :red:`NOT pushed`   :red:`False`
================  ==================  =================

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 9-15

      def test_doors_open_number_pushed(self):
          my_expectation = 'NOT MOVE'
          reality = src.elevator.elevator(
              doors_closed=False,
              number_pushed=True,
          )
          self.assertEqual(reality, my_expectation)

      def test_doors_open_number_not_pushed(self):
          my_expectation = 'NOT MOVE'
          reality = src.elevator.elevator(
              doors_closed=False,
              number_pushed=False,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test is still green.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* :red:`'NOT MOVE'` happens in 3 of the 4 tests, I make a :ref:`global variable<what is a variable?>` to remove repetition of the :ref:`variables<what is a variable?>` from the tests

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.elevator
    import unittest


    NOT_MOVE = 'NOT MOVE'


    class TestElevator(unittest.TestCase):

  this way all the tests can use the same :ref:`global variable<what is a variable?>` and I do not have to make one for each test

* I use the new :ref:`global variable<what is a variable?>` to remove :red:`'NOT_MOVE'` from :ref:`test_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2, 7-8

        def test_doors_closed_number_not_pushed(self):
            # my_expectation = 'NOT MOVE'
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_pushed(self):

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 18

        def test_doors_closed_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_pushed(self):

* I use the new :ref:`global variable<what is a variable?>` to remove :red:`'NOT_MOVE'` from :ref:`test_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2, 7-8

        def test_doors_open_number_pushed(self):
            # my_expectation = 'NOT MOVE'
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_not_pushed(self):

  green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 25

        def test_doors_open_number_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_not_pushed(self):

* I use the new :ref:`global variable<what is a variable?>` to remove :red:`'NOT_MOVE'` from :ref:`test_doors_open_number_not_pushed`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2, 7-8

        def test_doors_open_number_not_pushed(self):
            # my_expectation = 'NOT MOVE'
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, NOT_MOVE)


    # Exceptions seen

  still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 32

        def test_doors_open_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
            )
            self.assertEqual(reality, NOT_MOVE)


    # Exceptions seen

----

*********************************************************************************
test_weight_w_doors_closed_number_pushed
*********************************************************************************

So far, the :ref:`truth table` for the elevator is

================  ==================  =================
doors             floor button        output
================  ==================  =================
:green:`closed`    :green:`pushed`     :green:`True`
:green:`closed`    :red:`NOT pushed`   :red:`False`
:red:`NOT closed`  :green:`pushed`     :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`False`
================  ==================  =================

I want the elevator to move only when it is :red:`NOT above` a weight limit, the inputs for the elevator will then be

* are the doors closed?
* was the number for a floor pushed?
* is the elevator above the weight limit?

The :ref:`truth table` for when the doors are :green:`closed` and the button for a floor is :green:`pushed`, is:

==============  ==================  ==================  ===============
doors           floor number        weight limit        output
==============  ==================  ==================  ===============
:green:`closed`  :green:`pushed`     :green:`above`      :red:`False`
:green:`closed`  :green:`pushed`     :red:`NOT above`    :green:`True`
==============  ==================  ==================  ===============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` with a value for ``above_weight_limit`` to :ref:`test_doors_closed_number_pushed`, for when the doors are :green:`closed`, the button for a floor is :green:`pushed` and the elevator is :green:`above` the weight limit

==============  ==================  ==================  ===============
doors           floor number        weight limit        output
==============  ==================  ==================  ===============
:green:`closed`  :green:`pushed`     :green:`above`      :red:`False`
==============  ==================  ==================  ===============


.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 2-7

      def test_doors_closed_number_pushed(self):
          reality = src.elevator.elevator(
              doors_closed=True,
              number_pushed=True,
              above_weight_limit=True,
          )
          self.assertEqual(reality, NOT_MOVE)

          my_expectation = 'MOVE'
          reality = src.elevator.elevator(
              doors_closed=True,
              number_pushed=True,
          )
          self.assertEqual(reality, my_expectation)

      def test_doors_closed_number_not_pushed(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: shell

  TypeError: elevator() got
             an unexpected keyword argument 'above_weight_limit'

because the test :ref:`called<how to call a function with input>` the ``elevator`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``above_weight_limit``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``above_weight_limit`` to the :ref:`function signature<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit,
        ):
        not_move = 'NOT MOVE'

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  - the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      FAILED ...test_doors_closed_number_not_pushed - TypeError: elevator() missing 1 required positional argument: 'above_weight_limit'
      FAILED t...test_doors_open_number_not_pushed - TypeError: elevator() missing 1 required positional argument: 'above_weight_limit'
      FAILED ...test_doors_open_number_pushed - TypeError: elevator() missing 1 required positional argument: 'above_weight_limit'

    because the tests call the ``elevator`` :ref:`function<what is a function?>` with 2 arguments (``doors_closed`` and ``number_pushed``) and I just changed the :ref:`function signature<what is a function?>` to make it take 3 required arguments (``doors_closed``, ``number_pushed`` and ``above_weight_limit``). I have to make ``above_weight_limit`` a choice.

  - the terminal_ also shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      AssertionError: 'MOVE' != 'NOT MOVE'

    because the ``elevator`` :ref:`function<what is a function?>` returned :green:`True` when it was called with the ``above_weight_limit`` parameter and the :ref:`assertion<what is an assertion?>` expects :red:`'NOT MOVE'`

* I add a :ref:`default value<test_optional_arguments>` to make ``above_weight_limit`` a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False,
        ):

  - the :ref:`TypeError<what causes TypeError?>` goes away because

    .. code-block:: python

      src.elevator.elevator(
          doors_closed=True,
          number_pushed=False,
      )

    is now the same as

    .. code-block:: python

      src.elevator.elevator(
          doors_closed=True,
          number_pushed=False,
          above_weight_limit=False,
      )

    :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

  - the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'MOVE' != 'NOT MOVE'

  because the ``elevator`` :ref:`function<what is a function?>` returned :green:`True`  and the :ref:`assertion<what is an assertion?>` expects :red:`'NOT MOVE'`

* I add an :ref:`if statement<if statements>` to the :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False,
        ):
        not_move = 'NOT MOVE'

        if above_weight_limit == True:
            return not_move

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1-2

        # if above_weight_limit == True:
        if bool(above_weight_limit) == True:
            return not_move

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-4

        # if above_weight_limit == True:
        # if bool(above_weight_limit) == True:
        if bool(above_weight_limit):
            return not_move

  still green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-4

        # if above_weight_limit == True:
        # if bool(above_weight_limit) == True:
        # if bool(above_weight_limit):
        if above_weight_limit:
            return not_move

  green, because ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False,
        ):
        not_move = 'NOT MOVE'

        if above_weight_limit:
            return not_move

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  this is what happens when the ``elevator`` :ref:`function<what is a function?>` is called

  - it returns :red:`'NOT MOVE'` if the elevator is :green:`above` the weight limit
  - it returns :red:`'NOT MOVE'` if the button for the floor is :red:`NOT pushed`
  - it returns :red:`'NOT MOVE'` if the doors are :red:`NOT closed`
  - it returns :green:`True` if the above :ref:`conditions<if statements>` are NOT met

* I do not need to add a value for the ``above_weight_limit`` parameter to the next :ref:`assertion<what is an assertion?>` for if the doors are :green:`closed`, the button for the floor is :green:`pushed` and the elevator is :red:`NOT above` the weight limit

  ==============  ==================  ==================  ===============
  doors           floor number        weight limit        output
  ==============  ==================  ==================  ===============
  :green:`closed`  :green:`pushed`     :red:`NOT above`    :green:`True`
  ==============  ==================  ==================  ===============

  because

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=True,
        number_pushed=True,
    )

  is the same as

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=True,
        number_pushed=True,
        above_weight_limit=False,
    )

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the name of the test from :ref:`test_doors_closed_number_pushed` to :ref:`test_weight_w_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_weight_w_doors_closed_number_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=True,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

----

*********************************************************************************
test_weight_w_doors_closed_number_not_pushed
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :red:`NOT pushed` AND the elevator doors are :green:`closed`, is:

==============  ==================  ==================  ===============
doors           floor number        weight limit        output
==============  ==================  ==================  ===============
:green:`closed`  :red:`NOT pushed`   :green:`above`      :red:`False`
:green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`False`
==============  ==================  ==================  ===============

* I add a value for the ``above_weight_limit`` parameter to the :ref:`assertion<what is an assertion?>` for if the doors are :green:`closed`, the button for a floor is :red:`NOT pushed` and the elevator is :green:`above` the weight limit, in :ref:`test_doors_closed_number_not_pushed`

  ==============  ==================  ==================  ===============
  doors           floor number        weight limit        output
  ==============  ==================  ==================  ===============
  :green:`closed`  :red:`NOT pushed`   :green:`above`      :red:`False`
  ==============  ==================  ==================  ===============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

        def test_doors_closed_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_pushed(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :green:`closed`, the button for the floor is :red:`NOT pushed` and the elevator is :red:`NOT above` the weight limit

  ==============  ==================  ==================  ===============
  doors           floor number        weight limit        output
  ==============  ==================  ==================  ===============
  :green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`False`
  ==============  ==================  ==================  ===============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 9-13

        def test_doors_closed_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_pushed(self):

  still green. I do not need to add a value for the ``above_weight_limit`` parameter because

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=True,
        number_pushed=False,
    )

  is the same as

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=True,
        number_pushed=False,
        above_weight_limit=False,
    )

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the name of the test from :ref:`test_doors_closed_number_not_pushed` to :ref:`test_weight_w_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8

            my_expectation = 'MOVE'
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_weight_w_doors_closed_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

----

*********************************************************************************
test_weight_w_doors_open_number_pushed
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT closed` and the button for a floor is :green:`pushed`, is:

================  ==================  ==================  ===============
doors             floor number        weight limit        output
================  ==================  ==================  ===============
:red:`NOT closed`  :green:`pushed`     :green:`above`      :red:`False`
:red:`NOT closed`  :green:`pushed`     :red:`NOT above`    :red:`False`
================  ==================  ==================  ===============

* I add a value for the ``above_weight_limit`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_doors_open_number_pushed` for the case where the doors are :red:`NOT closed`, the button for a floor is :green:`pushed` and the elevator is :green:`above` the weight limit

  ================  ==================  ==================  ===============
  doors             floor number        weight limit        output
  ================  ==================  ==================  ===============
  :red:`NOT closed`  :green:`pushed`     :green:`above`      :red:`False`
  ================  ==================  ==================  ===============

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 5

        def test_doors_open_number_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_not_pushed(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_doors_open_number_pushed`, for when the doors are :red:`NOT closed`, the button for the floor is :green:`pushed` and the elevator is :red:`NOT above` the weight limit

  ================  ==================  ==================  ===============
  doors             floor number        weight limit        output
  ================  ==================  ==================  ===============
  :red:`NOT closed`  :green:`pushed`     :red:`NOT above`    :red:`False`
  ================  ==================  ==================  ===============

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 9-13

        def test_doors_open_number_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_doors_open_number_not_pushed(self):

  still green. I do not need to add a value for the ``above_weight_limit`` parameter because

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=False,
        number_pushed=True,
    )

  is the same as

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=False,
        number_pushed=True,
        above_weight_limit=False,
    )

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the name of the test from :ref:`test_doors_open_number_pushed` to :ref:`test_weight_w_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 7

            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_weight_w_doors_open_number_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

----

*********************************************************************************
test_weight_w_doors_open_number_not_pushed
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT closed` and the button for a floor is :red:`NOT pushed`, is:

================  ==================  ==================  ===============
doors             floor number        weight limit        output
================  ==================  ==================  ===============
:red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`False`
================  ==================  ==================  ===============

* I add a value for the ``above_weight_limit`` parameter to the :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed`, the button for a floor is :red:`NOT pushed` and the elevator is :green:`above` the weight , in :ref:`test_doors_open_number_not_pushed`

  ================  ==================  ==================  ===============
  doors             floor number        weight limit        output
  ================  ==================  ==================  ===============
  :red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :red:`False`
  ================  ==================  ==================  ===============

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 5

        def test_doors_open_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)


    # Exceptions seen

  green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed`, the button for the floor is :red:`NOT pushed` and the elevator is :red:`NOT above` the weight limit


  ================  ==================  ==================  ===============
  doors             floor number        weight limit        output
  ================  ==================  ==================  ===============
  :red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`False`
  ================  ==================  ==================  ===============

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 9-13

        def test_doors_open_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
            )
            self.assertEqual(reality, NOT_MOVE)


    # Exceptions seen

  still green. I do not need to add a value for the ``above_weight_limit`` parameter because

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=False,
        number_pushed=False,
    )

  is the same as

  .. code-block:: python

    src.elevator.elevator(
        doors_closed=False,
        number_pushed=False,
        above_weight_limit=False,
    )

  :ref:`A function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the name of the test from :ref:`test_doors_open_number_pushed` to :ref:`test_weight_w_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 7

            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
            )
            self.assertEqual(reality, NOT_MOVE)

        def test_weight_w_doors_open_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
                above_weight_limit=True,
            )
            self.assertEqual(reality, NOT_MOVE)

* I call the ``elevator`` :ref:`function<what is a function?>` directly in :ref:`test_weight_w_doors_open_number_not_pushed`, I do not need the ``reality`` :ref:`variable<what is a variable?>` because it is only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7-15, 21-28

        def test_weight_w_doors_open_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
                above_weight_limit=True,
            )
            # self.assertEqual(reality, NOT_MOVE)
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                ),
                NOT_MOVE
            )

            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=False,
            )
            # self.assertEqual(reality, NOT_MOVE)
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                ),
                NOT_MOVE
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 56

        def test_weight_w_doors_open_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    above_weight_limit=False,
                    number_pushed=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    above_weight_limit=False,
                    number_pushed=False,
                ),
                NOT_MOVE
            )


    # Exceptions seen

* I do the same thing in :ref:`test_weight_w_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7-15, 21-28

        def test_weight_w_doors_open_number_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
                above_weight_limit=True,
            )
            # self.assertEqual(reality, NOT_MOVE)
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                ),
                NOT_MOVE
            )

            reality = src.elevator.elevator(
                doors_closed=False,
                number_pushed=True,
            )
            # self.assertEqual(reality, NOT_MOVE)
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_not_pushed(self):

  still green.

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_weight_w_doors_open_number_pushed`

  .. code-block:: python
    :lineno-start: 39

        def test_weight_w_doors_open_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_not_pushed(self):

* on to :ref:`test_weight_w_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7-15, 21-28

        def test_weight_w_doors_closed_number_not_pushed(self):
            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
                above_weight_limit=True,
            )
            # self.assertEqual(reality, NOT_MOVE)
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                ),
                NOT_MOVE
            )

            reality = src.elevator.elevator(
                doors_closed=True,
                number_pushed=False,
            )
            # self.assertEqual(reality, NOT_MOVE)
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_pushed(self):

  green.

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_weight_w_doors_closed_number_not_pushed`

  .. code-block:: python
    :lineno-start: 25

        def test_weight_w_doors_closed_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_pushed(self):

* I call the ``elevator`` :ref:`function<what is a function?>` directly then remove the commented lines and unused :ref:`variables<what is a variable?>` in :ref:`test_weight_w_doors_closed_number_pushed`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-8, 12-16

        def test_weight_w_doors_closed_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                ),
                'MOVE'
            )

        def test_weight_w_doors_closed_number_not_pushed(self):

  still green.

----

*********************************************************************************
test_doors_closed_number_pushed_w_emergency
*********************************************************************************

The :ref:`truth table` for the elevator is

==============  ==================  ==================  ===============
doors           floor number        weight limit        output
==============  ==================  ==================  ===============
:green:`closed`  :green:`pushed`     :green:`above`      :red:`False`
:green:`closed`  :green:`pushed`     :red:`NOT above`    :green:`True`
:green:`closed`  :red:`NOT pushed`   :green:`above`      :red:`False`
:green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`False`
==============  ==================  ==================  ===============

================  ==================  ==================  ===============
doors             floor number        weight limit        output
================  ==================  ==================  ===============
:red:`NOT closed`  :green:`pushed`     :green:`above`      :red:`False`
:red:`NOT closed`  :green:`pushed`     :red:`NOT above`    :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`False`
================  ==================  ==================  ===============

I want to make sure the elevator can be stopped with a button in an emergency. The inputs will then be

* are the doors closed?
* was the number for a floor pushed?
* is the elevator above the weight limit?
* was the emergency button pushed?

and the :ref:`truth table` for when the doors are :green:`closed` and the number for a floor is :green:`pushed`, is

==============  ================  ==================  ====================  ================
doors           floor number      weight limit        emergency button      output
==============  ================  ==================  ====================  ================
:green:`closed`  :green:`pushed`   :green:`above`      :green:`pushed`       :red:`False`
:green:`closed`  :green:`pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:green:`closed`  :green:`pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:green:`closed`  :green:`pushed`   :red:`NOT above`    :red:`NOT pushed`     :green:`True`
==============  ================  ==================  ====================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for ``emergency`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_weight_w_doors_closed_number_pushed` for the case where the doors are :green:`closed`, the button for a floor is :green:`pushed`, the elevator is :green:`above` the weight limit,  and the emergency button is :green:`pushed`

==============  ================  ==================  ====================  ================
doors           floor number      weight limit        emergency button      output
==============  ================  ==================  ====================  ================
:green:`closed`  :green:`pushed`   :green:`above`      :green:`pushed`       :red:`False`
==============  ================  ==================  ====================  ================

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 7

      def test_weight_w_doors_closed_number_pushed(self):
          self.assertEqual(
              src.elevator.elevator(
                  doors_closed=True,
                  number_pushed=True,
                  above_weight_limit=True,
                  emergency=True,
              ),
              NOT_MOVE
          )

          self.assertEqual(
              src.elevator.elevator(
                  doors_closed=True,
                  number_pushed=True,
              ),
              'MOVE'
          )

      def test_weight_w_doors_closed_number_not_pushed(self):

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: elevator() got
             an unexpected keyword argument 'emergency'

because the test :ref:`called<how to call a function with input>` the ``elevator`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``emergency``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``emergency`` to the ``elevator`` :ref:`function signature<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency,
        ):
        not_move = 'NOT MOVE'

        if above_weight_limit:
            return not_move

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a :ref:`default value<test_optional_arguments>` for the ``emergency`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_weight_w_doors_closed_number_pushed` for when the doors are :green:`closed`, the button for a floor is :green:`pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :red:`NOT pushed`

  ==============  ================  ==================  ====================  ================
  doors           floor number      weight limit        emergency button      output
  ==============  ================  ==================  ====================  ================
  :green:`closed`  :green:`pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
  ==============  ================  ==================  ====================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12-20

        def test_weight_w_doors_closed_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                ),
                'MOVE'
            )

        def test_weight_w_doors_closed_number_not_pushed(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_weight_w_doors_closed_number_pushed` for when the doors are :green:`closed`, the button for the floor is :green:`pushed`, the elevator is :red:`NOT above` the weight limit and the emergency button is :green:`pushed`, in :ref:`test_weight_w_doors_closed_number_pushed` in ``test_elevator.py``

  ==============  ================  ==================  ====================  ================
  doors           floor number      weight limit        emergency button      output
  ==============  ================  ==================  ====================  ================
  :green:`closed`  :green:`pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
  ==============  ================  ==================  ====================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 22-30

        def test_weight_w_doors_closed_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                ),
                'MOVE'
            )

        def test_weight_w_doors_closed_number_not_pushed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'MOVE' != 'NOT MOVE'

  because the ``elevator`` :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`'NOT MOVE'`

* I add an :ref:`if statement<if statements>` to the ``elevator`` :ref:`function<what is a function?>` in ``elevator.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        not_move = 'NOT MOVE'

        if emergency == True:
            return not_move

        if above_weight_limit:
            return not_move

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  the test passes.

* I use :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1-2

        # if emergency == True:
        if bool(emergency) == True:
            return not_move

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-3

        # if emergency == True:
        # if bool(emergency) == True:
        if bool(emergency):
            return not_move

  still green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block::
    :lineno-start: 7
    :emphasize-lines: 3-4

        # if emergency == True:
        # if bool(emergency) == True:
        # if bool(emergency):
        if emergency:
            return not_move

  green, because ``if bool(something) == True`` is the same as ``if something == True`` is the same as ``if something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        not_move = 'NOT MOVE'

        if emergency:
            return not_move

        if above_weight_limit:
            return not_move

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  this is what happens when the ``elevator`` :ref:`function<what is a function?>` is called

  - it returns :red:`'NOT MOVE'` if the emergency button is :green:`pushed`
  - it returns :red:`'NOT MOVE'` if the elevator is :green:`above` the weight limit
  - it returns :red:`'NOT MOVE'` if the button for the floor is :red:`NOT pushed`
  - it returns :red:`'NOT MOVE'` if the doors are :red:`NOT closed`
  - it returns :green:`True` if the above :ref:`conditions<if statements>` are NOT met

* I add values for the ``above_weight_limit`` and ``emergency`` parameters to :ref:`test_weight_w_doors_closed_number_pushed`, even though I do not need to because they have :ref:`default values<test_optional_arguments>`. This will make things clearer in the last :ref:`assertion<what is an assertion?>` which is for when the doors are :green:`closed`, the button for the floor is :green:`pushed`, the elevator is :red:`NOT above` the weight limit,  and the emergency button is  :red:`NOT pushed`, in ``test_elevator.py``

  ==============  ================  ==================  ====================  ================
  doors           floor number      weight limit        emergency button      output
  ==============  ================  ==================  ====================  ================
  :green:`closed`  :green:`pushed`   :red:`NOT above`    :red:`NOT pushed`     :green:`True`
  ==============  ================  ==================  ====================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 36-37

        def test_weight_w_doors_closed_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=False,
                ),
                'MOVE'
            )

        def test_weight_w_doors_closed_number_not_pushed(self):

  green.

* I change the name of the test from :ref:`test_weight_w_doors_closed_number_pushed` to :ref:`test_doors_closed_number_pushed_w_emergency`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestElevator(unittest.TestCase):

        def test_doors_closed_number_pushed_w_emergency(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

----

*********************************************************************************
test_doors_closed_number_not_pushed_w_emergency
*********************************************************************************

The :ref:`truth table` for when the button for a floor is :red:`NOT pushed` AND the elevator doors are :green:`closed`, is

==============  ==================  ==================  ====================  ===============
doors           floor number        weight limit        emergency button      output
==============  ==================  ==================  ====================  ===============
:green:`closed`  :red:`NOT pushed`   :green:`above`      :green:`pushed`       :red:`False`
:green:`closed`  :red:`NOT pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
==============  ==================  ==================  ====================  ===============

* I add a value for the ``emergency`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_weight_w_doors_closed_number_not_pushed` for when the doors are :green:`closed`, button for a floor is :red:`NOT pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :green:`pushed`

  ==============  ==================  ==================  ====================  ===============
  doors           floor number        weight limit        emergency button      output
  ==============  ==================  ==================  ====================  ===============
  :green:`closed`  :red:`NOT pushed`   :green:`above`      :green:`pushed`       :red:`False`
  ==============  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 7

        def test_weight_w_doors_closed_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :green:`closed`, the button for a floor is :red:`NOT pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :red:`NOT pushed`

  ==============  ==================  ==================  ====================  ===============
  doors           floor number        weight limit        emergency button      output
  ==============  ==================  ==================  ====================  ===============
  :green:`closed`  :red:`NOT pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
  ==============  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-20

        def test_weight_w_doors_closed_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_pushed(self):

  the test is still green.

* I add values for the ``above_weight_limit`` and ``emergency`` parameters, even though I do not need to because they have :ref:`default values<test_optional_arguments>`. This will make things clearer in the last :ref:`assertion<what is an assertion?>`, for when the doors are :green:`closed`, the button for the floor is :red:`NOT pushed`, the elevator is :red:`NOT above` the weight limit, and the emergency button is :green:`pushed`

  ==============  ==================  ==================  ====================  ===============
  doors           floor number        weight limit        emergency button      output
  ==============  ==================  ==================  ====================  ===============
  :green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
  ==============  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 25, 27

        def test_weight_w_doors_closed_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_pushed(self):

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :green:`closed`, the button for the floor is :red:`NOT pushed`, the elevator is :red:`NOT above` the weight limit, and the emergency button is :red:`NOT pushed`

  ==============  ==================  ==================  ====================  ===============
  doors           floor number        weight limit        emergency button      output
  ==============  ==================  ==================  ====================  ===============
  :green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
  ==============  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 32-40

        def test_weight_w_doors_closed_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=False,
                    emergency=False,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_pushed(self):

  green.

* I change the name of the test from :ref:`test_weight_w_doors_closed_number_not_pushed` to :ref:`test_doors_closed_number_not_pushed_w_emergency`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=False,
                ),
                'MOVE'
            )

        def test_doors_closed_number_not_pushed_w_emergency(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

----

*********************************************************************************
test_doors_open_number_pushed_w_emergency
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT closed` and the button for a floor is :green:`pushed`, is

================  ================  ==================  ====================  ===============
doors             floor number      weight limit        emergency button      output
================  ================  ==================  ====================  ===============
:red:`NOT closed`  :green:`pushed`   :green:`above`      :green:`pushed`       :red:`False`
:red:`NOT closed`  :green:`pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:red:`NOT closed`  :green:`pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:red:`NOT closed`  :green:`pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
================  ================  ==================  ====================  ===============

* I add a value for the ``emergency`` parameter to the first :ref:`assertion<what is an assertion?>` of :ref:`test_weight_w_doors_open_number_pushed`, for when the doors are :red:`NOT closed`, the button for a floor is :green:`pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :green:`pushed`

  ================  ================  ==================  ====================  ===============
  doors             floor number      weight limit        emergency button      output
  ================  ================  ==================  ====================  ===============
  :red:`NOT closed`  :green:`pushed`   :green:`above`      :green:`pushed`       :red:`False`
  ================  ================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 7

        def test_weight_w_doors_open_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed`, the button for a floor is :green:`pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :red:`NOT pushed`

  ================  ================  ==================  ====================  ===============
  doors             floor number      weight limit        emergency button      output
  ================  ================  ==================  ====================  ===============
  :red:`NOT closed`  :green:`pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
  ================  ================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 12-20

        def test_weight_w_doors_open_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_not_pushed(self):

  still green.

* I add a value for the ``above_weight_limit``, even though I do not need to because it has a :ref:`default value<test_optional_arguments>`. I also add a value for the ``emergency`` parameter. This will make things clearer in the third :ref:`assertion<what is an assertion?>` which is for when the doors are :red:`NOT closed`, the button for the floor is :green:`pushed`, the elevator is :red:`NOT above` the weight limit, and the emergency button is :green:`pushed`

  ================  ================  ==================  ====================  ===============
  doors             floor number      weight limit        emergency button      output
  ================  ================  ==================  ====================  ===============
  :red:`NOT closed`  :green:`pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
  ================  ================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 26-27

        def test_weight_w_doors_open_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_not_pushed(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed`, the button for the floor is :green:`pushed`, the elevator is :red:`NOT above` the weight limit, and the emergency button is :red:`NOT pushed`

  ================  ================  ==================  ====================  ===============
  doors             floor number      weight limit        emergency button      output
  ================  ================  ==================  ====================  ===============
  :red:`NOT closed`  :green:`pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
  ================  ================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 32-40

        def test_weight_w_doors_open_number_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=False,
                    emergency=False,
                ),
                NOT_MOVE
            )

        def test_weight_w_doors_open_number_not_pushed(self):

  still green.

* I change the name of the test from :ref:`test_weight_w_doors_open_number_pushed` to :ref:`test_doors_open_number_pushed_w_emergency`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=True,
                    number_pushed=False,
                    above_weight_limit=False,
                    emergency=False,
                ),
                NOT_MOVE
            )

        def test_doors_open_number_pushed_w_emergency(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=True,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

----

*********************************************************************************
test_doors_open_number_not_pushed_w_emergency
*********************************************************************************

The :ref:`truth table` for when the doors are :red:`NOT closed` and the button for a floor is :red:`NOT pushed`, is

================  ==================  ==================  ====================  ===============
doors             floor number        weight limit        emergency button      output
================  ==================  ==================  ====================  ===============
:red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :green:`pushed`       :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
================  ==================  ==================  ====================  ===============

* I add a value for the ``emergency`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_weight_w_doors_open_number_not_pushed`, for when the doors are :red:`NOT closed`, the button for a floor is :red:`NOT pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :green:`pushed`

  ================  ==================  ==================  ====================  ===============
  doors             floor number        weight limit        emergency button      output
  ================  ==================  ==================  ====================  ===============
  :red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :green:`pushed`       :red:`False`
  ================  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7

        def test_weight_w_doors_open_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed`, the button for a floor is :red:`NOT pushed`, the elevator is :green:`above` the weight limit, and the emergency button is :red:`NOT pushed`

  ================  ==================  ==================  ====================  ===============
  doors             floor number        weight limit        emergency button      output
  ================  ==================  ==================  ====================  ===============
  :red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
  ================  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 12-20

        def test_weight_w_doors_open_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                ),
                NOT_MOVE
            )


    # Exceptions seen

  still green.

* I add values for the ``above_weight_limit`` parameter, even though I do not need to because it has a :ref:`default value<test_optional_arguments>`. I also add a value for the ``emergency`` parameter. This will make things clearer in the third :ref:`assertion<what is an assertion?>`, which is for when the doors are :red:`NOT closed`, the button for the floor is :red:`NOT pushed`, the elevator is :red:`NOT above` the weight limit, and the emergency button is :green:`pushed`

  ================  ==================  ==================  ====================  ===============
  doors             floor number        weight limit        emergency button      output
  ================  ==================  ==================  ====================  ===============
  :red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
  ================  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 26-27

        def test_weight_w_doors_open_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )


    # Exceptions seen

  green.

* I add an :ref:`assertion<what is an assertion?>` for if the doors are :red:`NOT closed`, the button for the floor is :red:`NOT pushed`, the elevator is :red:`NOT above` the weight limit,  and the emergency button is :red:`NOT pushed`

  ================  ==================  ==================  ====================  ===============
  doors             floor number        weight limit        emergency button      output
  ================  ==================  ==================  ====================  ===============
  :red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
  ================  ==================  ==================  ====================  ===============

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 32-40

        def test_weight_w_doors_open_number_not_pushed(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=True,
                    emergency=False,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    number_pushed=False,
                    above_weight_limit=False,
                    emergency=True,
                ),
                NOT_MOVE
            )

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    above_weight_limit=False,
                    number_pushed=False,
                    emergency=False,
                ),
                NOT_MOVE
            )


    # Exceptions seen

  all the tests are still green.

* I change the name of the test from :ref:`test_weight_w_doors_open_number_not_pushed` to :ref:`test_doors_open_number_not_pushed_w_emergency`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 11

            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    above_weight_limit=True,
                    number_pushed=False,
                    emergency=False,
                ),
                NOT_MOVE
            )

        def test_doors_open_number_not_pushed_w_emergency(self):
            self.assertEqual(
                src.elevator.elevator(
                    doors_closed=False,
                    above_weight_limit=False,
                    number_pushed=True,
                    emergency=True,
                ),
                NOT_MOVE
            )

* To review, the ``elevator`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        not_move = 'NOT MOVE'

        if emergency:
            return not_move

        if above_weight_limit:
            return not_move

        if not doors_closed:
            return not_move

        if not number_pushed:
            return not_move

        return 'MOVE'

  - returns :red:`'NOT MOVE'` if the emergency button is :green:`pushed`
  - returns :red:`'NOT MOVE'` if the elevator is :green:`above` the weight limit
  - returns :red:`'NOT MOVE'` if the button for the floor is :red:`NOT pushed`
  - returns :red:`'NOT MOVE'` if the doors are :red:`NOT closed`
  - returns :green:`True` if the above :ref:`conditions<if statements>` are NOT met

* All the :ref:`if statements` return :red:`'NOT MOVE'` which means I could use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put them together though it will be a long statement

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-11

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        if (
            emergency
            or above_weight_limit
            or not doors_closed
            or not number_pushed
        ):
            return 'NOT MOVE'

        return 'MOVE'

  the tests are still green.

* I rewrite the statement in terms of :ref:`NOT<test_logical_negation>` because it happens two times

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-19

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        # if (
        #     emergency
        #     or above_weight_limit
        #     or not doors_closed
        #     or not number_pushed
        # ):
        if (
            emergency
            or above_weight_limit
            or (
                (not doors_closed)
                (not and)
                (not number_pushed)
            )
        ):
            return 'NOT MOVE'

        return 'MOVE'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  because I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>`, this way

* I "factor" out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 11-28

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        # if (
        #     emergency
        #     or above_weight_limit
        #     or not doors_closed
        #     or not number_pushed
        # ):
        # if (
        #     emergency
        #     or above_weight_limit
        #     or (
        #         (not doors_closed)
        #         (not and)
        #         (not number_pushed)
        #     )
        # ):
        if (
            emergency
            or above_weight_limit
            or not (
                doors_closed
                and
                number_pushed
            )
        ):
            return 'NOT MOVE'

        return 'MOVE'

  the tests are green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def elevator(
            doors_closed, number_pushed,
            above_weight_limit=False, emergency=False,
        ):
        if (
            emergency
            or above_weight_limit
            or not (
                doors_closed
                and
                number_pushed
            )
        ):
            return 'NOT MOVE'

        return 'MOVE'

  Which do you like better? One :ref:`if statement<if statements>` to bind them all or many simple statements?

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

I ran tests for a elevator with these inputs:

* are the doors closed?
* is it above the weight limit?
* was the number for a floor pushed?
* was the emergency button pushed?

the inputs gave me this :ref:`truth table`

==============  ================  ==================  ====================  ================
doors           floor number      weight limit        emergency button      output
==============  ================  ==================  ====================  ================
:green:`closed`  :green:`pushed`   :green:`above`      :green:`pushed`       :red:`False`
:green:`closed`  :green:`pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:green:`closed`  :green:`pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:green:`closed`  :green:`pushed`   :red:`NOT above`    :red:`NOT pushed`     :green:`True`
==============  ================  ==================  ====================  ================

==============  ==================  ==================  ====================  ===============
doors           floor number        weight limit        emergency button      output
==============  ==================  ==================  ====================  ===============
:green:`closed`  :red:`NOT pushed`   :green:`above`      :green:`pushed`       :red:`False`
:green:`closed`  :red:`NOT pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:green:`closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
==============  ==================  ==================  ====================  ===============

================  ================  ==================  ====================  ===============
doors             floor number      weight limit        emergency button      output
================  ================  ==================  ====================  ===============
:red:`NOT closed`  :green:`pushed`   :green:`above`      :green:`pushed`       :red:`False`
:red:`NOT closed`  :green:`pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:red:`NOT closed`  :green:`pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:red:`NOT closed`  :green:`pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
================  ================  ==================  ====================  ===============

================  ==================  ==================  ====================  ===============
doors             floor number        weight limit        emergency button      output
================  ==================  ==================  ====================  ===============
:red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :green:`pushed`       :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :green:`above`      :red:`NOT pushed`     :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :green:`pushed`       :red:`False`
:red:`NOT closed`  :red:`NOT pushed`   :red:`NOT above`    :red:`NOT pushed`     :red:`False`
================  ==================  ==================  ====================  ===============

the only time this elevator goes up or down is when the doors are :green:`closed`, the button for a floor is :green:`pushed`, the elevator is :red:`NOT above` the weight limit, and the emergency button is :red:`NOT pushed`.

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