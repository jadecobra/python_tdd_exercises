classes
=======

We will step through writing classes in python using Test Driven Development

``classes`` are a template or blueprint that represent an object. They are a collection of ``methods(functions)`` and ``attributes(variables)`` that belong together

Prerequisites
-------------


:doc:`How to Setup a Test Driven Development Environment`

----


How to define a Class with pass
------------------------


* use the ``class`` keyword
* use ``TitleCase`` for naming
* use Descriptive names

RED: make it fail
^^^^^^^^^^^^^^^^^

we create a new file called ``test_classes.py`` in the ``tests`` directory

.. code-block:: python

   import unittest
   import classes


   class TestClasses(unittest.TestCase):

       def test_class_definitions_with_pass(self):
           self.assertIsInstance(classes.ClassWithPass(), object)

the terminal displays a :doc:`ModuleNotFoundError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* create a python module called ``classes.py`` and the terminal updates to show an :doc:`AttributeError`
* add the name ``ClassWithPass`` to the module

  .. code-block:: python

    ClassWithPass

  and the terminal updates to show a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because ``ClassWithPass`` is not defined anywhere

* update the name as an assignment to the null value :doc:`None </data structures: None>`

  .. code-block:: python

    ClassWithPass = None

* redefine the variable as a class using the ``class`` keyword

.. code-block:: python

   class ClassWithPass:

  the terminal updates to show an :doc:`IndentationError`

* add the ``pass`` keyword as a placeholder to the definition

.. code-block:: python

   class ClassWithPass:

       pass

  and the terminal updates to show passing tests


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Let us review what we have written so far


* ``pass`` is a placeholder
* ``self.assertIsInstance`` is a `unittest.TestCase <https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase>`_ :doc:`method <functions>` that checks if the first input to the :doc:`method <functions>` is an instance of the second input
* in python everything is an ``object`` which means there's a class definition for it, our test ``self.assertIsInstance(classes.ClassWithPass(), object)`` checks if ``ClassWithPass`` is an ``object``

How to define a Class with parentheses
--------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^

add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

       def test_classes_definitions_with_parentheses(self):
           self.assertIsInstance(classes.ClassWithParentheses(), object)

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``classes.py`` with a class definition

  .. code-block:: python


     class ClassWithParentheses:

         pass

  the terminal updates to show passing tests

* update the definition to include parentheses

    .. code-block:: python


    class ClassWithParentheses():

        pass

  the terminal shows all tests are still passing.


* We now know that we can define ``classes``

  - with parentheses
  - without parentheses
  - ``pass`` is a placeholder

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

In object oriented programming there is a concept called `Inheritance <https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming>`_\ ). With Inheritance we can define new ``objects`` that inherit from other existing ``objects``. This makes creating things easier because we do not have to reinvent or rewrite things that already exist, we can inherit them instead.

How to define a Class with inheritance
-------------------------------

To use inheritance we specify the "parent" in parentheses when we define the new object (the child) to establish the relationship

RED: make it fail
^^^^^^^^^^^^^^^^^

we add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

       def test_class_definition_with_object(self):
           self.assertIsInstance(classes.ClassWithObject(), object)

and the terminal displays an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a class definition to ``classes.py``

  .. code-block:: python


  class ClassWithObject():

      pass

  the terminal displays passing tests


* update the definition to explicitly state the parent ``object``

  .. code-block:: python


     class ClassWithObject(object):

         pass

  and the terminal still shows passing tests


We now know that in python


* classes can be defined

  - with parentheses explicitly stating what object the class inherits from
  - with parentheses without stating what object the class inherits from
  - without parentheses
  - ``pass`` is a placeholder

* classes implicitly inherit from the ``object`` class, because in each of our tests, whether explicitly stated or not, the class is an ``instance`` of an ``object``
* what is an `object <https://docs.python.org/3/glossary.html#term-object>`_\ ?

.. admonition:: RULE OF THUMB


    From `the zen of python <https://peps.python.org/pep-0020/>`_
    ``Explicit is better than implicit``
    I prefer to use the explicit form of class definitions with the parent ``object`` in parentheses


How to define a Class with attributes
------------------------------

Since we know how to define a class, add some tests for attributes

RED: make it fail
^^^^^^^^^^^^^^^^^


* we add a failing test to ``TestClasses`` in ``classes.py``

  .. code-block:: python

           def test_classes_with_attributes(self):
               self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)

  the terminal updates to show an :doc:`AttributeError`

* add a class definition to ``classes.py``

  .. code-block:: python


     class ClassWithAttributes(object):

         pass

  though the terminal still outputs an :doc:`AttributeError`, this time it is for a missing attribute in our newly defined class


GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* we add an attribute to ``ClassWithAttributes``

  .. code-block:: python


     class ClassWithAttributes(object):

         a_boolean

  and the terminal updates to show a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_


* after updating the name with an assignment to :doc:`None </data structures: None>`

  .. code-block:: python


     class ClassWithAttributes(object):

         a_boolean = None

  the terminal updates to show an :doc:`AssertionError`


