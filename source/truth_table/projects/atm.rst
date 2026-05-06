.. meta::
  :description: Learn Python boolean logic by building a real-world ATM withdrawal system. This step-by-step Test-Driven Development (TDD) tutorial teaches beginners how to translate truth tables into clean Python code using unittest, uv, and pytest-watcher.
  keywords: Python ATM project tutorial, translate truth tables to python code, TDD python exercises for beginners, learn boolean logic with python projects, python unittest step by step guide, how to use uv for python projects, pytest-watcher tutorial, red green refactor python example, Automated Teller Machine logic python, Jacob Itegboje

.. include:: ../../links.rst

.. _atm:

#################################################################################
Automated Teller Machine
#################################################################################

----

I want to make an **Automated Teller Machine** that allows withdrawals or denies them, if the inputs are

* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?

this is the :ref:`truth table` I get

==================  ======================= =================
PIN                 money                   withdrawal
==================  ======================= =================
:green:`right PIN`  :green:`enough money`   :green:`CASH`
:green:`right PIN`  :red:`NOT enough money` :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough money` :red:`DENIED`
==================  ======================= =================

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
* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init atm

  the terminal_ shows

  .. code-block:: shell

    Initialized project `atm` at `.../pumping_python/atm`

  then goes back to the command line

* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd atm

  the terminal_ shows I am in the ``atm`` folder_

  .. code-block:: shell

    .../pumping_python/atm

* I remove ``main.py`` from the project because I do not use it

  .. code-block:: python
    :emphasize-lines: 1

    rm main.py

  the terminal_ goes back to the command line

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

* I install the `Python packages`_ that I wrote in the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

  the terminal_ shows that it installed the `Python packages`_

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
    ├── tests
    │   ├── __init__.py
    │   └── test_atm.py
    └── uv.lock

  if you do not see ``uv.lock`` in your tree, make sure you ran ``uv add --requirement requirements.txt``, then run the tests next

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ======================== FAILURES ========================
    _________________ TestATM.test_failure ___________________

    self = <tests.test_atm.TestATM testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_atm.py:7: AssertionError
    ================ short test summary info =================
    FAILED tests/test_atm.py::TestATM::test_failure - AssertionError: True is not false
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`

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
test_right_pin_enough_money
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change ``test_failure`` to :ref:`test_right_pin_enough_money`, then add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered and there is :green:`enough money` in the account

==================  ======================= =================
PIN                 money                   withdrawal
==================  ======================= =================
:green:`right PIN`  :green:`enough money`   :green:`CASH`
==================  ======================= =================

.. code-block:: python
  :lineno-start: 4
  :emphasize-lines: 3-9

  class TestATM(unittest.TestCase):

      def test_right_pin_enough_money(self):
          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              right_pin=True,
              enough_money=True,
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

* I add an `import statement`_ at the top of the file_ so that I can test ``atm.py`` from the ``src`` folder_

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

  .. admonition:: If you get :ref:`ModuleNotFoundError<what is a module?>`

    .. code-block:: python

      ModuleNotFoundError: No module named 'src'

    check if you have ``__init__.py`` in the ``tests`` folder_ with underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``, then add :ref:`ModuleNotFoundError<what is a module?>` to the list of :ref:`Exceptions<errors>` seen

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

  I use the :ref:`Explorer<explorer on left>` to open ``atm.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* I add a :ref:`function<what is a function?>` to ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def withdraw():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got an unexpected keyword argument 'right_pin'

  because the test called the ``withdraw`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only takes calls with 0 arguments

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

    def withdraw(right_pin):
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: withdraw() got an unexpected keyword argument 'enough_money'

  because the test called the ``withdraw`` :ref:`function<what is a function?>` with 2 keyword arguments and this definition only takes calls with 1 input

* I add ``enough_money`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def withdraw(right_pin, enough_money):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'CASH'

  the ``withdraw`` :ref:`function<what is a function?>` always returns :ref:`None<what is None?>` and the test expects ``'CASH'``

* I change the `return statement`_ to give me ``'CASH'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def withdraw(right_pin, enough_money):
        return 'CASH'

  the test passes, this ATM works. The ``withdraw`` :ref:`function<what is a function?>` always returns :green:`'CASH'`, it does not care about the inputs. Is this :ref:`Tautology<test_tautology>` or :green:`'CASH'` that never ends?

----

