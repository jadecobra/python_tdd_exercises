.. meta::
  :description: Step-by-step TDD tutorial on Python inheritance, cooperative multiple inheritance, and Method Resolution Order (MRO). Learn how to inherit from parent classes, use the super() function to call parent constructors, inspect objects with dir(), and handle complex inheritance chains using double starred **kwargs. Learn to diagnose and resolve beginner bugs: TypeError: Blow.__init__() takes 1 positional argument but 2 were given, TypeError: got an unexpected keyword argument 'last_name', TypeError: missing 1 required positional argument, AttributeError: module has no attribute, and AssertionError: is not an instance of.
  :keywords: Jacob Itegboje, Pumping Python, python inheritance tutorial for beginners, test-driven development multiple inheritance python, what is cooperative multiple inheritance, python method resolution order mro, how to use super function in python class, why do all python classes inherit from object, using isinstance and assertIsInstance in tests, how to use double starred expression kwargs in python class, class vs instance python, TypeError Blow.__init__ takes 1 positional argument but 2 were given, TypeError got an unexpected keyword argument last_name, TypeError Person.__init__ missing 1 required positional argument, AttributeError module classes has no attribute Doe, NameError name person is not defined, AssertionError is not an instance of, method resolution order python super constructor, C3 linearization python multiple inheritance, pass keyword in python class inheritance, python class with parentheses vs without parentheses, how to call parent __init__ constructor, python red green refactor multiple inheritance tutorial, diamond problem python super, Doe, Blow, Smith, Jane, Joe, Mary, John, Lil

.. include:: ../links.rst

.. _super: https://docs.python.org/3/library/functions.html#super
.. _super built-in function: super_
.. _MRO: https://docs.python.org/3/howto/mro.html#python-2-3-mro
.. _Method Resolution Order: MRO_
.. _Python's Method Resolution Order: MRO_

#################################################################################
family ties
#################################################################################

In object oriented programming there is a concept called Inheritance_, it allows me to define new :ref:`objects<what is a class?>` that get their magic powers from other :ref:`objects<what is a class?>`.

Making new :ref:`objects<what is a class?>` can be easier with Inheritance_ because I do not have to rewrite things that have already been written, I can inherit them instead and change the new :ref:`objects<what is a class?>` to do what I want.

It can also be more complicated because I can make new instances to inherit from one :ref:`class<what is a class?>` and customize it for what I need instead of making new :ref:`classes<what is a class?>` that require me to keep track of `Python's Method Resolution Order`_.

----

*********************************************************************************
how to make a class with a parent
*********************************************************************************

To use inheritance_ I put the "parent" in parentheses when I :ref:`define<how to make a class>` the new :ref:`object<what is a class?>` (the child) to make the relationship

.. code-block:: python

  class Child(Parent):

      attribute = SOMETHING

      def method():
          the body of the method
          ...

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_family_ties.py
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

* I make a new file_ in the ``tests`` folder_ named ``test_classes.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/test_classes.py

* I make a new file_ in the ``src`` folder_ named ``classes.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch src/classes.py

* I open ``test_classes.py`` in the :ref:`editor<2 editors>` of the `Integrated Development Environment (IDE)`_

  .. tip::

    I can open a file_ from the terminal_ in the `Integrated Development Environment (IDE)`_ with the name of the program_ and the name of the file_. That means if I type this in the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code tests/test_classes.py

    `Visual Studio Code`_ opens ``test_classes.py`` in the :ref:`editor<2 editors>`

* I add :ref:`the first failing test<test_failure>` to ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestClasses(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)

* I go back to the terminal_ to add the new files_ and folders_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

  the terminal_ goes back to the command line.

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 8, 10

    ================================ FAILURES ==============================
    _______________________ TestClasses.test_failure _______________________

    self = <tests.test_classes.TestClasses testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_classes.py:7: AssertionError
    ======================== short test summary info =========================
    FAILED tests/test_classes.py::TestClasses::test_failure - AssertionError: True is not false
    =========================== 1 failed in X.YZs ============================

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py`` in the :ref:`editor<2 editors>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestFunctions(unittest.TestCase):

        def test_failure(self):
            self.assertFalse(True)


    # Exceptions seen
    # AssertionError

* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1

            self.assertFalse(False)

  the test passes.

----

*********************************************************************************
test_making_a_class_w_pass
*********************************************************************************

To review, I can make a :ref:`class<what is a class?>` with the :ref:`class<what is a class?>` keyword, use :ref:`CapWords format<CapWords>` for the name and use a name that tells what the group of :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` do.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

---------------------------------------------------------------------------------
how to test if something is NOT an instance of a class
---------------------------------------------------------------------------------

----

I can test if an :ref:`object<what is a class?>` is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of another :ref:`object<what is a class?>` or NOT with the `isinstance built-in function`_ from `The Python Standard Library`_, it checks if the thing in the parentheses on the left is an :ref:`instance<how to test if something is an instance of a class>` of the :ref:`class<what is a class?>` on the right in the parentheses

* I change ``test_failure`` to :ref:`test_making_a_class_w_pass` then add an :ref:`assertion<what is an assertion?>` with isinstance_

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-6

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            assert not isinstance(
                src.classes.WPass(), object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because ``src`` is not defined in this file_

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ for the ``classes`` :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.classes
    import unittest


    class TestClasses(unittest.TestCase):

  - ``import src.classes`` brings in an :ref:`object<what is a class?>` that represents the ``classes.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_classes.py``
  - the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

    .. code-block:: python

      AttributeError: module 'src.classes'
                      has no attribute 'WPass'

    because there is no definition for ``WPass`` in ``classes.py``

* I add :ref:`AttributeError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I use the :ref:`Explorer<explorer on left>` to open ``classes.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* then I add a :ref:`class<what is a class?>` definition for ``WPass`` to ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    class WPass: pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: python

    AssertionError: assert not True

  because the statement ``not isinstance(src.classes.WPass(), object)`` is :ref:`False<test_what_is_false>`

----

---------------------------------------------------------------------------------
how to test if something is an instance of a class
---------------------------------------------------------------------------------

----

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-3

        def test_making_a_class_w_pass(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WPass(), object
            )


    # Exceptions seen


  * the :ref:`assertion<what is an assertion?>` - ``assert isinstance(src.classes.WPass(), object)`` checks if the result of a call to ``WPass`` in ``src.classes.py`` in the ``src`` folder_ also known as ``src.classes.WPass()``, is an :ref:`instance<how to test if something is an instance of a class>` of the :ref:`object class<what is a class?>` (the mother of all :ref:`classes<what is a class?>`)

  * the :ref:`class definition<how to make a class>` simply says pass_ and the test passes
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body)
  * the test passes because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The `unittest.TestCase class`_ has 2 :ref:`methods<what is a method?>` I can also use to test if an :ref:`object<what is a class?>` is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of a :ref:`class<what is a class?>` or NOT - assertIsInstance_ and assertNotIsInstance_

----

---------------------------------------------------------------------------------
another way to test if something is NOT an instance of a class
---------------------------------------------------------------------------------

----

I add the `assertNotIsInstance method`_ to the test

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6-8
  :emphasize-text: Not

      def test_making_a_class_w_pass(self):
          # assert not isinstance(
          assert isinstance(
              src.classes.WPass(), object
          )
          self.assertNotIsInstance(
              src.classes.WPass(), object
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError:
      <src.classes.WPass() object at 0xffff8a7b6543>
      is an instance of <class 'object'>

----

---------------------------------------------------------------------------------
another way to test if something is an instance of a class
---------------------------------------------------------------------------------

----

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

        def test_making_a_class_w_pass(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WPass(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WPass(), object
            )


    # Exceptions seen

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``src.classes.WPass()``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            # assert not isinstance(
            assert isinstance(
                src.classes.WPass(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WPass(), object
            )


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WPass()``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4-6, 8-10

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            # assert not isinstance(
            assert isinstance(an_instance, object)
            #     src.classes.WPass(), object
            # )
            # self.assertNotIsInstance(
            self.assertIsInstance(an_instance, object)
            #     src.classes.WPass(), object
            # )


    # Exceptions seen

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)


    # Exceptions seen

* I open a new terminal_, then add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_pass'

:ref:`I can make a class with pass<test_making_a_class_w_pass>`

----

*********************************************************************************
test_making_a_class_w_parentheses
*********************************************************************************


I can also make a :ref:`class<what is a class?>` with parentheses/brackets ``( )``.

----

=================================================================================
:red:`RED`: make it red
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add another test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-9

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

        def test_making_a_class_w_parentheses(self):
            assert not isinstance(
                src.classes.WParentheses(), object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes'
                    has no attribute 'WParentheses'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a class definition like ``WPass`` to ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    class WPass: pass


    class WParentheses: pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

  because the statement ``not isinstance(src.classes.WParentheses(), object)`` is :ref:`False<test_what_is_false>`

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-3

        def test_making_a_class_w_parentheses(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses(), object
            )


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add parentheses to the definition

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1-2
    :emphasize-text: ( )

    # class WParentheses: pass
    class WParentheses(): pass

  * the test is still green because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`
  * the :ref:`assertion<what is an assertion?>` - ``assert isinstance(src.classes.WParentheses(), object)`` checks if the result of a call to ``WParentheses`` in ``src.classes.py`` in the ``src`` folder_ also known as ``src.classes.WParentheses()``, is an :ref:`instance<how to test if something is an instance of a class>` of the :ref:`object class<what is a class?>` (the mother of all :ref:`classes<what is a class?>`)

  * this :ref:`class definition<how to make a class>` has parentheses after the name
  * the :ref:`class definition<how to make a class>` simply says pass_ and the test passes
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body)

* I remove the commented line

  .. code-block:: python
    :linenos:

    class WPass: pass


    class WParentheses(): pass

* I add the `assertNotIsInstance method`_ to :ref:`test_making_a_class_w_parentheses` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 6-8
    :emphasize-text: Not

        def test_making_a_class_w_parentheses(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses(), object
            )
            self.assertNotIsInstance(
                src.classes.WParentheses(), object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.WParentheses() object at 0xffffab123456>
        is an instance of <class 'object'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 6-7

        def test_making_a_class_w_parentheses(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WParentheses(), object
            )


    # Exceptions seen

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``src.classes.WParentheses()``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WParentheses(), object
            )


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WParentheses()``

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 4-6, 8-10

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            # assert not isinstance(
            assert isinstance(an_instance, object)
            #     src.classes.WParentheses(), object
            # )
            # self.assertNotIsInstance(
            self.assertIsInstance(an_instance, object)
            #     src.classes.WParentheses(), object
            # )


    # Exceptions seen

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 12

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_parentheses'

:ref:`I can make a class with parentheses<test_making_a_class_w_parentheses>`

I have two :ref:`classes<what is a class?>` with different statements, and the tests show that they are both instances of the :ref:`object class<what is a class?>`

.. code-block:: python

  class WPass: pass

.. code-block:: python

  class WParentheses(): pass

because ":ref:`all classes inherit from 'object'<test_making_a_class_w_object>`", which leads me to the next test.

----

*********************************************************************************
test_making_a_class_w_object
*********************************************************************************

