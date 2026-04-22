.. meta::
  :description: Build a real-world Automatic Teller Machine using truth tables and Test-Driven Development in Python. Learn how boolean logic controls physical systems like traffic signals.
  :keywords: Jacob Itegboje, python truth table, Automatic Teller Machine python, tdd python, real world boolean logic, state machine truth table, pumping python

.. include:: ../../links.rst

.. _atm:

#################################################################################
Automatic Teller Machine
#################################################################################

----

I want to make an **Automatic Teller Machine** that allows withdrawals or denies them, if the inputs are

* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?

this is the :ref:`truth table` I get

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
test_withdrawal_when_pin_is_right
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_withdrawal_when_pin_is_right``, then add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered and there amount in the account is :green:`enough`

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:green:`right PIN`  :green:`enough`    :green:`CASH`
==================  =================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestATM(unittest.TestCase):

      def test_withdrawal_when_pin_is_right(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=True,
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

    TypeError: withdraw() got an unexpected keyword argument 'pin_is_right'

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

    def withdraw(pin_is_right):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got an unexpected keyword argument 'enough_balance'

* I add ``enough_balance`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(pin_is_right, enough_balance):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'CASH'

* I change the `return statement`_ to give me ``'CASH'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def withdraw(pin_is_right, enough_balance):
        return 'CASH'

  the test passes, this ATM works. The ``withdraw`` :ref:`function<what is a function?>` always returns :green:`CASH`, it does not care about the inputs. Is this :ref:`Tautology?<test_tautology>`

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

        def test_withdrawal_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

* I add an :ref:`if statement<if statements>` to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test passes

----

*********************************************************************************
test_withdrawal_when_pin_is_wrong
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered and the account balance is :green:`enough`, to  ``test_atm.py``

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:red:`wrong PIN`    :green:`yes`       :red:`DENIED`
==================  =================  =================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 16-22

      def test_withdrawal_when_pin_is_right(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'DENIED'
          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_withdrawal_when_pin_is_wrong(self):
          my_expectation = 'DENIED'
          reality = src.atm.withdraw(
              pin_is_right=False,
              enough_balance=True,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'CASH' != 'DENIED'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for this case to ``atm.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def withdraw(pin_is_right, enough_balance):
      if not pin_is_right and enough_balance:
          return 'DENIED'
      if pin_is_right and not enough_balance:
          return 'DENIED'
      return 'CASH'

the test passes. Is this :ref:`Exclusive Disjunction?<test_exclusive_disjunction>` or :ref:`Logical Equality<test_logical_equality>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`conditional expression<conditional expressions>` to test if it is :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_right, enough_balance):
        return (
            'DENIED' if pin_is_right != enough_balance
            else 'CASH'
        )
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green, and this :ref:`if statement<if statements>` is confusing

