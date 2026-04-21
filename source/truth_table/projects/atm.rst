.. meta::
  :description: Build a real-world Automatic Teller Machine using truth tables and Test-Driven Development in Python. Learn how boolean logic controls physical systems like traffic signals.
  :keywords: Jacob Itegboje, python truth table, Automatic Teller Machine python, tdd python, real world boolean logic, state machine truth table, pumping python

.. include:: ../../links.rst

.. ATTENTION:: This is still a work in progress. There will be errors in the text. The code works and will change as I work on it. Have fun!

.. _atm:

#################################################################################
Automatic Teller Machine
#################################################################################

----

I want to make an **Automatic Teller Machine** that shows different outputs, if the inputs are

* is the PIN correct?
* is the requested amount smaller or bigger than what is in the account?

then this is the :ref:`truth table` I get

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:green:`right PIN`  :green:`enough`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :red:`DENIED`
:red:`wrong PIN`    :green:`yes`       :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`DENIED`
==================  =================  =================

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_atm.py
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

* I name this project ``atm``
* I open a terminal_
* I make a directory_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir atm

  the terminal_ goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd atm

  the terminal_ is my friend, and shows I am in the ``atm`` folder_

  .. code-block:: shell

    .../pumping_python/atm

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

        touch src/atm.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/atm.py

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

        touch tests/test_atm.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/test_atm.py

  the terminal_ goes back to the command line

