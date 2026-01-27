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

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`how to make a person`
* :ref:`classes<what is a class?>`

----

*********************************************************************************
open the project
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

* I make a new file_ in the ``tests`` folder_ named ``test_classes.py``

* I make another file in the ``src`` folder_ named ``classes.py``

----

*********************************************************************************
test_making_a_class_w_pass
*********************************************************************************

----

to review, I can make a :ref:`class<what is a class?>` with the :ref:`class<what is a class?>` keyword, use :ref:`CapWords format<CapWords>` for the name and use a name that tells what the group of :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` do

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an `import statement`_ for the ``classes`` :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    import unittest
    import src.classes


    class TestClasses(unittest.TestCase):

* I change ``test_failure`` to ``test_making_a_class_w_pass``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            self.assertIsInstance(src.classes.WPass(), object)


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'WPass'

  there is no definition for ``WPass`` in ``classes.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``classes.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* then I add a :ref:`class<what is a class?>` definition to ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 3

    class WPass:

        pass

  the test passes

pass_ is a placeholder, it makes sure I am following Python_ rules and :ref:`I can make a class with pass<test_making_a_class_w_pass>`

----

*********************************************************************************
test_making_a_class_w_parentheses
*********************************************************************************

----

I can also make a :ref:`class<what is a class?>` with parentheses.

----

=================================================================================
:red:`RED`: make it red
=================================================================================

----

I add another test in ``test_classes.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 4-5

      def test_making_a_class_w_pass(self):
          self.assertIsInstance(src.classes.WPass(), object)

      def test_making_a_class_w_parentheses(self):
          self.assertIsInstance(src.classes.WParentheses(), object)


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  E       AttributeError: module 'src.classes' has no attribute 'WParentheses'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a class definition like ``WPass`` to ``classes.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 6, 8

  class WPass:

      pass


  class WParentheses:

      pass

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add parentheses to the definition

  .. code-block:: python
    :lineno-start: 6
    :emphasize-lines: 1
    :emphasize-text: ( )

    class WParentheses():

        pass

  the terminal_ shows all tests are still passing.

pass_ is a placeholder, it makes sure I am following Python_ rules, I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`

----

*********************************************************************************
test_making_a_class_w_object
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test to ``TestClasses`` in ``test_classes.py``

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 4-5

      def test_making_a_class_w_parentheses(self):
          self.assertIsInstance(src.classes.WParentheses(), object)

      def test_making_a_class_w_object(self):
          self.assertIsInstance(src.classes.WObject(), object)


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.classes' has no attribute 'WObject'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a class definition to ``classes.py``

.. code-block:: python
  :lineno-start: 6
  :emphasize-lines: 6, 8

  class WParentheses():

      pass


  class WObject():

      pass

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The last two tests pass because everything in Python_ is an object_ also known as a :ref:`class<what is a class?>`. object_ is the mother :ref:`class<what is a class?>` of all :ref:`classes<what is a class?>`. I can use anything in the `assertIsInstance method`_ and the test would pass.

I use the examples to show different ways to make a :ref:`class<what is a class?>`. I can also say who the parent of a :ref:`class<what is a class?>` is when I define it. I add object_ to the definition

.. code-block:: python
  :lineno-start: 11
  :emphasize-lines: 1

  class WObject(object):

      pass

the test is still green. pass_ is a placeholder, it makes sure I am following Python_ rules, I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`
* :ref:`its parent<test_making_a_class_w_object>`

----

*********************************************************************************
test_attributes_and_methods_of_objects
*********************************************************************************

I add a test to show the :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` of object_

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test to ``test_classes.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 4-8

      def test_making_a_class_w_object(self):
          self.assertIsInstance(src.classes.WObject(), object)

      def test_attributes_and_methods_of_objects(self):
          self.assertEqual(
              dir(object),
              []
          )


  # Exceptions seen

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: Lists differ: ['__class__', '__delattr__', '__dir__', '_[272 chars]k__'] != []

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I copy and paste the values from the terminal_ as the expectation and use the ``Find and Replace`` feature of the `Integrated Development Environment (IDE)`  to remove the extra characters

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 4-29

      def test_attributes_and_methods_of_objects(self):
          self.assertEqual(
              dir(object),
              [
                  '__class__',
                  '__delattr__',
                  '__dir__',
                  '__doc__',
                  '__eq__',
                  '__format__',
                  '__ge__',
                  '__getattribute__',
                  '__getstate__',
                  '__gt__',
                  '__hash__',
                  '__init__',
                  '__init_subclass__',
                  '__le__',
                  '__lt__',
                  '__ne__',
                  '__new__',
                  '__reduce__',
                  '__reduce_ex__',
                  '__repr__',
                  '__setattr__',
                  '__sizeof__',
                  '__str__',
                  '__subclasshook__'
              ]
          )


  # Exceptions seen

and it passes. All :ref:`classes<what is a class?>` automatically get these attributes, they inherit them

----

*********************************************************************************
test_making_classes_w_inheritance
*********************************************************************************

* I add

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

Would you like to :ref:`test ModuleNotFoundError?<what is a module?>`

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