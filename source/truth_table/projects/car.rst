.. meta::
  :description: Build a car ignition controller with Python TDD (Red-Green-Refactor): translate a four-input truth table (start button, key close, brake pressed, gear in park) into ``src.car.ignition`` that returns True only when every condition is met. Beginners use uv, unittest, and pytest-watcher; hit NameError, AttributeError, TypeError (unexpected keywords / missing args), SyntaxError (non-default after default), and AssertionError; learn default parameters, keyword calls, nested if / Logical Negation (NOT) / Logical Conjunction (AND), and assertTrue/assertFalse until only start pressed AND key close AND brake pressed AND in park starts the car.
  :keywords: Jacob Itegboje, Python car ignition project, TDD Red Green Refactor, truth table to code, unittest assertTrue assertFalse, uv package manager, pytest-watcher, start button, key close, brake pressed, in park, default parameters, keyword arguments, SyntaxError parameter without a default, TypeError unexpected keyword argument, NameError src not defined, AttributeError, Logical Negation NOT, Logical Conjunction AND, if statements, pumping python

.. include:: ../../links.rst

.. _car:

#################################################################################
Car
#################################################################################

I want to make a **Car** that comes :green:`ON` or stays :red:`OFF` when I push the start button.

----

*********************************************************************************
preview
*********************************************************************************

These are the tests I have at the end of the chapter

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :linenos:
  :caption: car/tests/test_car.py
  :lines: 1-23

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 25
  :caption: car/tests/test_car.py
  :lines: 25-41

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 43
  :caption: car/tests/test_car.py
  :lines: 43-59

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 61
  :caption: car/tests/test_car.py
  :lines: 61-77

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 79
  :caption: car/tests/test_car.py
  :lines: 79-95

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 97
  :caption: car/tests/test_car.py
  :lines: 97-113

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 115
  :caption: car/tests/test_car.py
  :lines: 115-131

.. literalinclude:: ../../code/car/test_car.py
  :language: python
  :lineno-start: 133
  :caption: car/tests/test_car.py
  :lines: 133-

----

*********************************************************************************
start the project
*********************************************************************************

* I open a terminal_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I open ``makePythonTdd.sh``
      * I change the name of the project to ``car`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/car/make_tdd/makePythonTddCar.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 5-6, 13, 21

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``car`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``
      * I change the name of the project to ``car`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/car/make_tdd/makePythonTddCar.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 4-5, 12, 20

      * I run ``makePythonTdd.ps1`` in the terminal_ to make the ``car`` project

        .. code-block:: python
          :emphasize-lines: 1

          .\makePythonTdd.ps1

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python
    :emphasize-lines: 10

    ======================== FAILURES =========================
    _________________ TestCar.test_failure ____________________

    self = <tests.test_car.TestCar testMethod=test_failure>

        def test_failure(self):
    >       self.assertFalse(True)
    E       AssertionError: True is not false

    tests/test_car.py:7: AssertionError
    ================ short test summary info ==================
    FAILED tests/test_car.py::TestCar::test_failure - AssertionError: True is not false
    ==================== 1 failed in X.YZs ====================

* I hold :kbd:`ctrl` (Windows_/Linux_) or :kbd:`option/command` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_car.py:7`` to open it
* I change :green:`True` to :red:`False` in ``test_car.py``

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 4-5

    class TestCar(unittest.TestCase):

        def test_failure(self):
            # self.assertFalse(True)
            self.assertFalse(False)


    # Exceptions seen

  the test passes.

* I open a new terminal_ then `change directory`_ to ``car``

  .. code-block:: python
    :emphasize-lines: 1

    cd car

* I add the new files_ and folder_ to git_ for tracking

  .. code-block:: python
    :emphasize-lines: 1

    git add .

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'setup project'

----

I want the car to start only when the start button is :green:`pressed`. I get this :ref:`truth table`

==================  =============
start button        output
==================  =============
:green:`pressed`    :green:`True`
:red:`NOT pressed`  :red:`False`
==================  =============

where :green:`True` is the **Car** comes :green:`ON` and :red:`False` is it stays :red:`OFF`.

----

*********************************************************************************
test_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I change :ref:`test_failure` to :ref:`test_start_pressed`, then add an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed`

  ==================  =============
  start button        output
  ==================  =============
  :green:`pressed`    :green:`True`
  ==================  =============

  .. code-block:: python
    :lineno-start: 4
    :emphasize-lines: 3-7

    class TestCar(unittest.TestCase):

        def test_start_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=True,
            )
            self.assertTrue(reality)


    # Exceptions seen
    # AssertionError


  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because I do not have a definition for ``src`` in this ``test_car.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

* I add an `import statement`_ at the top of the file_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.car
    import unittest


    class TestCar(unittest.TestCase):

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.car' has no attribute 'ignition'

  because ``car.py`` in the ``src`` folder_ does not have anything named ``ignition`` in it.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 4
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError

* I open ``car.py`` from the ``src`` folder_

* I delete all the text in the file_ then add a :ref:`function<what is a function?>` named ``ignition`` to ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def ignition():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: ignition() got
               an unexpected keyword argument 'start_is_pressed'

  because the test :ref:`called<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``start_is_pressed``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_car.py``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 5
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError

* I add ``start_is_pressed`` to the :ref:`function signature<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def ignition(start_is_pressed):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  because the ``ignition`` :ref:`function<what is a function?>` returns :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects :green:`True`.

* I change the :ref:`return statement<the return statement>` to give the test what it wants

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def ignition(start_is_pressed):
        return True

  the test passes.


* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_start_pressed'

The ``ignition`` :ref:`function<what is a function?>` always returns :green:`True`.

.. code-block:: python

  ignition(start_is_pressed=True ) -> True

----

