Write classes in python
====================

We will step through writing classes in python using Test Driven Development

### Prerequisites

- [How I setup a Test Driven Development Environment.md](./How I How I setup a Test Driven Development Environment.md.md)

---

## Classes

``(classes)`` are a template or blueprint that represent an object. They are a collection of `methods(functions)` and `attributes(variables)` that belong together

## Define a Class with pass

- use the ``(class)`` keyword
- use ``(TitleCase)`` for naming
- use Descriptive names

### RED: make it fail

we create a new file named `test_classes.py` in the ``(tests)`` directory

```python
import unittest
import classes


class TestClasses(unittest.TestCase):

    def test_class_definitions_with_pass(self):
        self.assertIsInstance(classes.ClassWithPass(), object)
```

the terminal displays a [ModuleNotFoundError](./MODULE_NOT_FOUND_ERROR.md)

### GREEN: make it pass

- create a python module named `classes.py` and the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
- add the name ``(ClassWithPass)`` to the module
    ```python


    ClassWithPass
    ```
    and the terminal updates to show a ``(NameError)`` because ``(ClassWithPass)`` is not defined anywhere
- update the name as an assignment to the null value ``(None)``
    ```python


    ClassWithPass = None
    ```
- redefine the variable as a class using the ``(class)`` keyword
    ```python


    class ClassWithPass:
    ```
    the terminal updates to show an [IndentationError](./02_INDENTATION_ERROR.md)
- add the ``(pass)`` keyword as a placeholder to the definition
    ```python


    class ClassWithPass:

        pass
    ```
    and the terminal updates to show passing tests

### REFACTOR: make it better

Let us review what we have written so far
- ``(pass)`` is a placeholder
- `self.assertIsInstance` is a `unittest.TestCase` method that checks if the first input to the method is an instance of the second input
- in python everything is an ``(object)`` which means there's a class definition for it, our test `self.assertIsInstance(classes.ClassWithPass(), object)` checks if ``(ClassWithPass)`` is an ``(object)``

## Define a Class with parentheses

### RED: make it fail

add another test to ``(TestClasses)`` in `test_classes.py`
```python
    def test_classes_definitions_with_parentheses(self):
        self.assertIsInstance(classes.ClassWithParentheses(), object)
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- update `classes.py` with a class definition
    ```python


    class ClassWithParentheses:

        pass
    ```
    the terminal updates to show passing tests
- update the definition to include parentheses
    ```python


    class ClassWithParentheses():

        pass
    ```
    the terminal shows all tests are still passing.
- We now know that we can define ``(classes)``
    - with parentheses
    - without parentheses
    - ``(pass)`` is a placeholder

### REFACTOR: make it better

In object oriented programming there is a concept called [Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)). With Inheritance we can define new ``(objects)`` that inherit from other existing ``(objects)``. This makes creating things easier because we do not have to reinvent or rewrite things that already exist, we can inherit them instead.


## Define a Class with inheritance

To use inheritance we specify the "parent" in parentheses when we define the new object (the child) to establish the relationship

### RED: make it fail

we add another test to ``(TestClasses)`` in `test_classes.py`
```python
    def test_class_definition_with_object(self):
        self.assertIsInstance(classes.ClassWithObject(), object)