*********************************************************************************
test_right_pin_not_enough_money
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a test with an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered AND there is :red:`NOT enough money` in the account

  ==================  ======================= =================
  PIN                 money                   withdrawal
  ==================  ======================= =================
  :green:`right PIN`  :red:`NOT enough money` :red:`DENIED`
  ==================  ======================= =================

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-15

        def test_right_pin_enough_money(self):
            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_right_pin_not_enough_money(self):
            my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  because the ``withdraw`` :ref:`function<what is a function?>` returns :green:`'CASH'` and the test expects :red:`'DENIED'`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``atm.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def withdraw(right_pin, enough_money):
      if enough_money == False:
          return 'DENIED'

      return 'CASH'

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def withdraw(right_pin, enough_money):
        # if enough_money == False:
        if bool(enough_money) == False:
            return 'DENIED'

        return 'CASH'

  the test is still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def withdraw(right_pin, enough_money):
        # if enough_money == False:
        # if bool(enough_money) == False:
        if not bool(enough_money) == True:
            return 'DENIED'

        return 'CASH'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def withdraw(right_pin, enough_money):
        # if enough_money == False:
        # if bool(enough_money) == False:
        # if not bool(enough_money) == True:
        if not bool(enough_money):
            return 'DENIED'

        return 'CASH'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(right_pin, enough_money):
        # if enough_money == False:
        # if bool(enough_money) == False:
        # if not bool(enough_money) == True:
        # if not bool(enough_money):
        if not enough_money:
            return 'DENIED'

        return 'CASH'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def withdraw(right_pin, enough_money):
        if not enough_money:
            return 'DENIED'

        return 'CASH'

  the test is still green.

This is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

* it returns :red:`'DENIED'` if there is :red:`NOT enough money` in the account
* it gives me :green:`'CASH'` if the :ref:`condition<if statements>`is NOT met

What :ref:`binary operation<truth table: Binary Operations>` is the ``withdraw`` :ref:`function<what is a function?>` using?

----

*********************************************************************************
test_wrong_pin_enough_money
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered and there is :green:`enough money` in the account, to  ``test_atm.py``