* we redefine the attribute to make the test pass

  .. code-block:: python


     class ClassWithAttributes(object):

         a_boolean = bool

  the terminal updates to show passing tests


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

What if we repeat this with other python `data structures <./DATA_STRUCTURES.rst>`_

RED: make it fail
^^^^^^^^^^^^^^^^^

update ``test_classes_with_attributes`` with more tests

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

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``ClassWithAttributes`` with attributes to make the tests pass

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

the terminal updates to show passing tests

How to define a Class with Methods
----------------------------------

We can define classes with :doc:`methods <functions>` which are function definitions within the class

RED: make it fail
^^^^^^^^^^^^^^^^^

Let us add some tests for class methods. update ``TestClasses`` in ``classes.py``

  .. code-block:: python

      def test_classes_with_methods(self):
          self.assertEqual(
              classes.ClassWithMethods.method_a(),
              'You called MethodA'
          )

the terminal updates to show :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* we add a class definition to ``classes.py``

  .. code-block:: python


  class ClassWithMethods(object):

      pass

  the terminal now gives an :doc:`AttributeError` with a different error


* add the missing attribute to the ``ClassWithMethods`` class

  .. code-block:: python


     class ClassWithMethods(object):

         method_a

  the terminal updates to show a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_ because there is no definition for ``method_a``


* when we define ``method_a`` as an attribute by assigning it as the name for the null value :doc:`None </data structures: None>`

  .. code-block:: python



  class ClassWithMethods(object):

      method_a = None

  the terminal now reveals a [TypeError](./TypeError.rst) since ``method_a`` is not callable


* update the definition of ``method_a`` to make it a function

  .. code-block:: python


     class ClassWithMethods(object):

         def method_a():
             return None

  and the terminal shows an :doc:`AssertionError`


* what we do now is change the value the function returns to match the expectation of our test

  .. code-block:: python

           def method_a():
               return 'You called MethodA'

  for the terminal to show passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* we can make this better by adding a few more tests to ``test_classes_with_methods`` for fun

  .. code-block:: python

           def test_classes_with_methods(self):
               self.assertEqual(classes.ClassWithMethods.method_a(), 'You called MethodA')
               self.assertEqual(classes.ClassWithMethods.method_b(), 'You called MethodB')
               self.assertEqual(classes.ClassWithMethods.method_c(), 'You called MethodC')
               self.assertEqual(classes.ClassWithMethods.method_d(), 'You called MethodD')

  the terminal updates to show an :doc:`AttributeError`

* update ``ClassWithmethods`` in ``classes.py`` until all tests pass

----

How to define a Class with Methods and Attributes
------------------------------------------

Since we know how to define classeswith Methods and how to define classes with attributes, What if we try defining a class that has both

RED: make it fail
^^^^^^^^^^^^^^^^^

we add another test for a class that has both attributes and methods

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

with the terminal giving an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

update ``classes.py`` to make the tests pass by defining the class, attribute and methods

.. code-block:: python


   class ClassWithAttributesAndMethods(object):

       attribute = 'attribute'

       def method():
           return 'you called a method'

----

How to define a Class with an initializer
----------------------------------

CONGRATULATIONS. You now know how to define classes, attributes and methods. We will now expand on this knowledge to learn how to use classes

RED: make it fail
^^^^^^^^^^^^^^^^^

we will add a failing test to ``test_classes.py``

.. code-block:: python

       def test_classes_with_initializers(self):
           self.assertEqual(classes.Boy().sex, 'M')

the terminal updates to show an :doc:`AttributeError`

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* add a definition for the class

  .. code-block:: python


     class Boy(object):

         pass

  the terminal updates to show another :doc:`AttributeError`


