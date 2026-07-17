.. meta::
  :description: TypeError with classes: calling methods on the class vs instances of the class in Python. TDD tutorial continuing the type_error project with uv run pytest-watcher. Match method calls (AClass.method_00() vs AClass().method_01()) to definitions; implicit self first argument for instance methods. Demonstrates AttributeError "module 'src.type_error' has no attribute 'AClass'", "type object 'AClass' has no attribute 'method_00'", NameError during method setup, TypeError "'NoneType' object is not callable", "AClass.method_01() takes 0 positional arguments but 1 was given", "missing 1 required positional argument: 'self'". Use @staticmethod when no class state needed. Red-green-refactor, remove the commented lines from test and src. Jacob Itegboje Pumping Python TDD.
  :keywords: Jacob Itegboje, Pumping Python, TypeError with classes, python TypeError methods, AClass.method_00, AClass().method_01, staticmethod decorator, takes 0 positional arguments but 1 was given, missing 1 required positional argument: 'self', type object 'AClass' has no attribute, module 'src.type_error' has no attribute 'AClass', test_type_error_w_class_methods, uv run pytest-watcher, TDD class methods, self first argument, class vs instance method call, red green refactor, remove the commented lines, src.type_error, what causes TypeError

.. include:: ../../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
TypeError with classes
#################################################################################

----

Since :ref:`methods<what is a method?>` are :ref:`functions<what is a function?>` in a :ref:`class<everything is an object>` I can assume that they have the same behavior as what I tested in :ref:`test_type_error_w_positional_arguments`, :ref:`test_type_error_w_keyword_arguments` and :ref:`test_type_error_w_args_and_kwargs`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/type_error/tests/test_type_error_w_classes.py
  :language: python
  :linenos:

*********************************************************************************
questions about TypeError with classes
*********************************************************************************

Questions to think about as I go through the chapter

* :ref:`How do methods behave when I call them with a class or an instance<test_type_error_w_class_methods>`?
* :ref:`Is every object callable<test_type_error_w_the_uncallables>`?

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`type_error folder<what causes TypeError?>` in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

* I open ``test_type_error.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_type_error.py ...                              [100%]

    =================== 3 passed in G.HIs ====================

----

*********************************************************************************
test_type_error_w_class_methods
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test with a :ref:`call<how to call a function with input>` to ``AClass.method`` from ``test_type_error.py``

.. code-block:: python
  :lineno-start: 84
  :emphasize-lines: 7-8

        src.type_error.function_08(
            'positional',
            argument='keyword',
        )


    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()


    # Exceptions seen

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.type_error'
                  has no attribute 'AClass'

because ``AClass`` is not defined in ``type_error.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``type_error.py``

* I add a :ref:`class definition<how to make a class>` for ``AClass`` to ``type_error.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 5, 7

    def function_08(name, argument):
        return None


    class AClass(object):

        pass

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: type object 'AClass' has no attribute 'method_00'

  because there is nothing named ``method_00`` in ``AClass``.

* I add the name to the :ref:`class definition<how to make a class>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3-4

    class AClass(object):

        # pass
        method_00

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'method_00' is not defined

* I define ``method_00`` by pointing it to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4-5

    class AClass(object):

        # pass
        # method_00
        method_00 = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``method_00`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I change ``method_00`` to a :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 5-6

    class AClass(object):

        # pass
        # method_00
        # method_00 = None
        def method_00(): return None

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 44

    class AClass(object):

        def method_00(): return None

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass().method_01`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 3

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'AClass' object
                    has no attribute 'method_01'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_01`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 4

    class AClass(object):

        def method_00(): return None
        def method_01(): return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_01() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add :ref:`@staticmethod<what is the staticmethod decorator?>` to ``method_01``

  .. code-block:: python
    :emphasize-lines: 5-6

    class AClass(object):

        def method_00(): return None

        @staticmethod
        def method_01(): return None

  the test passes because I can use the :ref:`staticmethod decorator<what is the staticmethod decorator?>` if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<everything is an object>`.

  Both :ref:`methods<what is a method?>` look the same. The difference is in how I :ref:`call<how to call a function>` them ``AClass.method_00()`` vs ``AClass().method_01()``.

  - ``AClass.method_00()`` :ref:`calls<how to call a function>` ``method_00`` of the ``AClass`` :ref:`class<everything is an object>`.
  - ``AClass().method_01()`` :ref:`calls<how to call a function>` ``method_01`` of an :ref:`instance<how to test if something is an instance>` of the ``AClass`` :ref:`class<everything is an object>`.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass().method_02`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 4

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'AClass' object
                    has no attribute 'method_02'.
                    Did you mean: 'method_00'?

