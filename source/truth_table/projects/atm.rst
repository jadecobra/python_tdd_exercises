.. meta::
  :description: Learn Python boolean logic by building a real-world ATM withdrawal system. This step-by-step Test-Driven Development (TDD) tutorial teaches beginners how to translate truth tables into clean Python code using unittest, uv, and pytest-watcher.
  keywords: Python ATM project tutorial, translate truth tables to python code, TDD python exercises for beginners, learn boolean logic with python projects, python unittest step by step guide, how to use uv for python projects, pytest-watcher tutorial, red green refactor python example, automatic teller machine logic python, Jacob Itegboje

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
:red:`wrong PIN`    :green:`enough`    :red:`DENIED`
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

  the terminal_ shows I am in the ``atm`` folder_

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

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

  the terminal_ goes back to the command line

* I add `pytest-watcher`_ to the requirements file_

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

* I use tree_ to look at the structure of the project

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── README.md
    ├── pyproject.toml
    ├── requirements.txt
    ├── src
    │   └── atm.py
    └── tests
        ├── __init__.py
        └── test_atm.py

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

  because :ref:`True<test_what_is_true>` is not :ref:`False<test_what_is_false>`

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` have 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    fix those errors then try to run ``uv run pytest-watcher . --now`` again

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
test_withdraw_w_right_pin
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered, is

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:green:`right PIN`  :green:`enough`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :red:`DENIED`
==================  =================  =================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to ``test_withdraw_w_right_pin``, then add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered and the amount in the account is :green:`enough`

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:green:`right PIN`  :green:`enough`    :green:`CASH`
==================  =================  =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestATM(unittest.TestCase):

      def test_withdraw_w_right_pin(self):
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

because I do not have a definition for ``src`` in this file_

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

  because ``atm.py`` in the ``src`` folder_ does not have anything named ``withdraw`` in it

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

  because I called the ``withdraw`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only allows calls with 0 arguments

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

  because I called the ``withdraw`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only allows calls with 1 input

* I add ``enough_balance`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(pin_is_right, enough_balance):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'CASH'

  the ``withdraw`` :ref:`function<what is a function?>` always returns :ref:`None<what is None?>` and the test expects ``'CASH'``

* I change the `return statement`_ to give me ``'CASH'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def withdraw(pin_is_right, enough_balance):
        return 'CASH'

  the test passes, this ATM works. The ``withdraw`` :ref:`function<what is a function?>` always returns :green:`'CASH'`, it does not care about the inputs. Is this :ref:`Tautology<test_tautology>` or :green:`'CASH'` that never ends?

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

        def test_withdraw_w_right_pin(self):
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

  because the ``withdraw`` :ref:`function<what is a function?>` returns :green:`'CASH'` and the test expects :red:`'DENIED'`

* I add an :ref:`if statement<if statements>` to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right == True:
            if enough_balance == False:
                return 'DENIED'
        return 'CASH'

  the test passes

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == True:
        if bool(pin_is_right) == True:
            # if enough_balance == False:
            if bool(enough_balance) == False:
                return 'DENIED'
        return 'CASH'

  the test is still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the second :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == True:
        if bool(pin_is_right) == True:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            if not bool(enough_balance) == True:
                return 'DENIED'
        return 'CASH'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4, 7-8

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == True:
        # if bool(pin_is_right) == True:
        if bool(pin_is_right):
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            if not bool(enough_balance):
                return 'DENIED'
        return 'CASH'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 9-10

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == True:
        # if bool(pin_is_right) == True:
        # if bool(pin_is_right):
        if pin_is_right:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            # if not bool(enough_balance):
            if not enough_balance:
                return 'DENIED'
        return 'CASH'

  still green because

  - ``if bool(something) == True`` is the same as ``if something``
  - ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5, 10-12

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == True:
        # if bool(pin_is_right) == True:
        # if bool(pin_is_right):
        # if pin_is_right:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            # if not bool(enough_balance):
            # if not enough_balance:
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  still green.

The ``withdraw`` :ref:`function<what is a function?>`

* returns :red:`'DENIED'` if the :green:`right PIN` is entered AND the balance is :red:`NOT enough`
* returns :green:`'CASH'` if the first condition is NOT met

What :ref:`binary operation<truth table: Binary Operations>` is the ``withdraw`` :ref:`function<what is a function?>` using?

----

*********************************************************************************
test_withdraw_w_wrong_pin
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered, is

