.. meta::
  :description: Step-by-step Python TDD tutorial for beginners explaining why everything in Python inherits from the base 'object' class. Learn how to use isinstance() and issubclass() in unittest, and understand the difference between subclasses and instances. Verify that None, bool, int, float, str, tuple, list, set, and dict are all children of object. Learn to inspect built-in classes with dir(object) and understand the inherited dunder methods. Resolve common beginner bugs: TypeError: issubclass() arg 1 must be a class, NameError: name 'src' is not defined, AttributeError: module has no attribute, and NameError: name 'E' is not defined.
  :keywords: Jacob Itegboje, Pumping Python, python inheritance tutorial for beginners, everything in python is an object, why does all python classes inherit from object, is None an instance of object, is bool a subclass of object python, is int a subclass of object python, is float a subclass of object python, is str a subclass of object python, is list a subclass of object python, is tuple a subclass of object python, is set a subclass of object python, is dict a subclass of object python, difference between subclass and instance python, python isinstance vs issubclass tutorial, unittest assertIsInstance, unittest assertNotIsInstance, unittest assertIsSubclass, unittest assertNotIsSubclass, how to use dir on object class python, dunder methods of object class python, python object __init__ dunder, python object __str__ dunder, python object __repr__ dunder, TypeError issubclass arg 1 must be a class, NameError name src is not defined, AttributeError module classes has no attribute, AssertionError assert not True, NameError name E is not defined pytest, python test driven development classes object, class vs instance parentheses python, learning python dunder class doc init repr str

.. include:: ../links.rst

.. _isinstance: https://docs.python.org/3/library/functions.html#isinstance
.. _isinstance built-in function: isinstance_
.. _assertNotIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertNotIsInstance
.. _unittest.TestCase.assertNotIsInstance: assertNotIsInstance_
.. _assertNotIsInstance method: assertNotIsInstance_
.. _assertIsInstance: https://docs.python.org/3/library/unittest.html?highlight=unittest#unittest.TestCase.assertIsInstance
.. _unittest.TestCase.assertIsInstance: assertIsInstance_
.. _assertIsInstance method: assertIsInstance_
.. _issubclass: https://docs.python.org/3/library/functions.html#issubclass
.. _issubclass built-in function: issubclass_
.. _assertNotIsSubclass: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsSubclass
.. _assertNotIsSubclass method: assertNotIsSubclass_
.. _unittest.TestCase.assertNotIsSubclass: assertNotIsSubclass_
.. _assertIsSubclass: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsSubclass
.. _assertIsSubclass method: assertIsSubclass_
.. _unittest.TestCase.assertIsSubclass: assertIsSubclass_


#################################################################################
everything is an object
#################################################################################

The :ref:`object class<what is a class?>` is the mother of all things in Python_.

----

*********************************************************************************
questions about classes
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`how can I make a class with pass?<test_making_a_class_w_pass>`
* :ref:`how can I make a class with parentheses?<test_making_a_class_w_parentheses>`
* :ref:`how can I make a class with object?<test_making_a_class_w_object>`
* :ref:`is None an object?<test_is_none_an_object>`
* :ref:`is a boolean an object?<test_is_a_boolean_an_object>`
* :ref:`is an integer an object?<test_is_an_integer_an_object>`
* :ref:`is a float an object?<test_is_a_float_an_object>`
* :ref:`is a string an object?<test_is_a_string_an_object>`
* :ref:`is a tuple an object?<test_is_a_tuple_an_object>`
* :ref:`is a list an object?<test_is_a_list_an_object>`
* :ref:`is a set an object?<test_is_a_set_an_object>`
* :ref:`is a dictionary an object?<test_is_a_dictionary_an_object>`
* :ref:`what is the difference between an instance and a subclass?<instance vs subclass>`
* :ref:`what do all Python objects inherit from?<everything is an object>`

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_classes.py
  :language: python
  :linenos:

----

*********************************************************************************
requirements
*********************************************************************************