* I add a :ref:`definition<how to make a function>` for ``method_02`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 8

    class AClass(object):

        def method_00(): return None

        @staticmethod
        def method_01(): return None

        def method_02(): return self.method_01()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_02() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add :ref:`@staticmethod<what is the staticmethod decorator?>` to ``method_02``

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4

        @staticmethod
        def method_01(): return None

        @staticmethod
        def method_02(): return self.method_01()

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses of ``method_02``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 2-4

        @staticmethod
        # def method_02(): return self.method_01()
        def method_02(self):
            return self.method_01()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_02() missing
               1 required positional argument: 'self'

* I comment out the :ref:`staticmethod decorator<what is the staticmethod decorator?>`

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 1

        # @staticmethod
        # def method_02(): return self.method_01()
        def method_02(self):
            return self.method_01()

  the test passes because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument which allows it to use things that belong to the :ref:`class<everything is an object>`.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_03`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 5

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_03'.
                    Did you mean: 'method_00'?

* I add a :ref:`definition<how to make a function>` for ``method_03`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 6-7

        # @staticmethod
        # def method_02(): return self.method_01()
        def method_02(self):
            return self.method_01()

        def method_03():
            return method_02()

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'method_02' is not defined

* I add ``AClass.`` before ``method_02``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 2-3

        def method_03():
            # return method_02()
            return AClass.method_02()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_02() missing
               1 required positional argument: 'self'

  because

  - ``method_02`` takes an :ref:`instance<how to test if something is an instance>` of the :ref:`class<everything is an object>` it belongs to as input.
  - I :ref:`called the method<how to call a function>` with the :ref:`class<everything is an object>` not an :ref:`instance of the class<how to test if something is an instance>`.

* I use an :ref:`instance of the class<how to test if something is an instance>` to :ref:`call the method<how to call a function>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3-4

        def method_03():
            # return method_02()
            # return AClass.method_02()
            return AClass().method_02()

  the test passes. This is a silly example because I used ``AClass()`` inside a :ref:`method<what is a method?>` of ``AClass``. I could just use ``self``. I would only need this if I was calling a :ref:`method<what is a method?>` of a different :ref:`class<everything is an object>`.

* Here is another silly example. I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_04`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 93
    :emphasize-lines: 3

        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_04'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_04`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 6-7

        def method_03():
            # return method_02()
            # return AClass.method_02()
            return AClass().method_02()

        def method_04():
            return AClass.method_02()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_02() missing
               1 required positional argument: 'self

  because

  - ``method_02`` takes an :ref:`instance<how to test if something is an instance>` of the :ref:`class<everything is an object>` it belongs to as input.
  - I :ref:`called the method<how to call a function>` with the :ref:`class<everything is an object>` not an :ref:`instance of the class<how to test if something is an instance>`.

* I pass ``AClass`` as input in the :ref:`call<how to call a function with input>` to ``method_02``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 2-3

        def method_04():
            # return AClass.method_02()
            return AClass.method_02(AClass)

  the test passes. I called a :ref:`method<what is a method?>` of ``AClass`` and passed ``AClass`` as input. I can use ``self``.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass().method_05`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 94
    :emphasize-lines: 3

        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
        src.type_error.AClass().method_05()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'AClass' object
                    has no attribute 'method_05'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_05`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 5-6

        def method_04():
            # return AClass.method_02()
            return AClass.method_02(AClass)

        def method_05():
            return method_02()

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add ``self`` to the parentheses of ``method_05``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 1-2

        # def method_05():
        def method_05(self):
            return method_02()

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'method_02' is not defined

  because there is no ``method_02`` at the :ref:`module<what is a module?>` level of ``type_error.py``. It is inside ``AClass`` in ``type_error.py``, I have to be specific.

