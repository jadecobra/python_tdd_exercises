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

* I add an `import statement`_ for the ``classes`` :ref:`module<what is a module?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.classes
    import unittest


    class TestClasses(unittest.TestCase):

  ``import src.classes`` brings in an :ref:`object<what is a class?>` that represents the ``classes.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_classes.py``

----

=================================================================================
how to test if something is NOT an instance of a class
=================================================================================

----

I can test if an :ref:`object<what is a class?>` is a child (instance) of another :ref:`object<what is a class?>` or NOT with the `isinstance built-in function`_ from `The Python Standard Library`_, it checks if the item in the parentheses on the left is an instance of the :ref:`class<what is a class?>` on the right

* I change ``test_failure`` to :ref:`test_making_a_class_w_pass` then add an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-6

    class TestClasses(unittest.TestCase):

        def test_making_a_class_w_pass(self):
            assert not isinstance(
                src.classes.WPass, object
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes'
                    has no attribute 'WPass'

  because there is no definition for ``WPass`` in ``classes.py``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use the :ref:`Explorer<explorer on left>` to open ``classes.py`` from the ``src`` folder_ in the :ref:`editor<2 editors>`

* then I add a :ref:`class<what is a class?>` definition for ``WPass`` to ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 3

    class WPass:

        pass

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


  * the :ref:`assertion<what is an assertion?>` - ``assert isinstance(src.classes.WPass, object)`` checks if the result of a call to ``WPass`` in ``src.classes.py`` in the ``src`` folder_ also known as ``src.classes.WPass``, is an instance of the :ref:`object class<what is a class?>` which is the mother of all :ref:`classes<what is a class?>`

  * the :ref:`class definition<how to make a class>` simply says pass_ and the test passes.
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body)
  * the test passes because :ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`, which leads me to the next test, but first git_ business

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

  the test passes

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
    :emphasize-lines: 6, 8

    class WPass:

        pass


    class WParentheses:

        pass

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
    :lineno-start: 6
    :emphasize-lines: 1-2
    :emphasize-text: ( )

    # class WParentheses:
    class WParentheses():

        pass

  * the :ref:`assertion<what is an assertion?>` - ``assert isinstance(src.classes.WParentheses, object)`` checks if the result of a call to ``WParentheses`` in ``src.classes.py`` in the ``src`` folder_ also known as ``src.classes.WParentheses``, is an instance of the :ref:`object class<what is a class?>` which is the mother of all :ref:`classes<what is a class?>`

  * this :ref:`class definition<how to make a class>` has parentheses after the name
  * the :ref:`class definition<how to make a class>` simply says pass_ and the test passes
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body)
  * the test is still green because :ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`

* I remove the commented line

  .. code-block:: python
    :linenos:

    class WPass:

        pass


    class WParentheses():

        pass

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

I add a test with an :ref:`assertion<what is an assertion?>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 4-5

      def test_making_a_class_w_parentheses(self):
          self.assertIsInstance(src.classes.WParentheses, object)

      def test_making_a_class_w_object(self):
          self.assertIsInstance(src.classes.WObject, object)


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
    :lineno-start: 6
    :emphasize-lines: 6, 8

    class WParentheses():

        pass


    class WObject():

        pass

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
                src.classes.WObject(), object
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
    :lineno-start: 11
    :emphasize-lines: 1-2
    :emphasize-text: object

    # class WObject():
    class WObject(object):

        pass

  the test is still green. :ref:`I can make a class with object<test_making_a_class_w_object>`

* I remove the commented line

  .. code-block:: python
    :lineno-start: 6

    class WParentheses():

        pass


    class WObject(object):

        pass

