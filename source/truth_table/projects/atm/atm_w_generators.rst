.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test atm with generators in the atm project. Continues the Automated Teller Machine truth table. Open existing project with uv run pytest-watcher . --now --patterns "**/*.py". Refactor nested for loops over booleans (right_pin, enough_cash, above_daily_limit, card_expired) into a generator expression using placeholder variable _ for unpack tuples. RED: add raise Exception inside with self.subTest to verify all 16 subtests fail. GREEN: remove raise Exception to make tests pass. REFACTOR: replace the generator expression with itertools.product(booleans, repeat=4). Terminal shows NameError: name 'itertools' is not defined (Did you forget to import 'itertools'?). Add import itertools. Simplify by passing (False, True) directly into itertools.product((False, True), repeat=4) and removing the booleans variable. Git commit 'test_atm with generators'.
  :keywords: Jacob Itegboje, Pumping Python, test atm with generators, Automated Teller Machine, ATM project, generator expressions, itertools.product, repeat parameter, nested for loops, subTest, 16 subtests, NameError name itertools is not defined, raise Exception, uv run pytest-watcher, pytest-watcher, python tdd generator, withdraw, truth table, red green refactor

.. include:: ../../../links.rst

.. _test atm with generators:

#################################################################################
test atm with generators
#################################################################################


I want to use a :ref:`generator<generator expressions>` in the :ref:`atm<Automated Teller Machine>` project.

----

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../../code/atm/tests/test_atm_w_generators.py
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
    :caption: terminal
    :emphasize-lines: 1

    cd atm

* I open ``test_atm.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
test_atm with generators
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a :ref:`generator expression<generator expressions>` for the :ref:`for loops<what is a for loop?>` in :ref:`test_atm<extract test_atm>`

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 7
  :emphasize-lines: 3-16

      def test_atm(self):
          booleans = (False, True)
          # for right_pin in booleans:
          #     for enough_cash in booleans:
          #         for above_daily_limit in booleans:
          #             for card_expired in booleans:
          for (
              right_pin, enough_cash,
              above_daily_limit, card_expired
          ) in (
              (_, _, _, _)
              for _ in booleans
              for _ in booleans
              for _ in booleans
              for _ in booleans
          ):

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 23
  :emphasize-lines: 7

                          with self.subTest(
                              right_pin=right_pin,
                              enough_cash=enough_cash,
                              above_daily_limit=above_daily_limit,
                              card_expired=card_expired,
                          ):
                              raise Exception
                              result = src.atm.withdraw(
                                  right_pin=right_pin,
                                  enough_cash=enough_cash,
                                  above_daily_limit=above_daily_limit,
                                  card_expired=card_expired,
                              )

the terminal_ is my friend, and shows :ref:`Exception<how to raise an Exception>` for sixteen sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the :ref:`Exception<how to raise an Exception>`

.. code-block:: python
  :caption: atm/tests/test_atm.py
  :lineno-start: 23

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

the test is green again.

``_`` is a placeholder like pass_. I can use it as the name for a :ref:`variable<what is a variable?>` when I do not need the name. If I did not use ``_`` in this case I would have to repeat the names

.. code-block:: python

  for (
      right_pin, enough_cash,
      above_daily_limit, card_expired
  ) in (
      (
          right_pin, enough_cash,
          above_daily_limit, card_expired
      )
      for right_pin in booleans
      for enough_cash in booleans
      for above_daily_limit in booleans
      for card_expired in booleans
  ):

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I use :ref:`itertools.product<another way to make a generator for nested loops>` in place of the :ref:`generator expression<generator expressions>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 7
    :emphasize-lines: 7-16

        def test_atm(self):
            booleans = (False, True)
            # for right_pin in booleans:
            #     for enough_cash in booleans:
            #         for above_daily_limit in booleans:
            #             for card_expired in booleans:
            # for (
            #     right_pin, enough_cash,
            #     above_daily_limit, card_expired
            # ) in (
            #     (_, _, _, _)
            #     for _ in booleans
            #     for _ in booleans
            #     for _ in booleans
            #     for _ in booleans
            # ):

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 23
    :emphasize-lines: 1-4

            for (
                right_pin, enough_cash,
                above_daily_limit, card_expired
            ) in itertools.product(booleans, repeat=4):
                            with self.subTest(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=above_daily_limit,
                                card_expired=card_expired,
                            ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

     NameError: name 'itertools' is not defined.
                Did you forget to import 'itertools'?

* I add an `import statement`_ for the `itertools library`_

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import src.atm
    import unittest


    class TestATM(unittest.TestCase):

  the test is green again.

* I no longer need the ``booleans`` :ref:`variable<what is a variable?>` because it is only used once as input to :ref:`itertools.product<another way to make a generator for nested loops>`

  .. code-block:: python
    :caption: atm/tests/test_atm.py
    :lineno-start: 24
    :emphasize-lines: 4

            for (
                right_pin, enough_cash,
                above_daily_limit, card_expired
            ) in itertools.product((False, True), repeat=4):
                            with self.subTest(
                                right_pin=right_pin,
                                enough_cash=enough_cash,
                                above_daily_limit=above_daily_limit,
                                card_expired=card_expired,
                            ):

  the test is still green.

* I remove the ``booleans`` :ref:`variable<what is a variable?>` and commented lines, then fix indentation in :ref:`test_atm<extract test_atm>`

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'test_atm with generators'

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

I can use a :ref:`generator expression<generator expressions>` to replace :ref:`for loops<what is a for loop?>`, and I can use `itertools.product`_ for nested :ref:`for loops<what is a for loop?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test atm with generators: test>`

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
* :ref:`I know how to use lists<what is a list?>`.
* :ref:`I know how to use list comprehensions<list comprehensions>`.

:ref:`Would you like to test the Car project with generators?<test car with generators>`

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