* I open ``test_atm.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. TIP::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_atm.py

    `Visual Studio Code`_ opens ``test_atm.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestATM(unittest.TestCase):

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

    Initialized project `atm`

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
    _________________________ TestATM.test_failure ___________________________

    self = <tests.test_atm.TestATM testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_atm.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_atm.py::TestATM::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestATM(unittest.TestCase):

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
test_atm_withdrawal
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_atm_withdrawal``, then add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered and there is enough money in the account

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:green:`right PIN`  :green:`enough`    :green:`CASH`
==================  =================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestATM(unittest.TestCase):

      def test_atm_withdrawal(self):
          my_expectation = 'ALLOWED'
          reality = src.atm.withdraw(
              pin_is_correct=True,
              balance_is_enough=True,
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

    import src.atm
    import unittest


    class TestATM(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.atm' has no attribute 'withdraw'

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``atm.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def withdraw():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got an unexpected keyword argument 'pin_is_correct'

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add the :ref:`keyword argument<test_functions_w_keyword_arguments>` to the :ref:`function<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(pin_is_correct):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got an unexpected keyword argument 'balance_is_enough'

* I add ``balance_is_enough`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(pin_is_correct, balance_is_enough):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'ALLOWED'

* I change the `return statement`_ to give the test what it expects

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def withdraw(pin_is_correct, balance_is_enough):
        return 'ALLOWED'

  the test passes. The ``withdraw`` :ref:`function<what is a function?>` always returns :green:`CASH`, it does not care about the inputs. Is this :ref:`Tautology?<test_tautology>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered AND there is :red:`NOT enough` money in the account

  ==================  =================  =================
  PIN                 balance            withdrawal
  ==================  =================  =================
  :green:`right PIN`  :green:`enough`    :green:`CASH`
  :green:`right PIN`  :red:`NOT enough`  :red:`DENIED`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-14

        def test_atm_withdrawal(self):
            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ALLOWED' != 'DENIED'

* I add an :ref:`if statement<if statements>` to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(pin_is_correct, balance_is_enough):
        if pin_is_correct and not balance_is_enough:
            return 'DENIED'
        return 'ALLOWED'

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered and there is :green:`enough` money in the account, to ``test_atm_withdrawal`` in ``test_atm.py``

  ==================  =================  =================
  PIN                 balance            withdrawal
  ==================  =================  =================
  :green:`right PIN`  :green:`enough`    :green:`CASH`
  :green:`right PIN`  :red:`NOT enough`  :red:`DENIED`
  :red:`wrong PIN`    :green:`yes`       :red:`DENIED`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines:

        def test_atm_withdrawal(self):
            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ALLOWED' != 'DENIED'

* I add an :ref:`if statement<if statements>` for this case to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(pin_is_correct, balance_is_enough):
        if not pin_is_correct and balance_is_enough:
            return 'DENIED'
        if pin_is_correct and not balance_is_enough:
            return 'DENIED'
        return 'ALLOWED'

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the last case - when the :red:`wrong PIN` is entered and there is :red:`NOT enough` money left in the account, in ``test_atm.py``

  ==================  =================  =================
  PIN                 balance            withdrawal
  ==================  =================  =================
  :green:`right PIN`  :green:`enough`    :green:`CASH`
  :green:`right PIN`  :red:`NOT enough`  :red:`DENIED`
  :red:`wrong PIN`    :green:`yes`       :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :red:`DENIED`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 23-28


        def test_atm_withdrawal(self):
            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ALLOWED' != 'DENIED'

* I add an :ref:`if statement<if statements>` to ``atm.py`` for the last case

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(pin_is_correct, balance_is_enough):
        if not pin_is_correct and not balance_is_enough:
            return 'DENIED'
        if not pin_is_correct and balance_is_enough:
            return 'DENIED'
        if pin_is_correct and not balance_is_enough:
            return 'DENIED'
        return 'ALLOWED'

  the test passes

* 3 of the cases return ``'DENIED'`` and only one case returns ``'ALLOWED'``. I add an :ref:`if statement with an else clause<if statements>` for the one case

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_correct, balance_is_enough):
        if pin_is_correct and balance_is_enough:
            return 'ALLOWED'
        else:
            return 'DENIED'
        if not pin_is_correct and not balance_is_enough:
            return 'DENIED'
        if not pin_is_correct and balance_is_enough:
            return 'DENIED'
        if pin_is_correct and not balance_is_enough:
            return 'DENIED'
        return 'ALLOWED'

  the test is still green

* I remove the other :ref:`if statements`

  .. code-block:: python
    :linenos:

    def withdraw(pin_is_correct, balance_is_enough):
        if pin_is_correct and balance_is_enough:
            return 'ALLOWED'
        else:
            return 'DENIED'

  still green

* I do not need to make the ``my_expectation`` :ref:`variable<what is a variable?>` 3 times in ``test_atm.py`` since it is the same value every time. I remove the repetition from ``test_atm.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9

        def test_atm_withdrawal(self):
            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green

----

*********************************************************************************
test_atm_withdrawal_w_daily_limit
*********************************************************************************

So far, the :ref:`truth table` for the Automatic Teller Machine is

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:green:`right PIN`  :green:`enough`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :red:`DENIED`
:red:`wrong PIN`    :green:`yes`       :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`DENIED`
==================  =================  =================

I want to add a condition for a daily limit on how much can be withdrawn from the account.The inputs for the ATM will then be

* is the PIN correct?
* is the requested amount smaller or bigger than what is in the account?
* will this put the account above or below the daily limit for withdrawals?

the :ref:`truth table` for the ATM will now be

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` for the first case where the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals, to ``test_atm_withdrawal`` in ``test_atm.py``

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
==================  =================  ====================  ==================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 2-8

        def test_atm_withdrawal(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: withdraw() got an unexpected keyword argument 'above_daily_limit'

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
            pin_is_correct, balance_is_enough,
            above_daily_limit,
        ):
        if pin_is_correct and balance_is_enough:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'ALLOWED' != 'DENIED'

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

        if pin_is_correct and balance_is_enough:
            if above_daily_limit:
                return 'DENIED'
            return 'ALLOWED'
        else:
            return 'DENIED'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() missing 1 required positional argument: 'above_daily_limit'

* I add a :ref:`default value<test_functions_w_default_arguments>` for ``above_daily_limit`` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False,
        ):
        if pin_is_correct and balance_is_enough:
            if above_daily_limit:
                return 'DENIED'
            return 'ALLOWED'
        else:
            return 'DENIED'

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I do not need to add anything to the second :ref:`assertion<what is an assertion?>` in ``test_atm_withdrawal`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  ==================  =================  ====================  ==================

  this means

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_correct=True,
        balance_is_enough=True,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_correct=True,
        balance_is_enough=True,
        above_daily_limit=False,
    )

* I add an :ref:`assertion<what is an assertion?>` for the case where the :green:`right PIN` is entered, the account balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals, in ``test_atm.py``

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19-24

        def test_atm_withdrawal(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I do not need to add anything to the fourth :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals, because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  =================  ====================  ==================

  this means

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_correct=True,
        balance_is_enough=False,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_correct=True,
        balance_is_enough=False,
        above_daily_limit=False,
    )

* I add ``above_daily_limit`` to the fifth :ref:`assertion<what is an assertion?>` for the case where the :red:`wrong PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 32-37

        def test_atm_withdrawal(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'ALLOWED'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I do not need to add anything to the sixth :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals, because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  =================  ====================  ==================

  this means

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_correct=False,
        balance_is_enough=False,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_correct=False,
        balance_is_enough=False,
        above_daily_limit=False,
    )

* I add an :ref:`assertion<what is an assertion?>` for the when the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 8-12

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=True
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 8-12

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=True
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I move the :ref:`assertion<what is an assertion?>` for the one case where the ATM gives cash, to the top and remove the second ``my_expectation`` :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-7

        def test_atm_withdrawal(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
                above_daily_limit=True
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

* There is only one case where the ``withdraw`` :ref:`function<what is a function?>` returns ``'ALLOWED'``. I add :ref:`if statements` for the other cases to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5, 7-12

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False,
        ):
        denial = 'DENIED'

        if not pin_is_correct:
            return denial
        if not balance_is_enough:
            return denial
        if above_daily_limit:
            return denial

        if pin_is_correct and balance_is_enough:
            if above_daily_limit:
                return 'DENIED'
            return 'ALLOWED'
        else:
            return 'DENIED'

  the test is still green.

  The ATM

  * :red:`denies` a withdrawal if the :red:`wrong PIN` is entered because you cannot enter the system
  * :red:`denies` a withdrawal if the account balance is :red:`NOT enough`. This only happens if the :green:`right PIN` is entered.
  * :red:`denies` a withdrawal if the account is :green:`above limit` for the daily withdrawal limit. This only happens if the account balance is :green:`enough`.

* I add a `return statement`_ for the one case where the withdrawal is allowed

  .. code-block:: python
    :linenos:
    :emphasize-lines: 13

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False,
        ):
        denial = 'DENIED'

        if not pin_is_correct:
            return denial
        if not balance_is_enough:
            return denial
        if above_daily_limit:
            return denial
        return 'ALLOWED'

        if pin_is_correct and balance_is_enough:
            if above_daily_limit:
                return 'DENIED'
            return 'ALLOWED'
        else:
            return 'DENIED'

  still green.

  The ATM

  * :red:`denies` a withdrawal if the :red:`wrong PIN` is entered because you cannot enter the system
  * :red:`denies` a withdrawal if the account balance is :red:`NOT enough`. This only happens if the :green:`right PIN` is entered.
  * :red:`denies` a withdrawal if the account is :green:`above limit` for the daily withdrawal limit. This only happens if the account balance is :green:`enough`.
  * :green:`approves` a withdrawal only if the :green:`right PIN` is entered and the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