I can make a :ref:`class<what is a class?>` with :ref:`object (the mother of all classes)<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a test with an :ref:`assertion<what is an assertion?>` for a new :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 6-9

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

        def test_making_a_class_w_object(self):
            assert not isinstance(
                src.classes.WObject(), object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'WObject'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the class definition to ``classes.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    class WParentheses(): pass


    class WObject(): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

* I change the statement of the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_object` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2-3

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject(), object
            )


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`object<what is a class?>` to the parentheses of the :ref:`class definition<how to make a class>` for ``WObject`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1-2
    :emphasize-text: object

    # class WObject(): pass
    class WObject(object): pass

  the test is still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    class WParentheses(): pass


    class WObject(object): pass

* I add an :ref:`assertion<what is an assertion?>` with the `assertNotIsInstance method`_ to :ref:`test_making_a_class_w_object` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-8

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject(), object
            )
            self.assertNotIsInstance(
                src.classes.WObject(), object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.WObject() object at 0xffffcd781234>
        is an instance of <class 'object'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-7

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WObject(), object
            )


    # Exceptions seen

  the test passes.

* I add a :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WObject()``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 2

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WObject(), object
            )


    # Exceptions seen

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WObject()``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4-6, 8-10

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            # assert not isinstance(
            assert isinstance(an_instance, object)
            #     src.classes.WObject(), object
            # )
            # self.assertNotIsInstance(
            self.assertIsInstance(an_instance, object)
            #     src.classes.WObject(), object
            # )


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 17

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_making_a_class_w_object'

I have three different :ref:`classes<what is a class?>`, and the tests show that they are all instances of the :ref:`object class<what is a class?>`

.. code-block:: python

  class WPass: pass

.. code-block:: python

  class WParentheses(): pass

.. code-block:: python

  class WObject(object): pass

their :ref:`definitions<how to make a class>` are different, their results are the same because ":ref:`all classes inherit from 'object'<test_making_a_class_w_object>`"

I like to write my :ref:`classes<what is a class?>` with ``(object)``, so that anyone can see what the parent :ref:`class<what is a class?>` is without thinking about it.

:ref:`I can make a class with object<test_making_a_class_w_object>`

----

*********************************************************************************
test_is_none_an_object
*********************************************************************************

I want to test if :ref:`None<what is None?>` is an :ref:`object.<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 6-7

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

        def test_is_none_an_object(self):
            assert not isinstance(None, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`None<what is None?>` is an :ref:`object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 2-3

      def test_is_none_an_object(self):
          # assert not isinstance(None, object)
          assert isinstance(None, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsInstance_ to show that :ref:`None<what is None?>` is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4

        def test_is_none_an_object(self):
            # assert not isinstance(None, object)
            assert isinstance(None, object)
            self.assertNotIsInstance(None, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError: None is an instance of <class 'object'>

  because :ref:`None<what is None?>` is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 4-5

        def test_is_none_an_object(self):
            # assert not isinstance(None, object)
            assert isinstance(None, object)
            # self.assertNotIsInstance(None, object)
            self.assertIsInstance(None, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

        def test_is_none_an_object(self):
            assert isinstance(None, object)
            self.assertIsInstance(None, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_an_object'

----

*********************************************************************************
test_is_a_boolean_an_object
*********************************************************************************

I want to test if a :ref:`boolean<what are booleans?>` is an :ref:`object.<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

---------------------------------------------------------------------------------
how to test if something is NOT a subclass of a class
---------------------------------------------------------------------------------

----

I can test if an :ref:`object<what is a class?>` is a :ref:`subclass (child) <what is a class?>` of another :ref:`object<what is a class?>` or NOT with the `issubclass built-in function`_ from `The Python Standard Library`_, it checks if the thing in the parentheses on the left is a :ref:`subclass<how to test if something is a subclass of a class>` of the :ref:`class<what is a class?>` on the right in the parentheses

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`bool<what are booleans?>` to show that :ref:`everything in Python is a child of object`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

        def test_is_none_an_object(self):
            assert isinstance(None, object)
            self.assertIsInstance(None, object)

        def test_is_a_boolean_an_object(self):
            assert not issubclass(bool, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`bool<what are booleans?>` is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

---------------------------------------------------------------------------------
how to test if something is a subclass of a class
---------------------------------------------------------------------------------

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 2-3

      def test_is_a_boolean_an_object(self):
          # assert not issubclass(bool, object)
          assert issubclass(bool, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The `unittest.TestCase class`_ has 2 :ref:`methods<what is a method?>` I can also use to test if an :ref:`object<what is a class?>` is a :ref:`subclass (child)<how to test if something is a subclass of a class>` of a :ref:`class<what is a class?>` or NOT - assertIsSubclass_ and assertNotIsSubclass_

----

---------------------------------------------------------------------------------
another way to test if something is NOT a subclass of a class
---------------------------------------------------------------------------------

----

I use `unittest.TestCase.assertNotIsSubclass`_ to show that :ref:`bool (the class for booleans)<what are booleans?>` is a :ref:`child of object<what is a class?>`

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 4

      def test_is_a_boolean_an_object(self):
          # assert not issubclass(bool, object)
          assert issubclass(bool, object)
          self.assertNotIsSubclass(bool, object)


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

.. code-block:: shell

  AssertionError:
      <class 'bool'> is a subclass of <class 'object'>

because :ref:`bool<what are booleans?>` is a :ref:`child of object<what is a class?>`.

----

---------------------------------------------------------------------------------
another way to test if something is a subclass of a class
---------------------------------------------------------------------------------

----

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4-5

        def test_is_a_boolean_an_object(self):
            # assert not issubclass(bool, object)
            assert issubclass(bool, object)
            # self.assertNotIsSubclass(bool, object)
            self.assertIsSubclass(bool, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 26

        def test_is_a_boolean_an_object(self):
            assert issubclass(bool, object)
            self.assertIsSubclass(bool, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_a_boolean_an_object'

:ref:`A boolean is an object.<test_is_a_boolean_an_object>`

----

*********************************************************************************
test_is_an_integer_an_object
*********************************************************************************

I want to test if an integer_ (a whole number without decimals) is an :ref:`object<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for int_ (the :ref:`class<what is a class?>` for whole numbers without decimals), to show that everything in Python_ is a :ref:`child of object.<what is a class?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5-6

        def test_is_a_boolean_an_object(self):
            assert issubclass(bool, object)
            self.assertIsSubclass(bool, object)

        def test_is_an_integer_an_object(self):
            assert not issubclass(int, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because int_ is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 30
  :emphasize-lines: 2-3

      def test_is_an_integer_an_object(self):
          # assert not issubclass(int, object)
          assert issubclass(int, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsSubclass_ to show that int_ is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4

        def test_is_an_integer_an_object(self):
            # assert not issubclass(int, object)
            assert issubclass(int, object)
            self.assertNotIsSubclass(int, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'int'> is a subclass of <class 'object'>

  because int_ is a :ref:`child of object<what is a class?>`.

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 4-5

        def test_is_an_integer_an_object(self):
            # assert not issubclass(int, object)
            assert issubclass(int, object)
            # self.assertNotIsSubclass(int, object)
            self.assertIsSubclass(int, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 30

        def test_is_an_integer_an_object(self):
            assert issubclass(int, object)
            self.assertIsSubclass(int, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_an_integer_an_object'

:ref:`An integer is an object.<test_is_an_integer_an_object>`

----

*********************************************************************************
test_is_a_float_an_object
*********************************************************************************

I want to test if a float_ (a binary floating point decimal number) is an :ref:`object<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for float_ (the :ref:`class<what is a class?>` for binary floating point decimal numbers), to show that everything in Python_ is a :ref:`child of object.<what is a class?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

        def test_is_an_integer_an_object(self):
            assert issubclass(int, object)
            self.assertIsSubclass(int, object)

        def test_is_a_float_an_object(self):
            assert not issubclass(float, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because float_ is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 2-3

      def test_is_a_float_an_object(self):
          # assert not issubclass(float, object)
          assert issubclass(float, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsSubclass_ to show that float_ is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4

        def test_is_a_float_an_object(self):
            # assert not issubclass(float, object)
            assert issubclass(float, object)
            self.assertNotIsSubclass(float, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'float'> is a subclass of <class 'object'>

  because float_ is a :ref:`child of object<what is a class?>`.

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-5

        def test_is_a_float_an_object(self):
            # assert not issubclass(float, object)
            assert issubclass(float, object)
            # self.assertNotIsSubclass(float, object)
            self.assertIsSubclass(float, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 34

        def test_is_a_float_an_object(self):
            assert issubclass(float, object)
            self.assertIsSubclass(float, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_a_float_an_object'

:ref:`A float is an object.<test_is_a_float_an_object>`

----

*********************************************************************************
test_is_a_string_an_object
*********************************************************************************

I want to test if a string_ (anything in :ref:`quotes`) is an :ref:`object.<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for str_ (the :ref:`class<what is a class?>` for anything in :ref:`quotes`), to show that :ref:`everything in Python is a child of object`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6

        def test_is_a_float_an_object(self):
            assert issubclass(float, object)
            self.assertIsSubclass(float, object)

        def test_is_a_string_an_object(self):
            assert not issubclass(str, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because str_ is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 38
  :emphasize-lines: 2-3

      def test_is_a_string_an_object(self):
          # assert not issubclass(str, object)
          assert issubclass(str, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsSubclass_ to show that str_ is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4

        def test_is_a_string_an_object(self):
            # assert not issubclass(str, object)
            assert issubclass(str, object)
            self.assertNotIsSubclass(str, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'str'> is a subclass of <class 'object'>

  because str_ is a :ref:`child of object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4-5

        def test_is_a_string_an_object(self):
            # assert not issubclass(str, object)
            assert issubclass(str, object)
            # self.assertNotIsSubclass(str, object)
            self.assertIsSubclass(str, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 38

        def test_is_a_string_an_object(self):
            assert issubclass(str, object)
            self.assertIsSubclass(str, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_a_string_an_object'

:ref:`A float is an object.<test_is_a_float_an_object>`

----

*********************************************************************************
test_is_a_tuple_an_object
*********************************************************************************

I want to test if a tuple_ (anything in parentheses ``( )`` separated by a comma) is an :ref:`object.<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for tuple_ (the :ref:`class<what is a class?>` for anything in parentheses ``( )`` separated by a comma), to show that :ref:`everything in Python is a child of object`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-6

        def test_is_a_string_an_object(self):
            assert issubclass(str, object)
            self.assertIsSubclass(str, object)

        def test_is_a_tuple_an_object(self):
            assert not issubclass(tuple, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because tuple_ is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 42
  :emphasize-lines: 2-3

      def test_is_a_tuple_an_object(self):
          # assert not issubclass(tuple, object)
          assert issubclass(tuple, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsSubclass_ to show that tuple_ is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4

        def test_is_a_tuple_an_object(self):
            # assert not issubclass(tuple, object)
            assert issubclass(tuple, object)
            self.assertNotIsSubclass(tuple, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'tuple'> is a subclass of <class 'object'>

  because tuple_ is a :ref:`child of object<what is a class?>`.

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4-5

        def test_is_a_tuple_an_object(self):
            # assert not issubclass(tuple, object)
            assert issubclass(tuple, object)
            # self.assertNotIsSubclass(tuple, object)
            self.assertIsSubclass(tuple, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 42

        def test_is_a_tuple_an_object(self):
            assert issubclass(tuple, object)
            self.assertIsSubclass(tuple, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_a_tuple_an_object'

:ref:`A tuple is an object.<test_is_a_tuple_an_object>`

----

*********************************************************************************
test_is_a_list_an_object
*********************************************************************************

I want to test if :ref:`a list<what is a list?>` (anything in square brackets ``[ ]``) is an :ref:`object<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`list (the class for anything in square brackets '[ ]')<what is a list?>`, to show that :ref:`everything in Python is a child of object`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 5-6

        def test_is_a_tuple_an_object(self):
            assert issubclass(tuple, object)
            self.assertIsSubclass(tuple, object)

        def test_is_a_list_an_object(self):
            assert not issubclass(list, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`list<what is a list?>` is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 46
  :emphasize-lines: 2-3

        def test_is_a_list_an_object(self):
            # assert not issubclass(list, object)
            assert issubclass(list, object)


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsSubclass_ to show that :ref:`list<what is a list?>` is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4

        def test_is_a_list_an_object(self):
            # assert not issubclass(list, object)
            assert issubclass(list, object)
            self.assertNotIsSubclass(list, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'list'> is a subclass of <class 'object'>

  because :ref:`list<what is a list?>` is a :ref:`child of object<what is a class?>`.

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 4-5

        def test_is_a_list_an_object(self):
            # assert not issubclass(list, object)
            assert issubclass(list, object)
            # self.assertNotIsSubclass(list, object)
            self.assertIsSubclass(list, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 46

        def test_is_a_list_an_object(self):
            assert issubclass(list, object)
            self.assertIsSubclass(list, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_a_list_an_object'

:ref:`A list is an object.<test_is_a_list_an_object>`

----

*********************************************************************************
test_is_a_set_an_object
*********************************************************************************

I want to test if a set_ (anything in curly braces ``{ }`` separated by a comma) is an :ref:`object.<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for set_ (the :ref:`class<what is a class?>` for anything in curly braces ``{ }`` separated by a comma), to show that :ref:`everything in Python is a child of object`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5-6

        def test_is_a_list_an_object(self):
            assert issubclass(list, object)
            self.assertIsSubclass(list, object)

        def test_is_a_set_an_object(self):
            assert not issubclass(set, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because set_ is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 50
  :emphasize-lines: 2-3

      def test_is_a_set_an_object(self):
          # assert not issubclass(set, object)
          assert issubclass(set, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I use assertNotIsSubclass_ to show that set_ is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4

        def test_is_a_set_an_object(self):
            # assert not issubclass(set, object)
            assert issubclass(set, object)
            self.assertNotIsSubclass(set, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'set'> is a subclass of <class 'object'>

  because set_ is a :ref:`child of object<what is a class?>`.

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4-5

        def test_is_a_set_an_object(self):
            # assert not issubclass(set, object)
            assert issubclass(set, object)
            # self.assertNotIsSubclass(set, object)
            self.assertIsSubclass(set, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 50

        def test_is_a_set_an_object(self):
            assert issubclass(set, object)
            self.assertIsSubclass(set, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_a_set_an_object'

:ref:`A set is an object.<test_is_a_set_an_object>`

----

*********************************************************************************
test_is_a_dictionary_an_object
*********************************************************************************

I want to test if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) is an :ref:`object.<what is a class?>`

----

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`dict (the class for any key-value pairs in curly braces '{ }' separated by a comma)<what is a dictionary?>`, to show that :ref:`everything in Python is a child of object`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 6

        def test_is_a_set_an_object(self):
            assert issubclass(set, object)
            self.assertIsSubclass(set, object)

        def test_is_a_dictionary_an_object(self):
            assert not issubclass(dict, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`dict<what is a dictionary?>` is a :ref:`child of object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 2-3

        def test_is_a_dictionary_an_object(self):
            # assert not issubclass(dict, object)
            assert issubclass(dict, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsSubclass_ to show that :ref:`dict<what is a dictionary?>` is a :ref:`child of object<what is a class?>`

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 4

        def test_is_a_dictionary_an_object(self):
            # assert not issubclass(dict, object)
            assert issubclass(dict, object)
            self.assertNotIsSubclass(dict, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'dict'> is a subclass of <class 'object'>

  because :ref:`dict<what is a dictionary?>` is a :ref:`child of object<what is a class?>`.

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 3-4

            # assert not isinstance(dict, object)
            assert isinstance(dict, object)
            # self.assertNotIsInstance(dict, object)
            self.assertIsInstance(dict, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 54

        def test_is_a_dictionary_an_object(self):
            assert issubclass(dict, object)
            self.assertIsSubclass(dict, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_a_dictionary_an_object'

:ref:`A dictionary is an object.<test_is_a_dictionary_an_object>`

----

*********************************************************************************
test_attributes_and_methods_of_objects
*********************************************************************************

In :ref:`test_attributes_and_methods_of_person_class` I saw the :ref:`methods<what is a method?>` I added to the ``Person`` :ref:`class<what is a class?>` and also names that I did not add, which led to the question of where they came from.

I want to test the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`object class<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test to ``test_classes.py``

  .. code-block:: python
    :lineno-start: 54
    :emphasize-lines: 5-8

        def test_is_a_dictionary_an_object(self):
            assert issubclass(dict, object)
            self.assertIsSubclass(dict, object)

        def test_attributes_and_methods_of_objects(self):
            reality = dir(object)
            my_expectation = []
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__class__', '__delattr__', '__dir__', '_[272 chars]k__']
     != []

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-7

        def test_attributes_and_methods_of_objects(self):
            reality = dir(object)
            # my_expectation = []
            my_expectation = [
                '__class__', '__delattr__', '__dir__',
                '_[272 chars]k__'
            ]
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__c[32 chars]', '__doc__', '__eq__',
         '__format__', '__ge__'[231 chars]k__']
     != ['__c[32 chars]', '_[272 chars]k__']

  it shows me the entire :ref:`list<what is a list?>` below the message

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 4-31
    :emphasize-text: __init__

        def test_attributes_and_methods_of_objects(self):
            reality = dir(object)
            # my_expectation = []
            # my_expectation = [
            #     '__class__', '__delattr__', '__dir__',
            #     '_[272 chars]k__'
            # ]
            my_expectation = E       - ['__class__',
    E       -  '__delattr__',
    E       -  '__dir__',
    E       -  '__doc__',
    E       -  '__eq__',
    E       -  '__format__',
    E       -  '__ge__',
    E       -  '__getattribute__',
    E       -  '__getstate__',
    E       -  '__gt__',
    E       -  '__hash__',
    E       -  '__init__',
    E       -  '__init_subclass__',
    E       -  '__le__',
    E       -  '__lt__',
    E       -  '__ne__',
    E       -  '__new__',
    E       -  '__reduce__',
    E       -  '__reduce_ex__',
    E       -  '__repr__',
    E       -  '__setattr__',
    E       -  '__sizeof__',
    E       -  '__str__',
    E       -  '__subclasshook__']
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'E' is not defined

* I use the ``find and replace`` feature of the `Integrated Development Environment (IDE)`_ to remove the extra characters, then remove the commented lines

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-28
    :emphasize-text: __init__

        def test_attributes_and_methods_of_objects(self):
            reality = dir(object)
            my_expectation = [
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
            self.assertEqual(reality, my_expectation)


    # Exceptions seen

  the test passes. All :ref:`classes<what is a class?>` automatically get these attributes, they inherit them because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

  The ``__init__`` :ref:`method<what is a method?>` is also inherited which means when I defined it in :ref:`test_classy_person_says_hello` I overwrote the inherited one.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attributes_and_methods_of_objects'

:ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

----

*********************************************************************************
test_making_a_class_w_inheritance
*********************************************************************************

I can make :ref:`classes<what is a class?>` with inheritance by stating the parent :ref:`class<what is a class?>`

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a new test

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 6-8

                '__str__',
                '__subclasshook__'
            ]
            self.assertEqual(reality, my_expectation)

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            assert isinstance(a_class, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Doe'

  because there is no definition for ``Doe`` in ``classes.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class<what is a class?>` definition to ``classes.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

    class WObject(object): pass


    class Doe(object): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

  because

  - ``doe`` is just a name for the ``Doe`` :ref:`class<what is a class?>`
  - ``Doe`` and ``Person`` are children of :ref:`object<what is a class?>`

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_inheritance` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)


    # Exceptions seen

  the test passes. ``Doe`` is not an :ref:`instance<how to test if something is an instance of a class>` of the ``Person`` :ref:`class.<what is a class?>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to the `assertIsInstance method`_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 5

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            self.assertIsInstance(a_class, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Doe'> is not
        an instance of <class 'src.person.Person'>

* I change assertIsInstance_ to assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 5-8

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )


    # Exceptions seen

  the test passes.

* I use the `issubclass built-in function`_ to test if ``Doe`` is a child of ``Person``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 9

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert

  because ``Doe`` is not a child of ``Person``, yet.

* I change the parent of ``Doe`` from ``object`` to ``Person`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1-2

    # class Doe(object): pass
    class Doe(person.Person): pass

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

  because there is no definition for ``person`` in ``classes.py``

* I add an `import statement`_ at the top of ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import person


    class WPass: pass

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    E   ModuleNotFoundError: No module named 'person'

  because the test cannot find ``person.py`` in the main project folder_ where I run the tests from, so it cannot import the :ref:`Module<what is a module?>`

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 99
    :emphasize-lines: 5
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # ModuleNotFoundError

* I change the `import statement`_ so the path to ``person.py`` from the main project folder_ is correct, in ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # import person
    import src.person


    class WPass: pass

  the terminal_ does not feel like my friend, it goes back to :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

* I add ``src.`` to the parent of ``Doe``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-3

    # class Doe(object): pass
    # class Doe(person.Person): pass
    class Doe(src.person.Person): pass

  - the test passes because ``Doe`` is now a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Person``.
  - ``import src.person`` brings in an :ref:`object<what is a class?>` that represents the ``person.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``classes.py``.
  - I have to use ``src.person.Person`` in ``classes.py`` because I am testing from the root folder_ of the project.
  - The test needs to know where ``person.py`` is in relation to where I ran the tests from.
  - This is a problem because if ``classes.py`` is run from inside ``src`` the `import statement`_ will not be able to find ``src.person`` from inside ``src``. Same thing if I run the tests from inside ``tests``. That is a problem for another time.

* I add the `assertNotIsSubclass method`_ to :ref:`test_making_a_class_w_inheritance` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 10-12

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            self.assertNotIsSubclass(
                a_class, src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Doe'> is a
        subclass of <class 'src.person.Person'>

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 10-11

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                a_class, src.person.Person
            )


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to show that ``a_class`` which points to ``Doe`` is just a name for the :ref:`class<what is a class?>` not an :ref:`instance<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 14

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                a_class, src.person.Person
            )
            assert isinstance(a_class, a_class)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert False

  because a :ref:`class<what is a class?>` is not an :ref:`instance<how to test if something is an instance of a class>`

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 14-15


        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                a_class, src.person.Person
            )
            # assert isinstance(a_class, a_class)
            assert not isinstance(a_class, a_class)


    # Exceptions seen

  the test passes.

* I add assertIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 16

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                a_class, src.person.Person
            )
            # assert isinstance(a_class, a_class)
            assert not isinstance(a_class, a_class)
            self.assertIsInstance(a_class, a_class)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Doe'> is not
        an instance of <class 'src.classes.Doe'>

  because a :ref:`class<what is a class?>` is not an :ref:`instance<how to test if something is an instance of a class>`

* I change assertIsInstance_ to assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 16-17

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                a_class, src.person.Person
            )
            # assert isinstance(a_class, a_class)
            assert not isinstance(a_class, a_class)
            # self.assertIsInstance(a_class, a_class)
            self.assertNotIsInstance(a_class, a_class)


    # Exceptions seen

----

=================================================================================
what is the difference between an instance and a class?
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`, this time with an :ref:`instance<how to test if something is an instance of a class>` of ``Doe``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 19-22

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert issubclass(a_class, src.person.Person)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                a_class, src.person.Person
            )
            # assert isinstance(a_class, a_class)
            assert not isinstance(a_class, a_class)
            # self.assertIsInstance(a_class, a_class)
            self.assertNotIsInstance(a_class, a_class)

            an_instance = src.classes.Doe()
            assert not isinstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` takes one required argument for ``first_name`` and I called ``Doe`` to make an :ref:`instance<how to test if something is an instance of a class>`. How did ``Person.__init__`` get called?

----

=================================================================================
what happens when the child calls the parent?
=================================================================================

----

* Here is what is happens when ``an_instance = src.class.Doe()`` runs

  .. code-block:: python

    an_instance = src.classes.Doe()
                  Doe # has no __init__, call Person
                  Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>`

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 6
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # ModuleNotFoundError
    # TypeError

----

=================================================================================
how to call the parent from the child
=================================================================================

----

* I add the `super built-in function`_ to ``Doe`` to call the parent (``Person``) ``__init__`` :ref:`method<what is a method?>` directly, in ``classes.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4, 6-7

    # class Doe(object): pass
    # class Doe(person.Person): pass
    # class Doe(src.person.Person): pass
    class Doe(src.person.Person):

        def __init__(self):
            super().__init__()

  - the terminal_ still shows :ref:`TypeError<what causes TypeError?>`
  - the `super built-in function`_ calls the ``__init__`` :ref:`method<what is a method?>` of the parent :ref:`class<what is a class?>`

* I add a value to ``src.classes.Doe`` in :ref:`test_making_a_class_w_inheritance` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 1-2

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('first_name')
            assert not isinstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe.__init__() takes
               1 positional argument but 2 were given

  because this happens when ``an_instance = src.classes.Doe('first_name')`` runs

  .. code-block:: python

    an_instance = src.classes.Doe('first_name')
                  Doe.__init__('first_name')

  which raises :ref:`TypeError<what causes TypeError?>` because the definition for the ``__init__`` :ref:`method<what is a method?>` in ``Doe`` only takes one :ref:`positional argument<test_w_positional_arguments>` (``self``) and it was called with two (``self`` and ``first_name``)

* I add a parameter for ``first_name`` to the ``__init__`` :ref:`method<what is a method?>` of ``Doe`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 6-7

    # class Doe(object): pass
    # class Doe(person.Person): pass
    # class Doe(src.person.Person): pass
    class Doe(src.person.Person):

        # def __init__(self):
        def __init__(self, first_name):
            super().__init__()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``an_instance = src.classes.Doe('first_name')`` runs

  .. code-block:: python

    an_instance = src.classes.Doe('first_name')
                  Doe.__init__('first_name')
                      super().__init__()
                  Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>`

* I add the required parameter to ``super().__init__()`` in ``Doe``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 8-9

    # class Doe(object): pass
    # class Doe(person.Person): pass
    # class Doe(src.person.Person): pass
    class Doe(src.person.Person):

        # def __init__(self):
        def __init__(self, first_name):
            # super().__init__()
            super().__init__(first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

  because

  - an instance of ``Doe`` is an instance of ``Person``
  - ``Person`` is the parent of ``Doe``
  - the test shows that this happens when ``an_instance = src.classes.Doe('first_name')`` runs

    .. code-block:: python

      an_instance = src.classes.Doe('first_name')
                    Doe.__init__('first_name')
                        super().__init__('first_name')
                    Person.__init__('first_name')

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_inheritance` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3-4

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('first_name')
            # assert not isinstance(
            assert isinstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the test passes.

* I add a call to the `assertNotIsInstance method`_

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 7-9

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('first_name')
            # assert not isinstance(
            assert isinstance(
                an_instance, src.person.Person
            )
            self.assertNotIsInstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Doe object at 0xffff01a2bc34> is
        an instance of <class 'src.person.Person'>

  because an instance of ``Doe`` is an instance of ``Person``

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 7-8

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('first_name')
            # assert not isinstance(
            assert isinstance(
                an_instance, src.person.Person
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the test passes.

* I add a test for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the ``Doe`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 12-15

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('first_name')
            # assert not isinstance(
            assert isinstance(
                an_instance, src.person.Person
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                an_instance, src.person.Person
            )

            self.assertEqual(
                dir(a_class),
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__class__', '__delattr__', '__dict__',
         '[370 chars]llo']
     != []

* I change the expectation to the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the ``Person`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 3-4

            self.assertEqual(
                dir(a_class),
                # []
                dir(src.person.Person)
            )


    # Exceptions seen

  the test passes because ``Doe`` has the same :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` as ``Person`` because ``Doe`` is a child of ``Parent``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 88

        def test_making_a_class_w_inheritance(self):
            a_class = src.classes.Doe

            assert not isinstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )

            assert issubclass(a_class, src.person.Person)
            self.assertIsSubclass(
                a_class, src.person.Person
            )

            assert not isinstance(a_class, a_class)
            self.assertNotIsInstance(a_class, a_class)

            an_instance = src.classes.Doe('first_name')
            assert isinstance(
                an_instance, src.person.Person
            )
            self.assertIsInstance(
                an_instance, src.person.Person
            )

            self.assertEqual(
                dir(a_class),
                dir(src.person.Person)
            )


    # Exceptions seen

* I remove the commented lines from ``classes.py``

  .. code-block:: python
    :linenos:

    import src.person


    class WPass: pass


    class WParentheses(): pass


    class WObject(object): pass


    class Doe(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name)

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_inheritance'

:ref:`I can make a class with inheritance.<test_making_a_class_w_inheritance>`

----

*********************************************************************************
test_classes_w_one_parent
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add a new test for Inheritance_ with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 6-8

            self.assertEqual(
                dir(a_class),
                dir(src.person.Person)
            )

        def test_classes_w_one_parent(self):
            doe = src.classes.Doe('doe')
            self.assertEqual(doe.last_name, '')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 117
  :emphasize-lines: 3-4

      def test_classes_w_one_parent(self):
          doe = src.classes.Doe('doe')
          # self.assertEqual(doe.last_name, '')
          self.assertEqual(doe.last_name, 'doe')


  # Exceptions seen

the test passes because this happens when ``doe = src.classes.Doe('doe')`` runs

.. code-block:: python

  doe = src.classes.Doe('doe')
        Doe.__init__('doe')
            super().__init__(first_name)
        Person.__init__('first_name')
            Person.__init__('first_name', last_name='doe')
            self.last_name = 'doe' # use the default value

the value for ``doe.last_name`` is ``doe`` because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_w_optional_arguments>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 6-7
    :emphasize-text: joe

        def test_classes_w_one_parent(self):
            doe = src.classes.Doe('doe')
            # self.assertEqual(doe.last_name, '')
            self.assertEqual(doe.last_name, 'doe')

            joe = src.classes.Doe('joe')
            self.assertEqual(joe.last_name, 'blow')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add a new :ref:`class definition<how to make a class>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 7

    class Doe(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name)


    class Blow(src.person.Person): pass

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change ``joe`` to use the new ``Blow`` :ref:`class<what is a class?>`, in :ref:`test_classes_w_one_parent` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 1-2
    :emphasize-text: joe Blow

            # joe = src.classes.Doe('joe')
            joe = src.classes.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')


    # Exceptions seen

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I add a :ref:`class attribute<what is a class attribute?>` for ``last_name`` in the ``Blow`` :ref:`class<what is a class?>` in ``classes.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 1-2, 4

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        last_name = 'blow'

  the terminal_ does not feel like my friend, it still shows :ref:`AssertionError<what causes AssertionError?>`

* I add the ``__init__`` :ref:`method<what is a method?>` to customize the last name

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4, 6-7

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        # last_name = 'blow'

        def __init__(self):
            self.last_name = 'blow'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Blow.__init__() takes
               1 positional argument but 2 were given

  because this happens when ``joe = src.classes.Blow('joe')`` runs

  .. code-block:: python

    joe = src.classes.Blow('joe')
          Blow.__init__('joe')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` o of ``Blow`` only takes one :ref:`positional argument<test_w_positional_arguments>` (``self``) and it got called with two (``self`` and ``first_name``)

* I add ``first_name`` to the parentheses for the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6-7

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        # last_name = 'blow'

        # def __init__(self):
        def __init__(self, first_name):
            self.last_name = 'blow'

  the test passes because this happens when ``joe = src.classes.Blow('joe')`` runs

  .. code-block:: python

    joe = src.classes.Blow('joe')
          Blow.__init__('joe')
              self.last_name = 'joe'

  I can define :ref:`classes<what is a class?>` that are related and have their own defaults. In this test

  - the ``Doe`` :ref:`class<what is a class?>` has a default ``last_name`` that is the same as the default last name for ``Person``
  - the ``Blow`` :ref:`class<what is a class?>` has a different default ``last_name``
  - ``Doe`` and ``Blow`` are :ref:`children (subclasses)<how to test if something is a subclass of a class>` of ``Person``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 13

    class Doe(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name)


    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'blow'

* In this case there is a simpler way to make ``joe`` and ``doe``. I could directly pass the values to the ``Person`` :ref:`class<what is a class?>` since all the ``Blow`` :ref:`class<what is a class?>` does is customize the ``last_name`` :ref:`attribute<what is a class attribute?>`, there is nothing special about it or the ``Doe`` :ref:`class<what is a class?>`. I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_one_parent` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 122
    :emphasize-lines: 5-6
    :emphasize-text: person

            # joe = src.classes.Doe('joe')
            joe = src.classes.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')

            blow = src.person.Person('joe')
            self.assertEqual(blow.last_name, joe.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add ``last_name='blow'`` to the call

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 1-2

            # blow = src.person.Person('joe')
            blow = src.person.Person('joe', last_name='blow')
            self.assertEqual(blow.last_name, joe.last_name)


    # Exceptions seen

  the test passes. I can make instances of :ref:`classes<what is a class?>` by customizing its :ref:`attributes<what is a class attribute?>` without having to make a new :ref:`class<what is a class?>`.

* I add an :ref:`assertion<what is an assertion?>` for ``jane``

  .. code-block:: python
    :lineno-start: 126
    :emphasize-lines: 5-6

            # blow = src.person.Person('joe')
            blow = src.person.Person('joe', last_name='blow')
            self.assertEqual(blow.last_name, joe.last_name)

            jane = src.person.Person('jane')
            self.assertEqual(jane.last_name, blow.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I change the expectation

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 2-3

            jane = src.person.Person('jane')
            # self.assertEqual(jane.last_name, blow.last_name)
            self.assertEqual(jane.last_name, doe.last_name)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``john``

  .. code-block:: python
    :lineno-start: 130
    :emphasize-lines: 5-6

            jane = src.person.Person('jane')
            # self.assertEqual(jane.last_name, blow.last_name)
            self.assertEqual(jane.last_name, doe.last_name)

            john = src.classes.Smith('john')
            self.assertEqual(john.last_name, 'smith')


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Smith'

* I add a :ref:`class definition<how to make a class>` for ``Smith`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 7

    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'blow'


    class Smith(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'smith'

  because this happens when ``john = src.classes.Smith('john')`` runs

  .. code-block:: python

    john = src.classes.Smith('john')
           Smith # Smith has no __init__, call Person
           Person.__init__('john')
               Person.__init__('john', last_name='doe')
               self.last_name = 'doe' # use the default value

* I add the ``__init__`` :ref:`method<what is a method?>` in ``Smith``

  .. code-block:: Python
    :lineno-start: 25
    :emphasize-lines: 1-2, 4-5

    # class Smith(src.person.Person): pass
    class Smith(src.person.Person):

        def __init__(self):
            self.last_name = 'smith'

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Smith.__init__() takes 1
               positional argument but 2 were given

  because this happens when ``john = src.classes.Smith('john')`` runs

  .. code-block:: python

    john = src.classes.Smith('john')
           Smith.__init__('john')

  the definition for the ``__init__`` :ref:`method<what is a method?>` only allows one input (``self``) and it got called with two (``self`` and ``first_name``)

* I add ``first_name`` in parentheses

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4-5

    # class Smith(src.person.Person): pass
    class Smith(src.person.Person):

        # def __init__(self):
        def __init__(self, first_name):
            self.last_name = 'smith'

  the test passes because this happens when ``john = src.classes.Smith('john')`` runs

  .. code-block:: python

    john = src.classes.Smith('john')
           Smith.__init__('john')
           self.last_name = 'smith'

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 19

    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'blow'


    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'smith'

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_one_parent` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 134
    :emphasize-lines: 4-5
    :emphasize-text: person

            john = src.classes.Smith('john')
            self.assertEqual(john.last_name, 'smith')

            smith = src.person.Person('john', 'smith')
            self.assertEqual(smith.last_name, doe.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != 'doe'

* I change the expectation

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 2-3

            smith = src.person.Person('john', 'smith')
            # self.assertEqual(smith.last_name, doe.last_name)
            self.assertEqual(smith.last_name, john.last_name)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 112

        def test_classes_w_one_parent(self):
            doe = src.classes.Doe('doe')
            self.assertEqual(doe.last_name, 'doe')

            joe = src.classes.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')

            blow = src.person.Person('joe', last_name='blow')
            self.assertEqual(blow.last_name, joe.last_name)

            jane = src.person.Person('jane')
            self.assertEqual(jane.last_name, doe.last_name)

            john = src.classes.Smith('john')
            self.assertEqual(john.last_name, 'smith')

            smith = src.person.Person('john', 'smith')
            self.assertEqual(smith.last_name, john.last_name)


    # Exceptions seen

  * this happens when an :ref:`instance<how to test if something is an instance of a class>` of ``Doe`` is made

    .. code-block:: python

      instance = src.classes.Doe('first_name')
                 Doe.__init__('first_name')
                 super().__init__(first_name)
                 Person.__init__('first_name')
                 Person.__init__('first_name', last_name='doe')
                 self.last_name = 'doe' # use the default value

  * this happens when an :ref:`instance<how to test if something is an instance of a class>` of ``Smith`` and ``Blow`` are made

    .. code-block:: python

      instance = src.classes.ClassName('first_name')
                 ClassName.__init__('first_name')
                 self.last_name = 'last_name'


  * this happens when instances of the ``Person`` :ref:`class<what is a class?>` are made

    .. code-block:: python

      instance = src.person.Person(first_name, last_name=last_name)
                 Person.__init__(first_name, last_name=last_name)
                 self.first_name = first_name
                 self.last_name = last_name

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_classes_w_one_parent'

:ref:`I can customize child classes with the __init__ method<test_classes_w_one_parent>`

----

*********************************************************************************
test_classes_w_multiple_parents
*********************************************************************************

Can a :ref:`class<what is a class?>` have more than one parent?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for ``jane``

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 4-6
    :emphasize-text: Jane

            smith = src.person.Person('john', 'smith')
            self.assertEqual(smith.last_name, john.last_name)

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Jane'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class<what is a class?>` for ``Jane`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'smith'


    class Jane(src.person.Person): pass

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``jane = src.classes.Jane()`` runs

  .. code-block:: python

    jane = src.classes.Jane()
           Jane # Jane has no __init__, call Person
           Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Person`` requires one positional argument (``first_name``) and it got called with zero

* I add the ``__init__`` :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``Jane``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 1-2, 4-5

    # class Jane(src.person.Person): pass
    class Jane(src.person.Person):

        def __init__(self):
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Jane' object has no attribute 'first_name'

* I add a value for ``first_name`` to the :ref:`definition<how to make a class>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 5

    # class Jane(src.person.Person): pass
    class Jane(src.person.Person):

        def __init__(self):
            self.first_name = 'jane'
            return None

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``jane`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 4

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Jane' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add a value for ``last_name`` to ``Jane`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6

    # class Jane(src.person.Person): pass
    class Jane(src.person.Person):

        def __init__(self):
            self.first_name = 'jane'
            self.last_name = 'doe'
            return None

  the test passes. This is a repetition because

  - the :ref:`default value<test_w_optional_arguments>` for ``Person`` is ``doe``
  - ``Jane`` is a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Person``

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_multiple_parents` to make sure ``Jane`` is a ``Doe``, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 5-7

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsSubclass(
                src.classes.Jane, src.classes.Doe
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Jane'> is not
        a subclass of <class 'src.classes.Doe'>

* I change the parent of ``Jane`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2-3

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        def __init__(self):
            self.first_name = 'jane'
            self.last_name = 'doe'
            return None

  the test passes

* I add a call to the `super built-in function`_ to use to remove the repetition of ``last_name``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-8

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        def __init__(self):
            super().__init__()
            # self.first_name = 'jane'
            # self.last_name = 'doe'
            return None

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``jane = src.classes.Jane()`` runs

  .. code-block:: python

    jane = src.classes.Jane()
           Jane.__init__()
               super().__init__()
           Doe.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Doe`` requires two positional arguments (``self`` and ``first_name``) and it got called with one (``self``)

* I add ``jane`` as the value for ``first_name`` in the call to the parent

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-7

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        def __init__(self):
            # super().__init__()
            super().__init__('jane')
            # self.first_name = 'jane'
            # self.last_name = 'doe'
            return None

  the test is green again because this happens when ``jane = src.classes.Jane()`` runs

  .. code-block:: python

    jane = src.classes.Jane()
           Jane.__init__()
               super().__init__('jane')
           Doe.__init__('jane')
               super().__init__(first_name)
           Person.__init__('jane')
               Person.__init__('jane', last_name='doe')
               self.first_name = 'jane'
               self.last_name = 'doe' # use the default value

* I add an :ref:`assertion<what is an assertion?>` for ``mary``, another instance of ``Jane`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 9-10

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsSubclass(
                src.classes.Jane, src.classes.Doe
            )

            mary = src.classes.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Jane.__init__() takes 1
               positional argument but 2 were given

  because this happens when ``mary = src.classes.Jane('mary')`` runs

  .. code-block:: python

    mary = src.classes.Jane('mary')
           Jane.__init__('mary')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` takes one :ref:`positional argument<test_w_positional_arguments>` (``self``) and it was called with two (``self`` and ``'mary'``)

* I add ``first_name`` to the parentheses for the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        # def __init__(self):
        def __init__(self, first_name):
            # super().__init__()
            super().__init__('jane')
            # self.first_name = 'jane'
            # self.last_name = 'doe'
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Jane.__init__() missing 1
               required positional argument: 'first_name'

  I broke the :ref:`assertion<what is an assertion?>` for ``jane`` because this happens when ``jane = src.classes.Jane()`` runs

  .. code-block:: python

    jane = src.classes.Jane()
           Jane.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` takes two required :ref:`positional arguments<test_w_positional_arguments>` (``self`` and ``first_name``) and the call only sends one (``self``)

* I add a :ref:`default value<test_w_optional_arguments>` to make ``first_name`` optional

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6-7

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        # def __init__(self):
        # def __init__(self, first_name):
        def __init__(self, first_name='jane'):
            # super().__init__()
            super().__init__('jane')
            # self.first_name = 'jane'
            # self.last_name = 'doe'
            return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'jane' != 'mary'

  because this happens when ``mary = src.classes.Jane('mary')`` runs

  .. code-block:: python
    :emphasize-lines: jane

    mary = src.classes.Jane('mary')
           Jane.__init__('mary')
               super().__init__('jane')
           Doe.__init__('jane')
               super().__init__(first_name)
           Person.__init__('jane')
               Person.__init__('jane', last_name='doe')
               self.first_name = 'jane'
               self.last_name = 'doe'

* I change the call to the `super built-in function`_ to use the name instead of a fixed value

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 9-10

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        # def __init__(self):
        # def __init__(self, first_name):
        def __init__(self, first_name='jane'):
            # super().__init__()
            # super().__init__('jane')
            super().__init__(first_name)
            # self.first_name = 'jane'
            # self.last_name = 'doe'
            return

  the test passes.

* I remove the commented lines and ``return None``

  .. code-block:: python
    :lineno-start: 25

    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'smith'


    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)

* I add an :ref:`assertion<what is an assertion?>` that will fail, for the last name of ``mary`` in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 144

            mary = src.classes.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')
            self.assertEqual(mary.last_name, mary.first_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'mary'

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 3-4

            mary = src.classes.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the test passes because ``mary`` and ``jane`` are :ref:`instances<how to test if something is an instance of a class>` of ``Jane``

----

* I add an :ref:`assertion<what is an assertion?>` for ``joe``

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 2-3
    :emphasize-text: Joe

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            self.assertEqual(joe.first_name, 'joe')

            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsSubclass(
                src.classes.Jane, src.classes.Doe
            )

            mary = src.classes.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        module 'src.classes' has no attribute 'Joe'.
        Did you mean: 'Doe'?

* I add a :ref:`definition<how to make a class>` for the ``Joe`` :ref:`class<what is a class?>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 7

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)


    class Joe(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``joe = src.classes.Joe()`` runs

  .. code-block:: python

    joe = src.classes.Joe()
          Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` takes two required :ref:`positional argument<test_w_positional_arguments>` (``self`` and ``first_name``) and it was called with one (``self``)

* I add the ``__init__`` :ref:`method<what is a method?>` to ``Joe``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 1-2, 4-5

    # class Joe(src.person.Person): pass
    class Joe(src.person.Person):

        def __init__(self):
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Joe' object has no attribute 'first_name'

* I add ``self.first_name`` to ``Joe`` with a value

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 5

    # class Joe(src.person.Person): pass
    class Joe(src.person.Person):

        def __init__(self):
            self.first_name = 'joe'
            return None

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_multiple_parents` to make sure that ``joe`` is a ``Blow``, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 5

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            # self.assertEqual(joe.first_name, 'mary')
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Joe' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add ``last_name`` to the ``__init__`` :ref:`method<what is a method?>` of ``Joe`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6

    # class Joe(src.person.Person): pass
    class Joe(src.person.Person):

        def __init__(self):
            self.first_name = 'joe'
            self.last_name = 'blow'
            return None

  the test passes. I cheated, which means I need a better test.

* I add issubclass_ to :ref:`test_classes_w_multiple_parents` to make sure ``Joe`` is a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Blow``, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 5-7

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            assert issubclass(
                src.classes.Joe, src.classes.Blow
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

* I change the parent of ``Joe`` to ``Blow`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 2-3

    # class Joe(src.person.Person): pass
    # class Joe(src.person.Person):
    class Joe(Blow):

        def __init__(self):
            self.first_name = 'joe'
            self.last_name = 'blow'
            return None

  the test passes.

* I no longer need ``self.last_name = 'blow'`` because it is a repetition. I add a call to the `super built-in function`_

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 6-8

    # class Joe(src.person.Person): pass
    # class Joe(src.person.Person):
    class Joe(Blow):

        def __init__(self):
            super().__init__('joe')
            # self.first_name = 'joe'
            # self.last_name = 'blow'
            return None

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Joe' object has no attribute 'first_name'.
        Did you mean: 'last_name'?

  because this happens when ``joe = src.classes.Joe()`` runs

  .. code-block:: python

    joe = src.classes.Joe()
          Joe.__init__()
              super().__init__('joe')
          Blow.__init__('joe')
              self.last_name = 'blow'

  there is no assignment of a value to the ``first_name`` :ref:`attribute<what is a class attribute?>` in ``Blow``

* I add ``self.first_name`` to ``Blow``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4

    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.first_name = first_name
            self.last_name = 'blow'

  the test passes because this happens when ``joe = src.classes.Joe()`` runs

  .. code-block:: python

    joe = src.classes.Joe()
          Joe.__init__()
              super().__init__('joe')
          Blow.__init__('joe')
              self.first_name = 'joe'
              self.last_name = 'blow'

* I remove the commented lines and ``return None`` from ``Joe``

  .. code-block:: python
    :lineno-start: 32

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)


    class Joe(Blow):

        def __init__(self):
            super().__init__('joe')

* I add a call to the `assertNotIsSubclass method`_ in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 8-10

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            assert issubclass(
                src.classes.Joe, src.classes.Blow
            )
            self.assertNotIsSubclass(
                src.classes.Joe, src.classes.Blow
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Joe object at 0xffffabcdef80>
        is a subclass of <class 'src.classes.Blow'>

* I change assertNotIsSubclass_ to assertIsSubclass_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 136
    :emphasize-lines: 8-9

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            assert issubclass(
                src.classes.Joe, src.classes.Blow
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Joe, src.classes.Blow
            )

  the test passes.

* I change ``mary`` to be an :ref:`instance<how to test if something is an instance of a class>` of ``Mary``, a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Jane``

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 1-2

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Mary'

* I add a :ref:`class definition<how to make a class>` for ``Mary`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7, 9-10

    class Joe(Blow):

        def __init__(self):
            super().__init__('joe')


    class Mary(Jane): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError: 'jane' != 'mary'

  because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary # has no __init__ call Jane
           Jane.__init__()
               # use the default value
               Jane.__init__(first_name='jane')
               super().__init__(first_name)
           Doe.__init__('jane')
               super().__init__(first_name)
           Person.__init__('jane')
               Person.__init__('jane', last_name='doe')
               self.first_name = 'jane'
               self.last_name = 'doe' # use the default value

* I add the ``__init__`` :ref:`method<what is a method?>` to ``Mary``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 1-2

    # class Mary(Jane): pass
    class Mary(Jane):

        def __init__(self):
            self.first_name = 'mary'

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Mary' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

  because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__()
               self.first_name = 'mary'

* I add a value for ``last_name``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 6

    # class Mary(Jane): pass
    class Mary(Jane):

        def __init__(self):
            self.first_name = 'mary'
            self.last_name = 'doe'

  the test passes. This is a repetition because

  - ``Mary`` is a ``Jane``
  - ``Jane`` is a ``Doe``
  - ``Doe`` is a ``Person``
  - the :ref:`default value<test_w_optional_arguments>` for ``last_name`` in ``Person`` is ``'doe'``

* I add a call to the `super built-in function`_ to remove the repetition

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-7

    # class Mary(Jane): pass
    class Mary(Jane):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the test is still green because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
                super().__init__(first_name)
           Doe.__init__('mary')
                super().__init__(first_name)
           Person.__init__('mary')
                Person.__init__('mary', last_name='doe')
                self.first_name = 'mary'
                self.last_name = 'doe' # use the default value

* I add an :ref:`assertion<what is an assertion?>` with the `issubclass built-in function`_ to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 6-8

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            assert not issubclass(
                src.classes.Mary, src.classes.Jane
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 6-7

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )


    # Exceptions seen

  the test passes.

* I add a call to assertNotIsSubclass_

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 10-12

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            self.assertNotIsSubclass(
                src.classes.Mary, src.classes.Jane
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Mary'> is
        a subclass of <class 'src.classes.Jane'>

* I change assertNotIsSubclass_ to the `assertIsSubclass method`_

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 10-11

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )


    # Exceptions seen

  the test passes.

----

=================================================================================
what happens when the child has more than one parent?
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to test if I can make ``Joe`` and ``Jane`` both be parents of ``Mary``?

  .. code-block:: python
    :lineno-start: 155
    :emphasize-lines: 14-16

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

  because ``Mary`` is not a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Joe``

* I add ``Joe`` as a parent of ``Mary`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 2-3

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Joe.__init__() takes 1
               positional argument but 2 were

  because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
               super().__init__(first_name)
           Joe.__init__('mary')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Joe`` only takes one :ref:`positional argument<test_w_positional_arguments>` (``self``) and it got called with two (``self`` and ``mary``)

* I change the ``__init__`` :ref:`method<what is a method?>` in ``Joe`` to take a ``first_name`` argument

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4

    class Joe(Blow):

        # def __init__(self):
        def __init__(self, first_name):
            super().__init__('joe')

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Joe.__init__() missing 1
               required positional argument: 'first_name'

  I broke the call that makes ``joe = src.classes.Joe()`` because the ``__init__`` :ref:`method<what is a method?>` now has two required :ref:`positional arguments<test_w_positional_arguments>` (``self`` and ``first_name``) and it was called with one (``self``)

* I add a :ref:`default value<test_w_optional_arguments>` to make ``first_name`` optional

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4-5

    class Joe(Blow):

        # def __init__(self):
        # def __init__(self, first_name):
        def __init__(self, first_name='joe'):
            super().__init__('joe')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'joe' != 'mary'

  for the first name of ``mary`` because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
               super().__init__(first_name)
           Joe.__init__('mary')
               super().__init__('joe') # the problem
           Blow.__init__('joe')
               self.first_name = 'joe'
               self.last_name = 'blow'

* I use the parameter name in the call to ``super`` instead of a fixed value in ``Joe``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 6-7

        class Joe(Blow):

            # def __init__(self):
            # def __init__(self, first_name):
            def __init__(self, first_name='joe'):
                # super().__init__('joe')
                super().__init__(first_name)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blow' != 'doe'

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_classes_w_multiple_parents` for the last name of ``mary`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 5-6

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )


    # Exceptions seen

  the test passes.

* I add a call to the `assertNotIsSubclass method`_

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 19-21

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            self.assertEqual(mary.eye_color, jane.eye_color)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )
            self.assertNotIsSubclass(
                src.classes.Mary, src.classes.Joe
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Mary'> is
        a subclass of <class 'src.classes.Joe'>

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 19-20

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            self.assertEqual(mary.eye_color, jane.eye_color)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Joe
            )

    # Exceptions seen

  the test passes.

----

* I change the order of the parents of ``Mary`` to see what it does to the value of ``last_name`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 47
    :emphasize-lines: 3-4

    # class Mary(Jane): pass
    # class Mary(Jane):
    # class Mary(Jane, Joe):
    class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the test is still green because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__()
               super().__init__('mary')
           Joe.__init__('mary')
               super().__init__(first_name)
           Blow.__init__('joe')
               self.first_name = 'joe'
               self.last_name = 'blow'

  the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` never gets called even though it is a parent of ``Mary``

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_multiple_parents` in ``classes.py``

  .. code-block:: python
    :lineno-start: 148
    :emphasize-lines: 4

            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertEqual(jane.eye_color, 'brown')
            self.assertIsSubclass(
                src.classes.Jane, src.classes.Doe
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AttributeError: 'Jane' object has no attribute 'eye_color'

* I add a :ref:`class attribute<what is a class attribute?>` to ``Jane`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 5

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)
            self.eye_color = 'brown'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``marry`` in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 7

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            self.assertEqual(mary.eye_color, jane.eye_color)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Joe
            )

    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Mary' object has no attribute 'eye_color'

* I change the order of the parents of ``Mary`` from ``(Joe, Jane)`` to ``(Jane, Joe)`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 3-4

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the test passes because this happens when ``mary = src.classes.Mary()`` runs

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
               super().__init__(first_name)
               self.eye_color = 'brown'
           Joe.__init__('mary')
               super().__init__('joe') # the problem
           Blow.__init__('joe')
               self.first_name = 'joe'
               self.last_name = 'blow'

  the order of the parents matters.

  - if the order is ``(Joe, Jane)`` then :ref:`instances<how to test if something is an instance of a class>`  of ``Mary`` get the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``Jane``
  - if the order is ``(Jane, Joe)`` then :ref:`instances<how to test if something is an instance of a class>`  of ``Mary`` do NOT get the ``eye_color`` :ref:`attribute<what is a class attribute?>`

----

* I add ``john`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 24-25

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            self.assertEqual(mary.eye_color, jane.eye_color)
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Joe
            )

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'John'

* I add a :ref:`class definition<how to make a class>` for ``John`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 12

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'


    class John(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``john = src.classes.John()`` runs

  .. code-block:: python

    john = src.classes.John()
           Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Person`` takes two :ref:`positional arguments<test_w_positional_arguments>` (``self`` and ``first_name``) and it got called with one (``self``)

* I add the ``__init__`` :ref:`method<what is a method?>` to ``John`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 1-2, 4-5

    # class John(src.person.Person): pass
    class John(src.person.Person):

        def __init__(self):
            self.first_name = 'john'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to make sure that ``John`` is a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Smith``

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 3-5

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            assert issubclass(
                src.classes.John, src.classes.Smith
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

  no cheating this time.

* I change the parent of ``John`` to ``Smith`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 2-3

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        def __init__(self):
            self.first_name = 'john'

  the test passes.

* I add a call to `assertNotIsSubclass`_ in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 6-8

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            assert issubclass(
                src.classes.John, src.classes.Smith
            )
            self.assertNotIsSubclass(
                src.classes.John, src.classes.Smith
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.John'> is
        a subclass of <class 'src.classes.Smith'>

* I change the call to `assertNotIsSubclass`_ to the `assertIsSubclass method`_

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 6-7

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            assert issubclass(
                src.classes.John, src.classes.Smith
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.John, src.classes.Smith
            )


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``last_name`` :ref:`attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 3

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            assert issubclass(
                src.classes.John, src.classes.Smith
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.John, src.classes.Smith
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'John' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add a :ref:`class attribute<what is a class attribute?>` for ``last_name`` in ``John`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 7

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        def __init__(self):
            self.first_name = 'john'
            self.last_name = 'smith'

  the test passes. This is a repetition because

  - ``John`` is a ``Smith``
  - the ``last_name`` :ref:`attribute<what is a class attribute?>` of :ref:`instance<how to test if something is an instance of a class>` of ``Smith`` is ``'smith'``

* I add a call to the `super built-in function`_ so :ref:`instances<how to test if something is an instance of a class>` of ``John`` can inherit the ``last_name`` :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 6-8

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        def __init__(self):
            super().__init__('john')
            # self.first_name = 'john'
            # self.last_name = 'smith'

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'John' object has no attribute 'first_name'.
        Did you mean: 'last_name'?

* I add the :ref:`attribute<what is a class attribute?>` to ``Smith``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5

    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.first_name = first_name
            self.last_name = 'smith'

  the test passes because this happens when ``john = src.classes.John()`` runs

  .. code-block:: python

    john = src.classes.John()
           John.__init__()
               super().__init__('john')
           Smith.__init__('john')
               self.first_name = 'john'
               self.last_name = 'smith'

----

* I add another person, a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``John`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 179
    :emphasize-lines: 12-15

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            assert issubclass(
                src.classes.John, src.classes.Smith
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.John, src.classes.Smith
            )

            lil = src.classes.Lil()
            assert issubclass(
                src.classes.Lil, src.classes.John
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Lil'

* I add a :ref:`class definition<how to make a class>` for ``Lil`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 11

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        def __init__(self):
            super().__init__('john')
            # self.first_name = 'john'
            # self.last_name = 'smith'


    class Lil(John): pass

  the test passes.

* I add a call to the `assertNotIsSubclass method`_ in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 5-7

            lil = src.classes.Lil()
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            self.assertNotIsSubclass(
                src.classes.Lil, src.classes.John
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Lil'> is
        a subclass of <class 'src.classes.John'>

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 5-6

            lil = src.classes.Lil()
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )


    # Exceptions seen

  the test passes

* I add an :ref:`assertion<what is an assertion?>` to test ``John`` and ``Mary`` as parents of ``Lil``?

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 9-11

            lil = src.classes.Lil()
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

* I add ``Mary`` as a parent to ``Lil`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 1-2

    # class Lil(John): pass
    class Lil(John, Mary): pass

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``first_name`` :ref:`attribute<what is a class attribute?>` of ``lil`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 2

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'john' != 'lil'

  because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil # has no __init__, call John
          John.__init__()
               super().__init__('john')
          Smith.__init__('john')
              self.first_name = 'john'
              self.last_name = 'smith'

* I add the ``__init__`` :ref:`method<what is a method?>` with a value for the ``first_name`` :ref:`attribute<what is a class attribute?>` in ``Lil`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2-3, 5-6

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):

        def __init__(self):
            self.first_name = 'lil'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``last_name`` :ref:`attribute<what is an attribute?>` of ``lil``, in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 3

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, mary.last_name)
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Lil' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add a value for ``last_name`` to ``Lil`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 7

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):

        def __init__(self):
            self.first_name = 'lil'
            self.last_name = 'blow'

  the test passes. This is a repetition, and a problem if the value of the ``last_name`` :ref:`attribute<what is a class attribute?>` of the parent changes.

* I add a call to the `super built-in function`_ to remove the repetition

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 6-8

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):

        def __init__(self):
            super().__init__('lil')
            # self.first_name = 'lil'
            # self.last_name = 'blow'

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: John.__init__() takes 1
               positional argument but 2 were given

  because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``John`` takes one :ref:`positional argument<test_w_positional_arguments>` (``self``) and it was called with two (``self`` and ``lil``)

* I change the ``__init__`` :ref:`method<what is a method?>` in ``John`` to take in a parameter for ``first_name`` with a :ref:`default value<test_w_optional_arguments>` to make it optional

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 5-8

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        # def __init__(self):
        def __init__(self, first_name='john'):
            # super().__init__('john')
            super().__init__(first_name)
            # self.first_name = 'john'
            # self.last_name = 'smith'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :lineno-start:

    AssertionError: 'smith' != 'blow'

  because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(first_name)
              self.first_name = first_name
              self.last_name = last_name

  no other ``__init__`` :ref:`methods<what is a method?>` get called for the parents of ``Lil``

* I add a call to the `super built-in function`_ in ``Smith`` to see what will happen

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 4-9

    class Smith(src.person.Person):

        def __init__(self, first_name):
            super().__init__(
                first_name=first_name,
                last_name='smith',
            )
            # self.first_name = first_name
            # self.last_name = 'smith'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Mary.__init__() got
               an unexpected keyword argument 'first_name'

  because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name, last_name='smith',
              )
          Mary.__init__('lil', 'smith')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Mary`` was called with a :ref:`keyword argument<test_w_keyword_arguments>` not ``self``

* I add ``first_name`` with a :ref:`default value<test_w_optional_arguments>` to the ``__init__`` :ref:`method<what is a method?>` of ``Mary``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 6-7

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        # def __init__(self):
        def __init__(self, first_name='mary'):
            # super().__init__('mary')
            super().__init__(first_name)
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Mary.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I add ``last_name`` to the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 7-8

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        # def __init__(self):
        # def __init__(self, first_name='mary'):
        def __init__(self, first_name='mary', last_name):
            # super().__init__('mary')
            super().__init__(first_name)
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
                 follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_w_args_and_kwargs>`

  this is a problem, I just broke the ``mary = src.classes.Mary()`` which was working before.

* I add a :ref:`default value<test_w_optional_arguments>` for ``last_name``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 8-12

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        # def __init__(self):
        # def __init__(self, first_name='mary'):
        # def __init__(self, first_name='mary', last_name):
        def __init__(
                self, first_name='mary',
                last_name=None,
            ):
            # super().__init__('mary')
            super().__init__(first_name)
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name, last_name='smith',
              )
          Mary.__init__('lil', 'smith')
              super().__init__(first_name)
          Jane.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'brown'
          Joe.__init__('lil')
              super().__init__('lil')
          Blow.__init__('lil')
              self.first_name = 'lil'
              self.last_name = 'blow'

* I change the order of the parents of ``Lil`` to ``(Mary, John)`` to see if the value will change to ``john.last_name``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3-4

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    # class Lil(John, Mary):
    class Lil(Mary, John):

        def __init__(self):
            super().__init__('lil')
            # self.first_name = 'lil'
            # self.last_name = 'blow'

  the test is still green because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__('lil')
              Mary.__init__('lil', last_name=None)
              super().__init__(first_name)
          Jane.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'brown'
          Joe.__init__('lil')
              super().__init__('lil')
          Blow.__init__('lil')
              self.first_name = 'lil'
              self.last_name = 'blow'

  no other ``__init__`` :ref:`methods<what is a method?>` get called for the parents of ``Lil``

* I add a call to the `super built-in function`_ in ``Blow``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 4-7

    class Blow(src.person.Person):

        def __init__(self, first_name):
            super().__init__(
                first_name=first_name,
                last_name='blow',
            )
            # self.first_name = first_name
            # self.last_name = 'blow'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        John.__init__() got
        an unexpected keyword argument 'last_name'.
        Did you mean 'first_name'?

  because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__('lil')
              Mary.__init__('lil', last_name=None)
              super().__init__(first_name)
          Jane.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'brown'
          Doe.__init__('lil')
              super().__init__(first_name)
          Joe.__init__('lil')
              super().__init__('lil')
          Blow.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='blow',
              )
          John.__init__(
              first_name='lil',
              last_name='blow',
          )

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``John`` does not have a parameter named ``last_name``

* I add ``last_name`` to ``John``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 6-7

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        # def __init__(self):
        # def __init__(self, first_name='john'):
        def __init__(self, first_name='john', last_name):
            # super().__init__('john')
            super().__init__(first_name)
            # self.first_name = 'john'
            # self.last_name = 'smith'

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
                 follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_w_args_and_kwargs>`

* I give ``last_name`` a :ref:`default value<test_w_optional_arguments>`

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 7-11

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        # def __init__(self):
        # def __init__(self, first_name='john'):
        # def __init__(self, first_name='john', last_name):
        def __init__(
                self, first_name='john',
                last_name=None,
            ):
            # super().__init__('john')
            super().__init__(first_name)
            # self.first_name = 'john'
            # self.last_name = 'smith'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != 'blow'

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``lil.last_name`` in :ref:`test_classes_w_multiple_parents`

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 3-4

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, mary.last_name)
            self.assertEqual(lil.last_name, john.last_name)
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  the test passes because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__('lil')
              Mary.__init__('lil', last_name=None)
              super().__init__(first_name)
          Jane.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'brown'
          Doe.__init__('lil')
              super().__init__(first_name)
          Joe.__init__('lil')
              super().__init__('lil')
          Blow.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='blow',
              )
          John.__init__(
              first_name='lil',
              last_name='blow',
          )
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='smith',
              )
          Person.__init__(
              first_name='lil',
              last_name='smith',
          )
              self.first_name = 'lil'
              self.last_name = 'smith'

  the order of the parents matters.

----

* I add an :ref:`assertion<what is an assertion?>` for ``lil.eye_color`` to test if :ref:`instance<how to test if something is an instance of a class>` of ``Lil`` inherit ``eye_color`` from ``Jane``, the parent of ``Mary``

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 5

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, mary.last_name)
            self.assertEqual(lil.last_name, john.last_name)
            self.assertEqual(lil.eye_color, '')
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'brown' != ''

* I change the expectation of the :ref:`assertion<what causes AssertionError?>`

  .. code-block:: python
    :lineno-start: 190
    :emphasize-lines: 5-6

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, mary.last_name)
            self.assertEqual(lil.last_name, john.last_name)
            # self.assertEqual(lil.eye_color, '')
            self.assertEqual(lil.eye_color, jane.eye_color)
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  :ref:`instances<how to test if something is an instance of a class>` of ``Lil`` and ``Mary`` get ``eye_color`` from ``Jane`` if ``Jane`` is an ancestor of the first parent in the order of parents.

----

* I want to see what happens when I add the ``eye_color`` :ref:`attribute<what is a class attribute?>` to ``Mary`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 8-12

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        # def __init__(self):
        # def __init__(self, first_name='mary'):
        # def __init__(self, first_name='mary', last_name):
        def __init__(
                self, first_name='mary',
                last_name=None,
            ):
            # super().__init__('mary')
            super().__init__(first_name)
            self.eye_color = 'red'
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'red' != 'brown'

  for ``mary.eye_color`` because :ref:`instances<how to test if something is an instance of a class>` of :ref:`classes<what is a class?>` can override the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` they inherit

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``mary.eye_color`` in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 156
    :emphasize-lines: 7-8

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # self.assertEqual(mary.eye_color, jane.eye_color)
            self.assertEqual(mary.eye_color, 'red')
            # assert not issubclass(
            assert issubclass(
                src.classes.Mary, src.classes.Jane
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Jane
            )
            assert issubclass(
                src.classes.Mary, src.classes.Joe
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Mary, src.classes.Joe
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'red' != 'brown'

  for ``lil.eye_color`` because this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__('lil')
              Mary.__init__('lil', last_name=None)
              super().__init__(first_name)
              self.eye_color = 'red'
          Jane.__init__('lil')
              super().__init__(first_name)
              # self.eye_color = 'brown' does not affect instance
          Doe.__init__('lil')
              super().__init__(first_name)
          Joe.__init__('lil')
              super().__init__('lil')
          Blow.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='blow',
              )
          John.__init__(
              first_name='lil',
              last_name='blow',
          )
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='smith',
              )
          Person.__init__(
              first_name='lil',
              last_name='smith',
          )
              self.first_name = 'lil'
              self.last_name = 'smith'

  the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``Jane`` never gets set for :ref:`instances<how to test if something is an instance of a class>` of ``Mary``

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``lil.eye_color`` in :ref:`test_classes_w_multiple_parents`

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 6-7

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, mary.last_name)
            self.assertEqual(lil.last_name, john.last_name)
            # self.assertEqual(lil.eye_color, '')
            # self.assertEqual(lil.eye_color, jane.eye_color)
            self.assertEqual(lil.eye_color, mary.eye_color)
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )


    # Exceptions seen

  the test passes.

* I change the order of the parents of ``Lil`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3-4

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):
    # class Lil(Mary, John):

        def __init__(self):
            super().__init__('lil')
            # self.first_name = 'lil'
            # self.last_name = 'blow'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blow' != 'smith'

  because the order of the parents has an effect on the ``last_name`` :ref:`attribute<what is a class attribute?>`.

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``lil.last_name``

  .. code-block:: python
    :lineno-start: 191
    :emphasize-lines: 3-4

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, mary.last_name)
            # self.assertEqual(lil.last_name, john.last_name)
            # self.assertEqual(lil.eye_color, '')
            # self.assertEqual(lil.eye_color, jane.eye_color)
            self.assertEqual(lil.eye_color, mary.eye_color)
            assert issubclass(
                src.classes.Lil, src.classes.John
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.Lil, src.classes.John
            )
            assert issubclass(
                src.classes.Lil, src.classes.Mary
            )

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``john.eye_color``

  .. code-block:: python
    :lineno-start: 180
    :emphasize-lines: 4

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertEqual(john.eye_color, 'orange')
            assert issubclass(
                src.classes.John, src.classes.Smith
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.John, src.classes.Smith
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'John' object has no attribute 'eye_color'

* I add a value for the ``eye_color`` :ref:`attribute<what is a class attribute?>` to ``Smith`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8

    class Smith(src.person.Person):

        def __init__(self, first_name):
            super().__init__(
                first_name=first_name,
                last_name='smith',
            )
            self.eye_color = 'orange'
            # self.first_name = first_name
            # self.last_name = 'smith'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'orange' != 'red'

  because if the parents of ``Lil`` are ``(John, Mary)``, this happens when ``lil = src.classes.Lil()`` runs

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name, last_name='smith',
              )
              self.eye_color = 'orange'
          Mary.__init__('lil', 'smith')
              super().__init__(first_name)
              # self.eye_color = 'red' does not affect instance
          Jane.__init__('lil')
              super().__init__(first_name)
              # self.eye_color = 'brown' does not affect instance
          Joe.__init__('lil')
              super().__init__('lil')
          Blow.__init__('lil')
              self.first_name = 'lil'
              self.last_name = 'blow'

*

----

----

----

----



----



* I add an :ref:`assertion<what is an assertion?>` for the ``first_name``, in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 3

            lil = src.classes.Lil()
            self.assertIsInstance(lil, src.classes.John)
            self.assertEqual(lil.first_name, 'lil')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'john' != 'lil'

* I add the ``__init__`` :ref:`method<what is a method?>` in the :ref:`definition<how to make a class>` of ``Lil`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 1-2, 4-5

    # class Lil(John): pass
    class Lil(John):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``lil``, in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 4

            lil = src.classes.Lil()
            self.assertIsInstance(lil, src.classes.John)
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, lil.first_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != 'lil'

* I change the expectation

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 4-5

            lil = src.classes.Lil()
            self.assertIsInstance(lil, src.classes.John)
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, lil.first_name)
            self.assertEqual(lil.last_name, john.last_name)


    # Exceptions seen

  the test passes because Python_ makes the following calls to resolve the call to make an instance of the ``Lil`` :ref:`class<what is a class?>` when ``John`` is the parent

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = John.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = Smith.__init__('lil')
          super().__init__(first_name, last_name='smith')
        = Person.__init__('lil', last_name='smith')
          self.first_name = 'lil'
          self.last_name = 'smith'

* I add assertIsInstance_ to test if ``Lil`` is an instance of ``Mary``

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 3

            lil = src.classes.Lil()
            self.assertIsInstance(lil, src.classes.John)
            self.assertIsInstance(lil, src.classes.Mary)
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, lil.first_name)
            self.assertEqual(lil.last_name, john.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Lil object at 0xffffaaaaaaaa>
        is not an instance of <class 'src.classes.Mary'>

  because ``Lil`` is not a child of ``Mary``, yet.

* I add ``Mary`` as a parent of ``Lil`` before ``John`` to see if it will change the ``last_name`` value, in ``classes.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 2-3

    # class Lil(John): pass
    # class Lil(John):
    class Lil(Mary, John):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: John.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  because Python_ makes the following calls to resolve the call to make an instance of the ``Lil`` :ref:`class<what is a class?>` if the parents are ``(Mary, John)``

  first it makes these calls for the ``Mary`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = Mary.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = Jane.__init__(first_name='lil', **kwargs)
          super().__init__(first_name=first_name)
        = Doe # Doe has no __init__, skip to Joe
        = Joe.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = Blow.__init__('lil')
          super().__init__(first_name, last_name='blow')

  then it makes this call for the ``John`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = John.__init__(first_name='lil', last_name='blow')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``John`` only takes one :ref:`keyword_argument<test_w_keyword_arguments>` (``first_name``) and the call provides two (``first_name`` and ``last_name``)

* I add a :ref:`double starred expression<double starred expressions>` to ``John`` so it can take any number of :ref:`keyword arguments<test_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 4-5

    # class John(src.person.Person):
    class John(Smith):

        # def __init__(self, first_name='john'):
        def __init__(self, first_name='john', **kwargs):
            super().__init__(first_name=first_name)

  the test passes Python_ makes this call for the ``John`` parent after it gets values from the ``Mary`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = John.__init__(first_name='lil', last_name='blow')
          super().__init__(first_name=first_name)
        = Smith.__init__(first_name='lil')
          super().__init__(first_name, last_name='smith')
        = Person.__init__('lil', last_name='smith')
          self.first_name = 'lil'
          self.last_name = 'smith'

----

* I change the order of the parents of ``Lil``

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-4

    # class Lil(John): pass
    # class Lil(John):
    # class Lil(Mary, John):
    class Lil(John, Mary):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Mary.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  same problem, same solution

* I add a :ref:`double starred expression<double starred expressions>` to ``Mary`` so it can take any number of :ref:`keyword arguments<test_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 6-7

    # class Mary(Jane): pass
    # class Mary(Joe, Jane): pass
    # class Mary(Joe, Jane):
    class Mary(Jane, Joe):

        # def __init__(self, first_name='mary'):
        def __init__(self, first_name='mary', **kwargs):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: 'blow' != 'smith'

  the order of the parents matters because Python_ makes the following calls to resolve the call to make an instance of the ``Lil`` :ref:`class<what is a class?>` if the parents are ``(John, Mary)``

  first it makes these calls for the ``John`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = src.classes.Lil()
          Lil.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = John.__init__(first_name='lil', **kwargs)
          super().__init__(first_name=first_name)
        = Smith.__init__(first_name='lil')
          super().__init__(first_name, last_name='smith')

  then it makes these calls for the ``Mary`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = Mary.__init__(first_name='lil', **kwargs)
          super().__init__(first_name=first_name)
        = Jane.__init__(first_name='lil', **kwargs)
          super().__init__(first_name=first_name)
        = Doe # Doe has no __init__, skip to Joe
        = Joe.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = Blow.__init__('lil')
          super().__init__(first_name, last_name='blow')
        = Person.__init__(first_name='lil', last_name='blow')
          self.first_name = 'lil'
          self.last_name = 'blow'

  - ``Jane`` and ``Mary`` do not pass on the value they receive for ``last_name`` to their parents when they call  ``super().__init__`` which means :ref:`the method uses the default value for the parameter because it is called without the parameter<test_w_optional_arguments>`
  - ``Blow`` always calls ``Person`` with ``blow`` as the value for ``last_name`` it does not matter if I send a different value
  - ``Smith`` always calls ``Person`` with ``smith`` as the value for ``last_name`` it does not matter if I send a different value
  - whichever parent calls ``Person`` last will be the values that the instance gets

* I change the order of the parents of ``Lil`` back to ``(Mary, John)``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3-4

    # class Lil(John): pass
    # class Lil(John):
    class Lil(Mary, John):
    # class Lil(John, Mary):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the test is green again. The test shows that

  - if the parents of ``Lil`` are defined as ``(Mary, John)`` the default value for ``last_name`` is the value for ``last_name`` of ``John``
  - if the parents of ``Lil`` are defined as ``(John, Mary)`` the default value for ``last_name`` is the value for the ``last_name`` of ``Mary``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 13

    class Doe(src.person.Person): pass


    class Blow(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name, last_name='blow')


    class Smith(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name, last_name='smith')


    class Jane(Doe):

        def __init__(self, first_name='jane', **kwargs):
            super().__init__(first_name=first_name)


    class Joe(Blow):

        def __init__(self, first_name='joe'):
            super().__init__(first_name=first_name)


    class Mary(Jane, Joe):

        def __init__(self, first_name='mary', **kwargs):
            super().__init__(first_name=first_name)


    class John(Smith):

        def __init__(self, first_name='john', **kwargs):
            super().__init__(first_name=first_name)


    class Lil(Mary, John):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

----

* I remove the commented lines from :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            self.assertIsInstance(joe, src.classes.Blow)

            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsInstance(jane, src.classes.Doe)

            mary = src.classes.Mary()
            self.assertEqual(mary.first_name, 'mary')
            self.assertEqual(mary.last_name, joe.last_name)
            self.assertIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Joe)

            john = src.classes.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertIsInstance(john, src.classes.Smith)

            lil = src.classes.Lil()
            self.assertIsInstance(lil, src.classes.John)
            self.assertIsInstance(lil, src.classes.Mary)
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, john.last_name)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_classes_w_multiple_parents'

.. NOTE:: All the instances could have been made with only the ``Person`` :ref:`class<what is a class?>` because there was nothing unique about the :ref:`classes<what is a class?>` I made it ``classes.py`` and it would not have given me the chance to practice making classes with multiple parents and seeing how Python_ resolves the order - this is called `Method Resolution Order`_

  .. code-block:: python

    joe = src.classes.Joe()
    joe = src.person.Person('joe', last_name='blow')

  .. code-block:: python

    jane = src.classes.Jane()
    jane = src.person.Person('jane')

  .. code-block:: python

    mary = src.classes.Mary()
    mary = src.person.Person('mary', 'blow')

  .. code-block:: python

    john = src.classes.John()
    john = src.person.Person('john', 'smith')

  .. code-block:: python

    lil = src.person.Lil()
    lil = src.person.Person('lil', 'smith')

  which would have just been Python_ making this call to make instances of the ``Person`` :ref:`class<what is a class?>`

  .. code-block:: python

    a_name = src.person.Person(first_name, last_name=last_name)
             Person.__init__(first_name, last_name=last_name)
             self.first_name = first_name
             self.last_name = last_name

:ref:`I can make classes with multiple parents<test_classes_w_multiple_parents>`

----

*********************************************************************************
review
*********************************************************************************

I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`
* :ref:`object<test_making_a_class_w_object>`
* :ref:`its parent<test_making_a_class_w_inheritance>`
* :ref:`multiple parents<test_classes_w_multiple_parents>`
* :ref:`I can make a class with object<test_making_a_class_w_object>`
* :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

----

*********************************************************************************
close the project
*********************************************************************************

* I close the file(s) I have open in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ where the tests are running, then use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

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

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`how to raise AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to use classes<classes>`
* :ref:`how to make classes<everything in python is a child of object>`

:ref:`Would you like to use test classes with parents?<family ties>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->