*********************************************************************************
test_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed`

  ==================  =============
  start button        output
  ==================  =============
  :red:`NOT pressed`  :red:`False`
  ==================  =============

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-7

            self.assertTrue(reality)

        def test_start_not_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=False,
            )
            self.assertFalse(reality)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the :ref:`function<what is a function?>` always returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`the return statement`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def ignition(start_is_pressed):
        return start_is_pressed

  the test passes.

  .. code-block:: python

    ignition(start_is_pressed=False) -> False
    ignition(start_is_pressed=True ) -> True

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1

    git commit -am 'add test_start_not_pressed'

The ``ignition`` :ref:`function<what is a function?>` always returns the value of ``start_is_pressed``. Is this the :ref:`Identity Function<test_logical_identity>`?

I want the car to start only when the start button is :green:`pressed` AND the key is :green:`close` to the ignition. The inputs to the ignition will then be

* was the start button pressed?
* is the key close to the ignition?

Which gives me this :ref:`truth table`

================  ==================  =============
key               start button        output
================  ==================  =============
:green:`close`    :green:`pressed`    :green:`True`
:red:`NOT close`  :green:`pressed`    :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`False`
================  ==================  =============

----

*********************************************************************************
test_key_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add ``key_is_close`` with a value to the :ref:`call<how to call a function with input>` to the ``ignition`` :ref:`function<what is a function?>` from :ref:`test_start_pressed` for if the the start button is :green:`pressed` AND the key is :green:`close` to the ignition

  ================  ==================  =============
  key               start button        output
  ================  ==================  =============
  :green:`close`    :green:`pressed`    :green:`True`
  ================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4

        def test_start_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=True,
                key_is_close=True,
            )
            self.assertTrue(reality)

        def test_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: ignition() got
               an unexpected keyword argument 'key_is_close

  because the test :ref:`called<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``key_is_close``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``key_is_close`` to the :ref:`function definition<how to make a function that takes input>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def ignition(start_is_pressed, key_is_close):
        return start_is_pressed

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: ignition() missing
               1 required positional argument: 'key_is_close'

  because the :ref:`assertion<what is an assertion?>` in :ref:`test_start_not_pressed` :ref:`calls<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with one argument (``start_is_pressed``) and I just changed the :ref:`function<what is a function?>` to make it take two required arguments (``key_is_close`` and ``start_is_pressed``). I have to make ``key_is_close`` a :ref:`choice<test_optional_arguments>`.

* I add a :ref:`default value<test_optional_arguments>` for ``key_is_close`` to make it a :ref:`choice<test_optional_arguments>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def ignition(start_is_pressed, key_is_close=False):
        return start_is_pressed

  the test passes.

  .. code-block:: python

    ignition(key_is_close=True , start_is_pressed=True ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of :ref:`test_start_pressed` to :ref:`test_key_close_start_pressed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_key_close_start_pressed(self):
            reality = src.car.ignition(
                key_is_close=True,
                start_is_pressed=True,
            )
            self.assertTrue(reality)

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_key_close_start_pressed'

----

*********************************************************************************
test_key_not_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition, in ``test_car.py``

  ================  ==================  =============
  key               start button        output
  ================  ==================  =============
  :red:`NOT close`  :green:`pressed`    :red:`False`
  ================  ==================  =============

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 3-7

          self.assertTrue(reality)

      def test_key_not_close_start_pressed(self):
          reality = src.car.ignition(
              start_is_pressed=True,
          )
          self.assertFalse(reality)

      def test_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``ignition`` :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`.

  I do not need to add a value for the ``key_is_close`` parameter since

  .. code-block:: python

    src.car.ignition(
        start_is_pressed=True
    )

  is the same as

  .. code-block:: python

    src.car.ignition(
        start_is_pressed=True,
        key_is_close=False,
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.


----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to ``car.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 2-3

  def ignition(start_is_pressed, key_is_close=False):
      if key_is_close == False:
          return False
      return start_is_pressed

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the ``ignition`` :ref:`function<what is a function?>` to check if the start button is :green:`pressed` before it checks if the key is :green:`close` to the ignition since there is no need to check for the key if the button is :red:`NOT pressed`. I change the :ref:`if statement<if statements>`

  .. code-block:: python
    :linenos:

    def ignition(start_is_pressed, key_is_close=False):
        # if key_is_close == False:
        #     return False
        # return start_is_pressed
        if start_is_pressed:
            return key_is_close

  the test is still green.

* I remove the commented lines from the ``ignition`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def ignition(start_is_pressed, key_is_close=False):
        if start_is_pressed:
            return key_is_close

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_key_not_close_start_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the start button is :green:`pressed`. If the start button is :green:`pressed` it returns the value of ``key_is_close`` (:green:`True` if it is :green:`close`, :red:`False` if it is :red:`NOT close`.

.. code-block:: python

  ignition(key_is_close=False, start_is_pressed=True ) -> False
  ignition(key_is_close=True , start_is_pressed=True ) -> True

----

*********************************************************************************
test_key_close_start_not_pressed
*********************************************************************************

* I go back to the terminal_ where the tests are running

* I add a value for the ``key_is_close`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_start_not_pressed` for if the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition, in ``test_car.py``

  ================  ==================  =============
  key               start button        output
  ================  ==================  =============
  :green:`close`    :red:`NOT pressed`  :red:`False`
  ================  ==================  =============

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 6

            self.assertFalse(reality)

        def test_start_not_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=False,
                key_is_close=True,
            )
            self.assertFalse(reality)

  the test is still green.

* I change the name from :ref:`test_start_not_pressed` to :ref:`test_key_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3

            self.assertFalse(reality)

        def test_key_close_start_not_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=False,
                key_is_close=True,
            )
            self.assertFalse(reality)


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_key_close_start_not_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>` it checks if the start button is :green:`pressed`. If the start button is :green:`pressed` it returns the value of ``key_is_close`` (:green:`True` if it is :green:`close`, :red:`False` if it is :red:`NOT close`.

.. code-block:: python

  ignition(key_is_close=True , start_is_pressed=False) -> False
  ignition(key_is_close=False, start_is_pressed=True ) -> False
  ignition(key_is_close=True , start_is_pressed=True ) -> True

----

*********************************************************************************
test_key_not_close_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition, in ``test_car.py``

  ================  ==================  =============
  key               start button        output
  ================  ==================  =============
  :red:`NOT close`  :red:`NOT pressed`  :red:`False`
  ================  ==================  =============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 3-7

            self.assertFalse(reality)

        def test_key_not_close_start_not_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=False,
            )
            self.assertTrue(reality)


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None is not true

  because :ref:`all functions return None by default<test_making_a_function_w_return_none>`.

  I do not give a value for the ``key_is_close`` parameter since

  .. code-block:: python

    src.car.ignition(
        start_is_pressed=False,
    )

  is the same as

  .. code-block:: python

    src.car.ignition(
        start_is_pressed=False,
        key_is_close=False,
    )

  because :ref:`a function uses the default value for a parameter when it is called without the parameter<test_optional_arguments>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`return statement<the return statement>` to the ``ignition`` :ref:`function<what is a function?>` to make it clearer, in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    def ignition(start_is_pressed, key_is_close=False):
        if start_is_pressed:
            return key_is_close
        return None

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`

