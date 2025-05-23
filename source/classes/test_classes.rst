.. include:: ../links.rst


#################################################################################
classes: test_classes
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
how to make a class in Python
*********************************************************************************

* use the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* use ``TitleCase`` for the name
* use a name that tells what the collection of :ref:`attributes<AttributeError>` and :ref:`methods (functions) <functions>` does - this is hard to do and is something I am still learning

----

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

the terminal shows :ref:`ModuleNotFoundError` because I have an import statement for a module called ``classes``

green: make it pass
#################################################################################

* I add :ref:`ModuleNotFoundError` to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I make Python module called ``classes.py`` and the terminal shows :ref:`AttributeError` which I add to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError

* I then add the name ``ClassWithPass`` to the module

  .. code-block:: python

    ClassWithPass

  and the terminal shows NameError_ because ``ClassWithPass`` is not defined anywhere

* I add the error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError

* I point the name to :ref:`None`

  .. code-block:: python

    ClassWithPass = None

* and then redefine the variable as a class using thePython `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword

  .. code-block:: python

    class ClassWithPass:

  the terminal shows IndentationError_ because I declared a class without adding any indented text
* I add the new error to the list of Exceptions_ encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # IndentationError

* Python has the `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword to use as a placeholder for moments like this cue `Kelly Clarkson <https://youtu.be/S7b8ADhadJU?si=TxScdecOYlsxB5uW>`_

  .. code-block:: python

    class ClassWithPass:

        pass

  and the terminal shows passing tests


refactor: make it better
#################################################################################

Here is a quick review of what has happened so far

* `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder
* ``self.assertIsInstance`` is a `unittest.TestCase`_ :ref:`method<functions>` that checks if the first input to the :ref:`method<functions>` is an instance of the second input
* the test ``self.assertIsInstance(classes.ClassWithPass(), object)`` checks if ``ClassWithPass`` is an :ref:`object<classes>`
* in Python everything is an :ref:`object<classes>` , which means if it exists in Python there is a class definition for it somewhere or it inherits from a class

----


*********************************************************************************
test_defining_classes_w_parentheses
*********************************************************************************

red: make it fail
#################################################################################

I add another test to ``TestClasses`` in ``test_classes.py`` to show another way to make a class

.. code-block:: python

  def test_defining_classes_w_parentheses(self):
      self.assertIsInstance(classes.ClassWithParentheses(), object)

the terminal shows :ref:`AttributeError`

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


*********************************************************************************
test_defining_classes_w_object
*********************************************************************************

In object oriented programming there is a concept called `Inheritance <https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming>`_\ ). With Inheritance I can define new objects_ that inherit from existing objects_.

Making new objects is easier because I do not have to reinvent or rewrite things that already exist, I can inherit them instead and change the new objects for my specific use case

To use inheritance I specify the "parent" in parentheses when I define the new object (the child) to make the relationship

red: make it fail
#################################################################################

I add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

  def test_defining_classes_w_object(self):
      self.assertIsInstance(classes.ClassWithObject(), object)

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithObject():

        pass

  the terminal shows all tests passed

* then I change the definition to explicitly state the parent :ref:`object<classes>`

  .. code-block:: python


    class ClassWithObject(object):

        pass

  and the terminal still shows passing tests


Here is a little summary

* classes can be defined

  - with parentheses stating what :ref:`object<classes>` the class inherits from
  - with parentheses without stating what :ref:`object<classes>` the class inherits from
  - without parentheses
  - `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder

* classes by default inherit from the :ref:`object<classes>` class, because in each of the tests, whether the parent is stated or not, each class I defined is an ``instance`` of an :ref:`object<classes>`

.. admonition:: Zen of Python (:PEP:`20`)


  I prefer to use the explicit form of class definitions with the parent :ref:`object<classes>` in parentheses, from the `Zen of Python`:
  ``Explicit is better than implicit``

Would you like to :doc:`test_classes_attributes_methods`?

----

:doc:`/code/code_classes`