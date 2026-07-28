.. meta::
  :description:
  :keywords:

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
  :caption: truth_table/tests/test_car.py

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

    .. tab-item:: no WSL
      :sync: no_wsl

      * I open ``makePythonTdd.ps1``

* I name this project ``car``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I change the name of the project to ``car`` in ``makePythonTdd.sh``

        .. literalinclude:: ../../code/car/make_tdd/makePythonTddCar.sh
          :language: python
          :linenos:
          :emphasize-lines: 2-3, 5, 12, 20

      * I run ``makePythonTdd.sh`` in the terminal_ to make the ``car`` project

        .. code-block:: python
          :emphasize-lines: 1

          ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      * I change the name of the project to ``car`` in ``makePythonTdd.ps1``

        .. literalinclude:: ../../code/car/make_tdd/makePythonTddCar.ps1
          :language: Powershell
          :linenos:
          :emphasize-lines: 1-2, 4, 11, 19

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

If the input to the **Car** ignition is if the start button pressed? I get this :ref:`truth table`

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

I change :ref:`test_failure` to :ref:`test_start_pressed`, then add an :ref:`assertion<what is an assertion?>` for if the start button is :green:`pressed`

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
* I add ``key_is_close`` with a value to the :ref:`call<how to call a function with input>` to the ``ignition`` :ref:`function<what is a function?>` for if the the start button is :green:`pressed` AND the key is :green:`close` to the ignition

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

  because the :ref:`assertion<what is an assertion?>` :ref:`calls<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with one argument(``start_is_pressed``) and I just changed the :ref:`<what is a function?>` to make it take two required arguments (``key_is_close`` and ``start_is_pressed``). I have to make ``key_is_close`` a :ref:`choice<test_optional_arguments>`.

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
    :emphasize-lines:

        # if brake_is_pressed == False:
        # if not brake_is_pressed:
        #     return False
        if start_is_pressed:
            # return key_is_close
            if key_is_close:
                return brake_is_pressed
        return False

    the test is still green.

* I remove the commented lines from the ``ignition`` :ref:`function<what is a function>`

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

* I change :ref:`assertTrue<another way to test if something is grouped as True>` to :ref:`assertFalse<another to test if something is grouped as False>` to match reality

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

* I add a git_ commit message in the other terminal_


* I add an :ref:`assertion<what is an assertion?>` for if the start button is :red:`NOT pressed` AND the key is :red:`NOT close` to the ignition AND the brake is :red:`NOT pressed`

  ==============  ==================  ==================  ===========
  key             brake               start button        output
  ==============  ==================  ==================  ===========
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
  ==============  ==================  ==================  ===========

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 9-14

        def test_key_not_close_brake_not_pressed(self):
            reality = src.car.ignition(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            self.assertEqual(reality, OFF)

            reality = src.car.ignition(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            self.assertEqual(reality, OFF)


    # Exceptions seen

  still green.

* I call the ``ignition`` :ref:`function<what is a function?>` directly in :ref:`test_key_not_close_brake_not_pressed`, I do not need the ``reality`` :ref:`variable<what is a variable?>` because it is only used once in each :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 7-15, 22-30

        def test_key_not_close_brake_not_pressed(self):
            reality = src.car.ignition(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.car.ignition(
                key_is_close=False,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

  the test is still green.

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>`

  .. code-block:: python
    :lineno-start: 56

        def test_key_not_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )


    # Exceptions seen

