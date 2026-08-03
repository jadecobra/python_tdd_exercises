.. meta::
  :description: Build an Automated Teller Machine with Python TDD (Red-Green-Refactor): translate a truth table for PIN, cash, daily withdrawal limit, and card expiration into src.atm.withdraw. Beginners use uv, unittest, and pytest-watcher; hit NameError, AttributeError, TypeError (unexpected keywords / missing args), SyntaxError (non-default after default), and AssertionError; learn default parameters, keyword calls, if/not short-circuit denies, a DENIED constant, and assertEqual until only right PIN + enough cash + not above limit + not expired returns CASH.
  :keywords: Jacob Itegboje, Python ATM project tutorial, TDD Red Green Refactor, truth table to code, unittest assertEqual, uv package manager, pytest-watcher, PIN verification, daily withdrawal limit, card expired, default parameters, keyword arguments, SyntaxError parameter without a default, TypeError unexpected keyword argument, NameError src not defined, AttributeError, Logical Negation NOT, if statements, DENIED CASH, pumping python

.. include:: ../../links.rst

.. _atm:

#################################################################################
Automated Teller Machine
#################################################################################


I want to make an **Automated Teller Machine** that gives me :green:`CASH` or :red:`DENIED` when I try to make a withdrawal.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :linenos:
  :caption: atm/tests/test_atm.py
  :lines: 1-28

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 30
  :caption: atm/tests/test_atm.py
  :lines: 30-48

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 50
  :caption: atm/tests/test_atm.py
  :lines: 50-68

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 70
  :caption: atm/tests/test_atm.py
  :lines: 70-88

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 90
  :caption: atm/tests/test_atm.py
  :lines: 90-108

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 110
  :caption: atm/tests/test_atm.py
  :lines: 110-128

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 130
  :caption: atm/tests/test_atm.py
  :lines: 130-148

.. literalinclude:: ../../code/atm/test_atm.py
  :language: python
  :lineno-start: 150
  :caption: atm/tests/test_atm.py
  :lines: 150-

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
      * I change the name of the project to ``atm`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/atm/make_tdd/makePythonTddATM.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 10, 18

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``atm`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``
      * I change the name of the project to ``atm`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/atm/make_tdd/makePythonTddATM.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 9, 17

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``atm`` project

        .. code-block:: python
          :emphasize-lines: 1

          .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES =========================
    _________________ TestATM.test_failure ____________________

    self = <tests.test_atm.TestATM testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_atm.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_atm.py::TestATM::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_atm.py:7`` to open it
* I change :ref:`assertFalse<another way to test if something is grouped as False>` to :ref:`assertTrue<another way to test if something is grouped as True>` in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestATM(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertTrue(True)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then `change directory`_ to ``atm``

  .. code-block:: python
    :emphasize-lines: 1

    cd atm

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

----

If the inputs to the **Automated Teller Machine** are

* is the PIN correct?
* is there enough cash in the account for the withdrawal?

then I get this :ref:`truth table`

==================  ======================= =================
PIN                 cash                    withdrawal
==================  ======================= =================
:green:`right PIN`  :green:`enough cash`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough cash`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`DENIED`
==================  ======================= =================

----

*********************************************************************************
test_right_pin_enough_cash
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change :ref:`test_failure` to :ref:`test_right_pin_enough_cash`, then add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered AND there is :green:`enough cash` in the account

