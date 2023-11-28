
classes
=======

``classes`` are a template or blueprint that represents an object. I think of ``classes`` as a a collection of :doc:`methods (functions) <functions>` and ``attributes(variables)`` that belong together

I will cover the following in this chapter

- How to define a class with pass
- How to define a class with parentheses
- How to define a class with methods
- How to define a class with attributes
- How to define a class with attributes and methods
- How to define a class with an initializer
- How to view the attributes and methods of a class



How to create a class in python
-------------------------------

* use the `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ keyword
* use ``TitleCase`` for the name
* use a descriptive name that describes the collection of :doc:`methods (functions) <functions>` and ``attributes(variables)`` - this is hard to do and is something I am still learning

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

the terminal displays a :doc:`ModuleNotFoundError` because I have an import statement for a module called ``classes``

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add :doc:`ModuleNotFoundError` to the running list of exceptions encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # ModuleNotFoundError

* I create a python module called ``classes.py`` and the terminal shows an :doc:`AttributeError` which I add to the list of exceptions encountered

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

* I change the name to an assignment to the null value :doc:`None <data_structures_none>`

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
* ``self.assertIsInstance`` is a `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`method <functions>` that checks if the first input to the :doc:`method <functions>` is an instance of the second input
* the test ``self.assertIsInstance(classes.ClassWithPass(), object)`` checks if ``ClassWithPass`` is an `object <https://docs.python.org/3/glossary.html#term-object>`_
* in python everything is an `object <https://docs.python.org/3/glossary.html#term-object>`_ , which means if it exists in python there is a class definition for it somewhere or it inherits from a class

How to define a class with parentheses
--------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

I add another test to ``TestClasses`` in ``test_classes.py`` to show another way to create a class

.. code-block:: python

  def test_classes_definitions_with_parentheses(self):
      self.assertIsInstance(classes.ClassWithParentheses(), object)

the terminal shows an :doc:`AttributeError`

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

* I can confidently say that in python

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

and the terminal displays an :doc:`AttributeError`

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



How to define a class with attributes
--------------------------------------

I will now add some tests for attributes since I know how to define a class for attributes

RED: make it fail
^^^^^^^^^^^^^^^^^


* I add a failing test to ``TestClasses`` in ``classes.py``

  .. code-block:: python

    def test_classes_with_attributes(self):
        self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)

  the terminal responds with an :doc:`AttributeError`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithAttributes(object):

        pass

  the terminal shows an :doc:`AttributeError` for a missing attribute in the newly defined class


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

* I add an attribute to ``ClassWithAttributes``

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean

  and the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

* after I change the name with an assignment to :doc:`None <data_structures_none>`

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = None

  the terminal shows an :doc:`AssertionError`

* I redefine the attribute to make the test pass

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = bool

  and the terminal shows all tests passed

RED: make it fail
^^^^^^^^^^^^^^^^^

Let us add more tests with the other python :doc:`/data_structures` to ``test_classes_with_attributes``

.. code-block:: python

  def test_classes_with_attributes(self):
      self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)
      self.assertEqual(classes.ClassWithAttributes.an_integer, int)
      self.assertEqual(classes.ClassWithAttributes.a_float, float)
      self.assertEqual(classes.ClassWithAttributes.a_string, str)
      self.assertEqual(classes.ClassWithAttributes.a_tuple, tuple)
      self.assertEqual(classes.ClassWithAttributes.a_list, list)
      self.assertEqual(classes.ClassWithAttributes.a_set, set)
      self.assertEqual(classes.ClassWithAttributes.a_dictionary, dict)

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

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

How to define a class with methods
----------------------------------

I can also define classes with :doc:`methods <functions>` which are function definitions that belong to the class

RED: make it fail
^^^^^^^^^^^^^^^^^

I add some tests for class methods to ``TestClasses`` in ``classes.py``

.. code-block:: python

  def test_classes_with_methods(self):
      self.assertEqual(
          classes.ClassWithMethods.method_a(),
          'You called MethodA'
      )

