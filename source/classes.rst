.. include:: links.rst

#################################################################################
classes
#################################################################################

``classes`` are definitions that represent an object. I think of them as :ref:`attributes<AttributeError>` and :ref:`methods (functions) <functions>` that belong together

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`how to make a person`

*********************************************************************************
how to make a class in Python
*********************************************************************************

* use the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* use ``TitleCase`` for the name
* use a name that tells what the collection of :ref:`attributes<AttributeError>` and :ref:`methods (functions) <functions>` does - this is hard to do and is something I am still learning

----

*********************************************************************************
test_make_a_class_w_pass
*********************************************************************************

red: make it fail
#################################################################################

I make a new file called ``test_classes.py`` in the ``tests`` directory

.. code-block:: python

  import unittest
  import classes


  class TestClasses(unittest.TestCase):

      def test_make_a_class_w_pass(self):
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
* in Python everything is an :ref:`object<classes>` , which means if it is in Python there is a class definition for it somewhere or it inherits from a class

----


*********************************************************************************
test_make_a_class_w_parentheses
*********************************************************************************

red: make it fail
#################################################################################

I add another test to ``TestClasses`` in ``test_classes.py`` to show another way to make a class

.. code-block:: python

  def test_make_a_class_w_parentheses(self):
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
test_make_a_class_w_object
*********************************************************************************

In object oriented programming there is a concept called `Inheritance <https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming>`_\ ). With Inheritance I can define new objects_ that inherit from existing objects_.

Making new objects is easier because I do not have to reinvent or rewrite things that already exist, I can inherit them instead and change the new objects for my specific use case

To use inheritance I specify the "parent" in parentheses when I define the new object (the child) to make the relationship

red: make it fail
#################################################################################

I add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

  def test_make_a_class_w_object(self):
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

*********************************************************************************
test_make_a_class_w_attributes
*********************************************************************************

I now add some tests for attributes since I know how to define a class for attributes

red: make it fail
#################################################################################


* I add a failing test to ``TestClasses`` in ``classes.py``

  .. code-block:: python

    def test_make_a_class_w_attributes(self):
        self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)

  the terminal shows :ref:`AttributeError`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithAttributes(object):

        pass

  the terminal shows :ref:`AttributeError` for a missing attribute in the newly defined class

green: make it pass
#################################################################################

