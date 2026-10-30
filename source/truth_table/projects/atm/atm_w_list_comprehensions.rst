.. meta::
  :description:
  :keywords:

.. include:: ../../../links.rst

.. _atm:

#################################################################################
test atm with list comprehensions
#################################################################################


I want to use :ref:`for loops<what is a for loop?>` in the :ref:`atm project<Automated Teller Machine>` to give a different message with each denial based on the following inputs

* has the card expired?
* is the PIN correct?
* is there enough cash in the account for the withdrawal?
* will the withdrawal put the account above or below the daily limit for withdrawals?

the :ref:`truth table` could be

==================  ===================== ======================  ==================  =============
PIN                 cash                  daily limit             card expired        withdrawal
==================  ===================== ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :green:`enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :green:`enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ===================== ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Not enough CASH in Account`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Wrong PIN. Try again...`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Wrong PIN. Try again...`
==================  ======================= ======================  ==================  =============

The :ref:`ATM<Automated Teller Machine>` only gives me :green:`'CASH'` when the :green:`right PIN` is entered, there is :green:`enough cash` in the account, it is :red:`NOT above limit` for daily withdrawals, and the bank card has :red:`NOT expired`.

----

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../../code/atm/tests/test_atm_w_loops.py
  :caption: atm/tests/test_atm.py
  :language: python
  :linenos:
  :lines: 1-58

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`atm folder<Automated Teller Machine>` in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd atm

* I open ``test_atm.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
test_if_card_expired
*********************************************************************************

The :ref:`truth table` for if the card has :green:`expired` is

==================  ======================= ======================  ==================  ===========================
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  ===========================
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
==================  ======================= ======================  ==================  ===========================

==================  ======================= ======================  ==================  ===========================
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  ===========================
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
==================  ======================= ======================  ==================  ===========================

I can write one :ref:`function<what is a function>` with :ref:`for loops<what is a for loop?>` for these cases.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for if the card has :green:`expired`

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 8
  :emphasize-lines: 3-12

  class TestATM(unittest.TestCase):

      def test_if_card_expired(self):
          booleans = (True, False)
          for right_pin in booleans:
              for enough_cash in booleans:
                  for above_daily_limit in booleans:
                      with self.subTest(
                          right_pin=right_pin,
                          enough_cash=enough_cash,
                          above_daily_limit=above_daily_limit,
                      ):

.. code-block:: python
  :lineno-start: 20
  :emphasize-lines: 1-9

                          self.assertEqual(
                              src.atm.withdraw(
                                  right_pin=right_pin,
                                  enough_cash=enough_cash,
                                  above_daily_limit=above_daily_limit,
                                  card_expired=True,
                              ),
                              'DENIED: Card Expired'
                          )

      def test_card_w_below_limit_right_pin_enough_cash(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  SUBFAILED(right_pin=False, enough_cash=False, above_daily_limit=False) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=False, enough_cash=False, above_daily_limit=True) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=False, enough_cash=True, above_daily_limit=False) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=False, enough_cash=True, above_daily_limit=True) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=True, enough_cash=False, above_daily_limit=False) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=True, enough_cash=False, above_daily_limit=True) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=True, enough_cash=True, above_daily_limit=False) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'
  SUBFAILED(right_pin=True, enough_cash=True, above_daily_limit=True) ...
      AssertionError: 'DENIED' != 'DENIED: Card Expired'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``__init__.py`` from the ``atm`` folder_ in the ``src`` folder_

* I change the error message for when ``card_expired`` is :green:`True` in the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 7

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_card_w_above_limit_right_pin_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_above_limit_right_pin_not_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_above_limit_wrong_pin_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_above_limit_wrong_pin_not_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_below_limit_right_pin_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_below_limit_right_pin_not_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_below_limit_wrong_pin_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'
    FAILED ...test_card_w_below_limit_wrong_pin_not_enough_cash -
        AssertionError: 'DENIED: Card Expired' != 'DENIED'

  I broke the other tests for if the card has :green:`expired` with my change.

* I undo the change

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 7

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return denied
        if above_daily_limit:

  the terminal_ shows the previous :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_if_card_expired`

* I add another parameter for ``card_expired`` with an :ref:`if statement<if statements>` so that I do not break the other tests

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 4, 7-8

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
            card_expired_a=False,
        ):
        denied = 'DENIED'
        if card_expired_a:
            return 'DENIED: Card Expired'
        if card_expired:
            return denied
        if above_daily_limit:

* I add ``card_expired_a`` to the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` from :ref:`test_if_card_expired` in ``tests/test_atm.py``

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 20
    :emphasize-lines: 7

                        self.assertEqual(
                            src.atm.withdraw(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=above_daily_limit,
                                card_expired=True,
                                card_expired_a=True,
                            ),
                            'DENIED: Card Expired'
                        )

        def test_card_w_below_limit_right_pin_enough_cash(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_below_limit_right_pin_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 31

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

        def test_card_w_above_limit_right_pin_enough_cash(self):

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_above_limit_right_pin_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 42

        def test_card_w_above_limit_right_pin_enough_cash(self):
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

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_above_limit_right_pin_not_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 53

        def test_card_w_above_limit_right_pin_not_enough_cash(self):
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

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_below_limit_right_pin_not_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 64

        def test_card_w_below_limit_right_pin_not_enough_cash(self):
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

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_above_limit_wrong_pin_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 75

        def test_card_w_above_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=True,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_below_limit_wrong_pin_enough_cash(self):

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_below_limit_wrong_pin_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 86

        def test_card_w_below_limit_wrong_pin_enough_cash(self):
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

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_above_limit_wrong_pin_not_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 97

        def test_card_w_above_limit_wrong_pin_not_enough_cash(self):
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

* I remove the :ref:`assertion<what is an assertion?>` for if the card has :green:`expired` from :ref:`test_card_w_below_limit_wrong_pin_not_enough_cash` because it is now covered by :ref:`test_if_card_expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 108

        def test_card_w_below_limit_wrong_pin_not_enough_cash(self):
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

