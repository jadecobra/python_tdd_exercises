.. include:: ../links.rst

.. _super: https://docs.python.org/3/library/functions.html#super
.. _super built-in function: super_
.. _assertNotIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance
.. _assertNotIsInstance method: assertNotIsInstance_
.. _assertIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance
.. _assertIsInstance method: assertIsInstance_
.. _isinstance: https://docs.python.org/3/library/functions.html#isinstance
.. _isinstance built-in function: isinstance_
.. _unittest.TestCase.assertIsInstance:
.. _unittest.TestCase.assertNotIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance

#################################################################################
family ties
#################################################################################

In object oriented programming there is a concept called Inheritance_, it allows me to define new :ref:`objects<what is a class?>` that get their magic powers from other :ref:`objects<what is a class?>`.

Making new :ref:`objects<what is a class?>` can be easier with Inheritance_ because I do not have to rewrite things that have already been written, I can inherit them instead and change the new :ref:`objects<what is a class?>` to do what I want.

To use inheritance_ I specify the "parent" in parentheses when I define the new object (the child) to make the relationship

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

To review, I can make a :ref:`class<what is a class?>` with the :ref:`class<what is a class?>` keyword, use :ref:`CapWords format<CapWords>` for the name and use a name that tells what the group of :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` do

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----


----

=================================================================================
how to test if something is NOT an instance of a class
=================================================================================

----

I can test if an :ref:`object<what is a class?>` is a child (instance) of another :ref:`object<what is a class?>` or NOT with the `isinstance built-in function`_ from `The Python Standard Library`_, it checks if the thing in the parentheses on the left is an instance of the :ref:`class<what is a class?>` on the right in the parenthesess

* I change ``test_failure`` to :ref:`test_making_a_class_w_pass` then add an :ref:`assertion<what is an assertion?>` with isinstance_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-9

    import unittest


    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            assert not isinstance(
                src.classes.WPass, object
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

  because the statement ``not isinstance(src.classes.WPass, object)`` is :ref:`False<test_what_is_false>`

----

=================================================================================
how to test if something is an instance of a class
=================================================================================

----

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-3

        def test_making_a_class_w_pass(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WPass, object
            )


    # Exceptions seen


  * the :ref:`assertion<what is an assertion?>` - ``assert isinstance(src.classes.WPass, object)`` checks if the result of a call to ``WPass`` in ``src.classes.py`` in the ``src`` folder_ also known as ``src.classes.WPass``, is an instance of the :ref:`object class<what is a class?>` which is the mother of all :ref:`classes<what is a class?>`

  * the :ref:`class definition<how to make a class>` simply says pass_ and the test passes
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body)
  * the test passes because :ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

The `unittest.TestCase class`_ has 2 :ref:`methods<what is a method?>` I can also use to test if an :ref:`object<what is a class?>` is a child (instance) of a :ref:`class<what is a class?>` or NOT - assertIsInstance_ and assertNotIsInstance_

----

=================================================================================
another way to test if something is NOT an instance of a class
=================================================================================

----

I add the `assertNotIsInstance method`_ to the test

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 6-8
  :emphasize-text: Not

      def test_making_a_class_w_pass(self):
          # assert not isinstance(
          assert isinstance(
              src.classes.WPass, object
          )
          self.assertNotIsInstance(
              src.classes.WPass, object
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError:
      <src.classes.WPass object at 0xffff8a7b6543>
      is an instance of <class 'object'>

----

=================================================================================
another way to test if something is an instance of a class
=================================================================================

----

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

        def test_making_a_class_w_pass(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WPass, object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WPass, object
            )


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_making_a_class_w_pass(self):
            assert isinstance(
                src.classes.WPass, object
            )
            self.assertIsInstance(
                src.classes.WPass, object
            )


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


I can also make a :ref:`class<what is a class?>` with parentheses.

----

=================================================================================
:red:`RED`: make it red
=================================================================================

----

* I go back to the terminal_ that is running the tests
* I add another test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-12

        def test_making_a_class_w_pass(self):
            assert isinstance(
                src.classes.WPass, object
            )
            self.assertIsInstance(
                src.classes.WPass, object
            )

        def test_making_a_class_w_parentheses(self):
            assert not isinstance(
                src.classes.WParentheses, object
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

  because the statement ``not isinstance(src.classes.WParentheses, object)`` is :ref:`False<test_what_is_false>`

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 2-3

        def test_making_a_class_w_parentheses(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses, object
            )


    # Exceptions seen

  the test passes

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

  * the :ref:`assertion<what is an assertion?>` - ``assert isinstance(src.classes.WParentheses, object)`` checks if the result of a call to ``WParentheses`` in ``src.classes.py`` in the ``src`` folder_ also known as ``src.classes.WParentheses``, is an instance of the :ref:`object class<what is a class?>` which is the mother of all :ref:`classes<what is a class?>`

  * this :ref:`class definition<how to make a class>` has parentheses after the name
  * the :ref:`class definition<how to make a class>` simply says pass_ and the test passes
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body)
  * the test is still green because :ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`

* I remove the commented line

  .. code-block:: python
    :linenos:

    class WPass: pass


    class WParentheses(): pass

