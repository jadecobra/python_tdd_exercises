.. meta::
  :description: Master TDD in Python to pass any data type, from strings to classes, and eliminate TypeError. Watch the full tutorial to fix errors in 15 minutes.
  :keywords: Jacob Itegboje, python pass multiple data types to function, python tdd tutorial for beginners, TypeError: 'NoneType' is not callable fix, how to handle different data types as function arguments in python, python pass by reference vs value, python tdd practical example, python unit testing tutorial, python f-string formatting, python NameError resolution, python AttributeError fix

.. include:: ../links.rst

#################################################################################
how to pass values
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/QEiyAO7aEVQ?si=gN_vRO0VrSyWR7R6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

I want to be able to send things from tests to the program_ I am testing and compare what I think will happen with the results I get. This helps me see what is the same, and what is different, the difference helps me know what to change to get what I want.

I use :ref:`the identity function<test_identity_function>` to show how input is passed from a test to a :ref:`function<functions>` in a :ref:`module<ModuleNotFoundError>`

----

*********************************************************************************
preview
*********************************************************************************

Here are the tests I have by the end of the chapter

.. literalinclude:: ../code/tests/test_telephone.py
  :language: python
  :linenos:

----

*********************************************************************************
requirements
*********************************************************************************

* I pick ``telephone`` as the name of this project
* I open a terminal_
* then I `make a directory`_ for the project

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir telephone

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd telephone

  the terminal_ shows I am now in the ``telephone`` folder_

  .. code-block:: shell

    .../pumping_python/telephone

* I `make a folder`_ for the source code

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/telephone