* I remove ``card_expired_a`` from the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` from :ref:`test_if_card_expired` in ``tests/test_atm.py``

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 20

                        self.assertEqual(
                            src.atm.withdraw(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=above_daily_limit,
                                card_expired=True,
                            ),
                            'DENIED: Card Expired'
                        )

        def test_card_w_below_limit_right_pin_enough_cash(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

* I change the error message of the :ref:`if statement<if statements>` for when ``card_expired`` is :green:`True` in the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 10

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
            card_expired_a=False,
        ):
        denied = 'DENIED'
        if card_expired_a:
            return 'DENIED: Card Expired'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:

  the test is green again.

* I remove ``card_expired_a`` and its :ref:`if statement<if statements>` from the ``withdraw`` :ref:`function<what is a function?>`

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:

  green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_if_card_expired'

----

*********************************************************************************
test_if_above_daily_limit
*********************************************************************************

The :ref:`truth table` for if the account is :green:`above limit` for daily withdrawals is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
==================  ======================= ======================  ==================  =============

I can write one :ref:`function<what is a function>` with :ref:`for loops<what is a for loop?>` for these cases.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for if the account is :green:`above limit` for daily withdrawals

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 8
  :emphasize-lines: 3-11

  class TestATM(unittest.TestCase):

      def test_if_above_daily_limit(self):
          booleans = (False, True)
          for right_pin in booleans:
              for enough_cash in booleans:
                  with self.subTest(
                      right_pin=right_pin,
                      enough_cash=enough_cash,
                  ):

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 1-9

                      self.assertEqual(
                          src.atm.withdraw(
                              right_pin=right_pin,
                              enough_cash=enough_cash,
                              above_daily_limit_a=True,
                              card_expired=False,
                          ),
                          'DENIED: exceeded daily withdrawal limit'
                      )

      def test_if_card_expired(self):

the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: shell
  :emphasize-text: True False

    SUBFAILED(right_pin=False, enough_cash=False) ...
        TypeError: withdraw() got an unexpected keyword argument 'enough_Cash'.
                   Did you mean 'above_daily_limit'?
    SUBFAILED(right_pin=False, enough_cash=True) ...
        TypeError: withdraw() got an unexpected keyword argument 'enough_Cash'.
                   Did you mean 'above_daily_limit'?
    SUBFAILED(right_pin=True, enough_cash=False) ...
        TypeError: withdraw() got an unexpected keyword argument 'enough_Cash'.
                   Did you mean 'above_daily_limit'?
    SUBFAILED(right_pin=True, enough_cash=True) ...
        TypeError: withdraw() got an unexpected keyword argument 'enough_Cash'.
                   Did you mean 'above_daily_limit'?

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add ``above_daily_limit_a`` to the ``withdraw`` :ref:`function<what is a function?>` with an :ref:`if statement<if statements>` for it, in ``src/atm/__init__.py``

.. code-block:: python
  :caption: atm/src/atm/__init__.py
  :linenos:
  :emphasize-lines: 4, 9-10

  def withdraw(
          right_pin, enough_cash,
          above_daily_limit=False, card_expired=False,
          above_daily_limit_a=False,
      ):
      denied = 'DENIED'
      if card_expired:
          return 'DENIED: Card Expired'
      if above_daily_limit_a:
          return 'DENIED: Exceeded the daily withdrawal limit'
      if above_daily_limit:

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove :ref:`test_card_w_above_limit_right_pin_enough_cash` because it is now covered by :ref:`test_if_above_daily_limit`, in ``tests/test_atm.py``
* I remove :ref:`test_card_w_above_limit_right_pin_not_enough_cash` because it is now covered by :ref:`test_if_above_daily_limit`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 48

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

        def test_card_w_below_limit_right_pin_not_enough_cash(self):

* I remove :ref:`test_card_w_above_limit_wrong_pin_enough_cash` because it is now covered by :ref:`test_if_above_daily_limit`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 59

        def test_card_w_below_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_below_limit_wrong_pin_enough_cash(self):

* I remove :ref:`test_card_w_above_limit_wrong_pin_not_enough_cash` because it is now covered by :ref:`test_if_above_daily_limit`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 70

        def test_card_w_below_limit_wrong_pin_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=False,
                    enough_cash=True,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                DENIED
            )

        def test_card_w_below_limit_wrong_pin_not_enough_cash(self):

* I change ``above_daily_limit_a`` to ``above_daily_limit`` in the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` from :ref:`test_if_above_daily_limit` in ``tests/test_atm.py``

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 18
    :emphasize-lines: 5

                        self.assertEqual(
                            src.atm.withdraw(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=True,
                                card_expired=False,
                            ),
                            'DENIED: Exceeded the daily withdrawal limit'
                        )

        def test_if_card_expired(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(right_pin=False, enough_cash=False) ...
        AssertionError: 'DENIED'
                     != 'DENIED: Exceeded daily withdrawal limit'
    SUBFAILED(right_pin=False, enough_cash=True) ...
        AssertionError: 'DENIED'
                     != 'DENIED: Exceeded daily withdrawal limit'
    SUBFAILED(right_pin=True, enough_cash=False) ...
        AssertionError: 'DENIED'
                     != 'DENIED: Exceeded daily withdrawal limit'
    SUBFAILED(right_pin=True, enough_cash=True) ...
        AssertionError: 'DENIED'
                     != 'DENIED: Exceeded daily withdrawal limit'

* I change the error message of the :ref:`if statement<if statements>` for when ``above_daily_limit`` is :green:`True` in the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 12

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
            above_daily_limit_a=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit_a:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if above_daily_limit:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if not right_pin:

  the tests passes.

* I remove ``above_daily_limit_a`` and its :ref:`if statement<if statements>` from the ``withdraw`` :ref:`function<what is a function?>`

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if not right_pin:

  the test is still green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_if_above_daily_limit'

----

*********************************************************************************
test_if_wrong_pin
*********************************************************************************

The :ref:`truth table` for if the :red:`wrong PIN` is entered is

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Wrong PIN. Try again...`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Wrong PIN. Try again...`
==================  ======================= ======================  ==================  =============

I can write one :ref:`function<what is a function>` with :ref:`for loops<what is a for loop?>` for the two cases.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for if the :red:`wrong PIN` is entered

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 8
  :emphasize-lines: 3-14

  class TestATM(unittest.TestCase):

      def test_if_wrong_pin(self):
          for enough_cash in (False, True):
              with self.subTest(enough_cash=enough_cash):
                  self.assertEqual(
                      src.atm.withdraw(
                          right_pin=False,
                          enough_cash=enough_cash,
                          above_daily_limit=False,
                          card_expired=False,
                      ),
                      'DENIED: Wrong PIN. Try again...'
                  )

      def test_if_above_daily_limit(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

    SUBFAILED(enough_cash=False) AssertionError:
        'DENIED' != 'DENIED: Wrong PIN. Try again...'
    SUBFAILED(enough_cash=True) AssertionError:
        'DENIED' != 'DENIED: Wrong PIN. Try again...'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``right_pin_a`` to the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 13
    :emphasize-lines: 4

                    self.assertEqual(
                        src.atm.withdraw(
                            right_pin=False,
                            right_pin_a=False,
                            enough_cash=enough_cash,
                            above_daily_limit=False,
                            card_expired=False,
                        ),
                        'DENIED: Wrong PIN. Try again...'
                    )

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell
    :emphasize-text: True, False

    SUBFAILED(enough_cash=False) ...
        TypeError: withdraw() got an unexpected keyword argument 'right_pin_a'.
                   Did you mean 'right_pin'?
    SUBFAILED(enough_cash=True) ...
        TypeError: withdraw() got an unexpected keyword argument 'right_pin_a'.
                   Did you mean 'right_pin'?

* I add ``right_pin_a`` with an :ref:`if statement<if statements>` for it, to the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 4, 11-12

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
            right_pin_a=True,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if not right_pin_a:
            return 'DENIED: Wrong PIN. Try again...'
        if not right_pin:

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove :ref:`test_card_w_below_limit_wrong_pin_enough_cash` because it is now covered by :ref:`test_if_wrong_pin`, in ``tests/test_atm.py``
* I remove :ref:`test_card_w_below_limit_wrong_pin_not_enough_cash` because it is now covered by :ref:`test_if_wrong_pin`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 73

        def test_card_w_below_limit_right_pin_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                DENIED
            )


    # Exceptions seen

* I remove ``right_pin_a`` from the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function?>` from :ref:`test_if_wrong_pin`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 10

        def test_if_wrong_pin(self):
            for enough_cash in (True, False):
                with self.subTest(enough_cash=enough_cash):
                    self.assertEqual(
                        src.atm.withdraw(
                            right_pin=False,
                            enough_cash=enough_cash,
                            above_daily_limit=False,
                            card_expired=False,
                        ),
                        'DENIED: Wrong PIN. Try again...'
                    )

        def test_if_above_daily_limit(self):

  the terminal_ is my friend, and shows :ref:`ASsertionError<what causes AssertionError?>`

* I change the error message of the :ref:`if statement<if statements>` for when ``right_pin`` is :red:`False` in the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:
    :emphasize-lines: 14

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
            right_pin_a=True,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if not right_pin_a:
            return 'DENIED: Wrong PIN. Try again...'
        if not right_pin:
            return 'DENIED: Wrong PIN. Try again...'
        if not enough_cash:

  the test is green again.

* I remove ``right_pin_a`` and its :ref:`if statement<if statements>` from the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        denied = 'DENIED'
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if not right_pin:
            return 'DENIED: Wrong PIN. Try again...'
        if not enough_cash:
            return denied
        return 'CASH'

  the test is still green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_if_wrong_pin'

----

*********************************************************************************
test_if_not_enough_cash
*********************************************************************************

There is only one message for if there is :red:`NOT enough cash` in the account, which is if the :green:`right PIN` is entered, the card has :red:`NOT expired` and the account is :red:`NOT above limit` for daily withdrawals

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Not enough CASH in Account`
==================  ======================= ======================  ==================  =============

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_card_w_below_limit_right_pin_not_enough_cash` in ``tests/test_atm.py``

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 72
  :emphasize-lines: 9

      def test_card_w_below_limit_right_pin_not_enough_cash(self):
          self.assertEqual(
              src.atm.withdraw(
                  right_pin=True,
                  enough_cash=False,
                  above_daily_limit=False,
                  card_expired=False,
              ),
              'DENIED: Not enough CASH in Account'
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

    AssertionError:
        'DENIED' != 'DENIED: Not enough CASH in Account

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the error message for if there is :red:`NOT enough cash` in the account, in the ``withdraw`` :ref:`function<what is a function?>` in ``src/atm/__init__.py``

.. code-block:: python
  :caption: atm/src/atm/__init__.py
  :linenos:
  :emphasize-lines: 13

  def withdraw(
          right_pin, enough_cash,
          above_daily_limit=False, card_expired=False,
      ):
      denied = 'DENIED'
      if card_expired:
          return 'DENIED: Card Expired'
      if above_daily_limit:
          return 'DENIED: Exceeded the daily withdrawal limit'
      if not right_pin:
          return 'DENIED: Wrong PIN. Try again...'
      if not enough_cash:
          return 'DENIED: Not enough CASH in Account'
      return 'CASH'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the ``denied`` :ref:`variable<what is a variable?>` because it is no longer used

  .. code-block:: python
    :caption: atm/src/atm/__init__.py
    :linenos:

    def withdraw(
            right_pin, enough_cash,
            above_daily_limit=False, card_expired=False,
        ):
        if card_expired:
            return 'DENIED: Card Expired'
        if above_daily_limit:
            return 'DENIED: Exceeded the daily withdrawal limit'
        if not right_pin:
            return 'DENIED: Wrong PIN. Try again...'
        if not enough_cash:
            return 'DENIED: Not enough CASH in Account'
        return 'CASH'

* I change the name of the test from :ref:`test_card_w_below_limit_right_pin_not_enough_cash` to :ref:`test_if_not_enough_cash`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 61
    :emphasize-lines: 12

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

        def test_if_not_enough_cash(self):
            self.assertEqual(
                src.atm.withdraw(
                    right_pin=True,
                    enough_cash=False,
                    above_daily_limit=False,
                    card_expired=False,
                ),
                'DENIED: Not enough CASH in Account'
            )


    # Exceptions seen

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'rename to test_if_not_enough_cash'

----

*********************************************************************************
extract test_atm
*********************************************************************************

:ref:`test_if_card_expired`, :ref:`test_if_above_daily_limit` and :ref:`test_if_wrong_pin` all use :ref:`for loops<what is a for loop?>` over a tuple_ of :ref:`booleans<what are booleans?>`. I can use a :ref:`function<what is a function?>` with :ref:`for loops<what is a for loop?>` to put them together with :ref:`test_card_w_below_limit_right_pin_enough_cash` and :ref:`test_if_not_enough_cash`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for all the cases with :ref:`for loops<what is a for loop?>`

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 8
  :emphasize-lines: 3-14

  class TestATM(unittest.TestCase):

      def test_atm(self):
          booleans = (False, True)
          for right_pin in booleans:
              for enough_cash in booleans:
                  for above_daily_limit in booleans:
                      for card_expired in booleans:
                          with self.subTest(
                              right_pin=right_pin,
                              enough_cash=enough_cash,
                              above_daily_limit=above_daily_limit,
                              card_expired=card_expired,
                          ):

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 22
  :emphasize-lines: 1-9

                              self.assertEqual(
                                  src.atm.withdraw(
                                      right_pin=right_pin,
                                      enough_cash=enough_cash,
                                      above_daily_limit=above_daily_limit,
                                      card_expired=card_expired,
                                  ),
                                  'BOOM!!!'
                              )

      def test_if_wrong_pin(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

    SUBFAILED(
        right_pin=False, enough_cash=False,
        above_daily_limit=False, card_expired=False
    ) ... AssertionError: 'DENIED: Wrong PIN. Try again...' != 'BOOM!!!'
    SUBFAILED(
        right_pin=False, enough_cash=False,
        above_daily_limit=False, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'
    SUBFAILED(
        right_pin=False, enough_cash=False,
        above_daily_limit=True, card_expired=False
    ) ... AssertionError: 'DENIED: Exceeded daily withdrawal limit' != 'BOOM!!!'
    SUBFAILED(
        right_pin=False, enough_cash=False,
        above_daily_limit=True, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'

.. code-block:: python

    SUBFAILED(
        right_pin=False, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) ... AssertionError: 'DENIED: Wrong PIN. Try again...' != 'BOOM!!!'
    SUBFAILED(
        right_pin=False, enough_cash=True,
        above_daily_limit=False, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'
    SUBFAILED(
        right_pin=False, enough_cash=True,
        above_daily_limit=True, card_expired=False
    ) ... AssertionError: 'DENIED: Exceeded daily withdrawal limit' != 'BOOM!!!'
    SUBFAILED(
        right_pin=False, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'

.. code-block:: python

    SUBFAILED(
        right_pin=True, enough_cash=False,
        above_daily_limit=False, card_expired=False
    ) ... AssertionError: 'DENIED: Not enough CASH in Account' != 'BOOM!!!'
    SUBFAILED(
        right_pin=True, enough_cash=False,
        above_daily_limit=False, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'
    SUBFAILED(
        right_pin=True, enough_cash=False,
        above_daily_limit=True, card_expired=False
    ) ... AssertionError: 'DENIED: Exceeded daily withdrawal limit' != 'BOOM!!!'
    SUBFAILED(
        right_pin=True, enough_cash=False,
        above_daily_limit=True, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'

.. code-block:: python

    SUBFAILED(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) ... AssertionError: 'CASH' != 'BOOM!!!'
    SUBFAILED(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'
    SUBFAILED(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=False
    ) ... AssertionError: 'DENIED: Exceeded daily withdrawal limit' != 'BOOM!!!'
    SUBFAILED(
        right_pin=True, enough_cash=True,
        above_daily_limit=True, card_expired=True
    ) ... AssertionError: 'DENIED: Card Expired' != 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for the result of the :ref:`call<how to call a function with input>` to the ``withdraw`` :ref:`function<what is a function>` then an :ref:`if statement<if statements>` for if the card has :green:`expired`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 16
    :emphasize-lines: 7-22

                            with self.subTest(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=above_daily_limit,
                                card_expired=card_expired,
                            ):
                                result = src.atm.withdraw(
                                    right_pin=right_pin,
                                    enough_cash=enough_cash,
                                    above_daily_limit=above_daily_limit,
                                    card_expired=card_expired,
                                )
                                if card_expired:
                                    self.assertEqual(
                                        result,
                                        'DENIED: Card Expired'
                                    )
                                else:
                                    self.assertEqual(
                                        result,
                                        'BOOM!!!'
                                    )

        def test_if_wrong_pin(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for eight out of the sixteen cases. Progress!

* I add an :ref:`if statement<if statements>` for if the account is :green:`above limit` for withdrawals

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 28
    :emphasize-lines: 7-17

                                if card_expired:
                                    self.assertEqual(
                                        result,
                                        'DENIED: Card Expired'
                                    )
                                else:
                                    if above_daily_limit:
                                        self.assertEqual(
                                            result,
                                            'DENIED: '
                                            'Exceeded daily withdrawal limit'
                                        )
                                    else:
                                        self.assertEqual(
                                            result,
                                            'BOOM!!!'
                                        )

        def test_if_wrong_pin(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for four out of the sixteen cases. More progress, and my :ref:`if statements` are getting more nested. Ugly!

* I add an :ref:`if statement<if statements>` for if the :red:`wrong PIN` is entered

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 39
    :emphasize-lines: 8-18

                                    if above_daily_limit:
                                        self.assertEqual(
                                            result,
                                            'DENIED: '
                                            'Exceeded daily withdrawal limit'
                                        )
                                    else:
                                        if not right_pin:
                                            self.assertEqual(
                                                result,
                                                'DENIED: Wrong PIN.'
                                                ' Try again...'
                                            )
                                        else:
                                            self.assertEqual(
                                                result,
                                                'BOOM!!!'
                                            )

        def test_if_wrong_pin(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for two out of the sixteen cases, and the nesting is uglier than before. Oh boy!

* I add an :ref:`if statement<if statements>` for if there is :red:`NOT enough cash` in the account

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 40
    :emphasize-lines: 7-17

                                        if not right_pin:
                                            self.assertEqual(
                                                result,
                                                'DENIED: Wrong PIN. Try again...'
                                            )
                                        else:
                                            if not enough_cash:
                                                self.assertEqual(
                                                    result,
                                                    'DENIED: '
                                                    'Not enough CASH in Account'
                                                )
                                            else:
                                                self.assertEqual(
                                                    result,
                                                    'BOOM!!!'
                                                )

        def test_if_wrong_pin(self):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for the only cash where I get :green:`'CASH'`

  .. code-block:: python

    SUBFAILED(
        right_pin=True, enough_cash=True,
        above_daily_limit=False, card_expired=False
    ) ...AssertionError: 'CASH' != 'BOOM!!!'

  more ugly nesting.

* I change the expectation of the :ref:`assertion<what is an assertion?>` to match

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 45
    :emphasize-lines: 16

                                        else:
                                            if not enough_cash:
                                                self.assertEqual(
                                                    result,
                                                    'DENIED: '
                                                    'Not enough CASH in Account'
                                                )
                                            else:
                                                self.assertEqual(
                                                    result,
                                                    'CASH'
                                                )

        def test_if_wrong_pin(self):

  the test passes.

----

*********************************************************************************
the elif statement
*********************************************************************************

I can write nested :ref:`if statements` with :ref:`the elif statement<if statements>`

.. code-block:: python

  if something:
      do this
  else:
      if something_else:
          do that
      else:
          do more

becomes

.. code-block:: python

  if something:
      do this
  elif something_else:
      do that
  else:
      do more

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the nested :ref:`if statements` to :ref:`elif statements<the elif statement>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 28
    :emphasize-lines: 6-30

                                if card_expired:
                                    self.assertEqual(
                                        result,
                                        'DENIED: Card Expired'
                                    )
                                elif above_daily_limit:
                                    self.assertEqual(
                                        result,
                                        'DENIED: Exceeded daily withdrawal limit'
                                    )

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 38
    :emphasize-lines: 1-16

                                elif not right_pin:
                                    self.assertEqual(
                                        result,
                                        'DENIED: Wrong PIN. Try again...'
                                    )
                                elif not enough_cash:
                                    self.assertEqual(
                                        result,
                                        'DENIED: '
                                        'Not enough CASH in Account'
                                    )
                                else:
                                    self.assertEqual(
                                        result,
                                        'CASH'
                                    )

        def test_if_wrong_pin(self):

  the test is still green.

* I remove :ref:`test_if_wrong_pin` because it is now covered by :ref:`test_atm<extract test_atm>`
* I remove :ref:`test_if_above_daily_limit` because it is now covered by :ref:`test_atm<extract test_atm>`
* I remove :ref:`test_if_card_expired` because it is now covered by :ref:`test_atm<extract test_atm>`
* I remove :ref:`test_card_w_below_limit_right_pin_enough_cash` because it is now covered by :ref:`test_atm<extract test_atm>`
* I remove :ref:`test_if_not_enough_cash` because it is now covered by :ref:`test_atm<extract test_atm>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 49

                                else:
                                    self.assertEqual(
                                        result,
                                        'CASH'
                                    )


    # Exceptions seen

* I remove the :ref:`DENIED<extract denied variable>` because it is no longer used

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :linenos:

    import src.atm
    import unittest


    class TestATM(unittest.TestCase):

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_if_not_enough_cash'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_atm.py`` and ``src/atm/__init__.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for an **Automated Teller Machine** with these inputs:

* has the card expired?
* is the PIN correct?
* is there enough cash in the account for the withdrawal?
* will the withdrawal put the account above or below the daily limit for withdrawals?

the inputs gave me this :ref:`truth table` with a message for each type of denial, so that the user knows why the withdrawal failed

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :green:`expired`    :red:`DENIED: Card Expired`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :green:`expired`    :red:`DENIED: Card Expired`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:green:`right PIN`  :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:red:`wrong PIN`    :green:`enough cash`    :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
:red:`wrong PIN`    :red:`NOT enough cash`  :green:`above limit`    :red:`NOT expired`  :red:`DENIED: Exceeded the daily withdrawal limit`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:red:`wrong PIN`    :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Wrong PIN. Try again...`
:red:`wrong PIN`    :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Wrong PIN. Try again...`
==================  ======================= ======================  ==================  =============

==================  ======================= ======================  ==================  =============
PIN                 cash                    daily limit             card expired        withdrawal
==================  ======================= ======================  ==================  =============
:green:`right PIN`  :red:`NOT enough cash`  :red:`NOT above limit`  :red:`NOT expired`  :red:`DENIED: Not enough CASH in Account`
:green:`right PIN`  :green:`enough cash`    :red:`NOT above limit`  :red:`NOT expired`  :green:`CASH`
==================  ======================= ======================  ==================  =============

* I used four nested loops to put all the tests together which makes for one test but ugly nesting.
* The :ref:`for loops<what is a for loop?>` led to significantly less lines of code.
* It is also now harder to understand what each thing tests, compared to when I had one :ref:`assertion<what is an assertion?>` for each case, :ref:`there has to be a better way<AssertionError with list comprehensions>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test atm with loops: tests and solution>`

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
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.

:ref:`Would you like to test booleans with loops?<test booleans with loops>`

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