* I add ``self.`` before ``method_02``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 3-4

        # def method_05():
        def method_05(self):
            # return method_02()
            return self.method_02()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass().method_06`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 95
    :emphasize-lines: 3

        src.type_error.AClass.method_04()
        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'AClass' object
                    has no attribute 'method_06'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_06`` to ``AClass``

  .. code-block:: python
    :lineno-start: 65
    :emphasize-lines: 6-7

        # def method_05():
        def method_05(self):
            # return method_02()
            return self.method_02()

        def method_06():
            return self.method_01()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_06() takes
               0 positional arguments but 1 was given

  because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument.

* I add ``self`` to the parentheses of ``method_06``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 1-2

        # def method_06():
        def method_06(self):
            return self.method_01()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass().method_07`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3

        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()
        src.type_error.AClass.method_07()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: 'AClass' object
                    has no attribute 'method_07'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_07`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 6-7

        # def method_06():
        def method_06(self):
            return self.method_01()

        def method_07(self):
            return self.method_00()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_07() missing
               1 required positional argument: 'self'

  because

  - ``method_07`` takes an :ref:`instance<how to test if something is an instance>` of the :ref:`class<everything is an object>` it belongs to as input.
  - I :ref:`called the method<how to call a function>` with the :ref:`class<everything is an object>` not an :ref:`instance of the class<how to test if something is an instance>`.

* I use an :ref:`instance of the class<how to test if something is an instance>` to :ref:`call the method<how to call a function>` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 96
    :emphasize-lines: 3-4

        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()
        # src.type_error.AClass.method_07()
        src.type_error.AClass().method_07()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_00() takes
               0 positional arguments but 1 was given

  because

  - ``method_00`` takes no input (the parentheses are empty).
  - I called it with an :ref:`instance of the class<how to test if something is an instance>` (``AClass()``) which passes the :ref:`instance<how to test if something is an instance>` as input.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to ``method_00`` of ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3

    class AClass(object):

        @staticmethod
        def method_00(): return None

  the test passes. I can use the :ref:`staticmethod decorator<what is the staticmethod decorator?>` if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<everything is an object>`.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_08()`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 3

        # src.type_error.AClass.method_07()
        src.type_error.AClass().method_07()
        src.type_error.AClass.method_08()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_08'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_08`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 75
    :emphasize-lines: 4-5

        def method_07(self):
            return self.method_00()

        def method_08(self):
            return self.method_04()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_08() missing
               1 required positional argument: 'self'

  because I called ``method_08`` like a :ref:`staticmethod<what is the staticmethod decorator?>` and it is :ref:`defined<how to make a function>` as an :ref:`instance method<how to make a function>` (It expects ``self`` as input).

* I use an :ref:`instance of the class<how to test if something is an instance>` to :ref:`call the method<how to call a function>` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 98
    :emphasize-lines: 3-4

        # src.type_error.AClass.method_07()
        src.type_error.AClass().method_07()
        # src.type_error.AClass.method_08()
        src.type_error.AClass().method_08()


    # Exceptions seen

  the terminal_ shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_04() takes
               0 positional arguments but 1 was given

  because

  - ``method_04`` takes no input (the parentheses are empty).
  - I called it with an :ref:`instance of the class<how to test if something is an instance>` (``AClass()``) which passes the :ref:`instance<how to test if something is an instance>` as input.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to ``method_04`` of ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 57
    :emphasize-lines: 6

        def method_03():
            # return method_02()
            # return AClass.method_02()
            return AClass().method_02()

        @staticmethod
        def method_04():
            # return AClass.method_02()
            return AClass.method_02(AClass)

        # def method_05():
        def method_05(self):
            # return method_02()
            return self.method_02()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_09()`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 3

        # src.type_error.AClass.method_08()
        src.type_error.AClass().method_08()
        src.type_error.AClass().method_09()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_09'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_09`` to ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 4-5

        def method_08(self):
            return self.method_04()

        def method_09(self):
            return self.method_03()

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

     TypeError: AClass.method_03() takes
                0 positional arguments but 1 was given

  because

  - ``method_03`` takes no input (the parentheses are empty).
  - I called it with an :ref:`instance of the class<how to test if something is an instance>` (``AClass()``) which passes the :ref:`instance<how to test if something is an instance>` as input.

* I add the :ref:`@staticmethod<what is the staticmethod decorator?>` to ``method_03`` of ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 6

        # @staticmethod
        # def method_02(): return self.method_01()
        def method_02(self):
            return self.method_01()

        @staticmethod
        def method_03():
            # return method_02()
            # return AClass.method_02()
            return AClass().method_02()

        @staticmethod
        def method_04():
            # return AClass.method_02()
            return AClass.method_02(AClass)

  the test passes.

* I remove the commented lines from ``type_error.py``

  .. code-block:: python
    :lineno-start: 44

    class AClass(object):

        @staticmethod
        def method_00(): return None

        @staticmethod
        def method_01(): return None

  .. code-block:: python
    :lineno-start: 52

        def method_02(self):
            return self.method_01()

        @staticmethod
        def method_03():
            return AClass().method_02()

  .. code-block:: python
    :lineno-start: 59

        @staticmethod
        def method_04():
            return AClass.method_02(AClass)

        def method_05(self):
            return self.method_02()

  .. code-block:: python
    :lineno-start: 66

        def method_06(self):
            return self.method_01()

        def method_07(self):
            return self.method_00()

  .. code-block:: python
    :lineno-start: 72

        def method_08(self):
            return self.method_04()

        def method_09(self):
            return self.method_03()

* I remove the commented lines from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 90

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()
        src.type_error.AClass().method_07()
        src.type_error.AClass().method_08()
        src.type_error.AClass().method_09()


    # Exceptions seen

* I open a new terminal_ then make sure I am in the ``type_error`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd type_error

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_type_error_w_class_methods'