==================  ======================= =================
PIN                 cash                    withdrawal
==================  ======================= =================
:green:`right PIN`  :green:`enough cash`    :green:`CASH`
==================  ======================= =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestATM(unittest.TestCase):

      def test_right_pin_enough_cash(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              right_pin=True,
              enough_cash=True,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen
  # AssertionError

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'src' is not defined

because I do not have a definition for ``src`` in this file_.

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

* I add an `import statement`_ at the top of the file_ so that I can test ``atm.py`` from the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.atm
    import unittest


    class TestATM(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.atm'
                    has no attribute 'withdraw'

  because ``atm/__init__.py`` in the ``src`` folder_ does not have anything named ``withdraw`` in it.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``atm.py`` from the ``src`` folder_

* I delete all the text in the file_ then add a :ref:`function<what is a function?>` named ``withdraw`` to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def withdraw():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got
               an unexpected keyword argument 'right_pin'

  because the test :ref:`called<how to call a function with input>` the ``withdraw`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``right_pin``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add ``right_pin`` to the :ref:`function definition<how to make a function that takes input>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(right_pin):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got
               an unexpected keyword argument 'enough_cash'

  because the test :ref:`called<how to call a function with input>` the ``withdraw`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``enough_cash``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add ``enough_cash`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(right_pin, enough_cash):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'CASH'

  the ``withdraw`` :ref:`function<what is a function?>` always returns :ref:`None<what is None?>` and I want ``'CASH'``.

* I change the :ref:`return statement<the return statement>` to give me ``'CASH'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def withdraw(right_pin, enough_cash):
        return 'CASH'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_right_pin_enough_cash'

The ``withdraw`` :ref:`function<what is a function?>` always returns :green:`'CASH'`, it does not care about the inputs. Is this :ref:`Tautology<test_tautology>` or :green:`'CASH'` that never ends?

.. code-block:: python

  withdraw(right_pin=True, enough_cash=True) -> 'CASH'

----

*********************************************************************************
test_right_pin_not_enough_cash
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered AND there is :red:`NOT enough cash` in the account

  ==================  ======================= =================
  PIN                 cash                    withdrawal
  ==================  ======================= =================
  :green:`right PIN`  :red:`NOT enough cash`  :red:`DENIED`
  ==================  ======================= =================

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-9

            self.assertEqual(reality, my_expectation)

        def test_right_pin_not_enough_cash(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  because the ``withdraw`` :ref:`function<what is a function?>` returns :green:`'CASH'` and the :ref:`assertion<what is an assertion?>` expects :red:`'DENIED'`. This **ATM** is broken, it should not give :green:`'CASH'` when there is :red:`NOT enough cash` in the account.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``atm.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def withdraw(right_pin, enough_cash):
      if enough_cash == False:
          return 'DENIED'
      return 'CASH'

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

    def withdraw(right_pin, enough_cash):
        # if enough_cash == False:
        if bool(enough_cash) == False:
            return 'DENIED'        return 'CASH'

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def withdraw(right_pin, enough_cash):
        # if enough_cash == False:
        # if bool(enough_cash) == False:
        if not bool(enough_cash) == True:
            return 'DENIED'
        return 'CASH'

  still green.

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def withdraw(right_pin, enough_cash):
        # if enough_cash == False:
        # if bool(enough_cash) == False:
        # if not bool(enough_cash) == True:
        if not bool(enough_cash):
            return 'DENIED'
        return 'CASH'

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(right_pin, enough_cash):
        # if enough_cash == False:
        # if bool(enough_cash) == False:
        # if not bool(enough_cash) == True:
        # if not bool(enough_cash):
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``.

* I remove the commented lines from the ``withdraw`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def withdraw(right_pin, enough_cash):
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_right_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account
* it gives me :green:`'CASH'` if the above :ref:`condition<if statements>` is NOT met

.. code-block:: python

  withdraw(right_pin=True, enough_cash=False) -> 'DENIED'
  withdraw(right_pin=True, enough_cash=True ) -> 'CASH'

What :ref:`binary operation<truth table: Binary Operations>` is the ``withdraw`` :ref:`function<what is a function?>` using?

----

*********************************************************************************
test_wrong_pin_enough_cash
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered AND there is :green:`enough cash` in the account, to  ``test_atm.py``

  ==================  ======================= =================
  PIN                 cash                    withdrawal
  ==================  ======================= =================
  :red:`wrong PIN`    :green:`enough cash`    :red:`DENIED`
  ==================  ======================= =================

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 3-9

            self.assertEqual(reality, my_expectation)

        def test_wrong_pin_enough_cash(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  because the ``withdraw`` :ref:`function<what is a function?>` returned :green:`'CASH'` and the :ref:`assertion<what is an assertion?>` expects :red:`DENIED`. Why is this ATM giving me :green:`'CASH'` when I enter the :red:`wrong PIN`?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for this case to ``atm.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def withdraw(right_pin, enough_cash):
      if right_pin == False:
          return 'DENIED'
      if not enough_cash:
          return 'DENIED'
      return 'CASH'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`the bool built-in function<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(right_pin, enough_cash):
        # if right_pin == False:
        if bool(right_pin) == False:
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  the test is still green.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def withdraw(right_pin, enough_cash):
        # if right_pin == False:
        # if bool(right_pin) == False:
        if not bool(right_pin) == True:
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  still green.

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def withdraw(right_pin, enough_cash):
        # if right_pin == False:
        # if bool(right_pin) == False:
        # if not bool(right_pin) == True:
        if not bool(right_pin):
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  green.

* I remove :ref:`bool<how to test if something is grouped as True>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(right_pin, enough_cash):
        # if right_pin == False:
        # if bool(right_pin) == False:
        # if not bool(right_pin) == True:
        # if not bool(right_pin):
        if not right_pin:
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``.

* I remove the commented lines from the ``withdraw`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def withdraw(right_pin, enough_cash):
        if not right_pin:
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_wrong_pin_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(right_pin=False, enough_cash=True ) -> 'DENIED'
  withdraw(right_pin=True , enough_cash=False) -> 'DENIED'
  withdraw(right_pin=True , enough_cash=True ) -> 'CASH'

What :ref:`binary operation<truth table: Binary Operations>` is the ``withdraw`` :ref:`function<what is a function?>` using now?

----

*********************************************************************************
test_wrong_pin_not_enough_cash
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for the last case, which is when the :red:`wrong PIN` is entered AND there is :red:`NOT enough cash` in the account, to ``test_atm.py``

  ==================  ======================= =================
  PIN                 cash                    withdrawal
  ==================  ======================= =================
  :red:`wrong PIN`    :red:`NOT enough cash`  :red:`DENIED`
  ==================  ======================= =================

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3-9

            self.assertEqual(reality, my_expectation)

        def test_wrong_pin_not_enough_cash(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :green:`'CASH'` to :red:`'DENIED'` in :ref:`test_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2

        def test_wrong_pin_not_enough_cash(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes.

  .. code-block:: python

    withdraw(right_pin=False, enough_cash=False) -> 'DENIED'
    withdraw(right_pin=False, enough_cash=True ) -> 'DENIED'
    withdraw(right_pin=True , enough_cash=False) -> 'DENIED'
    withdraw(right_pin=True , enough_cash=True ) -> 'CASH'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_wrong_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered

  .. code-block:: shell

    withdraw(right_pin=False, enough_cash=False) -> 'DENIED'
    └── def withdraw(right_pin, enough_cash):
        └── if not right_pin:
            └── return 'DENIED'
            if not enough_cash:
                return 'DENIED'
            return 'CASH'

  .. code-block:: shell

    withdraw(right_pin=False, enough_cash=True ) -> 'DENIED'
    └── def withdraw(right_pin, enough_cash):
        └── if not right_pin:
            └── return 'DENIED'
            if not enough_cash:
                return 'DENIED'
            return 'CASH'

* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account

  .. code-block:: shell

    withdraw(right_pin=True , enough_cash=False) -> 'DENIED'
    └── def withdraw(right_pin, enough_cash):
        ├── if not right_pin:
        │       return 'DENIED'
        └── if not enough_cash:
            └── return 'DENIED'
            return 'CASH'

  it only checks if there is :green:`enough cash` if the :green:`right PIN` is entered.

* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met

  .. code-block:: shell

    withdraw(right_pin=True , enough_cash=True ) -> 'CASH'
    └── def withdraw(right_pin, enough_cash):
        ├── if not right_pin:
        │       return 'DENIED'
        ├── if not enough_cash:
        │       return 'DENIED'
        └── return 'CASH'

----

*********************************************************************************
extract denied variable
*********************************************************************************

* I add a :ref:`global variable<what is a variable?>` to remove repetition of :red:`'DENIED'` from the tests because three of them use it, in ``test_atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.atm
    import unittest


    DENIED = 'DENIED'


    class TestATM(unittest.TestCase):

* I use the new :ref:`global variable<what is a variable?>` for ``my_expectation`` in :ref:`test_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2, 7-8

        def test_right_pin_not_enough_cash(self):
            # my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_cash(self):

  the test is still green.

* I remove the commented lines from :ref:`test_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 18

        def test_right_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_cash(self):

* I use the new :ref:`global variable<what is a variable?>` for ``my_expectation`` in :ref:`test_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2, 7-8

        def test_wrong_pin_enough_cash(self):
            # my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_cash(self):

  still green.

* I remove the commented lines from :ref:`test_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 25

        def test_wrong_pin_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_cash(self):

* I use the :ref:`global variable<what is a variable?>` for ``my_expectation`` in :ref:`test_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2, 7-8

        def test_wrong_pin_not_enough_cash(self):
            # my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, DENIED)


    # Exceptions seen

  green.

* I remove the commented lines from :ref:`test_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 32

        def test_wrong_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
            )
            self.assertEqual(reality, DENIED)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'extract denied variable'

So far, the :ref:`truth table` for the **Automated Teller Machine** is

==================  ======================= =================
PIN                 cash                    withdrawal
==================  ======================= =================
:green:`right PIN`  :green:`enough cash`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough cash`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`DENIED`
==================  ======================= =================

I want to add a :ref:`condition<if statements>` for a daily limit on how much can be taken from the account. The inputs to the **Automated Teller Machine** will then be

* is the PIN correct?
* is there enough cash in the account for the withdrawal?
* will the withdrawal put the account above or below the daily limit for withdrawals?

----

*********************************************************************************
test_above_limit_right_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :green:`enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :green:`CASH`
==================  ======================= ======================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for the case where the :green:`right PIN` is entered, there is :green:`enough cash` in the account, and it is :green:`above limit` for daily withdrawals, to :ref:`test_right_pin_enough_cash`

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :green:`enough cash`    :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 9-15

      def test_right_pin_enough_cash(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              right_pin=True,
              enough_cash=True,
          )
          self.assertEqual(reality, my_expectation)

      def test_above_limit_right_pin_enough_cash(self):
          reality = src.atm.withdraw(
              right_pin=True,
              enough_cash=True,
              above_daily_limit=True,
          )
          self.assertEqual(reality, DENIED)

      def test_right_pin_not_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got
              an unexpected keyword argument 'above_daily_limit'

  because the ``withdraw`` :ref:`function<what is a function?>` got :ref:`called<how to call a function with input>` with a :ref:`name<test_keyword_arguments>` (``above_daily_limit``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``above_daily_limit`` to the :ref:`function<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit,
        ):
        if not right_pin:
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` and :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_above_limit_right_pin_enough_cash -
        AssertionError: 'CASH' != 'DENIED'
    FAILED ...test_right_pin_enough_cash -
        TypeError: withdraw() missing
            1 required positional argument:
            'above_daily_limit'
    FAILED ...test_right_pin_not_enough_cash -
        TypeError: withdraw() missing
            1 required positional argument:
            'above_daily_limit'
    FAILED ...test_wrong_pin_enough_cash -
        TypeError: withdraw() missing
            1 required positional argument:
            'above_daily_limit'
    FAILED ...test_wrong_pin_not_enough_cash -
        TypeError: withdraw() missing
            1 required positional argument:
            'above_daily_limit'

  because

  - the ``withdraw`` :ref:`function<what is a function?>` returned :green:`'CASH'` and the :ref:`assertion<what is an assertion?>` expects :red:`DENIED`.
  - the other :ref:`assertions<what is an assertion?>` do not provide a value for ``above_daily_limit`` when they :ref:`call<how to call a function with input>` the ``withdraw`` :ref:`function<what is a function?>`, I have to make it a :ref:`choice<test_optional_arguments>`.

* I add a :ref:`default value<test_optional_arguments>` for the ``above_daily_limit`` parameter to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  because the ``withdraw`` :ref:`function<what is a function?>` returns :green:`'CASH'` and the :ref:`assertion<what is an assertion?>` expects :red:`'DENIED'`.

* I add an :ref:`if statement<if statements>` for this case

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        if above_daily_limit == True:
            return 'DENIED'
        if not right_pin:
            return 'DENIED'
        if not enough_cash:
            return 'DENIED'
        return 'CASH'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        # if above_daily_limit == True:
        if above_daily_limit:
            return 'DENIED'

  the test is still green because ``if something == True`` is the same as ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``.

* I add a :ref:`variable<what is a variable?>` for ``'DENIED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        denied = 'DENIED'
        # if above_daily_limit == True:

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'DENIED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9, 11-12, 14-15

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        denied = 'DENIED'
        # if above_daily_limit == True:
        if above_daily_limit:
            # return 'DENIED'
            return denied
        if not right_pin:
            # return 'DENIED'
            return denied
        if not enough_cash:
            # return 'DENIED'
            return denied
        return 'CASH'

  still green.

* I remove the commented lines from the ``withdraw`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        denied = 'DENIED'
        if above_daily_limit:
            return denied
        if not right_pin:
            return denied
        if not enough_cash:
            return denied
        return 'CASH'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_limit_right_pin_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'

----

*********************************************************************************
test_below_limit_right_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :green:`enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :green:`CASH`
==================  ======================= ======================  ==================

* I go back to the terminal_ where the tests are running

* I do not need to add anything to :ref:`test_right_pin_enough_cash` which is for when the :green:`right PIN` is entered, AND there is :green:`enough cash` in the account, and it is :red:`NOT above limit` for daily withdrawals, because the :ref:`default value<test_optional_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :green:`CASH`
  ==================  ======================= ======================  ==================

  this means that

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_cash=True,
    )

  is the same as

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_cash=True,
        above_daily_limit=False,
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I change the name of the test from :ref:`test_right_pin_enough_cash` to :ref:`test_below_limit_right_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_below_limit_right_pin_enough_cash(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_above_limit_right_pin_enough_cash(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_limit_right_pin_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=False
  ) -> 'CASH'

----

*********************************************************************************
test_above_limit_right_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :red:`NOT enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

* I go back to the terminal_ where the tests are running
* I add a value for the ``above_daily_limit`` parameter to the :ref:`assertion<what is an assertion?>` in  :ref:`test_right_pin_not_enough_cash`, for the case where the :green:`right PIN` is entered, there is :red:`NOT enough cash` in the account, and it is :green:`above limit` for daily withdrawals,

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5

        def test_right_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_cash(self):

  the test is still green.

* I change the name of the test from :ref:`test_right_pin_not_enough_cash` to :ref:`test_above_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 3

            self.assertEqual(reality, DENIED)

        def test_above_limit_right_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_cash(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_limit_right_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=True
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=False
  ) -> 'CASH'

----

*********************************************************************************
test_below_limit_right_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :red:`NOT enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough cash` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-8

            self.assertEqual(reality, DENIED)

        def test_below_limit_right_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
            )
            self.assertEqual(reality, 'CASH')

        def test_wrong_pin_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change my expectation to match reality in :ref:`test_below_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 6

        def test_below_limit_right_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_cash=False,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_cash(self):

  the test passes. I do not need to give a value for the ``above_daily_limit`` parameter because the :ref:`default value<test_optional_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_cash=False,
    )

  is the same as

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_cash=False,
        above_daily_limit=False,
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_limit_right_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=False
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=True
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=True,
      above_daily_limit=False
  ) -> 'CASH'

----

*********************************************************************************
test_above_limit_wrong_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered AND there is :green:`enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

* I go back to the terminal_ where the tests are running
* I add a value for the ``above_daily_limit`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_wrong_pin_enough_cash`, for the case where the :red:`wrong PIN` is entered, there is :green:`enough cash` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 5

        def test_wrong_pin_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_cash(self):

  the test is still green.

* I change the name of :ref:`test_wrong_pin_enough_cash` to :ref:`test_above_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3

            self.assertEqual(reality, DENIED)

        def test_above_limit_wrong_pin_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
                above_daily_limit=True,
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_limit_wrong_pin_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'

----

*********************************************************************************
test_below_limit_wrong_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered AND there is :green:`enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :green:`enough cash` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-8

            self.assertEqual(reality, DENIED)

        def test_below_limit_wrong_pin_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
            )
            self.assertEqual(reality, 'CASH')

        def test_wrong_pin_not_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :green:`'CASH'` to :red:`DENIED` in :ref:`test_below_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 6

        def test_below_limit_wrong_pin_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_cash(self):

  the test passes. I do not need to give a value for the ``above_daily_limit`` parameter in the call to ``src.atm.withdraw`` because the :ref:`default value<test_optional_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    src.atm.withdraw(
        right_pin=False,
        enough_cash=True,
    )

  is the same as

  .. code-block:: python

    src.atm.withdraw(
        right_pin=False,
        enough_cash=True,
        above_daily_limit=False,
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_limit_wrong_pin_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=False
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'

----

*********************************************************************************
test_above_limit_wrong_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered AND there is :red:`NOT enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

* I go back to the terminal_ where the tests are running
* I add ``above_daily_limit`` to the :ref:`call<how to call a function with input>` to ``src.atm.withdraw`` from :ref:`test_wrong_pin_not_enough_cash`, for when the :red:`wrong PIN` is entered, there is :red:`NOT enough cash` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 5

        def test_wrong_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)


    # Exceptions seen

  the test is still green.

* I change the name of the test from :ref:`test_wrong_pin_not_enough_cash` to :ref:`test_above_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3

            self.assertEqual(reality, DENIED)

        def test_above_limit_wrong_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
                above_daily_limit=True,
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_above_limit_wrong_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=False,
      above_daily_limit=True
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=False
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=True
  ) -> 'DENIED'

----

*********************************************************************************
test_below_limit_wrong_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered AND there is :red:`NOT enough cash` in the account, is

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough cash` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 cash                    daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 62
    :emphasize-lines: 3-8

            self.assertEqual(reality, DENIED)

        def test_below_limit_wrong_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
            )
            self.assertEqual(reality, 'CASH')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :green:`'CASH'` to :red:`DENIED` in :ref:`test_below_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 6

        def test_below_limit_wrong_pin_not_enough_cash(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_cash=False,
            )
            self.assertEqual(reality, DENIED)


    # Exceptions seen

  the test passes.

  .. code-block:: python

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=False
    ) -> 'DENIED'
    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=True
    ) -> 'DENIED'
    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=False
    ) -> 'DENIED'
    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=True
    ) -> 'DENIED'

  I do not need to give a value for the ``above_daily_limit`` parameter in the call to ``src.atm.withdraw`` because the :ref:`default value<test_optional_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    reality = src.atm.withdraw(
        right_pin=False,
        enough_cash=False,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        right_pin=False,
        enough_cash=False,
        above_daily_limit=False,
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_below_limit_wrong_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        ├── if above_daily_limit:
        │       return denied
        └── if not right_pin:
            └── return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        ├── if above_daily_limit:
        │       return denied
        └── if not right_pin:
            └── return denied
            if not enough_cash:
                return denied
            return 'CASH'

  it only checks if the :green:`right PIN` is entered if the account is :red:`NOT above limit` for daily withdrawals.

* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        ├── if above_daily_limit:
        │       return denied
        ├── if not right_pin:
        │       return denied
        └── if not enough_cash:
            └── return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        ├── if above_daily_limit:
        │       return denied
        ├── if not right_pin:
        │       return denied
        └── if not enough_cash:
            └── return denied
            return 'CASH'

  it only checks if there is :green:`enough cash` in the account if the :green:`right PIN` is entered.

* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=False
    ) -> 'CASH'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False,
        ):
        ├── denied = 'DENIED'
        ├── if above_daily_limit:
        │       return denied
        ├── if not right_pin:
        │       return denied
        ├── if not enough_cash:
        │       return denied
        └── return 'CASH'
----

*********************************************************************************
remove reality variable
*********************************************************************************

I can :ref:`call<how to call a function with input>` the ``withdraw`` :ref:`function<what is a function?>` directly in all the :ref:`assertions<what is an assertion?>` of the tests. I do not need the ``reality`` :ref:`variable<what is a variable?>` as a middle man because I only use the :ref:`variable<what is a variable?>` once in each test.

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_below_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2-13

        def test_below_limit_wrong_pin_not_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=False,
            #     enough_cash=False,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                ),
                DENIED
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_below_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 64

        def test_below_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                ),
                DENIED
            )


    # Exceptions seen

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_above_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2-15

        def test_above_limit_wrong_pin_not_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=False,
            #     enough_cash=False,
            #     above_daily_limit=True,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_below_limit_wrong_pin_not_enough_cash(self):

  still green.

* I remove the commented lines from :ref:`test_above_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 56

        def test_above_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_below_limit_wrong_pin_not_enough_cash(self):

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_below_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-13

        def test_below_limit_wrong_pin_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=False,
            #     enough_cash=True,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                ),
                DENIED
            )

        def test_above_limit_wrong_pin_not_enough_cash(self):

  green.