==================  ======================= =================
PIN                 money                   withdrawal
==================  ======================= =================
:red:`wrong PIN`    :green:`enough money`   :red:`DENIED`
==================  ======================= =================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 9-15

      def test_right_pin_not_enough_money(self):
          my_expectation = 'DENIED'
          reality = src.atm.withdraw(
              right_pin=True,
              enough_money=False,
          )
          self.assertEqual(reality, my_expectation)

      def test_wrong_pin_enough_money(self):
          my_expectation = 'DENIED'
          reality = src.atm.withdraw(
              right_pin=False,
              enough_money=True,
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
  :emphasize-lines: 2-3

  def withdraw(right_pin, enough_money):
      if right_pin == False:
          return 'DENIED'

      if not enough_money:
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
    :emphasize-lines: 2-3

    def withdraw(right_pin, enough_money):
        # if right_pin == False:
        if bool(right_pin) == False:
            return 'DENIED'

        if not enough_money:
            return 'DENIED'

        return 'CASH'

  the test is still green

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write the :ref:`if statement<if statements>` in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    def withdraw(right_pin, enough_money):
        # if right_pin == False:
        # if bool(right_pin) == False:
        if not bool(right_pin) == True:
            return 'DENIED'

        if not enough_money:
            return 'DENIED'

        return 'CASH'

  still green

* I remove ``== True``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    def withdraw(right_pin, enough_money):
        # if right_pin == False:
        # if bool(right_pin) == False:
        # if not bool(right_pin) == True:
        if not bool(right_pin):
            return 'DENIED'

        if not enough_money:
            return 'DENIED'

        return 'CASH'

  green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(right_pin, enough_money):
        # if right_pin == False:
        # if bool(right_pin) == False:
        # if not bool(right_pin) == True:
        # if not bool(right_pin):
        if not right_pin:
            return 'DENIED'

        if not enough_money:
            return 'DENIED'

        return 'CASH'

  still green, because ``if bool(something) == False`` is the same as ``if not bool(something) == True`` is the same as ``if not something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def withdraw(right_pin, enough_money):
        if not right_pin:
            return 'DENIED'

        if not enough_money:
            return 'DENIED'

        return 'CASH'

  this is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

  * it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered
  * it returns :red:`'DENIED'` if there is :red:`NOT enough money` in the account
  * it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met

  What :ref:`binary operation<truth table: Binary Operations>` is the ``withdraw`` :ref:`function<what is a function?>` using now?

----

*********************************************************************************
test_wrong_pin_not_enough_money
*********************************************************************************

I add a test with an :ref:`assertion<what is an assertion?>` for the last case - when the :red:`wrong PIN` is entered and there is :red:`NOT enough money` in the account, to ``test_atm.py``

==================  ======================= =================
PIN                 money                   withdrawal
==================  ======================= =================
:red:`wrong PIN`    :red:`NOT enough money` :red:`DENIED`
==================  ======================= =================

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 9-13

      def test_wrong_pin_enough_money(self):
          my_expectation = 'DENIED'
          reality = src.atm.withdraw(
              right_pin=False,
              enough_money=True,
          )
          self.assertEqual(reality, my_expectation)

          reality = src.atm.withdraw(
              right_pin=False,
              enough_money=False,
          )
          self.assertEqual(reality, my_expectation)


  # Exceptions seen

the test is still green

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a :ref:`global variable<what is a variable?>` to remove repetition of :red:`'DENIED'` from the tests because 3 of them use it, in ``test_atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.atm
    import unittest


    DENIED = 'DENIED'


    class TestATM(unittest.TestCase):

  this way I do not need to use a :ref:`variable<what is a variable?>` in each test, they can all use the :ref:`global variable<what is a variable?>`

* I use the new :ref:`global variable<what is a variable?>` in :ref:`test_right_pin_not_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2, 7-8

        def test_right_pin_not_enough_money_w_limit(self):
            # my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, DENIED)


    # Exceptions seen

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 34

        def test_right_pin_not_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
            )
            self.assertEqual(reality, DENIED)


    # Exceptions seen

* I use the new :ref:`global variable<what is a variable?>` in :ref:`test_wrong_pin_enough_money`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 2, 7-8

        def test_wrong_pin_enough_money(self):
            # my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, DENIED)

        def test_right_pin_not_enough_money_w_limit(self):

  still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 26

        def test_wrong_pin_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
            )
            self.assertEqual(reality, DENIED)

        def test_right_pin_not_enough_money_w_limit(self):

* I use the :ref:`global variable<what is a variable?>` in :ref:`test_right_pin_not_enough_money`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2, 7-8

        def test_right_pin_not_enough_money(self):
            # my_expectation = 'DENIED'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=False,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_money(self):

  green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 18

        def test_right_pin_not_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=False,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_money(self):

----

*********************************************************************************
test_right_pin_enough_money_w_limit
*********************************************************************************

So far, the :ref:`truth table` for the Automated Teller Machine is

==================  ======================= =================
PIN                 money                   withdrawal
==================  ======================= =================
:green:`right PIN`  :green:`enough money`   :green:`CASH`
:green:`right PIN`  :red:`NOT enough money` :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough money` :red:`DENIED`
==================  ======================= =================

I want to add a :ref:`condition<if statements>` for a daily limit on how much can be taken from the account. The inputs for the ATM will then be

* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will the withdrawal put the account above or below the daily limit for withdrawals?

The :ref:`truth table` for if the :green:`right PIN` is entered and there is :green:`enough money` in the account, is

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :green:`enough money`   :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :green:`enough money`   :red:`NOT above limit`  :green:`CASH`
==================  ======================= ======================  ==================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add an :ref:`assertion<what is an assertion?>` for the case where the :green:`right PIN` is entered, there is :green:`enough money` in the account, and it is :green:`above limit` for daily withdrawals, to :ref:`test_right_pin_enough_money`

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :green:`enough money`   :green:`above limit`    :red:`DENIED`
==================  ======================= ======================  ==================

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 2-7

      def test_right_pin_enough_money(self):
          reality = src.atm.withdraw(
              right_pin=True,
              enough_money=True,
              above_daily_limit=True,
          )
          self.assertEqual(reality, DENIED)

          my_expectation = 'CASH'
          reality = src.atm.withdraw(
              right_pin=True,
              enough_money=True,
          )
          self.assertEqual(reality, my_expectation)

      def test_right_pin_not_enough_money(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: withdraw() got an unexpected keyword argument 'above_daily_limit'

because the ``withdraw`` :ref:`function<what is a function?>` only takes 2 arguments (``right_pin`` and ``enough_money``) and the new :ref:`assertion<what is an assertion?>` called it with 3 arguments (``right_pin``, ``enough_money`` and ``above_daily_limit``)

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
            right_pin, enough_money,
            above_daily_limit,
        ):
        if not right_pin:
            return 'DENIED'

        if not enough_money:
            return 'DENIED'

        return 'CASH'

  the terminal_ is my friend, and shows

  - :ref:`AssertionError<what causes AssertionError?>`

    .. code-block:: python

      AssertionError: 'CASH' != 'DENIED'

    because the ``withdraw`` :ref:`function<what is a function?>` returned :green:`'CASH'` and the :ref:`assertion<what is an assertion?>` expects :red:`DENIED`.

  - :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      FAILED ...test_right_pin_not_enough_money - TypeError: withdraw() missing 1 required positional argument: 'above_daily_limit'
      FAILED ...test_wrong_pin_enough_money - TypeError: withdraw() missing 1 required positional argument: 'above_daily_limit'
      FAILED ...test_right_pin_not_enough_money_w_limit - TypeError: withdraw() missing 1 required positional argument: 'above_daily_limit'

    because the other :ref:`assertions<what is an assertion?>` do not provide a value for ``above_daily_limit`` when they call the ``withdraw`` :ref:`function<what is a function?>`, I have to make it a choice

* I add a :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False,
        ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  because the ``withdraw`` :ref:`function<what is a function?>` returns :green:`'CASH'` and the test expects :red:`'DENIED'`

* I add an :ref:`if statement<if statements>` for this case

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False,
        ):
        if above_daily_limit == True:
            return 'DENIED'

        if not right_pin:
            return 'DENIED'

        if not enough_money:
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
    :lineno-start: 5
    :emphasize-lines: 1-2

        # if above_daily_limit == True:
        if bool(above_daily_limit) == True:
            return 'DENIED'

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

        # if above_daily_limit == True:
        # if bool(above_daily_limit) == True:
        if bool(above_daily_limit):
            return 'DENIED'

  still green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

        # if above_daily_limit == True:
        # if bool(above_daily_limit) == True:
        # if bool(above_daily_limit):
        if above_daily_limit:
            return 'DENIED'

  green, because ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``'DENIED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False,
        ):
        denied = 'DENIED'
        # if above_daily_limit == True:

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``'DENIED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 10-11, 14-15, 18-19

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False,
        ):
        denied = 'DENIED'
        # if above_daily_limit == True:
        # if bool(above_daily_limit) == True:
        # if bool(above_daily_limit):
        if above_daily_limit:
            # return 'DENIED'
            return denied

        if not right_pin:
            # return 'DENIED'
            return denied

        if not enough_money:
            # return 'DENIED'
            return denied

        return 'CASH'

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False,
        ):
        denied = 'DENIED'

        if above_daily_limit:
            return denied

        if not right_pin:
            return denied

        if not enough_money:
            return denied

        return 'CASH'

  this is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

  * it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals
  * it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered
  * it returns :red:`'DENIED'` if there is :red:`NOT enough money` in the account
  * it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I do not need to add anything to the next :ref:`assertion<what is an assertion?>` which is for when the :green:`right PIN` is entered, and there is :green:`enough money` in the account, and it is :red:`NOT above limit` for daily withdrawals, because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :green:`enough money`   :red:`NOT above limit`  :green:`CASH`
  ==================  ======================= ======================  ==================

  this means that

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_money=True,
    )

  is the same as

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_money=True,
        above_daily_limit=False,
    )

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