* I add an attribute to ``ClassWithAttributes``

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean

  and the terminal shows a ` <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

* after I point the name to :ref:`None`

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = None

  the terminal shows :ref:`AssertionError`

* I redefine the attribute to make the test pass

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = bool

  and the terminal shows all tests passed

refactor: make it better
#################################################################################

red: make it fail
---------------------------------------------------------------------------------

Let us add more tests with the other Python data structures to ``test_make_a_class_w_attributes``

.. code-block:: python

  def test_make_a_class_w_attributes(self):
      self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)
      self.assertEqual(classes.ClassWithAttributes.an_integer, int)
      self.assertEqual(classes.ClassWithAttributes.a_float, float)
      self.assertEqual(classes.ClassWithAttributes.a_string, str)
      self.assertEqual(classes.ClassWithAttributes.a_tuple, tuple)
      self.assertEqual(classes.ClassWithAttributes.a_list, list)
      self.assertEqual(classes.ClassWithAttributes.a_set, set)
      self.assertEqual(classes.ClassWithAttributes.a_dictionary, dict)

the terminal shows :ref:`AttributeError`

green: make it pass
---------------------------------------------------------------------------------

I add matching attributes to ``ClassWithAttributes`` to make the tests pass

.. code-block:: python


  class ClassWithAttributes(object):

      a_boolean = bool
      an_integer = int
      a_float = float
      a_string = str
      a_tuple = tuple
      a_list = list
      a_set = set
      a_dictionary = dict

and the terminal shows all tests pass

----


*********************************************************************************
test_make_a_class_w_methods
*********************************************************************************

I can also define classes with :ref:`methods<functions>` which are :ref:`function<functions>` definitions that belong to the class

red: make it fail
#################################################################################

I add some tests for class methods to ``TestClasses`` in ``classes.py``

.. code-block:: python

  def test_make_a_class_w_methods(self):
      self.assertEqual(
          classes.ClassWithMethods.method_a(),
          'You called MethodA'
      )

and the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithMethods(object):

        pass

  the terminal now gives :ref:`AttributeError` with a different error


* When I add the missing attribute to the ``ClassWithMethods`` class

  .. code-block:: python


    class ClassWithMethods(object):

        method_a

  the terminal shows NameError_ because there is no definition for ``method_a``


* I define ``method_a`` as an attribute by pointing it to :ref:`None`

  .. code-block:: python


    class ClassWithMethods(object):

        method_a = None

  the terminal shows :ref:`TypeError` since ``method_a`` is :ref:`None` which is not callable

* I change the definition of ``method_a`` to make it a :ref:`function<functions>` which makes it callable

  .. code-block:: python


    class ClassWithMethods(object):

        def method_a():
            return None

  and the terminal shows :ref:`AssertionError`. Progress!

* I then change the value that ``method_a`` returns to match the expectation of the test

  .. code-block:: python

    def method_a():
        return 'You called MethodA'

  and the test passes

refactor: make it better
#################################################################################

* I can "make this better" by adding a few more tests to ``test_make_a_class_w_methods`` for fun

  .. code-block:: python

    def test_make_a_class_w_methods(self):
        self.assertEqual(
            classes.ClassWithMethods.method_a(),
            'You called MethodA'
        )
        self.assertEqual(
            classes.ClassWithMethods.method_b(),
            'You called MethodB'
        )
        self.assertEqual(
            classes.ClassWithMethods.method_c(),
            'You called MethodC'
        )
        self.assertEqual(
            classes.ClassWithMethods.method_d(),
            'You called MethodD'
        )

  the terminal shows :ref:`AttributeError`

* and I change each assertion to the right value until they all pass

----


*********************************************************************************
test_make_a_class_w_attributes_and_methods
*********************************************************************************

Since I know how to define classes with methods and how to define classes with attributes, what happens when I define a class with both?

red: make it fail
#################################################################################

I add another test for a class that has both attributes and methods

.. code-block:: python

  def test_make_a_class_w_attributes_and_methods(self):
      self.assertEqual(
          classes.ClassWithAttributesAndMethods.attribute,
          'attribute'
      )
      self.assertEqual(
          classes.ClassWithAttributesAndMethods.method(),
          'you called a method'
      )

the terminal shows :ref:`AttributeError`

green: make it pass
#################################################################################

I make ``classes.py`` to make the tests pass by defining the class, attribute and methods

.. code-block:: python


  class ClassWithAttributesAndMethods(object):

      attribute = 'attribute'

      def method():
          return 'you called a method'

----


*********************************************************************************
test_attributes_and_methods_of_objects
*********************************************************************************

To view what :ref:`attributes<AttributeError>` and ``methods`` are defined for any :ref:`object<classes>` I can call ``dir`` on the :ref:`object<classes>`.

The ``dir`` :ref:`method<functions>` returns a :ref:`list <lists>` of all :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the object provided to it as input

red: make it fail
#################################################################################

I add a test to ``test_classes.py``

.. code-block:: python

  def test_attributes_and_methods_of_objects(self):
    self.assertEqual(
        dir(classes.ClassWithAttributesAndMethods),
        []
    )

the terminal shows :ref:`AssertionError` as the expected and real values do not match

green: make it pass
#################################################################################

I copy the values from the terminal to change the expectation of the test

.. code-block:: python

  def test_attributes_and_methods_of_objects(self):
      self.assertEqual(
          dir(classes.ClassWithAttributesAndMethods),
          [
              '__class__',
              '__delattr__',
              '__dict__',
              '__dir__',
              '__doc__',
              '__eq__',
              '__format__',
              '__ge__',
              '__getattribute__',
              '__gt__',
              '__hash__',
              '__init__',
              '__init_subclass__',
              '__le__',
              '__lt__',
              '__module__',
              '__ne__',
              '__new__',
              '__reduce__',
              '__reduce_ex__',
              '__repr__',
              '__setattr__',
              '__sizeof__',
              '__str__',
              '__subclasshook__',
              '__weakref__',
              'attribute',
              'method',
          ]
      )

and it passes, the last 2 values in the list are ``attribute`` and ``method`` which I defined earlier

----

*********************************************************************************
test_make_a_class_w_initializer
*********************************************************************************

When making a new class, we can define an initializer which is a :ref:`method<functions>` that can receive inputs to be used to customize instances/copies of the class

*********************************************************************************
red: make it fail
*********************************************************************************

I add a failing test to ``test_classes.py``

.. code-block:: python

  def test_make_a_class_w_initializers(self):
      self.assertEqual(classes.Boy().sex, 'M')

the terminal shows :ref:`AttributeError`

*********************************************************************************
green: make it pass
*********************************************************************************

* I add a definition for the ``Boy`` class

  .. code-block:: python


    class Boy(object):

        pass

  the terminal shows another :ref:`AttributeError`

* I make the ``Boy`` class with an attribute called ``sex``

  .. code-block:: python


    class Boy(object):

        sex

  the terminal produces NameError_


* I add a definition for the ``sex`` attribute

  .. code-block:: python


    class Boy(object):

        sex = 'M'

  the terminal shows passing tests

*********************************************************************************
refactor: make it better
*********************************************************************************

* I add another assertion to ``test_make_a_class_w_initializers`` this time for a ``Girl`` class but with a difference, I provide the value for the ``sex`` attribute when I call the class

  .. code-block:: python

    def test_make_a_class_w_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')

  the terminal shows :ref:`AttributeError`

* I try the same solution I used for the ``Boy`` class then add a definition for the ``Girl`` class to ``classes.py``

  .. code-block:: python


    class Girl(object):

        sex = 'M'

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: Girl() takes no arguments

  - ``classes.Girl(sex='F')`` looks like a call to a :ref:`function<functions>`
  - I can define classes that take values by using an initializer
  - An initializer is a class :ref:`method<functions>` that allows customization of instances/copies of a `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