* I remove the commented lines from :ref:`test_below_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 49

        def test_below_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                ),
                DENIED
            )

        def test_above_limit_wrong_pin_not_enough_cash(self):

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_above_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-15

        def test_above_limit_wrong_pin_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=False,
            #     enough_cash=True,
            #     above_daily_limit=True,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_below_limit_wrong_pin_enough_cash(self):

  still green.

* I remove the commented lines from :ref:`test_above_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 41

        def test_above_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_below_limit_wrong_pin_enough_cash(self):

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_below_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2-13

        def test_below_limit_right_pin_not_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=True,
            #     enough_cash=False,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                ),
                DENIED
            )

        def test_above_limit_wrong_pin_enough_cash(self):

  the test is still green.

* I remove the commented lines from :ref:`test_below_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 34

        def test_below_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                ),
                DENIED
            )

        def test_above_limit_wrong_pin_enough_cash(self):

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_above_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2-15

        def test_above_limit_right_pin_not_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=True,
            #     enough_cash=False,
            #     above_daily_limit=True,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_below_limit_right_pin_not_enough_cash(self):

  still green.

* I remove the commented lines from :ref:`test_above_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 26

        def test_above_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_below_limit_right_pin_not_enough_cash(self):

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_above_limit_right_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2-15

        def test_above_limit_right_pin_enough_cash(self):
            # reality = src.atm.withdraw(
            #     right_pin=True,
            #     enough_cash=True,
            #     above_daily_limit=True,
            # )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_above_limit_right_pin_not_enough_cash(self):

  still green.

