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
  :lines: 1-39

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
    'extract test_traffic_light_control'

----

*********************************************************************************
test_traffic_light_failsafe with for loops
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add :ref:`for loops<what is a for loop?>` to :ref:`test_traffic_light_failsafe`

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 46
  :emphasize-lines: 2-12

      def test_traffic_light_failsafe(self):
          inputs = (GREEN, YELLOW, 'bad input')
          for red_phase in ('cross', 'parallel', 'bad input'):
              for current_parallel in inputs:
                  for current_cross in inputs:
                      for timer_done in (False, True):
                          with self.subTest(
                              red_phase=red_phase,
                              current_parallel=current_parallel,
                              current_cross=current_cross,
                              timer_done=timer_done,
                          ):

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 58
  :emphasize-lines: 1-9

                              self.assertEqual(
                                  src.traffic_light.control(
                                      red_phase=red_phase,
                                      current_parallel=current_parallel,
                                      current_cross=current_cross,
                                      timer_done=timer_done,
                                  ),
                                  'BOOM!!!'
                              )

          self.assertEqual(
              src.traffic_light.control(
                  red_phase='cross',
                  current_parallel='BAP',
                  current_cross=RED,
                  timer_done=False,
              ),
              (RED, RED)
          )

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>` for fifty four sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation of the new :ref:`assertion<what is an assertion?>` in :ref:`test_traffic_light_failsafe`

.. code-block:: python
  :caption: traffic_light/tests/test_traffic_light.py
  :lineno-start: 58
  :emphasize-lines: 8

                              self.assertEqual(
                                  src.traffic_light.control(
                                      red_phase=red_phase,
                                      current_parallel=current_parallel,
                                      current_cross=current_cross,
                                      timer_done=timer_done,
                                  ),
                                  (RED, RED)
                              )

          self.assertEqual(
              src.traffic_light.control(
                  red_phase='cross',
                  current_parallel='BAP',
                  current_cross=RED,
                  timer_done=False,
              ),
              (RED, RED)
          )

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the other :ref:`assertions<what is an assertion?>` from :ref:`test_traffic_light_failsafe` because they are now covered by the :ref:`for loops<what is a for loop?>`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 58

                                self.assertEqual(
                                    src.traffic_light.control(
                                        red_phase=red_phase,
                                        current_parallel=current_parallel,
                                        current_cross=current_cross,
                                        timer_done=timer_done,
                                    ),
                                    (RED, RED)
                                )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test_traffic_light_failsafe with for loops'

----

*********************************************************************************
test traffic light with walk signal
*********************************************************************************

What if the :ref:`Traffic Light` has a walk signal to let people know that it is safe to cross the street, the :ref:`truth table` would then be

==========  ==================  ==================  ===============  ==================  ==================  ==================
red         current             current                              next                next                walk
phase       parallel            cross               timer            parallel            cross
==========  ==================  ==================  ===============  ==================  ==================  ==================
'cross'     :green:`GREEN`      :red:`RED`          :red:`NOT done`  :green:`GREEN`      :red:`RED`          :green:`WALK`
'cross'     :green:`GREEN`      :red:`RED`          :green:`done`    :yellow:`YELLOW`    :red:`RED`          :red:`DO NOT WALK`
'cross'     :yellow:`YELLOW`    :red:`RED`          :red:`NOT done`  :yellow:`YELLOW`    :red:`RED`          :red:`DO NOT WALK`
'cross'     :yellow:`YELLOW`    :red:`RED`          :green:`done`    safety :red:`RED`   safety :red:`RED`   :red:`DO NOT WALK`
'cross'     :red:`RED`          :red:`RED`          :red:`NOT done`  safety :red:`RED`   safety :red:`RED`   :red:`DO NOT WALK`
'cross'     :red:`RED`          :red:`RED`          :green:`done`    :red:`RED`          :green:`GREEN`      :red:`DO NOT WALK`
==========  ==================  ==================  ===============  ==================  ==================  ==================


==========  ==================  ==================  ===============  ==================  ==================  ==================
red         current             current                              next                next                walk
phase       parallel            cross               timer            parallel            cross
==========  ==================  ==================  ===============  ==================  ==================  ==================
'parallel'  :red:`RED`          :green:`GREEN`      :red:`NOT done`  :red:`RED`          :green:`GREEN`      :red:`DO NOT WALK`
'parallel'  :red:`RED`          :green:`GREEN`      :green:`done`    :red:`RED`          :yellow:`YELLOW`    :red:`DO NOT WALK`
'parallel'  :red:`RED`          :yellow:`YELLOW`    :red:`NOT done`  :red:`RED`          :yellow:`YELLOW`    :red:`DO NOT WALK`
'parallel'  :red:`RED`          :yellow:`YELLOW`    :green:`done`    safety :red:`RED`   safety :red:`RED`   :red:`DO NOT WALK`
'parallel'  :red:`RED`          :red:`RED`          :red:`NOT done`  safety :red:`RED`   safety :red:`RED`   :red:`DO NOT WALK`
'parallel'  :red:`RED`          :red:`RED`          :green:`done`    :green:`GREEN`      :red:`RED`          :green:`WALK`
==========  ==================  ==================  ===============  ==================  ==================  ==================

The :ref:`Traffic Light` only shows :green:`WALK` if the :red:`RED` phase is ``'parallel'`` AND the current cross is :red:`RED` AND the timer is :green:`done` AND the next cross will stay :red:`RED` OR if the :red:`RED` phase is ``'cross'`` AND the current parallel is :green:`GREEN` AND the timer is :red:`NOT done` AND the next cross will stay :red:`RED`, which means there will be no car moving across the road the person is crossing.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add :ref:`global variables<what is a variable?>` for ``'WALK'`` and ``'DO NOT WALK'``

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :linenos:
    :emphasize-lines: 6

    import src.traffic_light
    import unittest


    GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'
    WALK, NOT_WALK = 'WALK', 'DO NOT WALK'


    class TestTrafficLight(unittest.TestCase):

* I add :green:`WALK` and :red:`NOT_WALK` to the expectations of :ref:`test_traffic_light_control`

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 11
    :emphasize-lines: 3-14
    :emphasize-text: WALK NOT_WALK

        def test_traffic_light_control(self):
            for row in (
                ('cross', GREEN, RED, False, (GREEN, RED, WALK)),
                ('cross', GREEN, RED, True, (YELLOW, RED, NOT_WALK)),
                ('cross', YELLOW, RED, False, (YELLOW, RED, NOT_WALK)),
                ('cross', YELLOW, RED, True, (RED, RED, NOT_WALK)),
                ('cross', RED, RED, False, (RED, RED, NOT_WALK)),
                ('cross', RED, RED, True, (RED, GREEN, NOT_WALK)),
                ('parallel', RED, GREEN, False, (RED, GREEN, NOT_WALK)),
                ('parallel', RED, GREEN, True, (RED, YELLOW, NOT_WALK)),
                ('parallel', RED, YELLOW, False, (RED, YELLOW, NOT_WALK)),
                ('parallel', RED, YELLOW, True, (RED, RED, NOT_WALK)),
                ('parallel', RED, RED, False, (RED, RED, NOT_WALK)),
                ('parallel', RED, RED, True, (GREEN, RED, WALK)),
            ):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        red_phase='cross', current_parallel='GREEN',
        current_cross='RED', timer_done=False
    ) ...AssertionError: Tuples differ: ('GREEN', 'RED')
                                     != ('GREEN', 'RED', 'WALK')
    SUBFAILED(
        red_phase='cross', current_parallel='GREEN',
        current_cross='RED', timer_done=True
    ) ...AssertionError: Tuples differ: ('YELLOW', 'RED')
                                     != ('YELLOW', 'RED', 'DO NOT WALK')
    SUBFAILED(
        red_phase='cross', current_parallel='YELLOW',
        current_cross='RED', timer_done=False
    ) ...AssertionError: Tuples differ: ('YELLOW', 'RED')
                                     != ('YELLOW', 'RED', 'DO NOT WALK')

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        red_phase='cross', current_parallel='YELLOW',
        current_cross='RED', timer_done=True
    ) ...AssertionError: Tuples differ: ('RED', 'RED')
                                     != ('RED', 'RED', 'DO NOT WALK')
    SUBFAILED(
        red_phase='cross', current_parallel='RED',
        current_cross='RED', timer_done=False
    ) ...AssertionError: Tuples differ: ('RED', 'RED')
                                     != ('RED', 'RED', 'DO NOT WALK')
    SUBFAILED(
        red_phase='cross', current_parallel='RED',
        current_cross='RED', timer_done=True
    ) ...AssertionError: Tuples differ: ('RED', 'GREEN')
                                     != ('RED', 'GREEN', 'DO NOT WALK')

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        red_phase='parallel', current_parallel='RED',
        current_cross='GREEN', timer_done=False
    ) ...AssertionError: Tuples differ: ('RED', 'GREEN')
                                     != ('RED', 'GREEN', 'DO NOT WALK')
    SUBFAILED(
        red_phase='parallel', current_parallel='RED',
        current_cross='GREEN', timer_done=True
    ) ...AssertionError: Tuples differ: ('RED', 'YELLOW')
                                     != ('RED', 'YELLOW', 'DO NOT WALK')
    SUBFAILED(
        red_phase='parallel', current_parallel='RED',
        current_cross='YELLOW', timer_done=False
    ) ...AssertionError: Tuples differ: ('RED', 'YELLOW')
                                     != ('RED', 'YELLOW', 'DO NOT WALK')

  .. code-block:: python
    :caption: terminal

    SUBFAILED(
        red_phase='parallel', current_parallel='RED',
        current_cross='YELLOW', timer_done=True
    ) ...AssertionError: Tuples differ: ('RED', 'RED')
                                     != ('RED', 'RED', 'DO NOT WALK')
    SUBFAILED(
        red_phase='parallel', current_parallel='RED',
        current_cross='RED', timer_done=False
    ) ...AssertionError: Tuples differ: ('RED', 'RED')
                                     != ('RED', 'RED', 'DO NOT WALK')
    SUBFAILED(
        red_phase='parallel', current_parallel='RED',
        current_cross='RED', timer_done=True
    ) ...AssertionError: Tuples differ: ('GREEN', 'RED')
                                     != ('GREEN', 'RED', 'WALK')

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``__init__.py`` from the :ref:`traffic_light folder<Traffic Light>` in the ``src`` folder_
* I add :ref:`global variables<what is a variable?>` for ``'WALK'`` and ``'DO NOT WALK'`` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :linenos:
    :emphasize-lines: 2

    GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'
    WALK, NOT_WALK = 'WALK', 'DO NOT WALK'


    def is_not_safe(parallel, cross):

* I add :green:`WALK` and :red:`NOT_WALK` to the :ref:`next_light function<extract next_light function>`

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :lineno-start: 26
    :emphasize-lines: 4, 6, 9, 11-12

    def next_light(red_phase, parallel, cross):
        if red_phase == 'cross':
            if parallel == GREEN:
                return YELLOW, RED, NOT_WALK
            if parallel == RED:
                return RED, GREEN, NOT_WALK
        if red_phase == 'parallel':
            if cross == GREEN:
                return RED, YELLOW, NOT_WALK
            if cross == RED:
                return GREEN, RED, WALK
        return RED, RED, NOT_WALK


    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for six sub tests.

* I add :red:`NOT_WALK` to the :ref:`if statement<if statements>` for if the timer is :red:`NOT done`, in the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :lineno-start: 40
    :emphasize-lines: 9

    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):
        if triggers_failsafe(current_parallel, current_cross):
            return RED, RED

        if not timer_done:
            return current_parallel, current_cross, NOT_WALK

        if timer_done:

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    SUBFAILED(
        red_phase='cross', current_parallel='GREEN',
        current_cross='RED', timer_done=False
    ) ... AssertionError: Tuples differ: ('GREEN', 'RED', 'DO NOT WALK')
                                      != ('GREEN', 'RED', 'WALK')

* I add an :ref:`if statement<if statements>` for if the :red:`RED` phase is ``'cross'`` AND ``current_parallel`` is :green:`GREEN` to ``if not timer_done:``

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :lineno-start: 47
    :emphasize-lines: 2-3

        if not timer_done:
            if red_phase == 'cross' and current_parallel == GREEN:
                return current_parallel, current_cross, WALK
            return current_parallel, current_cross, NOT_WALK

        if timer_done:

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :red:`NOT_WALK` to :ref:`test_traffic_light_failsafe` in ``tests/test_traffic_light.py`` because I cannot predict what light will be next when such events happen, for example a power failure

  .. code-block:: python
    :caption: traffic_light/tests/test_traffic_light.py
    :lineno-start: 59
    :emphasize-lines: 8

                                self.assertEqual(
                                    src.traffic_light.control(
                                        red_phase=red_phase,
                                        current_parallel=current_parallel,
                                        current_cross=current_cross,
                                        timer_done=timer_done,
                                    ),
                                    (RED, RED, NOT_WALK)
                                )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` for fifty four sub tests.