```
and the terminal displays an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- let us add a class definition to `classes.py`
    ```python


    class ClassWithObject():

        pass
    ```
    the terminal reveals passing tests
- update the definition to explicitly state the parent ``(object)``
    ```python


    class ClassWithObject(object):

        pass
    ```
    and the terminal still shows passing tests

We now know that in python
- classes can be defined
    - with parentheses explicitly stating what object the class inherits from
    - with parentheses without stating what object the class inherits from
    - without parentheses
    - ``(pass)`` is a placeholder
- classes implicitly inherit from the ``(object)`` class, because in each of our tests, whether explicitly stated or not, the class is an ``(instance)`` of an ``(object)``
- what is an [object](https://docs.python.org/3/glossary.html#term-object)?

*RULE OF THUMB*
> From [the zen of python](https://peps.python.org/pep-0020/)
> `Explicit is better than implicit`
> we will use the explicit form of class definitions with the parent ``(object)`` in parentheses

## Define a Class with attributes

Since we know how to define a class, let us add some tests for attributes

### RED: make it fail

- we add a failing test to ``(TestClasses)`` in `classes.py`
    ```python
        def test_classes_with_attributes(self):
            self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)
    ```
    the terminal updates to show [AttributeError](./ATTRIBUTE_ERROR.md)
- add a class definition to `classes.py`
    ```python


    class ClassWithAttributes(object):

        pass
    ```
    though the terminal still outputs an [AttributeError](./ATTRIBUTE_ERROR.md), this time it is for a missing attribute in our newly defined class

### GREEN: make it pass

- we add an attribute to ``(ClassWithAttributes)``
    ```python


    class ClassWithAttributes(object):

        a_boolean
    ```
    and the terminal updates to show a ``(NameError)``
- after updating the name with an assignment to ``(None)``
    ```python


    class ClassWithAttributes(object):

        a_boolean = None
    ```
    the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md)
- we redefine the attribute to make the test pass
    ```python


    class ClassWithAttributes(object):

        a_boolean = bool
    ```
    the terminal updates to show passing tests

### REFACTOR: make it better

let us repeat this with other python [data structures](./DATA_STRUCTURES.md)

### RED: make it fail

update ``(test_classes_with_attributes)`` with more tests
```python
    def test_classes_with_attributes(self):
        self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)
        self.assertEqual(classes.ClassWithAttributes.an_integer, int)
        self.assertEqual(classes.ClassWithAttributes.a_float, float)
        self.assertEqual(classes.ClassWithAttributes.a_string, str)
        self.assertEqual(classes.ClassWithAttributes.a_tuple, tuple)
        self.assertEqual(classes.ClassWithAttributes.a_list, list)
        self.assertEqual(classes.ClassWithAttributes.a_set, set)
        self.assertEqual(classes.ClassWithAttributes.a_dictionary, dict)
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

update ``(ClassWithAttributes)`` with attributes to make the tests pass
```python


class ClassWithAttributes(object):

    a_boolean = bool
    an_integer = int
    a_float = float
    a_string = str
    a_tuple = tuple
    a_list = list
    a_set = set
    a_dictionary = dict
```
the terminal updates to show passing tests

## Define a Class with Methods

We can define classes with methods which are function definitions within the class

### RED: make it fail

Let us add some tests for class methods. update ``(TestClasses)`` in `classes.py`
```python
    def test_classes_with_methods(self):
        self.assertEqual(
            classes.ClassWithMethods.method_a(),
            'You called MethodA'
        )
```
the terminal updates to show [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- we add a class definition to `classes.py`
    ```python


    class ClassWithMethods(object):

        pass
    ```
    the terminal now gives an [AttributeError](./ATTRIBUTE_ERROR.md) with a different error
- let us add the missing attribute to the ``(ClassWithMethods)`` class
    ```python


    class ClassWithMethods(object):

        method_a
    ```
    the terminal updates to show a ``(Nameerror)`` because there is no definition for ``(method_a)``
- when we define ``(method_a)`` as an attribute by assigning it as the name for the null value ``(None)``
    ```python


    class ClassWithMethods(object):

        method_a = None
    ```
    the terminal now reveals a [TypeError](./TYPE_ERROR.md) since ``(method_a)`` is not callable
- let us update the definition of ``(method_a)`` to make it a function
    ```python


    class ClassWithMethods(object):

        def method_a():
            return None
    ```
    and the terminal shows an [AssertionError](./ASSERTION_ERROR.md)
- what we do now is change the value the function returns to match the expectation of our test
    ```python
        def method_a():
            return 'You called MethodA'
    ```
    for the terminal to show passing tests

### REFACTOR: make it better

- we can make this better by adding a few more tests to ``(test_classes_with_methods)`` for fun
    ```python
        def test_classes_with_methods(self):
            self.assertEqual(classes.ClassWithMethods.method_a(), 'You called MethodA')
            self.assertEqual(classes.ClassWithMethods.method_b(), 'You called MethodB')
            self.assertEqual(classes.ClassWithMethods.method_c(), 'You called MethodC')
            self.assertEqual(classes.ClassWithMethods.method_d(), 'You called MethodD')
    ```
    the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)