and the terminal shows :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithMethods(object):

        pass

  the terminal now gives an :doc:`AttributeError` with a different error


* When I add the missing attribute to the ``ClassWithMethods`` class

  .. code-block:: python


   class ClassWithMethods(object):

      method_a

  the terminal shows a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because there is no definition for ``method_a``


* I define ``method_a`` as an attribute by assigning the name to the null value :doc:`None <data_structures_none>`

  .. code-block:: python


    class ClassWithMethods(object):

        method_a = None

  the terminal shows a :doc:`TypeError` since ``method_a`` refers to :doc:`None <data_structures_none>` which is not callable

* I change the definition of ``method_a`` to make it a :doc:`function <functions>` which makes it callable

  .. code-block:: python


    class ClassWithMethods(object):

        def method_a():
            return None

  and the terminal shows an :doc:`AssertionError`. Progress!


* I then change the value that ``method_a`` returns to match the expectation of the test

  .. code-block:: python

    def method_a():
        return 'You called MethodA'

  and the test passes


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

* I can "make this better" by adding a few more tests to ``test_classes_with_methods`` for fun

  .. code-block:: python

    def test_classes_with_methods(self):
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

  the terminal shows an :doc:`AttributeError`

* and I change ``ClassWithMethods`` in ``classes.py`` until all tests pass

----

How to define a class with attributes and methods
-------------------------------------------------

Since I know how to define classes with methods and how to define classes with attributes, what happens when I define a class with both?

RED: make it fail
^^^^^^^^^^^^^^^^^

I add another test for a class that has both attributes and methods

.. code-block:: python

  def test_classes_with_attributes_and_methods(self):
      self.assertEqual(
          classes.ClassWithAttributesAndMethods.attribute,
          'attribute'
      )
      self.assertEqual(
          classes.ClassWithAttributesAndMethods.method(),
          'you called a method'
      )

the terminal responds with an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I change ``classes.py`` to make the tests pass by defining the class, attribute and methods

.. code-block:: python


  class ClassWithAttributesAndMethods(object):

      attribute = 'attribute'

      def method():
          return 'you called a method'

----

How to define a class with an initializer
------------------------------------------

So far I have gone over how to define classes, attributes and methods. I will now expand on this to show how to use classes.

When creating a new class, we can define an initializer which is a :doc:`method <functions>` that can receive inputs to be used to customize instances/copies of the class

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a failing test to ``test_classes.py``

.. code-block:: python

  def test_classes_with_initializers(self):
      self.assertEqual(classes.Boy().sex, 'M')

the terminal shows an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* I add a definition for the ``Boy`` class

  .. code-block:: python


    class Boy(object):

        pass

  the terminal shows another :doc:`AttributeError`

* I change the ``Boy`` class with an attribute called ``sex``

  .. code-block:: python


    class Boy(object):

        sex

  the terminal produces a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_


* I add a definition for the ``sex`` attribute

  .. code-block:: python


    class Boy(object):

        sex = 'M'

  the terminal shows passing tests


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* I add another test to ``test_classes_with_initializers`` this time for a ``Girl`` class but with a difference, I provide the value for the ``sex`` attribute when I call the class

  .. code-block:: python

    def test_classes_with_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')

  the terminal displays an :doc:`AttributeError`