* I add a :ref:`conditional expression<conditional expressions>` for :ref:`Logical Equality<test_logical_equality>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_right, enough_balance):
        return (
            'CASH' if pin_is_right == enough_balance
            else 'DENIED'
        )
        return (
            'DENIED' if pin_is_right != enough_balance
            else 'CASH'
        )
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green, and this is also a confusing :ref:`if statement<if statements>`

* I add an :ref:`assertion<what is an assertion?>` for the last case - when the :red:`wrong PIN` is entered and the account balance is :red:`NOT enough`, to ``test_withdrawal_when_pin_is_wrong`` in ``test_atm.py``

  ==================  =================  =================
  PIN                 balance            withdrawal
  ==================  =================  =================
  :red:`wrong PIN`    :green:`yes`       :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :red:`DENIED`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 23-28


        def test_withdrawal_when_pin_is_wrong(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  this is not :ref:`Exclusive Disjunction<test_exclusive_disjunction>` or :ref:`Logical Equality<test_logical_equality>`

* I remove the :ref:`conditional expressions` then add an :ref:`if statement<if statements>` to ``atm.py`` for the last case

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(pin_is_right, enough_balance):
        if not pin_is_right and not enough_balance:
            return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test passes

* 3 of the cases return ``'DENIED'`` and only one case returns ``'CASH'``, this is :ref:`Logical Conjunction (AND)<test_logical_conjunction>`. I add an :ref:`if statement with an else clause<if statements>` for the one case that gives me ``'CASH'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right and enough_balance:
            return 'CASH'
        else:
            return 'DENIED'
        if not pin_is_right and not enough_balance:
            return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green

* I remove the :ref:`if statements` after the :ref:`else clause<if statements>`

  .. code-block:: python
    :linenos:

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right and enough_balance:
            return 'CASH'
        else:
            return 'DENIED'

  still green

* I do not need to make the ``my_expectation`` :ref:`variable<what is a variable?>` 2 times in ``test_withdrawal_when_pin_is_wrong`` since it is the same value both times. I remove the repetition from ``test_atm.py``

  .. code-block:: python
    :lineno-start: 22

        def test_withdrawal_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green

----

*********************************************************************************
test_withdrawal_w_daily_limit_when_pin_is_right
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

I want to add a condition for a daily limit on how much can be taken from the account.The inputs for the ATM will then be

* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will this put the account above or below the daily limit for withdrawals?

the :ref:`truth table` for the ATM will now be

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
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

I add an :ref:`assertion<what is an assertion?>` for the first case where the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals, to ``test_withdrawal_when_pin_is_right`` in ``test_atm.py``

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
==================  =================  ====================  ==================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 11-16

      def test_withdrawal_when_pin_is_right(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'DENIED'

          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=True,
              above_daily_limit=True,
          )
          self.assertEqual(reality, my_expectation)

          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_withdrawal_when_pin_is_wrong(self):

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
            pin_is_right, enough_balance,
            above_daily_limit,
        ):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    FAILED ...test_withdrawal_when_pin_is_right - TypeError: withdraw() missing 1 required positional argument: 'abo...
    FAILED ...test_withdrawal_when_pin_is_wrong - TypeError: withdraw() missing 1 required positional argument: 'abo...

  the other :ref:`assertions<what is an assertion?>` do not provide a value for ``above_daily_limit`` when they call the ``withdraw`` :ref:`function<what is a function?>`, I have to make it a choice

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        if pin_is_right and enough_balance:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

* I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

        if pin_is_right and enough_balance:
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I do not need to add anything to the first :ref:`assertion<what is an assertion?>` in ``test_withdrawal_when_pin_is_right`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  ==================  =================  ====================  ==================

  this means that

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=True,
        enough_balance=True,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=True,
        enough_balance=True,
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
    :emphasize-lines: 18-23

        def test_withdrawal_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_when_pin_is_wrong(self):

  the test is still green

* I do not need to add anything to the :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals, because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  =================  ====================  ==================

  this means that

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=True,
        enough_balance=False,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=True,
        enough_balance=False,
        above_daily_limit=False,
    )

* I change the name of the test from :ref:`test_withdrawal_when_pin_is_right` to :ref:`test_withdrawal_w_daily_limit_when_pin_is_right`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_withdrawal_w_daily_limit_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_withdrawal_w_daily_limit_when_pin_is_wrong
*********************************************************************************

* I add ``above_daily_limit`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_withdrawal_when_pin_is_wrong`, for the case where the :red:`wrong PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 7

        def test_withdrawal_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 11-15

        def test_withdrawal_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green. I do not need to give a value for the ``above_daily_limit`` parameter in the call to ``src.atm.withdraw`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=False,
        enough_balance=True,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=False,
        enough_balance=True,
        above_daily_limit=False,
    )