* I use touch_ to make an empty file_ for the program_ in the ``src`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    touch src/telephone.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item src/telephone.py`` instead of ``touch src/telephone.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item src/telephone.py

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/telephone

* I `make a directory`_ for the tests

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir tests

  the terminal_ goes back to the command line

* I use touch_ to make an empty file_ in the ``tests`` folder_ to tell Python_ that it is a `Python package`_

  .. ATTENTION:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/__init__.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/__init__.py`` instead of ``touch tests/__init__.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/__init__.py

  the terminal_ goes back to the command line

* I make an empty file_ for the actual test

  .. code-block:: shell
    :emphasize-lines: 1

    touch tests/test_telephone.py

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``New-Item tests/test_telephone.py`` instead of ``touch tests/test_telephone.py``

    .. code-block:: shell
      :emphasize-lines: 1

      New-Item tests/test_telephone.py

  the terminal_ goes back to the command line

* I click on ``test_telephone.py`` in the `Integrated Development Environment (IDE)`_ to open it in the :ref:`editor<2 editors>`

  .. TIP:: I can open a file_ from the terminal_ in `Visual Studio Code`_ by typing ``code`` and the name of the file_ with

    .. code-block:: shell
      :emphasize-lines: 1

      code tests/test_telephone.py

  ``test_telephone.py`` opens up in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-11

    import unittest


    class TestTelephone(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions Encountered
    # AssertionError

* I make a `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m venv .venv

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python3 -m venv .venv`` instead of ``python3 -m venv .venv``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m venv .venv

  the terminal_ takes some time then goes back to the command line

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` instead of ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/telephone

* I upgrade the `Python package manager (pip)`_ to the latest version

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --upgrade pip

  the terminal_ shows pip_ being uninstalled then installs the latest version or shows that it is already the latest version

* I make a ``requirements.txt`` file for the `Python programs`_ my project needs

  .. code-block:: shell
    :emphasize-lines: 1

    echo "pytest-watch" > requirements.txt

  the terminal_ goes back to the command line

* I use pip_ to use the requirements file_ to install ``pytest-watch``

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install --requirement requirements.txt

  .. admonition:: on Windows without `Windows Subsystem for Linux`_ use ``python -m pip install --requirement requirements.txt`` instead of ``python3 -m pip install --requirement requirements.txt``

    .. code-block:: shell
      :emphasize-lines: 1

      python -m pip install --requirement requirements.txt

  the terminal_ shows pip_ downloads and installs the `Python programs`_ that `pytest-watch`_ needs to run

* I run the tests

  .. code-block:: shell
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 10

    ================================ FAILURES ================================
    ______________________ TestTelephone.test_failure ________________________

    self = <tests.test_telephone.TestTelephone testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_telephone.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_telephone.py::TestTelephone::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_telephone.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

----

*********************************************************************************
test_passing_a_string
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I change ``test_failure`` to ``test_passing_a_string``

.. code-block:: python
  :linenos:
  :emphasize-lines: 6-10

  import unittest


  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          self.assertEqual(
              src.telephone.text("hello"),
              "I received: hello"
          )


  # Exceptions Encountered

the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: shell

  NameError: name 'src' is not defined

there is no definition for ``src`` in ``test_telephone.py``

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the error to the list of :ref:`Exceptions<errors>` encountered

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

* then I add an `import statement`_ for the ``telephone`` :ref:`module<ModuleNotFoundError>` which is in the ``src`` folder_, at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.telephone
    import unittest


    class TestTelephone(unittest.TestCase):

  the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.telephone' has no attribute 'text'

  there is no definition for ``text`` in ``telephone.py`` in the ``src`` folder_

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I open ``telephone.py`` from the ``src`` folder in the :ref:`editor<2 editors>`, then add a name

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'text' is not defined

  the name is in the file_ but I have not told Python_ what it means

* I point ``text`` to :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I cannot call :ref:`None` the way I can call a :ref:`function<functions>`

* I add the error to the list of :ref:`Exceptions<errors>` encountered in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I change ``text`` to a :ref:`function<functions>` in ``telephone.py`` to make it callable_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: text() takes 0 positional arguments but 1 was given

  ``src.telephone.text`` was called with ``"hello"`` as input but the definition of the :ref:`function<functions>` does not take any input - the parentheses are empty

* I make the :ref:`function<functions>` take input and call it ``the_input``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def text(the_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != 'I received: hello'

  the test expects ``'I received: hello'`` and the ``text`` :ref:`function<functions>` returns :ref:`None`

* I copy the string_ from the terminal_ and paste it in the `return statement`_ to replace :ref:`None`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return 'I received: hello'

  the test passes!

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

The problem with this solution is that the ``text`` :ref:`function<functions>` does not care about the input it gets, it always returns ``'I received: hello'`` when called. I want it to return the value it gets as part of the message.

---------------------------------------------------------------------------------
:red:`RED`: make it fail
---------------------------------------------------------------------------------

I add a new :ref:`assertion<AssertionError>` to ``test_passing_a_string`` in ``test_telephone.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6-9

      def test_passing_a_string(self):
          self.assertEqual(
              src.telephone.text("hello"),
              "I received: hello"
          )
          self.assertEqual(
              src.telephone.text("yes"),
              "I received: yes"
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'I received: hello' != 'I received: yes'

the ``text`` :ref:`function<functions>` always returns ``'I received: hello'``, the test expects ``'I received: yes'``

---------------------------------------------------------------------------------
:green:`GREEN`: make it pass
---------------------------------------------------------------------------------

I change the `return statement`_ in ``telephone.py`` to match

.. code-block:: python
  :linenos:
  :emphasize-lines: 2

  def text(the_input):
      return 'I received: yes'

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'I received: yes' != 'I received: hello'

it did not work, my change broke the test that was passing before. The `return statement`_ has to use the input

=================================================================================
string interpolation
=================================================================================

I use an `f-string`_ which lets me add any values I want to a string_

.. code-block:: python
  :linenos:
  :emphasize-lines: 2

  def text(the_input):
      return f'I received: {the_input}'

the test passes.

This is called `string interpolation`_, I can use it to put values in strings_.

A string_ is any characters inside :ref:`quotes` e.g.

- ``'single quotes'``
- ``'''triple single quotes'''``
- ``"double quotes"``
- ``"""triple double quotes"""``

----

*********************************************************************************
test_passing_a_class
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a failing test in ``test_telephone.py`` to see what happens when I pass a :ref:`class <classes>` from a test to the ``text`` :ref:`function<functions>`

.. code-block:: python
  :lineno-start: 12
  :emphasize-lines: 6-10

          self.assertEqual(
              src.telephone.text("yes"),
              "I received: yes"
          )

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: object"
          )


  # Exceptions Encountered

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: "I received: <class 'object'>" != 'I received: object'

:ref:`object<classes>` is the mother :ref:`class<classes>` that all Python_ :ref:`classes<classes>` come from

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation in the test to match the result

.. code-block:: python
  :lineno-start: 17
  :emphasize-lines: 4

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: <class 'object'>"
          )

the test passes

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

* I add another :ref:`assertion<AssertionError>` with the ``TestTelephone`` :ref:`class<classes>` to ``test_passing_a_class`` in ``test_telephone.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-9

        def test_passing_a_class(self):
            self.assertEqual(
                src.telephone.text(object),
                "I received: <class 'object'>"
            )
            self.assertEqual(
                src.telephone.text(TestTelephone),
                "I received: <class 'object'>"
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: "I received: <class 'tests.test_telephone.TestTelephone'>" != "I received: <class 'object'>"

  even though they are both :ref:`classes`, :ref:`object<classes>` and ``TestTelephone`` are different

* I change the expectation

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 8

        def test_passing_a_class(self):
            self.assertEqual(
                src.telephone.text(object),
                "I received: <class 'object'>"
            )
            self.assertEqual(
                src.telephone.text(TestTelephone),
                "I received: <class 'tests.test_telephone.TestTelephone'>"
            )

  the test passes

----

*********************************************************************************
test_passing_none
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a new failing test for :ref:`None` in ``test_telephone.py``

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 6-10

          self.assertEqual(
              src.telephone.text(TestTelephone),
              "I received: <class 'tests.test_telephone.TestTelephone'>"
          )

      def test_passing_none(self):
          self.assertEqual(
              src.telephone.text(None),
              "I received: 'None'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'I received: None' != "I received: 'None'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the :ref:`quotes` from around :ref:`None` in the expectation

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 4

      def test_passing_none(self):
          self.assertEqual(
              src.telephone.text(None),
              "I received: None"
          )


  # Exceptions Encountered

the test passes.

----

*********************************************************************************
test_passing_a_boolean
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for :ref:`booleans`, first with an :ref:`assertion<AssertionError>` for :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 7-11

      def test_passing_none(self):
          self.assertEqual(
              src.telephone.text(None),
              "I received: None"
          )

      def test_passing_a_boolean(self):
          self.assertEqual(
              src.telephone.text(True),
              "I received: 'True'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: "I received: True" != "I received: 'True'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I change the expectation

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4

        def test_passing_a_boolean(self):
            self.assertEqual(
                src.telephone.text(True),
                "I received: True"
            )

  the test passes

* I add an :ref:`assertion<AssertionError>` for :ref:`False<test_what_is_false>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6-9

        def test_passing_a_boolean(self):
            self.assertEqual(
                src.telephone.text(True),
                "I received: True"
            )
            self.assertEqual(
                src.telephone.text(False),
                "I received: 'False'"
            )

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: "I received: False" != "I received: 'False'"

