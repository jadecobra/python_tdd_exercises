.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
AttributeError with classes
#################################################################################

----

:ref:`test_attribute_error_w_variables` and :ref:`test_attribute_error_w_functions` show that :ref:`variables<what is a variable?>` and :ref:`functions<what is a function?>` in a :ref:`module<what is a module?>` are :ref:`attributes<what is a class attribute?>` of the :ref:`module<what is a module?>`.

Is a :ref:`class<what is a class?>` in a :ref:`module<what is a module?>` also an :ref:`attribute<what is a class attribute?>` of the :ref:`module<what is a module?>`?

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/attribute_error/tests/test_attribute_error_w_classes.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I `change directory`_ to the :ref:`attribute_error<what causes AttributeError?>` folder_ in the ``pumping_python`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd attribute_error

* I open :ref:`test_attribute_error.py<what causes AttributeError?>`

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell

    tests/test_attribute_error.py ..                  [100%]

    ================== 7 passed in D.EFs ===================

----

*********************************************************************************
test_attribute_error_w_class_attributes
*********************************************************************************



----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running

* I add a test for :ref:`class attributes<what is a class attribute?>` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 17
    :emphasize-lines: 14-15

    def test_attribute_error_w_functions():
        src.attribute_error.function_00()
        src.attribute_error.function_01()
        src.attribute_error.function_02()
        src.attribute_error.function_03()
        src.attribute_error.function_04()
        src.attribute_error.function_05()
        src.attribute_error.function_06()
        src.attribute_error.function_07()
        src.attribute_error.function_08()
        src.attribute_error.function_09()


    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: python

    AttributeError: module 'src.attribute_error'
                    has no attribute 'AClass'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I open ``attribute_error.py``

* I add a :ref:`function<what is a function?>` to ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

    def function_09(): return function_08()


    def AClass(): return function_09()

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: python

    AttributeError: 'function' object
                    has no attribute 'attribute_00'

* I add a :ref:`variable<what is a variable?>` to the :ref:`function <what is a function?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 3

    def AClass():

        attribute_00 = None
        return None

  the terminal_ still shows the same :ref:`Exception<errors>` because I cannot get to a :ref:`variable<what is a variable?>` inside a :ref:`function<what is a function?>` from outside the :ref:`function<what is a function?>`. The :ref:`variable<what is a variable?>` is only used within the :ref:`function<what is a function?>` when it runs.

* I use the :ref:`class<what is a class?>` keyword to change ``AClass`` from a :ref:`function<what is a function?>` to a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 1-2

    # def AClass():
    class AClass(object):

        attribute_00 = None
        return None

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    E    return None
    E    ^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

  because I cannot use a :ref:`return statement<the return statement>` outside a :ref:`function<what is a function?>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 35
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* I comment out the :ref:`return statement<the return statement>` from ``AClass`` in ``attribute_error.py`` since it is no longer a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 4

    # def AClass():
    class AClass(object):

        attribute_00 = None
        # return None

  - the test passes because ``attribute_00`` is now an :ref:`attribute/property<what is a class attribute?>` of the ``AClass`` :ref:`class<what is a class?>`
  - ``AClass`` is an :ref:`attribute<what is a class attribute?>` of the ``attribute_error.py`` :ref:`module<what is a module?>` in the ``src`` folder_
  - I can use ``attribute_00`` from outside the file_ with ``src.attribute_error.AClass.attribute_00`` or ``src.attribute_error.AClass().attribute_00``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 49

    def function_09():
        return None


    class AClass(object):

        attribute_00 = None

* I add a line for ``src.attribute_error.AClass.attribute_01`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 3

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_01'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 4

    class AClass(object):

        attribute_00 = None
        attribute_01 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass.attribute_02`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 4

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_02'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 5

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass.attribute_03`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 5

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_03'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 6

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass.attribute_04`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 6

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03
            src.attribute_error.AClass.attribute_04


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_04'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 7

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass().attribute_05`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 7

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03
            src.attribute_error.AClass.attribute_04
            src.attribute_error.AClass().attribute_05


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_05'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 8

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None

  the test passes because in this case it does not matter if I use the :ref:`class<what is a class?>` (``AClass``) or :ref:`an instance of the class<how to test if something is an instance>`  (``AClass()``).