* I do the same thing in :ref:`test_key_not_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 7-15, 22-30

        def test_key_not_close_brake_pressed(self):
            reality = src.car.ignition(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                    src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.car.ignition(
                key_is_close=False,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_not_close_brake_not_pressed(self):

  still green.

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_key_not_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 41

        def test_key_not_close_brake_pressed(self):
            self.assertEqual(
                    src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_not_close_brake_not_pressed(self):

* on to :ref:`test_key_close_brake_not_pressed`

  .. code-block:: python
    :lineno-start: 26
    :emphasize-lines: 7-15, 22-30

        def test_key_close_brake_not_pressed(self):
            reality = src.car.ignition(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            reality = src.car.ignition(
                key_is_close=True,
                brake_is_pressed=False,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_not_close_brake_pressed(self):

  green.

* I remove the commented lines and ``reality`` :ref:`variables<what is a variable?>` from :ref:`test_key_close_brake_not_pressed`

  .. code-block:: python
    :lineno-start: 26

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_not_close_brake_pressed(self):

* I call the ``ignition`` :ref:`function<what is a function?>` directly in :ref:`test_key_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 8-16, 23-31

        def test_key_close_brake_pressed(self):
            my_expectation = True
            reality = src.car.ignition(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=True,
            )
            # self.assertEqual(reality, my_expectation)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                True
            )

            reality = src.car.ignition(
                key_is_close=True,
                brake_is_pressed=True,
                start_is_pressed=False,
            )
            # self.assertEqual(reality, OFF)
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

  still green.

* I remove the commented lines and unused :ref:`variables<what is a variable?>` from :ref:`test_key_close_brake_pressed`

  .. code-block:: python
    :lineno-start: 10

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                ),
                True
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

----

*********************************************************************************
test_key_close_brake_pressed_w_gear
*********************************************************************************

the :ref:`truth table` for the car ignition is

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:green:`close`    :green:`pressed`    :green:`pressed`    :green:`True`
:green:`close`    :green:`pressed`    :red:`NOT pressed`  :red:`False`
:green:`close`  :red:`NOT pressed`  :green:`pressed`    :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
==============  ==================  ==================  ===========

==============  ==================  ==================  ===========
key             brake               start button        output
==============  ==================  ==================  ===========
:red:`NOT close`  :green:`pressed`    :green:`pressed`    :red:`False`
:red:`NOT close`  :green:`pressed`    :red:`NOT pressed`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`False`
==============  ==================  ==================  ===========

I want to make sure the car is in park before it can start, so it does not immediately move when it is turned on (that would be a problem). The inputs will then be

* is the key close to the ignition?
* is the brake being pressed?
* was the start button pressed?
* is the gear in park?

and the :ref:`truth table` for if the key is :green:`close` and the brake is being :green:`pressed`, is:

==============  ================  ==================  ==================  ================
key             brake             start button        gear                output
==============  ================  ==================  ==================  ================
:green:`close`    :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`True`
:green:`close`    :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:green:`close`    :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`    :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==============  ================  ==================  ==================  ================

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I go back to the terminal_ where the tests are running
I add a value for ``in_park`` to the :ref:`assertion<what is an assertion?>` for the case where the key is :green:`close`, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :green:`in park`, to :ref:`test_key_close_brake_pressed`

==============  ================  ==================  ==================  ================
key             brake             start button        gear                output
==============  ================  ==================  ==================  ================
:green:`close`    :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`True`
==============  ================  ==================  ==================  ================

.. code-block:: python
  :lineno-start: 10
  :emphasize-lines: 7

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                True
            )

the terminal shows :ref:`TypeError<what causes TypeError?>`

.. code-block:: python

  TypeError: ignition() got an unexpected keyword argument 'in_park'

  because the test :ref:`called<how to call a function with input>` the ``ignition`` :ref:`function<what is a function?>` with a :ref:`name<test_keyword_arguments>` (``in_park``) that is not in the parentheses of its :ref:`definition<how to make a function that takes input>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_car.py``

  .. code-block:: python
    :lineno-start: 16
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

* I add ``in_park`` to the ``ignition`` :ref:`function signature<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3

    def ignition(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park,
        ):
        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
        ):
            return False

        return True

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
        key_is_close, start_is_pressed,
        brake_is_pressed=False, in_park=False,
    ):

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I add an :ref:`assertion<what is an assertion?>` for if the key is :green:`close`, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :red:`NOT in park`

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`    :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`True`
  :green:`close`    :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 12-20

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                True
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: True != False

  because the ``ignition`` :ref:`function<what is a function?>` returns :green:`True` and the :ref:`assertion<what is an assertion?>` expects :red:`False`

