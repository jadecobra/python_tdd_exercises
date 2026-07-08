.. meta::
  :description:
    Step-by-step TDD continuation in the attribute_error project showing AttributeError with classes: deliberately trigger "type object 'AClass' has no attribute 'attribute_01'. Did you mean: 'attribute_00'?", SyntaxError: 'return' outside function, NameError: name 'self' is not defined, TypeError missing 1 required positional argument: 'self' when calling method on the class instead of instance. Add 10 class attributes (chained from function_09(), using both AClass.attr and AClass().attr) and 10 methods (with self, some bare attr access and some calls in tests). Demonstrates a class in a module and a function in a class (method) are attributes too. Re-uses the test_attribute_error.py from prior AttributeError chapter (vars + functions). Covers turning a function stub into class, remove the commented lines in REFACTOR, git commit after each step, uv run pytest-watcher. Review lesson: variables/functions/classes/methods are all attributes. Prepares for exception handling and "everything is an object". Part of the Pumping Python TDD book by Jacob Itegboje.
  :keywords:
    Jacob Itegboje, Pumping Python, AttributeError with classes, python AttributeError class attribute, type object 'AClass' has no attribute, Did you mean attribute_00, AttributeError AClass, SyntaxError return outside function, NameError name 'self' is not defined, TypeError missing 1 required positional argument self, AClass.attribute_00, src.attribute_error.AClass, class in module is attribute, method is attribute of class, test_attribute_error_w_class_attributes, test_attribute_error_w_class_methods, bare attribute access on class and instance, TDD class attributes methods, uv run pytest-watcher, remove the commented lines, red green refactor class, python everything is an object, Pumping Python exceptions AttributeError classes

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

* I open ``test_attribute_error.py``

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

* I add a test for :ref:`class attributes<what is a class attribute?>` to ``test_attribute_error.py``

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

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

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
    :emphasize-lines: 4

    def function_09(): return function_08()


    def AClass(): return function_09()

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: 'function' object
                    has no attribute 'attribute_00'

* I add a :ref:`variable<what is a variable?>` for ``attribute_00`` to the :ref:`function <what is a function?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 1-2, 4-5

    # def AClass(): return function_09()
    def AClass():

        attribute_00 = function_09()
        return function_09()

  the terminal_ still shows the same :ref:`Exception<errors>` because I cannot get to a :ref:`variable<what is a variable?>` inside a :ref:`function<what is a function?>` from outside the :ref:`function<what is a function?>`. The :ref:`variable<what is a variable?>` is only used inside the :ref:`function<what is a function?>` when it runs.

* I change ``AClass`` from a :ref:`function<what is a function?>` to a :ref:`class<what is a class?>`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 2-3

    # def AClass(): return function_09()
    # def AClass():
    class AClass(object):

        attribute_00 = function_09()
        return function_09()

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    E    return function_09()
    E    ^^^^^^^^^^^^^^^^^^^^
    E  SyntaxError: 'return' outside function

  because I cannot use a :ref:`return statement<the return statement>` outside a :ref:`function<what is a function?>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 7
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

* I comment out the :ref:`return statement<the return statement>` from ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

    # def AClass(): return function_09()
    # def AClass():
    class AClass(object):

        attribute_00 = function_09()
        # return function_09()

  - the test passes because ``attribute_00`` is now an :ref:`attribute/property<what is a class attribute?>` of the ``AClass`` :ref:`class<what is a class?>`
  - ``AClass`` is an :ref:`attribute<what is a class attribute?>` of the ``attribute_error.py`` :ref:`module<what is a module?>` in the ``src`` folder_
  - I can use ``attribute_00`` from outside the file_ with ``src.attribute_error.AClass.attribute_00`` or ``src.attribute_error.AClass().attribute_00``

    .. code-block:: shell

      src.attribute_error.AClass.attribute_00
      src.attribute_error.AClass().attribute_00
      src
      └── attribute_error.py
          └── class AClass(object):
              └── attribute_00 = function_09()

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :lineno-start: 22

    def function_09(): return function_08()


    class AClass(object):

        attribute_00 = function_09()