* :ref:`how to make a person`
* :ref:`what is a class?`

----

*********************************************************************************
continue the project
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

* I open ``test_classes.py``

* I add :ref:`the first failing test<test_failure>` to ``test_classes.py``

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

    ============================ FAILURES ==========================
    ___________________ TestClasses.test_failure ___________________

    self = <tests.test_classes.TestClasses testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_classes.py:7: AssertionError
    =================== short test summary info ====================
    FAILED tests/test_classes.py::TestClasses::test_failure - AssertionError: True is not false
    ================= 1 failed, 6 passed in X.YZs ==================

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestClasses(unittest.TestCase):

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

.. code-block:: python

  class NameOfClass(ParentClass):

      attribute = SOMETHING

      def method():
          the body of the method
          ...

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

---------------------------------------------------------------------------------
how to test if something is NOT an instance of a class
---------------------------------------------------------------------------------

----

I can test if an :ref:`object<what is a class?>` is :ref:`an instance (a copy)<how to test if something is an instance of a class>` of another :ref:`object<what is a class?>` or NOT with the `isinstance built-in function`_ from `The Python Standard Library`_.

isinstance_ checks if the thing in the parentheses on the left is an :ref:`instance (a copy)<how to test if something is an instance of a class>` of the :ref:`class<what is a class?>` on the right in the parentheses.

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

  - ``import src.classes`` brings in an :ref:`object<what is a class?>` for the ``classes.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_classes.py``
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

* I open ``classes.py`` from the ``src`` folder_

* then I add a :ref:`class<what is a class?>` definition for ``WPass`` to ``classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    class WPass: pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: python

    AssertionError: assert not True

  because the statement ``not isinstance(src.classes.WPass(), object)`` is :ref:`False<test_what_is_false>`.

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

The `unittest.TestCase class`_ has two :ref:`methods<what is a method?>` I can also use to test if an :ref:`object<what is a class?>` is :ref:`an instance (a copy) of a class<how to test if something is an instance of a class>` or NOT - assertIsInstance_ and assertNotIsInstance_

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
    :emphasize-lines: 3-4, 6-8, 10-12

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)
            # assert not isinstance(
            # assert isinstance(
            #     src.classes.WPass(), object
            # )
            # self.assertNotIsInstance(
            # self.assertIsInstance(
            #     src.classes.WPass(), object
            # )


    # Exceptions seen

  the test is still green.

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

  because the statement ``not isinstance(src.classes.WParentheses(), object)`` is :ref:`False<test_what_is_false>`.

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_parentheses` to make the statement :ref:`True<test_what_is_true>`, in ``test_classes.py``

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

* I add parentheses to the :ref:`definition<how to make a class>` of ``WParentheses`` in ``classes.py``

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
    :emphasize-lines: 3-4, 6-8, 10-12

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)
            # assert not isinstance(
            # assert isinstance(
            #     src.classes.WParentheses(), object
            # )
            # self.assertNotIsInstance(
            # self.assertIsInstance(
            #     src.classes.WParentheses(), object
            # )


    # Exceptions seen

  the test is still green.

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

because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`, which leads me to the next test.

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
    :emphasize-lines: 3-4, 6-8, 10-12

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)
            # assert not isinstance(
            # assert isinstance(
            #     src.classes.WObject(), object
            # )
            # self.assertNotIsInstance(
            # self.assertIsInstance(
            #     src.classes.WObject(), object
            # )


    # Exceptions seen

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_object'

I have three different :ref:`classes<what is a class?>`, and the tests show that they are all instances of the :ref:`object class<what is a class?>`

.. code-block:: python

  class WPass: pass

.. code-block:: python

  class WParentheses(): pass

.. code-block:: python

  class WObject(object): pass

their :ref:`definitions<how to make a class>` are different, their results are the same because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

I like to write my :ref:`classes<what is a class?>` with ``(object)``, so that anyone can see what the parent :ref:`class<what is a class?>` is without thinking about it.

