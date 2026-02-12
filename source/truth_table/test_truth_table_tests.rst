.. meta::
  :description: Master test-driven development in Python by learning to build and refactor logical functions from scratch. Watch the full tutorial to go from 20 failures to success.
  :keywords: Jacob Itegboje, python test driven development tutorial, how to write logical functions in python, python tdd practical example, python truth table tests, refactoring python code, python unittest tutorial, learn tdd with python, python binary operations tutorial

.. include:: ../links.rst

.. _test_truth_table_tests:

#################################################################################
truth table: test_truth_table_tests
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/DtGE6WqRZgo?si=08uXK8QMZaG06XWp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

I want to write a program_ that makes the tests in ``test_truth_table.py`` pass without looking at them

*********************************************************************************
requirements
*********************************************************************************

* :ref:`Binary Operations 4<truth table: Binary Operations 4>`

*********************************************************************************
continue the project
*********************************************************************************

* Make sure you are in the ``pumping_python`` folder_ with pwd_ in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  if the terminal_ shows anything other than

  .. code-block:: shell

    .../pumping_python

  `change directory`_ to the ``pumping_python`` folder

* Once in ``pumping_python``, `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd truth_table

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/truth_table

* I run the tests with `pytest-watcher`_

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

----

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

* I close ``test_truth_table.py``
* then delete everything in ``truth_table.py``, the terminal_ shows 20 failures, I start with the last one

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'tautology'

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add the name to ``truth_table.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    tautology

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'tautology' is not defined

  I point the name to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    tautology = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I make :ref:`tautology<test_tautology>` a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def tautology():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: tautology() takes 0 positional arguments but 2 were given

  I add names in parentheses for the :ref:`function<what is a function?>` to take input arguments

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def tautology(first_input, second_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not true

* I change :ref:`None<what is None?>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def tautology(first_input, second_input):
        return True

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'project_second'