* I add :red:`NOT_WALK` to ``if triggers_failsafe(current_parallel, current_cross):`` in the ``control`` :ref:`function<what is a function?>` in ``src/traffic_light/__init__.py``

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :lineno-start: 40
    :emphasize-lines: 6

    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):
        if triggers_failsafe(current_parallel, current_cross):
            return RED, RED, NOT_WALK

        if not timer_done:

  the test passes.

* I add a :ref:`global variable<what is a variable?>` for ``RED, RED, NOT_WALK``

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :linenos:
    :emphasize-lines: 3

    GREEN, YELLOW, RED = 'GREEN', 'YELLOW', 'RED'
    WALK, NOT_WALK = 'WALK', 'DO NOT WALK'
    FAILSAFE = RED, RED, NOT_WALK


    def is_not_safe(parallel, cross):

* I use the :ref:`variable<what is a variable?>` in the default :ref:`return statement<the return statement>` of the :ref:`next_light function<extract next_light function>`

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :lineno-start: 27
    :emphasize-lines: 12

    def next_light(red_phase, parallel, cross):
        if red_phase == 'cross':
            if parallel == GREEN:
                return YELLOW, RED, NOT_WALK
            if parallel == RED:
                return RED, GREEN, NOT_WALK
        if red_phase == 'parallel':
            if cross == GREEN:
                return RED, YELLOW, NOT_WALK
            if cross == RED:
                return GREEN, RED, WALK
        return FAILSAFE


    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):

  the tests are still green.