* I add the `assertNotIsInstance method`_ to :ref:`test_making_a_class_w_parentheses` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6-8
    :emphasize-text: Not

        def test_making_a_class_w_parentheses(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses, object
            )
            self.assertNotIsInstance(
                src.classes.WParentheses, object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.WParentheses object at 0xffffab123456>
        is an instance of <class 'object'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 6-7

        def test_making_a_class_w_parentheses(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WParentheses, object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WParentheses, object
            )


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 15

        def test_making_a_class_w_parentheses(self):
            assert isinstance(
                src.classes.WParentheses, object
            )
            self.assertIsInstance(
                src.classes.WParentheses, object
            )


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

  class WParentheses: pass

because ":ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`", which leads me to the next test.

----

*********************************************************************************
test_making_a_class_w_object
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with an :ref:`assertion<what is an assertion?>` for a new :ref:`class<what is a class?>`

.. code-block:: python
  :lineno-start: 15
  :emphasize-lines: 9-12

      def test_making_a_class_w_parentheses(self):
          assert isinstance(
              src.classes.WParentheses, object
          )
          self.assertIsInstance(
              src.classes.WParentheses, object
          )

      def test_making_a_class_w_object(self):
          assert not isinstance(
              src.classes.WObject, object
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
    :lineno-start: 23
    :emphasize-lines: 2-3

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject, object
            )


    # Exceptions seen

  the test passes

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

  the test is still green. :ref:`I can make a class with object<test_making_a_class_w_object>`

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    class WParentheses(): pass


    class WObject(object): pass

* I add an :ref:`assertion<what is an assertion?>` with the `assertNotIsInstance method`_ to :ref:`test_making_a_class_w_object` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6-8

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject, object
            )
            self.assertNotIsInstance(
                src.classes.WObject, object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.WObject object at 0xffffcd781234>
        is an instance of <class 'object'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 6-7

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject, object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WObject, object
            )


    # Exceptions seen

  the test passes. I have three different :ref:`classes<what is a class?>`, and the tests show that they are all instances of the :ref:`object class<what is a class?>`

  .. code-block:: python

    class WPass: pass

  .. code-block:: python

    class WParentheses(): pass



  .. code-block:: python

    class WObject(object): pass

  their :ref:`definitions<how to make a class>` are different, their results are the same because ":ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`"

  I like to write my :ref:`classes<what is a class?>` with ``(object)``, so that anyone can see what the parent :ref:`class<what is a class?>` is without thinking about it.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`None<what is None?>` to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 11

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WObject(), object
            )

            assert not isinstance(None, object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`None<what is None?>` is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 11-12

        def test_making_a_class_w_object(self):
            # assert not isinstance(
            assert isinstance(
                src.classes.WObject(), object
            )
            # self.assertNotIsInstance(
            self.assertIsInstance(
                src.classes.WObject(), object
            )

            # assert not isinstance(None, object)
            assert isinstance(None, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that :ref:`None<what is None?>` is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 3

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
    :lineno-start: 33
    :emphasize-lines: 3-4

            # assert not isinstance(None, object)
            assert isinstance(None, object)
            # self.assertNotIsInstance(None, object)
            self.assertIsInstance(None, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`bool<what are booleans?>` to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 6

            # assert not isinstance(None, object)
            assert isinstance(None, object)
            # self.assertNotIsInstance(None, object)
            self.assertIsInstance(None, object)

            assert not isinstance(bool, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`bool<what are booleans?>` is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 1-2

            # assert not isinstance(bool, object)
            assert isinstance(bool, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that :ref:`bool<what are booleans?>` is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3

            # assert not isinstance(bool, object)
            assert isinstance(bool, object)
            self.assertNotIsInstance(bool, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'bool'> is an instance of <class 'object'>

  because :ref:`bool<what are booleans?>` is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4

            # assert not isinstance(bool, object)
            assert isinstance(bool, object)
            # self.assertNotIsInstance(bool, object)
            self.assertIsInstance(bool, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for int_ (the :ref:`class<what is a class?>` for whole numbers without decimals), to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 6

            # assert not isinstance(bool, object)
            assert isinstance(bool, object)
            # self.assertNotIsInstance(bool, object)
            self.assertIsInstance(bool, object)

            assert not isinstance(int, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because int_ is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1-2

            # assert not isinstance(int, object)
            assert isinstance(int, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that int_ is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

            # assert not isinstance(int, object)
            assert isinstance(int, object)
            self.assertNotIsInstance(int, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'int'> is an instance of <class 'object'>

  because int_ is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3-4

            # assert not isinstance(int, object)
            assert isinstance(int, object)
            # self.assertNotIsInstance(int, object)
            self.assertIsInstance(int, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for float_ (the :ref:`class<what is a class?>` for binary floating point decimal numbers), to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6

            # assert not isinstance(int, object)
            assert isinstance(int, object)
            # self.assertNotIsInstance(int, object)
            self.assertIsInstance(int, object)

            assert not isinstance(float, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because float_ is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 1-2

            # assert not isinstance(float, object)
            assert isinstance(float, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that float_ is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 3

            # assert not isinstance(float, object)
            assert isinstance(float, object)
            self.assertNotIsInstance(float, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'float'> is an instance of <class 'object'>

  because float_ is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 3-4

            # assert not isinstance(float, object)
            assert isinstance(float, object)
            # self.assertNotIsInstance(float, object)
            self.assertIsInstance(float, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for str_ (the :ref:`class<what is a class?>` for anything in :ref:`quotes`), to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 6

            # assert not isinstance(float, object)
            assert isinstance(float, object)
            # self.assertNotIsInstance(float, object)
            self.assertIsInstance(float, object)

            assert not isinstance(str, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because str_ is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 1-2

            # assert not isinstance(str, object)
            assert isinstance(str, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that str_ is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3

            # assert not isinstance(str, object)
            assert isinstance(str, object)
            self.assertNotIsInstance(str, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'str'> is an instance of <class 'object'>

  because str_ is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3-4

            # assert not isinstance(str, object)
            assert isinstance(str, object)
            # self.assertNotIsInstance(str, object)
            self.assertIsInstance(str, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for tuple_ (the :ref:`class<what is a class?>` for anything in parentheses ``( )`` separated by a comma), to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 6

            # assert not isinstance(str, object)
            assert isinstance(str, object)
            # self.assertNotIsInstance(str, object)
            self.assertIsInstance(str, object)

            assert not isinstance(tuple, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because tuple_ is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 1-2

            # assert not isinstance(tuple, object)
            assert isinstance(tuple, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that tuple_ is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3

            # assert not isinstance(tuple, object)
            assert isinstance(tuple, object)
            self.assertNotIsInstance(tuple, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'tuple'> is an instance of <class 'object'>

  because tuple_ is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 3-4

            # assert not isinstance(tuple, object)
            assert isinstance(tuple, object)
            # self.assertNotIsInstance(tuple, object)
            self.assertIsInstance(tuple, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`list (the class for anything in square brackets '[ ]')<what is a list?>`, to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 58
    :emphasize-lines: 6

            # assert not isinstance(tuple, object)
            assert isinstance(tuple, object)
            # self.assertNotIsInstance(tuple, object)
            self.assertIsInstance(tuple, object)

            assert not isinstance(list, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`list<what is a list?>` is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 1-2

            # assert not isinstance(list, object)
            assert isinstance(list, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that :ref:`list<what is a list?>` is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

            # assert not isinstance(list, object)
            assert isinstance(list, object)
            self.assertNotIsInstance(list, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'list'> is an instance of <class 'object'>

  because :ref:`list<what is a list?>` is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3-4

            # assert not isinstance(list, object)
            assert isinstance(list, object)
            # self.assertNotIsInstance(list, object)
            self.assertIsInstance(list, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for set_ (the :ref:`class<what is a class?>` for anything in curly braces ``{ }`` separated by a comma), to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 6

            # assert not isinstance(list, object)
            assert isinstance(list, object)
            # self.assertNotIsInstance(list, object)
            self.assertIsInstance(list, object)

            assert not isinstance(set, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because set_ is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 1-2

            # assert not isinstance(set, object)
            assert isinstance(set, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that set_ is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3

            # assert not isinstance(set, object)
            assert isinstance(set, object)
            self.assertNotIsInstance(set, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'set'> is an instance of <class 'object'>

  because set_ is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 3-4

            # assert not isinstance(set, object)
            assert isinstance(set, object)
            # self.assertNotIsInstance(set, object)
            self.assertIsInstance(set, object)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for :ref:`dict (the class for any key-value pairs in curly braces '{ }', separated by a comma)<what is a dictionary?>`, to show that everything in Python_ is an object_

  .. code-block:: python
    :lineno-start: 68
    :emphasize-lines: 6

            # assert not isinstance(set, object)
            assert isinstance(set, object)
            # self.assertNotIsInstance(set, object)
            self.assertIsInstance(set, object)

            assert not isinstance(dict, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`dict<what is a dictionary?>` is an :ref:`object<what is a class?>`.

* I change the statement to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 1-2

            # assert not isinstance(dict, object)
            assert isinstance(dict, object)


    # Exceptions seen

  the test passes.

* I use assertNotIsInstance_ to show that :ref:`dict<what is a dictionary?>` is an :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 3

            # assert not isinstance(dict, object)
            assert isinstance(dict, object)
            self.assertNotIsInstance(dict, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'dict'> is an instance of <class 'object'>

  because :ref:`dict<what is a dictionary?>` is an :ref:`object<what is a class?>`.

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 73
    :emphasize-lines: 3-4

            # assert not isinstance(dict, object)
            assert isinstance(dict, object)
            # self.assertNotIsInstance(dict, object)
            self.assertIsInstance(dict, object)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 23

        def test_making_a_class_w_object(self):
            assert isinstance(
                src.classes.WObject, object
            )
            self.assertIsInstance(
                src.classes.WObject, object
            )

            assert isinstance(None, object)
            self.assertIsInstance(None, object)

            assert isinstance(bool, object)
            self.assertIsInstance(bool, object)

            assert isinstance(int, object)
            self.assertIsInstance(int, object)

            assert isinstance(float, object)
            self.assertIsInstance(float, object)

            assert isinstance(str, object)
            self.assertIsInstance(str, object)

            assert isinstance(tuple, object)
            self.assertIsInstance(tuple, object)

            assert isinstance(list, object)
            self.assertIsInstance(list, object)

            assert isinstance(set, object)
            self.assertIsInstance(set, object)

            assert isinstance(dict, object)
            self.assertIsInstance(dict, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_making_a_class_w_object'

:ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`.

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

I add a test to ``test_classes.py``

.. code-block:: python
  :lineno-start: 55
  :emphasize-lines: 4-7

          assert isinstance(dict, object)
          self.assertIsInstance(dict, object)

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

  the test passes. All :ref:`classes<what is a class?>` automatically get these attributes, they inherit them because :ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`.

  The ``__init__`` :ref:`method<what is a method?>` is also inherited which means when I defined it in :ref:`test_classy_person_says_hello` I overwrote the inherited one.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attributes_and_methods_of_objects'

:ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`.

----

*********************************************************************************
test_making_classes_w_inheritance
*********************************************************************************

I can make :ref:`classes<what is a class?>` with inheritance

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 83
  :emphasize-lines: 6-8

              '__str__',
              '__subclasshook__'
          ]
          self.assertEqual(reality, my_expectation)

      def test_making_classes_w_inheritance(self):
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

  because even though ``Doe`` and ``Person`` are children of :ref:`object<what is a class?>`, ``Doe`` is not an instance of ``Person``

* I change the parent of ``Doe``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1-2

    # class Doe(object): pass
    class Doe(person.Person): pass

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

  because there is no definition for ``person`` in this file_

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

* I change the `import statement`_ so the path to ``person.py`` from the main project folder_ is correct

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

  the terminal_ definitely does not feel like my friend, it goes back to :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

  because ``Doe`` is still not an instance of ``Person`` even though I defined ``Person`` as the parent of ``Doe``

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_classes_w_inheritance` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)


    # Exceptions seen

  the test passes.

  * ``import src.person`` brings in an :ref:`object<what is a class?>` that represents the ``person.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``classes.py``
  * I have to use ``src.person.Person`` in ``classes.py`` because I am testing from the root folder_ of the project
  * The test needs to know where ``person.py`` is in relation to where I ran the tests from
  * This is a problem because if ``classes.py`` is run from inside ``src`` the `import statement`_ will not be able to find ``src.person`` from inside ``src``. Same thing if I run the tests from inside ``tests``. That is a problem for another time.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to the `assertIsInstance method`_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 5

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            self.assertIsInstance(a_class, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Doe'> is
        not an instance of <class 'src.person.Person'>

  because the ``Doe`` :ref:`class<what is a class?>` is not an instance of the ``Person`` :ref:`class<what is a class?>` and ``a_class`` is just a name pointing to the ``Doe`` :ref:`class<what is a class?>`

* I change assertIsInstance_ to assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 5-8

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to show that ``a_class`` which points to ``Doe`` is just a name for the :ref:`class<what is a class?>` not an instance

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 9

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            assert isinstance(a_class, a_class)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError: assert False

  because a :ref:`class<what is a class?>` is not an instance

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 9-10


        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            # assert isinstance(a_class, a_class)
            assert not isinstance(a_class, a_class)


    # Exceptions

  the test passes.

* I add assertIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 11

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )
            # assert isinstance(a_class, a_class)
            assert not isinstance(a_class, a_class)
            self.assertIsInstance(a_class, a_class)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Doe'> is
        not an instance of <class 'src.classes.Doe'>

  because a :ref:`class<what is a class?>` is not an instance

* I change assertIsInstance_ to assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 11-12

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
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

* I add another :ref:`assertion<what is an assertion?>`, this time with an instance of ``Doe``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 14-17

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe
            # assert isinstance(a_class, src.person.Person)
            assert not isinstance(a_class, src.person.Person)
            # self.assertIsInstance(a_class, src.person.Person)
            self.assertNotIsInstance(
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

  I made an instance of the ``Doe`` :ref:`class<what is a class?>` and get :ref:`TypeError<what causes TypeError?>` about the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` because ``Doe`` is a child of ``Person``

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add a value for ``first_name``

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 1-2

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('doe')
            assert not isinstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

  because an instance of ``Doe`` is an instance of ``Person`` since ``Person`` is the parent of ``Doe``

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3-4

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('doe')
            # assert not isinstance(
            assert isinstance(
                an_instance, src.person.Person
            )


    # Exceptions seen

  the test passes.

* I add a call to the `assertNotIsInstance method`_

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 7-9

            # instance = src.classes.Doe()
            instance = src.classes.Doe('doe')
            # assert not isinstance(
            assert isinstance(
                instance, src.person.Person
            )
            self.assertNotIsInstance(
                instance, src.person.Person
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
    :lineno-start: 101
    :emphasize-lines: 7-8

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('doe')
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
    :lineno-start: 101
    :emphasize-lines: 12-15

            # an_instance = src.classes.Doe()
            an_instance = src.classes.Doe('doe')
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
    :lineno-start: 112
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

        def test_making_classes_w_inheritance(self):
            a_class = src.classes.Doe

            assert not isinstance(a_class, src.person.Person)
            self.assertNotIsInstance(
                a_class, src.person.Person
            )

            assert not isinstance(a_class, a_class)
            self.assertNotIsInstance(a_class, a_class)

            an_instance = src.classes.Doe('doe')
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


    class Doe(src.person.Person): pass

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_classes_w_inheritance'

:ref:`I can make a class with inheritance<test_making_classes_w_inheritance>`

----

*********************************************************************************
test_family_ties
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a new test for Inheritance_ with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 6-8

            self.assertEqual(
                dir(a_class),
                dir(src.person.Person)
            )

        def test_family_ties(self):
            doe = src.classes.Doe('doe')
            self.assertEqual(doe.last_name, '')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

  because ``Doe`` is an instance of ``Person`` it gets all the :ref:`attributes<what is a class?>` and :ref:`methods<what is a method?>` of ``Person``. I do not need to rewrite an ``__init__`` :ref:`method<what is a method?>` to handle creation of copies of the ``Doe`` :ref:`class<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 112
  :emphasize-lines: 3-4

      def test_family_ties(self):
          doe = src.classes.Doe('first')
          # self.assertEqual(doe.last_name, '')
          self.assertEqual(doe.last_name, 'doe')


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 112
    :emphasize-lines: 6-7
    :emphasize-text: joe

        def test_family_ties(self):
            doe = src.classes.Doe('first')
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
    :emphasize-lines: 4

    class Doe(src.person.Person): pass


    class Blow(src.person.Person): pass

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change ``joe`` to use the new ``Blow`` :ref:`class<what is a class?>`, in :ref:`test_family_ties` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 117
    :emphasize-lines: 1-2
    :emphasize-text: joe

            # joe = src.classes.Doe('joe')
            joe = src.classes.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')


    # Exceptions seen

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I add a :ref:`class attribute<what is a class attribute?>` for ``last_name`` in the ``Blow`` :ref:`class<what is a class?>` in ``classes.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1-2, 4

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        last_name = 'blow'

  the terminal_ does not feel like my friend, it still shows :ref:`AssertionError<what causes AssertionError?>`

* I add the ``__init__`` :ref:`method<what is a method?>` to customize the last name

  .. code-block:: python
    :lineno-start: 16
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

  the test passes.

----

=================================================================================
how to call the parent from the child
=================================================================================

----

* I can also call the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` with the values for ``first_name`` and ``last_name`` directly with the `super built-in function`_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 8-9

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        # last_name = 'blow'

        # def __init__(self):
        def __init__(self, first_name):
            # self.last_name = 'blow'
            super().__init__(first_name, last_name='blow')

  the test passes.

  - the `super built-in function`_ calls the ``__init__`` :ref:`method<what is a method?>` of the parent :ref:`class<what is a class?>` with the values I pass in parentheses.
  - In this case it calls the ``Person`` :ref:`class<what is a class?>` with values for ``first_name`` and ``last_name``
  - this shows that I can define :ref:`classes<what is a class?>` that are related and have their own defaults. In this case the ``Doe`` :ref:`class<what is a class?>` has a default ``last_name`` that is the same as the default last name for ``Person`` and the ``Blow`` :ref:`class<what is a class?>` has a different default ``last_name``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 16

    class Blow(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name, last_name='blow')

* In this case there is a simpler way to make ``joe`` and ``doe``. I could directly pass the values to the ``Person`` :ref:`class<what is a class?>` since all the ``Blow`` :ref:`class<what is a class?>` does is customize the ``last_name`` :ref:`attribute<what is a class attribute?>`, there is nothing special about it or the ``Doe`` :ref:`class<what is a class?>`. I add an :ref:`assertion<what is an assertion?>` to :ref:`test_family_ties` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 117
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
    :lineno-start: 121
    :emphasize-lines: 1-2

            # blow = src.person.Person('joe')
            blow = src.person.Person('joe', last_name='blow')
            self.assertEqual(blow.last_name, joe.last_name)


    # Exceptions seen

  the test passes. I can make instances of :ref:`classes<what is a class?>` by customizing its :ref:`attributes<what is a class attribute?>` without having to make a new :ref:`class<what is a class?>`.

* I add an :ref:`assertion<what is an assertion?>` for ``jane``

  .. code-block:: python
    :lineno-start: 121
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
    :lineno-start: 125
    :emphasize-lines: 2-3

            jane = src.person.Person('jane')
            # self.assertEqual(jane.last_name, blow.last_name)
            self.assertEqual(jane.last_name, doe.last_name)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``john``

  .. code-block:: python
    :lineno-start: 125
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

* I add a new :ref:`class definition<how to make a class>` with a call to the `super built-in function`_ to ``classes.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 7, 9-10

    class Blow(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name, last_name='blow')


    class Smith(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name, last_name='smith')

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_family_ties` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 129
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
    :lineno-start: 132
    :emphasize-lines: 2-3

            smith = src.person.Person('john', 'smith')
            # self.assertEqual(smith.last_name, doe.last_name)
            self.assertEqual(smith.last_name, john.last_name)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 112

        def test_family_ties(self):
            doe = src.classes.Doe('first')
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

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_family_ties'

----

=================================================================================
what happens when the child calls the parent?
=================================================================================

----

* Python_ makes the following calls to resolve a call to make an instance of the ``Blow`` :ref:`class<what is a class?>`

  .. code-block:: python

    joe = src.classes.Blow('joe')
          Blow.__init__('joe')
          super().__init__(first_name, last_name='blow')
        = Person().__init__('joe', last_name='blow')
          joe.first_name = 'joe'
          joe.last_name = 'blow'

* Python_ makes the following calls to resolve a call to make an instance of the ``Smith`` :ref:`class<what is a class?>`

  .. code-block:: python

    john = src.classes.Smith('john')
           Smith.__init__('john')
           super().__init__(first_name, last_name='smith')
         = Person().__init__('john', last_name='smith')
           self.first_name = 'john'
           self.last_name = 'smith'

* Python_ makes the following calls to resolve a call to make instances of the ``Person`` :ref:`class<what is a class?>`

  .. code-block:: python

    blow = src.person.Person('joe', last_name='blow')
           Person.__init__('joe', last_name='blow')
           self.first_name = 'joe'
           self.last_name = 'blow'

  .. code-block:: python

    jane = src.person.Person('jane')
           Person.__init__('jane', last_name='doe')
           self.first_name = 'jane'
           self.last_name = 'doe'

  .. code-block:: python

    smith = src.person.Person('john', 'smith')
          = Person.__init__('john', 'smith')
            self.first_name = 'john'
            self.last_name = 'smith'

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
    :lineno-start: 128
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

I add a :ref:`class<what is a class?>` for ``Jane`` to ``classes.py``

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 7, 9-10

  class Smith(src.person.Person):

      def __init__(self, first_name):
          super().__init__(first_name, last_name='smith')


  class Jane(src.person.Person):

      def __init__(self, first_name='jane'):
          super().__init__(first_name=first_name)

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``jane`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 4

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'jane')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'jane'

* I change the expectation

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 4-5

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            # self.assertEqual(jane.last_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``mary``, another instance of ``Jane``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 7-8

        def test_classes_w_multiple_parents(self):
            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            # self.assertEqual(jane.last_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')

            mary = src.classes.Jane('mary')
            self.assertEqual(mary.first_name, 'jane')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'mary' != 'jane'

* I change the expectation

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 2-3

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, '')
            self.assertEqual(mary.first_name, 'mary')


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``mary``

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 4

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            self.assertEqual(mary.last_name, 'mary')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'mary'

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 137
    :emphasize-lines: 4-5

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the test passes because ``mary`` like ``jane`` is an instance of ``src.classes.Jane``

* I add an :ref:`assertion<what is an assertion?>` for ``joe``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 2-3
    :emphasize-text: Joe

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            self.assertEqual(joe.first_name, 'mary')

            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            # self.assertEqual(jane.last_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        module 'src.classes' has no attribute 'Joe'.
        Did you mean: 'Doe'?

* I add the ``Joe`` :ref:`class<what is a class?>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 7, 9-10

    class Jane(src.person.Person):

        def __init__(self, first_name='jane'):
            super().__init__(first_name=first_name)


    class Joe(src.person.Person):

        def __init__(self, first_name='joe'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'joe' != 'mary'

* I change the expectation in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 3-4

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            # self.assertEqual(joe.first_name, 'mary')
            self.assertEqual(joe.first_name, 'joe')

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to make sure that ``joe`` is a ``Blow``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 5

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            # self.assertEqual(joe.first_name, 'mary')
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add a value for ``last_name`` to ``Joe`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 4-7

    class Joe(src.person.Person):

        def __init__(self, first_name='joe'):
            # super().__init__(first_name=first_name)
            super().__init__(
                first_name=first_name, last_name='blow',
            )

  the test passes. I cheated, which means I need a better test.

* I add assertIsInstance_ to :ref:`test_classes_w_multiple_parents` to make sure ``joe`` is a ``Blow``, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 6

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            # self.assertEqual(joe.first_name, 'mary')
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            self.assertIsInstance(joe, src.classes.Blow)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Joe object at 0xffffabcdef80>
        is not an instance of <class 'src.classes.Blow'>

  better

* I change the parent of ``Joe`` to ``Blow``, in ``classes.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 1-2

    # class Joe(src.person.Person):
    class Joe(Blow):

        def __init__(self, first_name='joe'):
            # super().__init__(first_name=first_name)
            super().__init__(
                first_name=first_name, last_name='blow',
            )

  the test passes.

* I can remove ``last_name`` from the call to the parent

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5-8

    # class Joe(src.person.Person):
    class Joe(Blow):

        def __init__(self, first_name='joe'):
            super().__init__(first_name=first_name)
            # super().__init__(
            #     first_name=first_name, last_name='blow',
            # )

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 28

    class Jane(src.person.Person):

        def __init__(self, first_name='jane'):
            super().__init__(first_name=first_name)


    class Joe(Blow):

        def __init__(self, first_name='joe'):
            super().__init__(first_name=first_name)

  Python_ makes the following calls to resolve the call to make an instance of the ``Joe`` :ref:`class<what is a class?>`

  .. code-block:: python

    joe = src.classes.Joe()
          Joe.__init__(first_name='joe')
          super().__init__(first_name=first_name)
        = Blow().__init__('joe')
          super().__init__(first_name, last_name='blow')
        = Person().__init__('joe', last_name='blow')
          self.first_name = 'joe'
          self.last_name = 'blow'

* I add assertIsInstance_ to :ref:`test_classes_w_multiple_parents` for ``jane`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 131
    :emphasize-lines: 12

        def test_classes_w_multiple_parents(self):
            joe = src.classes.Joe()
            # self.assertEqual(joe.first_name, 'mary')
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            self.assertIsInstance(joe, src.classes.Blow)

            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            # self.assertEqual(jane.last_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsInstance(jane, src.classes.Doe)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Jane object at 0xffffa8b7c6d5>
        is not an instance of <class 'src.classes.Doe'>

* I change the parent of ``Jane`` to ``Doe``, in ``classes.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 1-2

    # class Jane(src.person.Person):
    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name=first_name)

  the test passes.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 22

    class Smith(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name, last_name='smith')


    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name=first_name)

  Python_ makes the following calls to resolve the call to make an instance of the ``Jane`` :ref:`class<what is a class?>`

  .. code-block:: python

    jane = src.classes.Jane()
           Jane.__init__(first_name='jane')
           super().__init__(first_name=first_name)
         = Doe # Doe has no __init__, skip to Person
         = Person().__init__(first_name='jane', last_name='doe')
           self.first_name = 'jane'
           self.last_name = 'doe'

* I add assertNotIsInstance_ to :ref:`test_classes_w_multiple_parents` for ``mary`` to make sure she is a child of ``Jane``, in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 138
    :emphasize-lines: 12

            jane = src.classes.Jane()
            self.assertEqual(jane.first_name, 'jane')
            # self.assertEqual(jane.last_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsInstance(jane, src.classes.Doe)

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            self.assertNotIsInstance(mary, src.classes.Jane)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Jane object at 0xffff0e1d2c3b>
        is an instance of <class 'src.classes.Jane'>

* I change assertNotIsInstance_ to assertIsInstance_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 6-7

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)


    # Exceptions seen

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to show that ``mary`` is a child of ``Doe``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 8

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)
            self.assertNotIsInstance(mary, src.classes.Doe)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Jane object at 0xffff12e3dc45>
        is an instance of <class 'src.classes.Doe'>

  because ``mary`` is an instance of ``Jane`` and the parent of ``Jane`` is ``Doe``

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 8-9

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)
            # self.assertNotIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Doe)


    # Exceptions seen

  the test passes. I can follow the parents all the way back to :ref:`object<what is a class?>` because Python_ makes the following calls to resolve the call to make an instance of the ``Jane`` :ref:`class<what is a class?>`

  .. code-block:: python

    mary = src.classes.Jane('mary')
           Jane.__init__(first_name='jane')
           super().__init__(first_name=first_name)
         = Doe # Doe has no __init__, skip to Person
         = Person().__init__(first_name='mary', last_name='doe')
           self.first_name = 'mary'
           self.last_name = 'doe'

* What if ``mary`` is also a child of ``joe``? I add an :ref:`assertion<what is an assertion?>` to test it

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 10

            mary = src.classes.Jane('mary')
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)
            # self.assertNotIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Joe)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Jane object at 0xffff87a65cb43>
        is not an instance of <class 'src.classes.Joe'>

  ``mary`` is not a child of ``joe``, yet

* I change ``mary`` to be an instance of ``Mary``, a child of ``Jane``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 1-2

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)
            # self.assertNotIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Joe)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Mary'

* I add a :ref:`class definition<how to make a class>` for ``Mary`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 7, 9-10

    class Joe(Blow):

        def __init__(self, first_name='joe'):
            super().__init__(first_name=first_name)


    class Mary(Jane): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Mary object at 0xffffb4c5d6e7>
        is not an instance of <class 'src.classes.Joe'>

* I add ``Joe`` as a parent of ``Mary``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 1-2

    # class Mary(Jane): pass
    class Mary(Joe, Jane): pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError:
        Jane.__init__() got an
        unexpected keyword argument 'last_name'.
        Did you mean 'first_name'?

  because Python_ makes the following calls to resolve the call to make an instance of the ``Mary`` :ref:`class<what is a class?>` if the parents are ``(Joe, Jane)``

  I get the following calls for the ``Joe`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    mary = src.classes.Mary() # Mary has no __init__, skip to Joe
           Joe.__init__()
           super().__init__(first_name=first_name)
         = Blow().__init__(first_name='joe')
           super().__init__(first_name, last_name='blow')
         = Person().__init__('joe', last_name='blow')
           self.first_name = 'joe'
           self.last_name = 'blow'

  then I get the following calls for the ``Jane`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    mary = Jane.__init__(first_name='jane', last_name='blow')

  which raises :ref:`TypeError<what causes TypeError?>` because the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` only takes one :ref:`keyword_argument<test_w_keyword_arguments>` (``first_name``) and the call provides two (``first_name`` and ``last_name``)

* I add a :ref:`double starred expression<double starred expressions>` so that ``Jane`` can take any number of :ref:`keyword arguments<test_w_keyword_arguments>` because I do not want to repeat ``last_name='doe'`` since it is already part of the :ref:`class definition<how to make a class>` of ``Person``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 3-4

    class Jane(Doe):

        # def __init__(self, first_name='jane'):
        def __init__(self, first_name='jane', **kwargs):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'joe' != 'mary'

  because I did not give a value for ``first_name`` when in the :ref:`class definition<how to make a class>` for ``Mary``

* I add a call to the `super built-in function`_ in the ``__init__`` :ref:`method<what is a method?>` of ``Mary``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-3, 5-6

    # class Mary(Jane): pass
    # class Mary(Joe, Jane): pass
    class Mary(Joe, Jane):

        def __init__(self, first_name='mary'):
            super().__init__(first_name=first_name)

  the test passes because Python_ makes the following calls to resolve the call to make an instance of the ``Mary`` :ref:`class<what is a class?>` if the parents are ``(Joe, Jane)``

  I get the following calls for the ``Joe`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    mary = src.classes.Mary()
           Mary.__init__(first_name='mary')
           super().__init__(first_name='mary')
         = Joe.__init__(first_name='mary')
           super().__init__(first_name=first_name)
         = Blow().__init__(first_name='mary')
           super().__init__(first_name, last_name='blow')
         = Person().__init__('mary', last_name='blow')
           self.first_name = 'mary'
           self.last_name = 'blow'

  then I get the following calls for the ``Jane`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    mary = Jane.__init__(first_name='mary', last_name='blow')
           super().__init__(first_name=first_name)
         = Doe # Doe has no __init__, skip to Person
         = Person().__init__(first_name='mary', last_name='doe')
           self.first_name = 'mary'
           self.last_name = 'doe'

  This is a lot to keep track of - knowing the details of ``Jane``, ``Doe``, ``Joe``, ``Blow`` and ``Person`` to understand ``Mary``

* Since ``Joe`` and ``Jane`` are parents of ``Mary``, who does ``Mary`` get her ``last_name`` from? Right now the answer from the calls which is confirmed by the test, is ``Jane``, why is it not ``Joe``? I change the order of the parents of ``Mary``

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 3-4

    # class Mary(Jane): pass
    # class Mary(Joe, Jane): pass
    # class Mary(Joe, Jane):
    class Mary(Jane, Joe):

        def __init__(self, first_name='mary'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blow' != 'doe'

* I change the expectation for the last name of ``mary`` in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 144

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary()
            # self.assertEqual(mary.first_name, 'jane')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, 'mary')
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)
            # self.assertNotIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Joe)


    # Exceptions seen

  the test passes because Python_ makes the following calls to resolve the call to make an instance of the ``Mary`` :ref:`class<what is a class?>` if the parents are ``(Jane, Joe)``

  I get the following calls for the ``Jane`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    mary = Mary.__init__(first_name='mary')
           super().__init__(first_name=first_name)
         = Jane.__init__(first_name='mary')
           super().__init__(first_name=first_name)
         = Doe # Doe has no __init__, skip to Person
         = Person().__init__(first_name='mary', last_name='doe')
           self.first_name = 'mary'
           self.last_name = 'doe'

  then I get the following calls for the ``Joe`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    mary = src.classes.Mary()
           super().__init__(first_name='mary')
         = Joe.__init__(first_name='mary')
           super().__init__(first_name=first_name)
         = Blow().__init__(first_name='mary')
           super().__init__(first_name, last_name='blow')
         = Person().__init__('mary', last_name='blow')
           self.first_name = 'mary'
           self.last_name = 'blow'

  - This test shows that the order the parent is given matters.
  - It also misses something about the ``Jane`` :ref:`class<what is a class?>` - the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` never calls ``super().__init__`` with a value for ``last_name`` which means it will always use ``'doe'`` because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_w_optional_arguments>`.

* I add a :ref:`double starred expression<double starred expressions>` so that ``Jane`` calls ``super().__init__`` with any number of :ref:`keyword arguments<test_w_keyword_arguments>` the ``__init__`` :ref:`method<what is a method?>` get s

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-6

    class Jane(Doe):

        # def __init__(self, first_name='jane'):
        def __init__(self, first_name='jane', **kwargs):
            # super().__init__(first_name=first_name)
            super().__init__(first_name=first_name, **kwargs)

  the test is still green

* I change the order of the parents of ``Mary``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2-3

    # class Mary(Jane): pass
    class Mary(Joe, Jane): pass
    # class Mary(Jane, Joe): pass

  the test is still green. It looks like the order does not have the effect I thought it did. What causes the ``last_name`` of ``mary`` to be ``blow`` when I :ref:`define<how to make a class>` the parents as ``(Joe, Jane)`` or ``(Jane, Joe)``?

* I add ``john`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 144
    :emphasize-lines: 14-15

            # mary = src.classes.Jane('mary')
            mary = src.classes.Mary('mary')
            # self.assertEqual(mary.first_name, '')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, '')
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # self.assertNotIsInstance(mary, src.classes.Jane)
            self.assertIsInstance(mary, src.classes.Jane)
            # self.assertNotIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Doe)
            self.assertIsInstance(mary, src.classes.Joe)

            john = src.classes.John()
            self.assertEqual(john.first_name, 'mary')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'John'

* I add a :ref:`class definition<how to make a class>` for ``John`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 42

    # class Mary(Jane): pass
    class Mary(Joe, Jane): pass
    # class Mary(Jane, Joe): pass

    class John(src.person.Person):

        def __init__(self, first_name='john'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'john' != 'mary'

* I change the expectation in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 2-3

            john = src.classes.John()
            # self.assertEqual(john.first_name, 'mary')
            self.assertEqual(john.first_name, 'john')


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to make sure that ``John`` is a ``Smith``

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 4

            john = src.classes.John()
            # self.assertEqual(john.first_name, 'mary')
            self.assertEqual(john.first_name, 'john')
            self.assertIsInstance(john, src.classes.Smith)


    # Exceptions seen

  the terminal_ is my friend, and shows

  .. code-block:: shell

    AssertionError: <src.classes.John object at 0xffffa012b3c4>
    is not an instance of <class 'src.classes.Smith'>

  no cheating this time.

* I change the parent of ``John`` to ``Smith`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 1-2

    # class John(src.person.Person):
    class John(Smith):

        def __init__(self, first_name='john'):
            super().__init__(first_name=first_name)

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``last_name`` to :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 4

            john = src.classes.John()
            # self.assertEqual(john.first_name, 'mary')
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'john')
            self.assertIsInstance(john, src.classes.Smith)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != 'john'

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 4-5

            john = src.classes.John()
            # self.assertEqual(john.first_name, 'mary')
            self.assertEqual(john.first_name, 'john')
            # self.assertEqual(john.last_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertIsInstance(john, src.classes.Smith)


    # Exceptions seen

  the test passes.

* I remove the commented line from ``John`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 42

    # class Mary(Jane): pass
    class Mary(Joe, Jane): pass
    # class Mary(Jane, Joe): pass

    class John(Smith):

        def __init__(self, first_name='john'):
            super().__init__(first_name=first_name)

* I add another person, a child of ``john`` in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 157
    :emphasize-lines: 8-9

            john = src.classes.John()
            # self.assertEqual(john.first_name, 'mary')
            self.assertEqual(john.first_name, 'john')
            # self.assertEqual(john.last_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertIsInstance(john, src.classes.Smith)

            lil = src.classes.Lil()
            self.assertEqual(lil.first_name, 'john')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Lil'

* I add a :ref:`class definition<how to make a class>` for ``Lil`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 7, 9-10

    class John(Smith):

        def __init__(self, first_name='john'):
            super().__init__(first_name=first_name)


    class Lil(John):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'lil' != 'john'

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_classes_w_multiple_parents` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 164

            lil = src.classes.Lil()
            # self.assertEqual(lil.first_name, 'john')
            self.assertEqual(lil.first_name, 'lil')


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``lil``

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 4

            lil = src.classes.Lil()
            # self.assertEqual(lil.first_name, 'john')
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
            # self.assertEqual(lil.first_name, 'john')
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, lil.first_name)
            self.assertEqual(lil.last_name, john.last_name)


    # Exceptions seen

  the test passes.

* I add assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 6

            lil = src.classes.Lil()
            # self.assertEqual(lil.first_name, 'john')
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, lil.first_name)
            self.assertEqual(lil.last_name, john.last_name)
            self.assertNotIsInstance(lil, src.classes.John)


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <src.classes.Lil object at 0xffffabcdef00>
    is an instance of <class 'src.classes.John'>

* I change assertNotIsInstance_ to assertIsInstance_ to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 6-7

            lil = src.classes.Lil()
            # self.assertEqual(lil.first_name, 'john')
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, lil.first_name)
            self.assertEqual(lil.last_name, john.last_name)
            # self.assertNotIsInstance(lil, src.classes.John)
            self.assertIsInstance(lil, src.classes.John)


    # Exceptions seen

  the test passes

* I add assertIsInstance_ to test if ``Lil`` is an instance of ``Mary``

  .. code-block:: python
    :lineno-start: 164
    :emphasize-lines: 8

            lil = src.classes.Lil()
            # self.assertEqual(lil.first_name, 'john')
            self.assertEqual(lil.first_name, 'lil')
            # self.assertEqual(lil.last_name, lil.first_name)
            self.assertEqual(lil.last_name, john.last_name)
            # self.assertNotIsInstance(lil, src.classes.John)
            self.assertIsInstance(lil, src.classes.John)
            self.assertIsInstance(lil, src.classes.Mary)


    # Exceptions

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <src.classes.Lil object at 0xffffaaaaaaaa>
    is not an instance of <class 'src.classes.Mary'>

* I add ``Mary`` as a parent of ``Lil`` before ``John`` to see if that will also change the ``last_name`` value, in ``classes.py``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 1-2

    # class Lil(John):
    class Lil(Mary, John):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: John.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I add a :ref:`double starred expression<double starred expressions>` to ``John`` so it can take any number of :ref:`keyword arguments<test_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 3-6

    class John(Smith):

        # def __init__(self, first_name='john'):
        def __init__(self, first_name='john', **kwargs):
            # super().__init__(first_name=first_name)
            super().__init__(first_name=first_name, **kwargs)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Smith.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  same problem, same solution

* I add a :ref:`double starred expression<double starred expressions>` to ``Smith`` so it can take any number of :ref:`keyword arguments<test_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-4

    class Smith(src.person.Person):

        # def __init__(self, first_name):
        def __init__(self, first_name, **kwargs):
            super().__init__(first_name, last_name='smith')

  the test passes.

* I change the order of the parents of ``Lil``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 1-2

    # class Lil(Mary, John):
    class Lil(John, Mary):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Joe.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  same problem, same solution

* I add a :ref:`double starred expression<double starred expressions>` to ``Joe`` so it can take any number of :ref:`keyword arguments<test_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 3-6

    class Joe(Blow):

        # def __init__(self, first_name='joe'):
        def __init__(self, first_name='joe', **kwargs):
            # super().__init__(first_name=first_name)
            super().__init__(first_name=first_name, **kwargs)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Blow.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

  same problem, ...

* I add a :ref:`double starred expression<double starred expressions>` to ``Blow`` so it can take any number of :ref:`keyword arguments<test_w_keyword_arguments>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 3-4

    class Blow(src.person.Person):

        # def __init__(self, first_name):
        def __init__(self, first_name, **kwargs):
            super().__init__(first_name, last_name='blow')

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blow' != 'smith'

  okay! It looks like the order of the parents matter when a call to ``super().__init__`` is made in the ``__init__`` :ref:`method<what is an assertion>`

* I change the order of the parents of ``Lil`` back to ``Mary, John``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 1-2

    class Lil(Mary, John):
    # class Lil(John, Mary):

        def __init__(self, first_name='lil'):
            super().__init__(first_name=first_name)

  the test passes. The test shows that

  - if the parents of ``Lil`` are defined as ``(Mary, John)`` the default value for ``last_name`` is the value for ``last_name`` of ``John``
  - if the parents of ``Lil`` are defined as ``(John, Mary)`` the default value for ``last_name`` is the value for the ``last_name`` of ``Mary``

----

---------------------------------------------------------------------------------
what happens when the child calls the parent?
---------------------------------------------------------------------------------

----

* if the order of the parents of ``Lil`` is ``(Mary, John)`` then we get the following calls for the ``Mary`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = src.classes.Lil()
          super().__init__(first_name='lil')
        = Mary.__init__(first_name='lil')
          super().__init__(first_name=first_name)
        = Joe.__init__(first_name='lil', **kwargs)
          super().__init__(first_name=first_name, **kwargs)
        = Blow().__init__(first_name='lil', **kwargs)
          super().__init__(first_name, last_name='blow')
        = Person().__init__(first_name='lil', last_name='blow')
          self.first_name = 'lil'
          self.last_name = 'blow'

  this resolves the ``Mary`` parent.

  We get the following calls for the ``John`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = John.__init__(first_name='lil', last_name='blow')
          super().__init__(first_name=first_name, **kwargs)
        = Smith.__init(first_name='lil', last_name='blow')
          super().__init__(first_name, last_name='smith')
        = Person().__init__('lil', last_name='smith')
          self.first_name = 'lil'
          self.last_name = 'smith'

  this resolves the ``John`` parent. If the order of the parents is ``(Mary, John)`` the value for ``last_name`` is the value of ``John.last_name``

* if the order of the parents of ``Lil`` is ``(John, Mary)`` then we get the following calls for the ``John`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = src.classes.Lil()
          super().__init__(first_name='lil')
        = John.__init__(first_name='lil', **kwargs)
          super().__init__(first_name=first_name, **kwargs)
        = Smith.__init__(first_name='lil', **kwargs)
          super().__init__(first_name, last_name='smith')
        = Person().__init__(first_name='lil', last_name='smith')
          self.first_name = 'lil'
          self.last_name = 'smith'

  this resolves the ``John`` parent.

  We get the following calls for the ``Mary`` parent, to resolve the :ref:`attributes<what is a class attribute?>`

  .. code-block:: python

    lil = Mary.__init__(first_name='lil', last_name='smith')
          super().__init__(first_name=first_name)
        = Smith.__init(first_name='lil', last_name='blow')
          super().__init__(first_name, last_name='smith')
        = Person().__init__('lil', last_name='smith')
          self.first_name = 'lil'
          self.last_name = 'smith'

  this resolves the ``Mary`` parent. If the order of the parents is ``(John, Mary)`` the value for ``last_name`` is the value of ``Mary.last_name``



* I change the order of the parents of ``Mary`` to ``(Jane, Joe)`` to see if there is a difference now

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2-3

    # class Mary(Jane): pass
    # class Mary(Joe, Jane): pass
    class Mary(Jane, Joe): pass

  the test is still green

* I change the order back to ``(Joe, Jane)``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2-3

    # class Mary(Jane): pass
    class Mary(Joe, Jane): pass
    # class Mary(Jane, Joe): pass

* I add a call to the `super built-in function`_ in ``Mary``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2, 4, 6-7

    # class Mary(Jane): pass
    # class Mary(Joe, Jane): pass
    # class Mary(Jane, Joe): pass
    class Mary(Joe, Jane):

        def __init__(self, first_name='mary'):
            super().__init__(first_name=first_name)

  the test is still green

* I add a call to the `super built-in function`_ in ``Doe``

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2, 4, 6-7

    # class Mary(Jane): pass
    # class Mary(Joe, Jane): pass
    # class Mary(Jane, Joe): pass
    class Mary(Joe, Jane):

        def __init__(self, first_name='mary'):
            super().__init__(first_name=first_name)

  the test is still green


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

:ref:`Would you like to test if bool_ is an int_?<booleans 3: values of True and False>`

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