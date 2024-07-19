.. include:: ../links.rst

#################################################################################
how to pass values
#################################################################################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Og17sfCamr0?si=zPQO30JbmFjTiprI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

This is how to pass values from tests to programs with `f-strings`_

*********************************************************************************
test_passing_a_string
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal and run :ref:`makePythonTdd.sh` with ``telephone`` as the project name

  .. code-block:: python

    ./makePythonTdd.sh telephone

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 telephone

  and it shows an :ref:`AssertionError` after making the files I need

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_telephone.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and click on ``tests/test_telephone.py:7`` with the mouse to open it
* and change ``True`` to ``False`` to make ``test_failure`` pass
* then change ``test_failure`` to ``test_passing_a_string``

  .. code-block:: python

    class TestTelephone(unittest.TestCase):

        def test_passing_a_string(self):
            self.assertEqual(
                src.telephone.text('hello'),
                "I received this message: hello"
            )

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

* which I add to the list of telephone

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

green: make it pass
#################################################################################

* I add an `import statement`_ for the ``telephone`` module

  .. code-block:: python

    import src.telephone
    import unittest

  the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

* I add the error to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

- then add a name to ``telephone.py``

  .. code-block:: python

    text

  and the terminal shows a NameError_

  .. code-block:: python

    NameError: name 'text' is not defined

- I assign ``text`` to the null value :ref:`None`

  .. code-block:: python

    text = None

  and the terminal shows a :ref:`TypeError` because :ref:`None` is not callable_ and ``text`` is currently :ref:`None`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

- I add the exception to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

- I make ``text`` a :ref:`function<functions>` to make it callable_

  .. code-block:: python

      def text():
          return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  I gave ``hello`` as input when I called ``src.telephone.text`` in the test , but the current signature of the ``text`` :ref:`function<functions>` does not allow it accept any inputs
- I change the definition for ``text`` to make it accept a value as input

  .. code-block:: python

    def text(value):
        return None

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received this message: hello'

- I copy the text from the terminal and paste it in the `return statement`_ to make it match the expectation

  .. code-block:: python

    def text(value):
        return 'I received this message: hello'

refactor: make it better
#################################################################################

The problem with this solution is that no matter what value I send to the ``text`` :ref:`function<functions>` it will always return ``'I received this message: hello'``, it is a :doc:`singleton function </functions/test_singleton_functions>`. I want to make it return the value it receives by using an `f-string`_

red: make it fail
---------------------------------------------------------------------------------

I add a new assertion to ``test_passing_a_string``

.. code-block:: python

  def test_passing_a_string(self):
      self.assertEqual(
          src.telephone.text('hello'),
          "I received this message: hello"
      )
      self.assertEqual(
          src.telephone.text('yes'),
          "I received this message: yes"
      )


the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: hello' != 'I received this message: yes'

green: make it pass
---------------------------------------------------------------------------------

I change the string_ in the `return statement`_ to an `f-string` in the ``text`` :ref:`function<functions>`, this allows me to pass values to the string_. It is called `string interpolation`_

.. code-block:: python

  def text(value):
      return f'I received this message: {value}'

the terminal shows the test passed

----

I want to try this with other Python :doc:`/data_structures/data_structures` to see what happens

*********************************************************************************
test_passing_None
*********************************************************************************

red: make it fail
#################################################################################

I add a new failing test

