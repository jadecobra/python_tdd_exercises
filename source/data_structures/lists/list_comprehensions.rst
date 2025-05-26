.. include:: ../../links.rst

#################################################################################
lists: list comprehensions
#################################################################################

.. raw:: html

    <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/8v6fF6gHmE4?si=e2-lry14UZDgU6Qo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

.. contents:: table of contents
  :local:
  :depth: 1

----

`List Comprehensions <https://docs.python.org/3/tutorial/datastructures.html?highlight=list#list-comprehensions>`_ are a simple to make a :ref:`list <lists>` from an iterable_, by going over every item and performing operations with one line

*********************************************************************************
requirements
*********************************************************************************

* I open a terminal to run :ref:`makePythonTdd.sh` with ``list_comprehensions`` as the name of the project

  .. code-block:: python

    ./makePythonTdd.sh list_comprehensions

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1`

    .. code-block:: python

      ./makePythonTdd.ps1 list_comprehensions

  it makes the folders and files that are needed, installs packages, runs the first test, and the terminal shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_list_comprehensions.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_list_comprehensions.py:7`` to open it in the editor
* then change ``True`` to ``False`` to make the test pass

----

*********************************************************************************
test_make_a_list_w_a_for_loop
*********************************************************************************

red: make it fail
#################################################################################

I change ``test_failure`` to ``test_make_a_list_w_a_for_loop``

.. code-block:: python

  import unittest


  class TestListComprehensions(unittest.TestCase):

    def test_make_a_list_w_a_for_loop(self):
        a_list = []
        iterable = range(4)

        for item in iterable:
            a_list.append(item)

        self.assertEqual(a_list, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3] != []

green: make it pass
#################################################################################

I copy the value from the terminal and use it as the expectation

.. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])

the test passes, the list is no longer empty after calling the append_ :ref:`method<functions>` in the `for loop`_ which goes over every item in the iterable_

refactor: make it better
#################################################################################

* I add another assert_ statement

  .. code-block:: python

    self.assertEqual(a_list, [0, 1, 2, 3])
    self.assertEqual(
        src.list_comprehensions.for_loop(iterable),
        a_list
    )

  the terminal shows NameError_

  .. code-block:: python

    NameError: name 'src' is not defined

* I add it to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError

  then I add an `import statement`_

  .. code-block:: python

    import src.list_comprehensions
    import unittest

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'for_loop'

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError

* I add a :ref:`function<functions>` definition to ``list_comprehensions.py``

  .. code-block:: python

    def for_loop():
        return None

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: for_loop() takes 0 positional arguments but 1 was given

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

  then I change the signature of the :ref:`function<functions>` to take input

  .. code-block:: python

    def for_loop(argument):
        return None

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: None != [0, 1, 2, 3]

  I add a `for loop`_ to the :ref:`function<functions>`

  .. code-block:: python

    def for_loop(argument):
        result = []
        for item in argument:
            result.append(item)
        return result

  the test passes

  - ``result = []`` makes an empty :ref:`list<lists>`
  - ``for item in argument:`` loops over the items of ``argument``
  - ``result.append(item)`` adds each item from ``argument`` to ``result``
  - ``return result`` returns ``result`` after the loop completes

* I change the input name from ``argument`` to ``iterable`` to make it clearer

  .. code-block:: python

    def for_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

  all tests are still passing

I can make a :ref:`list <lists>` from an iterable_ by using a `for loop`_ or the :ref:`list <lists>` constructor

----

****************************************************************************************
test_make_a_list_w_list_comprehensions
****************************************************************************************

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_make_a_list_w_list_comprehensions(self):
      iterable = range(4)

      self.assertEqual(
          src.list_comprehensions.for_loop(iterable),
          []
      )

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 1, 2, 3] != []

green: make it pass
#################################################################################

I make the values in the test match the terminal

.. code-block:: python

      self.assertEqual(
          src.list_comprehensions.for_loop(iterable),
          [0, 1, 2, 3]
      )

the test passes

refactor: make it better
#################################################################################

I change the expectation to use a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

.. code-block:: python

  self.assertEqual(
      src.list_comprehensions.for_loop(iterable),
      # [0, 1, 2, 3]
      [item for item in iterable]
  )

the terminal still shows green. I remove the comment then add another assert_ statement

.. code-block:: python

  self.assertEqual(
      src.list_comprehensions.list_comprehension(iterable),
      src.list_comprehensions.for_loop(iterable)
  )

the terminal shows :ref:`AttributeError`

.. code-block:: python

  AttributeError: module 'src.list_comprehensions' has no attribute 'list_comprehension'

I add a :ref:`function<functions>` that uses a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to `list_comprehensions.py`

  .. code-block:: python

    def list_comprehension(iterable):
        return [item for item in iterable]

the test is green again. I made 2 :ref:`functions<functions>`, one that uses a `for loop`_ and another that uses a `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ to do the same thing difference between

