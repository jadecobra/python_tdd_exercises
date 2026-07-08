.. meta::
  :description: TypeError with classes: calling methods on the class vs instances of the class in Python. TDD tutorial continuing the type_error project with uv run pytest-watcher. Match method calls (AClass.method_00() vs AClass().method_01()) to definitions; implicit self first argument for instance methods. Demonstrates AttributeError "module 'src.type_error' has no attribute 'AClass'", "type object 'AClass' has no attribute 'method_00'", NameError during method setup, TypeError "'NoneType' object is not callable", "AClass.method_01() takes 0 positional arguments but 1 was given", "missing 1 required positional argument: 'self'". Use @staticmethod when no class state needed. Red-green-refactor, remove the commented lines from test and src. Jacob Itegboje Pumping Python TDD.
  :keywords: Jacob Itegboje, Pumping Python, TypeError with classes, python TypeError methods, AClass.method_00, AClass().method_01, staticmethod decorator, takes 0 positional arguments but 1 was given, missing 1 required positional argument: 'self', type object 'AClass' has no attribute, module 'src.type_error' has no attribute 'AClass', test_type_error_w_class_methods, uv run pytest-watcher, TDD class methods, self first argument, class vs instance method call, red green refactor, remove the commented lines, src.type_error, what causes TypeError

.. include:: ../../links.rst

.. _TypeError: https://docs.python.org/3/library/exceptions.html?highlight=exceptions#TypeError

#################################################################################
TypeError with classes
#################################################################################

----

Since :ref:`methods<what is a method?>` are :ref:`functions<what is a function?>` in a :ref:`class<what is a class?>` I can assume that they have the same behavior as what I tested in :ref:`test_type_error_w_positional_arguments`, :ref:`test_type_error_w_keyword_arguments` and :ref:`test_type_error_w_args_and_kwargs`.