* I add a line for ``src.attribute_error.AClass().attribute_06`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 8

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03
            src.attribute_error.AClass.attribute_04
            src.attribute_error.AClass().attribute_05
            src.attribute_error.AClass().attribute_06


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_06'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 9

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass().attribute_07`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 9

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03
            src.attribute_error.AClass.attribute_04
            src.attribute_error.AClass().attribute_05
            src.attribute_error.AClass().attribute_06
            src.attribute_error.AClass().attribute_07


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_07'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 10

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass().attribute_08`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 10

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03
            src.attribute_error.AClass.attribute_04
            src.attribute_error.AClass().attribute_05
            src.attribute_error.AClass().attribute_06
            src.attribute_error.AClass().attribute_07
            src.attribute_error.AClass().attribute_08


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_08'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 11

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None

  the test passes.

* I add a line for ``src.attribute_error.AClass().attribute_09`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 31
    :emphasize-lines: 11

        def test_attribute_error_w_class_attributes(self):
            src.attribute_error.AClass.attribute_00
            src.attribute_error.AClass.attribute_01
            src.attribute_error.AClass.attribute_02
            src.attribute_error.AClass.attribute_03
            src.attribute_error.AClass.attribute_04
            src.attribute_error.AClass().attribute_05
            src.attribute_error.AClass().attribute_06
            src.attribute_error.AClass().attribute_07
            src.attribute_error.AClass().attribute_08
            src.attribute_error.AClass().attribute_09


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_09'.
                    Did you mean: 'attribute_00'?

* I add the name to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 12

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None
        attribute_09 = None

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attribute_error_w_class_attributes'


* :ref:`A variable in a class is an attribute of the class<test_attribute_error_w_class_attributes>`
* :ref:`A class in a module is an attribute of the module<test_attribute_error_w_class_attributes>`
* :ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`
* :ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`

----

*********************************************************************************
test_attribute_error_w_class_methods
*********************************************************************************

The tests show that :ref:`variables<what is a variable?>`, :ref:`functions<what is a function?>` and :ref:`classes<what is a class?>` in a :ref:`module<what is a module?>` are :ref:`attributes of the module<what is a class attribute?>`, and :ref:`variables<what is a variable?>` in a :ref:`class<what is a class?>` are :ref:`attributes of the class<what is a class attribute?>`.

:ref:`Methods of a class<what is a method?>` are also :ref:`attributes of the class<what is a class attribute?>`.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test for :ref:`methods<what is a method?>` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 6-7

            src.attribute_error.AClass().attribute_06
            src.attribute_error.AClass().attribute_07
            src.attribute_error.AClass().attribute_08
            src.attribute_error.AClass().attribute_09

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_00'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``AClass`` and point it to :ref:`None<what is None?>`, in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 14

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None
        attribute_09 = None

        method_00 = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because ``method_00`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I use the def_ keyword to change it from a :ref:`variable (attribute)<what is a variable?>` to a :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 14-16

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None
        attribute_09 = None

        # method_00 = None
        def method_00():
            return None

  - the test passes because ``method_00`` is now an :ref:`attribute/property<what is a class attribute?>` of the ``AClass`` :ref:`class<what is a class?>`
  - ``AClass`` is an :ref:`attribute<what is a class attribute?>` of the ``attribute_error.py`` :ref:`module<what is a module?>` in the ``src`` folder_
  - I can call ``method_00`` from outside the file_ with ``src.attribute_error.AClass.method_00()`` or ``src.attribute_error.AClass().method_00()``

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line

  .. code-block:: python
    :lineno-start: 53

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None
        attribute_09 = None

        def method_00():
            return None

* You know the "drill", I add a line for ``src.attribute_error.AClass.method_01`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_01'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 17-18

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None
        attribute_09 = None

        def method_00():
            return None

        def method_01():
            return None

  the test passes because in this case it does not matter if I reference the :ref:`method<what is a method?>` (``AClass.method_01``) or call it  (``AClass.method_01()``).