* I add an :ref:`if statement<if statements>` to the ``ignition`` :ref:`function<what is a function?>` in ``car.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    def ignition(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park=False,
        ):
        if in_park == False:
            return False

        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
        ):
            return False

        return True

  the test passes.

* I use :ref:`Logical Negation (NOT)<test_logical_negation>` to write it in terms of :ref:`True<test_what_is_true>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

        # if in_park == False:
        if not in_park == True:
            return False

  the test is still green.

* I remove ``== True``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2-3

        # if in_park == False:
        # if not in_park == True:
        if not in_park:
            return False

  still green, because ``if something == False`` is the same as ``if not something == True`` is the same as ``if not something``.

* I use :ref:`Logical Disjunction (OR)<test_logical_disjunction>` to put the two :ref:`if statements` together because they both return :red:`False`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8, 10-21

    def ignition(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park=False,
        ):
        # if in_park == False:
        # if not in_park == True:
        # if not in_park:
        #     return False

        # if not (
        #     key_is_close
        #     and start_is_pressed
        #     and brake_is_pressed
        # ):
        if (
            not (
                key_is_close
                and start_is_pressed
                and brake_is_pressed
            ) or not in_park
        ):
            return False

        return True

  that is one long confusing statement

* I write the new :ref:`if statement<if statements>` in terms of :ref:`not<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 6-21

        # if not (
        #     key_is_close
        #     and start_is_pressed
        #     and brake_is_pressed
        # ):
        # if (
        #     not (
        #         key_is_close
        #         and start_is_pressed
        #         and brake_is_pressed
        #     ) or not in_park
        # ):
        if (
            (not (
                key_is_close
                and start_is_pressed
                and brake_is_pressed
            ))
            (not and)
            (not in_park)
        ):
            return False

        return True

  the terminal_ is my friend, and shows SyntaxError_

  .. code-block:: python

    SyntaxError: invalid syntax

  I cannot :ref:`negate<test_logical_negation>` :ref:`and<test_logical_conjunction>` this way

* I factor out the :ref:`nots<test_logical_negation>`

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 13-30

        # if not (
        #     key_is_close
        #     and start_is_pressed
        #     and brake_is_pressed
        # ):
        # if (
        #     not (
        #         key_is_close
        #         and start_is_pressed
        #         and brake_is_pressed
        #     ) or not in_park
        # ):
        # if (
        #     (not (
        #         key_is_close
        #         and start_is_pressed
        #         and brake_is_pressed
        #     ))
        #     (not and)
        #     (not in_park)
        # ):
        if not (
            (
                key_is_close
                and start_is_pressed
                and brake_is_pressed
            )
            and
            in_park
        ):
            return False

        return True

  the test is green again

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def ignition(
            key_is_close, start_is_pressed,
            brake_is_pressed=False, in_park=False,
        ):
        if not (
            key_is_close
            and start_is_pressed
            and brake_is_pressed
            and in_park
        ):
            return False

        return True

  When the ``ignition`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

  - it returns :red:`False` if the key is :red:`NOT close` to the ignition OR the start button is :red:`NOT pressed` OR the brake is :red:`NOT pressed` OR the car gear is :red:`NOT in park`
  - it returns :green:`True` if none of the conditions are met

* I add a value for the ``in_park`` parameter in the next :ref:`assertion<what is an assertion?>` for if the key is :green:`close`, the brake is being :green:`pressed`, the start button is :red:`NOT pressed` and the car gear is :green:`in park`, in :ref:`test_key_close_brake_pressed` in ``test_car.py``

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`    :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`True`
  :green:`close`    :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :green:`close`    :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 27

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                True
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :green:`close`, the brake is being :green:`pressed`, the start button is :red:`NOT pressed` and the car gear is  :red:`NOT in park`

  ==============  ================  ==================  ==================  ================
  key             brake             start button        gear                output
  ==============  ================  ==================  ==================  ================
  :green:`close`    :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`True`
  :green:`close`    :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :green:`close`    :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  :green:`close`    :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ==============  ================  ==================  ==================  ================

  .. code-block:: python
    :lineno-start: 10
    :emphasize-lines: 32-40

        def test_key_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                True
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed(self):

  green.

