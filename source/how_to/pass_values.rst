.. include:: ../links.rst

###################
how to pass values
###################

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Og17sfCamr0?si=zPQO30JbmFjTiprI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

this chapter shows how to pass values from tests to programs using `Formatted string literals <https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals>`_ to place values inside a string

****************
requirements
****************

:doc:`Create a Test Driven Development Environment </how_to/create_tdd_environment>` with ``telephone`` as the project name

----

*******************
red: make it fail
*******************

I add a test to ``test_telephone.py``

.. code-block:: python

  class TestTelephone(unittest.TestCase):

      def test_failure(self):
          self.assertFalse(True)

      def test_text_messages(self):
          self.assertEqual(
              telephone.text('hello'),
              'I received this message: hello'
          )

and the terminal shows a NameError_

.. code-block:: python

  NameError: name 'telephone' is not defined

which I add to the list of exceptions

.. code-block:: python

  # Exceptions Encountered
  # AssertionError
  # NameError

**********************
green: make it pass
**********************

* I remove ``test_failure`` then add an `import statement`_ for the ``telephone`` module

  .. code-block:: python

    import telephone
    import unittest

  the terminal shows an :ref:`AttributeError` ::

    AttributeError: module 'telephone' has no attribute 'text'

* I add the error to the list of exceptions encountered

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

  and the terminal shows a :ref:`TypeError` because ``text`` is not `callable <https://docs.python.org/3/glossary.html#term-callable>`_

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

- I add the exception to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

- I make ``text`` in ``telephone.py`` to a :ref:`function<functions>` to make it `callable <https://docs.python.org/3/glossary.html#term-callable>`_

  .. code-block:: python

      def text():
          return None

  and the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments but 1 was given

  I provided a positional argument as input with the value ``'hello'`` when I called ``telephone.text`` in the test , but the current signature of the ``text`` :ref:`function<functions>` does not allow it accept any inputs
- I make the definition for ``text`` to make it accept a value as input

  .. code-block:: python

    def text(value):
        return None

  the terminal shows an :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != 'I received this message: hello'

- I make the return value to match the expectation and the test pass

  .. code-block:: python

    def text(value):
        return 'I received this message: hello'

**************************
refactor: make it better
**************************

The problem with this solution is that no matter what value I send to the ``text`` :ref:`function<functions>` it will always return ``'I received this message: hello'``. I need to make it return a value based on the input it receives

red: make it fail
=========================

I add a new failing test to ``test_text_messages``

.. code-block:: python

  def test_text_messages(self):
      self.assertEqual(
          telephone.text('hello'),
          'I received this message: hello'
      )
      self.assertEqual(
          telephone.text('yes'),
          'I received this message: yes'
      )


the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: hello' != 'I received this message: yes'

green: make it pass
=========================

I make the ``text`` :ref:`function<functions>` in ``telephone.py`` to use an ``f`` string which allows passing variable values to strings. This is called `string interpolation <https://peps.python.org/pep-0498/>`_

.. code-block:: python

  def text(value):
      return f'I received this message: {value}'

the terminal shows passing tests

**************************
Passing Data Structures
**************************

I want to try this with other python data structures to see what happens

red: make it fail
=========================

I add a new failing test to ``test_text_messages``

.. code-block:: python

  def test_text_messages(self):
      self.assertEqual(
          telephone.text('hello'),
          'I received this message: hello'
      )
      self.assertEqual(
          telephone.text('yes'),
          'I received this message: yes'
      )
      self.assertEqual(
          telephone.text(None),
          'I received this message: "None"'
      )

the terminal shows an :ref:`AssertionError`

.. code-block:: python

  AssertionError: 'I received this message: None' != 'I received this message: "None"'

green: make it pass
=========================

I make the test match the expected value


.. code-block:: python

  self.assertEqual(
      telephone.text(None),
      'I received this message: None'
  )


the terminal shows passing tests

refactor: make it better
=========================