:ref:`I can make a class with object<test_making_a_class_w_object>`.

----

*********************************************************************************
test_is_none_an_object
*********************************************************************************

I want to test if :ref:`None<what is None?>` is an :ref:`object<what is a class?>`.

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

I want to test if a :ref:`boolean<what are booleans?>` is an :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

---------------------------------------------------------------------------------
how to test if something is NOT a subclass of a class
---------------------------------------------------------------------------------

----

I can test if an :ref:`object<what is a class?>` is a :ref:`subclass (child) <what is a class?>` of another :ref:`object<what is a class?>` or NOT with the `issubclass built-in function`_ from `The Python Standard Library`_.

issubclass_ checks if the thing in the parentheses on the left is a :ref:`subclass<how to test if something is a subclass of a class>` of the :ref:`class<what is a class?>` on the right in the parentheses.

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`bool<what are booleans?>` to show that :ref:`in Python everything is an object<everything is an object>`

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

The `unittest.TestCase class`_ has 2 :ref:`methods<what is a method?>` I can also use to test if an :ref:`object<what is a class?>` is a :ref:`subclass (child)<how to test if something is a subclass of a class>` of a :ref:`class<what is a class?>` or NOT - assertIsSubclass_ and assertNotIsSubclass_.

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

I want to test if an integer_ (a whole number without decimals) is an :ref:`object<what is a class?>`.

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
    :lineno-start: 30
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
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_a_float_an_object'

:ref:`A float is an object.<test_is_a_float_an_object>`

----

*********************************************************************************
test_is_a_string_an_object
*********************************************************************************

I want to test if a string_ (anything in :ref:`quotes`) is an :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for str_ (the :ref:`class<what is a class?>` for anything in :ref:`quotes`), to show that :ref:`in Python everything is an object<everything is an object>`

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

* I change assertNotIsSubclass_ to assertIsSubclass_

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
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_a_string_an_object'

:ref:`A string is an object.<test_is_a_string_an_object>`

----

*********************************************************************************
test_is_a_tuple_an_object
*********************************************************************************

I want to test if a tuple_ (anything in parentheses ``( )`` separated by a comma) is an :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for tuple_ (the :ref:`class<what is a class?>` for anything in parentheses ``( )`` separated by a comma), to show that :ref:`in Python everything is an object<everything is an object>`

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
    :emphasize-lines: 1-2

    git commit -am \
    'add test_is_a_tuple_an_object'

:ref:`A tuple is an object.<test_is_a_tuple_an_object>`

----

*********************************************************************************
test_is_a_list_an_object
*********************************************************************************

I want to test if :ref:`a list<what is a list?>` (anything in square brackets ``[ ]``) is an :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`list (the class for anything in square brackets '[ ]')<what is a list?>`, to show that :ref:`in Python everything is an object<everything is an object>`

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

I want to test if a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) is an :ref:`object<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for set_ (the :ref:`class<what is a class?>` for anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`), to show that :ref:`in Python everything is an object<everything is an object>`

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

I want to test if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by a comma) is an :ref:`object<what is a class?>`.

