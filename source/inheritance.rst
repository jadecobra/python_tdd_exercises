.. include:: links.rst

.. danger:: DANGER WILL ROBINSON! Though the code works, this chapter is still UNDER CONSTRUCTION it may look completely different when I am done

#################################################################################
family ties
#################################################################################

In :ref:`test_attributes_and_methods_of_classes` I saw the :ref:`methods<what is a function?>` I added to the ``Person`` :ref:`class<what is a class?>` and also saw a lot of :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` that I did not add, which led to the question of where they came from.

In object oriented programming there is a concept called Inheritance_, it allows me to define new :ref:`objects<what is a class?>` that inherit from other :ref:`objects<what is a class?>`.

Making new :ref:`objects<what is a class?>` is easier with Inheritance_ because I do not have to rewrite things that have already been written, I can inherit them instead and change the new :ref:`objects<what is a class?>` for what I need

To use inheritance I specify the "parent" in parentheses when I define the new object (the child) to make the relationship

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: code/tests/test_person_classes.py
  :language: python
  :linenos:

-----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``classes`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh classes

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: shell

      ./makePythonTdd.ps1 classes

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 3
    :emphasize-text: test_classes

    E       AssertionError: True is not false

    tests/test_classes.py:7: AssertionError

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_person.py:7`` to open it in the :ref:`editor<2 editors>`

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes

* I change the name of the :ref:`class<what is a class?>` to match the :ref:`CapWords format<CapWords>` to follow :ref:`Python convention<conventions>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1

    class TestClasses(unittest.TestCase):

----

*********************************************************************************
test_making_a_class_w_pass
*********************************************************************************

* I `change directory`_ to the ``person`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd person

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: python

    .../pumping_python/person

* I activate the `virtual environment`_

  .. code-block:: python
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: Powershell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: python

    (.venv) .../pumping_python/person

* I use ``pytest-watch`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    pytest-watch

  the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 4

    rootdir: .../pumping_python/person
    collected 2 items

    tests/test_person.py ..                                             [100%]

    ============================ 2 passed in X.YZs =============================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_person.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
how to make a class in Python
*********************************************************************************

to review, I can make a :ref:`class<what is a class?>` with the class_ keyword, use :ref:`CapWords format<CapWords>` for the name and use a name that tells what the group of :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` do

----

I add another test to ``TestClasses`` in ``test_classes.py`` to show another way to make a class

.. code-block:: python

  def test_making_a_class_w_parentheses(self):
      self.assertIsInstance(classes.ClassWithParentheses(), object)

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`




* I add a class definition like ``ClassWithPass`` to ``classes.py``

  .. code-block:: python


    class ClassWithParentheses:

        pass

  the test passes

* When I make the definition include parentheses

  .. code-block:: python


    class ClassWithParentheses():

        pass

  the terminal_ shows all tests are still passing.

* I can confidently say that in Python_

  - I can define ``classes`` with parentheses
  - I can define ``classes`` without parentheses
  - pass_ is a placeholder

----




In object oriented programming there is a concept called Inheritance_. With Inheritance_ I can define new :ref:`objects<what is a class?>` that inherit from existing objects_.

Making new objects is easier because I do not have to reinvent or rewrite things that already exist, I can inherit them instead and change the new objects for my specific use case

To use inheritance I specify the "parent" in parentheses when I define the new object (the child) to make the relationship

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python

  def test_making_a_class_w_object(self):
      self.assertIsInstance(classes.ClassWithObject(), object)

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithObject():

        pass

  the terminal_ shows all tests passed

* then I change the definition to explicitly state the parent :ref:`object<what is a class?>`

  .. code-block:: python


    class ClassWithObject(object):

        pass

  and the terminal_ still shows passing tests

*********************************************************************************
test_update_classy_person_year_of_birth
*********************************************************************************

I now add some tests for attributes since I know how to define a class for attributes

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----


* I add a failing test to ``TestClasses`` in ``classes.py``

  .. code-block:: python

    def test_making_a_class_w_attributes(self):
        self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithAttributes(object):

        pass

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>` for a missing attribute in the newly defined class

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an attribute to ``ClassWithAttributes``

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

* after I point the name to :ref:`None<what is None?>`

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

* I redefine the attribute to make the test pass

  .. code-block:: python


    class ClassWithAttributes(object):

        a_boolean = bool

  the terminal_ shows all tests passed

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

:red:`RED`: make it fail
---------------------------------------------------------------------------------

Let us add more tests with the other Python_ data structures to ``test_making_a_class_w_attributes``