- update ``(ClassWithmethods)`` in `classes.py` until all tests pass

---

## Define a Class with Methods and Attributes

Since we know how to define classes with methods and how to define classes with attributes, let us try defining a class that has both

### RED: make it fail

we add another test for a class that has both attributes and methods

```python
    def test_classes_with_attributes_and_methods(self):
        self.assertEqual(
            classes.ClassWithAttributesAndMethods.attribute,
            'attribute'
        )
        self.assertEqual(
            classes.ClassWithAttributesAndMethods.method(),
            'you called a method'
        )
```
with the terminal giving an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

update `classes.py` to make the tests pass by defining the class, attribute and methods

```python


class ClassWithAttributesAndMethods(object):

    attribute = 'attribute'

    def method():
        return 'you called a method'
```

---

## Define a Class with an initializer

CONGRATULATIONS. You now know how to define classes, attributes and methods. We will now expand on this knowledge to learn how to use classes

### RED: make it fail

we will add a failing test to `test_classes.py`

```python
    def test_classes_with_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
```
the terminal updates to show an [AttributeError](./ATTRIBUTE_ERROR.md)

### GREEN: make it pass

- add a definition for the class
    ```python


    class Boy(object):

        pass
    ```
    the terminal updates to show another [AttributeError](./ATTRIBUTE_ERROR.md)
- update the ``(Boy)`` class with the name ``(sex)``
    ```python


    class Boy(object):

        sex
    ```
    the terminal produces a ``(NameError)``
- we add a definition for the ``(sex)`` attribute
    ```python


    class Boy(object):

        sex = 'M'
    ```
    the terminal updates to show passing tests. Yes!

### REFACTOR: make it better

- let us add another test to ``(test_classes_with_initializers)``
    ```python
    def test_classes_with_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')
    ```
    the terminal gives an [AttributeError](./ATTRIBUTE_ERROR.md)
- trying the same solution we used for the ``(Boy)`` class, add a definition for the ``(Girl)`` class to `classes.py`
    ```python


    class Girl(object):

        sex = 'M'
    ```
    and the terminal displays a [TypeError](./TYPE_ERROR.md)
    ```python
    TypeError: Girl() takes no arguments
    ```
    - If you have gone through the [functions](./07_FUNCTIONS.md) chapter you will see a similarity in this last test and passing inputs to functions. The call `classes.Girl(sex='F')` looks like a call to a function with keyword arguments
    - Which begs the question - How do we define classes to accept keyword arguments when the definition of a class defines the parent it inherits from e.g. `class Class(object)`? The answer - We use an initializer
    - What's an initializer? a class method(function) that allows customization of `instances/copies` of a ``(class)``
- add an initiializer to the ``(Girl)`` class
    ```python


    class Girl(object):

        sex = 'F'

        def __init__(self):
            pass
    ```
    the terminal responds with a [TypeError](./TYPE_ERROR.md)
    ```python
    TypeError: __init__() got an unexpected keyword argument 'sex'
    ```
- update the signature of the ``(__init__)`` method to accept a keyword argument
    ```python
    def __init__(self, sex=None):
        pass
    ```
    the terminal updates to show passing tests
- let us add another test for a class initializer to ``(test_classes_with_initializers)``
    ```python
    def test_classes_with_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')
        self.assertEqual(classes.Other(sex='?').sex, '?')
    ```
    the terminal displays an [AttributeError](./ATTRIBUTE_ERROR.md)
- add a class definition to `classes.py`
    ```python


    class Other(object):

        sex = '?'

        def __init__(self, sex=None):
            pass
    ```
    the terminal reveals passing tests
