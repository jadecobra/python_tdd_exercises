.. meta::
  :description:
  :keywords:

.. include:: ../links.rst

#################################################################################
test objects with loops
#################################################################################

I want to use :ref:`for loops<for loops>` in the :ref:`objects<everything is an object>` project.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/objects/test_objects_w_loops.py
  :caption: objects/tests/test_objects.py
  :language: python
  :linenos:
  :lines: 1-10

.. literalinclude:: ../code/objects/test_objects_w_loops.py
  :caption: objects/tests/test_objects.py
  :language: python
  :lineno-start: 13
  :lines: 13-25

.. literalinclude:: ../code/objects/test_objects_w_loops.py
  :caption: objects/tests/test_objects.py
  :language: python
  :lineno-start: 27
  :lines: 27-33

.. literalinclude:: ../code/objects/test_objects_w_loops.py
  :caption: objects/tests/test_objects.py
  :language: python
  :lineno-start: 35
  :lines: 35-55

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd objects

* I open ``test_objects.py`` from the ``tests`` folder_
* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    uv run pytest-watcher . --now

----

*********************************************************************************
test_what_is_an_object
*********************************************************************************

All the tests except :ref:`test_is_none_an_object` :ref:`assert<what is an assertion?>` that an :ref:`object<everything is an object>` is an :ref:`instance<how to test if something is an instance>` and a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<everything is an object>`

.. code-block:: python

  assert isinstance(an_object(), object)
  self.assertIsInstance(an_object(), object)

  assert isinstance(an_object, object)
  self.assertIsInstance(an_object, object)

  assert issubclass(an_object, object)
  self.assertIsSubclass(an_object, object)

I can write a :ref:`function<what is a function?>` with a :ref:`for loop<what is a for loop?>` to remove the repetition.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with :ref:`instance<how to test if something is an instance>` and :ref:`subclass<how to test if something is a subclass>` tests

.. code-block:: python
  :caption: objects/tests/test_objects.py
  :lineno-start: 13
  :emphasize-lines: 3-13

  class TestClasses(unittest.TestCase):

      def test_what_is_an_object(self):
          for an_object in (
              WPass, WParentheses, WObject,
              bool, int, float, str,
              tuple, list, set, dict
          ):
              with self.subTest(an_object):
                  assert not isinstance(an_object(), object)
                  self.assertNotIsInstance(an_object(), object)
                  assert not issubclass(an_object, object)
                  self.assertNotIsSubclass(an_object, object)

      def test_making_a_class_w_pass(self):

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell
  :caption: terminal

  SUBFAILED[<class 'tests.test_objects.WPass'>] ...
      AssertionError: assert not True
  SUBFAILED[<class 'tests.test_objects.WParentheses'>] ...
      AssertionError: assert not True
  SUBFAILED[<class 'tests.test_objects.WObject'>] ...
      AssertionError: assert not True
  SUBFAILED[<class 'bool'>] ...AssertionError: assert not True
  SUBFAILED[<class 'int'>] ...AssertionError: assert not True
  SUBFAILED[<class 'float'>] ...AssertionError: assert not True
  SUBFAILED[<class 'str'>] ...AssertionError: assert not True
  SUBFAILED[<class 'tuple'>] ...AssertionError: assert not True
  SUBFAILED[<class 'list'>] ...AssertionError: assert not True
  SUBFAILED[<class 'set'>] ...AssertionError: assert not True
  SUBFAILED[<class 'dict'>] ...AssertionError: assert not True

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change ``assert not isinstance(an_object(), object)``

  .. code-block:: python
    :caption: objects/tests/test_objects.py
    :lineno-start: 21
    :emphasize-lines: 2

                with self.subTest(an_object):
                    assert isinstance(an_object(), object)
                    self.assertNotIsInstance(an_object(), object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :caption: terminal

    SUBFAILED[<class 'tests.test_objects.WPass'>] ...
        AssertionError: <tests.test_objects.WPass object at 0xffffa0bcd123>
                        is an instance of <class 'object'>
    SUBFAILED[<class 'tests.test_objects.WParentheses'>] ...
        AssertionError: <tests.test_objects.WParentheses object at 0xffffe4fab456>
                        is an instance of <class 'object'>
    SUBFAILED[<class 'tests.test_objects.WObject'>] ...
        AssertionError: <tests.test_objects.WObject object at 0xffffc7def801>
                        is an instance of <class 'object'>
    SUBFAILED[<class 'bool'>] ...
        AssertionError: False is an instance of <class 'object'>
    SUBFAILED[<class 'int'>] ...
        AssertionError: 0 is an instance of <class 'object'>
    SUBFAILED[<class 'float'>] ...
        AssertionError: 0.0 is an instance of <class 'object'>
    SUBFAILED[<class 'str'>] ...
        AssertionError: '' is an instance of <class 'object'>
    SUBFAILED[<class 'tuple'>] ...
        AssertionError: () is an instance of <class 'object'>
    SUBFAILED[<class 'list'>] ...
        AssertionError: [] is an instance of <class 'object'>
    SUBFAILED[<class 'set'>] ...
        AssertionError: set() is an instance of <class 'object'>
    SUBFAILED[<class 'dict'>] ...
        AssertionError: {} is an instance of <class 'object'>

* I change ``self.assertNotIsInstance(an_object(), object)``

  .. code-block:: python
    :caption: objects/tests/test_objects.py
    :lineno-start: 21
    :emphasize-lines: 3

                with self.subTest(an_object):
                    assert isinstance(an_object(), object)
                    self.assertIsInstance(an_object(), object)
                    assert not issubclass(an_object, object)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

* I change ``assert not issubclass(an_object, object)``

  .. code-block:: python
    :caption: objects/tests/test_objects.py
    :lineno-start: 21
    :emphasize-lines: 4

                with self.subTest(an_object):
                    assert isinstance(an_object(), object)
                    self.assertIsInstance(an_object(), object)
                    assert issubclass(an_object, object)
                    self.assertNotIsSubclass(an_object, object)

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :caption: terminal

    SUBFAILED[<class 'tests.test_objects.WPass'>] ...
        AssertionError: <class 'tests.test_objects.WPass'>
                        is a subclass of <class 'object'>
    SUBFAILED[<class 'tests.test_objects.WParentheses'>] ...
        AssertionError: <class 'tests.test_objects.WParentheses'>
                        is a subclass of <class 'object'>
    SUBFAILED[<class 'tests.test_objects.WObject'>] ...
        AssertionError: <class 'tests.test_objects.WObject'>
                        is a subclass of <class 'object'>
    SUBFAILED[<class 'bool'>] ...
        AssertionError: <class 'bool'> is a subclass of <class 'object'>
    SUBFAILED[<class 'int'>] ...
        AssertionError: <class 'int'> is a subclass of <class 'object'>
    SUBFAILED[<class 'float'>] ...
        AssertionError: <class 'float'> is a subclass of <class 'object'>
    SUBFAILED[<class 'str'>] ...
        AssertionError: <class 'str'> is a subclass of <class 'object'>
    SUBFAILED[<class 'tuple'>] ...
        AssertionError: <class 'tuple'> is a subclass of <class 'object'>
    SUBFAILED[<class 'list'>] ...
        AssertionError: <class 'list'> is a subclass of <class 'object'>
    SUBFAILED[<class 'set'>] ...
        AssertionError: <class 'set'> is a subclass of <class 'object'>
    SUBFAILED[<class 'dict'>] ...
        AssertionError: <class 'dict'> is a subclass of <class 'object'>

* I change ``self.assertNotIsSubclass(an_object, object)``

  .. code-block:: python
    :caption: objects/tests/test_objects.py
    :lineno-start: 21
    :emphasize-lines: 5

                with self.subTest(an_object):
                    assert isinstance(an_object(), object)
                    self.assertIsInstance(an_object(), object)
                    assert issubclass(an_object, object)
                    self.assertIsSubclass(an_object, object)

        def test_making_an_object_w_pass(self):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove all the other tests except :ref:`test_is_none_an_object` because they are now covered by :ref:`test_what_is_an_object`

  .. code-block:: python
    :caption: objects/tests/test_objects.py
    :lineno-start: 21

                with self.subTest(an_object):
                    assert isinstance(an_object(), object)
                    self.assertIsInstance(an_object(), object)
                    assert issubclass(an_object, object)
                    self.assertIsSubclass(an_object, object)

        def test_is_none_an_object(self):
            assert isinstance(None, object)
            self.assertIsInstance(None, object)

            # fails because None is not a class
            # assert issubclass(None, object)
            # self.assertIsSubclass(None, object)

        def test_dir_object(self):

* I add a git_ commit message

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1-2

    git commit -am \
    'extract test_what_is_an_object'

----

*********************************************************************************
review
*********************************************************************************

I used a :ref:`for loop<what is a for loop?>` to remove repetition from the tests.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_objects.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests
* I `change directory`_ to the parent of ``objects``

  .. code-block:: python
    :caption: terminal
    :emphasize-lines: 1

    cd ..

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<test objects with loops: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

* :ref:`I know how to make a Python Test Driven Development environment manually<how to make a Python Test Driven Development environment manually>`.
* :ref:`I know what a Python module is<what is a module?>`.
* :ref:`I know how to run tests automatically<how to run tests automatically>`.
* :ref:`I know what an assertion is<what is an assertion?>`.
* :ref:`I know how to make functions<what is a function?>`.
* :ref:`I know how to make a person with strings<how to make a person with strings>`.
* :ref:`I know how to make functions that take input<functions that take input>`.
* :ref:`I know what causes TypeError<what causes TypeError?>`.
* :ref:`I know how to place values in strings<telephone>`.
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with an object<how to make a person with an object>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.
* :ref:`I know how to make a person with loops<how to make a person with loops>`.

:ref:`Would you like to test the telephone project with loops?<test telephone with loops>`

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