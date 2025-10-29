.. meta::
  :description: Master TDD in Python to pass any data type, from strings to classes, and eliminate TypeError. Watch the full tutorial to fix errors in 15 minutes.
  :keywords: Jacob Itegboje, python pass multiple data types to function, python tdd tutorial for beginners, TypeError: 'NoneType' is not callable fix, how to handle different data types as function arguments in python, python pass by reference vs value, python tdd practical example, python unit testing tutorial, python f-string formatting, python NameError resolution, python AttributeError fix

.. include:: ../links.rst

#################################################################################
how to pass values
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/QEiyAO7aEVQ?si=gN_vRO0VrSyWR7R6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

I want to test passing values to programs

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``telephone`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh telephone

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 telephone

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_telephone.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_telephone.py:7`` to open it in the editor
* then I change ``True`` to ``False`` to make the test pass

  .. code-block:: python

    self.assertFalse(False)

* and I change the name of the :ref:`class<classes>` to match the :ref:`CapWords` format

  .. code-block:: python

    class TestSleepDuration(unittest.TestCase):

*********************************************************************************
test_passing_a_string
*********************************************************************************

red: make it fail
#################################################################################

* I change ``test_failure`` to ``test_passing_a_string``

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

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_telephone.py``

  .. code-block:: python
    :emphasize-lines: 3

    # Exceptions Encountered
    # AssertionError
    # NameError

* then I add an `import statement`_ for the ``telephone`` module at the top of ``test_telephone.py``

  .. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

  .. code-block:: python
    :emphasize-lines: 1
    :linenos:

    import src.telephone
    import unittest


    class TestTelephone(unittest.TestCase):
        ...

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_telephone.py``

  .. code-block:: python
    :emphasize-lines: 4

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I click on ``telephone.py`` to open it in the editor, then add a name

  .. code-block:: python

    text

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'text' is not defined

* I point ``text`` to :ref:`None`

  .. code-block:: python

    text = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add it to the list of :ref:`Exceptions<errors>` encountered in ``test_telephone.py``

  .. code-block:: python
    :emphasize-lines: 5

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I change ``text`` in ``telephone.py`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python
    :linenos:

      def text():
          return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  ``src.telephone.text`` was called with ``"hello"`` as input but the definition of the :ref:`function<functions>` does not take any input, the parentheses are empty

* I make the :ref:`function<functions>` take input and call it ``value``

  .. code-block:: python
    :emphasize-lines: 1

    def text(value):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received: hello'

* when I copy the string_ from the terminal and paste it in the `return statement`_ to replace :ref:`None` in ``telephone.py``

  .. code-block:: python
    :emphasize-lines: 2

    def text(value):
        return 'I received: hello'

  the test passes!

refactor: make it better
#################################################################################

The problem with this solution is that the ``text`` :ref:`function<functions>` does not care about the input it receives and will always return ``'I received: hello'``. I want it to return the value it receives as part of the message.

red: make it fail
---------------------------------------------------------------------------------

I add a new :ref:`assertion<AssertionError>` to ``test_passing_a_string`` in ``test_telephone.py``

.. code-block:: python
  :emphasize-lines: 8-11

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          self.assertEqual(
              src.telephone.text("hello"),
              "I received: hello"
          )
          self.assertEqual(
              src.telephone.text("yes"),
              "I received: yes"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: hello' != 'I received: yes'

green: make it pass
---------------------------------------------------------------------------------

* when I make the `return statement`_ in ``telephone.py`` match the expectation

  .. code-block:: python
    :emphasize-lines: 2

    def text(value):
        return 'I received: yes'

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'I received: yes' != 'I received: hello'

  this will not work, my change made a test that was passing before, fail. The `return statement`_ has to use the input

* I use an `f-string`_ to add values to the string_

  .. code-block:: python
    :emphasize-lines: 2

    def text(value):
        return f'I received: {value}'

  the test passes. This is called `string interpolation`_, I can use it to put values in strings_. A string_ is any characters in between quotes e.g.

  - ``'a string made with single quotes'``
  - ``"a string made with double quotes"``
  - ``'''a string made with triple single quotes'''``
  - ``"""a string made with triple double quotes"""``

----

I want to see what happens when I pass other Python_ :ref:`data structures` to the program

*********************************************************************************
test_passing_a_class
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test for a :ref:`class <classes>` in ``test_telephone.py``

.. code-block:: python
  :emphasize-lines: 13-17

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          self.assertEqual(
              src.telephone.text("hello"),
              "I received: hello"
          )
          self.assertEqual(
              src.telephone.text("yes"),
              "I received: yes"
          )

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: object"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: <class 'object'>" != 'I received: object'

object_ is the mother :ref:`class<classes>` that all Python_ :ref:`classes<classes>` come from

green: make it pass
#################################################################################

I make the expectation match reality

.. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

.. code-block:: python
  :emphasize-lines: 9

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: <class 'object'>"
          )