==================  =================  =================
PIN                 balance            withdrawal
==================  =================  =================
:red:`wrong PIN`    :green:`enough`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`DENIED`
==================  =================  =================

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

      def test_withdraw_w_right_pin(self):
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

      def test_withdraw_w_wrong_pin(self):
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

because the ``withdraw`` :ref:`function<what is a function?>` returned :green:`'CASH'` and the test expects :red:`DENIED`. Why is this ATM giving :green:`'CASH'` when the :red:`wrong PIN` is entered?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` for this case to ``atm.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-4

  def withdraw(pin_is_right, enough_balance):
      if pin_is_right == False:
          if enough_balance == True:
              return 'DENIED'
      if pin_is_right and not enough_balance:
          return 'DENIED'
      return 'CASH'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        if bool(pin_is_right) == False:
            # if enough_balance == True:
            if bool(enough_balance) == True:
                return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the first :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        if not bool(pin_is_right) == True:
            # if enough_balance == True:
            if bool(enough_balance) == True:
                return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 7-8

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        if not bool(pin_is_right):
            # if enough_balance == True:
            # if bool(enough_balance) == True:
            if bool(enough_balance):
                return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6, 9-10

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        # if not bool(pin_is_right):
        if not pin_is_right:
            # if enough_balance == True:
            # if bool(enough_balance) == True:
            # if bool(enough_balance):
            if enough_balance:
                return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  still green because

  - ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``
  - ``if bool(something) == True`` is the same as ``if something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6, 10-12

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        # if not bool(pin_is_right):
        # if not pin_is_right:
            # if enough_balance == True:
            # if bool(enough_balance) == True:
            # if bool(enough_balance):
            # if enough_balance:
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green. Is this :ref:`Exclusive Disjunction?<test_exclusive_disjunction>` or :ref:`Logical Equality<test_logical_equality>`

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def withdraw(pin_is_right, enough_balance):
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  The ``withdraw`` :ref:`function<what is a function?>`

  - returns :red:`'DENIED'` if the :red:`wrong PIN` is entered AND the balance is :green:`enough`
  - returns :red:`'DENIED'` if the :green:`right PIN` is entered AND the balance is :red:`NOT enough`
  - returns :green:`'CASH'` if none of the conditions are met

* I add an :ref:`if statement<if statements>` to test if it is :ref:`Exclusive Disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-10

    def withdraw(pin_is_right, enough_balance):
        # if not pin_is_right and enough_balance:
        #     return 'DENIED'
        # if pin_is_right and not enough_balance:
        #     return 'DENIED'
        # return 'CASH'
        if pin_is_right != enough_balance:
            return 'DENIED'
        else:
            return 'CASH'

  the test is still green, and this :ref:`if statement<if statements>` is confusing

* I add another :ref:`if statement<if statements>` for :ref:`Logical Equality<test_logical_equality>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-14

    def withdraw(pin_is_right, enough_balance):
        # if not pin_is_right and enough_balance:
        #     return 'DENIED'
        # if pin_is_right and not enough_balance:
        #     return 'DENIED'
        # return 'CASH'
        # if pin_is_right != enough_balance:
        #     return 'DENIED'
        # else:
        #     return 'CASH'
        if pin_is_right == enough_balance:
            return 'CASH'
        else:
            return 'DENIED'

  the test is still green, and this is also confusing

* I add an :ref:`assertion<what is an assertion?>` for the last case - when the :red:`wrong PIN` is entered and the account balance is :red:`NOT enough`, to ``test_withdraw_w_wrong_pin`` in ``test_atm.py``

  ==================  =================  =================
  PIN                 balance            withdrawal
  ==================  =================  =================
  :red:`wrong PIN`    :green:`yes`       :red:`DENIED`
  :red:`wrong PIN`    :red:`NOT enough`  :red:`DENIED`
  ==================  =================  =================

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 9-13

        def test_withdraw_w_wrong_pin(self):
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

  - I do not need to make a new ``my_expectation`` :ref:`variable<what is a variable?>` because the expectation for the new :ref:`assertion<what is an assertion?>` is the same as the last one (:red:`'DENIED'`)
  - the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      AssertionError: 'CASH' != 'DENIED'

    this is not :ref:`Exclusive Disjunction<test_exclusive_disjunction>` or :ref:`Logical Equality<test_logical_equality>`

* I remove the :ref:`if statements` for :ref:`Exclusive Disjunction<test_exclusive_disjunction>` and :ref:`Logical Equality<test_logical_equality>`, then add :ref:`if statements` for the last case, to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines:

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right == False:
            if enough_balance == False:
                return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test passes

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-5

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        if bool(pin_is_right) == False:
            # if enough_balance == False:
            if bool(enough_balance) == False:
                return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statements` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4, 6-7

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        if not bool(pin_is_right) == True:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            if not bool(enough_balance) == True:
                return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5, 8-9

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        if not bool(pin_is_right):
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            if not bool(enough_balance):
                return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6, 10-11

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        # if not bool(pin_is_right):
        if not pin_is_right:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            # if not bool(enough_balance):
            if not enough_balance:
                return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  still green because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the two :ref:`if statements` together

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6, 11-13

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        # if not bool(pin_is_right):
        # if not pin_is_right:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            # if not bool(enough_balance):
            # if not enough_balance:
        if not pin_is_right and not enough_balance:
            return 'DENIED'
        if not pin_is_right and enough_balance:
            return 'DENIED'
        if pin_is_right and not enough_balance:
            return 'DENIED'
        return 'CASH'

  the test is still green