* I remove the commented lines from :ref:`test_above_limit_right_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 18

        def test_above_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

        def test_above_limit_right_pin_not_enough_cash(self):

* I :ref:`call<how to call a function with input>` ``src.atm.withdraw`` directly and use :green:`'CASH'` for ``my_expectation`` in the :ref:`assertion<what is an assertion?>` of :ref:`test_below_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 2-13

        def test_below_limit_right_pin_enough_cash(self):
            # my_expectation = 'CASH'
            # reality = src.atm.withdraw(
            #     right_pin=True,
            #     enough_cash=True,
            # )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                ),
                'CASH'
            )

        def test_above_limit_right_pin_enough_cash(self):

  the test is still green.

* I remove the commented lines from :ref:`test_below_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 10

        def test_below_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                ),
                'CASH'
            )

        def test_above_limit_right_pin_enough_cash(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'remove reality variable'

The :ref:`truth table` for the **Automated Teller Machine** is now

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :green:`CASH`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

==================  ======================= ======================  ==================
PIN                 cash                    daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

What if the bank card has expired? The inputs to the **Automated Teller Machine** will then be

* has the card expired?
* is the PIN correct?
* is there enough cash in the account for the withdrawal?
* will the withdrawal put the account above or below the daily limit for withdrawals?

----

*********************************************************************************
test_card_w_below_limit_right_pin_enough_cash
*********************************************************************************


The :ref:`truth table` for if the :green:`right PIN` is entered, AND there is :green:`enough cash` in the account, AND it is :red:`NOT above limit` for daily withdrawals is

==================  ===================== ======================  ==================  =============
PIN                 cash                  daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ===================== ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``card_expired`` parameter to the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` for the case where the :green:`right PIN` is entered, there is :green:`enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`, in :ref:`test_below_limit_right_pin_enough_cash`

  ==================  ===================== ======================  ==================  =============
  PIN                 cash                  daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6

        def test_below_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_above_limit_right_pin_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got
               an unexpected keyword argument 'card_expired'

  because the test :ref:`called<how to call a function with input>` the ``withdraw`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``card_expired``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``card_expired`` to the :ref:`function signature<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a :ref:`default value<test_optional_arguments>` for ``card_expired`` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):

  the test passes.

  .. code-block:: python

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) -> 'CASH'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the value for the ``above_daily_limit`` parameter to :ref:`test_below_limit_right_pin_enough_cash` to make the :ref:`assertion<what is an assertion?>` clearer, in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6

        def test_below_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_above_limit_right_pin_enough_cash(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :green:`enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ===================== ======================  ==================  =============
  PIN                 cash                  daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 11-19

        def test_below_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

        def test_above_limit_right_pin_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  The **ATM** should not give me :green:`CASH` if the bank card has :green:`expired`.

* I add an :ref:`if statement<if statements>` to the ``withdraw`` :ref:`function<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired == True:
            return denied
        if above_daily_limit:
            return denied

  the test passes.

  .. code-block:: python

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'
    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) -> 'CASH'

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return denied
        if above_daily_limit:
            return denied
        if not right_pin:
            return denied
        if not enough_cash:
            return denied
        return 'CASH'

  the test is still green.