.. code-block:: python

  def test_making_a_class_w_attributes(self):
      self.assertEqual(classes.ClassWithAttributes.a_boolean, bool)
      self.assertEqual(classes.ClassWithAttributes.an_integer, int)
      self.assertEqual(classes.ClassWithAttributes.a_float, float)
      self.assertEqual(classes.ClassWithAttributes.a_string, str)
      self.assertEqual(classes.ClassWithAttributes.a_tuple, tuple)
      self.assertEqual(classes.ClassWithAttributes.a_list, list)
      self.assertEqual(classes.ClassWithAttributes.a_set, set)
      self.assertEqual(classes.ClassWithAttributes.a_dictionary, dict)

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

:green:`GREEN`: make it pass
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

the terminal_ shows all tests pass

----

*********************************************************************************
test_attributes_and_methods_of_classes
*********************************************************************************

I can also define classes with :ref:`methods<what is a function?>` which are :ref:`function<what is a function?>` definitions that belong to the class

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add some tests for class methods to ``TestClasses`` in ``classes.py``

.. code-block:: python

  def test_making_a_class_w_methods(self):
      self.assertEqual(
          classes.ClassWithMethods.method_a(),
          'You called MethodA'
      )

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----


* I add a class definition to ``classes.py``

  .. code-block:: python


    class ClassWithMethods(object):

        pass

  the terminal_ now gives :ref:`AttributeError<what causes AttributeError?>` with a different error


* When I add the missing attribute to the ``ClassWithMethods`` class

  .. code-block:: python


    class ClassWithMethods(object):

        method_a

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>` because there is no definition for ``method_a``


* I define ``method_a`` as an attribute by pointing it to :ref:`None<what is None?>`

  .. code-block:: python


    class ClassWithMethods(object):

        method_a = None

  the terminal_ shows :ref:`TypeError` since ``method_a`` is :ref:`None<what is None?>` which is not callable

* I change the definition of ``method_a`` to make it a :ref:`function<what is a function?>` which makes it callable

  .. code-block:: python


    class ClassWithMethods(object):

        def method_a():
            return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`. Progress!

* I then change the value that ``method_a`` returns to match the expectation of the test

  .. code-block:: python

    def method_a():
        return 'You called MethodA'

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I can "make this better" by adding a few more tests to ``test_making_a_class_w_methods`` for fun

  .. code-block:: python

    def test_making_a_class_w_methods(self):
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

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

* and I change each :ref:`assertion<what is an assertion?>` to the right value until they all pass

----


*********************************************************************************
test_making_a_class_w_attributes_and_methods
*********************************************************************************

Since I know how to define classes with methods and how to define classes with attributes, what happens when I define a class with both?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test for a class that has both attributes and methods

.. code-block:: python

  def test_making_a_class_w_attributes_and_methods(self):
      self.assertEqual(
          classes.ClassWithAttributesAndMethods.attribute,
          'attribute'
      )
      self.assertEqual(
          classes.ClassWithAttributesAndMethods.method(),
          'you called a method'
      )

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

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

To view what :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` are defined for any :ref:`object<what is a class?>` I can call dir_ on the :ref:`object<what is a class?>`.

The `dir built-in function`_ returns a :ref:`list <lists>` of all :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` of the object provided to it as input

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to ``test_classes.py``

.. code-block:: python

  def test_attributes_and_methods_of_objects(self):
    self.assertEqual(
        dir(classes.ClassWithAttributesAndMethods),
        []
    )

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` as the expected and real values do not match

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I copy the values from the terminal_ to change the expectation of the test

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
test_making_a_class_w_initializer
*********************************************************************************

When making a new class, we can define an initializer which is a :ref:`method<what is a function?>` that can receive inputs to be used to customize instances/copies of the class

*********************************************************************************
:red:`RED`: make it fail
*********************************************************************************

I add a failing test to ``test_classes.py``

.. code-block:: python

  def test_making_a_class_w_initializers(self):
      self.assertEqual(classes.Boy().sex, 'M')

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

*********************************************************************************
:green:`GREEN`: make it pass
*********************************************************************************

* I add a definition for the ``Boy`` class

  .. code-block:: python


    class Boy(object):

        pass

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

* I make the ``Boy`` class with an attribute called ``sex``

  .. code-block:: python


    class Boy(object):

        sex

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`


* I add a definition for the ``sex`` attribute

  .. code-block:: python


    class Boy(object):

        sex = 'M'

  the test passes

*********************************************************************************
:yellow:`REFACTOR`: make it better
*********************************************************************************

* I add another :ref:`assertion<what is an assertion?>` to ``test_making_a_class_w_initializers`` this time for a ``Girl`` class but with a difference, I provide the value for the ``sex`` attribute when I call the class

  .. code-block:: python

    def test_making_a_class_w_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