* I change the name of the test from :ref:`test_right_pin_enough_money` to :ref:`test_right_pin_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_right_pin_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

----

*********************************************************************************
test_right_pin_not_enough_money_w_limit
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered and there is :red:`NOT enough money` in the account, is

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

* I add a value for the ``above_daily_limit`` parameter to the :ref:`assertion<what is an assertion?>` in  :ref:`test_right_pin_not_enough_money`, for the case where the :green:`right PIN` is entered, there is :red:`NOT enough money` in the account, and it is :green:`above limit` for daily withdrawals,

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

        def test_right_pin_not_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_money(self):

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough money` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 9-12

    def test_right_pin_not_enough_money(self):
        reality = src.atm.withdraw(
            right_pin=True,
            enough_money=False,
            above_daily_limit=True,
        )
        self.assertEqual(reality, DENIED)

        reality = src.atm.withdraw(
            right_pin=True,
            enough_money=False,
        )
        self.assertEqual(reality, DENIED)

    def test_wrong_pin_enough_money(self):

  still green. I do not need to give a value for the ``above_daily_limit`` parameter because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_money=False,
    )

  is the same as

  .. code-block:: python

    src.atm.withdraw(
        right_pin=True,
        enough_money=False,
        above_daily_limit=False,
    )

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

* I change the name of the test from :ref:`test_right_pin_not_enough_money` to :ref:`test_right_pin_not_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 8

            my_expectation = 'CASH'
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=True,
            )
            self.assertEqual(reality, my_expectation)

        def test_right_pin_not_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

----

*********************************************************************************
test_wrong_pin_enough_money_w_limit
*********************************************************************************

The :ref:`truth table` for if the :green:`wrong PIN` is entered and there is :green:`enough money` in the account, is

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

* I add a value for the ``above_daily_limit`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_wrong_pin_enough_money`, for the case where the :red:`wrong PIN` is entered, there is :green:`enough money` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7

        def test_wrong_pin_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_money(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :green:`enough money` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 9-13

        def test_wrong_pin_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_money(self):

  green. I do not need to give a value for the ``above_daily_limit`` parameter in the call to ``src.atm.withdraw`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    src.atm.withdraw(
        right_pin=False,
        enough_money=True,
    )

  is the same as

  .. code-block:: python

    src.atm.withdraw(
        right_pin=False,
        enough_money=True,
        above_daily_limit=False,
    )

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

* I change the name of the test from :ref:`test_wrong_pin_enough_money` to :ref:`test_wrong_pin_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 8

            reality = src.atm.withdraw(
                right_pin=True,
                enough_money=False,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

----

*********************************************************************************
test_wrong_pin_not_enough_money_w_limit
*********************************************************************************

The :ref:`truth table` for if the :green:`wrong PIN` is entered and there is :red:`NOT enough money` in the account, is

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

* I add ``above_daily_limit`` to the call to ``src.atm.withdraw`` in :ref:`test_wrong_pin_not_enough_money`, for when the :red:`wrong PIN` is entered, there is :red:`NOT enough money` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 5

        def test_wrong_pin_not_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)


    # Exceptions seen

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough money` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================
  PIN                 money                   daily limit             withdrawal
  ==================  ======================= ======================  ==================
  :red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
  ==================  ======================= ======================  ==================

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 9-13

        def test_wrong_pin_not_enough_money(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
            )
            self.assertEqual(reality, DENIED)


    # Exceptions seen

  the test is still green. I do not need to give a value for the ``above_daily_limit`` parameter in the call to ``src.atm.withdraw`` because the :ref:`default value<test_functions_w_default_arguments>` for the ``above_daily_limit`` parameter of the ``withdraw`` :ref:`function<what is a function?>` is :ref:`False<test_what_is_false>`. This means that

  .. code-block:: python

    reality = src.atm.withdraw(
        right_pin=False,
        enough_money=False,
    )

  is the same as

  .. code-block:: python

    reality = src.atm.withdraw(
        right_pin=False,
        enough_money=False,
        above_daily_limit=False,
    )

  A :ref:`function<what is a function?>` uses the :ref:`default value<test_functions_w_default_arguments>` for a parameter when it is called without a value for the parameter.