* I add ``above_daily_limit`` to the next :ref:`assertion<what is an assertion?>`, which is for when the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 20

        def test_withdrawal_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

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
    :lineno-start: 37
    :emphasize-lines: 24-27

        def test_withdrawal_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=False,
            )


    # Exceptions seen

  the test is still green. I do not need to give a value for the ``above_daily_limit`` parameter in the call to ``src.atm.withdraw`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=False,
        enough_balance=False,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        pin_is_right=False,
        enough_balance=False,
        above_daily_limit=False,
    )

* I change the name of the test from :ref:`test_withdrawal_when_pin_is_wrong` to :ref:`test_withdrawal_w_daily_limit_when_pin_is_wrong`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 7

            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_daily_limit_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

* There is only one case where the ``withdraw`` :ref:`function<what is a function?>` returns ``'CASH'``. I add :ref:`if statements` for the other cases to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5, 7-12

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        denial = 'DENIED'

        if not pin_is_right:
            return denial
        if not enough_balance:
            return denial
        if above_daily_limit:
            return denial

        if pin_is_right and enough_balance:
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  the test is still green. The ATM

  * :red:`denies` a withdrawal if the :red:`wrong PIN` is entered.
  * :red:`denies` a withdrawal if the account balance is :red:`NOT enough`. This only happens if the :green:`right PIN` is entered.
  * :red:`denies` a withdrawal if the account is :green:`above limit` for the daily withdrawal limit. This only happens if the account balance is :green:`enough`, which only happens if the :green:`right PIN` is entered.

* I add a `return statement`_ for the one case where the withdrawal is allowed

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        denial = 'DENIED'

        if not pin_is_right:
            return denial
        if not enough_balance:
            return denial
        if above_daily_limit:
            return denial

        return 'CASH'

        if pin_is_right and enough_balance:
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  still green. The ATM

  * :red:`denies` a withdrawal if the :red:`wrong PIN` is entered.
  * :red:`denies` a withdrawal if the account balance is :red:`NOT enough`. This only happens if the :green:`right PIN` is entered.
  * :red:`denies` a withdrawal if the account is :green:`above limit` for the daily withdrawal limit. This only happens if the account balance is :green:`enough`, which only happens if the :green:`right PIN` is entered.
  * :green:`approves` a withdrawal only if the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

* I remove the other statements

  .. code-block:: python
    :linenos:

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        denial = 'DENIED'

        if not pin_is_right:
            return denial
        if not enough_balance:
            return denial
        if above_daily_limit:
            return denial

        return 'CASH'

----

*********************************************************************************
test_withdrawal_w_expired_card_when_pin_is_right
*********************************************************************************

The :ref:`truth table` for the Automatic Teller Machine is now

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

I want to add a condition for when the bank card is expired. The inputs for the ATM will then be

* has the card expired?
* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will this put the account above or below the daily limit for withdrawals?

the :ref:`truth table` for the ATM will now be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
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

I add a value for the ``card_expired`` parameter to the call to the ``withdraw`` :ref:`function<what is a function?>` for the case where the card has :green:`expired`, the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals, in :ref:`test_withdrawal_w_daily_limit_when_pin_is_right` in ``test_atm.py``

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
==================  ==================  =================  ====================  =============

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 12

      def test_withdrawal_w_daily_limit_when_pin_is_right(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              pin_is_right=True,
              enough_balance=True,
          )
          self.assertEqual(reality, my_expectation)

          my_expectation = 'DENIED'

          reality = src.atm.withdraw(
              card_expired=True,
              pin_is_right=True,
              enough_balance=True,
              above_daily_limit=True,
          )
          self.assertEqual(reality, my_expectation)

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: withdraw() got an unexpected keyword argument 'card_expired'

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
            pin_is_right, enough_balance,
            above_daily_limit=False, card_expired,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`I cannot put a parameter that does NOT have a default value after a parameter that has a default value<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for ``card_expired``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False, card_expired=False,
        ):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the card has :green:`expired`, the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals, to ``test_withdrawal_when_pin_is_right`` in ``test_atm.py``

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19-25

        def test_withdrawal_w_daily_limit_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
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
            pin_is_right, enough_balance,
            above_daily_limit=False, card_expired=False,
        ):
        denial = 'DENIED'

        if card_expired:
            return denial
        if not pin_is_right:
            return denial
        if not enough_balance:
            return denial
        if above_daily_limit:
            return denial

        return 'CASH'

  the test passes. the ATM

  * :red:`denies` a withdrawal if the card has :green:`expired`, it will NOT check the PIN.
  * :red:`denies` a withdrawal if the :red:`wrong PIN` is entered, which only happens if the card has :red:`NOT expired`.
  * :red:`denies` a withdrawal if the account balance is :red:`NOT enough`, which only happens if the :green:`right PIN` is entered, which only happens if the card has :red:`NOT expired`.
  * :red:`denies` a withdrawal if the account is :green:`above limit` for the daily withdrawal limit, which only happens if the account balance is :green:`enough`, which only happens if the :green:`right PIN` is entered, which only happens if the card has :red:`NOT expired`.
  * :green:`approves` a withdrawal only if the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

* I add ``card_expired`` to the fourth :ref:`assertion<what is an assertion?>`, which is for when the card has :green:`expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals, in :ref:`test_withdrawal_w_daily_limit_when_pin_is_right` in ``test_atm.py``

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 28

        def test_withdrawal_w_daily_limit_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

  the test is still green

* I add ``card_expired`` to the fifth :ref:`assertion<what is an assertion?>`, I also add ``above_daily_limit`` to be clearer. This is for the case where the card has :green:`expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 36, 39

        def test_withdrawal_w_daily_limit_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_daily_limit_when_pin_is_wrong(self):

  still green

* I change the name of the test from :ref:`test_withdrawal_w_daily_limit_when_pin_is_right` to :ref:`test_withdrawal_w_expired_card_when_pin_is_right`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines:

    class TestATM(unittest.TestCase):

        def test_withdrawal_w_expired_card_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

  the case where the ATM gives me ``'CASH'`` no longer belongs in this test

----

*********************************************************************************
test_withdrawal_w_not_expired_card_when_pin_is_right
*********************************************************************************

