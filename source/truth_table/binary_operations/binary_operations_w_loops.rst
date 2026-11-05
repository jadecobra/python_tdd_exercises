.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

.. _binary_operations_w_loops:

#################################################################################
truth table: test binary operations with loops
#################################################################################

I want to use :ref:`for loops<what is a for loop?>` in the :ref:`truth table` project for :ref:`binary operations<truth table: Binary Operations>`

*********************************************************************************
preview
*********************************************************************************

These is the test I have at the end of the chapter

.. literalinclude:: ../../code/truth_table/tests/test_binary_w_loops.py
  :caption: truth_table/tests/test_binary.py
  :language: python
  :linenos:
  :lines: 1-74

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

    uv run pytest-watcher . --now

----

*********************************************************************************
test_binary_operations
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`for loop<what is a for loop?>` for all the :ref:`binary operations<truth table: Binary Operations>` in ``tests/test_binary.py``

.. code-block:: python
  :caption: truth_table/tests/test_binary.py
  :lineno-start: 11
  :emphasize-lines: 3-21

  class TestBinaryOperations(unittest.TestCase):

      def test_binary_operations(self):
          for operation, tt_out, tf_out, ft_out, ff_out in (
              (src.truth_table.contradiction, False, False, False, False),
              (src.truth_table.logical_conjunction, True, False, False, False),
              (src.truth_table.project_second, True, False, True, False),
              (src.truth_table.converse_non_implication, False, False, True, False),
              (src.truth_table.negate_first, False, False, True, True),
              (src.truth_table.logical_nand, False, True, True, True),
              (src.truth_table.tautology, True, True, True, True),
              (src.truth_table.logical_disjunction, True, True, True, False),
              (src.truth_table.exclusive_disjunction, False, True, True, False),
              (src.truth_table.material_non_implication, False, True, False, False),
              (src.truth_table.project_first, True, True, False, False),
              (src.truth_table.converse_implication, True, True, False, True),
              (src.truth_table.negate_second, False, True, False, True),
              (src.truth_table.logical_nor, False, False, False, True),
              (src.truth_table.logical_equality, True, False, False, True),
              (src.truth_table.material_implication, True, False, True, True),
          ):

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 32
  :emphasize-lines: 1-5

              with self.subTest(operation=operation.__name__):
                  self.assertEqual(operation(*FF), 'BOOM!!!')
                  self.assertEqual(operation(*FT), 'BAP!!!')
                  self.assertEqual(operation(*TF), 'POW!!!')
                  self.assertEqual(operation(*TT), 'TING!!!')

      def test_contradiction(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python
  :caption: terminal

  SUBFAILED(operation='contradiction') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='logical_conjunction') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='project_second') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='converse_non_implication') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='negate_first') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='logical_nand') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='tautology') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='logical_disjunction') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='exclusive_disjunction') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='material_non_implication') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='project_first') ...AssertionError: False != 'BOOM!!!'
  SUBFAILED(operation='converse_implication') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='negate_second') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='logical_nor') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='logical_equality') ...AssertionError: True != 'BOOM!!!'
  SUBFAILED(operation='material_implication') ...AssertionError: True != 'BOOM!!!'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the expectation of ``self.assertEqual(operation(*FF), 'BOOM!!!')``

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 2

                with self.subTest(operation=operation.__name__):
                    self.assertEqual(operation(*FF), ff_out)
                    self.assertEqual(operation(*FT), 'BAP!!!')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED(operation='contradiction') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='logical_conjunction') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='project_second') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='converse_non_implication') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='negate_first') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='logical_nand') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='tautology') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='logical_disjunction') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='exclusive_disjunction') ...AssertionError: True != 'BAP!!!'
    SUBFAILED(operation='material_non_implication') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='project_first') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='converse_implication') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='negate_second') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='logical_nor') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='logical_equality') ...AssertionError: False != 'BAP!!!'
    SUBFAILED(operation='material_implication') ...AssertionError: True != 'BAP!!!'