* I change the name of the test from :ref:`test_wrong_pin_not_enough_money` to :ref:`test_wrong_pin_not_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 7

            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
            )
            self.assertEqual(reality, DENIED)

        def test_wrong_pin_not_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, DENIED)

* I call the ``withdraw`` :ref:`function<what is a function?>` directly in :ref:`test_wrong_pin_not_enough_money_w_limit`. I do not need the ``reality`` :ref:`variable<what is a variable?>` as a middle man because I only use the :ref:`variables<what is a variable?>` once for each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 7-15, 21-28

        def test_wrong_pin_not_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=False,
            )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=False,
                ),
                DENIED
            )

  still green

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_wrong_pin_not_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 53

        def test_wrong_pin_not_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=False,
                ),
                DENIED
            )


    # Exceptions seen

* I make the same change in :ref:`test_wrong_pin_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 7-15, 21-28

        def test_wrong_pin_enough_money_w_limit(self):
            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
            )
            # self.assertEqual(reality, DENIED)
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=True,
                ),
                DENIED
            )

        def test_wrong_pin_not_enough_money_w_limit(self):

  green

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_wrong_pin_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 39

        def test_wrong_pin_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=True,
                ),
                DENIED
            )

        def test_wrong_pin_not_enough_money_w_limit(self):

* I change :ref:`test_right_pin_not_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3-8, 12-16

        def test_right_pin_not_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                ),
                DENIED
            )

        def test_wrong_pin_enough_money_w_limit(self):

  still green

* I also change :ref:`test_right_pin_enough_money_w_limit`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-8, 12-16

        def test_right_pin_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                ),
                'CASH'
            )

        def test_right_pin_not_enough_money_w_limit(self):

  the test is still green

----

*********************************************************************************
test_right_pin_enough_money_w_card
*********************************************************************************

The :ref:`truth table` for the Automated Teller Machine is now

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:green:`right PIN`  :green:`enough money`   :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :green:`enough money`   :red:`NOT above limit`  :green:`CASH`
:green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

==================  ======================= ======================  ==================
PIN                 money                   daily limit             withdrawal
==================  ======================= ======================  ==================
:red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ======================= ======================  ==================

What if the bank card has expired? The inputs for the ATM will then be

* has the card expired?
* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will the withdrawal put the account above or below the daily limit for withdrawals?

The :ref:`truth table` for if the :green:`right PIN` is entered, AND there is :green:`enough money` in the account, is

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough money` :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough money` :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:green:`right PIN`  :green:`enough money` :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough money` :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ===================== ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a value for the ``card_expired`` parameter to the call to the ``withdraw`` :ref:`function<what is a function?>` for the case where the :green:`right PIN` is entered, there is :green:`enough money` in the account, it is :green:`above limit` for daily withdrawals, and the card has :green:`expired`, in the first :ref:`assertion<what is an assertion?>` in :ref:`test_right_pin_enough_money_w_limit`

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough money` :green:`above limit`    :green:`expired`    :red:`DENIED`
==================  ===================== ======================  ==================  =============

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 7

      def test_right_pin_enough_money_w_limit(self):
          self.assertEqual(
              src.atm.withdraw(
                  right_pin=True,
                  enough_money=True,
                  above_daily_limit=True,
                  card_expired=True,
              ),
              DENIED
          )

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: withdraw() got an unexpected keyword argument 'card_expired'

because the ``withdraw`` :ref:`function<what is a function?>` only takes 2 required arguments (``right_pin``, ``enough_money``) and 1 optional argument (``above_daily_limit``) and the test called it with 4 arguments (``right_pin``, ``enough_money``, ``above_daily_limit`` and ``card_expired``)

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
            right_pin, enough_money,
            above_daily_limit=False, card_expired,
        ):

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_functions_w_positional_and_keyword_arguments>`

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_atm.py``

  .. code-block:: python
    :lineno-start: 84
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a :ref:`default value<test_functions_w_default_arguments>` for ``card_expired`` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False, card_expired=False,
        ):

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :green:`enough money` in the account, it is :green:`above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough money` :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12-20

        def test_right_pin_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                ),
                'CASH'
            )

  the test is still green. I add a value for the ``card_expired`` parameter to make it clearer, even though it is the :ref:`default value<test_functions_w_default_arguments>`

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :green:`enough money` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough money` :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 22-30

        def test_right_pin_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                ),
                'CASH'
            )

        def test_right_pin_not_enough_money_w_limit(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'CASH' != 'DENIED'

  because the ``withdraw`` :ref:`function<what is a function?>` gives me :green:`'CASH'` and the test expects :red:`'DENIED'`

* I add an :ref:`if statement<if statements>` to the ``withdraw`` :ref:`function<what is a function?>` in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'

        if card_expired == True:
            return denied

        if above_daily_limit:
            return denied

        if not right_pin:
            return denied

        if not enough_money:
            return denied

        return 'CASH'

  the test passes

* I use the :ref:`bool built-in function<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1-2

        # if card_expired == True:
        if bool(card_expired) == True:
            return denied

  the test is still green

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-3

        # if card_expired == True:
        # if bool(card_expired) == True:
        if bool(card_expired):
            return denied

  still green

