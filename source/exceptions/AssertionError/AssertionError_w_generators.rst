.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): test AssertionError with generators in the assertion_error project. Open existing project with uv run pytest-watcher . --now --patterns "**/*.py". Replace nested for loops across basic_objects with a generator expression ((first, second) for first in self.basic_objects for second in self.basic_objects). RED: add raise Exception inside with self.subTest(pair=(first, second)) to verify all one hundred subtests fail. GREEN: remove raise Exception. REFACTOR: remove commented loops and fix indentation. Another way: replace the generator expression with itertools.product(self.basic_objects, self.basic_objects). Terminal shows NameError: name 'itertools' is not defined (Did you forget to import 'itertools'?). Add import itertools to pass. Verify with raise Exception again. Simplify with the repeat parameter: itertools.product(self.basic_objects, repeat=3) triggers ValueError: too many values to unpack (expected 2, got 3). Fix to repeat=2. Git commit 'test_assertion_error with a generator'.
  :keywords: Jacob Itegboje, Pumping Python, test AssertionError with generators, generator expressions, itertools.product, repeat parameter itertools, nested for loops, subTest, basic_objects, 100 subtests, NameError name itertools is not defined, ValueError too many values to unpack, expected 2 got 3, raise Exception, uv run pytest-watcher, assertion_error project, red green refactor, python tdd generator, test_assertion_error

.. include:: ../../links.rst

.. _product: https://docs.python.org/3/library/itertools.html#itertools.product
.. _itertools.product method: product_
.. _itertools.product: product_
.. _product method: product_

#################################################################################
test AssertionError with generators
#################################################################################

----

I want to use a :ref:`generator<generator expressions>` in the :ref:`assertion_error<what is an assertion?>` project.

----

*********************************************************************************
preview
*********************************************************************************

Here is the code in :ref:`test_assertion_error` by the end of the chapter

.. literalinclude:: ../../code/assertion_error/tests/test_assertion_error_w_generators.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :linenos:
  :lines: 1-5

.. literalinclude:: ../../code/assertion_error/tests/test_assertion_error_w_generators.py
  :caption: assertion_error/tests/test_assertion_error.py
  :language: python
  :lineno-start: 20
  :lines: 20-40


----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`assertion_error folder<what is an assertion?>` in the ``pumping_python`` folder_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd assertion_error

* I open ``test_assertion_error.py`` from the ``tests`` folder_

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now --patterns "**/*.py"

----

*********************************************************************************
test_assertion_error with a generator
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a :ref:`generator expression<generator expressions>` for the :ref:`for loops<what is a for loop?>` in :ref:`test_assertion_error`

.. code-block:: python
  :caption: assertion_error/tests/test_assertion_error.py
  :lineno-start: 19
  :emphasize-lines: 2-8, 10

      def test_assertion_error(self):
          # for first in self.basic_objects:
          #     for second in self.basic_objects:
          for first, second in (
              (first, second)
              for first in self.basic_objects
              for second in self.basic_objects
          ):
                  with self.subTest(pair=(first, second)):
                      raise Exception
                      try:
                          assert first is second
                      except AssertionError:
                          assert first is not second

the terminal_ shows :ref:`Exception<how to test that an Exception is raised>` for one hundred sub tests.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I remove ``raise Exception``

.. code-block:: python
  :caption: assertion_error/tests/test_assertion_error.py
  :lineno-start: 27

              with self.subTest(pair=(first, second)):
                  try:
                      assert first is second
                  except AssertionError:
                      assert first is not second

the test is green again.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines and fix the indentation

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :lineno-start: 19
    :emphasize-lines: 7-11, 13-16, 18-21

    def test_assertion_error(self):
        for first, second in (
            (first, second)
            for first in self.basic_objects
            for second in self.basic_objects
        ):
            with self.subTest(pair=(first, second)):
                try:
                    assert first is second
                except AssertionError:
                    assert first is not second

                try:
                    self.assertIsNot(first, second)
                except AssertionError:
                    self.assertIs(first, second)

                try:
                    self.assertEqual(first, second)
                except AssertionError:
                    self.assertNotEqual(first, second)

    def test_assert_keyword(self):

----

*********************************************************************************
another way to make a generator for nested loops
*********************************************************************************

I can also make a :ref:`generator<generator expressions>` with the `product method`_ from the `itertools library`_, it is part of `The Python Standard Library`_ and needs an `import statement`_

* I add a :ref:`call<how to call a function with input>` to `itertools.product`_ from :ref:`test_assertion_error`

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :lineno-start: 19
    :emphasize-lines: 2-9

        def test_assertion_error(self):
            # for first, second in (
            #     (first, second)
            #     for first in self.basic_objects
            #     for second in self.basic_objects
            # ):
            for first, second in itertools.product(
                self.basic_objects, self.basic_objects,
            ):
                with self.subTest(pair=(first, second)):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell
    :caption: terminal

    NameError: name 'itertools' is not defined.
               Did you forget to import 'itertools'?

* I add an `import statement`_ for the `itertools library`_

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :linenos:
    :emphasize-lines: 1

    import itertools
    import unittest


    def assert_not_equal(x, y):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`Exception<how to test that an Exception is raised>` after the first :ref:`try...except block<how to handle Exceptions>` to make sure the test works

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :lineno-start: 29
    :emphasize-lines: 7

                with self.subTest(pair=(first, second)):
                    try:
                        assert first is second
                    except AssertionError:
                        assert first is not second

                    raise Exception
                    try:
                        self.assertIsNot(first, second)
                    except AssertionError:
                        self.assertIs(first, second)

  the terminal_ shows :ref:`Exception<how to test that an Exception is raised>` for one hundred sub tests.

* I remove the comments and the :ref:`Exception<how to test that an Exception is raised>` from :ref:`test_assertion_error`

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :lineno-start: 20

        def test_assertion_error(self):
            for first, second in itertools.product(
                self.basic_objects, self.basic_objects,
            ):
                with self.subTest(pair=(first, second)):
                    try:
                        assert first is second
                    except AssertionError:
                        assert first is not second

                    try:
                        self.assertIsNot(first, second)
                    except AssertionError:
                        self.assertIs(first, second)

                    try:
                        self.assertEqual(first, second)
                    except AssertionError:
                        self.assertNotEqual(first, second)

        def test_assert_keyword(self):

  the test is green again.

* The `itertools.product method`_ has a parameter for repeating input so I do not have to say the same thing twice. I add it to the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :lineno-start: 20
    :emphasize-lines: 3

        def test_assertion_error(self):
            for first, second in itertools.product(
                self.basic_objects, repeat=3,
            ):

  the terminal_ is my friend, and shows ValueError_

  .. code-block:: python
    :caption: terminal

    ValueError: too many values to unpack (expected 2, got 3)

* I change the value from ``3`` to ``2``

  .. code-block:: python
    :caption: assertion_error/tests/test_assertion_error.py
    :lineno-start: 20
    :emphasize-lines: 3

        def test_assertion_error(self):
            for first, second in itertools.product(
                self.basic_objects, repeat=2,
            ):

  the test passes.

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'test_assertion_error with a generator'

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_assertion_error.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``assertion_error``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I can use a :ref:`generator expression<generator expressions>` to replace :ref:`for loops<what is a for loop?>`, and I can use `itertools.product`_ for nested :ref:`for loops<what is a for loop?>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test AssertionError with generators: tests>`

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

:ref:`Would you like to test the ATM project with generators?<test atm with generators>`

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