* I add a line for ``src.attribute_error.AClass.method_02`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 4

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_02'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4-5

        def method_01():
            return None

        def method_02():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_02() takes
               0 positional arguments but 1 was given

  because this happens when ``AClass().method_02()`` is called

  .. code-block:: python

    AClass().method_02()
        AClass.method_02(AClass)

  which raises :ref:`TypeError<what causes TypeError?>` since :ref:`the definition<how to make a function>` of ``method_02`` does not allow it take any :ref:`positional arguments<test_positional_arguments>` (the parentheses are empty).

* I add ``self`` to the parentheses of ``method_02``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 1-2

        # def method_02():
        def method_02(self):
            return None

  the test passes because this happens when ``AClass().method_02()`` is called

  .. code-block:: python

    AClass().method_02()
        AClass.method_02(self)

  where ``self`` is ``AClass``.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` :ref:`method definition<how to make a function>` instead of ``self`` since it does not use anything in the :ref:`class<what is a class?>`. That way I do not send more information than what the :ref:`method<what is a method?>` needs.

  .. code-block:: python
    :lineno-start: 69
    :emphasize-lines: 4-6

        def method_01():
            return None

        @staticmethod
        def method_02():
        # def method_02(self):
            return None

  the test is still green because this now happens when ``AClass().method_02()`` is called

  .. code-block:: python

    AClass().method_02()
        AClass.method_02()

  with the :ref:`staticmethod decorator<what is the staticmethod decorator?>` it does not matter if I call the :ref:`method<what is a method?>` from :ref:`an instance<how to test if something is an instance>` (``AClass()``) or from the :ref:`class<what is a class?>` (``AClass``).

* I remove the commented line

  .. code-block:: python
    :lineno-start: 69

        def method_01():
            return None

        @staticmethod
        def method_02():
            return None

* I add a line for ``src.attribute_error.AClass.method_03`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_03'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 5-6

        @staticmethod
        def method_02():
            return None

        def method_03():
            return None

  the test passes because in this case I reference the :ref:`method<what is a method?>` (``AClass().method_03``), I do not call it (``AClass().method_03()``).

* I add a line for ``src.attribute_error.AClass.method_04`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03
            src.attribute_error.AClass().method_04()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_04'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4-5

        def method_03():
            return None

        def method_04():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_04() takes
               0 positional arguments but 1 was given

  because this happens when ``AClass().method_04()`` is called

  .. code-block:: python

    AClass().method_04()
        AClass.method_04(AClass)

  which raises :ref:`TypeError<what causes TypeError?>` since :ref:`the definition<how to make a function>` of ``method_04`` does not allow it take any :ref:`positional arguments<test_positional_arguments>`.

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to the :ref:`definition<how to make a function>` for ``method_04``

  .. code-block:: python
    :lineno-start: 76
    :emphasize-lines: 4

        def method_03():
            return None

        @staticmethod
        def method_04():
            return None

  the test passes because this now happens when ``AClass().method_04()`` is called

  .. code-block:: python

    AClass().method_04()
        AClass.method_04()

  with the :ref:`staticmethod decorator<what is the staticmethod decorator?>` it does not matter if I call the :ref:`method<what is a method?>` from :ref:`an instance<how to test if something is an instance>` (``AClass()``) or from the :ref:`class<what is a class?>` (``AClass``).

* I add a line for ``src.attribute_error.AClass.method_05`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03
            src.attribute_error.AClass().method_04()
            src.attribute_error.AClass.method_05


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_05'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 79
    :emphasize-lines: 5-6

        @staticmethod
        def method_04():
            return None

        def method_05():
            return None

  the test passes.

* I add a line for ``src.attribute_error.AClass.method_06`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03
            src.attribute_error.AClass().method_04()
            src.attribute_error.AClass.method_05
            src.attribute_error.AClass.method_06()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_06'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 4-5

        def method_05():
            return None

        def method_06():
            return None

  the test passes because this happens when ``AClass.method_06()`` is called

  .. code-block:: python

    AClass.method_06()

  I called the :ref:`method<what is a method>` with the :ref:`class<what is a class?>` (``AClass.method_06()``) not :ref:`an instance of the class<how to test if something is an instance>` (``AClass().method_06()``).