* 3 of the cases return ``'DENIED'`` and only one case returns ``'CASH'``, this is :ref:`Logical Conjunction (AND)<test_logical_conjunction>`. I add an :ref:`if statement with an else clause<if statements>` for the one case that gives me ``'CASH'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 16-22

    def withdraw(pin_is_right, enough_balance):
        # if pin_is_right == False:
        # if bool(pin_is_right) == False:
        # if not bool(pin_is_right) == True:
        # if not bool(pin_is_right):
        # if not pin_is_right:
            # if enough_balance == False:
            # if bool(enough_balance) == False:
            # if not bool(enough_balance) == True:
            # if not bool(enough_balance):
            # if not enough_balance:
        # if not pin_is_right and not enough_balance:
        #     return 'DENIED'
        # if not pin_is_right and enough_balance:
        #     return 'DENIED'
        # if pin_is_right and not enough_balance:
        #     return 'DENIED'
        # return 'CASH'
        if pin_is_right and enough_balance:
            return 'CASH'
        else:
            return 'DENIED'

  the test is still green

* I remove the comments

  .. code-block:: python
    :linenos:

    def withdraw(pin_is_right, enough_balance):
        if pin_is_right and enough_balance:
            return 'CASH'
        else:
            return 'DENIED'

  The ``withdraw`` :ref:`function<what is a function?>`

  - returns :green:`'CASH'` if the :green:`right PIN` is entered AND the balance is :green:`enough`
  - returns :red:`'DENIED'` if the above condition is NOT met

----

*********************************************************************************
test_withdraw_w_daily_limit_w_right_pin
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

I want to add a condition for a daily limit on how much can be taken from the account. The inputs for the ATM will then be

* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will this put the account above or below the daily limit for withdrawals?

The :ref:`truth table` for if the :green:`right PIN` is entered, will be

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` for the first case where the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals, to ``test_withdraw_w_right_pin`` in ``test_atm.py``

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
==================  =================  ====================  ==================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 11-16

      def test_withdraw_w_right_pin(self):
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

      def test_withdraw_w_wrong_pin(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: withdraw() got an unexpected keyword argument 'above_daily_limit'

because the ``withdraw`` :ref:`function<what is a function?>` only takes 2 arguments (``pin_is_right`` and ``enough_balance``) and the new :ref:`assertion<what is an assertion?>` called it with 3 arguments (``pin_is_right``, ``enough_balance`` and ``above_daily_limit``)

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

    FAILED ...test_withdraw_w_right_pin - TypeError: withdraw() missing 1 required positional argument: 'abo...
    FAILED ...test_withdraw_w_wrong_pin - TypeError: withdraw() missing 1 required positional argument: 'abo...

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

  because the ``withdraw`` :ref:`function<what is a function?>` returns :green:`'CASH'` and the test expects :red:`'DENIED'`

* I add an :ref:`if statement<if statements>` for this case

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        if pin_is_right and enough_balance:
            if above_daily_limit == True:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  the test passes

* I add the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        if pin_is_right and enough_balance:
            # if above_daily_limit == True:
            if bool(above_daily_limit) == True:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        if pin_is_right and enough_balance:
            # if above_daily_limit == True:
            # if bool(above_daily_limit) == True:
            if bool(above_daily_limit):
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  still green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        if pin_is_right and enough_balance:
            # if above_daily_limit == True:
            # if bool(above_daily_limit) == True:
            # if bool(above_daily_limit):
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  green, because ``if bool(something) == True`` is the same as ``if something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        if pin_is_right and enough_balance:
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  This is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

  - if the :green:`right PIN` is entered AND the balance is :green:`enough`

    * it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals
    * it returns :green:`'CASH'` if the account is :red:`below limit` for daily withdrawals

  - it returns :red:`DENIED` if none of the above conditions are met

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I do not need to add anything to the first :ref:`assertion<what is an assertion?>` in ``test_withdraw_w_right_pin`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

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

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

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

        def test_withdraw_w_right_pin(self):
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

        def test_withdraw_w_wrong_pin(self):

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

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