* I change the name of the test from :ref:`test_key_close_brake_pressed` to :ref:`test_key_close_brake_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 8
    :emphasize-lines: 3

    class TestCar(unittest.TestCase):

        def test_key_close_brake_pressed_w_gear(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                True
            )

----

*********************************************************************************
test_key_close_brake_not_pressed_w_gear
*********************************************************************************

The :ref:`truth table` for if the key is :green:`close` and the brake is :red:`NOT pressed` is

==============  ==================  ==================  ==================  ==========
key             brake               start               gear                output
==============  ==================  ==================  ==================  ==========
:green:`close`    :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==============  ==================  ==================  ==================  ==========

* I add a value for the ``in_park`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_key_close_brake_not_pressed` for if the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :green:`pressed` and the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 7

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :green:`pressed` and the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 12-20

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_not_close_brake_pressed(self):

  the test is still green.

* I add a value for ``in_park`` to the next :ref:`assertion<what is an assertion?>`, for if the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed` and the car gear is :green:`in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 27

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

        def test_key_not_close_brake_pressed(self):

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :green:`close`, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed` and the car gear is :red:`NOT in park`

  ==============  ==================  ==================  ==================  ==========
  key             brake               start               gear                output
  ==============  ==================  ==================  ==================  ==========
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  :green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ==============  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 51
    :emphasize-lines: 32-40

        def test_key_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_not_close_brake_pressed(self):

  green.

* I change the name of the test from :ref:`test_key_close_brake_not_pressed` to :ref:`test_key_close_brake_not_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 41
    :emphasize-lines: 11

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_close_brake_not_pressed_w_gear(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

----

*********************************************************************************
test_key_not_close_brake_pressed_w_gear
*********************************************************************************

The :ref:`truth table` for if the key is :red:`NOT close` to the ignition and the brake is being :green:`pressed` is

==========  ================  ==================  ==================  ==========
key         brake             start               gear                output
==========  ================  ==================  ==================  ==========
:red:`NOT close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==========  ================  ==================  ==================  ==========

* I add a value for the ``in_park`` parameter in the first :ref:`assertion<what is an assertion?>` of :ref:`test_key_not_close_brake_pressed`, for if the key is :red:`NOT close` to the ignition, the brake is being :green:`pressed`, the start button is :green:`pressed`, and the car gear is :green:`in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 7

        def test_key_not_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

  still green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :red:`NOT close` to the ignition, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :red:`NOT in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 12-20

        def test_key_not_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                ),
                OFF
            )

        def test_key_not_close_brake_not_pressed(self):

  still green.

* I add a value for the ``in_park`` parameter to the next :ref:`assertion<what is an assertion?>` for if the key is :red:`NOT close` to the ignition, the brake is being :green:`pressed`, the start button is :red:`NOT pressed`, and the car gear is :green:`in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 27

        def test_key_not_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

        def test_key_not_close_brake_not_pressed(self):

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :red:`NOT close` to the ignition, the brake is being :green:`pressed`, the start button is :red:`NOT pressed`, and the car gear is :red:`NOT in park`

  ==========  ================  ==================  ==================  ==========
  key         brake             start               gear                output
  ==========  ================  ==================  ==================  ==========
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :red:`NOT close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  :red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ==========  ================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 32-40

        def test_key_not_close_brake_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_not_close_brake_not_pressed(self):

  still green.