.. code-block:: python

  def test_passing_None(self):
      self.assertEqual(
          src.telephone.text(None),
          "I received this message: 'None'"
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: None' != "I received this message: 'None'"

green: make it pass
#################################################################################

I change the expectation to match reality

.. code-block:: python

  self.assertEqual(
      src.telephone.text(None),
      "I received this message: None"
  )

and the test passes

*********************************************************************************
test_passing_a_class
*********************************************************************************

red: make it fail
#################################################################################

What happens when I pass in a :ref:`class <classes>` to the ``text`` :ref:`function<functions>`?

.. code-block:: python

  def test_passing_a_class(self):
      self.assertEqual(
          src.telephone.text(bool),
          "I received this message: bool"
      )

the terminal shows an :ref:`AssertionError` ::

  AssertionError: "I received this message: <class 'bool'>" != 'I received this message: bool'

green: make it pass
#################################################################################

I make the test match the expectation and the test passes

.. code-block:: python

  def test_passing_a_class(self):
      self.assertEqual(
          src.telephone.text(bool),
          "I received this message: <class 'bool'>"
      )

*********************************************************************************
test_passing_an_integer
*********************************************************************************

I also add a test for an integer_

.. code-block:: python

  def test_passing_an_integer(self):
      self.assertEqual(
          src.telephone.text(1234),
          "I received this message: '1234'"
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: 1234' != "I received this message: '1234'"

green: make it pass
#################################################################################

I remove the quotes from the expectation to make the test pass

.. code-block:: python

  def test_passing_an_integer(self):
      self.assertEqual(
          src.telephone.text(1234),
          "I received this message: 1234"
      )

*********************************************************************************
test_passing_a_float
*********************************************************************************

red: make it fail
#################################################################################

then add a test for a float_

.. code-block:: python

  def test_passing_a_float(self):
      self.assertEqual(
          src.telephone.text(1.234),
          "I received this message: '1.234'"
      )

and the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: 1.234' != "I received this message: '1.234'"

green: make it pass
#################################################################################

I remove the quotes from the expectation to make the test pass

.. code-block:: python

  def test_passing_a_float(self):
      self.assertEqual(
          src.telephone.text(1.234),
          "I received this message: 1.234"
      )

*********************************************************************************
test_passing_a_tuple
*********************************************************************************

red: make it fail
#################################################################################

then add a test for a tuple_

.. code-block:: python

  def test_passing_a_tuple(self):
      self.assertEqual(
          src.telephone.text((1, 2, 3, 'n')),
          "I received this message: '(1, 2, 3, n)'"
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received this message: (1, 2, 3, 'n')" != "I received this message: '(1, 2, 3, n)'"

green: make it pass
#################################################################################

and I make the expectation match reality

.. code-block:: python

  def test_passing_a_tuple(self):
      self.assertEqual(
          src.telephone.text((1, 2, 3, 'n')),
          "I received this message: (1, 2, 3, 'n')"
      )

*********************************************************************************
test_passing_a_list
*********************************************************************************

red: make it fail
#################################################################################

I add a test for a :doc:`list </data_structures/lists/lists>`

.. code-block:: python

  def test_passing_a_list(self):
      self.assertEqual(
          src.telephone.text([1, 2, 3, 'n']),
          "I received this message: '[1, 2, 3, n]'"
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received this message: [1, 2, 3, 'n']" != "I received this message: '[1, 2, 3, n]'"

green: make it pass
#################################################################################

I change the expectation to match reality

.. code-block:: python

  def test_passing_a_list(self):
      self.assertEqual(
          src.telephone.text([1, 2, 3, 'n']),
          "I received this message: [1, 2, 3, 'n']"
      )

*********************************************************************************
test_passing_a_dictionary
*********************************************************************************

red: make it fail
#################################################################################

finally, I add a test for a :doc:`dictionary </data_structures/dictionaries>`

.. code-block:: python

  def test_passing_a_dictionary(self):
      self.assertEqual(
          src.telephone.text({
              "key1": "value1",
              "keyN": "valueN"
          }),
          "I received this message: '{key1: value1, keyN: valueN}'"
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: "I received this message: {'key1': 'value1', 'keyN': 'valueN'}" != "I received this message: '{key1: value1, keyN: valueN}'"

green: make it pass
#################################################################################

I make the expectation match reality

.. code-block:: python

  def test_passing_a_dictionary(self):
      self.assertEqual(
          src.telephone.text({"key1": "value1", "keyN": "valueN"}),
          "I received this message: {'key1': 'value1', 'keyN': 'valueN'}"
      )

and the terminal shows all tests are passing

----

*********************************************************************************
test_telephone
*********************************************************************************

time to write the program that make the test in ``test_telephone.py`` pass without looking at it

red: make it fail
#################################################################################

* I close ``test_telephone.py``
* then delete all the text in ``telephone.py`` and the terminal shows an :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

green: make it pass
#################################################################################

* I add the name to ``telephone.py``

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

  I define it as a :ref:`function<functions>`

  .. code-block:: python

    def text():
        return None

  which gives me another :ref:`TypeError` with a different message

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  and I add a positional argument to the :ref:`function's'<functions>` signature

  .. code-block: python

    def text(argument):
        return None

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received this message: 1234'

* I change the `return statement`_ to match the expectation

  .. code-block:: python

    def text(argument):
        return 'I received this message: hello'

  and get another :ref:`AssertionError`

  .. code-block:: python

    AssertionError: 'I received this message: hello' != 'I received this message: yes'

* I add a `return statement`_ to see the difference between the input and the expected output

  .. code-block:: python

    def text(argument):
        return argument
        return 'I received this message: 1234'

  the test summary info shows an :ref:`AssertionError` for each test

  .. code-block:: python

    AssertionError: None != 'I received this message: None'
    AssertionError: <class 'bool'> != "I received this message: <class 'bool'>"
    AssertionError: {'key1': 'value1', 'keyN': 'valueN'} != "I received this message: {'key1': 'value1', 'keyN': 'v...
    AssertionError: 1.234 != 'I received this message: 1.234'
    AssertionError: [1, 2, 3, 'n'] != "I received this message: [1, 2, 3, 'n']"
    AssertionError: 'hello' != 'I received this message: hello'
    AssertionError: (1, 2, 3, 'n') != "I received this message: (1, 2, 3, 'n')"
    AssertionError: 1234 != 'I received this message: 1234'

  the tests expect the message to have the the argument passed

* I change the `return statement`_ to use an `f-string`

  .. code-block:: python

    def text(argument):
        return f'I received this message: {argument}'

  and the test passes

----

*********************************************************************************
review
*********************************************************************************

VOILA! You now know how to pass values from a test to a program and can represent values in a string_ with an `f-string`_

You also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to test :doc:`/how_to/make_person`?

----

:doc:`/code/code_pass_values`