* I change the name of the test from :ref:`test_withdraw_w_right_pin` to :ref:`test_withdraw_w_daily_limit_w_right_pin`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_withdraw_w_daily_limit_w_right_pin(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_withdraw_w_daily_limit_w_wrong_pin
*********************************************************************************

The :ref:`truth table` for if the :green:`wrong PIN` is entered, will be

==================  =================  ====================  ==================
PIN                 balance            daily limit           withdrawal
==================  =================  ====================  ==================
:red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  =================  ====================  ==================

* I add ``above_daily_limit`` to the first :ref:`assertion<what is an assertion?>` in :ref:`test_withdraw_w_wrong_pin`, for the case where the :red:`wrong PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals

  ==================  =================  ====================  ==================
  PIN                 balance            daily limit           withdrawal
  ==================  =================  ====================  ==================
  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
  ==================  =================  ====================  ==================

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 7

        def test_withdraw_w_wrong_pin(self):
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

        def test_withdraw_w_wrong_pin(self):
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

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

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

        def test_withdraw_w_wrong_pin(self):
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
    :emphasize-lines: 24-28

        def test_withdraw_w_wrong_pin(self):
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
            self.assertEqual(reality, my_expectation)


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

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

* I change the name of the test from :ref:`test_withdraw_w_wrong_pin` to :ref:`test_withdraw_w_daily_limit_w_wrong_pin`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 7

            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdraw_w_daily_limit_w_wrong_pin(self):
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
        denied = 'DENIED'

        if not pin_is_right:
            return denied
        if not enough_balance:
            return denied
        if above_daily_limit:
            return denied

        if pin_is_right and enough_balance:
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  the test is still green

* I add a `return statement`_ for the one case where the withdrawal is allowed

  .. code-block:: python
    :linenos:
    :emphasize-lines: 14

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        denied = 'DENIED'

        if not pin_is_right:
            return denied
        if not enough_balance:
            return denied
        if above_daily_limit:
            return denied

        return 'CASH'

        if pin_is_right and enough_balance:
            if above_daily_limit:
                return 'DENIED'
            return 'CASH'
        else:
            return 'DENIED'

  still green

* I remove the other statements

  .. code-block:: python
    :linenos:

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False,
        ):
        denied = 'DENIED'

        if not pin_is_right:
            return denied
        if not enough_balance:
            return denied
        if above_daily_limit:
            return denied

        return 'CASH'

This is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

* if the :red:`wrong PIN` is entered it returns :red:`'DENIED'`
* if the :green:`right PIN` is entered

  - it returns :red:`'DENIED'` if the balance in the account is :red:`NOT enough`
  - if the balance in the account is :green:`enough`

    * it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals

* it returns :green:`'CASH'` if none of the above conditions are met

----

*********************************************************************************
test_withdraw_w_expired_card_w_right_pin
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

The :ref:`truth table` for if the card has :green:`expired` AND the :green:`right PIN` is entered, will be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for the ``card_expired`` parameter to the call to the ``withdraw`` :ref:`function<what is a function?>` for the case where the card has :green:`expired`, the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :green:`above limit` for daily withdrawals, in the second :ref:`assertion<what is an assertion?>` in :ref:`test_withdraw_w_daily_limit_w_right_pin` in ``test_atm.py``

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
==================  ==================  =================  ====================  =============

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 12

      def test_withdraw_w_daily_limit_w_right_pin(self):
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

because the ``withdraw`` :ref:`function<what is a function?>` only takes 3 arguments (``pin_is_right``, ``enough_balance`` and ``above_daily_limit``) and the test called it with 4 arguments (``card_expired``, ``pin_is_right``, ``enough_balance`` and ``above_daily_limit``)

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

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_arguments>`

* I add a :ref:`default value<test_functions_w_default_arguments>` for ``card_expired``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False, card_expired=False,
        ):

  the test passes. This is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

  * if the :red:`wrong PIN` is entered it returns :red:`'DENIED'`
  * if the :green:`right PIN` is entered

    - it returns :red:`'DENIED'` if the balance in the account is :red:`NOT enough`
    - if the balance in the account is :green:`enough`

      * it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals

  * it returns :green:`'CASH'` if none of the above conditions are met

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the card has :green:`expired`, the :green:`right PIN` is entered, the account balance is :green:`enough` and the account is :red:`below limit` for daily withdrawals, to ``test_withdraw_w_right_pin`` in ``test_atm.py``

  ==================  ==================  =================  ====================  =============
  card expired        PIN                 balance            daily limit           withdrawal
  ==================  ==================  =================  ====================  =============
  :green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
  :green:`expired`    :green:`right PIN`  :green:`enough`    :red:`below limit`    :red:`DENIED`
  ==================  ==================  =================  ====================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 19-25

        def test_withdraw_w_daily_limit_w_right_pin(self):
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
        denied = 'DENIED'

        if card_expired:
            return denied
        if not pin_is_right:
            return denied
        if not enough_balance:
            return denied
        if above_daily_limit:
            return denied

        return 'CASH'

  the test passes. This is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

  * if the card has :green:`expired` it returns :red:`'DENIED'`
  * if the card has :red:`NOT expired`

    - if the :red:`wrong PIN` is entered it returns :red:`'DENIED'`
    - if the :green:`right PIN` is entered

      * it returns :red:`'DENIED'` if the balance in the account is :red:`NOT enough`
      * if the balance in the account is :green:`enough`

        - it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals

  * it returns :green:`'CASH'` if none of the above conditions are met

