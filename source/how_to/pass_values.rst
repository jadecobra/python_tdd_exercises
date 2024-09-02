.. include:: ../links.rst

#################################################################################
how to pass values
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/Og17sfCamr0?si=zPQO30JbmFjTiprI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

I want to test passing values to programs

*********************************************************************************
test_passing_a_string
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal to run :ref:`makePythonTdd.sh` with ``telephone`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh telephone

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 telephone

  and it shows an :ref:`AssertionError` after making the folders and files for the project

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_telephone.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_telephone.py:7`` with the mouse to open it
* then change ``True`` to ``False`` to make the test pass
* and change ``test_failure`` to ``test_passing_a_string``

  .. code-block:: python

    class TestTelephone(unittest.TestCase):

        def test_passing_a_string(self):
            self.assertEqual(
                src.telephone.text("hello"),
                "I received: hello"
            )

  I get a NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

green: make it pass
#################################################################################

* I add it to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

* then add an `import statement`_ for the ``telephone`` module

  .. code-block:: python

    import src.telephone
    import unittest

  which gives me an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

* another one for the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a name to ``telephone.py``

  .. code-block:: python

    text

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'text' is not defined

* then I assign ``text`` to :ref:`None`

  .. code-block:: python

    text = None

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* then change ``text`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python

      def text():
          return None

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  ``src.telephone.text`` was called with input but the definition of the :ref:`function<functions>` does not allow this

* I make it take a value

  .. code-block:: python

    def text(value):
        return None

  and get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received: hello'

* when I copy the string_ from the terminal and paste it in the `return statement`_ to replace :ref:`None`

  .. code-block:: python

    def text(value):
        return 'I received: hello'

  the test passes!

refactor: make it better
#################################################################################

The problem with this solution is that the ``text`` :ref:`function<functions>` will always return ``'I received: hello'``, it does not care about the input, it is a :doc:`singleton function </functions/test_singleton_functions>`. I want it to return the value it receives as part of the message.

red: make it fail
---------------------------------------------------------------------------------

I add a new assertion to ``test_passing_a_string``

.. code-block:: python

  def test_passing_a_string(self):
      self.assertEqual(
          src.telephone.text("hello"),
          "I received: hello"
      )
      self.assertEqual(
          src.telephone.text("yes"),
          "I received: yes"
      )

which gives me an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: hello' != 'I received: yes'

green: make it pass
---------------------------------------------------------------------------------

* when I make the `return statement`_ match the expectation

  .. code-block:: python

    def text(value):
        return 'I received: yes'

  I get an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'I received: yes' != 'I received: hello'

  this will not work, the `return statement`_ has to use the input

* I use an `f-string`_ to add values to the string_

  .. code-block:: python

    def text(value):
        return f'I received: {value}'

  and the terminal shows a passing test. This is called `string interpolation`_

----

I want to see what happens when I do this with other Python :doc:`/data_structures/data_structures`

*********************************************************************************
test_passing_a_class
*********************************************************************************

red: make it fail
#################################################################################

I add a failing test for a :ref:`class <classes>`