* I add a line for ``src.attribute_error.AClass.method_07`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 9

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03
            src.attribute_error.AClass().method_04()
            src.attribute_error.AClass.method_05
            src.attribute_error.AClass.method_06()
            src.attribute_error.AClass.method_07


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_07'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 86
    :emphasize-lines: 4-5

        def method_06():
            return None

        def method_07():
            return None

  the test passes.

* I add a line for ``src.attribute_error.AClass.method_08`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03
            src.attribute_error.AClass().method_04()
            src.attribute_error.AClass.method_05
            src.attribute_error.AClass.method_06()
            src.attribute_error.AClass.method_07
            src.attribute_error.AClass().method_08()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_08'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 4-5

        def method_07():
            return None

        def method_08():
            return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_08() takes
               0 positional arguments but 1 was given

  because this happens when ``AClass().method_08()`` is called

  .. code-block:: python

    AClass().method_08()
        AClass.method_08(AClass)

  which raises :ref:`TypeError<what causes TypeError?>` since :ref:`the definition<how to make a function>` of ``method_08`` does not allow it take any :ref:`positional arguments<test_positional_arguments>` (the parentheses are empty).

* I add the :ref:`staticmethod decorator<what is the staticmethod decorator?>` to the :ref:`method definition<how to make a function>` since it does not use anything in the :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 89
    :emphasize-lines: 4

        def method_07():
            return None

        @staticmethod
        def method_08():
            return None

  the test passes because this now happens when ``AClass().method_08()`` is called

  .. code-block:: python

    AClass().method_08()
        AClass.method_08()

  with the :ref:`staticmethod decorator<what is the staticmethod decorator?>` it does not matter if I call the :ref:`method<what is a method?>` from :ref:`an instance<how to test if something is an instance>` (``AClass()``) or from the :ref:`class<what is a class?>` (``AClass``).

* I add a line for ``src.attribute_error.AClass.method_09`` to :ref:`test_attribute_error.py<what causes AttributeError?>`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 11

        def test_attribute_error_w_class_methods(self):
            src.attribute_error.AClass.method_00()
            src.attribute_error.AClass.method_01
            src.attribute_error.AClass().method_02()
            src.attribute_error.AClass().method_03
            src.attribute_error.AClass().method_04()
            src.attribute_error.AClass.method_05
            src.attribute_error.AClass.method_06()
            src.attribute_error.AClass.method_07
            src.attribute_error.AClass().method_08()
            src.attribute_error.AClass().method_09


    # Exceptions seen
    # AssertionError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_09'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 53
    :emphasize-lines: 44-45

    class AClass(object):

        attribute_00 = None
        attribute_01 = None
        attribute_02 = None
        attribute_03 = None
        attribute_04 = None
        attribute_05 = None
        attribute_06 = None
        attribute_07 = None
        attribute_08 = None
        attribute_09 = None

        def method_00():
            return None

        def method_01():
            return None

        @staticmethod
        def method_02():
            return None

        def method_03():
            return None

        @staticmethod
        def method_04():
            return None

        def method_05():
            return None

        def method_06():
            return None

        def method_07():
            return None

        @staticmethod
        def method_08():
            return None

        def method_09():
            return None

  the test passes because in this case I reference the :ref:`method<what is a method?>` (``AClass().method_09``), I do not call it (``AClass().method_09()``).

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attribute_error_w_class_methods'


* :ref:`A function in a class is an attribute of the class and is called a method<test_attribute_error_w_class_methods>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``attribute_error.py`` and :ref:`test_attribute_error.py<what causes AttributeError?>`
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``attribute_error``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

All the tests I have run for :ref:`AttributeError<what causes AttributeError?>` show that :ref:`because in Python everything is an object<everything is an object>`

* :ref:`A variable in an object is an attribute of the object<test_attribute_error_w_class_attributes>`
* :ref:`A function in an object is an attribute of the object<test_attribute_error_w_class_methods>`

My problem with the tests is still that they all show the correct way to use :ref:`attributes<what is a class attribute?>` I made in ``attribute_error.py``. If someone reads the file_ or runs it, there is no way for them to know how the code relates to :ref:`AttributeError<what causes AttributeError?>` unless they go through the process with me, there has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AttributeError: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

You know

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

:ref:`Would you like to know where the extra attributes and methods of the Person class came from?<everything is an object>`

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