* I add ``card_expired`` to the fourth :ref:`assertion<what is an assertion?>`, which is for when the card has :green:`expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :green:`above limit` for daily withdrawals, in :ref:`test_withdraw_w_daily_limit_w_right_pin` in ``test_atm.py``

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

        def test_withdraw_w_daily_limit_w_right_pin(self):
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

* I add ``card_expired`` to the fifth :ref:`assertion<what is an assertion?>`, I also add ``above_daily_limit`` to make it clearer. This is for the case where the card has :green:`expired`, the :green:`right PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

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

        def test_withdraw_w_daily_limit_w_right_pin(self):
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

        def test_withdraw_w_daily_limit_w_wrong_pin(self):

  still green

* I change the name of the test from :ref:`test_withdraw_w_daily_limit_w_right_pin` to :ref:`test_withdraw_w_expired_card_w_right_pin`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_withdraw_w_expired_card_w_right_pin(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

  the case where the ATM gives me ``'CASH'`` no longer belongs in this test

----

*********************************************************************************
test_withdraw_w_not_expired_card_w_right_pin
*********************************************************************************

The :ref:`truth table` for if the card has :red:`NOT expired` AND the :green:`right PIN` is entered, will be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :red:`below limit`    :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============


* I add a new test for when the card has :red:`NOT expired` and move the case where the ATM gives me ``'CASH'`` to the new test

  .. TIP:: I can move lines I select or where the cursor is, with :kbd:`alt/option+Up` on the keyboard to move lines up or  :kbd:`alt/option+Down` to move lines down

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-9

    class TestATM(unittest.TestCase):

        def test_withdraw_w_not_expired_card_w_right_pin(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                pin_is_right=True,
                enough_balance=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_withdraw_w_expired_card_w_right_pin(self):
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
    :emphasize-lines: 9, 11-17

        def test_withdraw_w_not_expired_card_w_right_pin(self):
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

        def test_withdraw_w_expired_card_w_right_pin(self):

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

        def test_withdraw_w_not_expired_card_w_right_pin(self):
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

        def test_withdraw_w_expired_card_w_right_pin(self):

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

        def test_withdraw_w_not_expired_card_w_right_pin(self):
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

        def test_withdraw_w_expired_card_w_right_pin(self):

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

        def test_withdraw_w_not_expired_card_w_right_pin(self):
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

        def test_withdraw_w_expired_card_w_right_pin(self):

  the test is still green.

----

*********************************************************************************
test_withdraw_w_expired_card_w_wrong_pin
*********************************************************************************

The :ref:`truth table` for if the card has :green:`expired` AND the :red:`wrong PIN` is entered, will be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

* I change the name of :ref:`test_withdraw_w_daily_limit_w_wrong_pin` to :ref:`test_withdraw_w_expired_card_w_wrong_pin`

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

        def test_withdraw_w_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_expired_card_w_wrong_pin(self):
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

* I add values for the ``card_expired`` and ``above_daily_limit`` parameters to the last :ref:`assertion<what is an assertion?>`, for when the card has :green:`expired`, the :red:`wrong PIN` is entered, the balance is :red:`NOT enough` and the account is :red:`below limit` for daily withdrawals

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

        def test_withdraw_w_expired_card_w_wrong_pin(self):
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
test_withdraw_w_not_expired_card_w_wrong_pin
*********************************************************************************

The :ref:`truth table` for if the card has :red:`NOT expired` AND the :red:`wrong PIN` is entered, will be

==================  ==================  =================  ====================  =============
card expired        PIN                 balance            daily limit           withdrawal
==================  ==================  =================  ====================  =============
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`below limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :red:`below limit`    :red:`DENIED`
==================  ==================  =================  ====================  =============

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

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):
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

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdraw_w_not_expired_card_w_wrong_pin` because I do not need them, I can call the ``withdraw`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):
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

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdraw_w_expired_card_w_wrong_pin` as well, I can call the ``withdraw`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_withdraw_w_expired_card_w_wrong_pin(self):
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

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdraw_w_expired_card_w_right_pin` next

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_withdraw_w_expired_card_w_right_pin(self):
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

        def test_withdraw_w_expired_card_w_wrong_pin(self):

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_withdraw_w_not_expired_card_w_right_pin`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-9, 15-21, 25-31, 35-41

        def test_withdraw_w_not_expired_card_w_right_pin(self):
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

        def test_withdraw_w_expired_card_w_right_pin(self):

* I add a :ref:`global variable<what is a variable?>` for ``'DENIED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.atm
    import unittest


    DENIED = 'DENIED'


    class TestATM(unittest.TestCase):

* I use the new :ref:`variable<what is a variable?>` to remove repetition from :ref:`test_withdraw_w_not_expired_card_w_right_pin`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12, 21-22, 32-33, 43-44

        def test_withdraw_w_not_expired_card_w_right_pin(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                'CASH'
            )

            # my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                # my_expectation
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                # my_expectation
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                # my_expectation
                DENIED
            )

        def test_withdraw_w_expired_card_w_right_pin(self):

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_withdraw_w_not_expired_card_w_right_pin(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                'CASH'
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                DENIED
            )

        def test_withdraw_w_expired_card_w_right_pin(self):

* I do the same thing in :ref:`test_withdraw_w_expired_card_w_right_pin`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 9, 19, 29, 39

        def test_withdraw_w_expired_card_w_right_pin(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=True,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                DENIED
            )

        def test_withdraw_w_expired_card_w_wrong_pin(self):

* also in :ref:`test_withdraw_w_expired_card_w_wrong_pin`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 9, 19, 29, 39

        def test_withdraw_w_expired_card_w_wrong_pin(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                DENIED
            )

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):

* and in :ref:`test_withdraw_w_not_expired_card_w_wrong_pin`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 9, 19, 29, 39

        def test_withdraw_w_not_expired_card_w_wrong_pin(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=True,
                    above_daily_limit=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    pin_is_right=False,
                    enough_balance=False,
                    above_daily_limit=False,
                ),
                DENIED
            )


    # Exceptions seen

  all tests are still green

* The ``withdraw`` :ref:`function<what is a function?>` could also be written using :ref:`Logical Conjunction (AND)<test_logical_conjunction>` for the one case where the ATM gives me :green:`'CASH'`, in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-12

    def withdraw(
            pin_is_right, enough_balance,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'

        if (
            not card_expired and pin_is_right
            and enough_balance and not above_daily_limit
        ):
            return 'CASH'
        return denied

  all the tests are still passing. Which do you like better? Time to eat.

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

I ran tests for an Automatic Teller Machine with these inputs:

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

The ATM only gives me ``'CASH'`` when the card has :red:`NOT expired`, the :green:`right PIN` is entered, the balance is :green:`enough` for the withdrawal, and the account is :red:`below limit` for daily withdrawals.

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

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`

:ref:`Would you like to test making a Microwave?<Microwave>`

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