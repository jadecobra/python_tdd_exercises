.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

.. _binary_operations_generators:

#################################################################################
truth table: test binary operations with generators
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`truth table` project for :ref:`binary operations<truth table: Binary Operations>`

*********************************************************************************
preview
*********************************************************************************

This is the test I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary_w_loops.py
  :caption: truth_table/tests/test_binary.py
  :language: python
  :linenos:
  :lines: 1-75

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`truth_table folder<truth table>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd truth_table

* I open ``test_binary.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
test_binary_operations with generators
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the the nested :ref:`for loops<what is a for loop?>` in :ref:`test_binary_operations` to a :ref:`generator expression<generator expressions>`

.. code-block:: python
  :caption: truth_table/tests/test_binary.py
  :lineno-start: 7
  :emphasize-lines: 3-18

      def test_binary_operations(self):
          booleans = (False, True)
          for first, second, operation, expectation in (
              (first, second, operation, expectation)
              for first in booleans
              for second in booleans
              for operation, expectation in (
                  (src.truth_table.contradiction, False),
                  (
                      src.truth_table.logical_conjunction,
                      (first, second) == (True, True)
                  ),
                  (src.truth_table.project_second, second),
                  (
                      src.truth_table.converse_non_implication,
                      (first, second) == (False, True)
                  ),
                  (src.truth_table.negate_first, not first),

.. code-block:: python
  :caption: truth_table/tests/test_binary.py
  :lineno-start: 25
  :emphasize-lines: 1-18

                  (
                      src.truth_table.logical_nand,
                      (first, second) != (True, True)
                  ),
                  (src.truth_table.tautology, True),
                  (
                      src.truth_table.logical_disjunction,
                      (first, second) != (False, False)
                  ),
                  (
                      src.truth_table.exclusive_disjunction,
                      first != second
                  ),
                  (
                      src.truth_table.material_non_implication,
                      (first, second) == (True, False)
                  ),
                  (src.truth_table.project_first, first),

.. code-block:: python
  :caption: truth_table/tests/test_binary.py
  :lineno-start: 43
  :emphasize-lines: 1-13

                  (
                      src.truth_table.converse_implication,
                      (first, second) != (False, True)
                  ),
                  (src.truth_table.negate_second, not second),
                  (
                      src.truth_table.logical_nor,
                      (first, second) == (False, False)
                  ),
                  (
                      src.truth_table.logical_equality,
                      first == second
                  ),

.. code-block:: python
  :caption: truth_table/tests/test_binary.py
  :lineno-start: 56
  :emphasize-lines: 1-16
  :emphasize-text: raise Exception

                  (
                      src.truth_table.material_implication,
                      (first, second) != (True, False)
                  ),
              )
          ):
              with self.subTest(
                  operation.__name__,
                  first=first,
                  second=second
              ):
                  raise Exception
                  self.assertEqual(
                      operation(first, second),
                      expectation
                  )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`Exception<how to raise an Exception>` for sixty four sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`Exception<how to raise an Exception>`

.. code-block:: python
  :caption: truth_table/tests/test_binary.py
  :lineno-start: 62

              with self.subTest(
                  operation.__name__,
                  first=first,
                  second=second
              ):
                  self.assertEqual(
                      operation(first, second),
                      expectation
                  )


  # Exceptions seen

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`itertools.product<another way to make a generator for nested loops>` to make the statement simpler

  .. code-block:: python
    :caption: truth_table/tests/test_binary.py
    :lineno-start: 7
    :emphasize-lines: 2-10

        def test_binary_operations(self):
            # booleans = (False, True)
            # for first, second, operation, expectation in (
            #     (first, second, operation, expectation)
            #     for first in booleans
            #     for second in booleans
            for first, second in itertools.product(
                (False, True), repeat=2
            ):
                for operation, expectation in (
                    (src.truth_table.contradiction, False),
                    (
                        src.truth_table.logical_conjunction,
                        (first, second) == (True, True)
                    ),

  .. code-block:: python
    :caption: truth_table/tests/test_binary.py
    :lineno-start: 59
    :emphasize-lines: 5-14

                    (
                        src.truth_table.material_implication,
                        (first, second) != (True, False)
                    ),
                ):
                    with self.subTest(
                        operation.__name__,
                        first=first,
                        second=second
                    ):
                        self.assertEqual(
                            operation(first, second),
                            expectation
                        )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

     NameError: name 'itertools' is not defined.
                Did you forget to import 'itertools'?

* I add an `import statement`_ for the `itertools library`_

  .. code-block:: python
    :caption: truth_table/tests/test_binary.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import src.truth_table
    import unittest


  the test is green again.

* I remove the commented lines

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    git commit -am 'test_binary_operations with generators'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_binary.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I used :ref:`for loops<what is a for loop?>` to turn all the tests into one which is simpler and at the same time more complex.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Binary Operations with loops: test>`

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

:ref:`Would you like to test lists?<what is a list?>`

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