* I change the name of the test from :ref:`test_below_limit_right_pin_enough_cash` to :ref:`test_card_w_below_limit_right_pin_enough_cash` in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_card_w_below_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am \
    'add test_card_w_below_limit_right_pin_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the card has :green:`expired`.
* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

----

*********************************************************************************
test_card_w_above_limit_right_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered, AND there is :green:`enough cash` in the account, AND it is :green:`above limit` for daily withdrawals is

==================  ===================== ======================  ==================  =============
PIN                 cash                  daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
==================  ===================== ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``card_expired`` parameter to the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` for the case where the :green:`right PIN` is entered, there is :green:`enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :green:`expired`, in :ref:`test_above_limit_right_pin_enough_cash`

  ==================  ===================== ======================  ==================  =============
  PIN                 cash                  daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7

        def test_above_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

        def test_above_limit_right_pin_not_enough_cash(self):

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>` for the case where the :green:`right PIN` is entered, there is :green:`enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ===================== ======================  ==================  =============
  PIN                 cash                  daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 11-19

        def test_above_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_above_limit_right_pin_not_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :green:`'CASH'` to :red:`DENIED` in :ref:`test_above_limit_right_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 8

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

        def test_above_limit_right_pin_not_enough_cash(self):

  the test passes.

  .. code-block:: python

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=False
    ) -> 'DENIED'
    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_above_limit_right_pin_enough_cash` to :ref:`test_card_w_above_limit_right_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

        def test_card_w_above_limit_right_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_card_w_above_limit_right_pin_enough_cash'

----

*********************************************************************************
test_card_w_above_limit_right_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :red:`NOT enough cash` in the account, AND it is :green:`above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``card_expired`` parameter to the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` for the case where the :green:`right PIN` is entered, there is :red:`NOT enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============


  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 7

        def test_above_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

        def test_below_limit_right_pin_not_enough_cash(self):

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 11-19

        def test_above_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_below_limit_right_pin_not_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change my expectation to match reality in :ref:`test_above_limit_right_pin_not_enough_cash`

