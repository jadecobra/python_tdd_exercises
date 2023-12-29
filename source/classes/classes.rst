
########
classes
########

``classes`` are a template or blueprint that represents an object. I think of ``classes`` as a a container of :doc:`methods (functions) </functions/functions>` and ``attributes(variables)`` that belong together

I will show the following in this chapter

- How to define a class with pass
- How to define a class with parentheses
- How to define a class with methods
- How to define a class with attributes
- How to define a class with attributes and methods
- How to define a class with an initializer
- How to view the attributes and methods of a class

How to create a class in Python
-------------------------------

* use the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* use ``TitleCase`` for the name
* use a descriptive name that describes the collection of :doc:`methods (functions) </functions/functions>` and ``attributes(variables)`` - this is hard to do and is something I am still learning

How to define a class with pass
-------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I create a new file called ``test_classes.py`` in the ``tests`` directory

.. code-block:: python

  import unittest
  import classes


  class TestClasses(unittest.TestCase):

      def test_class_definitions_with_pass(self):
          self.assertIsInstance(classes.ClassWithPass(), object)

the terminal shows a :doc:`/exceptions/ModuleNotFoundError` because I have an import statement for a module called ``classes``

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add :doc:`/exceptions/ModuleNotFoundError` to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I create a python module called ``classes.py`` and the terminal shows an :doc:`/exceptions/AttributeError` which I add to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I then add the name ``ClassWithPass`` to the module

  .. code-block:: python

    ClassWithPass

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because ``ClassWithPass`` is not defined anywhere

* I add the error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* I change the name to an assignment to the null value :doc:`None </data_structures/none>`

  .. code-block:: python

    ClassWithPass = None

* and then redefine the variable as a class using the python `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword

  .. code-block:: python

    class ClassWithPass:

  the terminal shows an :doc:`IndentationError` because I declared a class without adding any indented text
* I add the new error to the list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # IndentationError

* python has the `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword to use as a placeholder for moments like this cue `Kelly Clarkson <https://youtu.be/S7b8ADhadJU?si=TxScdecOYlsxB5uW>`_

  .. code-block:: python

    class ClassWithPass:

        pass

  and the terminal shows passing tests


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Here is a quick review of what has happened so far

* `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder
* ``self.assertIsInstance`` is a `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`method </functions/functions>` that checks if the first input to the :doc:`method </functions/functions>` is an instance of the second input
* the test ``self.assertIsInstance(classes.ClassWithPass(), object)`` checks if ``ClassWithPass`` is an `object <https://docs.python.org/3/glossary.html#term-object>`_
* in Python everything is an `object <https://docs.python.org/3/glossary.html#term-object>`_ , which means if it exists in Python there is a class definition for it somewhere or it inherits from a class

How to define a class with parentheses
--------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add another test to ``TestClasses`` in ``test_classes.py`` to show another way to create a class

.. code-block:: python

  def test_classes_definitions_with_parentheses(self):
      self.assertIsInstance(classes.ClassWithParentheses(), object)

the terminal shows an :doc:`/exceptions/AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a class definition like ``ClassWithPass`` to ``classes.py``

  .. code-block:: python


    class ClassWithParentheses:

        pass

  the terminal shows passing tests

* When I change the definition to include parentheses

  .. code-block:: python


    class ClassWithParentheses():

        pass

  the terminal shows all tests are still passing.

* I can confidently say that in Python

  - I can define ``classes`` with parentheses
  - I can define ``classes`` without parentheses
  - `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder

How to define a class with inheritance
--------------------------------------

In object oriented programming there is a concept called `Inheritance <https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming>`_\ ). With Inheritance I can define new `objects <https://docs.python.org/3/glossary.html#term-object>`_ that inherit from existing `objects <https://docs.python.org/3/glossary.html#term-object>`_.

This makes creating new objects easier because I do not have to reinvent or rewrite things that already exist, I can inherit them instead and change the new objects for my specific use case

To use inheritance I specify the "parent" in parentheses when I define the new object (the child) to establish the relationship

RED: make it fail
^^^^^^^^^^^^^^^^^

I will add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

  def test_class_definition_with_object(self):
      self.assertIsInstance(classes.ClassWithObject(), object)

and the terminal shows an :doc:`/exceptions/AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithObject():

        pass

  the terminal shows all tests passed

* then I change the definition to explicitly state the parent `object <https://docs.python.org/3/glossary.html#term-object>`_

  .. code-block:: python


    class ClassWithObject(object):

        pass

  and the terminal still shows passing tests


Here is a little summary

* classes can be defined

  - with parentheses stating what `object <https://docs.python.org/3/glossary.html#term-object>`_ the class inherits from
  - with parentheses without stating what `object <https://docs.python.org/3/glossary.html#term-object>`_ the class inherits from
  - without parentheses
  - `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder

* classes by default inherit from the `object <https://docs.python.org/3/glossary.html#term-object>`_  class, because in each of the tests, whether the parent is stated or not, each class I defined is an ``instance`` of an `object <https://docs.python.org/3/glossary.html#term-object>`_

.. admonition:: Zen of Python


  I prefer to use the explicit form of class definitions with the parent `object <https://docs.python.org/3/glossary.html#term-object>`_ in parentheses, from `the zen of python <https://peps.python.org/pep-0020/>`_
  ``Explicit is better than implicit``