* I change the expectation

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 8

        def test_passing_a_boolean(self):
            self.assertEqual(
                src.telephone.text(True),
                "I received: True"
            )
            self.assertEqual(
                src.telephone.text(False),
                "I received: False"
            )


    # Exceptions Encountered

  the test passes.

----

*********************************************************************************
test_passing_an_integer
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for an integer_ (a whole number)

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 6-10

          self.assertEqual(
              src.telephone.text(False),
              "I received: False"
          )

      def test_passing_an_integer(self):
          self.assertEqual(
              src.telephone.text(1234),
              "I received: '1234'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'I received: 1234' != "I received: '1234'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the :ref:`quotes` from the expectation

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 4

      def test_passing_an_integer(self):
          self.assertEqual(
              src.telephone.text(1234),
              "I received: 1234"
          )


  # Exceptions Encountered

the test passes.

----

*********************************************************************************
test_passing_a_float
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for a float_ (floating point decimal numbers)

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 7-11

      def test_passing_an_integer(self):
          self.assertEqual(
              src.telephone.text(1234),
              "I received: 1234"
          )

      def test_passing_a_float(self):
          self.assertEqual(
              src.telephone.text(1.234),
              "I received: '1.234'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: 'I received: 1.234' != "I received: '1.234'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I remove the :ref:`quotes` from the number

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 4

      def test_passing_a_float(self):
          self.assertEqual(
              src.telephone.text(1.234),
              "I received: 1.234"
          )


  # Exceptions Encountered

the test passes.

----

*********************************************************************************
test_passing_a_tuple
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for a tuple_ (things in parentheses (``()``), separated by a comma)

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 7-11

      def test_passing_a_float(self):
          self.assertEqual(
              src.telephone.text(1.234),
              "I received: 1.234"
          )

      def test_passing_a_tuple(self):
          self.assertEqual(
              src.telephone.text((1, 2, 3, "n")),
              "I received: '(1, 2, 3, n)'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: "I received: (1, 2, 3, 'n')" != "I received: '(1, 2, 3, n)'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 4

      def test_passing_a_tuple(self):
          self.assertEqual(
              src.telephone.text((1, 2, 3, "n")),
              "I received: (1, 2, 3, 'n')"
          )

the test passes.

----

*********************************************************************************
test_passing_a_list
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for a :ref:`list <lists>` (things in square brackets (``[]``), separated by a comma)

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 7-11

      def test_passing_a_tuple(self):
          self.assertEqual(
              src.telephone.text((1, 2, 3, "n")),
              "I received: (1, 2, 3, 'n')"
          )

      def test_passing_a_list(self):
          self.assertEqual(
              src.telephone.text([1, 2, 3, "n"]),
              "I received: '[1, 2, 3, n]'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: "I received: [1, 2, 3, 'n']" != "I received: '[1, 2, 3, n]'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation to match reality

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 4

      def test_passing_a_list(self):
          self.assertEqual(
              src.telephone.text([1, 2, 3, "n"]),
              "I received: [1, 2, 3, 'n']"
          )

the test passes.

----

*********************************************************************************
test_passing_a_dictionary
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

I add a test for a :ref:`dictionary <dictionaries>` (key-value pairs in curly braces (``{}``), separated by a comma)

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 7-14

      def test_passing_a_list(self):
          self.assertEqual(
              src.telephone.text([1, 2, 3, "n"]),
              "I received: [1, 2, 3, 'n']"
          )

      def test_passing_a_dictionary(self):
          self.assertEqual(
              src.telephone.text({
                  "key1": "value1",
                  "keyN": [0, 1, 2, "n"],
              }),
              "I received: '{key1: value1, keyN: [0, 1, 2, 'n']}'"
          )

the terminal_ shows :ref:`AssertionError`

.. code-block:: shell

  AssertionError: "I received: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}" != "I received: '{key1: value1, keyN: [0, 1, 2, 'n']}'"

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

I change the expectation

.. code-block:: python
  :lineno-start: 67
  :emphasize-lines: 7

      def test_passing_a_dictionary(self):
          self.assertEqual(
              src.telephone.text({
                  "key1": "value1",
                  "keyN": [0, 1, 2, "n"],
              }),
              "I received: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
          )


  # Exceptions Encountered

the terminal_ shows all tests are passing.

----

*********************************************************************************
test_telephone
*********************************************************************************

Time to write the program_ that makes the tests pass without looking at ``test_telephone.py``

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I close ``test_telephone.py``
* then delete all the text in ``telephone.py``, the terminal_ shows 9 failures, I start with the last :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.telephone' has no attribute 'text'

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

* I add the name to ``telephone.py``

  .. code-block:: python
    :linenos:

    text

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'text' is not defined

  I point it to :ref:`None`

  .. code-block:: python
    :linenos:

    text = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  I make ``text`` a :ref:`function<functions>`

  .. code-block:: python
    :linenos:

    def text():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: text() takes 0 positional arguments but 1 was given

  I make the :ref:`function<functions>` take input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def text(the_input):
        return None

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: None != 'I received: None'

* I copy the string_ from the terminal_ and paste it in the `return statement`_ to match the expectation of the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return 'I received: None'

  the terminal_ shows :ref:`AssertionError`

  .. code-block:: shell

    AssertionError: 'I received: None' != 'I received: 1234'

* I add a `return statement`_ to see the difference between the input and the expected output

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return the_input
        return 'I received: None'

  the test summary info shows that every test has :ref:`AssertionError`

  .. code-block:: shell
    :force:

    AssertionError: True != 'I received: True'
    AssertionError: <class 'object'> != "I received: <class 'object'>"
    AssertionError: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']} != "I received: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
    AssertionError: 1.234 != 'I received: 1.234'
    AssertionError: [1, 2, 3, 'n'] != "I received: [1, 2, 3, 'n']"
    AssertionError: "hello" != 'I received: hello'
    AssertionError: (1, 2, 3, 'n') != "I received: (1, 2, 3, 'n')"
    AssertionError: 1234 != 'I received: 1234'
    AssertionError: None != 'I received: None'

  they all expect the input as part of the message

* I remove the first `return statement`_ then make the second one use an `f-string`_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def text(the_input):
        return f'I received: {the_input}'

  and all the tests are passing! Once again! I am a programmer!!

----

*********************************************************************************
review
*********************************************************************************

Here are the tests I ran to see what happens when I pass Python_ basic :ref:`data structures` from a test to a program_ and place them in an `f-string`_ which is one way to do :ref:`string interpolation`

* `test_passing_a_string`_
* `test_passing_a_class`_
* `test_passing_none`_
* `test_passing_a_boolean`_
* `test_passing_an_integer`_
* `test_passing_a_float`_
* `test_passing_a_tuple`_
* `test_passing_a_list`_
* `test_passing_a_dictionary`_

I also ran into the following :ref:`Exceptions<errors>`

* :ref:`AssertionError`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError`
* :ref:`TypeError`

----

:ref:`Click Here to see the code from this chapter<how to pass values: tests and solution>`

----

*********************************************************************************
what is next?
*********************************************************************************

you have covered a bit so far and know

* :ref:`how to make a test driven development environment`
* :ref:`how to raise AssertionError with assert methods<AssertionError>`
* :ref:`how to write functions<functions>` and
* :ref:`how to pass values from tests to functions<how to pass values>`

Would you like to use some of the `assert methods`_ from :ref:`AssertionError` to :ref:`test Python's data structures?<data structures>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->