* I change :ref:`None<what is None?>` to :red:`False` in the :ref:`return statement<the return statement>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4

    def ignition(start_is_pressed, key_is_close=False):
        if start_is_pressed:
            return key_is_close
        return False

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` to match ``reality`` in :ref:`test_key_not_close_start_not_pressed` in ``test_car.py``

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 5

        def test_key_not_close_start_not_pressed(self):
            reality = src.car.ignition(
                start_is_pressed=False,
            )
            self.assertFalse(reality)


    # Exceptions seen

  the test passes.

  .. code-block:: python

    ignition(key_is_close=False, start_is_pressed=False) -> False
    ignition(key_is_close=True , start_is_pressed=False) -> False
    ignition(key_is_close=False, start_is_pressed=True ) -> False
    ignition(key_is_close=True , start_is_pressed=True ) -> True

* I add a git_ commit message in the other terminal_

  .. code-block::
    :emphasize-lines: 1-2

    git commit -am \
    'add test_key_not_close_start_not_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`. It checks if the start button is :green:`pressed`.

* If the start button is :red:`NOT pressed` it returns :red:`False`

  .. code-block:: shell

    ignition(key_is_close=False, start_is_pressed=False) -> False
    └── def ignition(start_is_pressed, key_is_close=False):
        ├── if start_is_pressed:
        │       return key_is_close
        └── return False

  .. code-block:: shell

    ignition(key_is_close=True , start_is_pressed=False) -> False
    └── def ignition(start_is_pressed, key_is_close=False):
        ├── if start_is_pressed:
        │       return key_is_close
        └── return False

* If the start button is :green:`pressed` it returns the value of ``key_is_close``

  - if the key is :red:`NOT close` to the ignition it returns :red:`False`

    .. code-block:: shell

      ignition(key_is_close=False, start_is_pressed=True ) -> False
      └── def ignition(start_is_pressed, key_is_close=False):
          └── if start_is_pressed:
              └── return key_is_close
                  return False
              return False

  - if the key is :green:`close` to the ignition it returns :green:`True`

  .. code-block:: shell

      ignition(key_is_close=True , start_is_pressed=True ) -> True
      └── def ignition(start_is_pressed, key_is_close=False):
          └── if start_is_pressed:
              └── return key_is_close
                  return True
              return False

----

*********************************************************************************
remove reality variable
*********************************************************************************

I can :ref:`call<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` directly in all the :ref:`assertions<what is an assertion?>`.

* I :ref:`call<how to call a function with input>` ``src.car.ignition`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_key_not_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 27
    :emphasize-lines: 2-10

        def test_key_not_close_start_not_pressed(self):
            # reality = src.car.ignition(
            #     start_is_pressed=False,
            # )
            # self.assertFalse(reality)
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                )
            )


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_key_not_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 27

        def test_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                )
            )


    # Exceptions seen

* I :ref:`call<how to call a function with input>` ``src.car.ignition`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_key_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 20
    :emphasize-lines: 2-12

        def test_key_close_start_not_pressed(self):
            # reality = src.car.ignition(
            #     key_is_close=True,
            #     start_is_pressed=False,
            # )
            # self.assertFalse(reality)
            self.assertFalse(
                  src.car.ignition(
                    key_is_close=True,
                    start_is_pressed=False,
                )
            )

        def test_key_not_close_start_not_pressed(self):

  still green.

* I remove the commented lines from :ref:`test_key_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 20

        def test_key_close_start_not_pressed(self):
            self.assertFalse(
                  src.car.ignition(
                    key_is_close=True,
                    start_is_pressed=False,
                )
            )

        def test_key_not_close_start_not_pressed(self):

* I :ref:`call<how to call a function with input>` ``src.car.ignition`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_key_not_close_start_pressed`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-10

        def test_key_not_close_start_pressed(self):
            # reality = src.car.ignition(
            #     start_is_pressed=True
            # )
            # self.assertFalse(reality)
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True
                )
            )

        def test_key_close_start_not_pressed(self):

  green.

* I remove the commented lines from :ref:`test_key_not_close_start_pressed`

  .. code-block:: python
    :lineno-start: 14

        def test_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True
                )
            )

        def test_key_close_start_not_pressed(self):

* I :ref:`call<how to call a function with input>` ``src.car.ignition`` directly in the :ref:`assertion<what is an assertion?>` of :ref:`test_key_close_start_pressed`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 2-12

        def test_key_close_start_pressed(self):
            # reality = src.car.ignition(
            #     key_is_close=True,
            #     start_is_pressed=True,
            # )
            # self.assertTrue(reality)
            self.assertTrue(
                src.car.ignition(
                    key_is_close=True,
                    start_is_pressed=True,
                )
            )

        def test_key_not_close_start_pressed(self):

  the test is still green.

* I remove the commented lines from :ref:`test_key_close_start_pressed`

  .. code-block:: python
    :lineno-start: 7

        def test_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    key_is_close=True,
                    start_is_pressed=True,
                )
            )

        def test_key_not_close_start_pressed(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am 'remove reality variable'

----

So far, the :ref:`truth table` for the ignition is

================  ==================  =============
key               start button        output
================  ==================  =============
:green:`close`    :green:`pressed`    :green:`True`
:red:`NOT close`  :green:`pressed`    :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`False`
================  ==================  =============

I want the car to start only when the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake pedal is :green:`pressed`. The inputs to the ignition will then be

* was the start button pressed?
* is the key close to the ignition?
* is the brake being pressed?

----

*********************************************************************************
test_brake_pressed_key_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for ``brake_is_pressed`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_key_close_start_pressed`, for if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :green:`close`    :green:`pressed`    :green:`pressed`    :green:`True`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 6

        def test_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

        def test_key_not_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: ignition() got
               an unexpected keyword argument 'brake_is_pressed'.
               Did you mean 'start_is_pressed'?

  because the test :ref:`called<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``brake_is_pressed``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``brake_is_pressed`` to the :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-4

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed,
        ):
        if start_is_pressed:
            return key_is_close
        return False

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add SyntaxError_ to the list of :ref:`Exceptions<errors>` seen, in ``test_car.py``

  .. code-block:: python
    :lineno-start: 39
    :emphasize-lines: 6
    :emphasize-text: SyntaxError

    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

* I add a :ref:`default value<test_optional_arguments>` for the ``brake_is_pressed`` parameter, in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed=False,
        ):
        if not key_is_close:
            return False
        return start_is_pressed

  the test passes.

  .. code-block:: python

    ignition(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=True
    ) -> True

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_key_close_start_pressed` to :ref:`test_brake_pressed_key_close_start_pressed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_brake_pressed_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am
    'add test_brake_pressed_key_close_start_pressed'