* I remove :ref:`bool<booleans 2: test with bool>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-4

        # if card_expired == True:
        # if bool(card_expired) == True:
        # if bool(card_expired):
        if card_expired:
            return denied

  green, because ``if bool(something) == True`` is the same as ``if bool(something)`` is the same as ``if something``

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'

        if card_expired:
            return denied

        if above_daily_limit:
            return denied

        if not right_pin:
            return denied

        if not enough_money:
            return denied

        return 'CASH'

  this is what happens when the ``withdraw`` :ref:`function<what is a function?>` is called

  * it returns :red:`'DENIED'` if the card has :green:`expired`
  * it returns :red:`'DENIED'` if the account is :green:`above limit` for daily withdrawals
  * it returns :red:`'DENIED'` if the :red:`wrong PIN` is entered
  * it returns :red:`'DENIED'` if there is :red:`NOT enough money` in the account
  * it gives me :green:`'CASH'` if the above :ref:`conditions<if statements>` are NOT met

* I add values for the ``daily_limit`` and ``card_expired`` parameters to make it clearer even though they have :ref:`default values<test_functions_w_default_arguments>`, in the next :ref:`assertion<what is an assertion?>` in :ref:`test_right_pin_enough_money_w_limit` for the case where the :green:`right PIN` is entered, there is :green:`enough money` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`, in ``test_atm.py``

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :green:`right PIN`  :green:`enough money` :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 36-37

        def test_right_pin_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_right_pin_not_enough_money_w_limit(self):

  still green

* I change the name of the test from :ref:`test_right_pin_enough_money_w_limit` to :ref:`test_right_pin_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestATM(unittest.TestCase):

        def test_right_pin_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

----

*********************************************************************************
test_right_pin_not_enough_money_w_card
*********************************************************************************

The :ref:`truth table` for if the :green:`right PIN` is entered AND there is :red:`NOT enough money` in the account, is

==================  ======================= ======================  ==================  =============
PIN                 money                   daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

* I add a value for the ``card_expired`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_right_pin_not_enough_money_w_limit` for when the :green:`right PIN` is entered, there is :red:`NOT enough money` in the account, it is :green:`above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============


  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 7

        def test_right_pin_not_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough money` in the account, it is :green:`above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-20

        def test_right_pin_not_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                ),
                DENIED
            )

        def test_wrong_pin_enough_money_w_limit(self):

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough money` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :green:`expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 22-30

        def test_right_pin_not_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                ),
                DENIED
            )

        def test_wrong_pin_enough_money_w_limit(self):

  green

* I add values for the ``above_daily_limit`` and ``card_expired`` parameters to the :ref:`assertion<what is an assertion?>` for when the :green:`right PIN` is entered, there is :red:`NOT enough money` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 32-40

        def test_right_pin_not_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                    card_expired=True,
                ),
                DENIED
            )

        def test_wrong_pin_enough_money_w_limit(self):

  still green