----

*********************************************************************************
test_type_error_w_the_uncallables
*********************************************************************************

Is every :ref:`object callable<how to make a function>`?

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ that is running the tests.
* I add a test to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 100
    :emphasize-lines: 4-5

        src.type_error.AClass().method_09()


    def test_type_error_w_the_uncallables():
        src.type_error.none()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error' has no attribute 'none'

  there is nothing named ``none`` in ``type_error.py`` in the ``src`` folder_ yet

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``none`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    none = None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  - the ``()`` to the right of ``src.type_error.none`` makes it a call
  - the name ``none`` points to :ref:`None<what is None?>` which is NOT :ref:`callable<how to make a function>`. Using substitution

    .. code-block:: python

      none = None   # point the name to the object
      none()        # call the name
      None()        # substitute the value for the name

    ``None()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make ``none`` a :ref:`function<what is a function?>` in ``type_error.py`` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # none = None
    def none(): return None


    def function_00(the_input):
        return None

  the test passes.

I can call a :ref:`function<what is a function?>`, :ref:`I cannot call None<test_type_error_w_the_uncallables>`

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for ``false`` to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 90
    :emphasize-lines: 3

    def test_type_error_w_the_uncallables():
        src.type_error.none()
        src.type_error.false()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'false'

  ``false`` is not in ``type_error.py``

* I add ``false`` to ``type_error.py`` and point it to :ref:`False<test_what_is_false>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    # none = None
    def none(): return None
    false = False


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'bool' object is not callable

  ``false`` points to :ref:`False<test_what_is_false>` which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    false = False
    false()
    False()

  ``False()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a boolean like a function<test_type_error_w_the_uncallables>`

* I change ``false`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # none = None
    def none(): return None
    # false = False
    def false(): return False


    def function_00(the_input):
        return None

  the test is green again.

* I add an :ref:`assertion<what is an assertion?>` for the other :ref:`boolean<what are booleans?>` to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 103
    :emphasize-lines: 4

    def test_type_error_w_the_uncallables():
        src.type_error.none()
        src.type_error.false()
        src.type_error.true()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'true'

  there is nothing named ``true`` in ``type_error.py``

* I add ``true`` and point it to :ref:`True<test_what_is_true>` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 3
    :emphasize-lines: 3

    # false = False
    def false(): return False
    true = True


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'bool' object is not callable