* I add a line for ``src.attribute_error.AClass().attribute_01`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 3

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_01'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_01`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 4

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00

  - the test passes because in this case it does not matter if I use the :ref:`class<what is a class?>` (``AClass``) or an :ref:`instance of the class<how to test if something is an instance>`  (``AClass()``).
  - ``attribute_01`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_01`` or ``src.attribute_error.AClass().attribute_01``

    .. code-block:: shell

      src.attribute_error.AClass.attribute_01
      src.attribute_error.AClass().attribute_01
      src
      └── attribute_error.py
          └── class AClass(object):
              └── attribute_01 = attribute_00

* I add a line for ``src.attribute_error.AClass.attribute_02`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 4

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_02'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_02`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01

  the test passes because ``attribute_02`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_02`` or ``src.attribute_error.AClass().attribute_02``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_02
    src.attribute_error.AClass().attribute_02
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_02 = attribute_01

* I add a line for ``src.attribute_error.AClass().attribute_03`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 5

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_03'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_03`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 6

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02

  the test passes because ``attribute_03`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_03`` or ``src.attribute_error.AClass().attribute_03``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_03
    src.attribute_error.AClass().attribute_03
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_03 = attribute_02

* I add a line for ``src.attribute_error.AClass.attribute_04`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 6

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03
        src.attribute_error.AClass.attribute_04


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_04'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_04`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03

  the test passes because ``attribute_04`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_04`` or ``src.attribute_error.AClass().attribute_04``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_04
    src.attribute_error.AClass().attribute_04
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_04 = attribute_03


* I add a line for ``src.attribute_error.AClass().attribute_05`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 7

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03
        src.attribute_error.AClass.attribute_04
        src.attribute_error.AClass().attribute_05


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_05'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_05`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 8

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04

  the test passes because ``attribute_05`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_05`` or ``src.attribute_error.AClass().attribute_05``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_05
    src.attribute_error.AClass().attribute_05
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_05 = attribute_04

* I add a line for ``src.attribute_error.AClass().attribute_06`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 8

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03
        src.attribute_error.AClass.attribute_04
        src.attribute_error.AClass().attribute_05
        src.attribute_error.AClass().attribute_06


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_06'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_06`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 9

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05

  the test passes because ``attribute_06`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_06`` or ``src.attribute_error.AClass().attribute_06``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_06
    src.attribute_error.AClass().attribute_06
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_06 = attribute_05

* I add a line for ``src.attribute_error.AClass.attribute_07`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 9

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03
        src.attribute_error.AClass.attribute_04
        src.attribute_error.AClass().attribute_05
        src.attribute_error.AClass().attribute_06
        src.attribute_error.AClass.attribute_07


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_07'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_07`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05
        attribute_07 = attribute_06

  the test passes because ``attribute_07`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_07`` or ``src.attribute_error.AClass().attribute_07``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_07
    src.attribute_error.AClass().attribute_07
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_07 = attribute_06

* I add a line for ``src.attribute_error.AClass.attribute_08`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 10

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03
        src.attribute_error.AClass.attribute_04
        src.attribute_error.AClass().attribute_05
        src.attribute_error.AClass().attribute_06
        src.attribute_error.AClass.attribute_07
        src.attribute_error.AClass.attribute_08


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_08'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_08`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 11

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05
        attribute_07 = attribute_06
        attribute_08 = attribute_07

  the test passes because ``attribute_08`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_08`` or ``src.attribute_error.AClass().attribute_08``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_08
    src.attribute_error.AClass().attribute_08
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_08 = attribute_07

* I add a line for ``src.attribute_error.AClass().attribute_09`` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 30
    :emphasize-lines: 11

    def test_attribute_error_w_class_attributes():
        src.attribute_error.AClass.attribute_00
        src.attribute_error.AClass().attribute_01
        src.attribute_error.AClass.attribute_02
        src.attribute_error.AClass().attribute_03
        src.attribute_error.AClass.attribute_04
        src.attribute_error.AClass().attribute_05
        src.attribute_error.AClass().attribute_06
        src.attribute_error.AClass.attribute_07
        src.attribute_error.AClass.attribute_08
        src.attribute_error.AClass().attribute_09


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'attribute_09'.
                    Did you mean: 'attribute_00'?

* I add ``attribute_09`` to the :ref:`class definition<how to make a class>` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 12

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05
        attribute_07 = attribute_06
        attribute_08 = attribute_07
        attribute_09 = attribute_08

  the test passes because ``attribute_09`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass.attribute_09`` or ``src.attribute_error.AClass().attribute_09``

  .. code-block:: shell

    src.attribute_error.AClass.attribute_09
    src.attribute_error.AClass().attribute_09
    src
    └── attribute_error.py
        └── class AClass(object):
            └── attribute_09 = attribute_08

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
* I add a test for :ref:`methods<what is a method?>` to ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-5

        src.attribute_error.AClass().attribute_09


    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass.method_00()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_00'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``AClass`` and point it to ``attribute_09``, in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 14

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05
        attribute_07 = attribute_06
        attribute_08 = attribute_07
        attribute_09 = attribute_08

        method_00 = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

  because ``method_00`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I use the def_ keyword to change it from a :ref:`variable (attribute)<what is a variable?>` to a :ref:`method<what is a method?>`

  .. code-block:: python
    :lineno-start: 36
    :emphasize-lines: 3-4

        attribute_09 = attribute_08

        # method_00 = attribute_09
        def method_00(): return attribute_09

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'attribute_09' is not defined

  because there is nothing inside ``method_00`` named ``attribute_09`` and it cannot get to ``attribute_09`` of ``AClass``, yet.

* I add ``self.`` before the name to reference the :ref:`class attribute<what is a class attribute?>`

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2-3

        # method_00 = attribute_09
        # def method_00(): return attribute_09
        def method_00(): return self.attribute_09

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'self' is not defined

* I add ``self`` to the parentheses of ``method_00``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3-4

        # method_00 = attribute_09
        # def method_00(): return attribute_09
        # def method_00(): return self.attribute_09
        def method_00(self): return self.attribute_09

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: AClass.method_00() missing
               1 required positional argument: 'self'

  because I :ref:`called the method<how to call a function>` with the :ref:`class<what is a class?>` not an :ref:`instance of the class<how to test if something is an instance>`.

* I use an :ref:`instance of the class<how to test if something is an instance>` to :ref:`call the method<how to call a function>` in ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 2-3

    def test_attribute_error_w_class_methods():
        # src.attribute_error.AClass.method_00()
        src.attribute_error.AClass().method_00()


    # Exceptions seen

  - the test passes because ``method_00`` is now an :ref:`attribute/property<what is a class attribute?>` of the ``AClass`` :ref:`class<what is a class?>`
  - ``AClass`` is an :ref:`attribute<what is a class attribute?>` of the ``attribute_error.py`` :ref:`module<what is a module?>` in the ``src`` folder_
  - I can :ref:`call<how to call a function>` ``method_00`` from outside the file_ with ``src.attribute_error.AClass().method_00()``

  .. code-block:: shell

    src.attribute_error.AClass().method_00
    src
    └── attribute_error.py
        └── class AClass(object):
            └── def method_00(self): return self.attribute_09

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05
        attribute_07 = attribute_06
        attribute_08 = attribute_07
        attribute_09 = attribute_08

        def method_00(self): return self.attribute_09

* I remove the commented line from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()


    # Exceptions seen

* You know the "drill", I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_01``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 3

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_01'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 2

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()

  the test passes because ``method_01`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass().method_01()``

  .. code-block:: shell

    src.attribute_error.AClass().method_01
    src
    └── attribute_error.py
        └── class AClass(object):
            └── def method_01(self): return self.method_00()

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_02`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 4

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_02'.
                    Did you mean: 'method_00'?

* I add the :ref:`method<what is a method?>` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 3

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()

  the test passes because ``method_02`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass().method_02()``

  .. code-block:: shell

    src.attribute_error.AClass().method_02
    src
    └── attribute_error.py
        └── class AClass(object):
            └── def method_02(self): return self.method_01()

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_03`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 5

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_03'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_03`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 4

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()

  the test passes because ``method_03`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass().method_03()``

  .. code-block:: shell

    src.attribute_error.AClass().method_03
    src
    └── attribute_error.py
        └── class AClass(object):
            └── def method_03(self): return self.method_02()

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_04`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()
        src.attribute_error.AClass().method_04()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_04'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_04`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()
        def method_04(self): return self.method_03()

  the test passes because ``method_04`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass().method_04()``

  .. code-block:: shell

    src.attribute_error.AClass().method_04
    src
    └── attribute_error.py
        └── class AClass(object):
            └── def method_04(self): return self.method_03()

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_05`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()
        src.attribute_error.AClass().method_04()
        src.attribute_error.AClass().method_05()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_05'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_05`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 6

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()
        def method_04(self): return self.method_03()
        def method_05(self): return self.method_04()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_06`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 8

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()
        src.attribute_error.AClass().method_04()
        src.attribute_error.AClass().method_05()
        src.attribute_error.AClass().method_06()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_06'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_06`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 7

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()
        def method_04(self): return self.method_03()
        def method_05(self): return self.method_04()
        def method_06(self): return self.method_05()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_07`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 9

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()
        src.attribute_error.AClass().method_04()
        src.attribute_error.AClass().method_05()
        src.attribute_error.AClass().method_06()
        src.attribute_error.AClass().method_07()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_07'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_07`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 8

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()
        def method_04(self): return self.method_03()
        def method_05(self): return self.method_04()
        def method_06(self): return self.method_05()
        def method_07(self): return self.method_06()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_08`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()
        src.attribute_error.AClass().method_04()
        src.attribute_error.AClass().method_05()
        src.attribute_error.AClass().method_06()
        src.attribute_error.AClass().method_07()
        src.attribute_error.AClass().method_08()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_08'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_08`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 9

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()
        def method_04(self): return self.method_03()
        def method_05(self): return self.method_04()
        def method_06(self): return self.method_05()
        def method_07(self): return self.method_06()
        def method_08(self): return self.method_07()

  the test passes.