* I change the expectation of ``self.assertEqual(operation(*FT), 'BOOM!!!')``

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 3

                with self.subTest(operation=operation.__name__):
                    self.assertEqual(operation(*FF), ff_out)
                    self.assertEqual(operation(*FT), ft_out)
                    self.assertEqual(operation(*TF), 'POW!!!')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED(operation='contradiction') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='logical_conjunction') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='project_second') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='converse_non_implication') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='negate_first') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='logical_nand') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='tautology') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='logical_disjunction') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='exclusive_disjunction') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='material_non_implication') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='project_first') ...AssertionError: False != 'POW!!!'
    SUBFAILED(operation='converse_implication') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='negate_second') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='logical_nor') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='logical_equality') ...AssertionError: True != 'POW!!!'
    SUBFAILED(operation='material_implication') ...AssertionError: True != 'POW!!!'

* I change the expectation of ``self.assertEqual(operation(*TF), 'BOOM!!!')``

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 4

                with self.subTest(operation=operation.__name__):
                    self.assertEqual(operation(*FF), ff_out)
                    self.assertEqual(operation(*FT), ft_out)
                    self.assertEqual(operation(*TF), tf_out)
                    self.assertEqual(operation(*TT), 'TING!!!')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED(operation='contradiction') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='logical_conjunction') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='project_second') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='converse_non_implication') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='negate_first') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='logical_nand') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='tautology') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='logical_disjunction') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='exclusive_disjunction') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='material_non_implication') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='project_first') ...AssertionError: False != 'TING!!!'
    SUBFAILED(operation='converse_implication') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='negate_second') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='logical_nor') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='logical_equality') ...AssertionError: True != 'TING!!!'
    SUBFAILED(operation='material_implication') ...AssertionError: True != 'TING!!!'

