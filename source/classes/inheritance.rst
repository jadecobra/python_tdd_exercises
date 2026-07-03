.. meta::
  :description: Step-by-step Python TDD tutorial for beginners on "everything is an object": use bare `assert isinstance()` and `assert issubclass()` (plain pytest test functions, no unittest.TestCase) to prove None (special-cased), bool, int, float, str, tuple, list, set and dict all inherit from the base `object` class. Create classes with `pass`, `()` and `(object)`. Distinguish instance (with `()`) vs subclass using TypeError from issubclass(instance). Inspect dunder methods with `dir(object)`. Real errors shown: "AssertionError: assert not True", "TypeError: issubclass() arg 1 must be a class", NameError before defs. Project uses `uv init classes`, tests layout, requirements + `uv add`, pytest-watcher and git. Part of Jacob Itegboje Pumping Python series.
  :keywords: Jacob Itegboje, Pumping Python, everything is an object, python inherits from object, is None an object python, isinstance issubclass tutorial, bare assert isinstance, class pass parentheses object, instance vs subclass python, TypeError issubclass arg 1 must be a class, AssertionError assert not True, dir(object) dunder, test_is_none_an_object, uv init classes pytest-watcher, WPass WParentheses, python TDD everything is an object, class vs instance parentheses, python object base class dunder methods, None is not a class for issubclass, python test driven development classes object, learning python inheritance for beginners

.. include:: ../links.rst

.. _isinstance: https://docs.python.org/3/library/functions.html#isinstance
.. _isinstance built-in function: isinstance_
.. _issubclass: https://docs.python.org/3/library/functions.html#issubclass
.. _issubclass built-in function: issubclass_


#################################################################################
everything is an object
#################################################################################

The :ref:`object class<what is a class?>` is the mother of all things in Python_. I think of classes_ as :ref:`attributes (variables)<what is a class attribute?>` and :ref:`methods (functions) <what is a method?>` that belong together.

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

.. literalinclude:: ../code/classes/test_classes.py
  :language: python
  :linenos:

----

*********************************************************************************
start the project
*********************************************************************************

* I name this project ``classes``
* I open a terminal_
* I `change directory`_ to the ``classes`` folder_ in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd classes

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: classes

* I use uv_ to make a directory_ for the project and initialize it

  .. code-block:: python
    :emphasize-lines: 1

    uv init classes

  the terminal_ shows

  .. code-block:: shell

    Initialized project `classes`
    at `.../pumping_python/classes`

* I `change directory`_ to ``classes``

  .. code-block:: python
    :emphasize-lines: 1

    cd classes

  the terminal_ shows I am in the ``classes`` folder_

  .. code-block:: python

    .../pumping_python/classes

* I `make a directory`_ for the tests

  .. code-block:: python
    :emphasize-lines: 1

    mkdir tests

* I make the ``tests`` directory_ a `Python package`_

  .. danger:: use 2 underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch tests/__init__.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item tests/__init__.py

* I use the `mv program`_ to change the name of ``main.py`` to ``test_classes.py`` and move it to the ``tests`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        mv main.py tests/test_classes.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        Move-Item main.py tests/test_classes.py

* I open ``test_classes.py``

* I delete the text in the file_ then add :ref:`the first failing test<test_failure>` to ``test_classes.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_failure():
        assert False is True

* I go back to the terminal_ to make a requirements file_ for the `Python packages`_ I need

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest" > requirements.txt

* I add `pytest-watcher`_ to the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    echo "pytest-watcher" >> requirements.txt

* I use uv_ to install `pytest-watcher`_ with the requirements file_

  .. code-block:: python
    :emphasize-lines: 1

    uv add --requirement requirements.txt

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 6, 8, 10

    ======================== FAILURES ========================
    ______________________ test_failure ______________________

        def test_failure():
    >       assert False is True
    E       assert False is True

    test_classes.py:2: AssertionError
    ================ short test summary info =================
    FAILED test_classes.py::test_failure - assert False is True
    =================== 1 failed in X.YZs ====================

  because :ref:`True<test_what_is_true>` is NOT :ref:`False<test_what_is_false>`.

  .. admonition:: if the terminal_ does not show the same error, then check

    * if your ``tests/__init__.py`` has two underscores (__) before and after ``init`` for ``__init__.py`` not ``_init_.py``
    * if you ran ``echo "pytest-watcher" >> requirements.txt``, to add ``pytest-watcher`` to the requirements file_

    and try ``uv run pytest-watcher . --now`` again

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6
    :emphasize-text: AssertionError

    def test_failure():
        assert False is True


    # Exceptions seen
    # AssertionError

* I change :ref:`False<test_what_is_false>` to :ref:`True<test_what_is_true>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-3

    def test_failure():
        # assert False is True
        assert True is True


    # Exceptions seen
    # AssertionError

  the test passes.