* I try the same solution I used for the ``Boy`` class then add a definition for the ``Girl`` class to ``classes.py``

  .. code-block:: python


    class Girl(object):

        sex = 'M'

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: Girl() takes no arguments

  - ``classes.Girl(sex='F')`` looks like a call to a :ref:`function<what is a function?>`
  - I can define classes that take values by using an initializer
  - An initializer is a class :ref:`method<what is a function?>` that allows customization of instances/copies of a class_

* I add the initializer :ref:`method<what is a function?>` called ``__init__`` to the ``Girl`` class

  .. code-block:: python


    class Girl(object):

        sex = 'F'

        def __init__(self):
            pass

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

   TypeError: __init__() got an unexpected keyword argument 'sex'

* I make the definition of the ``__init__`` :ref:`method<what is a function?>` take a keyword argument

  .. code-block:: python

    def __init__(self, sex=None):
        pass

  the test passes

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python

    def test_making_a_class_w_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')
        self.assertEqual(classes.Other(sex='?').sex, '?')

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class Other(object):

        sex = '?'

        def __init__(self, sex=None):
            pass

  the test passes

* Wait a minute, I just repeated the same thing twice.

  - I defined a class_ with a name
  - I defined an attribute called ``sex``
  - I defined an ``__init__`` :ref:`method<what is a function?>` which takes in a ``sex`` keyword argument

* I am going to make it a third repetition by redefining the ``Boy`` class to match the ``Girl`` and ``Other`` class because it is fun to do bad things

  .. code-block:: python


    class Boy(object):

        sex = 'M'

        def __init__(self, sex=None):
            pass

  the terminal_ shows all tests still passing and I have now written the same thing 3 times. Earlier on I mentioned inheritance, and now try to use it to remove this duplication so `I do not repeat myself`_

* I add a new class called ``Human`` to ``classes.py`` before the definition for ``Boy`` with the same attribute and :ref:`method<what is a function?>` of the classes I am trying to abstract

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            pass

  the terminal_ still shows passing tests

* I change the definitions for ``Boy`` to inherit from the ``Human`` class and all tests are still passing

  .. code-block:: python


    class Boy(Human):

        sex = 'M'

        def __init__(self, sex=None):
            pass

* I remove the ``sex`` attribute from the ``Boy`` class and the tests continue to pass
* I remove the ``__init__`` method, then add the pass_ placeholder

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

* I remove the ``sex`` attribute the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`
* I make the ``Human`` class to set the ``sex`` attribute in the parent initializer instead of at the child level

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            self.sex = sex

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* when I remove the ``__init__`` :ref:`method<what is a function?>` from the ``Girl`` class

  .. code-block:: python


    class Girl(Human):

        pass

  the test passes. Lovely

* I wonder if I can do the same with the ``Other`` class? I change the definition to inherit from the ``Human`` class

  .. code-block:: python


    class Other(Human):

        pass

  the test passes

* One More Thing! I remove the ``sex`` attribute from the ``Human`` class

  .. code-block:: python

    class Human(object):

      def __init__(self, sex='M'):
          self.sex = sex

  all tests are passing, I have successfully refactored the 3 classes and abstracted a ``Human`` class from them

* the ``Boy``, ``Girl`` and ``Other`` class now inherit from the ``Human`` class which means they all get the same :ref:`methods<what is a function?>` and attributes that the ``Human`` class has, including the ``__init__`` method
* ``self.sex`` in each class is the ``sex`` attribute in the class, allowing its definition from inside the ``__init__`` method
* since ``self.sex`` is defined as a class attribute, it is accessible from outside the class as I do in the tests i.e ``classes.Girl(sex='F').sex`` and ``classes.Other(sex='?').sex``

----

*********************************************************************************
review
*********************************************************************************

the tests show

* how to define a class with an attribute
* how to define a class with a :ref:`method<what is a function?>`
* how to define a class with an initializer
* how to view the :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` of a class
* classes can be defined

  - with parentheses stating what :ref:`object<what is a class?>` the class inherits from
  - with parentheses without stating what :ref:`object<what is a class?>` the class inherits from
  - without parentheses
  - pass_ is a placeholder

* classes by default inherit from the :ref:`object<what is a class?>` class, because in each of the tests, whether the parent is stated or not, each class I defined is an ``instance`` of an :ref:`object<what is a class?>`

.. attention:: :PEP:`Zen of Python <20>`

  I prefer to use the explicit form of class definitions with the parent :ref:`object<what is a class?>` in parentheses, from the :PEP:`Zen of Python <20>`:
  ``Explicit is better than implicit``

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I have open in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ and exit the tests with :kbd:`ctrl+c` on the keyboard
* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/person

* I `change directory`_ to the parent of ``person``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<classes: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of things and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`what you can do with classes<what is a class?>`

Would you like to :ref:`test ModuleNotFoundError?<ModuleNotFoundError>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->