.. code-block:: python
  :lineno-start: 60
  :emphasize-lines: 8

          self.assertEqual(
              src.atm.withdraw(
                  right_pin=True,
                  enough_cash=False,
                  above_daily_limit=True,
                  card_expired=False,
              ),
              DENIED
          )

      def test_below_limit_right_pin_not_enough_cash(self):

the test passes.

.. code-block:: python

  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=True, card_expired=False
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=True, card_expired=True
  ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_above_limit_right_pin_not_enough_cash` to :ref:`test_card_w_above_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_above_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_card_w_above_limit_right_pin_not_enough_cash'

----

*********************************************************************************
test_card_w_below_limit_right_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :red:`NOT enough cash` in the account, AND it is :red:`NOT above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add values for the ``card_expired`` and ``above_daily_limit`` parameters to the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` for the case where the :green:`right PIN` is entered, there is :red:`NOT enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :green:`expired` in :ref:`test_below_limit_right_pin_not_enough_cash`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 6-7

        def test_below_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

        def test_above_limit_wrong_pin_enough_cash(self):

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 11-19

        def test_below_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_above_limit_wrong_pin_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :green:`'CASH'` to :red:`DENIED` in :ref:`test_below_limit_right_pin_not_enough_cash`

.. code-block:: python
  :lineno-start: 80
  :emphasize-lines: 8

          self.assertEqual(
              src.atm.withdraw(
                  right_pin=True,
                  enough_cash=False,
                  above_daily_limit=False,
                  card_expired=False,
              ),
              DENIED
          )

      def test_above_limit_wrong_pin_enough_cash(self):

the test passes.

.. code-block:: python

  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=False, card_expired=False
  ) -> 'DENIED'
  withdraw(
      right_pin=True, enough_cash=False,
      above_daily_limit=False, card_expired=True
  ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_below_limit_right_pin_not_enough_cash` to :ref:`test_card_w_below_limit_right_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_below_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_card_w_below_limit_right_pin_not_enough_cash'

----

*********************************************************************************
test_card_w_above_limit_wrong_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered, AND there is :green:`enough cash` in the account, AND it is :green:`above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``card_expired`` parameter  to the :ref:`assertion<what is an assertion?>` in :ref:`test_above_limit_wrong_pin_enough_cash` for the case where the :red:`wrong PIN` is entered, there is :green:`enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 7

        def test_above_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

        def test_wrong_pin_enough_cash_below_limit(self):

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>` for the case where the :red:`wrong PIN` is entered, there is :green:`enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 11-19

        def test_above_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_wrong_pin_enough_cash_below_limit(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change my expectation to match reality in the second :ref:`assertion<what is an assertion?>` in :ref:`test_above_limit_wrong_pin_enough_cash`

.. code-block:: python
  :lineno-start: 100
  :emphasize-lines: 8

          self.assertEqual(
              src.atm.withdraw(
                  right_pin=False,
                  enough_cash=True,
                  above_daily_limit=True,
                  card_expired=False,
              ),
              DENIED
          )

      def test_wrong_pin_enough_cash_below_limit(self):

the test passes.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=True, card_expired=False
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=True, card_expired=True
  ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_above_limit_wrong_pin_enough_cash` to :ref:`test_card_w_above_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_above_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_card_w_above_limit_wrong_pin_enough_cash'

----

*********************************************************************************
test_card_w_below_limit_wrong_pin_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered, AND there is :green:`enough cash` in the account, AND it is :red:`NOT above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add values for the ``card_expired`` and ``above_daily_limit`` parameters to the :ref:`assertion<what is an assertion?>` in :ref:`test_below_limit_wrong_pin_enough_cash` for the case where the :red:`wrong PIN` is entered, there is :green:`enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 6-7

        def test_below_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

        def test_above_limit_wrong_pin_not_enough_cash(self):

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :green:`enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 11-19

        def test_below_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_above_limit_wrong_pin_not_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :green:`'CASH'` to :red:`DENIED` in :ref:`test_below_limit_wrong_pin_enough_cash`