* I add a :ref:`call<how to call a function>` to ``src.attribute_error.AClass().method_09`` from ``test_attribute_error.py``

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 11

    def test_attribute_error_w_class_methods():
        src.attribute_error.AClass().method_00()
        src.attribute_error.AClass().method_01()
        src.attribute_error.AClass().method_02()
        src.attribute_error.AClass().method_03()
        src.attribute_error.AClass().method_04()
        src.attribute_error.AClass().method_05()
        src.attribute_error.AClass().method_06()
        src.attribute_error.AClass().method_07()
        src.attribute_error.AClass().method_08()
        src.attribute_error.AClass().method_09()


    # Exceptions seen
    # AssertionError
    # ModuleNotFoundError
    # AttributeError
    # NameError
    # TypeError
    # SyntaxError

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: type object 'AClass'
                    has no attribute 'method_09'.
                    Did you mean: 'method_00'?

* I add a :ref:`method definition<how to make a function>` for ``method_09`` to the :ref:`definition<how to make a class>` of ``AClass`` in ``attribute_error.py``

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 23

    class AClass(object):

        attribute_00 = function_09()
        attribute_01 = attribute_00
        attribute_02 = attribute_01
        attribute_03 = attribute_02
        attribute_04 = attribute_03
        attribute_05 = attribute_04
        attribute_06 = attribute_05
        attribute_07 = attribute_06
        attribute_08 = attribute_07
        attribute_09 = attribute_08

        def method_00(self): return self.attribute_09
        def method_01(self): return self.method_00()
        def method_02(self): return self.method_01()
        def method_03(self): return self.method_02()
        def method_04(self): return self.method_03()
        def method_05(self): return self.method_04()
        def method_06(self): return self.method_05()
        def method_07(self): return self.method_06()
        def method_08(self): return self.method_07()
        def method_09(self): return self.method_08()

  the test passes because ``method_09`` is now an :ref:`attribute<what is a class attribute?>` of ``AClass`` in ``attribute_error.py`` in the ``src`` folder_, and I can use it from outside the file_ with ``src.attribute_error.AClass().method_09()``

  .. code-block:: shell

    src.attribute_error.AClass().method_09
    src
    └── attribute_error.py
        └── class AClass(object):
            └── def method_09(self): return self.method_08()

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_attribute_error_w_class_methods'

:ref:`A function in a class is an attribute of the class and is called a method<test_attribute_error_w_class_methods>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``attribute_error.py`` and ``test_attribute_error.py``
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

All the tests I have run for :ref:`AttributeError<what causes AttributeError?>` show that

* :ref:`A variable in a class is an attribute of the class<test_attribute_error_w_class_attributes>`
* :ref:`A function in a class is an attribute of the class<test_attribute_error_w_class_methods>`
* :ref:`A class in a module is an attribute of the module<test_attribute_error_w_class_attributes>`
* :ref:`A function in a module is an attribute of the module<test_attribute_error_w_functions>`
* :ref:`A variable in a module is an attribute of the module<test_attribute_error_w_variables>`

I still have the problem that the tests all show the correct way to use :ref:`attributes<what is a class attribute?>` I made in ``attribute_error.py``. If someone reads the file_ or runs it, there is no way for them to know how the code relates to :ref:`AttributeError<what causes AttributeError?>` unless they go through the process with me, there has to be a better way.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<AttributeError with classes: tests and solutions>`

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
* :ref:`that everything in Python is an object<everything is an object>`

:ref:`Would you like to test TypeError with classes?<TypeError with classes>`

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