* I try the same solution I used for the ``Boy`` class and add a definition for the ``Girl`` class to ``classes.py``

  .. code-block:: python


    class Girl(object):

        sex = 'M'

  and the terminal displays a :doc:`TypeError`

  .. code-block:: python

    TypeError: Girl() takes no arguments

  - ``classes.Girl(sex='F')`` looks like a call to a :doc:`function <functions>`
  - I can define classes that accept values by using an initializer
  - An initializer is a class :doc:`method <functions>` that allows customization of instances/copies of a `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_


* I add the initializer :doc:`method <functions>` called ``__init__`` to the ``Girl`` class

  .. code-block:: python


    class Girl(object):

        sex = 'F'

        def __init__(self):
            pass

  and the terminal responds with a :doc:`TypeError`

  .. code-block:: python

   TypeError: __init__() got an unexpected keyword argument 'sex'

* I change the signature of the ``__init__`` :doc:`method <functions>` to accept a keyword argument

  .. code-block:: python

    def __init__(self, sex=None):
        pass

  and the terminal shows passing tests

* I add another test for a class initializer to ``test_classes_with_initializers``

  .. code-block:: python

    def test_classes_with_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')
        self.assertEqual(classes.Other(sex='?').sex, '?')

  and the terminal displays an :doc:`AttributeError`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class Other(object):

        sex = '?'

        def __init__(self, sex=None):
            pass

  the terminal displays passing tests


* Wait a minute, I just repeated the same thing twice.

  - I defined a `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ with a name
  - I defined an attribute called ``sex``
  - I defined an ``__init__`` :doc:`method <functions>` which takes in a ``sex`` keyword argument

* I am going to make it a third repetition by redefining the ``Boy`` class to match the ``Girl`` and ``Other`` class, and because it is fun to do bad things

  .. code-block:: python


    class Boy(object):

        sex = 'M'

        def __init__(self, sex=None):
            pass

  the terminal responds with all tests still passing and I have now written the same thing 3 times. Earlier on I mentioned inheritance, and will now try to use it to remove this duplication so `I Do Not Repeat Myself <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_


* I add a new class called ``Human`` to ``classes.py`` before the definition for ``Boy`` with the same attribute and :doc:`method <functions>` of the classes I am trying to abstract

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
* I remove the ``__init__`` method, and add the `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ placeholder

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

* I remove the ``sex`` attribute and the terminal outputs an :doc:`AssertionError`
* I change the ``Human`` class to set the ``sex`` attribute in the parent initializer instead of at the child level

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            self.sex = sex

  the terminal still shows an :doc:`AssertionError`

* when I remove the ``__init__`` :doc:`method <functions>` from the ``Girl`` class

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

Why did that work?


* the ``Boy``, ``Girl`` and ``Other`` class now inherit from the ``Human`` class which means they all get the same :doc:`methods <functions>` and attributes that the ``Human`` class has, including the ``__init__`` method
* ``self.sex`` within each class refers to the ``sex`` attribute in the class, allowing its definition from within the ``__init__`` method
* since ``self.sex`` is defined as a class attribute, it is accessible from outside the class as I do in the tests i.e ``classes.Girl(sex='F').sex`` and ``classes.Other(sex='?').sex``

----

How to View the attributes and methods of a class
--------------------------------------------------

To view what ``attributes`` and ``methods`` are defined for any `object <https://docs.python.org/3/glossary.html#term-object>`_ I can call ``dir`` on the `object <https://docs.python.org/3/glossary.html#term-object>`_.

The ``dir`` :doc:`method <functions>` returns a :doc:`list <data_structures_lists>` of all attributes and :doc:`methods <functions>` of the object provided to it as input

RED: make it fail
^^^^^^^^^^^^^^^^^

I add a test to ``test_classes.py``

.. code-block:: python

  def test_view_attributes_and_methods_of_an_object(self):
    self.assertEqual(
        dir(classes.ClassWithAttributesAndMethods),
        []
    )

the terminal shows an :doc:`AssertionError` as the expected and real values do not match

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

I copy the values from the terminal to update the expectation of the test

.. code-block:: python

  def test_view_attributes_and_methods_of_an_object(self):
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

and it passes, the last two values in the list are ``attribute`` and ``method`` which I defined earlier

CONGRATULATIONS! If you made it this far and typed along with me, You know

* how to define a class with an attribute
* how to define a class with a :doc:`method <functions>`
* how to define a class with an initializer
* how to view the attributes and :doc:`methods <functions>` of a class

Do you want to `read more about classes? <https://docs.python.org/3/tutorial/classes.html#tut-firstclasses>`_