* I add a new test for when the card has :red:`NOT expired` and move the case where the ATM gives me ``'CASH'`` to it

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-9

    class TestATM(unittest.TestCase):

        def test_withdrawal_w_not_expired_card_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_expired_card_when_pin_is_right(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

* I add an :ref:`assertion<what is an assertion?>` for when the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============


  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 11-17

        def test_withdrawal_w_not_expired_card_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_expired_card_when_pin_is_right(self):

  the test is still green

* I add values for the ``card_expired`` and ``above_daily_limit`` parameters to the :ref:`assertion<what is an assertion?>` for when the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4, 7

        def test_withdrawal_w_not_expired_card_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_expired_card_when_pin_is_right(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  :red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 21-27

        def test_withdrawal_w_not_expired_card_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_expired_card_when_pin_is_right(self):

  green

* I add an :ref:`assertion<what is an assertion?>` for when the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
  :red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 29-35

        def test_withdrawal_w_not_expired_card_when_pin_is_right(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_expired_card_when_pin_is_right(self):

  the test is still green.

----

*********************************************************************************
test_withdrawal_w_expired_card_when_pin_is_wrong
*********************************************************************************

* I change the name of :ref:`test_withdrawal_w_daily_limit_when_pin_is_wrong` to :ref:`test_withdrawal_w_expired_card_when_pin_is_wrong`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 9

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=True,
                enough_balance=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

* I add values for the ``card_expired`` and ``above_daily_limit`` parameters  to the :ref:`assertion<what is an assertion?>` for the case where the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                pin_is_right=False,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add an :ref:`assertion<what is an assertion?>` for the case where the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 13, 16

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

  green

* I add ``card_expired`` to the next :ref:`assertion<what is an assertion?>`, which is for when the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 21

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I values for the ``card_expired`` and ``above_daily_limit`` parameters to the last :ref:`assertion<what is an assertion?>`, for when the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 29, 32

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

----

*********************************************************************************
test_withdrawal_w_not_expired_card_when_pin_is_wrong
*********************************************************************************

* I add a new test, with an :ref:`assertion<what is an assertion?>` for when the card is :red:`NOT expired` and the :green:`wrong PIN` is entered, the balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 10, 12-18

            reality = src.atm.withdraw(
                card_expired=True,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdrawal_w_not_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I add the next :ref:`assertion<what is an assertion?>`, where the card has :red:`NOT expired`, the :red:`wrong PIN` is entered, the balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 12-18

        def test_withdrawal_w_not_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green

* I add an :ref:`assertion<what is an assertion?>` for when the card has :red:`NOT expired`, the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 20-26

        def test_withdrawal_w_not_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the card has :red:`NOT expired`, the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 28-34

        def test_withdrawal_w_not_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                pin_is_right=False,
                enough_balance=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the tests are all green

----

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdrawal_w_not_expired_card_when_pin_is_wrong` because I do not need them, I can call the ``withdraw`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_withdrawal_w_not_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )


    # Exceptions seen

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdrawal_w_expired_card_when_pin_is_wrong` as well, I can call the ``withdraw`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):
            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )

        def test_withdrawal_w_not_expired_card_when_pin_is_wrong(self):

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdrawal_w_expired_card_when_pin_is_right` next

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_withdrawal_w_expired_card_when_pin_is_right(self):
            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )

        def test_withdrawal_w_expired_card_when_pin_is_wrong(self):

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdrawal_w_not_expired_card_when_pin_is_right`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-9, 15-21, 25-31, 35-41

        def test_withdrawal_w_not_expired_card_when_pin_is_right(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                'CASH'
            )

            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )

        def test_withdrawal_w_expired_card_when_pin_is_right(self):

  all tests are green

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

I ran tests for an Automatic Teller Machine with the following inputs:

* has the card expired?
* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will this put the account above or below the daily limit for withdrawals?

the inputs gave me this :ref:`truth table`

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

What if I want the ATM to give a different message with each denial, so that the user knows why the withdrawal failed? The :ref:`truth table` could then be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED: Card Expired`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED: Card Expired`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED: Card Expired`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED: Card Expired`
==================  ==================  =================  ====================  =============

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED: You have exceeded the daily withdrawal Limit`
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED: There is not enough money in the account to complete the withdrawal`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED: There is not enough money in the account to complete the withdrawal`
==================  ==================  =================  ====================  =============


==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`Error: You entered the wrong PIN. Try again`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`Error: You entered the wrong PIN. Try again`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`Error: You entered the wrong PIN. Try again`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`Error: You entered the wrong PIN. Try again`
==================  ==================  =================  ====================  =============

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