----

*********************************************************************************
test_brake_not_pressed_key_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a new test with an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-17

        def test_brake_pressed_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

        def test_brake_not_pressed_key_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                )
            )

        def test_key_not_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

  because the ``ignition`` :ref:`function<what is a function?>` returned :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`. I do not need to give a value for the ``brake_is_pressed`` parameter since it is the same as the :ref:`default value<test_optional_arguments>`, I do it to make things clearer.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an :ref:`if statement<if statements>` to the ``ignition`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed=False,
        ):
        if brake_is_pressed == False:
            return False
        if start_is_pressed:
            return key_is_close
        return False

  the test passes.

* I write a simpler version of the new :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

        # if brake_is_pressed == False:
        if not brake_is_pressed:
            return False

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``.

* I want the ``ignition`` :ref:`function<what is a function?>` to only check if the brake is :green:`pressed` if the start button is :green:`pressed` AND the key is :green:`close` to the ignition. I change the :ref:`if statements`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3, 5-7

        # if brake_is_pressed == False:
        # if not brake_is_pressed:
        #     return False
        if start_is_pressed:
            # return key_is_close
            if key_is_close:
                return brake_is_pressed
        return False

    the test is still green.

* I remove the commented lines from the ``ignition`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed=False,
        ):
        if start_is_pressed:
            if key_is_close:
                return brake_is_pressed
        return False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_brake_not_pressed_key_close_start_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`. It checks if the start button is :green:`pressed`.

* If the start button is :red:`NOT pressed` it returns :red:`False`
* If the start button is :green:`pressed` it checks if the key is :green:`close` to the ignition

  - if the key is :red:`NOT close` to the ignition it leaves the :ref:`if statements<if statements>` then returns :red:`False`
  - if the key is :green:`close` to the ignition it returns the value of ``brake_is_pressed``

    * if the brake is :red:`NOT pressed` it returns :red:`False`
    * if the brake is :green:`pressed` it returns :green:`True`

.. code-block:: python

  ignition(
      start_is_pressed=True, key_is_close=True,
      brake_is_pressed=False
  ) -> False
  ignition(
      start_is_pressed=True, key_is_close=True,
      brake_is_pressed=True
  ) -> True

----

*********************************************************************************
test_brake_pressed_key_not_close_start_pressed
*********************************************************************************

* I add values for the ``key_is_close`` and ``brake_is_pressed`` parameters to the :ref:`assertion<what is an assertion?>` in :ref:`test_key_not_close_start_pressed` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition AND the brake is being :green:`pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :red:`NOT close`  :green:`pressed`    :green:`pressed`    :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 5-6

        def test_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )

        def test_key_close_start_not_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=True
    ) -> False
    ignition(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=False
    ) -> False
    ignition(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=True
    ) -> True

* I change the name of the test from :ref:`test_key_not_close_start_pressed` to :ref:`test_brake_pressed_key_not_close_start_pressed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 10

        def test_brake_not_pressed_key_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                )
            )

        def test_brake_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )

        def test_key_close_start_not_pressed(self):

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am \
    'add test_brake_pressed_key_not_close_start_pressed'

----

*********************************************************************************
test_brake_not_pressed_key_not_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :red:`NOT pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-17

        def test_brake_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )

        def test_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                )
            )

        def test_key_close_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` to match the result of the :ref:`call<how to call a function with input>` to the ``ignition`` :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 2

        def test_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                )
            )

        def test_key_close_start_not_pressed(self):

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_brake_not_pressed_key_not_close_start_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`. It checks if the start button is :green:`pressed`.

* If the start button is :red:`NOT pressed` it returns :red:`False`
* If the start button is :green:`pressed` it checks if the key is :green:`close` to the ignition

  - if the key is :red:`NOT close` to the ignition it leaves the :ref:`if statements<if statements>` then returns :red:`False`

    .. code-block:: shell

      ignition(
          start_is_pressed=True, key_is_close=False,
          brake_is_pressed=False
      ) -> False
      └── def ignition(
                  start_is_pressed, key_is_close=False,
                  brake_is_pressed=False,
              ):
              └── if start_is_pressed:
              ┌───┴── if key_is_close:
              │           return brake_is_pressed
              └── return False

    .. code-block:: shell

      ignition(
          start_is_pressed=True, key_is_close=False,
          brake_is_pressed=True
      ) -> False
      └── def ignition(
                  start_is_pressed, key_is_close=False,
                  brake_is_pressed=False,
              ):
              └── if start_is_pressed:
              ┌───┴── if key_is_close:
              │           return brake_is_pressed
              └── return False

  - if the key is :green:`close` to the ignition it returns the value of ``brake_is_pressed``

    * if the brake is :red:`NOT pressed` it returns :red:`False`

      .. code-block:: shell

        ignition(
            start_is_pressed=True, key_is_close=True,
            brake_is_pressed=False
        ) -> False
        └── def ignition(
                    start_is_pressed, key_is_close=False,
                    brake_is_pressed=False,
                ):
                └── if start_is_pressed:
                    └── if key_is_close:
                        └── return brake_is_pressed
                            return False
                    return False

    * if the brake is :green:`pressed` it returns :green:`True`

      .. code-block:: shell

        ignition(
            start_is_pressed=True, key_is_close=True,
            brake_is_pressed=True
        ) -> True
        └── def ignition(
                    start_is_pressed, key_is_close=False,
                    brake_is_pressed=False,
                ):
                └── if start_is_pressed:
                    └── if key_is_close:
                        └── return brake_is_pressed
                            return True
                    return False

----

*********************************************************************************
test_brake_pressed_key_close_start_not_pressed
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add a value for the ``brake_is_pressed`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_key_close_start_not_pressed` for the case where the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :green:`close`    :green:`pressed`    :red:`NOT pressed`  :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 6

        def test_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

        def test_key_not_close_start_not_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True
    ) -> False

* I change the name from :ref:`test_key_close_start_not_pressed` to :ref:`test_brake_pressed_key_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10

        def test_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                )
            )

        def test_brake_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_brake_pressed_key_close_start_not_pressed'

----

*********************************************************************************
test_brake_not_pressed_key_close_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>`, for if the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10-17

        def test_brake_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

        def test_brake_not_pressed_key_close_start_not_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                )
            )

        def test_key_not_close_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` to match reality

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2

          def test_brake_not_pressed_key_close_start_not_pressed(self):
              self.assertFalse(
                  src.car.ignition(
                      start_is_pressed=False,
                      key_is_close=True,
                      brake_is_pressed=False,
                  )
              )

          def test_key_not_close_start_not_pressed(self):

  the test passes.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False
    ) -> False
    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True
    ) -> False

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_brake_not_pressed_key_close_start_not_pressed'

