.. include:: ../links.rst

#############################################################################
classes: attributes and methods
#############################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

*****************************************************************************
requirements
*****************************************************************************

:ref:`test_classes`

----

.. _test_classes_w_attributes:

*****************************************************************************
test_classes_w_attributes
*****************************************************************************

I now add some tests for attributes since I know how to define a class for attributes

.. _test_classes_w_attributes_red:

red: make it fail
#############################################################################


* I add a failing test to ``TestClasses`` in ``classes.py``

  .. code-block:: python

    def test_classes_w_attributes(self):
        self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)

  the terminal shows an :ref:`AttributeError`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithAttributes(object):

        pass

  the terminal shows an :ref:`AttributeError` for a missing attribute in the newly defined class

.. _test_classes_w_attributes_green:

green: make it pass
#############################################################################

* I add an attribute to ``ClassWithAttributes``

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean

  and the terminal shows a ` <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_

* after I make the name with an assignment to :ref:`None`

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = None

  the terminal shows an :ref:`AssertionError`

* I redefine the attribute to make the test pass

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = bool

  and the terminal shows all tests passed

.. _test_classes_w_attributes_refactor:

refactor: make it better
#############################################################################

.. _test_classes_w_attributes_refactor_red:

red: make it fail
-----------------------------------------------------------------------------

Let us add more tests with the other python data structures to ``test_classes_w_attributes``

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

the terminal shows an :ref:`AttributeError`

.. _test_classes_w_attributes_refactor_green:

green: make it pass
-----------------------------------------------------------------------------

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

.. _test_classes_w_methods:

*****************************************************************************
test_classes_w_methods
*****************************************************************************

I can also define classes with :ref:`methods<functions>` which are function definitions that belong to the class

.. _test_classes_w_methods_red:

red: make it fail
#############################################################################

I add some tests for class methods to ``TestClasses`` in ``classes.py``

.. code-block:: python

  def test_classes_w_methods(self):
      self.assertEqual(
          classes.ClassWithMethods.method_a(),
          'You called MethodA'
      )

and the terminal shows :ref:`AttributeError`

.. _test_classes_w_methods_green:

green: make it pass
#############################################################################


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithMethods(object):

        pass

  the terminal now gives an :ref:`AttributeError` with a different error


* When I add the missing attribute to the ``ClassWithMethods`` class

  .. code-block:: python


    class ClassWithMethods(object):

        method_a

  the terminal shows a NameError_ because there is no definition for ``method_a``


* I define ``method_a`` as an attribute by assigning the name to the null value :ref:`None`

  .. code-block:: python


    class ClassWithMethods(object):

        method_a = None

  the terminal shows a :ref:`TypeError` since ``method_a`` refers to :ref:`None` which is not callable

* I make the definition of ``method_a`` to make it a :ref:`function<functions>` which makes it callable

  .. code-block:: python


    class ClassWithMethods(object):

        def method_a():
            return None

  and the terminal shows an :ref:`AssertionError`. Progress!

* I then change the value that ``method_a`` returns to match the expectation of the test

  .. code-block:: python

    def method_a():
        return 'You called MethodA'

  and the test passes

.. _test_classes_w_methods_refactor:

refactor: make it better
#############################################################################

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

  the terminal shows an :ref:`AttributeError`

* and I change each assertion with the correct value until they all pass

----

.. _test_classes_w_attributes_and_methods:

*****************************************************************************
test_classes_w_attributes_and_methods
*****************************************************************************

Since I know how to define classes with methods and how to define classes with attributes, what happens when I define a class with both?

.. _test_classes_w_attributes_and_methods_red:

red: make it fail
#############################################################################

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

the terminal shows an :ref:`AttributeError`

.. _test_classes_w_attributes_and_methods_green:

green: make it pass
#############################################################################

I make ``classes.py`` to make the tests pass by defining the class, attribute and methods

.. code-block:: python


  class ClassWithAttributesAndMethods(object):

      attribute = 'attribute'

      def method():
          return 'you called a method'

----

.. _test_object_attributes_and_methods:

*****************************************************************************
test_object_attributes_and_methods
*****************************************************************************

To view what :ref:`attributes<AttributeError>` and ``methods`` are defined for any `object <https://docs.python.org/3/glossary.html#term-object>`_ I can call ``dir`` on the `object <https://docs.python.org/3/glossary.html#term-object>`_.

The ``dir`` :ref:`method<functions>` returns a :doc:`list </data_structures/lists/lists>` of all attributes and :ref:`methods<functions>` of the object provided to it as input

.. _test_object_attributes_and_methods_red:

red: make it fail
#############################################################################

I add a test to ``test_classes.py``

.. code-block:: python

  def test_object_attributes_and_methods(self):
    self.assertEqual(
        dir(classes.ClassWithAttributesAndMethods),
        []
    )

the terminal shows an :ref:`AssertionError` as the expected and real values do not match

.. _test_object_attributes_and_methods_green:

green: make it pass
#############################################################################

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

*****************************************************************************
review
*****************************************************************************

CONGRATULATIONS! If you made it this far and typed along with me, You know

* how to define a class with an attribute
* how to define a class with a :ref:`method<functions>`
* how to define a class with an initializer
* how to view the attributes and :ref:`methods<functions>` of a class

Would you like to :ref:`test_classes_w_initializers`?

----

:doc:`code/code_classes`