* I change ``true`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 3
    :emphasize-lines: 3-4

    # false = False
    def false(): return False
    # true = True
    def true(): return True


    def function_00(the_input):
        return None

  the test passes. I can call a :ref:`function<what is a function?>`, :ref:`I cannot call a boolean or None<test_type_error_w_the_uncallables>`

----

* I add an :ref:`assertion<what is an assertion?>` for an integer_, to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 105
    :emphasize-lines: 3

        src.type_error.false()
        src.type_error.true()
        src.type_error.an_integer()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'an_integer'

* I add ``an_integer`` and point it to ``1234`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    # true = True
    def true(): return True
    an_integer = 1234


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: python

    TypeError: 'int' object is not callable

  the name ``an_integer`` points to an integer_ (``1234``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    an_integer = 1234  # point the name to the object
    an_integer()       # call the name
    1234()             # substitute the value for the name

  ``1234()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call an integer like a function<test_type_error_w_the_uncallables>`.

* I change ``an_integer`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3-4

    # true = True
    def true(): return True
    # an_integer = 1234
    def an_integer(): return 1234


    def function_00(the_input):
        return None

  the test passes. I can call a :ref:`function<what is a function?>`, :ref:`I cannot call an integer, a boolean or None<test_type_error_w_the_uncallables>`.

* I add an :ref:`assertion<what is an assertion?>` for a float_ to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 106
    :emphasize-lines: 3

        src.type_error.true()
        src.type_error.an_integer()
        src.type_error.a_float()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'a_float'

* I add ``a_float`` and point it to ``5.678`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3

    # an_integer = 1234
    def an_integer(): return 1234
    a_float = 5.678


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'float' object is not callable

  ``a_float`` points to a float_ (``5.678``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    a_float = 5.678
    a_float()
    5.678()

  ``5.678()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a float like a function<test_type_error_w_the_uncallables>`.

* I change ``a_float`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 3-4

    # an_integer = 1234
    def an_integer(): return 1234
    # a_float = 5.678
    def a_float(): return 5.678


    def function_00(the_input):
        return None

  the test passes. I can call a :ref:`function<what is a function?>`, :ref:`I cannot call a float, integer, boolean or None<test_type_error_w_the_uncallables>`.

* I add an :ref:`assertion<what is an assertion?>` for a string_ (anything in :ref:`quotes`) to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 107
    :emphasize-lines: 3

        src.type_error.an_integer()
        src.type_error.a_float()
        src.type_error.a_string()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'a_string'

* I add ``a_string`` and point it to ``'a string'`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 3

    # a_float = 5.678
    def a_float(): return 5.678
    a_string = 'a string'


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'str' object is not callable

  the name ``a_string`` points to a string_ (``'a string'``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    a_string = 'a string' # point the name to the object
    a_string()            # call the name
    'a string'()          # substitute the value for the name

  ``'a string'()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a string like a function<test_type_error_w_the_uncallables>`.

* I change ``a_string`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 3-4

    # a_float = 5.678
    def a_float(): return 5.678
    # a_string = 'a string'
    def a_string(): return 'a string'


    def function_00(the_input):
        return None

  the test passes. I can call a :ref:`function<what is a function?>`. :ref:`I cannot call a string, float, integer, boolean or None<test_type_error_w_the_uncallables>`.

* I add an :ref:`assertion<what is an assertion?>` for a tuple_ (anything in parentheses ``()``, separated by a comma) to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 108
    :emphasize-lines: 3

        src.type_error.a_float()
        src.type_error.a_string()
        src.type_error.a_tuple()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'a_tuple'

* I add ``a_tuple`` and point it to ``(0, 1, 2, 'n')`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3

    # a_string = 'a string'
    def a_string(): return 'a string'
    a_tuple = (0, 1, 2, 'n')


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'tuple' object is not callable

  the name ``a_tuple`` points to a tuple_ (``(0, 1, 2, 'n')``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    a_tuple = (0, 1, 2, 'n')
    a_tuple()
    (0, 1, 2, 'n')()

  ``(0, 1, 2, 'n')()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a tuple like a function<test_type_error_w_the_uncallables>`.

* I change ``a_tuple`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-4

    # a_string = 'a string'
    def a_string(): return 'a string'
    # a_tuple = (0, 1, 2, 'n')
    def a_tuple(): return (0, 1, 2, 'n')


    def function_00(the_input):
        return None

  the test passes. I can call a :ref:`function<what is a function?>`. :ref:`I cannot call a tuple, string, float, integer, boolean or None<test_type_error_w_the_uncallables>`.

* I add an :ref:`assertion<what is an assertion?>` for a :ref:`list<what is a list?>` to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 109
    :emphasize-lines: 3

        src.type_error.a_string()
        src.type_error.a_tuple()
        src.type_error.a_list()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'a_list'

* I add ``a_list`` and point it to ``[0, 1, 2, 'n']`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3

    # a_tuple = (0, 1, 2, 'n')
    def a_tuple(): return (0, 1, 2, 'n')
    a_list = [0, 1, 2, 'n']


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'list' object is not callable

  ``a_list`` points to a :ref:`list<what is a list?>` (``[0, 1, 2, 'n']``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    a_list = [0, 1, 2, 'n']
    a_list()
    [0, 1, 2, 'n']()

  ``[0, 1, 2, 'n']()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a list like a function<test_type_error_w_the_uncallables>`.

* I change ``a_list`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3-4

    # a_tuple = (0, 1, 2, 'n')
    def a_tuple(): return (0, 1, 2, 'n')
    # a_list = [0, 1, 2, 'n']
    def a_list(): return [0, 1, 2, 'n']


    def function_00(the_input):
        return None


  the test passes. I can call a :ref:`function<what is a function?>`, :ref:`I cannot call a list, tuple, string, float, integer, boolean or None<test_type_error_w_the_uncallables>`.

* I add an :ref:`assertion<what is an assertion?>` for a set_ to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 110
    :emphasize-lines: 3

        src.type_error.a_tuple()
        src.type_error.a_list()
        src.type_error.a_set()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'a_set'

* I add ``a_set`` and point it to ``{0, 1, 2, 'n'}`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3

    # a_list = [0, 1, 2, 'n']
    def a_list(): return [0, 1, 2, 'n']
    a_set = {0, 1, 2, 'n'}


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'set' object is not callable

  ``a_set`` points to a set_ (``{0, 1, 2, 'n'}``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    a_set = {0, 1, 2, 'n'}
    a_set()
    {0, 1, 2, 'n'}()

  ``{0, 1, 2, 'n'}()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a set like a function<test_type_error_w_the_uncallables>`.

* I change ``a_set`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 15
    :emphasize-lines: 3-4

    # a_list = [0, 1, 2, 'n']
    def a_list(): return [0, 1, 2, 'n']
    # a_set = {0, 1, 2, 'n'}
    def a_set(): return {0, 1, 2, 'n'}


    def function_00(the_input):
        return None

  the test passes. I can call a :ref:`function<what is a function?>`, :ref:`I cannot call a set, list, tuple, string, float, integer, boolean or None<test_type_error_w_the_uncallables>`.

* I add an :ref:`assertion<what is an assertion?>` for a :ref:`dictionary<what is a dictionary?>` to ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 111
    :emphasize-lines: 3

        src.type_error.a_list()
        src.type_error.a_set()
        src.type_error.a_dictionary()


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.type_error'
                    has no attribute 'a_dictionary'

* I add ``a_dictionary`` and point it to ``{'key': 'value'}`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3

    # a_set = {0, 1, 2, 'n'}
    def a_set(): return {0, 1, 2, 'n'}
    a_dictionary = {'key': 'value'}


    def function_00(the_input):
        return None

  the terminal_ is my friend, and shows TypeError_

  .. code-block:: shell

    TypeError: 'dict' object is not callable

  ``a_dictionary`` points to a :ref:`dictionary<what is a dictionary?>` (``{'key': 'value'}``) which is NOT :ref:`callable<how to make a function>`. Using substitution

  .. code-block:: python

    a_dictionary = {'key': 'value'}
    a_dictionary()
    {'key': 'value'}()

  ``{'key': 'value'}()`` raises :ref:`TypeError<what causes TypeError?>` because :ref:`I cannot call a dictionary like a function<test_type_error_w_the_uncallables>`.

* I change ``a_dictionary`` from a :ref:`variable<what is a variable?>` to a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 3-4

    # a_set = {0, 1, 2, 'n'}
    def a_set(): return {0, 1, 2, 'n'}
    # a_dictionary = {'key': 'value'}
    def a_dictionary(): return {'key': 'value'}


    def function_00(the_input):
        return None

  the test is green again. I can call a :ref:`function<what is a function?>`, :ref:`I cannot call a dictionary, set, list, tuple, string, float, integer, boolean or None<test_type_error_w_the_uncallables>`.

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def none(): return None
    def false(): return False
    def true(): return True
    def an_integer(): return 1234
    def a_float(): return 5.678
    def a_string(): return 'a string'
    def a_tuple(): return (0, 1, 2, 'n')
    def a_list(): return [0, 1, 2, 'n']
    def a_set(): return {0, 1, 2, 'n'}
    def a_dictionary(): return {'key': 'value'}


    def function_00(the_input):
        return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'add test_type_error_w_the_uncallables'

*********************************************************************************
review
*********************************************************************************

The tests show that

* If I :ref:`call a method<how to call a function>` with an :ref:`instance<how to test if something is an instance>`, it takes the :ref:`instance<how to test if something is an instance>` as the first argument (``self``)
* I can use the :ref:`staticmethod decorator<what is the staticmethod decorator?>` if the :ref:`method<what is a method?>` does not use anything that belongs to the :ref:`class<everything is an object>` it is part of.
* :ref:`There are that are not callable<test_type_error_w_the_uncallables>`.


All the tests so far show that I get :ref:`TypeError<what causes TypeError?>` when I :ref:`call an object<everything is an object>` in a way that is different from its :ref:`definition<how to make a function>`.

:ref:`How many questions can you answer about TypeError with class?<questions about TypeError with classes>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<TypeError with classes: tests and solutions>`

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
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.

:ref:`Would you like to see another way to write tests?<another way to write tests>`

-----

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