----

*********************************************************************************
how to test if something is NOT an instance
*********************************************************************************

I can make a :ref:`class<what is a class?>` with the :ref:`class<what is a class?>` keyword, use :ref:`CapWords format<CapWords>` for the name and use a name that tells what the group of :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` do.

.. code-block:: python

  class NameOfClass(ParentClass):

      attribute = SOMETHING

      def method():
          the body of the method
          ...

I can test if an :ref:`object<everything is an object>` is NOT :ref:`an instance (a copy)<how to test if something is an instance>` of another :ref:`object<everything is an object>` with the `isinstance built-in function`_ from `The Python Standard Library`_.

isinstance_ checks if the thing in the parentheses on the left is an :ref:`instance (a copy)<how to test if something is an instance>` of the :ref:`class<what is a class?>` on the right in the parentheses.

----

*********************************************************************************
test_making_a_class_w_pass
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I change :ref:`test_failure` to :ref:`test_making_a_class_w_pass` then add an :ref:`assertion<what is an assertion?>` with isinstance_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_making_a_class_w_pass():
        assert not isinstance(WPass(), object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'WPass' is not defined

  because ``WPass`` is not defined in this file_.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 5
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

I add a :ref:`class definition<how to make a class>` for ``WPass``

.. code-block:: python
  :linenos:
  :emphasize-lines: 1

  class WPass: pass


  def test_making_a_class_w_pass():
      assert not isinstance(WPass(), object)

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  E       assert not True

because the statement ``not isinstance(WPass(), object)`` is not :ref:`True<test_what_is_true>`.

----

*********************************************************************************
how to test if something is an instance
*********************************************************************************

I can test if an :ref:`object<everything is an object>` is :ref:`an instance (a copy)<how to test if something is an instance>` of another :ref:`object<everything is an object>` with the `isinstance built-in function`_ from `The Python Standard Library`_.

isinstance_ checks if the thing in the parentheses on the left is an :ref:`instance (a copy)<how to test if something is an instance>` of the :ref:`class<what is a class?>` on the right in the parentheses.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 2-3

    def test_making_a_class_w_pass():
        # assert not isinstance(WPass(), object)
        assert isinstance(WPass(), object)


    # Exceptions seen

  * The test passes because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.
  * The :ref:`assertion<what is an assertion?>` - ``assert isinstance(WPass(), object)`` checks if the result of a :ref:`call<how to call a function>` to ``WPass`` is an :ref:`instance<how to test if something is an instance>` of the :ref:`object class (the mother of all classes)<what is a class?>`.
  * The :ref:`class definition<how to make a class>` simply says pass_ and the test passes.
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body).

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 4

    def test_making_a_class_w_pass():
        assert isinstance(WPass(), object)


    # Exceptions seen

* I open a new terminal_ then make sure I am in ``classes`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd classes

* I add a git_ commit message in the new terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_pass'

:ref:`I can make a class with pass<test_making_a_class_w_pass>`.

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