* I change the expectation of ``self.assertEqual(operation(*T), 'BOOM!!!')``

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 5

                with self.subTest(operation=operation.__name__):
                    self.assertEqual(operation(*FF), ff_out)
                    self.assertEqual(operation(*FT), ft_out)
                    self.assertEqual(operation(*TF), tf_out)
                    self.assertEqual(operation(*TT), tt_out)

        def test_contradiction(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other tests because they are now covered by :ref:`test_binary_operations`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32

                with self.subTest(operation=operation.__name__):
                    self.assertEqual(operation(*FF), ff_out)
                    self.assertEqual(operation(*FT), ft_out)
                    self.assertEqual(operation(*TF), tf_out)
                    self.assertEqual(operation(*TT), tt_out)


    # Exceptions seen
    # AttributeError
    # TypeError
    # AssertionError
    # Syntaxerror

* I change the :ref:`assertions<what is an assertion?>` in :ref:`test_binary_operations` with another :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 13

        def test_binary_operations(self):
            for operation, tt_out, tf_out, ft_out, ff_out in (
                (src.truth_table.contradiction, False, False, False, False),
                (src.truth_table.logical_conjunction, True, False, False, False),
                (src.truth_table.project_second, True, False, True, False),
                (src.truth_table.converse_non_implication, False, False, True, False),
                (src.truth_table.negate_first, False, False, True, True),
                (src.truth_table.logical_nand, False, True, True, True),
                (src.truth_table.tautology, True, True, True, True),
                (src.truth_table.logical_disjunction, True, True, True, False),
                (src.truth_table.exclusive_disjunction, False, True, True, False),
                (src.truth_table.material_non_implication, False, True, False, False),
                (src.truth_table.project_first, True, True, False, False),
                (src.truth_table.converse_implication, True, True, False, True),
                (src.truth_table.negate_second, False, True, False, True),
                (src.truth_table.logical_nor, False, False, False, True),
                (src.truth_table.logical_equality, True, False, False, True),
                (src.truth_table.material_implication, True, False, True, True),
            ):

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 1-11

                for inputs, result in (
                    (FF, ff_out),
                    (FT, ft_out),
                    (TF, tf_out),
                    (TT, tt_out)
                ):
                    with self.subTest(
                        operation=operation.__name__,
                        inputs=inputs, result=result
                    ):
                        self.assertEqual(operation(*inputs), 'BOOM!!!')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for sixty four sub tests.

* I change the expectation of ``self.assertEqual(operation(*inputs), 'BOOM!!!')``

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 38
    :emphasize-lines: 5

                    with self.subTest(
                        operation=operation.__name__,
                        inputs=inputs, result=result
                    ):
                        self.assertEqual(operation(*inputs), result)


    # Exceptions seen

  the test is green again.

* I no longer need the :ref:`TT, TF, FT and FF global variables<extract global variables for truth table cases>` because they are only used in one place. I write out their values

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 2-5

                for inputs, result in (
                    ((False, False), ff_out),
                    ((False, True), ft_out),
                    ((True, False), tf_out),
                    ((True, True), tt_out)
                ):
                    with self.subTest(
                        operation=operation.__name__,
                        inputs=inputs, result=result
                    ):
                        self.assertEqual(operation(*inputs), result)


    # Exceptions seen

* I remove the :ref:`TT, TF, FT and FF global variables<extract global variables for truth table cases>` because they are no longer used

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :linenos:

    import src.truth_table
    import unittest


    class TestBinaryOperations(unittest.TestCase):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_binary_operations'


----

*********************************************************************************
refactor test_binary_operations
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I rewrite the test a different way without listing four :ref:`booleans<what are booleans?>` for each operation

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 5
  :emphasize-lines: 3-24

  class TestBinaryOperations(unittest.TestCase):

      def test_binary_operations(self):
          booleans = (False, True)
          for first in booleans:
              for second in booleans:
                  for operation, expectation in (
                      (src.truth_table.contradiction, 'BOOM!!!'),
                      (src.truth_table.logical_conjunction, 'BAP!!!'),
                      (src.truth_table.project_second, 'POW!!!'),
                      (src.truth_table.converse_non_implication, 'BOOM!!!'),
                      (src.truth_table.negate_first, 'BAP!!!'),
                      (src.truth_table.logical_nand, 'POW!!!'),
                      (src.truth_table.tautology, 'BOOM!!!'),
                      (src.truth_table.logical_disjunction, 'BAP!!!'),
                      (src.truth_table.exclusive_disjunction, 'POW!!!'),
                      (src.truth_table.material_non_implication, 'BOOM!!!'),
                      (src.truth_table.project_first, 'BAP!!!'),
                      (src.truth_table.converse_implication, 'POW!!'),
                      (src.truth_table.negate_second, 'BOOM!!!'),
                      (src.truth_table.logical_nor, 'BOOM!!!'),
                      (src.truth_table.logical_equality, 'BAP!!!'),
                      (src.truth_table.material_implication, 'BOOM!!!'),
                  ):

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 29
  :emphasize-lines: 1-9

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

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for sixty four sub tests. Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change the value of ``expectation`` for :ref:`contradiction<test_contradiction>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 11
    :emphasize-lines: 2

                    for operation, expectation in (
                        (src.truth_table.contradiction, False),
                        (src.truth_table.logical_conjunction, 'BAP!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for sixty sub tests.

* I change the value of ``expectation`` for :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 11
    :emphasize-lines: 3-6

                    for operation, expectation in (
                        (src.truth_table.contradiction, False),
                        (
                            src.truth_table.logical_conjunction,
                            (first, second) == (True, True)
                        ),
                        (src.truth_table.project_second, 'POW!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for fifty six sub tests.

* I change the value of ``expectation`` for :ref:`project_second<test_project_second>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 13
    :emphasize-lines: 5

                        (
                            src.truth_table.logical_conjunction,
                            (first, second) == (True, True)
                        ),
                        (src.truth_table.project_second, second),
                        (src.truth_table.converse_non_implication, 'BOOM!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for fifty two sub tests.

* I change the value of ``expectation`` for :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 17
    :emphasize-lines: 2-5

                        (src.truth_table.project_second, second),
                        (
                            src.truth_table.converse_non_implication,
                            (first, second) == (False, True)
                        ),
                        (src.truth_table.negate_first, 'BAP!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for forty eight tests.

* I change the value of ``expectation`` for :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 18
    :emphasize-lines: 5

                        (
                            src.truth_table.converse_non_implication,
                            (first, second) == (False, True)
                        ),
                        (src.truth_table.negate_first, not first),
                        (src.truth_table.logical_nand, 'POW!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for forty four sub tests.

* I change the value of ``expectation`` for :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 22
    :emphasize-lines: 2-5

                        (src.truth_table.negate_first, not first),
                        (
                            src.truth_table.logical_nand,
                            (first, second) != (True, True)
                        ),
                        (src.truth_table.tautology, 'BOOM!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for forty sub tests.

* I change the value of ``expectation`` for :ref:`tautology<test_tautology>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 23
    :emphasize-lines: 5

                        (
                            src.truth_table.logical_nand,
                            (first, second) != (True, True)
                        ),
                        (src.truth_table.tautology, True),
                        (src.truth_table.logical_disjunction, 'BAP!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for thirty six sub tests.

* I change the value of ``expectation`` for :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 27
    :emphasize-lines: 2+5

                        (src.truth_table.tautology, True),
                        (
                            src.truth_table.logical_disjunction,
                            (first, second) != (False, False)
                        ),
                        (src.truth_table.exclusive_disjunction, 'POW!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for thirty two sub tests.

* I change the value of ``expectation`` for :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 28
    :emphasize-lines: 5-8

                        (
                            src.truth_table.logical_disjunction,
                            (first, second) != (False, False)
                        ),
                        (
                            src.truth_table.exclusive_disjunction,
                            first != second
                        ),
                        (src.truth_table.material_non_implication, 'BOOM!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty eight sub tests.

* I change the value of ``expectation`` for :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 32
    :emphasize-lines: 5-8

                        (
                            src.truth_table.exclusive_disjunction,
                            first != second
                        ),
                        (
                            src.truth_table.material_non_implication,
                            (first, second) == (True, False)
                        ),
                        (src.truth_table.project_first, 'BAP!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty four sub tests.

* I change the value of ``expectation`` for :ref:`project_first<test_project_first>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 36
    :emphasize-lines: 5

                        (
                            src.truth_table.material_non_implication,
                            (first, second) == (True, False)
                        ),
                        (src.truth_table.project_first, first),
                        (src.truth_table.converse_implication, 'POW!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twenty sub tests.

* I change the value of ``expectation`` for :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 40
    :emphasize-lines: 2-5

                        (src.truth_table.project_first, first),
                        (
                            src.truth_table.converse_implication,
                            (first, second) != (False, True)
                        ),
                        (src.truth_table.negate_second, 'BOOM!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for sixteen sub tests.

* I change the value of ``expectation`` for :ref:`negate_second<test_negate_second>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 41
    :emphasize-lines: 5

                        (
                            src.truth_table.converse_implication,
                            (first, second) != (False, True)
                        ),
                        (src.truth_table.negate_second, not second),
                        (src.truth_table.logical_nor, 'BOOM!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for twelve sub tests.

* I change the value of ``expectation`` for :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 45
    :emphasize-lines: 2-5

                        (src.truth_table.negate_second, not second),
                        (
                            src.truth_table.logical_nor,
                            (first, second) == (False, False)
                        ),
                        (src.truth_table.logical_equality, 'BAP!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for eight sub tests.

* I change the value of ``expectation`` for :ref:`logical_equality<test_logical_equality>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 46
    :emphasize-lines: 5-8

                        (
                            src.truth_table.logical_nor,
                            (first, second) == (False, False)
                        ),
                        (
                            src.truth_table.logical_equality,
                            first == second
                        ),
                        (src.truth_table.material_implication, 'BOOM!!!'),

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for four sub tests.

* I change the value of ``expectation`` for :ref:`material_implication<test_material_implication>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 50
    :emphasize-lines: 5-8

                        (
                            src.truth_table.logical_equality,
                            first == second
                        ),
                        (
                            src.truth_table.material_implication,
                            (first, second) != (True, False)
                        ),
                    ):
                        with self.subTest(
                            operation.__name__,
                            first_input=first,
                            second_input=second
                        ):

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'refactor test_binary_operations'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_traffic_light.py`` and ``src/traffic_light/__init__.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I used :ref:`for loops<what is a for loop?>` to make less tests which is simpler and at the same time more complex

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test traffic_light with loops: tests and solutions>`

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

:ref:`Would you like to test making a person with lists?<how to make a person with lists>`

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