* I change the name of the test from :ref:`test_right_pin_not_enough_money_w_limit` to :ref:`test_right_pin_not_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'CASH'
            )

        def test_right_pin_not_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

----

*********************************************************************************
test_wrong_pin_enough_money_w_card
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered, and there is :green:`enough money` in the account, is

==================  ======================= ======================  ==================  =============
PIN                 money                   daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
==================  ======================= ======================  ==================  =============

* I add a value for the ``card_expired`` parameter  to the :ref:`assertion<what is an assertion?>` in :ref:`test_wrong_pin_enough_money_w_limit` for the case where the :red:`wrong PIN` is entered, the card has :green:`expired`,  there is :green:`enough money` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 7

        def test_wrong_pin_enough_money_w_limit(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                    card_expired=True,
                ),
                DENIED
            )

  the test is still green

* I add an :ref:`assertion<what is an assertion?>` for the case where the :red:`wrong PIN` is entered, there is :green:`enough money` in the account, the card has :red:`NOT expired`,  and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 13, 16

        def test_wrong_pin_enough_money_w_card(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

  green

* I add ``card_expired`` to the next :ref:`assertion<what is an assertion?>`, which is for when the :red:`wrong PIN` is entered, the card has :green:`expired`,  there is :red:`NOT enough money` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 21

        def test_wrong_pin_enough_money_w_card(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

  still green

* I add values for the ``card_expired`` and ``above_daily_limit`` parameters to the last :ref:`assertion<what is an assertion?>`, for when the :red:`wrong PIN` is entered, the card has :green:`expired`,  there is :red:`NOT enough money` in the account, and it is :red:`NOT above limit` for daily withdrawals

  ==================  ======================= ======================  ==================  =============
  PIN                 money                   daily limit             card expired        withdrawal
  ==================  ======================= ======================  ==================  =============
  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED`
  ==================  ======================= ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 29, 32

        def test_wrong_pin_enough_money_w_card(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test is still green

* I change the name of :ref:`test_wrong_pin_enough_money` to :ref:`test_wrong_pin_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 9

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=True,
                enough_money=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_wrong_pin_enough_money_w_card(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

----

*********************************************************************************
test_not_expired_card_w_wrong_pin
*********************************************************************************

The :ref:`truth table` for if the card has :red:`NOT expired` AND the :red:`wrong PIN` is entered, is

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ===================== ======================  ==================  =============

* I add a new test, with an :ref:`assertion<what is an assertion?>` for when the card is :red:`NOT expired` and the :green:`wrong PIN` is entered, there is :green:`enough money` in the account, and it is :green:`above limit` for daily withdrawals

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 10, 12-18

            reality = src.atm.withdraw(
                card_expired=True,
                right_pin=False,
                enough_money=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

        def test_not_expired_card_w_wrong_pin(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I add the next :ref:`assertion<what is an assertion?>`, where the :red:`wrong PIN` is entered, there is :green:`enough money` in the account, the card has :red:`NOT expired`,  and it is :red:`NOT above limit` for daily withdrawals

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 12-18

        def test_not_expired_card_w_wrong_pin(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  green

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough money` in the account, it is :green:`above limit` for daily withdrawals and the card has :red:`NOT expired`

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 20-26

        def test_not_expired_card_w_wrong_pin(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  still green

* I add an :ref:`assertion<what is an assertion?>` for when the :red:`wrong PIN` is entered, there is :red:`NOT enough money` in the account, it is :red:`NOT above limit` for daily withdrawals, and the card has :red:`NOT expired`

  ==================  ===================== ======================  ==================  =============
  PIN                 money                 daily limit             card expired        withdrawal
  ==================  ===================== ======================  ==================  =============
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
  :red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
  ==================  ===================== ======================  ==================  =============

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 28-34

        def test_not_expired_card_w_wrong_pin(self):
            my_expectation = 'DENIED'

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=True,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=False,
                above_daily_limit=True,
            )
            self.assertEqual(reality, my_expectation)

            reality = src.atm.withdraw(
                card_expired=False,
                right_pin=False,
                enough_money=False,
                above_daily_limit=False,
            )
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the tests are all green

----

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_not_expired_card_w_wrong_pin` because I do not need them, I can call the ``withdraw`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_not_expired_card_w_wrong_pin(self):
            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )


    # Exceptions seen

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_wrong_pin_enough_money_w_card` as well, I can call the ``withdraw`` :ref:`function<what is a function?>` directly

  .. code-block:: python
    :lineno-start: 113
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_wrong_pin_enough_money_w_card(self):
            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )

        def test_not_expired_card_w_wrong_pin(self):

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_right_pin_enough_money_w_card` next

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5-11, 15-21, 25-31, 35-41

        def test_right_pin_enough_money_w_card(self):
            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )

        def test_wrong_pin_enough_money_w_card(self):

* I remove the ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_right_pin_not_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-9, 15-21, 25-31, 35-41

        def test_right_pin_not_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                'CASH'
            )

            my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                my_expectation
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                my_expectation
            )

        def test_right_pin_enough_money_w_card(self):

* I add a :ref:`global variable<what is a variable?>` for ``'DENIED'``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    import src.atm
    import unittest


    DENIED = 'DENIED'


    class TestATM(unittest.TestCase):

* I use the new :ref:`variable<what is a variable?>` to remove repetition from :ref:`test_right_pin_not_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12, 21-22, 32-33, 43-44

        def test_right_pin_not_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                'CASH'
            )

            # my_expectation = 'DENIED'

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                # my_expectation
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                # my_expectation
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                # my_expectation
                DENIED
            )

        def test_right_pin_enough_money_w_card(self):

  the test is still green

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

        def test_right_pin_not_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                'CASH'
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                DENIED
            )

        def test_right_pin_enough_money_w_card(self):

* I do the same thing in :ref:`test_right_pin_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 9, 19, 29, 39

        def test_right_pin_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=True,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                DENIED
            )

        def test_wrong_pin_enough_money_w_card(self):