* update the ``Boy`` class with the name ``sex``

  .. code-block:: python


     class Boy(object):

         sex

  the terminal produces a `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_


* we add a definition for the ``sex`` attribute

  .. code-block:: python


     class Boy(object):

         sex = 'M'

  the terminal updates to show passing tests. Yes!


REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^


* add another test to ``test_classes_with_initializers``

  .. code-block:: python

       def test_classes_with_initializers(self):
           self.assertEqual(classes.Boy().sex, 'M')
           self.assertEqual(classes.Girl(sex='F').sex, 'F')

  the terminal displays an :doc:`AttributeError`

* trying the same solution we used for the ``Boy`` class, add a definition for the ``Girl`` class to ``classes.py``

  .. code-block:: python


     class Girl(object):

         sex = 'M'

  and the terminal displays a [TypeError](./TypeError.rst)

  .. code-block:: python
     TypeError: Girl() takes no arguments

  - If you have gone through the [functions](./07_functions.rst) chapter you will see a similarity in this last test and passing inputs to functions. The call `classes.Girl(sex='F')` looks like a call to a function with keyword arguments
  - Which begs the question - How do we define classes to accept keyword arguments when the definition of a class defines the parent it inherits from for example,  `class Class(object)`? The answer - We use an initializer
  - What is an initializer? a class method(function) that allows customization of `instances/copies` of a ``class``


* add an initiializer to the ``Girl`` class

  .. code-block:: python


     class Girl(object):

         sex = 'F'

         def __init__(self):
             pass

  the terminal responds with a [TypeError](./TypeError.rst)

  .. code-block:: python
     TypeError: __init__() got an unexpected keyword argument 'sex'


* update the signature of the ``__init__`` :doc:`method <functions>` to accept a keyword argument

  .. code-block:: python

       def __init__(self, sex=None):
           pass

  the terminal updates to show passing tests

* add another test for a class initializer to ``test_classes_with_initializers``

  .. code-block:: python

       def test_classes_with_initializers(self):
           self.assertEqual(classes.Boy().sex, 'M')
           self.assertEqual(classes.Girl(sex='F').sex, 'F')
           self.assertEqual(classes.Other(sex='?').sex, '?')

  the terminal displays an :doc:`AttributeError`

* add a class definition to ``classes.py``

  .. code-block:: python


    class Other(object):

        sex = '?'

        def __init__(self, sex=None):
            pass

  the terminal displays passing tests


* Wait a minute, we just repeated the same thing twice.

  - We defined a ``class`` with a name
  - defined an attribute called ``sex``
  - defined an ``__init__`` :doc:`method <functions>` which takes in a ``sex`` keyword argument

* What if we make the repetition complete by redefining the ``Boy`` class to match the ``Girl`` and ``Other`` class

  .. code-block:: python


    class Boy(object):

        sex = 'M'

        def __init__(self, sex=None):
            pass

  the terminal responds with all tests still passing and we have now written the same thing 3 times. Earlier on we discussed inheritance, and will now try to use it to remove this duplication


* try adding a new class called ``Human`` to ``classes.py`` before the definition for ``Boy`` with the same attribute and :doc:`method <functions>` of the classes we are trying to abstract

  .. code-block:: python


     class Human(object):

         sex = 'M'

         def __init__(self, sex='M'):
             pass


     class Boy(object):
         ...

  the terminal still shows passing tests


* Update the definitions for ``Boy`` to inherit from the ``Human`` class and all tests are still passing

  .. code-block:: python


     class Boy(Human):
         ...

* remove the ``sex`` attribute from the ``Boy`` class and the tests continue to pass
* remove the ``__init__`` method, and add the ``pass`` placeholder

  .. code-block:: python


    class Boy(Human):

        pass


* What if we try the same thing with the ``Girl`` class and update its definition to inherit from the ``Human`` class

  .. code-block:: python


       class Girl(Human):
           ...

* remove the ``sex`` attribute and the terminal outputs an :doc:`AssertionError`
* update the ``Human`` class to set the ``sex`` attribute in the initializer instead of at the class level

  .. code-block:: python


       class Human(object):

           sex = 'M'

           def __init__(self, sex='M'):
               self.sex = sex

  the terminal still shows an :doc:`AssertionError`

* when we remove the ``__init__`` :doc:`method <functions>` from the ``Girl`` class

  .. code-block:: python


       class Girl(Human):

           pass

  the terminal updates to show passing tests

* can we do the same with the ``Other`` class? update the definition to inherit from the ``Human`` class

  .. code-block:: python


       class Other(Human):

           pass

    the terminal updates to show passing tests

* one last change and we remove the ``sex`` attribute from the ``Human`` class

  .. code-block:: python

       class Human(object):

           def __init__(self, sex='M'):
               self.sex = sex

  all tests are passing in the terminal, we have successfully refactored the 3 classes and abstracted a ``Human`` class

Why did that work?


* the ``Boy``, ``Girl`` and ``Other`` class now inherit from the ``Human`` class which means they all get the same :doc:`methods <functions>` and attributes that the ``Human`` class has, including the ``__init__`` method
* ``self.sex`` within each class refers to the ``sex`` attribute in the class, allowing its definition from within the ``__init__`` method
* since ``self.sex`` is defined as a class attribute, it is accessible from outside the class as we do in our tests i.e ``classes.Girl(sex='F').sex`` and ``classes.Other(sex='?').sex``

----

How to View the Attributes and Methods of a Class
--------------------------------------------------

To view what ``attributes`` and ``methods`` are defined for any object we can call ``dir`` on the object. The ``dir`` :doc:`method <functions>` returns a :doc:`list` that contains the names of all attributes and :doc:`methods <functions>`in the class

RED: make it fail
^^^^^^^^^^^^^^^^^

add a test to ``test_classes.py``

.. code-block:: python

       def test_view_attributes_and_methods_of_an_object(self):
           self.assertEqual(
               dir(classes.ClassWithAttributesAndMethods),
               [

               ]
           )

the terminal updates to show an :doc:`AssertionError` as our expected and real values do not match

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^

copy the values from the terminal to update the test to make it pass

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
                   'method'
               ]
           )

the tests pass and we see the last two values in our list are ``attribute`` and ``method`` which we defined earlier

CONGRATULATIONS
You know


* how to define a class with an attribute
* how to define a class with a method
* how to define a class with an initializer
* how to view the attributes and :doc:`methods <functions>`of a class

Do you want to `read more about classes? <https://docs.python.org/3/tutorial/classes.html#tut-firstclasses>`_