* I remove the other statements

  .. code-block:: python
    :linenos:

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False,
        ):
        denial = 'DENIED'

        if not pin_is_correct:
            return denial
        if not balance_is_enough:
            return denial
        if above_daily_limit:
            return denial
        return 'ALLOWED'

----

*********************************************************************************
test_atm_withdrawal_w_expired_bank_card
*********************************************************************************

The :ref:`truth table` for the Automatic Teller Machine is now

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

I want to add a condition for when the bank card is expired.The inputs for the ATM will then be

* has the card expired?
* is the PIN correct?
* is the requested amount smaller or bigger than what is in the account?
* will this put the account above or below the daily limit for withdrawals?

the :ref:`truth table` for the ATM will now be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for the ``card_expired`` parameter to the call to the ``withdraw`` :ref:`function<what is a function?>` for the case where the card has :green:`expired`, the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals, in ``test_atm_withdrawal`` in ``test_atm.py``

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
==================  ==================  =================  ====================  =============

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 11-17

      def test_atm_withdrawal(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              pin_is_correct=True,
              balance_is_enough=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'DENIED'

          reality = src.atm.withdraw(
              card_has_expired=True,
              pin_is_correct=True,
              balance_is_enough=True,
              above_daily_limit=True,
          )
          self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: withdraw() got an unexpected keyword argument 'card_has_expired'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``card_has_expired`` to the :ref:`function signature<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False, card_has_expired,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`I cannot put a parameter that does NOT have a default value after a parameter that has a default value<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for ``card_has_expired``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False, card_has_expired=False,
        ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the card has :green:`expired`, the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals, to ``test_atm_withdrawal`` in ``test_atm.py``

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19-25

        def test_atm_withdrawal(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

* I add an :ref:`if statement<if statements>` to the ``withdraw`` :ref:`function<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def withdraw(
            pin_is_correct, balance_is_enough,
            above_daily_limit=False, card_has_expired=False,
        ):
        denial = 'DENIED'

        if card_has_expired:
            return denial
        if not pin_is_correct:
            return denial
        if not balance_is_enough:
            return denial
        if above_daily_limit:
            return denial
        return 'CASH'

  the test passes. the ATM

  * :red:`denies` a withdrawal if the card has :green:`expired`, it will NOT check the PIN.
  * :red:`denies` a withdrawal if the :red:`wrong PIN` is entered because you cannot enter the system.
  * :red:`denies` a withdrawal if the account balance is :red:`NOT enough`. This only happens if the :green:`right PIN` is entered.
  * :red:`denies` a withdrawal if the account is :green:`above limit` for the daily withdrawal limit. This only happens if the account balance is :green:`enough`.
  * :green:`approves` a withdrawal only if the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

* I add ``card_has_expired`` to the fourth :ref:`assertion<what is an assertion?>`, which is for when the card has :green:`expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :gree:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 27-33

        def test_atm_withdrawal(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_correct=True,
                balance_is_enough=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add ``card_has_expired`` to the fifth :ref:`assertion<what is an assertion?>`, I also add ``above_daily_limit`` to be clearer. This is for the case where the card has :green:`expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 10, 13

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add ``card_has_expired`` to the next :ref:`assertion<what is an assertion?>` , for the case where the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 10

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=True,
                balance_is_enough=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_has_expired=True,
                pin_is_correct=False,
                balance_is_enough=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_correct=False,
                balance_is_enough=False,
            )
            self.assertEqual(reality, my_expectation)

  green

* I add an :ref:`assertion<what is an assertion?>` for the case where the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_atm.py`` and ``atm.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line

* I `change directory`_ to the parent of ``atm``

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

I ran tests for a Automatic Teller Machine

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Automatic Teller Machine: tests and solutions>`

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