----

*********************************************************************************
test_brake_pressed_key_not_close_start_not_pressed
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add values for the ``key_is_close`` and ``brake_is_pressed`` parameters to :ref:`test_key_not_close_start_not_pressed` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is being :green:`pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 5-6

        def test_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )


    # Exceptions seen

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True
    ) -> False
    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False
    ) -> False
    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True
    ) -> False

* I change the name from :ref:`test_key_not_close_start_not_pressed` to :ref:`test_brake_pressed_key_not_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10

        def test_brake_not_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                )
            )

        def test_brake_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_brake_pressed_key_not_close_start_not_pressed'

----

*********************************************************************************
test_brake_not_pressed_key_not_close_start_not_pressed
*********************************************************************************

* I go back to the terminal_ where the tests are running
* I add a test with an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :red:`NOT pressed`

  ================  ==================  ==================  =============
  key               brake               start button        output
  ================  ==================  ==================  =============
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
  ================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10-17

        def test_brake_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )

        def test_brake_not_pressed_key_not_close_start_not_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` to match the result of the :ref:`call<how to call a function with input>` to ``src.car.ignition`` in :ref:`test_brake_not_pressed_key_not_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 2

        def test_brake_not_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                )
            )


    # Exceptions seen

  the test passes.

* I add a git_ commit message in the other terminal_

  .. code-block:: python

    git commit -am \
    'add test_brake_not_pressed_key_not_close_start_not_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`. It checks if the start button is :green:`pressed`.

* If the start button is :red:`NOT pressed` it returns :red:`False`

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False,
            ):
            ├── if start_is_pressed:
            │       if key_is_close:
            │           return brake_is_pressed
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False,
            ):
            ├── if start_is_pressed:
            │       if key_is_close:
            │           return brake_is_pressed
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False,
            ):
            ├── if start_is_pressed:
            │       if key_is_close:
            │           return brake_is_pressed
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False,
            ):
            ├── if start_is_pressed:
            │       if key_is_close:
            │           return brake_is_pressed
            └── return False

* If the start button is :green:`pressed` it checks if the key is :green:`close` to the ignition

  - if the key is :red:`NOT close` to the ignition it leaves the :ref:`if statements<if statements>` then returns :red:`False`

    .. code-block:: shell

      ignition(
          start_is_pressed=True, key_is_close=False,
          brake_is_pressed=False
      ) -> False
      └── def ignition(
                  start_is_pressed, key_is_close=False,
                  brake_is_pressed=False,
              ):
              └── if start_is_pressed:
              ┌───┴── if key_is_close:
              │           return brake_is_pressed
              └── return False

    .. code-block:: shell

      ignition(
          start_is_pressed=True, key_is_close=False,
          brake_is_pressed=True
      ) -> False
      └── def ignition(
                  start_is_pressed, key_is_close=False,
                  brake_is_pressed=False,
              ):
              └── if start_is_pressed:
              ┌───┴── if key_is_close:
              │           return brake_is_pressed
              └── return False

  - if the key is :green:`close` to the ignition it returns the value of ``brake_is_pressed``

    * if the brake is :red:`NOT pressed` it returns :red:`False`

      .. code-block:: shell

        ignition(
            start_is_pressed=True, key_is_close=True,
            brake_is_pressed=False
        ) -> False
        └── def ignition(
                    start_is_pressed, key_is_close=False,
                    brake_is_pressed=False,
                ):
                └── if start_is_pressed:
                    └── if key_is_close:
                        └── return brake_is_pressed
                            return False
                    return False

    * if the brake is :green:`pressed` it returns :green:`True`

      .. code-block:: shell

        ignition(
            start_is_pressed=True, key_is_close=True,
            brake_is_pressed=True
        ) -> True
        └── def ignition(
                    start_is_pressed, key_is_close=False,
                    brake_is_pressed=False,
                ):
                └── if start_is_pressed:
                    └── if key_is_close:
                        └── return brake_is_pressed
                            return True
                    return False

The :ref:`truth table` for the **Car Ignition** is

================  ==================  ==================  =============
key               brake               start button        output
================  ==================  ==================  =============
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`False`
:red:`NOT close`  :green:`pressed`    :green:`pressed`    :red:`False`
:green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`False`
:green:`close`    :green:`pressed`    :green:`pressed`    :green:`True`
================  ==================  ==================  =============

================  ==================  ==================  =============
key               brake               start button        output
================  ==================  ==================  =============
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
:red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
:green:`close`    :green:`pressed`    :red:`NOT pressed`  :red:`False`
================  ==================  ==================  =============

I want to make sure the car is in park before it can start, so it does not immediately move when it is turned on (that would be a problem). The inputs will then be

* was the start button pressed?
* is the key close to the ignition?
* is the brake being pressed?
* is the gear in park?

----

*********************************************************************************
test_park_w_brake_not_pressed_key_not_close_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for ``in_park`` to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_not_pressed_key_not_close_start_not_pressed` for the case where the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is being :red:`NOT pressed` AND the car gear is :green:`in park`, to :ref:`test_brake_not_pressed_key_not_close_start_not_pressed`

  ================  ==================  ==================  ==================  ============
  key               brake               start               gear                output
  ================  ==================  ==================  ==================  ============
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ================  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 7

        def test_brake_not_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )


    # Exceptions seen

  the terminal shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: ignition() got
               an unexpected keyword argument 'in_park'

  because the test :ref:`called<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``in_park``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``in_park`` to the :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed=False, in_park,
        ):
            if start_is_pressed:
                if key_is_close:
                    return brake_is_pressed
            return False

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: parameter without a default follows
                 parameter with a default

  because :ref:`parameters without default values must come before parameters with default values<test_args_and_kwargs>`.