----

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`dict (the class for key-value pairs in curly braces '{ }' separated by a comma)<what is a dictionary?>`, to show that :ref:`in Python everything is an object<everything is an object>`

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
    :emphasize-lines: 4-5

        def test_is_a_dictionary_an_object(self):
            # assert not issubclass(dict, object)
            assert issubclass(dict, object)
            # self.assertNotIsSubclass(dict, object)
            self.assertIsSubclass(dict, object)


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
instance vs subclass
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_making_a_class_w_pass` to show that :ref:`an instance (a copy)<how to test if something is an instance of a class>` is different from a :ref:`subclass (child)<how to test if something is a subclass of a class>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)
            assert issubclass(an_instance, object)

        def test_making_a_class_w_parentheses(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because the argument I put on the left is an :ref:`instance<how to test if something is an instance of a class>` not a :ref:`subclass<how to test if something is a subclass of a class>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 60
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 7
  :emphasize-lines: 5-6

      def test_making_a_class_w_pass(self):
          an_instance = src.classes.WPass()
          assert isinstance(an_instance, object)
          self.assertIsInstance(an_instance, object)
          # assert issubclass(an_instance, object)
          assert issubclass(src.classes.WPass, object)

      def test_making_a_class_w_parentheses(self):

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to the `assertNotIsSubclass method`_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7-9

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)
            # assert issubclass(an_instance, object)
            assert issubclass(src.classes.WPass, object)
            self.assertNotIsSubclass(
                src.classes.WPass, object
            )

        def test_making_a_class_w_parentheses(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.WPass'> is
        a subclass of <class 'object'>

* I change assertNotIsSubclass_ to assertIsSubclass_

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)
            # assert issubclass(an_instance, object)
            assert issubclass(src.classes.WPass, object)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.WPass, object
            )

        def test_making_a_class_w_parentheses(self):

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``src.classes.WPass``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WPass
            # assert issubclass(an_instance, object)
            assert issubclass(src.classes.WPass, object)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.WPass, object
            )

        def test_making_a_class_w_parentheses(self):

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WPass``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7-9, 12-14

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WPass
            assert issubclass(a_class, object)
            self.assertIsSubclass(a_class, object)
            # assert issubclass(an_instance, object)
            # assert issubclass(src.classes.WPass, object)
            # self.assertNotIsSubclass(
            # self.assertIsSubclass(
            #     src.classes.WPass, object
            # )

        def test_making_a_class_w_parentheses(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7

        def test_making_a_class_w_pass(self):
            an_instance = src.classes.WPass()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WPass
            assert issubclass(a_class, object)
            self.assertIsSubclass(a_class, object)

        def test_making_a_class_w_parentheses(self):

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_making_a_class_w_parentheses`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            assert issubclass(an_instance, object)

        def test_making_a_class_w_object(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because ``src.classes.WParentheses()`` is an :ref:`instance<how to test if something is an instance of a class>` not a :ref:`subclass<how to test if something is a subclass of a class>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6-9

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WParentheses, object
            )

        def test_making_a_class_w_object(self):

  the test passes.

* I add a call to the `assertNotIsSubclass method`_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10-12

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WParentheses, object
            )
            self.assertNotIsSubclass(
                src.classes.WParentheses, object
            )

        def test_making_a_class_w_object(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.WParentheses'> is
        a subclass of <class 'object'>

* I change assertNotIsSubclass_ to the `assertIsSubclass method`_

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10-11

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WParentheses, object
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.WParentheses, object
            )

        def test_making_a_class_w_object(self):

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``src.classes.WParentheses``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 6

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WParentheses
            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WParentheses, object
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.WParentheses, object
            )

        def test_making_a_class_w_object(self):

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WParentheses``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 7-8, 10-12, 14-17

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WParentheses
            assert issubclass(a_class, object)
            self.assertIsSubclass(a_class, object)
            # assert issubclass(an_instance, object)
            # assert issubclass(
            #     src.classes.WParentheses, object
            # )
            # self.assertNotIsSubclass(
            # self.assertIsSubclass(
            #     src.classes.WParentheses, object
            # )

        def test_making_a_class_w_object(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 16

        def test_making_a_class_w_parentheses(self):
            an_instance = src.classes.WParentheses()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WParentheses
            assert issubclass(a_class, object)
            self.assertIsSubclass(a_class, object)

        def test_making_a_class_w_object(self):

----

* I also add an :ref:`assertion<what is an assertion?>` to :ref:`test_making_a_class_w_object`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            assert issubclass(an_instance, object)

        def test_is_none_an_object(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because ``src.classes.WObject()`` is an :ref:`instance<how to test if something is an instance of a class>` not a :ref:`subclass<how to test if something is a subclass of a class>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6-9

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WObject, object
            )

        def test_is_none_an_object(self):

  the test passes.

* I add a call to the `assertNotIsSubclass method`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-12

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WObject, object
            )
            self.assertNotIsSubclass(
                src.classes.WObject, object
            )

        def test_is_none_an_object(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.classes.WObject'> is
        a subclass of <class 'object'>

* I change assertNotIsSubclass_ to the `assertIsSubclass method`_

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-11

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WObject, object
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.WObject, object
            )

        def test_is_none_an_object(self):

  the test passes.