.. code-block:: python

    a_list = []
    for item in iterable:
        a_list.append()

and

.. code-block:: python

    [item for item in iterable]

the difference between them is that in the first case I have to

* make a :ref:`list<lists>`
* loop through the iterable_
* do the operation I want on the item of the iterable_

With the list comprehension I can get the same result in one line that covers all those steps

----

****************************************************************************************
test_make_a_list_w_list_comprehensions
****************************************************************************************

There is more I can do with `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_, I can add conditions when I perform an operation

red: make it fail
#################################################################################

I add a failing test

.. code-block:: python

  def test_list_comprehensions_w_conditions_i(self):
      iterable = range(10)
      even_numbers = []

      for item in iterable:
          if item % 2 == 0:
              even_numbers.append(item)

      self.assertEqual(even_numbers, [])

the terminal shows :ref:`AssertionError`

.. code-block:: python

  AssertionError: Lists differ: [0, 2, 4, 6, 8] != []

* ``if item % 2 == 0:`` checks if the item in ``iterable`` leaves a remainder of ``0`` when divided by ``2``
* ``%`` is the modulo_ operator, it divides the number on the left by the number on the right and returns a remainder

green: make it pass
#################################################################################

I copy the values from the terminal and paste in the test

.. code-block:: python

  self.assertEqual(even_numbers, [0, 2, 4, 6, 8])

the test passes

refactor: make it better
#################################################################################

* I add another assert_ statement

  .. code-block:: python

    self.assertEqual(even_numbers, [0, 2, 4, 6, 8])
    self.assertEqual(
        [item for item in iterable],
        even_numbers
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [0, 2, 4, 6, 8]

  the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_ is missing the condition, I add it

  .. code-block:: python

    self.assertEqual(
        [item for item in iterable if item % 2 == 0],
        even_numbers
    )

  the test passes

* I add another assert_ statement

  .. code-block:: python

    self.assertEqual(
        [item for item in iterable if item % 2 == 0],
        even_numbers
    )
    self.assertEqual(
        src.list_comprehensions.get_even_numbers(iterable),
        even_numbers
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_even_numbers'

  I add a :ref:`function<functions>` to ``list_comprehensions.py``

  .. code-block:: python

    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]

  the test passes

* I add another test

  .. code-block:: python

    def test_list_comprehensions_w_conditions_ii(self):
        iterable = range(10)
        odd_numbers = []

        for item in iterable:
            if item % 2 != 0:
                odd_numbers.append(item)

        self.assertEqual(odd_numbers, [])

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [1, 3, 5, 7, 9] != []

  I change the expectation to match

  .. code-block:: python

    self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])

  the test passes

* I add another assert_ statement

  .. code-block:: python

    self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])
    self.assertEqual(
        [item for item in iterable],
        odd_numbers
    )

  the terminal shows :ref:`AssertionError`

  .. code-block:: python

    AssertionError: Lists differ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] != [1, 3, 5, 7, 9]

  I add the condition to the `list comprehension <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

  .. code-block:: python

    self.assertEqual(
        [item for item in iterable if item % 2 != 0],
        odd_numbers
    )

  the test passes

* I add another assert_ statement

  .. code-block:: python

    self.assertEqual(
        [item for item in iterable if item % 2 != 0],
        odd_numbers
    )
    self.assertEqual(
        src.list_comprehensions.get_odd_numbers(iterable),
        odd_numbers
    )

  the terminal shows :ref:`AttributeError`

  .. code-block:: python

    AttributeError: module 'src.list_comprehensions' has no attribute 'get_odd_numbers'. Did you mean: 'get_even_numbers'?

  I add the :ref:`function`

  .. code-block:: python

    def get_even_numbers(iterable):
        return [item for item in iterable if item % 2 == 0]


    def get_odd_numbers(iterable):
        return [item for item in iterable if item % 2 != 0]

----

*********************************************************************************
review
*********************************************************************************

From the tests I can make a :ref:`list<lists>` from an iterable_ by using

* a `for loop`_ loop
* the :ref:`list <lists>` constructor_
* `list comprehensions <https://docs.python.org/3/glossary.html#term-list-comprehension>`_

I also ran into the following Exceptions_

* :ref:`AssertionError`
* NameError_
* :ref:`ModuleNotFoundError`
* :ref:`AttributeError`
* :ref:`TypeError`

Would you like to test :ref:`dictionaries`?

----

:doc:`/code/code_list_comprehensions`