* I use the :ref:`variable<what is a variable?>` in the ``control`` :ref:`function<what is a function?>`

  .. code-block:: python
    :caption: traffic_light/src/traffic_light/__init__.py
    :lineno-start: 41
    :emphasize-lines: 6, 18

    def control(
            timer_done, red_phase='parallel',
            current_parallel=RED, current_cross=RED,
        ):
        if triggers_failsafe(current_parallel, current_cross):
            return FAILSAFE

        if not timer_done:
            if red_phase == 'cross' and current_parallel == GREEN:
                return current_parallel, current_cross, WALK
            return current_parallel, current_cross, NOT_WALK

        if timer_done:
            return next_light(
                red_phase, current_parallel, current_cross
            )

        return FAILSAFE

  still green.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'test traffic_light with walk signal'

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

* I used :ref:`for loops<what is a for loop?>` to make less tests which is simpler and at the same time more complex
* I used a tuple_ to represent all the states of the :ref:`Traffic Light` and its outputs in :ref:`test_traffic_light_control`, which is not as easy to read, :ref:`there has to be a better way<test traffic_light with list comprehensions>`
* I used nested :ref:`for loops<what is a for loop?>` in :ref:`test_traffic_light_failsafe`, :ref:`there has to be a better way<test traffic_light with list comprehensions>`

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

:ref:`Would you like to test binary operations from the truth_table project with loops?<truth table: test binary operations with loops>`

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