.. include:: ../links.rst

.. _super: https://docs.python.org/3/library/functions.html#super
.. _super built-in function: super_

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

.. literalinclude:: ../code/tests/test_classes.py
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

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    pytest-watcher

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

I copy and paste the values from the terminal_ as the expectation and use the ``Find and Replace`` feature of the `Integrated Development Environment (IDE)`_ to remove the extra characters

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


=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 5-9

                  '__subclasshook__'
              ]
          )

      def test_making_classes_w_inheritance(self):
          self.assertIsInstance(
              src.classes.Doe('doe'),
              src.person.Person
          )


  # Exceptions seen

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.classes' has no attribute 'Doe'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class<what is a class?>` definition to ``classes.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 6, 8

    class WObject(object):

        pass


    class Doe(object):

        pass

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe() takes no arguments

* I add the ``__init__`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3, 4

    class Doe(object):

        def __init__(self):
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe.__init__() takes 1 positional argument but 2 were given

* I add a parameter to the :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

    class Doe(object):

        def __init__(self, first_name):
            return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <src.classes.Doe object at 0xffff01a2bc34> is not an instance of <class 'src.person.Person'>

* I add an `import statement`_ at the top of ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.person


    class WPass:

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change the "parent" of ``Doe``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1

    class Doe(src.person.Person):

        def __init__(self, first_name):
            return None

  the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a test for the :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` of the ``Doe`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 47

        def test_making_classes_w_inheritance(self):
            self.assertIsInstance(
                src.classes.Doe('doe'),
                src.person.Person
            )
            self.assertEqual(
                dir(src.classes.Doe),
                []
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ: ['__class__', '__delattr__', '__dict__', '[377 chars]llo'] != []

* I change the expectation

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 8

        def test_making_classes_w_inheritance(self):
            self.assertIsInstance(
                src.classes.Doe('doe'),
                src.person.Person
            )
            self.assertEqual(
                dir(src.classes.Doe),
                dir(src.person.Person)
            )


    # Exceptions seen

  the test passes. I do not need to add an `import statement`_ because ``classes.py`` imports ``src.person`` and I import ``src.classes`` at the beginning of ``test_person.py``

* I add the `import statement`_ to be clearer

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    import unittest
    import src.classes
    import src.person


    class TestClasses(unittest.TestCase):

  the test is still green

* I can remove the ``__init__`` :ref:`method<what is a function?>` from the ``Doe`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1

    class Doe(src.person.Person): pass

  the test is still green

----

*********************************************************************************
test_family_ties
*********************************************************************************


=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test for Inheritance_

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 6-9

            self.assertEqual(
                dir(src.classes.Doe),
                dir(src.person.Person)
            )

        def test_family_ties(self):
            doe = src.classes.Doe('doe')
            jane = src.classes.Doe('jane')
            john = src.classes.Doe('john')


    # Exceptions seen

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``doe``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3

            john = src.classes.Doe('john')

            self.assertEqual(doe.last_name, '')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 63
  :emphasize-lines: 1

            self.assertEqual(doe.last_name, 'doe')

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 4

            john = src.classes.Doe('john')

            self.assertEqual(doe.last_name, 'doe')
            self.assertEqual(jane.last_name, '')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 1

            self.assertEqual(jane.last_name, 'doe')

  the test passes

* I add one more :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2

            self.assertEqual(jane.last_name, 'doe')
            self.assertEqual(john.last_name, '')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 1

            self.assertEqual(john.last_name, 'doe')

  the test passes. All 3 people made with the ``Doe`` :ref:`class<what is a class?>` have the same last name, they are related.

* I add a person from another family

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 5

        def test_family_ties(self):
            doe = src.classes.Doe('doe')
            jane = src.classes.Doe('jane')
            john = src.classes.Doe('john')
            mary = src.classes.Smith('mary')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Smith'