* I change the name of the test from :ref:`test_key_not_close_brake_pressed` to :ref:`test_key_not_close_brake_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 11

            self.assertEqual(
                src.car.ignition(
                    key_is_close=True,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_not_close_brake_pressed_w_gear(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

----

*********************************************************************************
test_key_not_close_brake_not_pressed_w_gear
*********************************************************************************

The :ref:`truth table` for if the key is :red:`NOT close` to the ignition and the brake is :red:`NOT pressed` is

==========  ==================  ==================  ==================  ==========
key         brake               start               gear                output
==========  ==================  ==================  ==================  ==========
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==========  ==================  ==================  ==================  ==========

* I add a value for the ``in_park`` parameter to the first :ref:`assertion<what is an assertion?>` in :ref:`test_key_not_close_brake_not_pressed`, for if the key is :red:`NOT close` to the ignition, the brake is :red:`NOT pressed`, the start button is :green:`pressed`, and the car gear is :green:`in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 7

        def test_key_not_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

  the test is still green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :red:`NOT close` to the ignition, the brake is :red:`NOT pressed`, the start button is :green:`pressed`, and the car gear is :red:`NOT in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 12-20

        def test_key_not_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                ),
                OFF
            )


    # Exceptions seen

  still green.

* I add a value for the ``in_park`` parameter to the next :ref:`assertion<what is an assertion?>`, for if the key is :red:`NOT close` to the ignition, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed`, and the car gear is :green:`in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 27

        def test_key_not_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

  green.

* I add an :ref:`assertion<what is an assertion?>` for if the key is :red:`NOT close` to the ignition, the brake is :red:`NOT pressed`, the start button is :red:`NOT pressed`, and the car gear is :red:`NOT in park`

  ==========  ==================  ==================  ==================  ==========
  key         brake               start               gear                output
  ==========  ==================  ==================  ==================  ==========
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
  :red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
  ==========  ==================  ==================  ==================  ==========

  .. code-block:: python
    :lineno-start: 133
    :emphasize-lines: 32-40

        def test_key_not_close_brake_not_pressed(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=False,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=True,
                ),
                OFF
            )

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )


    # Exceptions seen

  all the tests are still green.

* I change the name of the test from :ref:`test_key_not_close_brake_not_pressed` to :ref:`test_key_not_close_brake_not_pressed_w_gear`

  .. code-block:: python
    :lineno-start: 123
    :emphasize-lines: 11

            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=True,
                    start_is_pressed=False,
                    in_park=False,
                ),
                OFF
            )

        def test_key_not_close_brake_not_pressed_w_gear(self):
            self.assertEqual(
                src.car.ignition(
                    key_is_close=False,
                    brake_is_pressed=False,
                    start_is_pressed=True,
                    in_park=True,
                ),
                OFF
            )

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_car.py`` and ``car.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``car``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests for a car with these inputs:

* is the key close to the ignition?
* is the brake being pressed?
* was the start button pressed?
* is the car in park?

the inputs gave me this :ref:`truth table`

==============  ================  ==================  ==================  ================
key             brake             start button        gear                output
==============  ================  ==================  ==================  ================
:green:`close`    :green:`pressed`  :green:`pressed`    :green:`in park`    :green:`True`
:green:`close`    :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:green:`close`    :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`    :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==============  ================  ==================  ==================  ================

==============  ==================  ==================  ==================  ==========
key             brake               start               gear                output
==============  ==================  ==================  ==================  ==========
:green:`close`    :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:green:`close`    :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:green:`close`    :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==============  ==================  ==================  ==================  ==========

==========  ================  ==================  ==================  ==========
key         brake             start               gear                output
==========  ================  ==================  ==================  ==========
:red:`NOT close`  :green:`pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :green:`pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==========  ================  ==================  ==================  ==========

==========  ==================  ==================  ==================  ==========
key         brake               start               gear                output
==========  ==================  ==================  ==================  ==========
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :green:`pressed`    :red:`NOT in park`  :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :green:`in park`    :red:`False`
:red:`NOT close`  :red:`NOT pressed`  :red:`NOT pressed`  :red:`NOT in park`  :red:`False`
==========  ==================  ==================  ==================  ==========

the only time I can start this car is if the key is :green:`close` to the ignition, the brake is being :green:`pressed`, the start button is :green:`pressed` and the car gear is :green:`in park`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<car: tests and solutions>`

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
* :ref:`how to write programs that make decisions<truth table>`

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