As an exercise I add more tests to ``test_text_messages`` to see what happens when I pass different data structures to the ``text`` function

* What happens when I pass in a :doc:`class </classes/classes>` constructor to the ``text`` function

  .. code-block:: python

    ...
    self.assertEqual(
        telephone.text(None),
        'I received this message: None'
    )
    self.assertEqual(
        telephone.text(bool),
        "I received this message: bool"
    )

  the terminal shows an :ref:`AssertionError` ::

    AssertionError: "I received this message: <class 'bool'>" != 'I received this message: bool'

* I make the test match the expectation and the test passes ::

    self.assertEqual(
        telephone.text(bool),
        "I received this message: <class 'bool'>"
    )

* I also add a test for `integers <https://docs.python.org/3/library/functions.html#int>`_ ::

    self.assertEqual(
        telephone.text(123),
        "I received this message: '123'"
    )

  and the terminal shows an :ref:`AssertionError` ::

    AssertionError: 'I received this message: 123' != "I received this message: '123'"

  I remove the quotes from the test to make it pass ::

    self.assertEqual(
        telephone.text(123),
        "I received this message: 123"
    )


* then add a test for `floats <https://docs.python.org/3/library/functions.html#float>`_ ::

    self.assertEqual(
        telephone.text(1.23),
        "I received this message: '1.23'"
    )

  and the terminal shows an :ref:`AssertionError` ::

    AssertionError: 'I received this message: 1.23' != "I received this message: '1.23'"

  I remove the quotes to make the test pass ::

    self.assertEqual(
        telephone.text(1.23),
        "I received this message: 1.23"
    )

* and add a test for `tuples <https://docs.python.org/3/library/stdtypes.html#tuples>`_ ::

    self.assertEqual(
        telephone.text((1, 2, 3, 'n')),
        "I received this message: '(1, 2, 3, n)'"
    )

  the terminal shows an :ref:`AssertionError` ::

* and add a test for :doc:`lists </data_structures/lists/lists>` ::

    self.assertEqual(
        telephone.text([1, 2, 3, 'n']),
        "I received this message: '[1, 2, 3, n]'"
    )

  the terminal shows an :ref:`AssertionError` ::

    AssertionError: "I received this message: (1, 2, 3, 'n')" != "I received this message: '(1, 2, 3, n)'"

  I make the test match the expectation ::

    self.assertEqual(
        telephone.text((1, 2, 3, 'n')),
        "I received this message: (1, 2, 3, 'n')"
    )

* and add a test for `set <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset>`_ ::

    self.assertEqual(
        telephone.text({1, 2, 3, 'n'}),
        "I received this message: '{1, 2, 3, n}'"
    )

  the terminal shows an :ref:`AssertionError` ::

    AssertionError: "I received this message: {1, 2, 3, 'n'}" != "I received this message: {1, 2, 3, n}'"

  I make the test match the expectation ::

    self.assertEqual(
        telephone.text({1, 2, 3, 'n'}),
        "I received this message: {1, 2, 3, 'n'}"
    )

* finally, I add a test for :doc:`dictionaries </data_structures/dictionaries>` ::

    self.assertEqual(
        telephone.text({"key1": "value1", "keyN": "valueN"}),
        "I received this message: '{key1: value1, keyN: valueN}'"
    )

  the terminal shows an :ref:`AssertionError` ::

    AssertionError: "I received this message: {'key1': 'value1', 'keyN': 'valueN'}" != "I received this message: '{key1: value1, keyN: valueN}'"

  I make the test match the expected output ::

    self.assertEqual(
        telephone.text({"key1": "value1", "keyN": "valueN"}),
        "I received this message: {'key1': 'value1', 'keyN': 'valueN'}"
    )

  and all tests are passing

VOILA! You now know how to pass values from a test to a program and can represent any values as strings using interpolation. You also encountered the following exceptions

* :ref:`AssertionError`
* NameError_
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to know :doc:`/how_to/create_person`?

----

:doc:`/code/code_pass_values`