* I add a :ref:`class<what is a class?>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    class Doe(src.person.Person): pass
    class Smith(src.person.Person): pass

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the ``last_name`` of ``mary``

  .. code-block:: python
    :lineno-start: 66

            self.assertEqual(john.last_name, 'doe')
            self.assertEqual(mary.last_name, '')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* ``mary`` should have a last name of ``smith`` not ``doe``. I change the expectation

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1

            self.assertEqual(mary.last_name, 'smith')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'smith'

* I add a value for ``last_name`` to the ``Smith`` :ref:`class<what is a class?>` in ``classes.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1, 3-4

    class Smith(src.person.Person):

        def __init__(self, first_name, last_name='smith'):
            pass

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Smith' object has no attribute 'last_name'

* I need to add the :ref:`class attributes<test_attribute_error_w_class_attributes>`. I can do that by calling the ``__init__`` :ref:`method<what is a function?>` of the ``Person`` :ref:`class<what is a class?>`. Python_ has a way for me to do that, I add it

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4

    class Smith(src.person.Person):

        def __init__(self, first_name, last_name='smith'):
            super().__init__(first_name, last_name)

  the test passes.

  the `super built-in function`_ calls the ``__init__`` :ref:`method<what is a function?>` of the parent :ref:`class<what is a class?>` with the values I pass in parentheses.

  In this case it calls the ``Person`` :ref:`class<what is a class?>` with values for ``first_name`` and ``last_name``

* I add another person to ``test_classes.py``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3

            john = src.classes.Doe('john')
            mary = src.classes.Smith('mary')
            joe = src.classes.Blow('joe')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Blow'

* I add the :ref:`class<what is a class?>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 21

    class Smith(src.person.Person):

        def __init__(self, first_name, last_name='smith'):
            super().__init__(first_name, last_name)

    class Blow(src.person.Person): pass

  the test passes

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``joe``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

            self.assertEqual(john.last_name, 'doe')
            self.assertEqual(mary.last_name, 'smith')
            self.assertEqual(joe.last_name, 'blow')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add the ``__init__`` :ref:`method<what is a function?>` to the class

  .. code-block:: python
    :lineno-start: 26

    class Blow(src.person.Person):

        def __init__(self, first_name, last_name='blow'):
            pass

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Blow' object has no attribute 'last_name'

* I use the `super built-in function`_

  .. code-block:: python
    :lineno-start: 28

    class Blow(src.person.Person):

        def __init__(self, first_name, last_name='blow'):
            super().__init__(first_name, last_name)

  the test passes

* I add a new person who is a child of ``jane`` named ``baby`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

            joe = src.classes.Blow('joe')
            baby = src.classes.Baby('baby')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Baby'

* I add a :ref:`class<what is a class?>` for ``baby`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 7

    class Blow(src.person.Person):

        def __init__(self, first_name, last_name='blow'):
            super().__init__(first_name, last_name)


    class Baby(Doe): pass

  the test passes

* ``baby`` is also the child of ``joe``. I add an :ref:`assertion<what is an assertion?>` for the last name of ``baby`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

            self.assertEqual(mary.last_name, 'smith')
            self.assertEqual(joe.last_name, 'blow')
            self.assertEqual(baby.last_name, 'blow')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add another parent to the ``Baby`` :ref:`class<what is a class?>` in ``classes.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    class Baby(Blow, Doe): pass

  the test passes

* I add another person, a child of ``john`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

            joe = src.classes.Blow('joe')
            baby = src.classes.Baby('baby')
            lil = src.classes.Lil('lil')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ shows :ref:`AttributError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Lil'

* I add a :ref:`class<what is a class?>` for ``lil`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4

    class Baby(Blow, Doe): pass


    class Lil(Doe): pass

  the test passes

* ``lil`` is also the child of ``mary``. I add an :ref:`assertion<what is an assertion?>` for the last name of ``lil``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

            self.assertEqual(joe.last_name, 'blow')
            self.assertEqual(baby.last_name, 'blow')
            self.assertEqual(lil.last_name, '')


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I add another parent to show that ``lil`` is a child of ``Doe`` and ``Smith`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1

    class Lil(Doe, Smith): pass

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != ''

  this is a problem. When I made ``Baby``, it took the last name of the first parent, and when I try the same thing with ``Lil`` it has the last name of the second parent

* I add a call to the `super built-in function`_ in the ``Doe`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1, 3-4

    class Doe(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name)


    class Smith(src.person.Person):

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe.__init__() takes 2 positional arguments but 3 were given

  because the ``Baby`` class passes a value for ``last_name``

* I add ``last_name`` to the call to ``__init__`` :ref:`method<what is a function?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3-4

    class Doe(src.person.Person):

        def __init__(self, first_name, last_name='doe'):
            super().__init__(first_name, last_name)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I change the expectation in ``test_classes.py``

  .. code-block:: python

            self.assertEqual(lil.last_name, 'doe')

  the test passes

----

*********************************************************************************
review
*********************************************************************************

I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`
* :ref:`its parent<test_making_a_class_w_object>`

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

:ref:`Would you like to test if bool_ is an int_?<booleans 3>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->