* I add a :ref:`default value<test_optional_arguments>` for the ``in_park`` parameter in the :ref:`function signature<what is a function?>` to make it a choice

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed=False, in_park=False,
        ):

  the test passes.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is being :red:`NOT pressed` AND the car gear is :red:`NOT in park`

  ================  ==================  ==================  ==================  ============
  key               brake               start               gear                output
  ================  ==================  ==================  ==================  ============
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ================  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 10-17

        def test_brake_not_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=False,
                )
            )


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

  because the ``ignition`` :ref:`function<what is a function?>` returns :red:`False` and the :ref:`assertion<what is an assertion?>` expects :green:`True`

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` to match the result of the :ref:`call<how to call a function with input>`

  .. code-block:: python
    :lineno-start: 70
    :emphasize-lines: 10

        def test_brake_not_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=False,
                )
            )


    # Exceptions seen
    # AssertionError
    # NameError
    # AttributeError
    # TypeError
    # SyntaxError

  the test passes.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) -> False
    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=False
    ) -> False

* I change the name of the test to from:ref:`test_brake_not_pressed_key_not_close_start_not_pressed` to :ref:`test_park_w_brake_not_pressed_key_not_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10

        def test_brake_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )

        def test_park_w_brake_not_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_not_pressed_key_not_close_start_not_pressed'

----

*********************************************************************************
test_park_w_brake_pressed_key_not_close_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_pressed_key_not_close_start_not_pressed` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :green:`in park`

  ================  ================  ==================  ==================  ============
  key               brake             start               gear                output
  ================  ================  ==================  ==================  ============
  :red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ================  ================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 7

        def test_brake_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

        def test_park_w_brake_not_pressed_key_not_close_start_not_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True, in_park=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :red:`NOT in park`

  ================  ================  ==================  ==================  ============
  key               brake             start               gear                output
  ================  ================  ==================  ==================  ============
  :red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ================  ================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 61
    :emphasize-lines: 10-17

        def test_brake_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=False,
                )
            )

        def test_brake_not_pressed_key_not_close_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_brake_pressed_key_not_close_start_not_pressed`

.. code-block:: python
  :lineno-start: 61
  :emphasize-lines: 10

      def test_brake_pressed_key_not_close_start_not_pressed(self):
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=False,
                  key_is_close=False,
                  brake_is_pressed=True,
                  in_park=True,
              )
          )
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=False,
                  key_is_close=False,
                  brake_is_pressed=True,
                  in_park=False,
              )
          )

      def test_brake_not_pressed_key_not_close_start_not_pressed(self):

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=False, key_is_close=False,
      brake_is_pressed=True, in_park=True
  ) -> False
  ignition(
      start_is_pressed=False, key_is_close=False,
      brake_is_pressed=True, in_park=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_brake_pressed_key_not_close_start_not_pressed` to :ref:`test_park_w_brake_pressed_key_not_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10

        def test_brake_not_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                )
            )

        def test_park_w_brake_pressed_key_not_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_pressed_key_not_close_start_not_pressed'

----

*********************************************************************************
test_park_w_brake_not_pressed_key_close_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_not_pressed_key_close_start_not_pressed` for if the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed` AND the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  ============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ============
  :green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ==============  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 7

        def test_brake_not_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

        def test_park_w_brake_pressed_key_not_close_start_not_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False, in_park=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed` AND the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  ============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ============
  :green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ==============  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 10-17

        def test_brake_not_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=False,
                )
            )

        def test_park_w_brake_pressed_key_not_close_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_brake_not_pressed_key_close_start_not_pressed`

.. code-block:: python
  :lineno-start: 52
  :emphasize-lines: 10

      def test_brake_not_pressed_key_close_start_not_pressed(self):
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=False,
                  key_is_close=True,
                  brake_is_pressed=False,
                  in_park=True,
              )
          )
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=False,
                  key_is_close=True,
                  brake_is_pressed=False,
                  in_park=False,
              )
          )

      def test_park_w_brake_pressed_key_not_close_start_not_pressed(self):

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=False, key_is_close=True,
      brake_is_pressed=False, in_park=True
  ) -> False
  ignition(
      start_is_pressed=False, key_is_close=True,
      brake_is_pressed=False, in_park=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name of the test from :ref:`test_brake_not_pressed_key_close_start_not_pressed` to :ref:`test_park_w_brake_not_pressed_key_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10

        def test_brake_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

        def test_park_w_brake_not_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_not_pressed_key_close_start_not_pressed'

----

*********************************************************************************
test_park_w_brake_pressed_key_close_start_not_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_pressed_key_close_start_not_pressed` for if the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :green:`in park`

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 7

        def test_brake_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

        def test_park_w_brake_not_pressed_key_close_start_not_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True, in_park=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  ============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ============
  :green:`close`  :green:`pressed`    :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ==============  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 43
    :emphasize-lines: 10-17

        def test_brake_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=False,
                )
            )

        def test_park_w_brake_not_pressed_key_close_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_brake_pressed_key_close_start_not_pressed`

.. code-block:: python
  :lineno-start: 43
  :emphasize-lines: 10

      def test_brake_pressed_key_close_start_not_pressed(self):
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=False,
                  key_is_close=True,
                  brake_is_pressed=True,
                  in_park=True,
              )
          )
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=False,
                  key_is_close=True,
                  brake_is_pressed=True,
                  in_park=False,
              )
          )

      def test_park_w_brake_not_pressed_key_close_start_not_pressed(self):

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=False, key_is_close=True,
      brake_is_pressed=True, in_park=True
  ) -> False
  ignition(
      start_is_pressed=False, key_is_close=True,
      brake_is_pressed=True, in_park=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_brake_pressed_key_close_start_not_pressed` to :ref:`test_park_w_brake_pressed_key_close_start_not_pressed`

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10

        def test_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                )
            )

        def test_park_w_brake_pressed_key_close_start_not_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=False,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_pressed_key_close_start_not_pressed'

----

*********************************************************************************
test_park_w_brake_not_pressed_key_not_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_not_pressed_key_not_close_start_pressed` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :red:`NOT pressed` AND the car gear is :green:`in park`

  ================  ==================  ==================  ==================  ============
  key               brake               start               gear                output
  ================  ==================  ==================  ==================  ============
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  ================  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 7

        def test_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

        def test_park_w_brake_pressed_key_close_start_not_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :red:`NOT pressed` AND the car gear is :red:`NOT in park`

  ================  ==================  ==================  ==================  ============
  key               brake               start               gear                output
  ================  ==================  ==================  ==================  ============
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  ================  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 34
    :emphasize-lines: 10-17

        def test_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=False,
                )
            )

        def test_park_w_brake_pressed_key_close_start_not_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_brake_not_pressed_key_not_close_start_pressed`

