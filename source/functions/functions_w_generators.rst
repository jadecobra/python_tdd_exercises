.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test functions with generators in the functions project. Continues test_args_and_kwargs in functions/tests/test_functions.py. Open existing project with uv run pytest-watcher . --now". Refactor nested for loops over input pairs and functions (positional_arguments, keyword_arguments, args_and_kwargs, optional_arguments) into a generator expression. RED: add raise Exception inside with self.subTest to verify all 20 subtests fail. GREEN: remove raise Exception to make tests pass. REFACTOR: replace the generator expression with itertools.product. Terminal shows NameError: name 'itertools' is not defined. Did you forget to import 'itertools'? Add import itertools at the top of tests/test_functions.py. Terminal shows ValueError: not enough values to unpack (expected 3, got 2); unpack for a_function, (first, second) as a tuple to pass. Remove commented lines, fix indentation, and git commit 'test_args_and_kwargs with generators'.
  :keywords: Jacob Itegboje, Pumping Python, test functions with generators, functions project, test_args_and_kwargs, generator expressions, itertools.product, nested for loops, subTest, 20 subtests, tuple unpacking, NameError name itertools is not defined, ValueError not enough values to unpack, raise Exception, uv run pytest-watcher, pytest-watcher, python tdd generator, src.functions, red green refactor

.. include:: ../links.rst

#################################################################################
test functions with generators
#################################################################################

I want to use a :ref:`generator<generator expressions>` in the :ref:`functions<what is a function?>` project.

----

*********************************************************************************
preview
*********************************************************************************

This is the code in :ref:`test_args_and_kwargs` at the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_w_generators.py
  :caption: functions/tests/test_functions.py
  :language: python
  :lineno-start: 52
  :lines: 52-92

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd functions

* I open ``test_functions.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now"

----

*********************************************************************************
test_args_and_kwargs with generators
*********************************************************************************

I add a :ref:`generator expression<generator expressions>` for the nested :ref:`for loops<what is a for loop?>` in :ref:`test_args_and_kwargs`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 51
  :emphasize-lines: 2-14

      def test_args_and_kwargs(self):
          # for first, second in (
          #     (self.first, self.last),
          #     (self.last, self.first),
          #     (0, 1),
          #     (self.a_tuple, self.a_list),
          #     (self.a_set, self.a_dictionary),
          # ):
          #     for a_function in (
          #         src.functions.positional_arguments,
          #         src.functions.keyword_arguments,
          #         src.functions.args_and_kwargs,
          #         src.functions.optional_arguments,
          #     ):

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 65
  :emphasize-lines: 1-16, 20

          for a_function, first, second in (
              (a_function, first, second)
              for a_function in (
                  src.functions.positional_arguments,
                  src.functions.keyword_arguments,
                  src.functions.args_and_kwargs,
                  src.functions.optional_arguments,
              )
              for (first, second) in (
                  (self.first, self.last),
                  (self.last, self.first),
                  (0, 1),
                  (self.a_tuple, self.a_list),
                  (self.a_set, self.a_dictionary),
              )
          ):
                  with self.subTest(
                      a_function=a_function, inputs=(first, second)
                  ):
                      raise Exception
                      self.assertEqual(
                          a_function(first, second),
                          (first, second)
                      )

the terminal_ is my friend, and shows :ref:`Exception<how to raise an Exception>` for twenty sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove the :ref:`Exception<how to raise an Exception>`

.. code-block:: python
  :caption: functions/tests/test_functions.py
  :lineno-start: 81

                  with self.subTest(
                      a_function=a_function, inputs=(first, second)
                  ):
                      self.assertEqual(
                          a_function(first, second),
                          (first, second)
                      )

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use :ref:`itertools.product<another way to make a generator for nested loops>` in place of the :ref:`generator expression<generator expressions>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 65
    :emphasize-lines: 1-16

            # for a_function, first, second in (
            #     (a_function, first, second)
            #     for a_function in (
            #         src.functions.positional_arguments,
            #         src.functions.keyword_arguments,
            #         src.functions.args_and_kwargs,
            #         src.functions.optional_arguments,
            #     )
            #     for (first, second) in (
            #         (self.first, self.last),
            #         (self.last, self.first),
            #         (0, 1),
            #         (self.a_tuple, self.a_list),
            #         (self.a_set, self.a_dictionary),
            #     )
            # ):

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 81
    :emphasize-lines: 1-14

            for a_function, first, second in itertools.product(
                (
                    src.functions.positional_arguments,
                    src.functions.keyword_arguments,
                    src.functions.args_and_kwargs,
                    src.functions.optional_arguments,
                ), (
                    (self.first, self.last),
                    (self.last, self.first),
                    (0, 1),
                    (self.a_tuple, self.a_list),
                    (self.a_set, self.a_dictionary),
                )
            ):
                    with self.subTest(
                        a_function=a_function, inputs=(first, second)
                    ):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

    NameError: name 'itertools' is not defined.
               Did you forget to import 'itertools'?

* I add an `import statement`_ for itertools_

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import src.functions
    import unittest

  the terminal_ is my friend, and shows ValueError_

  .. code-block:: python
    :caption: terminal

    ValueError: not enough values to unpack
                (expected 3, got 2)

* I change ``first, second`` to a tuple_ in the :ref:`for loop<what is a for loop?>`

  .. code-block:: python
    :caption: functions/tests/test_functions.py
    :lineno-start: 74
    :emphasize-lines: 9

            #     for (first, second) in (
            #         (self.first, self.last),
            #         (self.last, self.first),
            #         (0, 1),
            #         (self.a_tuple, self.a_list),
            #         (self.a_set, self.a_dictionary),
            #     )
            # ):
            for a_function, (first, second) in itertools.product(
                (
                    src.functions.positional_arguments,
                    src.functions.keyword_arguments,
                    src.functions.args_and_kwargs,
                    src.functions.optional_arguments,
                ), (
                    (self.first, self.last),
                    (self.last, self.first),
                    (0, 1),
                    (self.a_tuple, self.a_list),
                    (self.a_set, self.a_dictionary),
                )
            ):

  the test passes.

* I remove the commented lines, then fix indentation in :ref:`test_args_and_kwargs`

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_args_and_kwargs with generators'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``tests/test_functions.py`` and ``src/functions/__init__.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I can use a :ref:`generator expression<generator expressions>` or `itertools.product`_ for nested :ref:`for loops<what is a for loop?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test functions with generators: tests>`

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
* :ref:`I know that everything in Python is an object<what is an object?>`.
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
* :ref:`I know how to use list comprehensions<what is a list comprehension?>`.

:ref:`Would you like to test the microwave project with generators?<test microwave with generators>`

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