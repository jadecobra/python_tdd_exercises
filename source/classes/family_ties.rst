.. meta::
  :description: Step-by-step TDD tutorial on Python cooperative multiple inheritance (family ties chapter), Method Resolution Order (MRO), super() for parent __init__ calls, and inheriting from a Person base class built in prior chapters. Follow red-green-refactor to create Doe, Blow, Smith (class attr eye_color), Jane, Joe, Mary (Joe + Jane), John, Lil (Mary + John) with custom last_name and eye_color. Diagnose and fix real beginner errors shown: TypeError: Blow.__init__() takes 1 positional argument but 2 were given, TypeError: got an unexpected keyword argument 'last_name', TypeError: missing 1 required positional argument, AttributeError: module 'src.family_ties' has no attribute 'Blow', AssertionError: 'brown' != '', "is not an instance of", initial AssertionError: True is not false. Uses only local variables in TestFamilyTies methods (no setUp), assertIsInstance/assertNotIsInstance/assertIsSubclass on classes vs instances, dir() comparisons. Builds directly on how_to/make_person (Person + factory), classes, and inheritance ("everything is an object").
  :keywords: Jacob Itegboje, Pumping Python, python cooperative multiple inheritance tutorial, python MRO method resolution order for beginners, super __init__ cooperative inheritance python, family ties python tdd Doe Blow Smith Jane Joe Mary John Lil, python multiple inheritance order of parents matters, TypeError takes 1 positional argument but 2 were given, TypeError got an unexpected keyword argument last_name, AttributeError module src.family_ties has no attribute, AssertionError is not an instance of, python inherit from Person class TDD, no setUp needed local variables each test, assertIsSubclass assertIsInstance unittest inheritance, C3 linearization python, diamond problem python super, red green refactor multiple inheritance, python class with parent tutorial for beginners

.. include:: ../links.rst

.. _super: https://docs.python.org/3/library/functions.html#super
.. _super built-in function: super_
.. _MRO: https://docs.python.org/3/howto/mro.html#python-2-3-mro
.. _Method Resolution Order: MRO_
.. _Python's Method Resolution Order: MRO_
.. _Inheritance: https://grokipedia.com/page/Inheritance_(object-oriented_programming)

#################################################################################
family ties
#################################################################################

The tests from :ref:`everything is an object` show that in Python everything :ref:`inherits<test_attributes_and_methods_of_objects>`. This allows me to make new :ref:`objects<everything is an object>` that get their magic powers from other :ref:`objects<everything is an object>`.

Making new :ref:`objects<everything is an object>` can be easier with :ref:`Inheritance<test_attributes_and_methods_of_objects>` because I do not have to write things that have already been written again, I can :ref:`inherit<test_attributes_and_methods_of_objects>` them instead and change the new :ref:`objects<everything is an object>` to do what I want.

It can also be more complicated because I can make new :ref:`instances<how to test if something is an instance of a class>` to :ref:`inherit<test_attributes_and_methods_of_objects>` from one :ref:`class<what is a class?>` and customize it for what I need instead of making new :ref:`classes<what is a class?>` that require me to keep track of `Python's Method Resolution Order`_.

----

*********************************************************************************
what is Python's Method Resolution Order?
*********************************************************************************

When :ref:`an instance of a class<how to test if something is an instance of a class>` is made, Python_ calls every ``__init__`` :ref:`method<what is a method?>` of the parent and its parent going through every ancestor until it gets to the last one that is needed to make the :ref:`instance<how to test if something is an instance of a class>`.

----

*********************************************************************************
how to make a class with a parent
*********************************************************************************

To use :ref:`inheritance<test_attributes_and_methods_of_objects>` I put the "parent" in parentheses when I :ref:`make<how to make a class>` the new :ref:`object<everything is an object>` (the child) to make the relationship.

.. code-block:: python

  class Child(Parent):

      attribute = SOMETHING

      def method():
          the body of the method
          ...

----

*********************************************************************************
questions about family ties
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`what is Python's Method Resolution Order?`
* :ref:`how can I make a class with inheritance?<test_making_a_class_w_inheritance>`
* :ref:`what is the difference between an instance and a subclass?<more about instances vs subclasses>`
* :ref:`how can I make a class with one parent?<test_classes_w_one_parent>`
* :ref:`what happens when a child calls the parent?`
* :ref:`how can I make a class with more than one parent?<test_classes_w_multiple_parents>`
* :ref:`how can I call a parent class from a child class?<how to call the parent from the child>`
* :ref:`what happens when a class has more than one parent?<what happens when a child has more than one parent?>`

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
* :ref:`what is a class?`
* :ref:`everything is an object`

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

* I make a new file_ in the ``tests`` folder_ named ``test_family_ties.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch tests/test_family_ties.py

* I make a new file_ in the ``src`` folder_ named ``family_ties.py``

  .. code-block:: python
    :emphasize-lines: 1

    touch src/family_ties.py

* I open ``test_family_ties.py``

* I add :ref:`the first failing test<test_failure>` to ``test_family_ties.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1, 4, 6-7

    import unittest


    class TestFamilyTies(unittest.TestCase):

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
    _________________ TestFamilyTies.test_failure __________________

    self = <tests.test_family_ties.TestFamilyTies testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_family_ties.py:7: AssertionError
    =================== short test summary info ====================
    FAILED tests/test_family_ties.py::TestFamilyTies::test_failure - AssertionError: True is not false
    ================= 1 failed, 6 passed in X.YZs ==================

* I add :ref:`AssertionError<what causes AssertionError?>` to the list of :ref:`Exceptions<errors>` seen in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7-8
    :emphasize-text: AssertionError

    class TestFamilyTies(unittest.TestCase):

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
test_making_a_class_w_inheritance
*********************************************************************************