* I add a :ref:`variable<what is a variable?>` to use to remove repetition of ``src.classes.WObject``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WObject
            # assert issubclass(an_instance, object)
            assert issubclass(
                src.classes.WObject, object
            )
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.classes.WObject, object
            )

        def test_is_none_an_object(self):

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.classes.WObject``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7-8, 10-12, 14-16

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WObject
            assert issubclass(a_class, object)
            self.assertIsSubclass(a_class, object)
            # assert issubclass(an_instance, object)
            # assert issubclass(
            #     src.classes.WObject, object
            # )
            # self.assertNotIsSubclass(
            # self.assertIsSubclass(
            #     src.classes.WObject, object
            # )

        def test_is_none_an_object(self):

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 25

        def test_making_a_class_w_object(self):
            an_instance = src.classes.WObject()
            assert isinstance(an_instance, object)
            self.assertIsInstance(an_instance, object)

            a_class = src.classes.WObject
            assert issubclass(a_class, object)
            self.assertIsSubclass(a_class, object)

        def test_is_none_an_object(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add instance vs subclass'

The difference between a :ref:`subclass (child)<how to test if something is a subclass of a class>` and an :ref:`an instance (a copy)<how to test if something is an instance of a class>` is the ``()`` after the name

.. code-block:: python

  a_name = ClassName

points the ``a_name`` :ref:`variable<what is a variable?>` to ``ClassName``

.. code-block:: python

  a_name = ClassName()

points the ``a_name`` :ref:`variable<what is a variable?>` to the result of calling ``ClassName()``

----

*********************************************************************************
test_attributes_and_methods_of_objects
*********************************************************************************

In :ref:`test_attributes_and_methods_of_person_class` I saw the :ref:`methods<what is a method?>` I added to the ``Person`` :ref:`class<what is a class?>` and also names that I did not add, which led to the question of where they came from.

I want to test the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the :ref:`object class<what is a class?>` because it is the mother of all :ref:`classes<what is a class?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests

* I add a test to ``test_classes.py``

  .. code-block:: python
    :lineno-start: 66
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
    :lineno-start: 70
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
    :lineno-start: 70
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
    :lineno-start: 70
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
review
*********************************************************************************

I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`
* :ref:`object<test_making_a_class_w_object>`

Everything in Python_ is an :ref:`object<what is a class?>`

* :ref:`None is an object<test_is_none_an_object>`
* :ref:`A boolean is an object<test_is_a_boolean_an_object>`
* :ref:`An integer is an object<test_is_an_integer_an_object>`
* :ref:`A float is an object<test_is_a_float_an_object>`
* :ref:`A string is an object<test_is_a_string_an_object>`
* :ref:`A tuple is an object<test_is_a_tuple_an_object>`
* :ref:`A list is an object<test_is_a_list_an_object>`
* :ref:`A set is an object<test_is_a_set_an_object>`
* :ref:`A dictionary is an object<test_is_a_dictionary_an_object>`
* :ref:`An instance is NOT a subclass<instance vs subclass>`

:ref:`How many questions can you answer about classes?<questions about classes>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_classes.py`` and ``classes.py`` in the :ref:`editor(s)<2 editors>`
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

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

You now know

* :ref:`how to make a Python test driven development environment manually<how to make a Python test driven development environment>`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`

:ref:`Would you like to use class attributes to remove repetition from the assertion_error project?<AssertionError 2: use class attributes>`

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