* I add the :ref:`function<what is a function?>` using the solution I just used for :ref:`tautology<test_tautology>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def tautology(first_input, second_input):
        return True


    def project_second(first_input, second_input):
        return True

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

* I change the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def project_second(first_input, second_input):
        return False

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  The expectation of the test changes. I want to see the difference between the inputs and the expected output

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def project_second(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  ``second_input`` is :ref:`False<test_what_is_false>`, I remove ``first_input`` from the `return statement`_

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def project_second(first_input, second_input):
        return second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'project_first'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-6

    def project_second(first_input, second_input):
        return second_input


    def project_first(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  ``first_input`` is :ref:`False<test_what_is_false>`

* I remove ``second_input`` from the `return statement`_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def project_first(first_input, second_input):
        return first_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'negate_second'

* I add a :ref:`function<what is a function?>` for :ref:`negate_second<test_negate_second>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-6

    def project_first(first_input, second_input):
        return first_input


    def negate_second(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>` to :ref:`negate_second<test_negate_second>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    def negate_second(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'negate_first'

* I add a :ref:`function<what is a function?>` for it

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 7-8

    def negate_second(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input


    def negate_first(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True)

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

    def negate_first(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'material_non_implication'

* I add a :ref:`function<what is a function?>` for :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 5-6

        if (first_input, second_input) == (True, False): return False
        return first_input, second_input


    def material_non_implication(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_non_implication(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

    def material_non_implication(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an :ref:`if statement<if statements>` for it

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

    def material_non_implication(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'material_implication'

* I add a :ref:`function<what is a function?>` for ``material_implication``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, False): return False
        return first_input, second_input


    def material_implication(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_nor'

* I add a :ref:`function<what is a function?>` for :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 5-6

        if (first_input, second_input) == (True, False): return False
        return first_input, second_input


    def logical_nor(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines:  2

    def logical_nor(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3

    def logical_nor(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 4

    def logical_nor(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_nand'. Did you mean: 'logical_nor'?

* I add a :ref:`function<what is a function?>` for :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, True): return False
        return first_input, second_input


    def logical_nand(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_equality'

* I add the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 5-6

        if (first_input, second_input) == (True, True): return False
        return first_input, second_input


    def logical_equality(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2

    def logical_equality(first_input, second_input):
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3

    def logical_equality(first_input, second_input):
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_disjunction'

* I add a :ref:`function<what is a function?>` for :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, True): return False
        return first_input, second_input


    def logical_disjunction(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_conjunction'. Did you mean: 'logical_disjunction'?

* I add a :ref:`function<what is a function?>` for :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, False): return False
        return first_input, second_input


    def logical_conjunction(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 3

    def logical_conjunction(first_input, second_input):
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 4

    def logical_conjunction(first_input, second_input):
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'exclusive_disjunction'

* I add a :ref:`function<what is a function?>` for :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, False): return False
        return first_input, second_input


    def exclusive_disjunction(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2

    def exclusive_disjunction(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

    def exclusive_disjunction(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'converse_non_implication'. Did you mean: 'material_non_implication'?

* I add a definition for the :ref:`converse_non_implication<test_converse_non_implication>` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, False): return False
        return first_input, second_input


    def converse_non_implication(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 3

    def converse_non_implication(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 4

    def converse_non_implication(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'converse_implication'. Did you mean: 'converse_non_implication'?

* I add the :ref:`function<what is a function?>` for :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, False): return False
        return first_input, second_input


    def converse_implication(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'contradiction'

* I add a :ref:`function<what is a function?>` for :ref:`contradiction<test_contradiction>`

  .. code-block:: python
    :lineno-start: 81
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, True): return False
        return first_input, second_input


    def contradiction(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, True) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 2

    def contradiction(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (True, False) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 3

    def contradiction(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, True) is not false

  I add another :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 4

    def contradiction(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: (False, False) is not false

  I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 5

    def contradiction(first_input, second_input):
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_negation'. Did you mean: 'logical_conjunction'?

* I add a :ref:`function<what is a function?>` for ``logical_negation``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 5-6

        if (first_input, second_input) == (False, False): return False
        return first_input, second_input


    def logical_negation(first_input, second_input):
        return first_input, second_input

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: logical_negation() missing 1 required positional argument: 'second_input'

* I remove ``second_input`` from the parentheses, to make the :ref:`function<what is a function?>` take only 1 input,

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 1-2

    def logical_negation(first_input):
        return first_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: True is not false

  I add "not_" to the `return statement`_

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 2

    def logical_negation(first_input):
        return not first_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_identity'. Did you mean: 'logical_equality'?

* I add a :ref:`function<what is a function?>` for ``logical_identity``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 5-6

    def logical_negation(first_input):
        return not first_input


    def logical_identity(the_input):
        return not the_input

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  I remove "not_" from the `return statement`_

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 2

    def logical_identity(the_input):
        return the_input

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_true'. Did you mean: 'logical_nand'?

* I add a :ref:`function<what is a function?>` for ``logical_true``

  .. code-block:: python
    :lineno-start: 97
    :emphasize-lines: 5-6

    def logical_identity(the_input):
        return the_input


    def logical_true(the_input):
        return the_input

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: logical_true() missing 1 required positional argument: 'x'

  I remove ``first_input`` from the parentheses, this :ref:`function<what is a function?>` does not take input, I change the `return statement`_

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 1-2

    def logical_true():
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None is not true

* I change :ref:`None<what is None?>` to :ref:`True<test_what_is_true>` in the `return statement`_

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 2

    def logical_true():
        return True

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.truth_table' has no attribute 'logical_false'. Did you mean: 'logical_nand'?

* I add a :ref:`function<what is a function?>` for ``logical_false``

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 5-6

    def logical_true():
        return True


    def logical_false():
        return False

  the test is green again! All tests are passing and the world is a better place than when I started.

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

I can refactor the :ref:`functions<what is a function?>` I have, to make them simpler since all the tests are passing

* :ref:`logical_false<test_logical_false>`, :ref:`logical_true<test_logical_true>`, :ref:`logical_identity<test_logical_identity>` and :ref:`logical_negation<test_logical_negation>` are already simple

* I change the name of the input in :ref:`Logical Negation<test_logical_negation>`

  .. TIP:: In `Visual Studio Code`_ I can change everywhere a name is by using

    * Find and Replace - ``ctrl+H`` on Windows_ or ``option+command+F`` on MacOS_
    * Rename Symbol

      - Right click on the name you want to change, for example ``first_input`` then select ``Rename Symbol`` or
      - Select the name you want to change then use :kbd:`F2` on your keyboard to rename it

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 1-2

    def logical_negation(the_input):
        return not the_input

  the test is still green

* :ref:`contradiction<test_contradiction>`  returns :ref:`False<test_what_is_false>` in 4 cases, with 2 inputs there are only 4 cases. I add a `return statement`_

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 2

    def contradiction(first_input, second_input):
        return False
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the test is still green. I remove the other lines in the :ref:`function<what is a function?>` in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 85

    def contradiction(first_input, second_input):
        return False


    def logical_negation(the_input):
        return not the_input

* :ref:`converse_implication<test_converse_implication>` returns :ref:`False<test_what_is_false>` in only one case, I return the :ref:`logical negation<test_logical_negation>` of the :ref:`if statement<if statements>`, for the 3 cases that return :ref:`True<test_what_is_true>`

  .. NOTE:: "!=" is the NOT Equal Symbol made with :kbd:`!+=`

  .. code-block:: python
    :lineno-start: 80
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return (first_input, second_input) != (False, True)
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  still green. I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 80

    def converse_implication(first_input, second_input):
        return (first_input, second_input) != (False, True)


    def contradiction(first_input, second_input):
        return False

* :ref:`converse_non_implication<test_converse_non_implication>` has only one case that returns :ref:`True<test_what_is_true>`, it is the missing case. I add a `return statement`_ for it

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return (first_input, second_input) == (False, True)
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the test is still green and I remove the other lines in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 73

    def converse_non_implication(first_input, second_input):
        return (first_input, second_input) == (False, True)


    def converse_implication(first_input, second_input):
        return (first_input, second_input) != (False, True)

* :ref:`exclusive_disjunction<test_exclusive_disjunction>` has two :ref:`if statements`. I put them together to make one :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-6

    def exclusive_disjunction(first_input, second_input):
        if (
            (first_input, second_input) == (True, True)
            or
            (first_input, second_input) == (False, False)
        ): return False
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the test is still green. I remove the other :ref:`if statements` then return the :ref:`logical negation<test_logical_negation>` of the :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 2-6

    def exclusive_disjunction(first_input, second_input):
        return (
            (first_input, second_input) != (True, True)
            and
            (first_input, second_input) != (False, False)
        )


    def converse_non_implication(first_input, second_input):
        return (first_input, second_input) == (False, True)

  the test is still green, I remove the other lines in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 67

    def exclusive_disjunction(first_input, second_input):
        return (first_input, second_input) != (True, True) and (first_input, second_input) != (False, False)


    def converse_non_implication(first_input, second_input):
        return (first_input, second_input) == (False, True)

* :ref:`logical_conjunction<test_logical_conjunction>` only has one case that returns :ref:`True<test_what_is_true>`, it is the missing case. I add a `return statement`_ for it

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return (first_input, second_input) == (True, True)
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  still green, I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 60

    def logical_conjunction(first_input, second_input):
        return (first_input, second_input) == (True, True)


    def exclusive_disjunction(first_input, second_input):
        return (


* :ref:`logical_disjunction<test_logical_disjunction>` only has one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for the opposite of it which covers the other 3 cases

  .. code-block:: python
    :lineno-start: 55
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return (first_input, second_input) != (False, False)
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the test is still green. I remove the other lines in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 55

    def logical_disjunction(first_input, second_input):
        return (first_input, second_input) != (False, False)


    def logical_conjunction(first_input, second_input):
        return (first_input, second_input) == (True, True)

* :ref:`logical_equality<test_logical_equality>` has two :ref:`if statements`.  I use what I know from :ref:`exclusive_disjunction<test_exclusive_disjunction>` to add a `return statement`_

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-6

    def logical_equality(first_input, second_input):
        return (
            (first_input, second_input) != (True, False)
            and
            (first_input, second_input) != (False, True)
        )
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  the test is still green. I remove the other lines in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 49

    def logical_equality(first_input, second_input):
        return (
            (first_input, second_input) != (True, False)
            and
            (first_input, second_input) != (False, True)
        )


    def logical_disjunction(first_input, second_input):
        return (first_input, second_input) != (False, False)

* :ref:`logical_nand<test_logical_nand>` only has one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for its opposite which covers the other 3 cases

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return (first_input, second_input) != (True, True)
        if (first_input, second_input) == (True, True): return False
        return first_input, second_input

  still green. I remove the other lines in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 44

    def logical_nand(first_input, second_input):
        return (first_input, second_input) != (True, True)


    def logical_equality(first_input, second_input):
        return (

* :ref:`logical_nor<test_logical_nor>` only has one case that returns :ref:`True<test_what_is_true>`, I add a `return statement`_ for it

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return (first_input, second_input) == (False, False)
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  still green, I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return (first_input, second_input) == (False, False)


    def logical_nand(first_input, second_input):
        return (first_input, second_input) != (True, True)

* :ref:`material_implication<test_material_implication>` has only one case that returns :ref:`False<test_what_is_false>`, I add a `return statement`_ for the other 3

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return (first_input, second_input) != (True, False)
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the test is still green. I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 32

    def material_implication(first_input, second_input):
        return (first_input, second_input) != (True, False)


    def logical_nor(first_input, second_input):
        return (first_input, second_input) == (False, False)

* :ref:`material_non_implication<test_material_non_implication>` has 3 cases that return :ref:`False<test_what_is_false>`. I add a `return statement`_ for the missing case that returns :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_non_implication(first_input, second_input):
        return (first_input, second_input) == (True, False)
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, True): return False
        if (first_input, second_input) == (False, False): return False
        return first_input, second_input

  the test is still green. I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 25

    def material_non_implication(first_input, second_input):
        return (first_input, second_input) == (True, False)


    def material_implication(first_input, second_input):
        return (first_input, second_input) != (True, False)

* ``first_input`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_first<test_negate_first>` returns :ref:`False<test_what_is_false>`, I add an :ref:`if statement<if statements>` for them

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        if first_input == True: return False
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (True, False): return False
        return first_input, second_input

  the test is still green. I remove the other :ref:`if statements`, then add a simpler `return statement`_

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return first_input != True
        if first_input == True: return False
        return first_input, second_input

  the test is still green, I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 19

    def negate_first(first_input, second_input):
        return first_input != True


    def material_non_implication(first_input, second_input):
        return (first_input, second_input) == (True, False)

* ``second_input`` is :ref:`True<test_what_is_true>` in the 2 cases where :ref:`negate_second<test_negate_second>` returns :ref:`False<test_what_is_false>`. I add a `return statement`_ like the one from :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(first_input, second_input):
        return second_input != True
        if (first_input, second_input) == (True, True): return False
        if (first_input, second_input) == (False, True): return False
        return first_input, second_input

  still green. I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 13

    def negate_second(first_input, second_input):
        return second_input != True


    def negate_first(first_input, second_input):
        return first_input != True

* :ref:`project_second<test_project_second>`, :ref:`project_first<test_project_first>` and :ref:`tautology<test_tautology>` are already simple

* I change the `return statement`_ in :ref:`negate_second<test_negate_second>` to make it simpler

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(first_input, second_input):
        return not second_input == True
        return second_input != True

  when ``not second_input`` is :ref:`True<test_what_is_true>` it means the `return statement`_ is ``True == True`` which is a duplication. I remove the second part of the statement and the second `return statement`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2

    def negate_second(first_input, second_input):
        return not second_input


    def negate_first(first_input, second_input):

  the test is still green

* I do the same thing with :ref:`negate_first<test_negate_first>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

    def negate_first(first_input, second_input):
        return not first_input
        return first_input != True

  still green. I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 17

    def negate_first(first_input, second_input):
        return not first_input


    def material_non_implication(first_input, second_input):

* I use this with :ref:`material_non_implication<test_material_non_implication>`

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 2

    def material_non_implication(first_input, second_input):
        return first_input and not second_input
        return (first_input, second_input) == (True, False)

  the terminal_ shows all tests are still passing. I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 21

    def material_non_implication(first_input, second_input):
        return first_input and not second_input


    def material_implication(first_input, second_input):

* I try it with :ref:`material_implication<test_material_implication>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not first_input and second_input
        return (first_input, second_input) != (True, False)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: False is not true

  Not good! I change "and_" to "or_"

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2

    def material_implication(first_input, second_input):
        return not first_input or second_input
        return (first_input, second_input) != (True, False)

  the test is green again. Note to self - use "or_" the next time I see ``!=`` in these tests. I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 25

    def material_implication(first_input, second_input):
        return not first_input or second_input


    def logical_nor(first_input, second_input):

* I do the same thing with :ref:`logical_nor<test_logical_nor>`

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return not first_input and not second_input
        return (first_input, second_input) == (False, False)

  the test is still green. I remove the second `return statement`_ and change the first `return statement`_ in terms of "not_" since it happens 2 times

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2

    def logical_nor(first_input, second_input):
        return (not first_input) (not or) (not second_input)
        return not first_input and not second_input

  the terminal_ shows SyntaxError_

  .. code-block:: shell

    SyntaxError: invalid syntax

  I comment the line out then factor out "not_"

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 2-3

    def logical_nor(first_input, second_input):
        return not (first_input or second_input)
        # return (not first_input) (not or) (not second_input)
        return not first_input and not second_input

  the test is still green. I remove the other statements in the :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 29

    def logical_nor(first_input, second_input):
        return not (first_input or second_input)


    def logical_nand(first_input, second_input):

* I add a `return statement`_ to :ref:`logical_nand<test_logical_nand>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return not first_input or not second_input
        return (first_input, second_input) != (True, True)

  the test is still green, I remove the second `return statement`_ then factor out "not_" in the first

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 2

    def logical_nand(first_input, second_input):
        return not (first_input and second_input)
        return not first_input or not second_input

  still green. I remove the other `return statements`_

  .. code-block:: python
    :lineno-start: 33

    def logical_nand(first_input, second_input):
        return not (first_input and second_input)


    def logical_equality(first_input, second_input):

* I add a `return statement`_ to :ref:`logical_equality<test_logical_equality>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2

    def logical_equality(first_input, second_input):
        return (not first_input or second_input) and (first_input or not second_input)
        return (
            (first_input, second_input) != (True, False)
            and
            (first_input, second_input) != (False, True)
        )

  the test is still green, I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 37

    def logical_equality(first_input, second_input):
        return (not first_input or second_input) and (first_input or not second_input)


    def logical_disjunction(first_input, second_input):

* I do the same thing with :ref:`logical_disjunction<test_logical_disjunction>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def logical_disjunction(first_input, second_input):
        return first_input or second_input
        return (first_input, second_input) != (False, False)

  still green. I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 41

    def logical_disjunction(first_input, second_input):
        return first_input or second_input


    def logical_conjunction(first_input, second_input):

* on to :ref:`logical_conjunction<test_logical_conjunction>`

  .. code-block:: python
    :lineno-start: 45
    :emphasize-lines: 2

    def logical_conjunction(first_input, second_input):
        return first_input and second_input
        return (first_input, second_input) == (True, True)

  the test is still green. I remove the other `return statement`_

  .. code-block:: python
    :lineno-start: 45

    def logical_conjunction(first_input, second_input):
        return first_input and second_input


    def exclusive_disjunction(first_input, second_input):

* I add a `return statement`_ to :ref:`exclusive_disjunction<test_exclusive_disjunction>`

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 2-6

    def exclusive_disjunction(first_input, second_input):
        return (
            (not first_input or not second_input)
            and
            (first_input or second_input)
        )
        return (
            (first_input, second_input) != (True, True)
            and
            (first_input, second_input) != (False, False)
        )

  still green. I remove the second `return statement`_ then factor out "not_" from the first part of the statement

  .. code-block:: python
    :lineno-start: 49
    :emphasize-lines: 3-4

    def exclusive_disjunction(first_input, second_input):
        return (
            not (first_input and second_input)
            # (not first_input or not second_input)
            and
            (first_input or second_input)
        )

  the test is still green. I remove the commented line

  .. code-block:: python
    :lineno-start: 49

    def exclusive_disjunction(first_input, second_input):
        return (
            not (first_input and second_input)
            and
            (first_input or second_input)
        )


    def converse_non_implication(first_input, second_input):

* I add a simpler `return statement`_ to :ref:`converse_non_implication<test_converse_non_implication>`

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2

    def converse_non_implication(first_input, second_input):
        return not first_input and second_input
        return (first_input, second_input) == (False, True)

  still green. I remove the other line

  .. code-block:: python
    :lineno-start: 57

    def converse_non_implication(first_input, second_input):
        return not first_input and second_input


    def converse_implication(first_input, second_input):

* time for :ref:`converse_implication<test_converse_implication>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

    def converse_implication(first_input, second_input):
        return first_input or not second_input
        return (first_input, second_input) != (False, True)

  I remove the second `return statement`_

  .. code-block:: python
    :lineno-start: 61

    def converse_implication(first_input, second_input):
        return first_input or not second_input


    def contradiction(first_input, second_input):

all the tests are still passing

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_truth_table.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``truth_table``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran tests using :ref:`booleans<what are booleans?>` which can be :ref:`True<test_what_is_true>` or :ref:`False<test_what_is_false>` for the operations of the `Truth Table`_ from Mathematics

* there are 2 :ref:`nullary operations<Nullary Operations>`, they do not take input and always return the same thing, they are :ref:`constant<test_constant_function>`

  - :ref:`Logical False<test_logical_false>` always returns :ref:`False<test_what_is_false>`
  - :ref:`Logical True<test_logical_true>` always returns :ref:`True<test_what_is_true>`

* there are 2 :ref:`unary operations<Unary Operations>`, they take one input

  - :ref:`Logical Identity<test_logical_identity>` returns its input as output
  - :ref:`Logical Negation<test_logical_negation>` returns the negation of its input as output

* there are 16 binary operations, they each take 2 inputs, in this case I named the second input ``second_input`` and the first one ``first_input``

  * :ref:`Contradiction <test_contradiction>`

    - always returns :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Tautology<test_tautology>` which always returns :ref:`True<test_what_is_true>`

  * :ref:`Converse Implication <test_converse_implication>`

    - returns ``first_input or not second_input``
    - returns :ref:`False<test_what_is_false>`, if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse NonImplication<test_converse_non_implication>` which only returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

  * :ref:`Converse NonImplication <test_converse_non_implication>`

    - returns ``not first_input and second_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Converse Implication<test_converse_implication>` which only returns :ref:`False<test_what_is_false>`, if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`

  * :ref:`Exclusive Disjunction <test_exclusive_disjunction>`

    - returns ``first_input != second_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` and ``second_input`` are NOT equal
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Equality<test_logical_equality>` which only returns :ref:`True<test_what_is_true>`, if the two inputs are equal

  * :ref:`Logical Conjunction <test_logical_conjunction>` returns

    - returns ``first_input and second_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` and ``second_input`` are both :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NAND<test_logical_nand>` which only returns :ref:`False<test_what_is_false>`, if the two inputs are :ref:`True<test_what_is_true>`

  * :ref:`Logical Disjunction <test_logical_disjunction>`

    - returns ``first_input or second_input``
    - returns :ref:`False<test_what_is_false>`, if ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`
    - is the  :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical NOR<test_logical_nor>` which only returns :ref:`True<test_what_is_true>`, if the two inputs are :ref:`False<test_what_is_false>`

  * :ref:`Logical Equality <test_logical_equality>`

    - returns ``first_input == second_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` and ``second_input`` are equal
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Exclusive Disjunction (Exclusive OR)<test_exclusive_disjunction>` which only returns :ref:`True<test_what_is_true>`, if the two inputs are NOT equal

  * :ref:`Logical NAND <test_logical_nand>`

    - returns ``not (first_input and second_input)``
    - returns :ref:`False<test_what_is_false>`, if ``first_input`` and ``second_input`` are both :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation) (not)<test_logical_negation>` of :ref:`Logical Conjunction (and)<test_logical_conjunction>` which only returns :ref:`True<test_what_is_true>`, if the two inputs are :ref:`True<test_what_is_true>`

  * :ref:`Logical NOR <test_logical_nor>`

    - returns ``not (first_input or second_input)``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` and ``second_input`` are both :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Logical Disjunction<test_logical_disjunction>` which only returns :ref:`False<test_what_is_false>`, if the two inputs are :ref:`False<test_what_is_false>`

  * :ref:`Material Implication  <test_material_implication>`

    - returns ``not first_input or second_input``
    - returns :ref:`False<test_what_is_false>`, if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material NonImplication<test_material_non_implication>` which returns :ref:`True<test_what_is_true>` only, if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

  * :ref:`Material NonImplication <test_material_non_implication>`

    - returns ``first_input and not second_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`False<test_what_is_false>` and ``second_input`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Material/Logical Implication<test_material_implication>` which only returns :ref:`False<test_what_is_false>`, if ``first_input`` is :ref:`True<test_what_is_true>` and ``second_input`` is :ref:`False<test_what_is_false>`

  * :ref:`Negate First<test_negate_first>`

    - returns ``not first_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`False<test_what_is_false>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project First<test_project_first>` which only returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`True<test_what_is_true>`

  * :ref:`Negate Second <test_negate_second>`

    - returns ``not second_input``
    - returns :ref:`True<test_what_is_true>`, if ``second_input`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Project Second<test_project_second>` which only returns :ref:`True<test_what_is_true>`, if ``second_input`` is :ref:`True<test_what_is_true>`

  * :ref:`Project First <test_project_first>`

    - returns ``first_input``
    - returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate First<test_negate_first>` which only returns :ref:`True<test_what_is_true>`, if ``first_input`` is :ref:`False<test_what_is_false>`
  * :ref:`Project Second <test_project_second>`

    - returns ``second_input``
    - returns :ref:`True<test_what_is_true>`, if ``second_input`` is :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`Negate Second<test_negate_second>` which only returns :ref:`True<test_what_is_true>`, if ``second_input`` is :ref:`False<test_what_is_false>`

  * :ref:`Tautology <test_tautology>`

    - always returns :ref:`True<test_what_is_true>`
    - is the :ref:`opposite (Logical Negation)<test_logical_negation>` of :ref:`contradiction<test_contradiction>`  which always returns :ref:`False<test_what_is_false>`

and

* :ref:`Logical Disjunction is "or"<test_logical_disjunction>`
* :ref:`Logical Conjunction is "and"<test_logical_conjunction>`
* :ref:`Logical Negation is "not" <test_logical_negation>`

All the logic statements or conditions have been written with some or all of the above 3.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed for the Truth Table?<truth table: tests and solutions>`

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

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->