- Wait a minute, we just repeated the same thing twice.
    - We defined a ``(class)`` with a name
    - defined an attribute named ``(sex)``
    - defined an ``(__init__)`` method which takes in a ``(sex)`` keyword argument
- let us make the repetition complete by redefining the ``(Boy)`` class to match the ``(Girl)`` and ``(Other)`` class
    ```python


    class Boy(object):

        sex = 'M'

        def __init__(self, sex=None):
            pass
    ```
    the terminal responds with all tests still passing and we have now written the same thing 3 times. Earlier on we discussed inheritance, and will now try to use it to remove this duplication
- try adding a new class called ``(Human)`` to `classes.py` before the definition for ``(Boy)`` with the same attribute and method of the classes we are trying to abstract
    ```python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            pass


    class Boy(object):
        ...
    ```
    the terminal still shows passing tests
- Update the definitions for ``(Boy)`` to inherit from the ``(Human)`` class and all tests are still passing
    ```python
    class Boy(Human):
        ...
    ```
- remove the ``(sex)`` attribute from the ``(Boy)`` class and the tests continue to pass
- remove the ``(__init__)`` method, and add the ``(pass)`` placeholder
    ```python


    class Boy(Human):

        pass
    ```
- let us try the same thing with the ``(Girl)`` class and update its definition to inherit from the ``(Human)`` class
    ```python
    class Girl(Human):
        ...
    ```
- remove the ``(sex)`` attribute and the terminal outputs an [AssertionError](./ASSERTION_ERROR.md)
- update the ``(Human)`` class to set the ``(sex)`` attribute in the initializer instead of at the class level
    ```python
    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            self.sex = sex
    ```
    the terminal still responds with an [AssertionError](./ASSERTION_ERROR.md)
- when we remove the ``(__init__)`` method from the ``(Girl)`` class
    ```python
    class Girl(Human):

        pass
    ```
    the terminal updates to show passing tests
- can we do the same with the ``(Other)`` class? update the definition to inherit from the ``(Human)`` class
    ```python
    class Other(Human):

        pass
    ```
    the terminal updates to show passing tests
- one last change and we remove the ``(sex)`` attribute from the ``(Human)`` class
    ```python
    class Human(object):

        def __init__(self, sex='M'):
            self.sex = sex
    ```
    all tests are passing in the terminal, we have successfully refactored the 3 classes and abstracted a ``(Human)`` class

Why did that work?
- the ``(Boy)``, ``(Girl)`` and ``(Other)`` class now inherit from the ``(Human)`` class which means they all get the same methods and attributes that the ``(Human)`` class has, including the ``(__init__)`` method
- `self.sex` within each class refers to the ``(sex)`` attribute in the class, allowing its definition from the withing the ``(__init__)`` method
- since `self.sex` is defined as a class attribute, it is accessible from outside the class as we do in our tests i.e `classes.Girl(sex='F').sex` and `classes.Other(sex='?').sex`

## View the Attributes and Methods of a Class

To view what ``(attributes)`` and ``(methods)`` are defined for any object we can call ``(dir)`` on the object. The ``(dir)`` method returns a [list](./LISTS.md) that contains the names of all attributes and methods in the class

### RED: make it fail

add a test to `test_classes.py`
```python
    def test_view_attributes_and_methods_of_an_object(self):
        self.assertEqual(
            dir(classes.ClassWithAttributesAndMethods),
            [

            ]
        )
```

the terminal updates to show an [AssertionError](./ASSERTION_ERROR.md) as our expected and real values do not match

### GREEN: make it pass

copy the values from the terminal to update the test to make it pass

```python
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
```

the tests pass and we see the last two values in our list are ``(attribute)`` and ``(method)`` which we defined earlier

CONGRATULATIONS
You know
- how to define a class with an attribute
- how to define a class with a method
- how to define a class with an initializer
- how to view the attributes and methods defined for a class
- Do you want to [read more about classes?](https://docs.python.org/3/tutorial/classes.html#tut-firstclasses)