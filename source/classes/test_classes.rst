.. include:: ../links.rst

.. _test_classes:

#################################################################################
classes: test_classes
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

``classes`` are things that represent an object. I think of ``classes`` as a a container of :doc:`methods (functions) </functions/functions>` and ``attributes (variables)`` that belong together

*********************************************************************************
how to make a class in Python
*********************************************************************************

* use the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* use ``TitleCase`` for the name
* use a descriptive name that describes the collection of :doc:`methods (functions) </functions/functions>` and ``attributes (variables)`` - this is hard to do and is something I am still learning

----
.. _test_defining_classes_w_pass

*********************************************************************************
test_defining_classes_w_pass
*********************************************************************************

red: make it fail
#################################################################################

I make a new file called ``test_classes.py`` in the ``tests`` directory

.. code-block:: python

  import unittest
  import classes


  class TestClasses(unittest.TestCase):

      def test_defining_classes_w_pass(self):
          self.assertIsInstance(classes.ClassWithPass(), object)

the terminal shows a :ref:`ModuleNotFoundError` because I have an import statement for a module called ``classes``

green: make it pass
#################################################################################

* I add :ref:`ModuleNotFoundError` to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I make a python module called ``classes.py`` and the terminal shows an :ref:`AttributeError` which I add to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I then add the name ``ClassWithPass`` to the module

  .. code-block:: python

    ClassWithPass

  and the terminal shows a NameError_ because ``ClassWithPass`` is not defined anywhere

* I add the error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* I make the name to an assignment to the null value :ref:`None`

  .. code-block:: python

    ClassWithPass = None

* and then redefine the variable as a class using the python `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword

  .. code-block:: python

    class ClassWithPass:

  the terminal shows an :ref:`IndentationError` because I declared a class without adding any indented text
* I add the new error to the list of :doc:`Exceptions</how_to/exception_handling_programs>` encountered

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


refactor: make it better
#################################################################################

Here is a quick review of what has happened so far

* `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder
* ``self.assertIsInstance`` is a `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :ref:`method<functions>` that checks if the first input to the :ref:`method<functions>` is an instance of the second input
* the test ``self.assertIsInstance(classes.ClassWithPass(), object)`` checks if ``ClassWithPass`` is an `object <https://docs.python.org/3/glossary.html#term-object>`_
* in Python everything is an `object <https://docs.python.org/3/glossary.html#term-object>`_ , which means if it exists in Python there is a class definition for it somewhere or it inherits from a class

----

.. _test_defining_classes_w_parentheses:

*********************************************************************************
test_defining_classes_w_parentheses
*********************************************************************************

red: make it fail
#################################################################################

I add another test to ``TestClasses`` in ``test_classes.py`` to show another way to make a class

.. code-block:: python

  def test_defining_classes_w_parentheses(self):
      self.assertIsInstance(classes.ClassWithParentheses(), object)

the terminal shows an :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a class definition like ``ClassWithPass`` to ``classes.py``

  .. code-block:: python


    class ClassWithParentheses:

        pass

  the terminal shows passing tests

* When I make the definition include parentheses

  .. code-block:: python


    class ClassWithParentheses():

        pass

  the terminal shows all tests are still passing.

* I can confidently say that in Python

  - I can define ``classes`` with parentheses
  - I can define ``classes`` without parentheses
  - `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder

----

.. _test_defining_classes_w_object:

*********************************************************************************
test_defining_classes_w_object
*********************************************************************************

In object oriented programming there is a concept called `Inheritance <https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming>`_\ ). With Inheritance I can define new `objects <https://docs.python.org/3/glossary.html#term-object>`_ that inherit from existing `objects <https://docs.python.org/3/glossary.html#term-object>`_.

Making new objects is easier because I do not have to reinvent or rewrite things that already exist, I can inherit them instead and change the new objects for my specific use case

To use inheritance I specify the "parent" in parentheses when I define the new object (the child) to establish the relationship

red: make it fail
#################################################################################

I add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

  def test_defining_classes_w_object(self):
      self.assertIsInstance(classes.ClassWithObject(), object)

and the terminal shows an :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithObject():

        pass

  the terminal shows all tests passed

* then I make the definition to explicitly state the parent `object <https://docs.python.org/3/glossary.html#term-object>`_

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

* classes by default inherit from the `object <https://docs.python.org/3/glossary.html#term-object>`_ class, because in each of the tests, whether the parent is stated or not, each class I defined is an ``instance`` of an `object <https://docs.python.org/3/glossary.html#term-object>`_

.. admonition:: Zen of Python (:PEP:`20`)


  I prefer to use the explicit form of class definitions with the parent `object <https://docs.python.org/3/glossary.html#term-object>`_ in parentheses, from the zen of python:
  ``Explicit is better than implicit``

Would you like to :doc:`test_classes_attributes_methods`?

----

:doc:`/code/code_classes`