* I go back to the terminal_ where the tests are running
* I add another test to ``test_classes.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 5-6

    def test_making_a_class_w_pass():
        assert isinstance(WPass(), object)


    def test_making_a_class_w_parentheses():
        assert not isinstance(WParentheses(), object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'WParentheses' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class definition<how to make a class>` for ``WParentheses`` like I did for ``WPass``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    class WPass: pass


    class WParentheses: pass


    def test_making_a_class_w_pass():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

  because the statement ``not isinstance(WParentheses(), object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_parentheses` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2-3

    def test_making_a_class_w_parentheses():
        # assert not isinstance(WParentheses(), object)
        assert isinstance(WParentheses(), object)


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add parentheses to the :ref:`definition<how to make a class>` of ``WParentheses``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 1-2
    :emphasize-text: ( )

    # class WParentheses: pass
    class WParentheses(): pass


    def test_making_a_class_w_pass():

  * The test is still green because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.
  * The :ref:`assertion<what is an assertion?>` - ``assert isinstance(WParentheses(), object)`` checks if the result of a :ref:`call<how to call a function>` to ``WParentheses`` is an :ref:`instance<how to test if something is an instance>` of the :ref:`object class (the mother of all classes)<what is a class?>`.
  * This :ref:`class definition<how to make a class>` has parentheses after the name.
  * The :ref:`class definition<how to make a class>` simply says pass_ and the test passes.
  * pass_ is a special keyword that allows the :ref:`class definition<how to make a class>` to follow Python_ language rules (the :ref:`class<what is a class?>` must have a body).

* I remove the commented lines

  .. code-block:: python
    :linenos:

    class WPass: pass


    class WParentheses(): pass


    def test_making_a_class_w_pass():
        assert isinstance(WPass(), object)


    def test_making_a_class_w_parentheses():
        assert isinstance(WParentheses(), object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_parentheses'

:ref:`I can make a class with parentheses<test_making_a_class_w_parentheses>`.

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

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for a new :ref:`class<what is a class?>` in ``test_classes.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 5-6

    def test_making_a_class_w_parentheses():
        assert isinstance(WParentheses(), object)


    def test_making_a_class_w_object():
        assert not isinstance(WObject(), object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'WObject' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I a :ref:`class definition<how to make a class>` for ``WObject``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4

    class WParentheses(): pass


    class WObject(): pass


    def test_making_a_class_w_pass():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert not True

  because ``not isinstance(WParentheses(), object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_object` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 2-3

    def test_making_a_class_w_object():
        # assert not isinstance(WObject(), object)
        assert isinstance(WObject(), object)


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add :ref:`object<everything is an object>` to the parentheses of the :ref:`class definition<how to make a class>` for ``WObject``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 1-2
    :emphasize-text: object

    # class WObject(): pass
    class WObject(object): pass


    def test_making_a_class_w_pass():

  the test is still green.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    class WPass: pass


    class WParentheses(): pass


    class WObject(object): pass


    def test_making_a_class_w_pass():
        assert isinstance(WPass(), object)


    def test_making_a_class_w_parentheses():
        assert isinstance(WParentheses(), object)


    def test_making_a_class_w_object():
        assert isinstance(WObject(), object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_making_a_class_w_object'

I have three different :ref:`classes<what is a class?>`, and the tests show that they are all :ref:`instances<how to test if something is an instance>` of the :ref:`object class<what is a class?>`

.. code-block:: python

  class WPass: pass

.. code-block:: python

  class WParentheses(): pass

.. code-block:: python

  class WObject(object): pass

their results are the same because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

I like to write my :ref:`classes<what is a class?>` with ``(object)``, so that anyone can see what the parent :ref:`class<what is a class?>` is without thinking about it.

:ref:`I can make a class with object<test_making_a_class_w_object>`.

----

*********************************************************************************
test_is_none_an_object
*********************************************************************************

I want to test if :ref:`None<what is None?>` is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 5-6

    def test_making_a_class_w_object():
        assert isinstance(WObject(), object)


    def test_is_none_an_object():
        assert not isinstance(None, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`None<what is None?>` is an :ref:`object<everything is an object>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 22
  :emphasize-lines: 2-3

    def test_is_none_an_object():
        # assert not isinstance(None, object)
        assert isinstance(None, object)


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 22

    def test_is_none_an_object():
        assert isinstance(None, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_is_none_an_object'

----

*********************************************************************************
how to test if something is NOT a subclass
*********************************************************************************

I can test if an :ref:`object<everything is an object>` is NOT a :ref:`subclass (child) <what is a class?>` of another :ref:`object<everything is an object>` with the `issubclass built-in function`_ from `The Python Standard Library`_.

issubclass_ checks if the thing in the parentheses on the left is a :ref:`subclass<how to test if something is a subclass>` of the :ref:`class<what is a class?>` on the right in the parentheses.

----

*********************************************************************************
test_is_a_boolean_an_object
*********************************************************************************

I want to test if a :ref:`boolean<what are booleans?>` is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`bool (the class for booleans)<how to test if something is grouped as True>` to show that :ref:`in Python everything is an object<everything is an object>`

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

    def test_is_none_an_object():
        assert isinstance(None, object)


    def test_is_a_boolean_an_object():
        assert not issubclass(bool, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`bool<how to test if something is grouped as True>` is a :ref:`child of object<what is a class?>`.

----

*********************************************************************************
how to test if something is a subclass
*********************************************************************************

I can test if an :ref:`object<everything is an object>` is a :ref:`subclass (child) <what is a class?>` of another :ref:`object<everything is an object>` with the `issubclass built-in function`_ from `The Python Standard Library`_.

issubclass_ checks if the thing in the parentheses on the left is a :ref:`subclass<how to test if something is a subclass>` of the :ref:`class<what is a class?>` on the right in the parentheses.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 26
  :emphasize-lines: 2-3

    def test_is_a_boolean_an_object():
        # assert not issubclass(bool, object)
        assert issubclass(bool, object)


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 26

    def test_is_a_boolean_an_object():
        assert issubclass(bool, object)


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

I want to test if an integer_ (a whole number without decimals) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for int_ (the :ref:`class<what is a class?>` for whole numbers without decimals), to show that everything in Python_ is a :ref:`child of object.<what is a class?>`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 5-6

    def test_is_a_boolean_an_object():
        assert issubclass(bool, object)


    def test_is_an_integer_an_object():
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

  def test_is_an_integer_an_object():
      # assert not issubclass(int, object)
      assert issubclass(int, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 30

    def test_is_an_integer_an_object():
        assert issubclass(int, object)


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

I want to test if a float_ (a binary floating point decimal number) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for float_ (the :ref:`class<what is a class?>` for binary floating point decimal numbers), to show that everything in Python_ is a :ref:`child of object.<what is a class?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5-6

    def test_is_an_integer_an_object():
        assert issubclass(int, object)


    def test_is_a_float_an_object():
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

    def test_is_a_float_an_object():
        # assert not issubclass(float, object)
        assert issubclass(float, object)


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 34

    def test_is_a_float_an_object():
        assert issubclass(float, object)


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

I want to test if a string_ (anything in :ref:`quotes`) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for str_ (the :ref:`class<what is a class?>` for anything in :ref:`quotes`), to show that :ref:`in Python everything is an object<everything is an object>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 5-6

    def test_is_a_float_an_object():
        assert issubclass(float, object)


    def test_is_a_string_an_object():
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

    def test_is_a_string_an_object():
        # assert not issubclass(str, object)
        assert issubclass(str, object)


    # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 38

    def test_is_a_string_an_object():
        assert issubclass(str, object)


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

I want to test if a tuple_ (anything in parentheses ``( )`` separated by a comma) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for tuple_ (the :ref:`class<what is a class?>` for anything in parentheses ``( )`` separated by a comma), to show that :ref:`in Python everything is an object<everything is an object>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-6

    def test_is_a_string_an_object():
        assert issubclass(str, object)


    def test_is_a_tuple_an_object():
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

  def test_is_a_tuple_an_object():
      # assert not issubclass(tuple, object)
      assert issubclass(tuple, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 42

    def test_is_a_tuple_an_object():
        assert issubclass(tuple, object)


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

I want to test if a :ref:`list<what is a list?>` (anything in square brackets ``[ ]``) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`list (the class for anything in square brackets '[ ]')<what is a list?>`, to show that :ref:`in Python everything is an object<everything is an object>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 5-6

    def test_is_a_tuple_an_object():
        assert issubclass(tuple, object)


    def test_is_a_list_an_object():
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

  def test_is_a_list_an_object():
      # assert not issubclass(list, object)
      assert issubclass(list, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 46

    def test_is_a_list_an_object():
        assert issubclass(list, object)


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

I want to test if a set_ (anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for set_ (the :ref:`class<what is a class?>` for anything in curly braces ``{ }``, not :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`), to show that :ref:`in Python everything is an object<everything is an object>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 5-6

    def test_is_a_list_an_object():
        assert issubclass(list, object)


    def test_is_a_set_an_object():
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

  def test_is_a_set_an_object():
      # assert not issubclass(set, object)
      assert issubclass(set, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 50

    def test_is_a_set_an_object():
        assert issubclass(set, object)


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

I want to test if a :ref:`dictionary<what is a dictionary?>` (any :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>` in curly braces ``{ }`` separated by commas) is an :ref:`object<everything is an object>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for :ref:`dict (the class for key-value pairs in curly braces '{ }' separated by commas)<what is a dictionary?>`, to show that :ref:`in Python everything is an object<everything is an object>`

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 5-6

    def test_is_a_set_an_object():
        assert issubclass(set, object)


    def test_is_a_dictionary_an_object():
        assert not issubclass(dict, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because :ref:`dict<what is a dictionary?>` is a :ref:`child of object<what is a class?>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the statement to make it :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 54
  :emphasize-lines: 2-3

  def test_is_a_dictionary_an_object():
      # assert not issubclass(dict, object)
      assert issubclass(dict, object)


  # Exceptions seen

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 54

    def test_is_a_dictionary_an_object():
        assert issubclass(dict, object)


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

An :ref:`instance<how to test if something is an instance>` is a copy of an :ref:`object<what is a class?>` and a :ref:`subclass<how to test if something is a subclass>` is a child of an :ref:`object<what is a class?>`. They are different.

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_making_a_class_w_pass` to show that :ref:`an instance (a copy)<how to test if something is an instance>` is different from a :ref:`subclass (child)<how to test if something is a subclass>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3

    def test_making_a_class_w_pass():
        assert isinstance(WPass(), object)
        assert issubclass(WPass(), object)


    def test_making_a_class_w_parentheses():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because the first argument given in a :ref:`call<how to call a function with input>` to the :ref:`issubclass function<how to test if something is a subclass>`  is an :ref:`instance<how to test if something is an instance>` not a :ref:`class<what is a class?>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 3-4

  def test_making_a_class_w_pass():
      assert isinstance(WPass(), object)
      # assert issubclass(WPass(), object)
      assert issubclass(WPass, object)


  def test_making_a_class_w_parentheses():

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line from :ref:`test_making_a_class_w_pass`

  .. code-block:: python
    :lineno-start: 10

    def test_making_a_class_w_pass():
        assert isinstance(WPass(), object)
        assert issubclass(WPass, object)


    def test_making_a_class_w_parentheses():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_making_a_class_w_parentheses` to show that :ref:`an instance (a copy)<how to test if something is an instance>` is different from a :ref:`subclass (child)<how to test if something is a subclass>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

    def test_making_a_class_w_parentheses():
        assert isinstance(WParentheses(), object)
        assert issubclass(WParentheses(), object)


    def test_making_a_class_w_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because ``WParentheses()`` is an :ref:`instance<how to test if something is an instance>` and the argument I put in the parentheses on the left should be a :ref:`class<what is a class?>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3-4

    def test_making_a_class_w_parentheses():
        assert isinstance(WParentheses(), object)
        # assert issubclass(WParentheses(), object)
        assert issubclass(WParentheses, object)


    def test_making_a_class_w_object():

  the test passes.

* I remove the commented line from :ref:`test_making_a_class_w_parentheses`

  .. code-block:: python
    :lineno-start: 15

    def test_making_a_class_w_parentheses():
        assert isinstance(WParentheses(), object)
        assert issubclass(WParentheses, object)


    def test_making_a_class_w_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_making_a_class_w_object`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3

    def test_making_a_class_w_object():
        assert isinstance(WObject(), object)
        assert issubclass(WObject(), object)


    def test_is_none_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because ``WObject()`` is an :ref:`instance<how to test if something is an instance>` not a :ref:`subclass<how to test if something is a subclass>`.

* I change the :ref:`assertion<what is an assertion?>` to make the statement :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 3-4

    def test_making_a_class_w_object():
        assert isinstance(WObject(), object)
        # assert issubclass(WObject(), object)
        assert issubclass(WObject, object)


    def test_is_none_an_object():

  the test passes.

* I remove the commented line from :ref:`test_making_a_class_w_object`

  .. code-block:: python
    :lineno-start: 25

    def test_making_a_class_w_object():
        assert isinstance(WObject(), object)
        assert issubclass(WObject, object)


    def test_is_none_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_none_an_object`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3

    def test_is_none_an_object():
        assert isinstance(None, object)
        assert issubclass(None, object)


    def test_is_a_boolean_an_object():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: issubclass() arg 1 must be a class

  because :ref:`None<what is None?>` is not a :ref:`class<what is a class?>`.

* I comment the line out with a note to help me remember

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3-4

    def test_is_none_an_object():
        assert isinstance(None, object)
        # assert issubclass(None, object)
        # fails because None is not a class


    def test_is_a_boolean_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_boolean_an_object`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2

    def test_is_a_boolean_an_object():
        assert not isinstance(bool, object)
        assert issubclass(bool, object)


    def test_is_an_integer_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(bool, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_True>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 2-3

    def test_is_a_boolean_an_object():
        # assert not isinstance(bool, object)
        assert isinstance(bool, object)
        assert issubclass(bool, object)


    def test_is_an_integer_an_object():

  the test passes because :ref:`bool<what are booleans?>` is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_boolean_an_object`

  .. code-block:: python
    :lineno-start: 31

    def test_is_a_boolean_an_object():
        assert isinstance(bool, object)
        assert issubclass(bool, object)


    def test_is_an_integer_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_an_integer_an_object`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2

    def test_is_an_integer_an_object():
        assert not isinstance(int, object)
        assert issubclass(int, object)


    def test_is_a_float_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(int, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 2-3

    def test_is_an_integer_an_object():
        # assert not isinstance(int, object)
        assert isinstance(int, object)
        assert issubclass(int, object)


    def test_is_a_float_an_object():

  the test passes because int_ is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_an_integer_an_object`

  .. code-block:: python
    :lineno-start: 36

    def test_is_an_integer_an_object():
        assert isinstance(int, object)
        assert issubclass(int, object)


    def test_is_a_float_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_float_an_object`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2

    def test_is_a_float_an_object():
        assert not isinstance(float, object)
        assert issubclass(float, object)


    def test_is_a_string_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(float, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 2-3

    def test_is_a_float_an_object():
        # assert not isinstance(float, object)
        assert isinstance(float, object)
        assert issubclass(float, object)


    def test_is_a_string_an_object():

  the test passes because float_ is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_float_an_object`

  .. code-block:: python
    :lineno-start: 41

    def test_is_a_float_an_object():
        assert isinstance(float, object)
        assert issubclass(float, object)


    def test_is_a_string_an_object():


* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_string_an_object`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2

    def test_is_a_string_an_object():
        assert not isinstance(str, object)
        assert issubclass(str, object)


    def test_is_a_tuple_an_object():


  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(str, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 46
    :emphasize-lines: 2-3

    def test_is_a_string_an_object():
        # assert not isinstance(str, object)
        assert isinstance(str, object)
        assert issubclass(str, object)


    def test_is_a_tuple_an_object():

  the test passes because str_ is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_string_an_object`

  .. code-block:: python
    :lineno-start: 46

    def test_is_a_string_an_object():
        assert isinstance(str, object)
        assert issubclass(str, object)


    def test_is_a_tuple_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_tuple_an_object`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2

    def test_is_a_tuple_an_object():
        assert not isinstance(tuple, object)
        assert issubclass(tuple, object)


    def test_is_a_list_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(tuple, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test what is true>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3

    def test_is_a_tuple_an_object():
        # assert not isinstance(tuple, object)
        assert isinstance(tuple, object)
        assert issubclass(tuple, object)


    def test_is_a_list_an_object():

  the test passes because tuple_ is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_tuple_an_object`

  .. code-block:: python
    :lineno-start: 51

    def test_is_a_tuple_an_object():
        assert isinstance(tuple, object)
        assert issubclass(tuple, object)


    def test_is_a_list_an_object():


* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_list_an_object`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2

    def test_is_a_list_an_object():
        assert not isinstance(list, object)
        assert issubclass(list, object)


    def test_is_a_set_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(list, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2-3

    def test_is_a_list_an_object():
        # assert not isinstance(list, object)
        assert isinstance(list, object)
        assert issubclass(list, object)


    def test_is_a_set_an_object():

  the test passes because :ref:`list<what is a list?>` is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_list_an_object`

  .. code-block:: python
    :lineno-start: 56

    def test_is_a_list_an_object():
        assert isinstance(list, object)
        assert issubclass(list, object)


    def test_is_a_set_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_set_an_object`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2

    def test_is_a_set_an_object():
        assert not isinstance(set, object)
        assert issubclass(set, object)


    def test_is_a_dictionary_an_object():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(set, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

    def test_is_a_set_an_object():
        # assert not isinstance(set, object)
        assert isinstance(set, object)
        assert issubclass(set, object)


    def test_is_a_dictionary_an_object():

  the test passes because set_ is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_set_an_object`

  .. code-block:: python
    :lineno-start: 61

    def test_is_a_set_an_object():
        assert isinstance(set, object)
        assert issubclass(set, object)


    def test_is_a_dictionary_an_object():

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_is_a_dictionary_an_object`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2

    def test_is_a_dictionary_an_object():
        assert not isinstance(dict, object)
        assert issubclass(dict, object)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert not True

  because ``assert not isinstance(dict, object)`` is not :ref:`True<test_what_is_true>`.

* I change the :ref:`assertion<what is an assertion?>` to make it :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 2-3

    def test_is_a_dictionary_an_object():
        # assert not isinstance(dict, object)
        assert isinstance(dict, object)
        assert issubclass(dict, object)


    # Exceptions seen


  the test passes because :ref:`dict<what is a dictionary?>` is a

  - :ref:`built-in function<what is a function?>` that comes with Python_
  - is an :ref:`instance<how to test if something is an instance>` of :ref:`object<what is a class?>`
  - is a :ref:`subclass<how to test if something is a subclass>` of :ref:`object<what is a class?>`

* I remove the commented line from :ref:`test_is_a_dictionary_an_object`

  .. code-block:: python
    :lineno-start: 66

    def test_is_a_dictionary_an_object():
        assert isinstance(dict, object)
        assert issubclass(dict, object)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'test instance vs subclass'

The difference between a :ref:`subclass (child)<how to test if something is a subclass>` I make, and an :ref:`an instance (a copy)<how to test if something is an instance>` is the ``()`` after the name

.. code-block:: python

  a_name = ClassName

points the ``a_name`` :ref:`variable<what is a variable?>` to ``ClassName``

.. code-block:: python

  a_name = ClassName()

points the ``a_name`` :ref:`variable<what is a variable?>` to the result of calling ``ClassName()``.

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

* I go back to the terminal_ where the tests are running

* I add a test to ``test_classes.py`` with a call to the `dir built-in function`_ to get the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of :ref:`object<what is a class?>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 6-9

    def test_is_a_dictionary_an_object():
        assert isinstance(dict, object)
        assert issubclass(dict, object)


    def test_attributes_and_methods_of_objects():
        reality = dir(object)
        my_expectation = []
        assert reality == my_expectation


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       AssertionError:
                assert ['__class__',...ormat__', ...]
                    == []
    E
    E         Left contains 24 more items,
              first extra item: '__class__'
    E         Use -v to get more diff

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I click in the terminal_ where the tests are running then press :kbd:`v` on the keyboard for `pytest-watcher`_ to show me more of the difference between ``reality`` and ``my_expectation`` and it shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E         ...Full output truncated (24 lines hidden),
                 use '-vv' to show

* I press :kbd:`w` on the keyboard in the terminal_ where the tests are running, to show the menu for `pytest-watcher`_ and it shows

  .. code-block:: python
    :emphasize-lines: 2, 10

    [pytest-watcher]
    Current runner args: [-v]

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

* I press :kbd:`c` on the keyboard to change runner args, and the terminal_ shows

  .. code-block:: python
    :emphasize-lines: 7, 14

    [pytest-watcher]
    Current runner args: []

    Controls:
    > Enter : Invoke test runner
    > r     : reset all runner args
    > c     : change runner args
    > f     : run only failed tests (--lf)
    > p     : drop to pdb on fail (--pdb)
    > v     : increase verbosity (-v)
    > e     : Erase terminal screen
    > q     : quit pytest-watcher

    Enter new runner args: -vv

* I press :kbd:`-+v+v` on the keyboard then press :kbd:`enter` to show the full difference, and the terminal_ shows :ref:`AssertionError<what causes AssertionError?>` with the full :ref:`list<what is a list?>`.

* I copy (:kbd:`ctrl/command+c`) the values from the terminal_ and paste (:kbd:`ctrl/command+v`) them as ``my_expectation``

  .. code-block:: python
    :lineno-start: 71
    :emphasize-lines: 3-12
    :emphasize-text: __init__

    def test_attributes_and_methods_of_objects():
        reality = dir(object)
        my_expectation = [
            '__class__', '__delattr__', '__dir__',
            '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__',
            '__getstate__', '__gt__', '__hash__',
            '__init__', '__init_subclass__', '__le__',
            '__lt__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__',
            '__sizeof__', '__str__', '__subclasshook__'
        ]
        assert reality == my_expectation


    # Exceptions seen

  - The test passes.
  - The :ref:`__init__ method<the constructor method>` is in the :ref:`list of attributes and methods<test_attributes_and_methods_of_person_class>`
  - All :ref:`classes<what is a class?>` automatically get these :ref:`attributes<what is a class attribute>`, they inherit them because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.
  - The ``__init__`` :ref:`method<what is a method?>` is also inherited which means when I defined it in :ref:`test_classy_person_says_hello` I overwrote the inherited one.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attributes_and_methods_of_objects'

:ref:`Everything in Python is an object<everything is an object>` because :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`.

----

*********************************************************************************
review
*********************************************************************************

I can make a :ref:`class<what is a class?>` with

* :ref:`pass<test_making_a_class_w_pass>`
* :ref:`parentheses<test_making_a_class_w_parentheses>`
* :ref:`object<test_making_a_class_w_object>`

Everything in Python_ is an :ref:`object<everything is an object>`

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

* I close ``test_classes.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``classes``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<everything is an object: tests>`

----

*************************************************************************************
what is next?
*************************************************************************************

You now know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError?`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hi with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal functions>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`

:ref:`Would you like to test another way to write tests?<another way to write tests>`

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