.. code-block:: python
  :lineno-start: 120
  :emphasize-lines: 8

          self.assertEqual(
              src.atm.withdraw(
                  right_pin=False,
                  enough_cash=True,
                  above_daily_limit=False,
                  card_expired=False,
              ),
              DENIED
          )

      def test_above_limit_wrong_pin_not_enough_cash(self):

the test passes.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=False, card_expired=False
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=True,
      above_daily_limit=False, card_expired=True
  ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of :ref:`test_below_limit_wrong_pin_enough_cash` to :ref:`test_card_w_below_limit_wrong_pin_enough_cash`

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

        def test_wrong_pin_enough_cash_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_card_w_below_limit_wrong_pin_enough_cash'

----

*********************************************************************************
test_card_w_above_limit_wrong_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered, AND there is :red:`NOT enough cash` in the account, AND it is :green:`above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``card_expired`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_above_limit_wrong_pin_not_enough_cash` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 7

        def test_above_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

        def test_below_limit_wrong_pin_not_enough_cash(self):

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>`, for when the :red:`wrong PIN` is entered, there is :red:`NOT enough cash` in the account, it is :green:`above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 11-19

        def test_above_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_below_limit_wrong_pin_not_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :green:`'CASH'` to :red:`DENIED` in the second :ref:`assertion<what is an assertion?>` of :ref:`test_above_limit_wrong_pin_not_enough_cash`

.. code-block:: python
  :lineno-start: 140
  :emphasize-lines: 8

          self.assertEqual(
              src.atm.withdraw(
                  right_pin=False,
                  enough_cash=False,
                  above_daily_limit=True,
                  card_expired=False,
              ),
              DENIED
          )

      def test_below_limit_wrong_pin_not_enough_cash(self):

the test passes.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=False,
      above_daily_limit=True, card_expired=False
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=False,
      above_daily_limit=True, card_expired=True
  ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of :ref:`test_above_limit_wrong_pin_not_enough_cash` to :ref:`test_card_w_above_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 120
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_above_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_card_w_above_limit_wrong_pin_not_enough_cash'