I know from :ref:`test_making_a_class_w_object` that I can make :ref:`classes<what is a class?>` with :ref:`inheritance<test_attributes_and_methods_of_objects>` by stating the parent :ref:`class<what is a class?>` and that :ref:`an instance (a copy)<how to test if something is an instance of a class>` and a :ref:`subclass (child)<how to test if something is a subclass of a class>` are different.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change :ref:`test_failure` to :ref:`test_making_a_class_w_inheritance` with an :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-7

    class TestFamilyTies(unittest.TestCase):

        def test_making_a_class_w_inheritance(self):
            self.assertIsInstance(
                src.family_ties.Doe,
                src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because ``src`` is not defined in this file_.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 4
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

* I add an `import statement`_ for the ``family_ties`` :ref:`module<what is a module?>` at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.family_ties
    import unittest


    class TestFamilyTies(unittest.TestCase):

  - ``import src.family_ties`` brings in an :ref:`object<everything is an object>` for the ``family_ties.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``test_family_ties.py``
  - the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

    .. code-block:: python

      AttributeError: module 'src.family_ties'
                      has no attribute 'Doe'

    because there is no definition for ``Doe`` in ``family_ties.py``

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``family_ties.py`` from the ``src`` folder_

* I add a :ref:`class definition<how to make a class>` definition to ``family_ties.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    class Doe(object): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Doe'> is not
        an instance of <class 'src.person.Person'>

  because ``Doe`` is not an :ref:`instance (a copy)<how to test if something is an instance of a class>` of ``Person``.

* I change the :ref:`assertion<what is an assertion?>` in :ref:`test_making_a_class_w_inheritance` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-3

        def test_making_a_class_w_inheritance(self):
            # self.assertIsInstance(
            self.assertNotIsInstance(
                src.family_ties.Doe,
                src.person.Person
            )


    # Exceptions seen

  the test passes. ``Doe`` is NOT an :ref:`instance<how to test if something is an instance of a class>` of the ``Person`` :ref:`class<what is a class?>`, they are siblings - both children of :ref:`object<everything is an object>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add a call to :ref:`assertIsSubclass<another way to test if something is a subclass of a class>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-11

        def test_making_a_class_w_inheritance(self):
            self.assertIsInstance(
            # self.assertNotIsInstance(
                src.family_ties.Doe,
                src.person.Person
            )

            self.assertIsSubclass(
                src.family_ties.Doe,
                src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Doe'> is not a
        subclass of <class 'src.person.Person'>

  because ``Doe`` is not a child of ``Person``, yet.

* I change the parent of ``Doe`` from ``object`` to ``Person`` in ``family_ties.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # class Doe(object): pass
    class Doe(person.Person): pass

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

  because there is no definition for ``person`` in ``family_ties.py``

* I add an `import statement`_ at the top of ``family_ties.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import person


    # class Doe(object): pass
    class Doe(person.Person): pass

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    E   ModuleNotFoundError: No module named 'person'

  because Python_ cannot find ``person.py`` in the main project folder_ (the parent of ``src`` and ``tests``) where I run the tests from, so it cannot :ref:`import the Module<test_module_not_found_error>`.

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 5
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # ModuleNotFoundError

* I add the path of ``person.py`` from the main project folder_ (the parent of ``src`` and ``tests``) to the `import statement`_, in ``family_ties.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # import person
    import src.person


    # class Doe(object): pass
    class Doe(person.Person): pass

  the terminal_ is my friend, it goes back to :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'person' is not defined

  because there is no definition for ``person`` in this file_.

* I add ``src.`` to the parent of ``Doe``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

    # class Doe(object): pass
    # class Doe(person.Person): pass
    class Doe(src.person.Person): pass

  - ``import src.person`` brings in an :ref:`object<everything is an object>` for the ``person.py`` :ref:`module<what is a module?>` from the ``src`` folder_ so I can use it in ``family_ties.py``.
  - I have to use ``src.person.Person`` in ``family_ties.py`` because I am testing from the root folder_ of the project (the parent folder_ of ``src`` and ``tests``).
  - The test needs to know where ``person.py`` is in relation to where I ran the tests from.
  - This is a problem because if ``family_ties.py`` is run from inside ``src`` the `import statement`_ will not be able to find ``src.person`` from inside ``src``. Same thing if I run the tests from inside ``tests`` :ref:`(a problem for another time)<test_module_not_found_error>`.
  - The test passes because ``Doe`` is now a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Person``.

----

=================================================================================
more about instances vs subclasses
=================================================================================

----

* I add a call to :ref:`assertIsInstance<another way to test if something is an instance of a class>` to show that ``src.family_ties.Doe`` is not an :ref:`instance<how to test if something is an instance of a class>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-11

        def test_making_a_class_w_inheritance(self):
            # self.assertIsInstance(
            self.assertNotIsInstance(
                src.family_ties.Doe,
                src.person.Person
            )

            self.assertIsInstance(
                src.family_ties.Doe,
                src.family_ties.Doe
            )

            self.assertIsSubclass(
                src.family_ties.Doe,
                src.person.Person
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Doe'> is not
        an instance of <class 'src.family_ties.Doe'>

  because a :ref:`class<what is a class?>` is not an :ref:`instance<how to test if something is an instance of a class>`.

* I change :ref:`assertIsInstance<another way to test if something is an instance of a class>` to :ref:`assertNotIsInstance<another way to test if something is NOT an instance of a class>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8-9

        def test_making_a_class_w_inheritance(self):
            # self.assertIsInstance(
            self.assertNotIsInstance(
                src.family_ties.Doe,
                src.person.Person
            )

            # self.assertIsInstance(
            self.assertNotIsInstance(
                src.family_ties.Doe,
                src.family_ties.Doe
            )

            self.assertIsSubclass(
                src.family_ties.Doe,
                src.person.Person
            )


    # Exceptions seen

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_making_a_class_w_inheritance(self):
            doe_class = src.family_ties.Doe

            # self.assertIsInstance(
            self.assertNotIsInstance(
                src.family_ties.Doe,
                src.person.Person
            )

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.family_ties.Doe`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6-7, 13-15, 19-20

        def test_making_a_class_w_inheritance(self):
            doe_class = src.family_ties.Doe

            # self.assertIsInstance(
            self.assertNotIsInstance(
                # src.family_ties.Doe,
                doe_class,
                src.person.Person
            )

            # self.assertIsInstance(
            self.assertNotIsInstance(
                # src.family_ties.Doe,
                # src.family_ties.Doe
                doe_class, doe_class
            )

            self.assertIsSubclass(
                # src.family_ties.Doe,
                doe_class,
                src.person.Person
            )


    # Exceptions seen

  the test is still green.

----

=================================================================================
what happens when a child calls the parent?
=================================================================================

----

* I add a call to the :ref:`assertIsInstance method<another way to test if something is an instance of a class>`, this time with an :ref:`instance<how to test if something is an instance of a class>` of ``Doe``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 7-10

            self.assertIsSubclass(
                # src.family_ties.Doe,
                doe_class,
                src.person.Person
            )

            self.assertIsInstance(
                src.family_ties.Doe(),
                src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  I called ``Doe`` to make an :ref:`instance<how to test if something is an instance of a class>`. How did ``Person.__init__`` get called?

* Here is what is happens when ``src.class.Doe()`` runs

  .. code-block:: python

    src.family_ties.Doe()
    Doe # has no __init__
    # call the parent of Doe (Person)
    Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` takes one required argument for ``first_name``.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 36
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

* I add the `super built-in function`_ to ``Doe`` to call the parent ``__init__`` :ref:`method<what is a method?>` (``Parent.__init__``) directly from ``Doe``, in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4, 6-7

    # class Doe(object): pass
    # class Doe(person.Person): pass
    # class Doe(src.person.Person): pass
    class Doe(src.person.Person):

        def __init__(self):
            super().__init__()

  - the `super built-in function`_ calls the ``__init__`` :ref:`method<what is a method?>` of the parent :ref:`class<what is a class?>`
  - ``super()`` is the parent - ":ref:`super class<how to call the parent from the child>`" for parent, ":ref:`subclass<how to test if something is a subclass of a class>`" for child
  - ``super`` is ``Person`` in this case
  - ``super().__init__()`` is ``Person.__init__()`` in this case
  - the terminal_ still shows :ref:`TypeError<what causes TypeError?>`

    .. code-block:: python

      TypeError: Person.__init__() missing 1
                 required positional argument: 'first_name'

    because this is what happens now when ``src.class.Doe()`` runs

    .. code-block:: python

      src.family_ties.Doe()
      Doe.__init__()
          super().__init__()
      # super is the parent (Person)
      Person.__init__()

    which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of the ``Person`` :ref:`class<what is a class?>` takes one required argument for ``first_name``.

* I add a value for ``first_name`` to the call to ``src.family_ties.Doe()`` in :ref:`test_making_a_class_w_inheritance` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 2-3

            self.assertIsInstance(
                # src.family_ties.Doe(),
                src.family_ties.Doe('the_first'),
                src.person.Person
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Doe.__init__() takes
               1 positional argument but 2 were given

  because this happens when ``src.family_ties.Doe('the_first')`` runs

  .. code-block:: python

    src.family_ties.Doe('the_first')
    Doe.__init__('the_first')

  - which raises :ref:`TypeError<what causes TypeError?>` since the definition for the ``__init__`` :ref:`method<what is a method?>` of ``Doe`` only takes one :ref:`positional argument<test_positional_arguments>` (``self``) and it was called with two (``self`` and ``'the_first'``)
  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Doe.__init__()``, ``self`` is ``Doe`` in ``Doe``. It would be like calling ``Doe.__init__(Doe)``.

* I add a parameter for ``first_name`` to the ``__init__`` :ref:`method<what is a method?>` of ``Doe`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 5
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

  because this happens when ``src.family_ties.Doe('the_first')`` runs

  .. code-block:: python

    src.family_ties.Doe('the_first')
    Doe.__init__('the_first')
        super().__init__() # call the parent
    Person.__init__()

  - which raises :ref:`TypeError<what causes TypeError?>` since the definition for the ``__init__`` :ref:`method<what is a method?>` of ``Person`` requires a :ref:`positional argument<test_positional_arguments>` for ``first_name`` and it was called with ``self``
  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Person.__init__()``, ``self`` is ``Person`` in ``Person``. It would be like calling ``Person.__init__(Person)``.

* I add the required parameter to ``super().__init__()`` in ``Doe``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 8-9

    # class Doe(object): pass
    # class Doe(person.Person): pass
    # class Doe(src.person.Person): pass
    class Doe(src.person.Person):

        # def __init__(self):
        def __init__(self, first_name):
            # super().__init__()
            super().__init__(first_name)

  the test passes because

  - :ref:`an instance (a copy)<how to test if something is an instance of a class>` of ``Doe`` is an :ref:`an instance (a copy)<how to test if something is an instance of a class>` of ``Person``
  - ``Person`` is the parent of ``Doe``
  - the test shows that this happens when ``src.family_ties.Doe('the_first')`` runs

    .. code-block:: python

      src.family_ties.Doe('the_first')
      Doe.__init__('the_first')
          super().__init__('the_first')
      Person.__init__('the_first')

* I add a test for the :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` of the ``Doe`` :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7-10

            self.assertIsInstance(
                # src.family_ties.Doe(),
                src.family_ties.Doe('the_first'),
                src.person.Person
            )

            self.assertEqual(
                dir(doe_class),
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
    :lineno-start: 36
    :emphasize-lines: 3-4

            self.assertEqual(
                dir(doe_class),
                # []
                dir(src.person.Person)
            )


    # Exceptions seen

  the test passes because ``Doe`` has the same :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` as ``Person`` because ``Doe`` is a :ref:`child<how to test if something is a subclass of a class>` of ``Parent``.

* I add a :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2

        def test_making_a_class_w_inheritance(self):
            person_class = src.person.Person
            doe_class = src.family_ties.Doe

* I use the :ref:`variable<what is a variable?>` to remove repetition of ``src.person.Person`` from the test

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 9-10, 23-24, 30-31, 37-38

        def test_making_a_class_w_inheritance(self):
            person_class = src.person.Person
            doe_class = src.family_ties.Doe

            # self.assertIsInstance(
            self.assertNotIsInstance(
                # src.family_ties.Doe,
                doe_class,
                # src.person.Person
                person_class
            )

            # self.assertIsInstance(
            self.assertNotIsInstance(
                # src.family_ties.Doe,
                # src.family_ties.Doe
                doe_class, doe_class
            )

            self.assertIsSubclass(
                # src.family_ties.Doe,
                doe_class,
                # src.person.Person
                person_class
            )

            self.assertIsInstance(
                # src.family_ties.Doe(),
                src.family_ties.Doe('the_first'),
                # src.person.Person
                person_class
            )

            self.assertEqual(
                dir(doe_class),
                # []
                # dir(src.person.Person)
                dir(person_class)
            )


    # Exceptions seen

  still green.

* I add a :ref:`variable<what is a variable?>` for ``src.family_ties.Doe('the_first')``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_making_a_class_w_inheritance(self):
            person_class = src.person.Person
            doe_class = src.family_ties.Doe
            doe_instance = doe_class('the_first')

            # self.assertIsInstance(
            self.assertNotIsInstance(
                # src.family_ties.Doe,
                doe_class,
                # src.person.Person
                person_class
            )

* I use the new :ref:`variable<what is a variable?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 3-4

            self.assertIsInstance(
                # src.family_ties.Doe(),
                # src.family_ties.Doe('the_first'),
                doe_instance,
                # src.person.Person
                person_class
            )

  green, because ``doe_class()`` and ``src.classes.Doe()`` are the same since ``doe_class = src.classes.Doe``.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7, 11, 15, 19, 23

        def test_making_a_class_w_inheritance(self):
            person_class = src.person.Person
            doe_class = src.family_ties.Doe
            doe_instance = doe_class('the_first')

            self.assertNotIsInstance(
                doe_class, person_class
            )

            self.assertNotIsInstance(
                doe_class, doe_class
            )

            self.assertIsSubclass(
                doe_class, person_class
            )

            self.assertIsInstance(
                doe_instance, person_class
            )

            self.assertEqual(
                dir(doe_class), dir(person_class)
            )


    # Exceptions seen

* I remove the commented lines from ``family_ties.py``

  .. code-block:: python
    :linenos:

    import src.person


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

I want to test how the :ref:`attributes<what is a class attribute?>` of :ref:`classes<what is a class?>` are set if they have only one parent (super :ref:`class<what is a class?>`).

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new test for :ref:`Inheritance<test_attributes_and_methods_of_objects>` with an :ref:`assertion<what is an assertion?>`, in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 5-7

            self.assertEqual(
                dir(doe_class), dir(person_class)
            )

        def test_classes_w_one_parent(self):
            doe = src.family_ties.Doe('the_first')
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
  :lineno-start: 32
  :emphasize-lines: 3-4

      def test_classes_w_one_parent(self):
          doe = src.family_ties.Doe('the_first')
          # self.assertEqual(doe.last_name, '')
          self.assertEqual(doe.last_name, 'doe')


  # Exceptions seen

the test passes because this happens when ``doe = src.family_ties.Doe('the_first')`` runs

.. code-block:: python

  doe = src.family_ties.Doe('the_first')
        Doe.__init__('the_first')
            super().__init__(first_name)
        Person.__init__('the_first')
            Person.__init__('the_first', last_name='the_first')
            self.last_name = 'the_first' # use the default value

the value for ``doe.last_name`` is ``doe`` because :ref:`a method uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add another :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 6-7
    :emphasize-text: joe

        def test_classes_w_one_parent(self):
            doe = src.family_ties.Doe('the_first')
            # self.assertEqual(doe.last_name, '')
            self.assertEqual(doe.last_name, 'doe')

            joe = src.family_ties.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.family_ties' has no attribute 'Blow'

  because there is no :ref:`definition<how to make a class>` for ``Blow`` in ``family_ties.py``

* I add a new :ref:`class definition<how to make a class>` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 7

    class Doe(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name)


    class Blow(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

  because this happens when ``joe = src.family_ties.Blow('joe')`` runs

  .. code-block:: python

    joe = src.family_ties.Blow('joe')
          Blow # has no __init__
          # call the parent of Blow (Person)
          Person.__init__('joe')
              Person.__init__('joe', last_name='doe')
              self.last_name = 'doe' # use the default value

* I add a :ref:`class attribute<what is a class attribute?>` for ``last_name`` in the ``Blow`` :ref:`class<what is a class?>` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 1-2, 4

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        last_name = 'blow'

  the terminal_ does not feel like my friend, it still shows :ref:`AssertionError<what causes AssertionError?>` because this happens when ``joe = src.family_ties.Blow('joe')`` runs

  .. code-block:: python

    joe = src.family_ties.Blow('joe')
          Blow # has no __init__
          # call the parent of Blow (Person)
              self.last_name = 'blow'
          Person.__init__('joe')
              Person.__init__('joe', last_name='doe')
              self.last_name = 'doe' # use the default value

  the value for ``last_name`` does not get sent to the parent (``Person.__init__``)

* I add the ``__init__`` :ref:`method<what is a method?>` to customize the last name

  .. code-block:: python
    :lineno-start: 10
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

  because this happens when ``joe = src.family_ties.Blow('joe')`` runs

  .. code-block:: python

    joe = src.family_ties.Blow('joe')
          Blow.__init__('joe')

  - which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Blow`` only takes one :ref:`positional argument<test_positional_arguments>` (``self``) and it got called with two (``self`` and ``first_name``).

  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Blow.__init__('joe')``, ``self`` is ``Blow`` in ``Blow``. It would be like calling ``Blow.__init__(Blow, 'joe')``.


* I add ``first_name`` to the parentheses of the ``__init__`` :ref:`method definition<how to make a function>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-7

    # class Blow(src.person.Person): pass
    class Blow(src.person.Person):

        # last_name = 'blow'

        # def __init__(self):
        def __init__(self, first_name):
            self.last_name = 'blow'

  the test passes because this happens when ``joe = src.family_ties.Blow('joe')`` runs

  .. code-block:: python

    joe = src.family_ties.Blow('joe')
          Blow.__init__('joe')
              self.last_name = 'joe'

  I can :ref:`make classes<how to make a class>` that are related and have their own defaults. In this test

  - the ``Doe`` :ref:`class<what is a class?>` has a default value for the ``last_name`` :ref:`attribute<what is a class attribute?>` that is the :ref:`default value<test_optional_arguments>` for the ``last_name`` :ref:`attribute<what is a class attribute?>` of ``Person``
  - the ``Blow`` :ref:`class<what is a class?>` has a different :ref:`default value<test_optional_arguments>` for the value of the  ``last_name`` :ref:`attribute<what is a class attribute?>`
  - ``Doe`` and ``Blow`` are :ref:`children (subclasses)<how to test if something is a subclass of a class>` of ``Person``

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 4

    class Doe(src.person.Person):

        def __init__(self, first_name):
            super().__init__(first_name)


    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'blow'

* In this case there is a simpler way to make ``joe`` and ``doe``. I could pass the values to the ``Person`` :ref:`class<what is a class?>` directly, since all the ``Blow`` :ref:`class<what is a class?>` does is customize the ``last_name`` :ref:`attribute<what is a class attribute?>`, there is nothing special about it or the ``Doe`` :ref:`class<what is a class?>`. I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_one_parent` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 9-10
    :emphasize-text: person

        def test_classes_w_one_parent(self):
            doe = src.family_ties.Doe('the_first')
            # self.assertEqual(doe.last_name, '')
            self.assertEqual(doe.last_name, 'doe')

            joe = src.family_ties.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')

            blow = src.person.Person('joe')
            self.assertEqual(blow.last_name, joe.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'blow'

* I add ``last_name='blow'`` to the call

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 1-2

            # blow = src.person.Person('joe')
            blow = src.person.Person('joe', last_name='blow')
            self.assertEqual(blow.last_name, joe.last_name)


    # Exceptions seen

  the test passes. I can make :ref:`an instance of a class<how to test if something is an instance of a class>` and change the values of its :ref:`attributes<what is a class attribute?>` without making a new :ref:`class<what is a class?>`.

* I add an :ref:`assertion<what is an assertion?>` for ``jane``

  .. code-block:: python
    :lineno-start: 40
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
    :lineno-start: 44
    :emphasize-lines: 2-3

            jane = src.person.Person('jane')
            # self.assertEqual(jane.last_name, blow.last_name)
            self.assertEqual(jane.last_name, doe.last_name)


    # Exceptions seen

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``john``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-6

            jane = src.person.Person('jane')
            # self.assertEqual(jane.last_name, blow.last_name)
            self.assertEqual(jane.last_name, doe.last_name)

            john = src.family_ties.Smith('john')
            self.assertEqual(john.last_name, 'smith')


    # Exceptions seen

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.family_ties'
                    has no attribute 'Smith'

* I add a :ref:`class definition<how to make a class>` for ``Smith`` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 7

    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'blow'


    class Smith(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'smith'

  because this happens when ``john = src.family_ties.Smith('john')`` runs

  .. code-block:: python

    john = src.family_ties.Smith('john')
           Smith # has no __init__
           # call the parent of Smith (Person)
           Person.__init__('john')
               Person.__init__('john', last_name='doe')
               self.last_name = 'doe' # use the default value

* I add the ``__init__`` :ref:`method<what is a method?>` to ``Smith``

  .. code-block:: Python
    :lineno-start: 16
    :emphasize-lines: 1-2, 4-5

    # class Smith(src.person.Person): pass
    class Smith(src.person.Person):

        def __init__(self):
            self.last_name = 'smith'

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Smith.__init__() takes 1
               positional argument but 2 were given

  because this happens when ``john = src.family_ties.Smith('john')`` runs

  .. code-block:: python

    john = src.family_ties.Smith('john')
           Smith.__init__('john')

  - which raises :ref:`TypeError<what causes TypeError?>` since the definition for the ``__init__`` :ref:`method<what is a method?>` of ``Smith`` takes only one :ref:`positional argument<test_positional_arguments>` (``self``) and it got called with two (``self`` and ``'john'``)
  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Smith.__init__('john')``, ``self`` is ``Smith`` in ``Smith``. It would be like calling ``Smith.__init__(Smith, 'john')``.

* I add ``first_name`` to the parentheses of the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 4-5

    # class Smith(src.person.Person): pass
    class Smith(src.person.Person):

        # def __init__(self):
        def __init__(self, first_name):
            self.last_name = 'smith'

  the test passes because this happens when ``john = src.family_ties.Smith('john')`` runs

  .. code-block:: python

    john = src.family_ties.Smith('john')
           Smith.__init__('john')
               self.last_name = 'smith'

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 10

    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'blow'


    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'smith'

  the test passes.

* I add another :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_one_parent` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4-5
    :emphasize-text: person

            john = src.family_ties.Smith('john')
            self.assertEqual(john.last_name, 'smith')

            smith = src.person.Person('john', 'smith')
            self.assertEqual(smith.last_name, doe.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != 'doe'

* I change the expectation

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3

            smith = src.person.Person('john', 'smith')
            # self.assertEqual(smith.last_name, doe.last_name)
            self.assertEqual(smith.last_name, john.last_name)


    # Exceptions seen

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 32

        def test_classes_w_one_parent(self):
            doe = src.family_ties.Doe('the_first')
            self.assertEqual(doe.last_name, 'doe')

            joe = src.family_ties.Blow('joe')
            self.assertEqual(joe.last_name, 'blow')

            blow = src.person.Person('joe', last_name='blow')
            self.assertEqual(blow.last_name, joe.last_name)

            jane = src.person.Person('jane')
            self.assertEqual(jane.last_name, doe.last_name)

            john = src.family_ties.Smith('john')
            self.assertEqual(john.last_name, 'smith')

            smith = src.person.Person('john', 'smith')
            self.assertEqual(smith.last_name, john.last_name)


    # Exceptions seen

  * From the :ref:`class definition<how to make a class>` of ``Doe``, this happens when :ref:`an instance (a copy)<how to test if something is an instance of a class>` of ``Doe`` is made

    .. code-block:: python

      src.family_ties.Doe('first_name')
      Doe.__init__('first_name')
          super().__init__(first_name)
      Person.__init__('first_name')
          Person.__init__('first_name', last_name='doe')
          self.last_name = 'doe' # use the default value

    because :ref:`a method uses the default value for the parameter because it is called without the parameter<test_optional_arguments>`.

  * From the :ref:`class definitions<how to make a class>` of ``Smith`` and ``Blow`` this happens when :ref:`an instance (a copy)<how to test if something is an instance of a class>` of ``Smith`` or ``Blow`` is made

    .. code-block:: python

      src.family_ties.ClassName('first_name')
      ClassName.__init__('first_name')
          self.last_name = 'last_name'

    where ``ClassName`` is ``Smith`` or ``Blow``

  * From the :ref:`class definition of Person<test_factory_person_says_hello>`, this happens when :ref:`an instance (a copy)<how to test if something is an instance of a class>` of the ``Person`` :ref:`class<what is a class?>` is made

    .. code-block:: python

      src.person.Person(first_name, last_name=last_name)
      Person.__init__(first_name, last_name=last_name)
          self.first_name = first_name
          self.last_name = last_name

  it will use the :ref:`default value<test_optional_arguments>` for ``last_name`` if no value is given because :ref:`a function uses the default value for the parameter because it is called without the parameter<test_optional_arguments>`.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_classes_w_one_parent'

:ref:`I can customize child classes with the __init__ method<test_classes_w_one_parent>`.

----

*********************************************************************************
test_classes_w_multiple_parents
*********************************************************************************

Can a :ref:`class<what is a class?>` have more than one parent? How are the :ref:`attributes<what is a class attribute?>` set if they have more than one parent (super :ref:`class<what is a class?>`)?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test with an :ref:`assertion<what is an assertion?>` for ``jane``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4-6
    :emphasize-text: Jane

            smith = src.person.Person('john', 'smith')
            self.assertEqual(smith.last_name, john.last_name)

        def test_classes_w_multiple_parents(self):
            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.family_ties'
                    has no attribute 'Jane'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`class definition<how to make a class>` for ``Jane`` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 7

    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'smith'


    class Jane(src.person.Person): pass

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``jane = src.family_ties.Jane()`` runs

  .. code-block:: python

    jane = src.family_ties.Jane()
           Jane # has no __init__
           # call the parent of Jane (Person)
           Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Person`` requires one positional argument (``first_name``) and it got called with zero

* I add the ``__init__`` :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``Jane``

  .. code-block:: python
    :lineno-start: 22
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
    :lineno-start: 22
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

* I add an :ref:`assertion<what is an assertion?>` for the value of the  ``last_name`` :ref:`attribute<what is a class attribute?>` of ``jane`` to :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4

        def test_classes_w_multiple_parents(self):
            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Jane' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add a value for ``last_name`` to ``Jane`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 6

    # class Jane(src.person.Person): pass
    class Jane(src.person.Person):

        def __init__(self):
            self.first_name = 'jane'
            self.last_name = 'doe'
            return None

  the test passes. This is a repetition because

  - the :ref:`default value<test_optional_arguments>` for ``Person`` is ``doe``
  - ``Jane`` is a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Person``

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_multiple_parents` to make sure ``Jane`` is a ``Doe``, in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-7

        def test_classes_w_multiple_parents(self):
            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsSubclass(
                src.family_ties.Jane, src.family_ties.Doe
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Jane'> is not
        a subclass of <class 'src.family_ties.Doe'>

* I change the parent of ``Jane`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 2-3

    # class Jane(src.person.Person): pass
    # class Jane(src.person.Person):
    class Jane(Doe):

        def __init__(self):
            self.first_name = 'jane'
            self.last_name = 'doe'
            return None

  the test passes.

* I add a call to the `super built-in function`_ to use to remove the repetition of ``last_name``

  .. code-block:: python
    :lineno-start: 22
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

  because this happens when ``jane = src.family_ties.Jane()`` runs

  .. code-block:: python

    jane = src.family_ties.Jane()
           Jane.__init__()
               super().__init__()
           Doe.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Doe`` requires two positional arguments (``self`` and ``first_name``) and it got called with one (``self``)

* I add ``jane`` as the value for ``first_name`` in the call to the parent

  .. code-block:: python
    :lineno-start: 22
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

  the test is green again because this happens when ``jane = src.family_ties.Jane()`` runs

  .. code-block:: python

    jane = src.family_ties.Jane()
           Jane.__init__()
               super().__init__('jane')
           Doe.__init__('jane')
               super().__init__(first_name)
           Person.__init__('jane')
               Person.__init__('jane', last_name='doe')
               self.first_name = 'jane'
               self.last_name = 'doe' # use the default value

  :ref:`a method uses the default value for the parameter because it is called without the parameter<test_optional_arguments>`.

----

* I add an :ref:`assertion<what is an assertion?>` for ``mary``, another instance of ``Jane`` to :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 9-10

        def test_classes_w_multiple_parents(self):
            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsSubclass(
                src.family_ties.Jane, src.family_ties.Doe
            )

            mary = src.family_ties.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Jane.__init__() takes 1
               positional argument but 2 were given

  because this happens when ``mary = src.family_ties.Jane('mary')`` runs

  .. code-block:: python

    mary = src.family_ties.Jane('mary')
           Jane.__init__('mary')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` takes one :ref:`positional argument<test_positional_arguments>` (``self``) and it was called with two (``self`` and ``'mary'``)

* I add ``first_name`` to the parentheses for the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 22
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

  I broke the :ref:`assertion<what is an assertion?>` for ``jane`` because this happens when ``jane = src.family_ties.Jane()`` runs

  .. code-block:: python

    jane = src.family_ties.Jane()
           Jane.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` takes two required :ref:`positional arguments<test_positional_arguments>` (``self`` and ``first_name``) and the call only sends one (``self``).

* I add a :ref:`default value<test_optional_arguments>` to make ``first_name`` optional

  .. code-block:: python
    :lineno-start: 22
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

  because this happens when ``mary = src.family_ties.Jane('mary')`` runs

  .. code-block:: python
    :emphasize-text: jane

    mary = src.family_ties.Jane('mary')
           Jane.__init__('mary')
               super().__init__('jane')
           Doe.__init__('jane')
               super().__init__(first_name)
           Person.__init__('jane')
               Person.__init__('jane', last_name='doe')
               self.first_name = 'jane'
               self.last_name = 'doe'

  The parent of ``Jane (Doe)`` gets called with a different value for the ``first_name`` parameter.

* I change the call to the `super built-in function`_ to use the name instead of a fixed value

  .. code-block:: python
    :lineno-start: 22
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
    :lineno-start: 16

    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.last_name = 'smith'


    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)

* I add an :ref:`assertion<what is an assertion?>` that will fail, for the last name of ``mary`` in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3

            mary = src.family_ties.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')
            self.assertEqual(mary.last_name, mary.first_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'doe' != 'mary'

* I change the expectation to match reality

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 3-4

            mary = src.family_ties.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the test passes because ``mary`` and ``jane`` are :ref:`instances<how to test if something is an instance of a class>` of ``Jane``

----

* I add an :ref:`assertion<what is an assertion?>` for ``joe``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-3
    :emphasize-text: Joe

        def test_classes_w_multiple_parents(self):
            joe = src.family_ties.Joe()
            self.assertEqual(joe.first_name, 'joe')

            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertIsSubclass(
                src.family_ties.Jane, src.family_ties.Doe
            )

            mary = src.family_ties.Jane('mary')
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        module 'src.family_ties' has no attribute 'Joe'.
        Did you mean: 'Doe'?

* I add a :ref:`class definition<how to make a class>` for the ``Joe`` :ref:`class<what is a class?>` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 7

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)


    class Joe(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``joe = src.family_ties.Joe()`` runs

  .. code-block:: python

    joe = src.family_ties.Joe()
          Person.__init__()

  - which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` takes two required :ref:`positional arguments<test_positional_arguments>` (``self`` and ``first_name``) and it was called with one (``self``)
  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Joe.__init__()``, ``self`` is ``Joe`` in ``Joe``. It would be like calling ``Joe.__init__(Joe)``

* I add the ``__init__`` :ref:`method<what is a method?>` to ``Joe``

  .. code-block:: python
    :lineno-start: 28
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
    :lineno-start: 28
    :emphasize-lines: 5

    # class Joe(src.person.Person): pass
    class Joe(src.person.Person):

        def __init__(self):
            self.first_name = 'joe'
            return None

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to :ref:`test_classes_w_multiple_parents` to make sure that ``joe`` is a ``Blow``, in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 4

        def test_classes_w_multiple_parents(self):
            joe = src.family_ties.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Joe' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add ``last_name`` to the ``__init__`` :ref:`method<what is a method?>` of ``Joe`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 28
    :emphasize-lines: 6

    # class Joe(src.person.Person): pass
    class Joe(src.person.Person):

        def __init__(self):
            self.first_name = 'joe'
            self.last_name = 'blow'
            return None

  the test passes. I cheated, which means I need a better test.

* I add :ref:`assertIsSubclass<another way to test if something is a subclass of a class>` to :ref:`test_classes_w_multiple_parents` to make sure ``Joe`` is a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Blow``, in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-7

        def test_classes_w_multiple_parents(self):
            joe = src.family_ties.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            self.assertIsSubclass(
                src.family_ties.Joe, src.family_ties.Blow
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Joe'> is
        not a subclass of <class 'src.family_ties.Blow'>

* I change the parent of ``Joe`` to ``Blow`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 28
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
    :lineno-start: 28
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

  because this happens when ``joe = src.family_ties.Joe()`` runs

  .. code-block:: python

    joe = src.family_ties.Joe()
          Joe.__init__()
              super().__init__('joe')
          Blow.__init__('joe')
              self.last_name = 'blow'

  there is no assignment of a value to the ``first_name`` :ref:`attribute<what is a class attribute?>` in ``Blow``.

* I add ``self.first_name`` to ``Blow``

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 4

    class Blow(src.person.Person):

        def __init__(self, first_name):
            self.first_name = first_name
            self.last_name = 'blow'

  the test passes because this happens when ``joe = src.family_ties.Joe()`` runs

  .. code-block:: python

    joe = src.family_ties.Joe()
          Joe.__init__()
              super().__init__('joe')
          Blow.__init__('joe')
              self.first_name = 'joe'
              self.last_name = 'blow'

* I remove the commented lines and ``return None``, from ``Joe``

  .. code-block:: python
    :lineno-start: 23

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)


    class Joe(Blow):

        def __init__(self):
            super().__init__('joe')

----

* I change ``mary`` to be an :ref:`instance<how to test if something is an instance of a class>` of ``Mary``, a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Jane``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 1-2

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.family_ties'
                    has no attribute 'Mary'

* I add a :ref:`class definition<how to make a class>` for ``Mary`` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 7, 9-10

    class Joe(Blow):

        def __init__(self):
            super().__init__('joe')


    class Mary(Jane): pass

  the terminal_ is my friend, and shows :ref:`AssertionError<what is an assertion?>`

  .. code-block:: shell

    AssertionError: 'jane' != 'mary'

  because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary # has no __init__
           # call the parent of Mary (Jane)
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
    :lineno-start: 35
    :emphasize-lines: 1-2, 4-5

    # class Mary(Jane): pass
    class Mary(Jane):

        def __init__(self):
            self.first_name = 'mary'

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Mary' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

  because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
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
  - the :ref:`default value<test_optional_arguments>` for ``last_name`` in ``Person`` is ``'doe'``

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

  the test is still green because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
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

* I add a call to the :ref:`assertNotIsSubclass method<another way to test if something is NOT a subclass of a class>` to :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 6-8

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            self.assertNotIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Mary'> is
        a subclass of <class 'src.family_ties.Jane'>

* I change :ref:`assertNotIsSubclass<another way to test if something is NOT a subclass of a class>` to the :ref:`assertIsSubclass method<another way to test if something is a subclass of a class>`

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 6-7

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )


    # Exceptions seen

  the test passes.

----

=================================================================================
what happens when a child has more than one parent?
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` to test if I can make ``Joe`` and ``Jane`` both be parents of ``Mary``?

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 10-12

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.Mary'> is not
        a subclass of <class 'src.family_ties.Joe'>

  because ``Mary`` is not a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Joe``.

* I add ``Joe`` as a parent of ``Mary`` in ``family_ties.py``

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

  because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
               super().__init__(first_name)
           Doe.__init__('mary')
               super().__init__(first_name)
           # call the next parent of Mary
           Joe.__init__('mary')

  - which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Joe`` only takes one :ref:`positional argument<test_positional_arguments>` (``self``) and it got called with two (``self`` and ``mary``)
  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Joe.__init__('mary')``, ``self`` is ``Joe`` in ``Joe``. It would be like calling ``Joe.__init__(Joe, 'mary')``.

* I change the ``__init__`` :ref:`method<what is a method?>` of ``Joe`` to take a ``first_name`` argument

  .. code-block:: python
    :lineno-start: 29
    :emphasize-lines: 3-4

    class Joe(Blow):

        # def __init__(self):
        def __init__(self, first_name):
            super().__init__('joe')

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Joe.__init__() missing 1
               required positional argument: 'first_name'

  I broke the ``joe = src.family_ties.Joe()`` call because the ``__init__`` :ref:`method<what is a method?>` now has two required :ref:`positional arguments<test_positional_arguments>` (``self`` and ``first_name``) and it was called with one (``self``)

* I add a :ref:`default value<test_optional_arguments>` to make ``first_name`` optional

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

  for ``mary.first_name`` because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
               super().__init__(first_name)
           Doe.__init__('mary')
               super().__init__(first_name)
           Joe.__init__('mary')
               super().__init__('joe') # the problem
           Blow.__init__('joe')
               self.first_name = 'joe'
               self.last_name = 'blow'

* I use the parameter name in the call to ``super`` instead of a fixed value in ``Joe``

  .. code-block:: python
    :lineno-start: 29
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

* I change the expectation of the :ref:`assertion<what is an assertion?>` in :ref:`test_classes_w_multiple_parents` for the last name of ``mary`` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 66
    :emphasize-lines: 5-6

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )


    # Exceptions seen

  the test passes.

----

* I change the order of the parents of ``Mary`` to see what it does to the value of ``last_name``, in ``family_ties.py``

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

  the test is still green because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary.__init__()
               super().__init__('mary')
           Joe.__init__('mary')
               super().__init__(first_name)
           Blow.__init__('mary')
               self.first_name = 'mary'
               self.last_name = 'blow'

  the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` did not get called even though it is a parent of ``Mary``

* I add an :ref:`assertion<what is an assertion?>` to show this in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 59
    :emphasize-lines: 4

            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertEqual(jane.eye_color, 'green')
            self.assertIsSubclass(
                src.family_ties.Jane, src.family_ties.Doe
            )

            # mary = src.family_ties.Jane('mary')

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AttributeError: 'Jane' object has no attribute 'eye_color'

* I add a :ref:`class attribute<what is a class attribute?>` to ``Jane`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 23
    :emphasize-lines: 5

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)
            self.eye_color = 'green'


  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``Mary`` in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 7

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            self.assertEqual(mary.eye_color, jane.eye_color)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Mary' object has no attribute 'eye_color'

  because the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` did not get called.

* I change the order of the parents of ``Mary`` from ``(Joe, Jane)`` back to ``(Jane, Joe)`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-4

    # class Mary(Jane): pass
    # class Mary(Jane):
    class Mary(Jane, Joe):
    # class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the test passes because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary.__init__()
               super().__init__('mary')
           Jane.__init__('mary')
               super().__init__(first_name)
               self.eye_color = 'green'
           Doe.__init__('mary')
               super().__init__(first_name)
           Joe.__init__('mary')
               super().__init__('joe')
           Blow.__init__('mary')
               self.first_name = 'mary'
               self.last_name = 'blow'

  The order of the parents matters.

  - If the order is ``(Jane, Joe)`` then :ref:`instances<how to test if something is an instance of a class>` of ``Mary`` get the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``Jane``.
  - If the order is ``(Joe, Jane)`` then :ref:`instances<how to test if something is an instance of a class>` of ``Mary`` do NOT get the ``eye_color`` :ref:`attribute<what is a class attribute?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` does not get called.

* I change the order of the parents to ``(Joe, Jane)`` again

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 3-4

    # class Mary(Jane): pass
    # class Mary(Jane):
    # class Mary(Jane, Joe):
    class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')
            # self.first_name = 'mary'
            # self.last_name = 'doe'

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'Mary' object has no attribute 'eye_color'

* I add the ``eye_color`` :ref:`class attribute<what is a class attribute?>` to ``Joe``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8

    class Joe(Blow):

        # def __init__(self):
        # def __init__(self, first_name):
        def __init__(self, first_name='joe'):
            # super().__init__('joe')
            super().__init__(first_name)
            self.eye_color = 'blue'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blue' != 'green'

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``mary.eye_color`` in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 7-8

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # self.assertEqual(mary.eye_color, jane.eye_color)
            self.assertEqual(mary.eye_color, joe.eye_color)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )


    # Exceptions seen

  the test passes because this happens when ``mary = src.family_ties.Mary()`` runs

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary.__init__()
               super().__init__('mary')
           Joe.__init__('mary')
               super().__init__(first_name)
               self.eye_color = 'blue'
           Blow.__init__('mary')
               self.first_name = 'mary'
               self.last_name = 'blow'

  The order of the parents matters.

  - If the order is ``(Jane, Joe)`` then :ref:`instances<how to test if something is an instance of a class>`  of ``Mary`` get the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``Jane``.
  - If the order is ``(Joe, Jane)`` then

    * :ref:`instances<how to test if something is an instance of a class>`  of ``Mary`` get the ``eye_color`` :ref:`attribute<what is a class attribute?>` of ``Joe``
    * the  ``__init__`` :ref:`method<what is a method?>` of ``Jane`` does not get called


* I remove the commented lines from ``Joe`` and ``Mary`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 23

    class Jane(Doe):

        def __init__(self, first_name='jane'):
            super().__init__(first_name)
            self.eye_color = 'green'


    class Joe(Blow):

        def __init__(self, first_name='joe'):
            super().__init__(first_name)
            self.eye_color = 'blue'


    class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')

----

* I add ``john`` to :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 17-18

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            # self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.last_name, joe.last_name)
            # self.assertEqual(mary.eye_color, jane.eye_color)
            self.assertEqual(mary.eye_color, joe.eye_color)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.family_ties'
                    has no attribute 'John'

* I add a :ref:`class definition<how to make a class>` for ``John`` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 37
    :emphasize-lines: 7

    class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')


    class John(src.person.Person): pass

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: Person.__init__() missing 1
               required positional argument: 'first_name'

  because this happens when ``john = src.family_ties.John()`` runs

  .. code-block:: python

    john = src.family_ties.John()
           Person.__init__()

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Person`` takes two :ref:`positional arguments<test_positional_arguments>` (``self`` and ``first_name``) and it got called with one (``self``)

* I add the ``__init__`` :ref:`method<what is a method?>` to ``John`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 1-2, 4-5

    # class John(src.person.Person): pass
    class John(src.person.Person):

        def __init__(self):
            self.first_name = 'john'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to make sure that ``John`` is a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``Smith``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3-5

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')
            self.assertIsSubclass(
                src.family_ties.John, src.family_ties.Smith
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError:
        <class 'src.family_ties.John'> is
        a subclass of <class 'src.family_ties.Smith'>

  no cheating this time.

* I change the parent of ``John`` to ``Smith`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-3

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        def __init__(self):
            self.first_name = 'john'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``last_name`` :ref:`attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 3

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertIsSubclass(
                src.family_ties.John, src.family_ties.Smith
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'John' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add a :ref:`class attribute<what is a class attribute?>` for ``last_name`` to ``John`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

    # class John(src.person.Person): pass
    # class John(src.person.Person):
    class John(Smith):

        def __init__(self):
            self.first_name = 'john'
            self.last_name = 'smith'

  the test passes. This is a repetition because

  - ``John`` is a ``Smith``
  - the ``last_name`` :ref:`attribute<what is a class attribute?>` of :ref:`instances<how to test if something is an instance of a class>` of ``Smith`` is ``'smith'``

* I add a call to the `super built-in function`_ so :ref:`instances<how to test if something is an instance of a class>` of ``John`` can inherit the ``last_name`` :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 43
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

* I add the ``first_name`` :ref:`attribute<what is a class attribute?>` to ``Smith``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 4

    class Smith(src.person.Person):

        def __init__(self, first_name):
            self.first_name = first_name
            self.last_name = 'smith'

  the test passes because this happens when ``john = src.family_ties.John()`` runs

  .. code-block:: python

    john = src.family_ties.John()
           John.__init__()
               super().__init__('john')
           Smith.__init__('john')
               self.first_name = 'john'
               self.last_name = 'smith'

* I remove the commented lines from ``John``

  .. code-block:: python
    :lineno-start: 38

    class Mary(Joe, Jane):

        def __init__(self):
            super().__init__('mary')


    class John(Smith):

        def __init__(self):
            super().__init__('john')

----

* I add ``lil``, an :ref:`instance<how to test if something is an instance of a class>` of a :ref:`child (subclass)<how to test if something is a subclass of a class>` of ``John`` to :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 8-11

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertIsSubclass(
                src.family_ties.John, src.family_ties.Smith
            )

            lil = src.family_ties.Lil()
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.family_ties' has no attribute 'Lil'

* I add a :ref:`class definition<how to make a class>` for ``Lil`` to ``family_ties.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 7

    class John(Smith):

        def __init__(self):
            super().__init__('john')


    class Lil(John): pass

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` to test ``John`` and ``Mary`` as parents of ``Lil``?

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 5-7

            lil = src.family_ties.Lil()
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.Mary
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <class 'src.family_ties.Lil'> is not
                    a subclass of <class 'src.family_ties.Mary'>

* I add ``Mary`` as a parent to ``Lil`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 1-2

    # class Lil(John): pass
    class Lil(John, Mary): pass

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``first_name`` :ref:`attribute<what is a class attribute?>` of ``lil`` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 2

            lil = src.family_ties.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.Mary
            )


    # Exceptions seen

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'john' != 'lil'

  because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil # has no __init__
          # call the parent of Lil (John)
          John.__init__()
              super().__init__('john')
          Smith.__init__('john')
              self.first_name = 'john'
              self.last_name = 'smith'

* I add the ``__init__`` :ref:`method<what is a method?>` with a value for the ``first_name`` :ref:`attribute<what is a class attribute?>` into ``Lil`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 2-3, 5-6

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):

        def __init__(self):
            self.first_name = 'lil'

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for the ``last_name`` :ref:`attribute<what is an attribute?>` of ``lil``, in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 3

            lil = src.family_ties.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, john.last_name)
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.Mary
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError:
        'Lil' object has no attribute 'last_name'.
        Did you mean: 'first_name'?

* I add a value for ``last_name`` to ``Lil`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 7

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):

        def __init__(self):
            self.first_name = 'lil'
            self.last_name = 'smith'

  the test passes. This is a repetition, and a problem if the value of the ``last_name`` :ref:`attribute<what is a class attribute?>` of the parent changes.

* I add a call to the `super built-in function`_ to remove the repetition

  .. code-block:: python
    :lineno-start: 50
    :emphasize-lines: 6-8

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    class Lil(John, Mary):

        def __init__(self):
            super().__init__('lil')
            # self.first_name = 'lil'
            # self.last_name = 'smith'

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: John.__init__() takes 1
               positional argument but 2 were given

  because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``John`` takes one :ref:`positional argument<test_positional_arguments>` (``self``) and it was called with two (``self`` and ``lil``)

* I change the ``__init__`` :ref:`method<what is a method?>` in ``John`` to take in a parameter for ``first_name`` with a :ref:`default value<test_optional_arguments>` to make it optional

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3-6

    class John(Smith):

        # def __init__(self):
        def __init__(self, first_name='john'):
            # super().__init__('john')
            super().__init__(first_name)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'smith' != 'blow'

  because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(first_name)
              self.first_name = first_name
              self.last_name = last_name

  the ``__init__`` :ref:`method<what is a method?>` of ``Mary`` did not get called.

* I add a call to the `super built-in function`_ in ``Smith``

  .. code-block:: python
    :lineno-start: 17
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

  because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='smith',
              )
          # call the next parent of Lil
          Mary.__init__(
              first_name='lil',
              last_name='smith'
          )

  - which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Mary`` was called with a :ref:`keyword argument<test_keyword_arguments>` and it only takes ``self``
  - ``self`` is the :ref:`class<what is a class?>` itself, which means that for ``Mary.__init__(first_name='lil', last_name='smith')``, ``self`` is ``Mary`` in ``Mary``. It would be like calling ``Mary.__init__(Mary, first_name='lil', last_name='smith')``.

* I add ``first_name`` with a :ref:`default value<test_optional_arguments>` to the ``__init__`` :ref:`method<what is a method?>` of ``Mary``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 3-6

    class Mary(Joe, Jane):

        # def __init__(self):
        def __init__(self, first_name='mary'):
            # super().__init__('mary')
            super().__init__(first_name)

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: Mary.__init__() got
               an unexpected keyword argument 'last_name'.
               Did you mean 'first_name'?

* I add ``last_name`` to the ``__init__`` :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 4-5

    class Mary(Joe, Jane):

        # def __init__(self):
        # def __init__(self, first_name='mary'):
        def __init__(self, first_name='mary', last_name):
            # super().__init__('mary')
            super().__init__(first_name)

  the terminal_ shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
                 follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a :ref:`default value<test_optional_arguments>` for ``last_name``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 5-9

    class Mary(Joe, Jane):

        # def __init__(self):
        # def __init__(self, first_name='mary'):
        # def __init__(self, first_name='mary', last_name):
        def __init__(
                self, first_name='mary',
                last_name=None,
            ):
            # super().__init__('mary')
            super().__init__(first_name)

  the test passes because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          John.__init__('lil')
              super().__init__(first_name)
          Smith.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='smith',
              )
          Mary.__init__('lil', 'smith')
              super().__init__(first_name)
              # no last_name passed to Parent
          Joe.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'blue'
          Blow.__init__('lil')
              self.first_name = 'lil'
              self.last_name = 'blow'

  the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` did not get called.

* I change the order of the parents of ``Lil`` to ``(Mary, John)`` to see if the value will change to ``john.last_name``

  .. code-block:: python
    :lineno-start: 63
    :emphasize-lines: 3-4

    # class Lil(John): pass
    # class Lil(John, Mary): pass
    # class Lil(John, Mary):
    class Lil(Mary, John):

        def __init__(self):
            super().__init__('lil')
            # self.first_name = 'lil'
            # self.last_name = 'smith'

  the test is still green because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__('lil')
              Mary.__init__('lil', last_name=None)
              # use the default value
              super().__init__(first_name)
              # no last_name passed to Parent
          Joe.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'blue'
          Blow.__init__('lil')
              self.first_name = 'lil'
              self.last_name = 'blow'

  the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` did not get called.

* I add a call to the `super built-in function`_ in ``Blow``

  .. code-block:: python
    :lineno-start: 10
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
        Jane.__init__() got
        an unexpected keyword argument 'last_name'.
        Did you mean 'first_name'?

  because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__('lil')
              Mary.__init__('lil', last_name=None)
              # use the default value
              super().__init__(first_name)
              # no last_name passed to Parent
          Joe.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'blue'
          Blow.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='blow'
              )
          # call the next parent of Mary
          Jane.__init__('lil', last_name='blow')

  which raises :ref:`TypeError<what causes TypeError?>` since the ``__init__`` :ref:`method<what is a method?>` of ``Jane`` does not have a parameter named ``last_name``. Confused?

* I add ``last_name`` to ``Jane``

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 3-4

    class Jane(Doe):

        # def __init__(self, first_name='jane'):
        def __init__(self, first_name='jane', last_name):
            super().__init__(first_name)
            self.eye_color = 'green'

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default
                 follows parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I give ``last_name`` a :ref:`default value<test_optional_arguments>`

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

    AssertionError: 'doe' != 'blow'

  for the expectation of ``mary.last_name`` because this happens when ``mary = src.family_ties.Mary()`` runs, if the parents of ``Mary`` are ``(Joe, Jane)``

  .. code-block:: python

    mary = src.family_ties.Mary()
           Mary.__init__(
               first_name='mary',
               last_name=None,
           )
               super().__init__(first_name)
           Joe.__init__('mary')
               super().__init__(first_name)
               self.eye_color = 'blue'
           Blow.__init__('mary')
               super().__init__(
                   first_name=first_name,
                   last_name='blow'
               )
           # call the next parent of Mary
           Jane.__init__('mary', last_name='blow')
               super().__init__('mary')
               self.eye_color = 'green'
           Doe.__init__('mary')
               super().__init__('mary')
           Person.__init__('mary')
               Person.__init__('mary', last_name='doe')
               self.first_name = 'mary'
               self.last_name = 'doe' # use the default value

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``mary.last_name`` in :ref:`test_classes_w_multiple_parents`

  .. code-block:: python
    :lineno-start: 67
    :emphasize-lines: 4-5

            # mary = src.family_ties.Jane('mary')
            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            # self.assertEqual(mary.last_name, mary.first_name)
            self.assertEqual(mary.last_name, jane.last_name)
            # self.assertEqual(mary.last_name, joe.last_name)
            # self.assertEqual(mary.eye_color, jane.eye_color)
            self.assertEqual(mary.eye_color, joe.eye_color)
            # self.assertNotIsSubclass(
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )

  the test passes because this happens when ``lil = src.family_ties.Lil()`` runs

  .. code-block:: python

    lil = src.family_ties.Lil()
          Lil.__init__()
              super().__init__('lil')
          Mary.__init__(
              first_name='lil',
              last_name=None,
          )
              super().__init__(first_name)
          Joe.__init__('lil')
              super().__init__(first_name)
              self.eye_color = 'blue'
          Blow.__init__('lil')
              super().__init__(
                  first_name=first_name,
                  last_name='blow'
              )
          # call the next parent of Mary
          Jane.__init__(
              first_name='lil',
              last_name='blow',
          )
              super().__init__('lil')
              # last_name does not get passed to parent
              self.eye_color = 'green'
          Doe.__init__('lil')
              super().__init__('lil')
          # call the next parent of Lil
          John.__init__('lil')
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

* I remove the commented lines from ``family_ties.py``

  .. code-block:: python
    :lineno-start: 10

    class Blow(src.person.Person):

        def __init__(self, first_name):
            super().__init__(
                first_name=first_name,
                last_name='blow',
            )


    class Smith(src.person.Person):

        def __init__(self, first_name):
            super().__init__(
                first_name=first_name,
                last_name='smith',
            )


    class Jane(Doe):

        def __init__(
                self, first_name='jane',
                last_name=None
            ):
            super().__init__(first_name)
            self.eye_color = 'green'


    class Joe(Blow):

        def __init__(self, first_name='joe'):
            super().__init__(first_name)
            self.eye_color = 'blue'


    class Mary(Joe, Jane):

        def __init__(
                self, first_name='mary',
                last_name=None,
            ):
            super().__init__(first_name)


    class John(Smith):

        def __init__(self, first_name='john'):
            super().__init__(first_name)


    class Lil(Mary, John):

        def __init__(self):
            super().__init__('lil')

----

* I add an :ref:`assertion<what is an assertion?>` for ``lil.eye_color`` to test if :ref:`instances<how to test if something is an instance of a class>` of ``Lil`` inherit ``eye_color`` from ``Jane`` or ``Joe``, in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 4

            lil = src.family_ties.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, john.last_name)
            self.assertEqual(lil.eye_color, jane.eye_color)
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.Mary
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blue' != 'green'

* I change the expectation of the :ref:`assertion<what causes AssertionError?>`

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 4-5

            lil = src.family_ties.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, john.last_name)
            # self.assertEqual(lil.eye_color, jane.eye_color)
            self.assertEqual(lil.eye_color, mary.eye_color)
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.Mary
            )


    # Exceptions seen

  - :ref:`instances<how to test if something is an instance of a class>` of ``Lil`` :ref:`inherit<test_attributes_and_methods_of_objects>` ``eye_color`` from ``Mary``
  - :ref:`instances<how to test if something is an instance of a class>` of ``Mary`` :ref:`inherit<test_attributes_and_methods_of_objects>` ``eye_color`` from ``Joe``
  - :ref:`instances<how to test if something is an instance of a class>` of ``Lil`` :ref:`inherit<test_attributes_and_methods_of_objects>` ``last_name`` from ``John``
  - :ref:`instances<how to test if something is an instance of a class>` of ``John`` :ref:`inherit<test_attributes_and_methods_of_objects>` ``last_name`` from ``Smith``

----

* I add an :ref:`assertion<what is an assertion?>` for ``joe.eye_color`` that will fail

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5

        def test_classes_w_multiple_parents(self):
            joe = src.family_ties.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            self.assertEqual(joe.eye_color, '')
            self.assertIsSubclass(
                src.family_ties.Joe, src.family_ties.Blow
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'blue' != ''

* I change the expectation of the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 5-6

        def test_classes_w_multiple_parents(self):
            joe = src.family_ties.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            # self.assertEqual(joe.eye_color, '')
            self.assertEqual(joe.eye_color, 'blue')
            self.assertIsSubclass(
                src.family_ties.Joe, src.family_ties.Blow
            )

  the test passes.

* I add an :ref:`assertion<what is an assertion?>` for ``john.eye_color``

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 4

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertEqual(john.eye_color, '')
            self.assertIsSubclass(
                src.family_ties.John, src.family_ties.Smith
            )

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'John' object has no attribute 'eye_color'

* I add the ``eye_color`` :ref:`attribute<what is a class attribute?>` to ``Smith`` in ``family_ties.py``

  .. code-block:: python
    :lineno-start: 19
    :emphasize-lines: 3

    class Smith(src.person.Person):

        eye_color = 'brown'

        def __init__(self, first_name):
            super().__init__(
                first_name=first_name,
                last_name='smith',
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 'brown' != ''

* I change the expectation of the :ref:`assertion<what is an assertion?>` for ``john.eye_color`` in :ref:`test_classes_w_multiple_parents` in ``test_family_ties.py``

  .. code-block:: python
    :lineno-start: 85
    :emphasize-lines: 4-5

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            # self.assertEqual(john.eye_color, '')
            self.assertEqual(john.eye_color, 'brown')
            self.assertIsSubclass(
                src.family_ties.John, src.family_ties.Smith
            )

  the test passes.

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 51

        def test_classes_w_multiple_parents(self):
            joe = src.family_ties.Joe()
            self.assertEqual(joe.first_name, 'joe')
            self.assertEqual(joe.last_name, 'blow')
            self.assertEqual(joe.eye_color, 'blue')
            self.assertIsSubclass(
                src.family_ties.Joe, src.family_ties.Blow
            )

            jane = src.family_ties.Jane()
            self.assertEqual(jane.first_name, 'jane')
            self.assertEqual(jane.last_name, 'doe')
            self.assertEqual(jane.eye_color, 'green')
            self.assertIsSubclass(
                src.family_ties.Jane, src.family_ties.Doe
            )

            mary = src.family_ties.Mary()
            self.assertEqual(mary.first_name, 'mary')
            self.assertEqual(mary.last_name, jane.last_name)
            self.assertEqual(mary.eye_color, joe.eye_color)
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Jane
            )
            self.assertIsSubclass(
                src.family_ties.Mary, src.family_ties.Joe
            )

            john = src.family_ties.John()
            self.assertEqual(john.first_name, 'john')
            self.assertEqual(john.last_name, 'smith')
            self.assertEqual(john.eye_color, 'brown')
            self.assertIsSubclass(
                src.family_ties.John, src.family_ties.Smith
            )

            lil = src.family_ties.Lil()
            self.assertEqual(lil.first_name, 'lil')
            self.assertEqual(lil.last_name, john.last_name)
            self.assertEqual(lil.eye_color, mary.eye_color)
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.John
            )
            self.assertIsSubclass(
                src.family_ties.Lil, src.family_ties.Mary
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # ModuleNotFoundError
    # TypeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_classes_w_multiple_parents'

.. NOTE:: All the instances could have been made with only the ``Person`` :ref:`class<what is a class?>` because there was nothing unique about the :ref:`classes<what is a class?>` I made in ``family_ties.py`` and it would not have given me the chance to practice making classes with multiple parents and seeing how Python_ resolves them.

  .. code-block:: python

    joe = src.family_ties.Joe()
    joe = src.person.Person('joe', last_name='blow')
    joe.eye_color = 'blue'

  .. code-block:: python

    jane = src.family_ties.Jane()
    jane = src.person.Person('jane')
    jane.eye_color = 'green'

  .. code-block:: python

    mary = src.family_ties.Mary()
    mary = src.person.Person('mary', joe.last_name)
    mary.eye_color = joe.eye_color

  .. code-block:: python

    john = src.family_ties.John()
    john = src.person.Person('john', 'smith')
    john.eye_color = 'brown'

  .. code-block:: python

    lil = src.family_ties.Lil()
    lil = src.person.Person('lil', john.last_name)
    lil.eye_color = mary.eye_color

  which would have just been Python_ making these calls to make :ref:`instances (copies)<how to test if something is an instance of a class>` of the ``Person`` :ref:`class<what is a class?>`

  .. code-block:: python

    a_name = src.person.Person(first_name, last_name=last_name)
             Person.__init__(first_name, last_name=last_name)
             self.first_name = first_name
             self.last_name = last_name
    a_name.eye_color = color

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
* :ref:`all classes inherit from 'object'<test_making_a_class_w_object>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_family_ties.py`` and ``family_ties.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``person``

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

:ref:`Do you want to see all the CODE I typed in this chapter?<classes: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

:ref:`how to make a Python test driven development environment manually`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`how to make classes<classes>`
* :ref:`how to use class attributes to remove repetition<AssertionError 2: use class attributes>`
* :ref:`what happens when classes have one or more parents<family ties>`


:ref:`Would you like to use class attributes with the 'functions' project?<Functions 2: use class attributes>`

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