* I add an :ref:`assertion<what is an assertion?>` with the `assertNotIsInstance method`_ to :ref:`test_making_a_class_w_object` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 23
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
        <src.classes.WObject object at 0xffffcd781234>
        is an instance of <class 'object'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 23
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


    # Exceptions

  the test passes. I have three different :ref:`classes<what is a class?>`, and the tests show that they are all instances of the :ref:`object class<what is a class?>`

  .. code-block:: python

    class WPass: pass

  .. code-block:: python

    class WParentheses(): pass



  .. code-block:: python

    class WObject(object): pass

  their :ref:`definitions<how to make a class>` are different, their results are the same because ":ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`"

  I like to write my :ref:`classes<what is a class?>` with ``(object)``, so that anyone can see what the :ref:`class<what is a class?>` inherits from without having to think about it.

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

  because :ref:`None<what is None?>` is an :ref:`object<what is a class?>`

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

  because :ref:`None<what is None?>` is an :ref:`object<what is a class?>`

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

  because :ref:`bool<what are booleans?>` is an :ref:`object<what is a class?>`

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

  because :ref:`bool<what are booleans?>` is an :ref:`object<what is a class?>`

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

  because int_ is an :ref:`object<what is a class?>`

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

  because int_ is an :ref:`object<what is a class?>`

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

  because float_ is an :ref:`object<what is a class?>`

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

  because float_ is an :ref:`object<what is a class?>`

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

  because str_ is an :ref:`object<what is a class?>`

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

  because str_ is an :ref:`object<what is a class?>`

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

  because tuple_ is an :ref:`object<what is a class?>`

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

  because tuple_ is an :ref:`object<what is a class?>`

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

  because :ref:`list<what is a list?>` is an :ref:`object<what is a class?>`

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

  because :ref:`list<what is a list?>` is an :ref:`object<what is a class?>`

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

  because set_ is an :ref:`object<what is a class?>`

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

  because set_ is an :ref:`object<what is a class?>`

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

  because :ref:`dict<what is a dictionary?>` is an :ref:`object<what is a class?>`

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

  because :ref:`dict<what is a dictionary?>` is an :ref:`object<what is a class?>`

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
                src.classes.WObject(), object
            )
            self.assertIsInstance(
                src.classes.WObject(), object
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

:ref:`all classes inherit from 'object' by default<test_making_a_class_w_object>`

----

*********************************************************************************
test_attributes_and_methods_of_objects
*********************************************************************************

In :ref:`test_attributes_and_methods_of_person_class` I saw the :ref:`methods<what is a method?>` I added to the ``Person`` :ref:`class<what is a class?>` and also names that I did not add, which led to the question of where they came from.

I want to test the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`object class<what is a class?>`

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

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

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
          doe = src.classes.Doe
          assert isinstance(doe, src.person.Person)


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
    :lineno-start: 11
    :emphasize-lines: 6, 8

    class WObject(object):

        pass


    class Doe(object):

        pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

  because even though ``Doe`` and ``Person`` are children of :ref:`object<what is a class?>`, ``Doe`` is not an instance of ``Person``

* I change the parent of ``Doe``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 1-2

    # class Doe(object):
    class Doe(person.Person):

        pass

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

  because there is no definition for ``person`` in this file_

* I add an `import statement`_ at the top of ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import person


    class WPass:

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


    class WPass:

  the terminal_ does not feel like my friend, it goes back to :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

* I add ``src.`` to the parent of ``Doe``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 1-2

    # class Doe(object):
    class Doe(src.person.Person):

        pass

  the terminal_ definitely does not feel like my friend, it goes back to :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert False

  because ``Doe`` is still not an instance of ``Person`` even though I defined ``Person`` as the parent of ``Doe``

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_classes_w_inheritance` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 3-4

        def test_making_classes_w_inheritance(self):
            doe = src.classes.Doe
            # assert isinstance(doe, src.person.Person)
            assert not isinstance(doe, src.person.Person)


    # Exceptions seen

  the test passes.

  * ``import src.person`` brings in an :ref:`object<what is a class?>` that represents the ``person.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``classes.py``
  * I have to use ``src.person.Person`` in ``classes.py`` because I am testing from ``test_classes.py`` in the ``tests`` folder_
  * The test needs to know where ``person.py`` is in relation to where ``test_classes.py`` is
  * This is a problem because if ``classes.py`` is run from inside ``src`` because the `import statement`_ will not be able to find ``src.person`` from inside ``src``. That is a problem for another time.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to the `assertIsInstance method`_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 4-5

        def test_making_classes_w_inheritance(self):
            doe = src.classes.Doe
            # assert isinstance(doe, src.person.Person)
            assert not isinstance(doe, src.person.Person)
            self.assertIsInstance(doe, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.Doe'> is
        not an instance of <class 'src.person.Person'>

* I change assertIsInstance_ to assertNotIsInstance_

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 5-6

        def test_making_classes_w_inheritance(self):
            doe = src.classes.Doe
            # assert isinstance(doe, src.person.Person)
            assert not isinstance(doe, src.person.Person)
            # self.assertIsInstance(doe, src.person.Person)
            self.assertNotIsInstance(doe, src.person.Person)


    # Exceptions seen

  the test passes. When is ``Doe`` an instance of ``Person``?

* I add another :ref:`assertion<what is an assertion?>`, this time with an instance of ``Doe``

  .. code-block:: python
    :lineno-start: 88
    :emphasize-lines: 8-9

        def test_making_classes_w_inheritance(self):
            doe = src.classes.Doe
            # assert isinstance(doe, src.person.Person)
            assert not isinstance(doe, src.person.Person)
            # self.assertIsInstance(doe, src.person.Person)
            self.assertNotIsInstance(doe, src.person.Person)

            doe = src.classes.Doe('doe')
            assert not isinstance(doe, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

  because an instance of ``Doe`` is an instance of ``Person`` since ``Person`` is the parent of ``Doe``

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 2-3

            doe = src.classes.Doe('doe')
            # assert not isinstance(doe, src.person.Person)
            assert isinstance(doe, src.person.Person)


    # Exceptions seen

  the test passes

* I add a call to the `assertNotIsInstance method`_

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 4

            doe = src.classes.Doe('doe')
            # assert not isinstance(doe, src.person.Person)
            assert isinstance(doe, src.person.Person)
            self.assertNotIsInstance(doe, src.person.Person)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <src.classes.Doe object at 0xffff01a2bc34> is
        an instance of <class 'src.person.Person'>

* I change assertNotIsInstance_ to assertIsInstance_

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 4-5

            doe = src.classes.Doe('doe')
            # assert not isinstance(doe, src.person.Person)
            assert isinstance(doe, src.person.Person)
            # self.assertNotIsInstance(doe, src.person.Person)
            self.assertIsInstance(doe, src.person.Person)


    # Exceptions seen

  the test passes.

* I add a test for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the ``Doe`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 7-10

            doe = src.classes.Doe('doe')
            # assert not isinstance(doe, src.person.Person)
            assert isinstance(doe, src.person.Person)
            # self.assertNotIsInstance(doe, src.person.Person)
            self.assertIsInstance(doe, src.person.Person)

            self.assertEqual(
                dir(src.classes.Doe),
                []
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: Lists differ:
        ['__class__', '__delattr__', '__dict__', '[370 chars]llo']
     != []

* I change the expectation

  .. code-block:: python
    :lineno-start: 101
    :emphasize-lines: 3-4

            self.assertEqual(
                dir(src.classes.Doe),
                # []
                dir(src.person.Person),
            )


    # Exceptions seen

  the test passes because ``Doe`` has the same :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` as ``Person`` even though there is nothing in the :ref:`class definition<how to make a class>` for ``Doe`` except stating its parent

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 88

        def test_making_classes_w_inheritance(self):
            doe = src.classes.Doe
            assert not isinstance(doe, src.person.Person)
            self.assertNotIsInstance(doe, src.person.Person)

            doe = src.classes.Doe('doe')
            assert isinstance(doe, src.person.Person)
            self.assertIsInstance(doe, src.person.Person)

            self.assertEqual(
                dir(src.classes.Doe),
                dir(src.person.Person),
            )


    # Exceptions seen

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

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I change the expectation

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 1

            self.assertEqual(jane.last_name, 'doe')

  the test passes.

* I add one more :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 2

            self.assertEqual(jane.last_name, 'doe')
            self.assertEqual(john.last_name, '')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Smith'

* I add a :ref:`class<what is a class?>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 2

    class Doe(src.person.Person): pass
    class Smith(src.person.Person): pass

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``last_name`` of ``mary``

  .. code-block:: python
    :lineno-start: 66

            self.assertEqual(john.last_name, 'doe')
            self.assertEqual(mary.last_name, '')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* ``mary`` should have a last name of ``smith`` not ``doe``. I change the expectation

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 1

            self.assertEqual(mary.last_name, 'smith')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'smith'

* I add a value for ``last_name`` to the ``Smith`` :ref:`class<what is a class?>` in ``classes.py``

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 1, 3-4

    class Smith(src.person.Person):

        def __init__(self, first_name, last_name='smith'):
            pass

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Smith' object has no attribute 'last_name'

* I need to add the :ref:`class attributes<test_attribute_error_w_class_attributes>`. I can do that by calling the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>`. Python_ has a way for me to do that, I add it

  .. code-block:: python
    :lineno-start: 21
    :emphasize-lines: 4

    class Smith(src.person.Person):

        def __init__(self, first_name, last_name='smith'):
            super().__init__(first_name, last_name)

  the test passes.

  the `super built-in function`_ calls the ``__init__`` :ref:`method<what is a method?>` of the parent :ref:`class<what is a class?>` with the values I pass in parentheses.

  In this case it calls the ``Person`` :ref:`class<what is a class?>` with values for ``first_name`` and ``last_name``

* I add another person to ``test_classes.py``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 3

            john = src.classes.Doe('john')
            mary = src.classes.Smith('mary')
            joe = src.classes.Blow('joe')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Blow'

* I add the :ref:`class<what is a class?>` to ``classes.py``

  .. code-block:: python
    :lineno-start: 21

    class Smith(src.person.Person):

        def __init__(self, first_name, last_name='smith'):
            super().__init__(first_name, last_name)

    class Blow(src.person.Person): pass

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the last name of ``joe``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 3

            self.assertEqual(john.last_name, 'doe')
            self.assertEqual(mary.last_name, 'smith')
            self.assertEqual(joe.last_name, 'blow')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add the ``__init__`` :ref:`method<what is a method?>` to the class

  .. code-block:: python
    :lineno-start: 26

    class Blow(src.person.Person):

        def __init__(self, first_name, last_name='blow'):
            pass

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Blow' object has no attribute 'last_name'

* I use the `super built-in function`_

  .. code-block:: python
    :lineno-start: 26

    class Blow(src.person.Person):

        def __init__(self, first_name, last_name='blow'):
            super().__init__(first_name, last_name)

  the test passes.

* I add a new person who is a child of ``jane`` named ``baby`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 2

            joe = src.classes.Blow('joe')
            baby = src.classes.Baby('baby')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Baby'

* I add a :ref:`class<what is a class?>` for ``baby`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 7

    class Blow(src.person.Person):

        def __init__(self, first_name, last_name='blow'):
            super().__init__(first_name, last_name)


    class Baby(Doe): pass

  the test passes.

* ``baby`` is also the child of ``joe``. I add an :ref:`assertion<what is an assertion?>` for the last name of ``baby`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 3

            self.assertEqual(mary.last_name, 'smith')
            self.assertEqual(joe.last_name, 'blow')
            self.assertEqual(baby.last_name, 'blow')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add another parent to the ``Baby`` :ref:`class<what is a class?>` in ``classes.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 1

    class Baby(Blow, Doe): pass

  the test passes.

* I add another person, a child of ``john`` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3

            joe = src.classes.Blow('joe')
            baby = src.classes.Baby('baby')
            lil = src.classes.Lil('lil')

            self.assertEqual(doe.last_name, 'doe')

  the terminal_ is my friend, and shows :ref:`AttributError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.classes' has no attribute 'Lil'

* I add a :ref:`class<what is a class?>` for ``lil`` to ``classes.py``

  .. code-block:: python
    :lineno-start: 33
    :emphasize-lines: 4

    class Baby(Blow, Doe): pass


    class Lil(Doe): pass

  the test passes.

* ``lil`` is also the child of ``mary``. I add an :ref:`assertion<what is an assertion?>` for the last name of ``lil``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3

            self.assertEqual(joe.last_name, 'blow')
            self.assertEqual(baby.last_name, 'blow')
            self.assertEqual(lil.last_name, '')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I add another parent to show that ``lil`` is a child of ``Doe`` and ``Smith`` in ``classes.py``

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 1

    class Lil(Doe, Smith): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

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

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe.__init__() takes 2 positional arguments but 3 were given

  because the ``Baby`` class passes a value for ``last_name``

* I add ``last_name`` to the call to ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3-4

    class Doe(src.person.Person):

        def __init__(self, first_name, last_name='doe'):
            super().__init__(first_name, last_name)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != ''

* I change the expectation in ``test_classes.py``

  .. code-block:: python

            self.assertEqual(lil.last_name, 'doe')

  the test passes.

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