.. code-block:: python
  :lineno-start: 34
  :emphasize-lines: 10

      def test_brake_not_pressed_key_not_close_start_pressed(self):
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=True,
                  key_is_close=False,
                  brake_is_pressed=False,
                  in_park=True,
              )
          )
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=True,
                  key_is_close=False,
                  brake_is_pressed=False,
                  in_park=False,
              )
          )

      def test_park_w_brake_pressed_key_close_start_not_pressed(self):

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=True, key_is_close=False,
      brake_is_pressed=False, in_park=False
  ) -> False
  ignition(
      start_is_pressed=True, key_is_close=False,
      brake_is_pressed=False, in_park=True
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_brake_not_pressed_key_not_close_start_pressed` to :ref:`test_park_w_brake_not_pressed_key_not_close_start_pressed`

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10

        def test_brake_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                )
            )

        def test_park_w_brake_not_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_not_pressed_key_not_close_start_pressed'

----

*********************************************************************************
test_park_w_brake_pressed_key_not_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_pressed_key_not_close_start_pressed` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :green:`pressed` AND the car gear is :green:`in park`

  ================  ==================  ==================  ==================  ============
  key               brake               start               gear                output
  ================  ==================  ==================  ==================  ============
  :red:`NOT close`  :green:`pressed`    :green:`pressed`    :green:`in park`    :red:`False`
  ================  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 7

        def test_brake_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

        def test_park_w_brake_not_pressed_key_not_close_start_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=True, in_park=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :green:`pressed` AND the car gear is :red:`NOT in park`

  ================  ==================  ==================  ==================  ============
  key               brake               start               gear                output
  ================  ==================  ==================  ==================  ============
  :red:`NOT close`  :green:`pressed`    :green:`pressed`    :red:`NOT in park`  :red:`False`
  ================  ==================  ==================  ==================  ============

  .. code-block:: python
    :lineno-start: 25
    :emphasize-lines: 10-17

        def test_brake_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=False,
                )
            )

        def test_park_w_brake_not_pressed_key_not_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_brake_pressed_key_not_close_start_pressed`

.. code-block:: python
  :lineno-start: 25
  :emphasize-lines: 10

      def test_brake_pressed_key_not_close_start_pressed(self):
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=True,
                  key_is_close=False,
                  brake_is_pressed=True,
                  in_park=True,
              )
          )
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=True,
                  key_is_close=False,
                  brake_is_pressed=True,
                  in_park=False,
              )
          )

      def test_park_w_brake_not_pressed_key_not_close_start_pressed(self):

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=True, key_is_close=False,
      brake_is_pressed=True, in_park=True
  ) -> False
  ignition(
      start_is_pressed=True, key_is_close=False,
      brake_is_pressed=True, in_park=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_brake_pressed_key_not_close_start_pressed` to :ref:`test_park_w_brake_pressed_key_not_close_start_pressed`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10

        def test_brake_not_pressed_key_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                )
            )

        def test_park_w_brake_pressed_key_not_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=False,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_pressed_key_not_close_start_pressed'

----

*********************************************************************************
test_park_w_brake_not_pressed_key_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_not_pressed_key_close_start_pressed` for if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed` AND the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  =============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  =============
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  ==============  ==================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 7

        def test_brake_not_pressed_key_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

        def test_park_w_brake_pressed_key_not_close_start_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=False, in_park=True
    ) -> False

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed` AND the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  =============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  =============
  :green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  ==============  ==================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 10-17

        def test_brake_not_pressed_key_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=False,
                )
            )

        def test_park_w_brake_pressed_key_not_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: False is not true

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another way to test if something is grouped as False>` in :ref:`test_brake_not_pressed_key_close_start_pressed`

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 10

      def test_brake_not_pressed_key_close_start_pressed(self):
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=True,
                  key_is_close=True,
                  brake_is_pressed=False,
                  in_park=True,
              )
          )
          self.assertFalse(
              src.car.ignition(
                  start_is_pressed=True,
                  key_is_close=True,
                  brake_is_pressed=False,
                  in_park=False,
              )
          )

      def test_park_w_brake_pressed_key_not_close_start_pressed(self):

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=True, key_is_close=True,
      brake_is_pressed=False, in_park=True
  ) -> False
  ignition(
      start_is_pressed=True, key_is_close=True,
      brake_is_pressed=False, in_park=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I change the name from :ref:`test_brake_not_pressed_key_close_start_pressed` to :ref:`test_park_w_brake_not_pressed_key_close_start_pressed`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10

        def test_brake_pressed_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                )
            )

        def test_park_w_brake_not_pressed_key_close_start_pressed(self):
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=False,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_not_pressed_key_close_start_pressed'

----

*********************************************************************************
test_park_w_brake_pressed_key_close_start_pressed
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
* I add a value for the ``in_park`` parameter to the :ref:`assertion<what is an assertion?>` in :ref:`test_brake_pressed_key_close_start_pressed` for if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  =============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  =============
  :green:`close`  :green:`pressed`    :green:`pressed`    :green:`in park`    :green:`True`
  ==============  ==================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 7

        def test_brake_pressed_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

        def test_park_w_brake_not_pressed_key_close_start_pressed(self):

  the test is still green.

  .. code-block:: python

    ignition(
        start_is_pressed=True, key_is_close=True,
        brake_is_pressed=True, in_park=True
    ) -> True