----

*********************************************************************************
test_card_w_below_limit_wrong_pin_not_enough_cash
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered, AND there is :red:`NOT enough cash` in the account, AND it is :red:`NOT above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add values for the ``card_expired`` and ``above_daily_limit`` parameters to the :ref:`assertion<what is an assertion?>` in :ref:`test_below_limit_wrong_pin_not_enough_cash` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 7

        def test_below_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 cash                    daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 150
    :emphasize-lines: 11-19

        def test_below_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'DENIED' != 'CASH'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change my expectation to match reality in :ref:`test_below_limit_wrong_pin_not_enough_cash`

.. code-block:: python
  :lineno-start: 160
  :emphasize-lines: 8

          self.assertEqual(
              src.atm.withdraw(
                  right_pin=False,
                  enough_cash=False,
                  above_daily_limit=False,
                  card_expired=False,
              ),
              DENIED
          )


  # Exceptions seen
  # AssertionError
  # NameError
  # AttributeError
  # TypeError
  # SyntaxError

the test passes.

.. code-block:: python

  withdraw(
      right_pin=False, enough_cash=False,
      above_daily_limit=False, card_expired=False
  ) -> 'DENIED'
  withdraw(
      right_pin=False, enough_cash=False,
      above_daily_limit=False, card_expired=True
  ) -> 'DENIED'

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_below_limit_wrong_pin_not_enough_cash` to :ref:`test_card_w_below_limit_wrong_pin_not_enough_cash`

  .. code-block:: python
    :lineno-start: 140
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_below_limit_wrong_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am \
    'add test_card_w_below_limit_wrong_pin_not_enough_cash'

When the ``withdraw`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* it returns :red:`'DENIED'` if the card has :green:`expired`.

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=True, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=False, card_expired=True
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        └── if card_expired:
            └── return denied
            if above_daily_limit:
                return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

* it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals.

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=True, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=True, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=True, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        └── if above_daily_limit:
            └── return denied
            if not right_pin:
                return denied
            if not enough_cash:
                return denied
            return 'CASH'

  it only checks if the account is :green:`above limit` for daily withdrawals if the card has :red:`NOT expired`
* it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered.

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        ├── if above_daily_limit:
        │       return denied
        └── if not right_pin:
            └── return denied
            if not enough_cash:
                return denied
            return 'CASH'

  .. code-block:: shell

    withdraw(
        right_pin=False, enough_cash=False,
        above_daily_limit=False, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        ├── if above_daily_limit:
        │       return denied
        └── if not right_pin:
            └── return denied
            if not enough_cash:
                return denied
            return 'CASH'

  it only checks if the :green:`right PIN` is entered if the account is :red:`NOT above limit` for daily withdrawals.
* it returns :red:`'DENIED'` if there is :red:`NOT enough cash` in the account.

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=False,
        above_daily_limit=False, card_expired=False
    ) -> 'DENIED'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        ├── if above_daily_limit:
        │       return denied
        ├── if not right_pin:
        │       return denied
        └── if not enough_cash:
            └── return denied
            return 'CASH'

  it only checks if there is :green:`enough cash` in the account if the :green:`right PIN` is entered.
* it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met.

  .. code-block:: shell

    withdraw(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) -> 'CASH'
    └── def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        ├── denied = 'DENIED'
        ├── if card_expired:
        │       return denied
        ├── if above_daily_limit:
        │       return denied
        ├── if not right_pin:
        │       return denied
        ├── if not enough_cash:
        │       return denied
        └── return 'CASH'

The ``withdraw`` :ref:`function<what is a function?>` can also be written with :ref:`Logical Disjunction (OR)<test_logical_disjunction>` or :ref:`Logical Conjunction (AND)<test_logical_conjunction>`. Try it and see which one you like.

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_atm.py`` and ``atm.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for an Automated Teller Machine with these inputs:

* has the card expired?
* is the PIN correct?
* is there enough cash in the account for the withdrawal?
* will the withdrawal put the account above or below the daily limit for withdrawals?

the inputs gave me this :ref:`truth table`

==================  ===================== ======================  ==================  =============
PIN                 cash                  daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ===================== ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

The ATM only gives me ``'CASH'`` when the :green:`right PIN` is entered, there is :green:`enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the bank card has :red:`NOT expired`.

What if I want the ATM to give a different message with each denial, so that the user knows why the withdrawal failed? The :ref:`truth table` could then be

==================  ===================== ======================  ==================  =============
PIN                 cash                  daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: You have exceeded the daily withdrawal limit`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ===================== ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: You have exceeded the daily withdrawal limit`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: There is not enough Cash in the Account`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED: You entered the wrong PIN. Try again...`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: You entered the wrong PIN. Try again...`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: You entered the wrong PIN. Try again...`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: You entered the wrong PIN. Try again...`
==================  ======================= ======================  ==================  =============

What would I change in the tests and solution?

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Automated Teller Machine: tests and solutions>`

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

:ref:`Would you like to test making a Car?<Car>`

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