* also in :ref:`test_wrong_pin_enough_money_w_card`

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 9, 19, 29, 39

        def test_wrong_pin_enough_money_w_card(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=True,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                DENIED
            )

        def test_not_expired_card_w_wrong_pin(self):

* and in :ref:`test_not_expired_card_w_wrong_pin`

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 9, 19, 29, 39

        def test_not_expired_card_w_wrong_pin(self):
            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=True,
                    above_daily_limit=False,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=True,
                ),
                DENIED
            )

            self.assertEqual(
                src.atm.withdraw(
                    card_expired=False,
                    right_pin=False,
                    enough_money=False,
                    above_daily_limit=False,
                ),
                DENIED
            )


    # Exceptions seen

  all tests are still green

* This is what the ``withdraw`` :ref:`function<what is a function?>` looks like now

  .. code-block:: python
    :linenos:

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'

        if card_expired:
            return denied
        if not right_pin:
            return denied
        if not enough_money:
            return denied
        if above_daily_limit:
            return denied

        return 'CASH'

  it could also be written using :ref:`Logical Disjunction (OR)<test_logical_disjunction>` for all the :ref:`if statements` because they all return :red:`'DENIED'`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-12

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'

        if (
            card_expired
            or not right_pin
            or not enough_money
            or above_daily_limit
        ):
            return denied

        return 'CASH'

  it could also be written using :ref:`Logical Conjunction (AND)<test_logical_conjunction>` for the one case where the ATM gives me :green:`'CASH'`, in ``atm.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-12

    def withdraw(
            right_pin, enough_money,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'

        if (
            not card_expired
            and right_pin
            and enough_money
            and not above_daily_limit
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

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*************************************************************************************
review
*************************************************************************************

I ran tests for an Automated Teller Machine with these inputs:

* has the card expired?
* is the PIN correct?
* is the amount I want to take, smaller or bigger than what is in the account?
* will the withdrawal put the account above or below the daily limit for withdrawals?

the inputs gave me this :ref:`truth table`

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough money` :green:`above limit`    :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough money` :green:`above limit`    :red:`NOT expired`  :red:`DENIED`
:green:`right PIN`  :green:`enough money` :red:`NOT above limit`  :green:`expired`    :red:`DENIED`
:green:`right PIN`  :green:`enough money` :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ===================== ======================  ==================  =============

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`expired`    :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ===================== ======================  ==================  =============

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:red:`NOT expired`  :green:`right PIN`  :green:`enough money`   :green:`above limit`    :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :green:`enough money`   :red:`NOT above limit`  :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ===================== ======================  ==================  =============

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :green:`above limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough money`   :red:`NOT above limit`  :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :green:`above limit`    :red:`DENIED`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough money` :red:`NOT above limit`  :red:`DENIED`
==================  ===================== ======================  ==================  =============

The ATM only gives me ``'CASH'`` when the :green:`right PIN` is entered, the card has :red:`NOT expired`, the balance is :green:`enough` for the withdrawal, and the account is :red:`NOT above limit` for daily withdrawals.

What if I want the ATM to give a different message with each denial, so that the user knows why the withdrawal failed? The :ref:`truth table` could then be

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`expired`    :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :green:`right PIN`  :green:`enough`    :red:`NOT above limit`    :red:`DENIED: Card Expired`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :green:`right PIN`  :red:`NOT enough`  :red:`NOT above limit`    :red:`DENIED: Card Expired`
==================  ===================== ======================  ==================  =============

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :red:`wrong PIN`    :green:`enough`    :red:`NOT above limit`    :red:`DENIED: Card Expired`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`DENIED: Card Expired`
:green:`expired`    :red:`wrong PIN`    :red:`NOT enough`  :red:`NOT above limit`    :red:`DENIED: Card Expired`
==================  ===================== ======================  ==================  =============

==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:red:`NOT expired`  :green:`right PIN`  :green:`enough`    :green:`above limit`  :red:`DENIED: You have exceeded the daily withdrawal Limit`
:red:`NOT expired`  :green:`right PIN`  :green:`enough money`   :red:`NOT above limit`  :green:`CASH`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :green:`above limit`  :red:`DENIED: There is not enough money in the account to complete the withdrawal`
:red:`NOT expired`  :green:`right PIN`  :red:`NOT enough`  :red:`NOT above limit`    :red:`DENIED: There is not enough money in the account to complete the withdrawal`
==================  ===================== ======================  ==================  =============


==================  ===================== ======================  ==================  =============
PIN                 money                 daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :green:`above limit`  :red:`Error: You entered the wrong PIN. Try again`
:red:`NOT expired`  :red:`wrong PIN`    :green:`enough`    :red:`NOT above limit`    :red:`Error: You entered the wrong PIN. Try again`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :green:`above limit`  :red:`Error: You entered the wrong PIN. Try again`
:red:`NOT expired`  :red:`wrong PIN`    :red:`NOT enough`  :red:`NOT above limit`    :red:`Error: You entered the wrong PIN. Try again`
==================  ===================== ======================  ==================  =============

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Automated Teller Machine: tests and solutions>`

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