* I add an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  =============
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  =============
  :green:`close`  :green:`pressed`    :green:`pressed`    :red:`NOT in park`  :red:`False`
  ==============  ==================  ==================  ==================  =============

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 10-17

        def test_brake_pressed_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )
            self.assertFalse(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=False,
                )
            )

        def test_park_w_brake_not_pressed_key_close_start_pressed(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True is not false

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add an :ref:`if statement<if statements>` to the ``ignition`` :ref:`function<what is a function?>` in ``car.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def ignition(
          start_is_pressed, key_is_close=False,
          brake_is_pressed=False, in_park=False,
      ):
      if in_park == False:
          return False
      if start_is_pressed:
          if key_is_close:
              return brake_is_pressed
      return False

the test passes.

.. code-block:: python

  ignition(
      start_is_pressed=True, key_is_close=True,
      brake_is_pressed=True, in_park=True
  ) -> True
  ignition(
      start_is_pressed=True, key_is_close=True,
      brake_is_pressed=True, in_park=False
  ) -> False

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I make the :ref:`if statement<if statements>` simpler with :ref:`Logical Negation (NOT)<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

        # if in_park == False:
        if not in_park:
            return False

  the test is still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``.

* I want the :ref:`function<what is a function?>` to check if the start button is :green:`pressed` before it checks the other :ref:`conditions<if statements>`. I add an :ref:`if statement<if statements>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3, 6-8

        # if in_park == False:
        # if not in_park:
        #     return False
        if start_is_pressed:
            if key_is_close:
                # return brake_is_pressed
                if brake_is_pressed:
                    return in_park
        return False

  still green.

* I use :ref:`Logical Conjunction (AND)<test_logical_conjunction>` to put the :ref:`if statements` together

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 4-5, 7-14

        # if in_park == False:
        # if not in_park:
        #     return False
        # if start_is_pressed:
        #     if key_is_close:
                # return brake_is_pressed
                # if brake_is_pressed:
                #     return in_park
        if (
            start_is_pressed
            and key_is_close
            and brake_is_pressed
        ):
            return in_park
        return False

  green.

* I remove the commented lines from the ``ignition`` :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:

    def ignition(
            start_is_pressed, key_is_close=False,
            brake_is_pressed=False, in_park=False,
        ):
        if (
            start_is_pressed
            and key_is_close
            and brake_is_pressed
        ):
            return in_park
        return False

* I change the name from :ref:`test_brake_pressed_key_close_start_pressed` to :ref:`test_park_w_brake_pressed_key_close_start_pressed`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_park_w_brake_pressed_key_close_start_pressed(self):
            self.assertTrue(
                src.car.ignition(
                    start_is_pressed=True,
                    key_is_close=True,
                    brake_is_pressed=True,
                    in_park=True,
                )
            )

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'add test_park_w_brake_pressed_key_close_start_pressed'

When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`. It checks if the start button is :green:`pressed` then if the key is :green:`close` to the ignition then if the brake is :green:`pressed`

* If the start button is :red:`NOT pressed` it returns :red:`False`

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=False, in_park=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True, in_park=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=False,
        brake_is_pressed=True, in_park=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False, in_park=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=False, in_park=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True, in_park=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=False, key_is_close=True,
        brake_is_pressed=True, in_park=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
            ┌───┴── start_is_pressed
            │       and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

* if the start button is :green:`pressed` AND the key is :red:`NOT close` to the ignition it leaves the :ref:`if statements<if statements>` then returns :red:`False`

  .. code-block:: shell

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=False, in_park=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
                ├── start_is_pressed
            ┌───┴── and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=False, in_park=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
                ├── start_is_pressed
            ┌───┴── and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=True, in_park=True
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
                ├── start_is_pressed
            ┌───┴── and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

  .. code-block:: shell

    ignition(
        start_is_pressed=True, key_is_close=False,
        brake_is_pressed=True, in_park=False
    ) -> False
    └── def ignition(
                start_is_pressed, key_is_close=False,
                brake_is_pressed=False, in_park=False,
            ):
            └── if (
                ├── start_is_pressed
            ┌───┴── and key_is_close
            │       and brake_is_pressed
            │   ):
            │       return in_park
            └── return False

* if the start button is :green:`pressed` AND the key is :green:`close` to the ignition it checks if the brake is being :green:`pressed`

  - if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is :red:`NOT pressed` it leaves the :ref:`if statement<if statements>` then returns :red:`False`

    .. code-block:: shell

      ignition(
          start_is_pressed=True, key_is_close=True,
          brake_is_pressed=False, in_park=True
      ) -> False
      └── def ignition(
                  start_is_pressed, key_is_close=False,
                  brake_is_pressed=False, in_park=False,
              ):
              └── if (
                  ├── start_is_pressed
                  ├── and key_is_close
              ┌───┴── and brake_is_pressed
              │   ):
              │       return in_park
              └── return False

    .. code-block:: shell

      ignition(
          start_is_pressed=True, key_is_close=True,
          brake_is_pressed=False, in_park=False
      ) -> False
      └── def ignition(
                  start_is_pressed, key_is_close=False,
                  brake_is_pressed=False, in_park=False,
              ):
              └── if (
                  ├── start_is_pressed
                  ├── and key_is_close
              ┌───┴── and brake_is_pressed
              │   ):
              │       return in_park
              └── return False

  - if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is :green:`pressed` it returns the value of ``in_park``

    * if the car gear is :red:`NOT in park` it returns :red:`False`

      .. code-block:: shell

        ignition(
            start_is_pressed=True, key_is_close=True,
            brake_is_pressed=True, in_park=False
        ) -> False
        └── def ignition(
                    start_is_pressed, key_is_close=False,
                    brake_is_pressed=False, in_park=False,
                ):
                └── if (
                    ├── start_is_pressed
                    ├── and key_is_close
                    └── and brake_is_pressed
                    ):
                    └── return in_park
                        return False
                    return False

    * if the car gear is :green:`in park` it returns :green:`True`

      .. code-block:: shell

        ignition(
            start_is_pressed=True, key_is_close=True,
            brake_is_pressed=True, in_park=True
        ) -> True
        └── def ignition(
                    start_is_pressed, key_is_close=False,
                    brake_is_pressed=False, in_park=False,
                ):
                └── if (
                    ├── start_is_pressed
                    ├── and key_is_close
                    └── and brake_is_pressed
                    ):
                    └── return in_park
                        return True
                    return False



*********************************************************************************
close the project
*********************************************************************************

* I close ``test_car.py`` and ``car.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for a car with these inputs:

* was the start button pressed?
* is the key close to the ignition?
* is the brake being pressed?
* is the car in park?

the inputs gave me this :ref:`truth table`

==============  ==================  ==================  ==================  =============
key             brake               start               gear                output
==============  ==================  ==================  ==================  =============
:green:`close`  :green:`pressed`    :green:`pressed`    :green:`in park`    :green:`True`
:green:`close`  :green:`pressed`    :green:`pressed`    :red:`NOT in park`  :red:`False`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
==============  ==================  ==================  ==================  =============

================  ==================  ==================  ==================  ============
key               brake               start               gear                output
================  ==================  ==================  ==================  ============
:red:`NOT close`  :green:`pressed`    :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`    :green:`pressed`    :red:`NOT in park`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
================  ==================  ==================  ==================  ============

==============  ==================  ==================  ==================  ============
key             brake               start               gear                output
==============  ==================  ==================  ==================  ============
:green:`close`  :green:`pressed`    :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`  :green:`pressed`    :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==============  ==================  ==================  ==================  ============

================  ==================  ==================  ==================  ============
key               brake               start               gear                output
================  ==================  ==================  ==================  ============
:red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
================  ==================  ==================  ==================  ============

the only time I can start this car is if the start button is :green:`pressed` AND the key is :green:`close` to the ignition AND the brake is being :green:`pressed` AND the car gear is :green:`in park`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Car: tests and solutions>`

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
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.
* :ref:`I know how Python groups objects into False or True<what are booleans?>`
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`
* :ref:`I know how to write programs that make decisions<truth table>`

:ref:`Would you like to test making an Elevator?<elevator>`

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