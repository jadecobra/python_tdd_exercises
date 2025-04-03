.. include:: ../links.rst

#################################################################################
classes: attributes and methods
#################################################################################


.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`test_classes`

----


*********************************************************************************
test_classes_w_attributes
*********************************************************************************

I now add some tests for attributes since I know how to define a class for attributes

red: make it fail
#################################################################################


* I add a failing test to ``TestClasses`` in ``classes.py``

  .. code-block:: python

    def test_classes_w_attributes(self):
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

Let us add more tests with the other Python data structures to ``test_classes_w_attributes``

.. code-block:: python

  def test_classes_w_attributes(self):
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
test_classes_w_methods
*********************************************************************************

I can also define classes with :ref:`methods<functions>` which are :ref:`function<functions>` definitions that belong to the class

red: make it fail
#################################################################################

I add some tests for class methods to ``TestClasses`` in ``classes.py``

.. code-block:: python

  def test_classes_w_methods(self):
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

* I can "make this better" by adding a few more tests to ``test_classes_w_methods`` for fun

  .. code-block:: python

    def test_classes_w_methods(self):
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
test_classes_w_attributes_and_methods
*********************************************************************************

Since I know how to define classes with methods and how to define classes with attributes, what happens when I define a class with both?

red: make it fail
#################################################################################

I add another test for a class that has both attributes and methods

.. code-block:: python

  def test_classes_w_attributes_and_methods(self):
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
test_object_attributes_and_methods
*********************************************************************************

To view what :ref:`attributes<AttributeError>` and ``methods`` are defined for any object_ I can call ``dir`` on the object_.

The ``dir`` :ref:`method<functions>` returns a :ref:`list <lists>` of all :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of the object provided to it as input

red: make it fail
#################################################################################

I add a test to ``test_classes.py``

.. code-block:: python

  def test_object_attributes_and_methods(self):
    self.assertEqual(
        dir(classes.ClassWithAttributesAndMethods),
        []
    )

the terminal shows :ref:`AssertionError` as the expected and real values do not match

green: make it pass
#################################################################################

I copy the values from the terminal to change the expectation of the test

.. code-block:: python

  def test_object_attributes_and_methods(self):
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

----

*********************************************************************************
review
*********************************************************************************

CONGRATULATIONS! If you made it this far and typed along with me, You know

* how to define a class with an attribute
* how to define a class with a :ref:`method<functions>`
* how to define a class with an initializer
* how to view the :ref:`attributes<AttributeError>` and :ref:`methods<functions>` of a class

Would you like to :ref:`test_classes_w_initializers? <classes: test_classes_w_initializers>`

----

:doc:`/code/code_classes`