The difference is that how :ref:`I call a method<how to call a function>` is affected by if I do it with a :ref:`class<what is a class?>` or an :ref:`instance<how to test if something is an instance>`.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/type_error/tests/test_type_error_w_classes.py
  :language: python
  :linenos:

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
  :lineno-start: 82
  :emphasize-lines: 6-7

      src.type_error.function_08(
          'positional', argument='keyword'
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
    :lineno-start: 87
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

  the test passes because I can use the :ref:`staticmethod decorator<what is the staticmethod decorator?>` if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<what is a class?>`.

  Both :ref:`methods<what is a method?>` look the same. The difference is in how I :ref:`call<how to call a function>` them ``AClass.method_00()`` vs ``AClass().method_01()``.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass().method_02`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 87
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

  the test passes because a :ref:`method<what is a method?>` of an :ref:`instance<how to test if something is an instance>` takes the :ref:`instance of the class<how to test if something is an instance>` (``self``) it belongs to as the first argument which allows it to use things that belong to the :ref:`class<what is a class?>`.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_03`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 87
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

  - ``method_02`` takes an :ref:`instance<how to test if something is an instance>` of the :ref:`class<what is a class?>` it belongs to as input.
  - I :ref:`called the method<how to call a function>` with the :ref:`class<what is a class?>` not an :ref:`instance of the class<how to test if something is an instance>`.

* I use an :ref:`instance of the class<how to test if something is an instance>` to :ref:`call the method<how to call a function>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 3-4

        def method_03():
            # return method_02()
            # return AClass.method_02()
            return AClass().method_02()

  the test passes. This is a silly example because I used ``AClass()`` inside a :ref:`method<what is a method?>` of ``AClass``. I could just use ``self``. I would only need this if I was calling a :ref:`method<what is a method?>` of a different :ref:`class<what is a class?>`.

* Here is another silly example. I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_04`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 6

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_04'.
                    Did you mean: 'method_00'?

* I add :ref:`method definition<how to make a function>` for ``method_04`` to ``AClass`` in ``type_error.py``

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

  - ``method_02`` takes an :ref:`instance<how to test if something is an instance>` of the :ref:`class<what is a class?>` it belongs to as input.
  - I :ref:`called the method<how to call a function>` with the :ref:`class<what is a class?>` not an :ref:`instance of the class<how to test if something is an instance>`.

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
    :lineno-start: 87
    :emphasize-lines: 7

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
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
    :lineno-start: 87
    :emphasize-lines: 8

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
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
    :lineno-start: 87
    :emphasize-lines: 9

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
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

  - ``method_07`` takes an :ref:`instance<how to test if something is an instance>` of the :ref:`class<what is a class?>` it belongs to as input.
  - I :ref:`called the method<how to call a function>` with the :ref:`class<what is a class?>` not an :ref:`instance of the class<how to test if something is an instance>`.

* I use an :ref:`instance of the class<how to test if something is an instance>` to :ref:`call the method<how to call a function>` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 9-10

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
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
  - I called it with an :ref:`instance of the class<how to test if something is an instance>` (``self``) which passes the :ref:`instance<how to test if something is an instance>` as input.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator>` to ``method_00`` of ``AClass`` in ``type_error.py``

  .. code-block:: python
    :lineno-start: 44
    :emphasize-lines: 3

    class AClass(object):

        @staticmethod
        def method_00(): return None

  the test passes. I can use the :ref:`staticmethod decorator<what is the staticmethod decorator?>` if I do not want to add ``self`` to the :ref:`method definition<how to make a function>` when it does not use anything in the :ref:`class<what is a class?>`.

* I add a :ref:`call<how to call a function>` to ``src.type_error.AClass.method_08()`` from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 87
    :emphasize-lines: 11

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()
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
    :lineno-start: 87
    :emphasize-lines: 11-12

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()
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
  - I called it with an :ref:`instance of the class<how to test if something is an instance>` (``self``) which passes the :ref:`instance<how to test if something is an instance>` as input.

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
    :lineno-start: 87
    :emphasize-lines: 13

    def test_type_error_w_class_methods():
        src.type_error.AClass.method_00()
        src.type_error.AClass().method_01()
        src.type_error.AClass().method_02()
        src.type_error.AClass.method_03()
        src.type_error.AClass.method_04()
        src.type_error.AClass().method_05()
        src.type_error.AClass().method_06()
        # src.type_error.AClass.method_07()
        src.type_error.AClass().method_07()
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
  - I called it with an :ref:`instance of the class<how to test if something is an instance>` (``self``) which passes the :ref:`instance<how to test if something is an instance>` as input.

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

        def method_02(self):
            return self.method_01()

        @staticmethod
        def method_03():
            return AClass().method_02()

        @staticmethod
        def method_04():
            return AClass.method_02(AClass)

        def method_05(self):
            return self.method_02()

        def method_06(self):
            return self.method_01()

        def method_07(self):
            return self.method_00()

        def method_08(self):
            return self.method_04()

        def method_09(self):
            return self.method_03()

* I remove the commented lines from ``test_type_error.py``

  .. code-block:: python
    :lineno-start: 87

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
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

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
review
*********************************************************************************

The tests show that

* If I :ref:`call a method<how to call a function>` with an :ref:`instance<how to test if something is an instance>`, it takes the :ref:`instance<how to test if something is an instance>` as the first argument (``self``)
* I can use the :ref:`staticmethod decorator<what is the staticmethod decorator?>` if the :ref:`method<what is a method?>` does not use anything that belongs to the :ref:`class<what is a class?>` it is part of.


All the tests so far show that I get :ref:`TypeError<what causes TypeError?>` when I :ref:`call a function/method<how to call a function>` in a way that is different from its :ref:`definition<how to make a function>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<TypeError with classes: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

so far you know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what an assertion is<what is an assertion?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`what causes TypeError?`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hello with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal functions>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to make a person with a class<how to make a person with a class>`
* :ref:`that everything in Python is an object<everything is an object>`

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