.. code-block:: python

  def test_passing_a_class(self):
      self.assertEqual(
          src.telephone.text(object),
          "I received: object"
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: <class 'object'>" != 'I received: object'

green: make it pass
#################################################################################

I make the expectation match reality and the test passes

.. code-block:: python

  def test_passing_a_class(self):
      self.assertEqual(
          src.telephone.text(object),
          "I received: <class 'object'>"
      )

refactor: make it better
#################################################################################

I add another assertion with a different :ref:`class<classes>` name

.. code-block:: python

  def test_passing_a_class(self):
      self.assertEqual(
          src.telephone.text(TestTelephone),
          "I received: <class 'object'>"
      )
      self.assertEqual(
          src.telephone.text(TestTelephone),
          "I received: <class 'object'>"
      )

which gives me an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: <class 'tests.test_telephone.TestTelephone'>" != "I received: <class 'object'>"

when I change the name of the :ref:`class<classes>` to match reality

.. code-block:: python

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

I add a new failing test for :ref:`None`

.. code-block:: python

  def test_passing_none(self):
      self.assertEqual(
          src.telephone.text(None),
          "I received: 'None'"
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: None' != "I received: 'None'"

green: make it pass
#################################################################################

I remove the quotes from around :ref:`None` in the expectation

.. code-block:: python

  self.assertEqual(
      src.telephone.text(None),
      "I received: None"
  )

and the test passes.

*********************************************************************************
test_passing_a_boolean
*********************************************************************************

red: make it fail
#################################################################################

I add a test for :ref:`booleans`, first with an assertion for :ref:`True <test_what_is_true>`

.. code-block:: python

  def test_passing_a_boolean(self):
      self.assertEqual(
          src.telephone.text(True),
          "I received: 'True'"
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: True" != "I received: 'True'"

green: make it pass
#################################################################################

* I change the expectation

  .. code-block:: python

    def test_passing_a_boolean(self):
        self.assertEqual(
            src.telephone.text(True),
            "I received: True"
        )

  and the test passes

* then I add an assertion for :ref:`False <test_what_is_false>`

  .. code-block:: python

    def test_passing_a_boolean(self):
        self.assertEqual(
            src.telephone.text(True),
            "I received: True"
        )
        self.assertEqual(
            src.telephone.text(False),
            "I received: 'False'"
        )

  which gives me an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: "I received: False" != "I received: 'False'"

* when I change the expectation

  .. code-block:: python

    self.assertEqual(
        src.telephone.text(False),
        "I received: False"
    )

  the test passes.

*********************************************************************************
test_passing_an_integer
*********************************************************************************

I also add a test for an integer_

.. code-block:: python

  def test_passing_an_integer(self):
      self.assertEqual(
          src.telephone.text(1234),
          "I received: '1234'"
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: 1234' != "I received: '1234'"

green: make it pass
#################################################################################

I remove the quotes from the expectation

.. code-block:: python

  def test_passing_an_integer(self):
      self.assertEqual(
          src.telephone.text(1234),
          "I received: 1234"
      )

and the terminal shows a passing test

*********************************************************************************
test_passing_a_float
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a float_

.. code-block:: python

  def test_passing_a_float(self):
      self.assertEqual(
          src.telephone.text(1.234),
          "I received: '1.234'"
      )

and get an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received: 1.234' != "I received: '1.234'"

green: make it pass
#################################################################################

I remove the quotes from the number

.. code-block:: python

  def test_passing_a_float(self):
      self.assertEqual(
          src.telephone.text(1.234),
          "I received: 1.234"
      )

and the test shows passing tests.

*********************************************************************************
test_passing_a_tuple
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a tuple_

.. code-block:: python

  def test_passing_a_tuple(self):
      self.assertEqual(
          src.telephone.text((1, 2, 3, "n")),
          "I received: '(1, 2, 3, n)'"
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: (1, 2, 3, 'n')" != "I received: '(1, 2, 3, n)'"

green: make it pass
#################################################################################

I make the expectation match reality

.. code-block:: python

  def test_passing_a_tuple(self):
      self.assertEqual(
          src.telephone.text((1, 2, 3, "n")),
          "I received: (1, 2, 3, 'n')"
      )

and the terminal shows green again.

*********************************************************************************
test_passing_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a :doc:`list </data_structures/lists/lists>`

.. code-block:: python

  def test_passing_a_list(self):
      self.assertEqual(
          src.telephone.text([1, 2, 3, "n"]),
          "I received: '[1, 2, 3, n]'"
      )

and get an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: [1, 2, 3, 'n']" != "I received: '[1, 2, 3, n]'"

green: make it pass
#################################################################################

I change the expectation to match reality

.. code-block:: python

  def test_passing_a_list(self):
      self.assertEqual(
          src.telephone.text([1, 2, 3, "n"]),
          "I received: [1, 2, 3, 'n']"
      )

and the terminal shows passing tests.

*********************************************************************************
test_passing_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a :doc:`dictionary </data_structures/dictionaries>`

.. code-block:: python

  def test_passing_a_dictionary(self):
      self.assertEqual(
          src.telephone.text({
              "key1": "value1",
              "keyN": "valueN",
          }),
          "I received: '{key1: value1, keyN: valueN}'"
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received: {'key1': 'value1', 'keyN': 'valueN'}" != "I received: '{key1: value1, keyN: valueN}'"

green: make it pass
#################################################################################

when I make the expectation match reality

.. code-block:: python

  def test_passing_a_dictionary(self):
      self.assertEqual(
          src.telephone.text({
              "key1": "value1",
              "keyN": "valueN"
          }),
          "I received: {'key1': 'value1', 'keyN': 'valueN'}"
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
* then delete the text in ``telephone.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

green: make it pass
#################################################################################

* I add the name

  .. code-block:: python

    text

  and get a NameError_

  .. code-block:: python

    NameError: name 'text' is not defined

  I assign it to :ref:`None`

  .. code-block:: python

    text = None

  and the terminal shows a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  when I make it a :ref:`function<functions>`

  .. code-block:: python

    def text():
        return None

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  I add a positional argument to the :ref:`function's<functions>` signature

  .. code-block:: python

    def text(argument):
        return None

  and the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received: None'

* I copy the string_ from the terminal, paste it in the `return statement`_ to match the expectation of the test

  .. code-block:: python

    def text(argument):
        return 'I received: None'

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'I received: None' != 'I received: 1234'

* I add a `return statement`_ to see the difference between the input and the expected output

  .. code-block:: python

    def text(argument):
        return argument
        return 'I received: None'

  the test summary info shows that every test has an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: True != 'I received: True'
    AssertionError: <class 'object'> != "I received: <class 'object'>"
    AssertionError: {'key1': 'value1', 'keyN': 'valueN'} != "I received: {'key1': 'value1', 'keyN': 'valueN'}"
    AssertionError: 1.234 != 'I received: 1.234'
    AssertionError: [1, 2, 3, 'n'] != "I received: [1, 2, 3, 'n']"
    AssertionError: "hello" != 'I received: hello'
    AssertionError: (1, 2, 3, 'n') != "I received: (1, 2, 3, 'n')"
    AssertionError: 1234 != 'I received: 1234'
    AssertionError: None != 'I received: None'

  the tests expect the input as part of the message

* I remove the first `return statement`_ then make the second one use an `f-string`_

  .. code-block:: python

    def text(argument):
        return f'I received: {argument}'

  and all tests pass!

----

*********************************************************************************
review
*********************************************************************************

I ran the following tests to see what happens when I pass Python :doc:`/data_structures/data_structures` from a test to a program and place them in an `f-string`_

* `test_passing_a_string`_
* `test_passing_a_class`_
* `test_passing_none`_
* `test_passing_a_boolean`_
* `test_passing_an_integer`_
* `test_passing_a_float`_
* `test_passing_a_tuple`_
* `test_passing_a_list`_
* `test_passing_a_dictionary`_

I also encountered the following :ref:`Exceptions<Exceptions>`

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to test :doc:`/how_to/make_person`?

----

:doc:`/code/code_pass_values`