* I add the initializer :ref:`method<functions>` called ``__init__`` to the ``Girl`` class

  .. code-block:: python


    class Girl(object):

        sex = 'F'

        def __init__(self):
            pass

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

   TypeError: __init__() got an unexpected keyword argument 'sex'

* I make the signature of the ``__init__`` :ref:`method<functions>` take a keyword argument

  .. code-block:: python

    def __init__(self, sex=None):
        pass

  and the terminal shows passing tests

* I add another assertion

  .. code-block:: python

    def test_make_a_class_w_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')
        self.assertEqual(classes.Other(sex='?').sex, '?')

  and the terminal shows :ref:`AttributeError`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class Other(object):

        sex = '?'

        def __init__(self, sex=None):
            pass

  the terminal shows passing tests

* Wait a minute, I just repeated the same thing twice.

  - I defined a `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ with a name
  - I defined an attribute called ``sex``
  - I defined an ``__init__`` :ref:`method<functions>` which takes in a ``sex`` keyword argument

* I am going to make it a third repetition by redefining the ``Boy`` class to match the ``Girl`` and ``Other`` class because it is fun to do bad things

  .. code-block:: python


    class Boy(object):

        sex = 'M'

        def __init__(self, sex=None):
            pass

  the terminal shows all tests still passing and I have now written the same thing 3 times. Earlier on I mentioned inheritance, and will now try to use it to remove this duplication so `I do not repeat myself`_

* I add a new class called ``Human`` to ``classes.py`` before the definition for ``Boy`` with the same attribute and :ref:`method<functions>` of the classes I am trying to abstract

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            pass

  the terminal still shows passing tests

* I change the definitions for ``Boy`` to inherit from the ``Human`` class and all tests are still passing

  .. code-block:: python


    class Boy(Human):

        sex = 'M'

        def __init__(self, sex=None):
            pass

* I remove the ``sex`` attribute from the ``Boy`` class and the tests continue to pass
* I remove the ``__init__`` method, then add the `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ placeholder

  .. code-block:: python


    class Boy(Human):

        pass

  all tests are still passing. Lovely

* What if I try the same thing with the ``Girl`` class and change its definition to inherit from the ``Human`` class?

  .. code-block:: python

    class Girl(Human):

        sex = 'F'

        def __init__(self):
            pass

* I remove the ``sex`` attribute and the terminal shows :ref:`AssertionError`
* I make the ``Human`` class to set the ``sex`` attribute in the parent initializer instead of at the child level

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            self.sex = sex

  the terminal still shows :ref:`AssertionError`

* when I remove the ``__init__`` :ref:`method<functions>` from the ``Girl`` class

  .. code-block:: python


    class Girl(Human):

        pass

  the terminal shows passing tests. Lovely

* I wonder if I can do the same with the ``Other`` class? I change the definition to inherit from the ``Human`` class

  .. code-block:: python


    class Other(Human):

        pass

  the terminal shows passing tests

* One More Thing! I remove the ``sex`` attribute from the ``Human`` class

  .. code-block:: python

    class Human(object):

      def __init__(self, sex='M'):
          self.sex = sex

  all tests are passing, I have successfully refactored the 3 classes and abstracted a ``Human`` class from them

* the ``Boy``, ``Girl`` and ``Other`` class now inherit from the ``Human`` class which means they all get the same :ref:`methods<functions>` and attributes that the ``Human`` class has, including the ``__init__`` method
* ``self.sex`` in each class is the ``sex`` attribute in the class, allowing its definition from inside the ``__init__`` method
* since ``self.sex`` is defined as a class attribute, it is accessible from outside the class as I do in the tests i.e ``classes.Girl(sex='F').sex`` and ``classes.Other(sex='?').sex``

----

*********************************************************************************
review
*********************************************************************************

the tests show

* how to define a class with an attribute
* how to define a class with a :ref:`method<functions>`
* how to define a class with an initializer
* how to view the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of a class
* classes can be defined

  - with parentheses stating what :ref:`object<classes>` the class inherits from
  - with parentheses without stating what :ref:`object<classes>` the class inherits from
  - without parentheses
  - `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ is a placeholder

* classes by default inherit from the :ref:`object<classes>` class, because in each of the tests, whether the parent is stated or not, each class I defined is an ``instance`` of an :ref:`object<classes>`

.. admonition:: Zen of Python (:PEP:`20`)


  I prefer to use the explicit form of class definitions with the parent :ref:`object<classes>` in parentheses, from the `Zen of Python`:
  ``Explicit is better than implicit``


----

:doc:`/code/code_classes`