the test passes

refactor: make it better
#################################################################################

I add another :ref:`assertion<AssertionError>` to ``test_passing_a_class`` with the ``TestTelephone`` :ref:`class<classes>`

.. code-block:: python
  :emphasize-lines: 11-14

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: <class 'object'>"
          )
          self.assertEqual(
              src.telephone.text(TestTelephone),
              "I received: <class 'object'>"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: <class 'tests.test_telephone.TestTelephone'>" != "I received: <class 'object'>"

when I change the expectation to match reality

.. code-block:: python
  :emphasize-lines: 13

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: <class 'object'>"
          )
          self.assertEqual(
              src.telephone.text(TestTelephone),
              "I received: <class 'tests.test_telephone.TestTelephone'>"
          )

the test passes.

*********************************************************************************
test_passing_none
*********************************************************************************

red: make it fail
#################################################################################

I add a new failing test for :ref:`None` in ``test_telephone.py``

.. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

.. code-block:: python
  :emphasize-lines: 16-20

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          self.assertEqual(
              src.telephone.text(object),
              "I received: <class 'object'>"
          )
          self.assertEqual(
              src.telephone.text(TestTelephone),
              "I received: <class 'tests.test_telephone.TestTelephone'>"
          )

      def test_passing_none(self):
          self.assertEqual(
              src.telephone.text(None),
              "I received: 'None'"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: None' != "I received: 'None'"

green: make it pass
#################################################################################

I remove the quotes from around :ref:`None` in the expectation

.. code-block:: python
  :emphasize-lines: 4

  def test_passing_none(self):
      self.assertEqual(
          src.telephone.text(None),
          "I received: None"
      )

the test passes.

*********************************************************************************
test_passing_a_boolean
*********************************************************************************

red: make it fail
#################################################################################

I add a test for :ref:`booleans`, first with an :ref:`assertion<AssertionError>` for :ref:`True<test_what_is_true>`

.. NOTE:: the ...(ellipsis) represents code that does not need to change in this part

.. code-block:: python
  :emphasize-lines: 15-19

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          ...

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

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: True" != "I received: 'True'"

green: make it pass
#################################################################################

* I change the expectation

  .. code-block:: python
    :emphasize-lines: 4

    def test_passing_a_boolean(self):
        self.assertEqual(
            src.telephone.text(True),
            "I received: True"
        )

  the test passes

* I add an :ref:`assertion<AssertionError>` for :ref:`False<test_what_is_false>`

  .. code-block:: python
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

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "I received: False" != "I received: 'False'"

* I change the expectation

  .. code-block:: python
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

  the test passes.

*********************************************************************************
test_passing_an_integer
*********************************************************************************

red: make it fail
#################################################################################

I add a test for an integer_

.. code-block:: python
  :emphasize-lines: 15-19

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          ...

      def test_passing_none(self):
          ...

      def test_passing_a_boolean(self):
          ...

      def test_passing_an_integer(self):
          self.assertEqual(
              src.telephone.text(1234),
              "I received: '1234'"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: 1234' != "I received: '1234'"

green: make it pass
#################################################################################

I remove the quotes from the expectation

.. code-block:: python
  :emphasize-lines: 4

  def test_passing_an_integer(self):
      self.assertEqual(
          src.telephone.text(1234),
          "I received: 1234"
      )

the test passes.

*********************************************************************************
test_passing_a_float
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a float_

.. code-block:: python
  :emphasize-lines: 18-22

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          ...

      def test_passing_none(self):
          ...

      def test_passing_a_boolean(self):
          ...

      def test_passing_an_integer(self):
          ...

      def test_passing_a_float(self):
          self.assertEqual(
              src.telephone.text(1.234),
              "I received: '1.234'"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: 1.234' != "I received: '1.234'"

green: make it pass
#################################################################################

I remove the quotes from the number

.. code-block:: python
  :emphasize-lines: 4

  def test_passing_a_float(self):
      self.assertEqual(
          src.telephone.text(1.234),
          "I received: 1.234"
      )

the test passes.

*********************************************************************************
test_passing_a_tuple
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a tuple_

.. code-block:: python
  :emphasize-lines: 21-25

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          ...

      def test_passing_none(self):
          ...

      def test_passing_a_boolean(self):
          ...

      def test_passing_an_integer(self):
          ...

      def test_passing_a_float(self):
          ...

      def test_passing_a_tuple(self):
          self.assertEqual(
              src.telephone.text((1, 2, 3, "n")),
              "I received: '(1, 2, 3, n)'"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: (1, 2, 3, 'n')" != "I received: '(1, 2, 3, n)'"

green: make it pass
#################################################################################

I make the expectation match reality

.. code-block:: python
  :emphasize-lines: 4

  def test_passing_a_tuple(self):
      self.assertEqual(
          src.telephone.text((1, 2, 3, "n")),
          "I received: (1, 2, 3, 'n')"
      )

the test passes.

*********************************************************************************
test_passing_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a :ref:`list <lists>`

.. code-block:: python
  :emphasize-lines: 24-28

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          ...

      def test_passing_none(self):
          ...

      def test_passing_a_boolean(self):
          ...

      def test_passing_an_integer(self):
          ...

      def test_passing_a_float(self):
          ...

      def test_passing_a_tuple(self):
          ...

      def test_passing_a_list(self):
          self.assertEqual(
              src.telephone.text([1, 2, 3, "n"]),
              "I received: '[1, 2, 3, n]'"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: [1, 2, 3, 'n']" != "I received: '[1, 2, 3, n]'"

green: make it pass
#################################################################################

I change the expectation to match reality

.. code-block:: python
  :emphasize-lines: 4

  def test_passing_a_list(self):
      self.assertEqual(
          src.telephone.text([1, 2, 3, "n"]),
          "I received: [1, 2, 3, 'n']"
      )

the test passes.

*********************************************************************************
test_passing_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a :ref:`dictionary <dictionaries>`

.. code-block:: python
  :emphasize-lines: 27-34

  class TestTelephone(unittest.TestCase):

      def test_passing_a_string(self):
          ...

      def test_passing_a_class(self):
          ...

      def test_passing_none(self):
          ...

      def test_passing_a_boolean(self):
          ...

      def test_passing_an_integer(self):
          ...

      def test_passing_a_float(self):
          ...

      def test_passing_a_tuple(self):
          ...

      def test_passing_a_list(self):
          ...

      def test_passing_a_dictionary(self):
          self.assertEqual(
              src.telephone.text({
                  "key1": "value1",
                  "keyN": [0, 1, 2, "n"],
              }),
              "I received: '{key1: value1, keyN: [0, 1, 2, 'n']}'"
          )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}" != "I received: '{key1: value1, keyN: [0, 1, 2, 'n']}'"

green: make it pass
#################################################################################

when I make the expectation match reality

.. code-block:: python
  :emphasize-lines: 7

  def test_passing_a_dictionary(self):
      self.assertEqual(
          src.telephone.text({
              "key1": "value1",
              "keyN": [0, 1, 2, "n"],
          }),
          "I received: {'key1': 'value1', 'keyN': [0, 1, 2, 'n']}"
      )

the terminal shows all tests are passing.

----

*********************************************************************************
test_telephone
*********************************************************************************

Time to write the program that makes the tests in ``test_telephone.py`` pass without looking at them

red: make it fail
#################################################################################

* I close ``test_telephone.py``
* then delete all the text in ``telephone.py``, the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

green: make it pass
#################################################################################

* I add the name to ``telephone.py``

  .. code-block:: python

    text

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'text' is not defined

  I point it to :ref:`None`

  .. code-block:: python

    text = None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  I make ``text`` a :ref:`function<functions>`

  .. code-block:: python

    def text():
        return None

  the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  I make the :ref:`function<functions>` take input

  .. code-block:: python
    :emphasize-lines: 1

    def text(argument):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received: None'

* I copy the string_ from the terminal and paste it in the `return statement`_ to match the expectation of the test

  .. code-block:: python
    :emphasize-lines: 2

    def text(argument):
        return 'I received: None'

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'I received: None' != 'I received: 1234'

* I add a `return statement`_ to see the difference between the input and the expected output

  .. code-block:: python
    :emphasize-lines: 2

    def text(argument):
        return argument
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
    :emphasize-lines: 2

    def text(argument):
        return f'I received: {argument}'

  and all the tests are passing! Once again! I am a programmer!!

----

*********************************************************************************
review
*********************************************************************************

Here are the tests I ran to see what happens when I pass Python_ :ref:`data structures` from a test to a program and place them in an `f-string`_

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
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to test :ref:`making a person?<how to make a person>`

----

:ref:`how to pass values: tests and solution`
