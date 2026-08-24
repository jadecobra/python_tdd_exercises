.. meta::
  :description: How to handle Exceptions in Python programs with try/except/else, unittest assertRaisesRegex for Exception messages (BOOM!!! vs empty string), and a homemade assert_raises that raises AssertionError like unittest. TDD RED/GREEN for raise_exception (AttributeError has no attribute, NameError is not defined, TypeError NoneType not callable), then an_exception_handler that returns failed when a function raises and succeeded when it does not. Catching Exception vs ModuleNotFoundError shows a child cannot catch its parent. Pumping Python TDD by Jacob Itegboje.
  :keywords: Jacob Itegboje, Pumping Python TDD, how to handle Exceptions in programs, try except else, assertRaisesRegex, BOOM!!! does not match empty string, raise Exception message, assert_raises f-string not raised, an_exception_handler failed succeeded, AttributeError raise_exception, NameError is not defined, TypeError NoneType not callable, TypeError takes 0 positional arguments but 1 was given, Exception not ModuleNotFoundError, child cannot catch parent Exception, exceptions/tests/test_exceptions.py, src/exceptions/__init__.py

.. include:: ../../links.rst

#################################################################################
how to handle Exceptions in programs
#################################################################################

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_programs.py
  :language: python
  :linenos:
  :caption: exceptions/tests/test_exceptions.py
  :lines: 1-14

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_programs.py
  :language: python
  :lineno-start: 82
  :caption: exceptions/tests/test_exceptions.py
  :lines: 82-94

.. literalinclude:: ../../code/exception_handling/test_exceptions_in_programs.py
  :language: python
  :lineno-start: 96
  :caption: exceptions/tests/test_exceptions.py
  :lines: 96-

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`how to test that an Exception is raised`

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``exceptions`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    cd exceptions

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ is my friend, and shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/exceptions
    configfile: pyproject.toml
    collected 8 items

    tests/test_exceptions.py ........                      [100%]

    ==================== 8 passed in X.YZs ======================

* I hold :kbd:`ctrl` on the keyboard, then click on ``tests/test_exceptions.py`` to open it

----

*********************************************************************************
test_catching_exceptions_w_messages
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add a failing test to ``tests/test_exceptions.py``

  .. code-block:: python
    :lineno-start: 77
    :emphasize-lines: 6-7

        def test_catching_exceptions(self):
            self.assert_raises('raise Exception', Exception)
            with self.assertRaises(Exception):
                raise Exception

        def test_catching_exceptions_w_messages(self):
            src.exceptions.raise_exception()


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.exceptions'
                    has no attribute 'raise_exception'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``src/exceptions/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def function_name():
        return None


    raise_exception

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'raise_exception' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    raise_exception = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* I make ``raise_exception`` a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def raise_exception():
        return None

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I want the :ref:`function<what is a function?>` to :ref:`raise Exception<how to raise an Exception>` when it is :ref:`called<how to call a function with input>` as a way to make a failure happen. I add :ref:`assertRaises<another way to test if an Exception is raised>` to :ref:`test_catching_exceptions_w_messages` in ``tests/test_exceptions.py``

  .. code-block:: python
    :lineno-start: 82
    :emphasize-lines: 2-3

        def test_catching_exceptions_w_messages(self):
            with self.assertRaises(Exception):
                src.exceptions.raise_exception()

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Exception not raised

* I add a :ref:`raise statement<how to raise an Exception>` to the ``raise_exception`` :ref:`function<what is a function?>` in ``src/exceptions/__init__.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def raise_exception():
        raise Exception

  the test passes.

----

*********************************************************************************
how to test the message of an Exception
*********************************************************************************

I can use the `assertRaisesRegex method`_ to test what message I get with an :ref:`Exception<how to test that an Exception is raised>`. It helps tell the difference between two :ref:`Exceptions<how to test that an Exception is raised>` with the same name.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change :ref:`assertRaises<another way to test if an Exception is raised>` to assertRaisesRegex_ in :ref:`test_catching_exceptions_w_messages` in ``tests/test_exceptions.py``

.. code-block:: python
  :lineno-start: 82
  :emphasize-lines: 2-4

      def test_catching_exceptions_w_messages(self):
          with self.assertRaisesRegex(
              Exception, 'BOOM!!!'
          ):
              src.exceptions.raise_exception()

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: "BOOM!!!" does not match ""

because the :ref:`Exception raised<how to raise an Exception>` by the ``raise_exception`` :ref:`function<what is a function?>` has no message and the `assertRaisesRegex method`_ checks that the code in its context (``src.exceptions.raise_exception()``) :ref:`raises<how to raise an Exception>` the :ref:`Exception<how to test that an Exception is raised>` it is given, with the message it is given (``'BOOM!!!'``).

The default message of the :ref:`Exception<how to test that an Exception is raised>` is the empty string_ (``''``) and the :ref:`assertion<what is an assertion?>` expects ``"BOOM!!!"``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add the expected message in ``src/exceptions/__init__.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 2

  def raise_exception():
      raise Exception('BOOM!!!')

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

This means I can make my :ref:`assert_raises method<extract assert_raises method>` have a message like :ref:`unittest.TestCase.assertRaises<another way to test if an Exception is raised>`.

* I add an :ref:`f-string<telephone>` to my :ref:`assert_raises method<extract assert_raises method>` in ``tests/test_exceptions.py``

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 8

        @staticmethod
        def assert_raises(code, exception):
            try:
                exec(code)
            except exception:
                pass
            else:
                raise AssertionError(f'{exception} not raised')

        def test_catching_module_not_found_error(self):

* I change the statement in :ref:`test_catching_module_not_found_error` to make the test fail

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-4

        def test_catching_module_not_found_error(self):
            self.assert_raises(
                # 'import does_not_exist', ModuleNotFoundError
                'import src.exceptions', ModuleNotFoundError
            )
            with self.assertRaises(ModuleNotFoundError):
                import does_not_exist

        def test_catching_name_error(self):

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: <class 'ModuleNotFoundError'> not raised

  it is now closer to the message of :ref:`the assertRaises method<another way to test if an Exception is raised>`, just not as good.

* I undo the change to :ref:`test_catching_module_not_found_error`

  .. code-block:: python
    :lineno-start: 16

    def test_catching_module_not_found_error(self):
        self.assert_raises(
            'import does_not_exist', ModuleNotFoundError
        )
        with self.assertRaises(ModuleNotFoundError):
            import does_not_exist

    def test_catching_name_error(self):

  the test is green again.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_catching_exceptions_w_messages'

----

In some cases I want to send a message to the user instead of the :ref:`Exception<how to test that an Exception is raised>` which they may not understand.

I might also want the program_ to make a decision if an :ref:`Exception<how to test that an Exception is raised>` happens so it continues without stopping.

I want the program_ to process its input and return ``failed`` if an :ref:`Exception is raised<how to raise an Exception>` while processing the input or return ``success`` if an :ref:`Exception<how to test that an Exception is raised>` is NOT raised.

================= =====================
Exception         output
================= =====================
:green:`raised`   :red:`failed`
:red:`NOT raised` :green:`success`
================= =====================

*********************************************************************************
test_catching_failure
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test for if a :ref:`function is called<how to call a function with input>` and an :ref:`Exception is raised<how to raise an Exception>` to ``tests/test_exceptions.py``

================= =====================
Exception         output
================= =====================
:green:`raised`   :red:`failed`
================= =====================

.. code-block:: python
  :lineno-start: 82
  :emphasize-lines: 7-13

        def test_catching_exceptions_w_messages(self):
            with self.assertRaisesRegex(
                Exception, 'BOOM!!!'
            ):
                src.exceptions.raise_exception()

        def test_catching_failure(self):
            self.assertEqual(
                src.exceptions.an_exception_handler(
                    src.exceptions.raise_exception
                ),
                'failed'
            )

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block::

  AttributeError: module 'src.exceptions'
                  has no attribute 'an_exception_handler'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add ``an_exception_handler`` to ``src/exceptions/__init__.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5

    def raise_exception():
        raise Exception('BOOM!!!')


    an_exception_handler

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: shell

    NameError: name 'an_exception_handler' is not defined

* I point ``an_exception_handler`` to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    an_exception_handler = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* I make ``an_exception_handler`` a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-2

    def an_exception_handler():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: shell

    TypeError: an_exception_handler() takes
               0 positional arguments but 1 was given

* I make ``an_exception_handler`` take input

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def an_exception_handler(the_input):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 'failed'

  the result of the call to ``src.exceptions.an_exception_handler`` is :ref:`None<what is None?>` and the :ref:`assertion<what is an assertion?>` expects ``'failed'``.

* I change the :ref:`return statement<the return statement>` to match the expectation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def an_exception_handler(the_input):
        return 'failed'

  the test passes.

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines:

    git commit -am 'add test_catching_failure'

----

*********************************************************************************
test_catching_success
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test for if ``an_exception_handler`` is :ref:`called<how to call a function with input>` and an :ref:`Exception<how to test that an Exception is raised>` is NOT raised, in ``tests/test_exceptions.py``

================= =====================
Exception         output
================= =====================
:red:`NOT raised` :green:`success`
================= =====================

.. code-block:: python
  :lineno-start: 88
  :emphasize-lines: 9-15

      def test_catching_failure(self):
          self.assertEqual(
              src.exceptions.an_exception_handler(
                  src.exceptions.raise_exception
              ),
              'failed'
          )

      def test_catching_success(self):
          self.assertEqual(
              src.exceptions.an_exception_handler(
                  src.exceptions.function_name
              ),
              'succeeded'
          )


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: python

  AssertionError: 'failed' != 'succeeded'

``src.exceptions.an_exception_handler`` always returns ``'failed'``, the :ref:`assertion<what is an assertion?>` expects ``'succeeded'``

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I make ``an_exception_handler`` return its input

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def an_exception_handler(the_input):
        return the_input
        return 'failed'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    ...test_catching_failure - AssertionError:
            <function raise_exception at 0xabcd12e34567> != 'failed'
    ...test_catching_success - AssertionError:
            <function function_name at 0xfecdb8a7f6e5> != 'succeeded'

  both tests fail because ``an_exception_handler`` returns the name and address in the computer of the :ref:`function<what is a function?>` it receives.

* I change the name of the input parameter to make it clearer

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-2

    def an_exception_handler(a_function):
        return a_function
        return 'failed'

* I make ``an_exception_handler`` return the result of a :ref:`call<how to call a function with input>` to its input

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def an_exception_handler(a_function):
        return a_function()
        return 'failed'

  the terminal_ is my friend, and shows :ref:`Exception<how to test that an Exception is raised>` and :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    FAILED ...test_catching_failure -
        Exception: BOOM!!!
    FAILED ...test_catching_success -
        AssertionError: None != 'succeeded'

  because if ``an_exception_handler`` is :ref:`called<how to call a function with input>`, it :ref:`calls<how to call a function with input>` the input it receives

  * If the :ref:`call<how to call a function with input>` to its input :ref:`raises an Exception<how to raise an Exception>`, the program_ stops

    .. code-block:: shell

      src.exceptions.an_exception_handler(
          src.exceptions.raise_exception
      )
      └── def an_exception_handler(a_function):
          └── return a_function()
              └── def raise_exception():
                  └── raise Exception('BOOM!!!')

  * If the :ref:`call<how to call a function with input>` to its input does NOT :ref:`raise an Exception<how to raise an Exception>`, it returns the result of the :ref:`call<how to call a function with input>` to its input

    .. code-block:: shell

      src.exceptions.an_exception_handler(
          src.exceptions.function_name
      )
      └── def an_exception_handler(a_function):
          └── return a_function()
              └── def function_name():
                  └── return None

* I add a :ref:`try statement<how to handle Exceptions>` to ``an_exception_handler`` to make it choose what to do if an :ref:`Exception is raised<how to raise an Exception>`,  in ``src/exceptions/__init__.py``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2-5

    def an_exception_handler(a_function):
        try:
            return a_function()
        except Exception:
            return 'failed'

  :ref:`test_catching_failure` passes. The terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` for :ref:`test_catching_success`

  .. code-block:: shell

    AssertionError: None != 'succeeded'

  because ``an_exception_handler`` returns the result of :ref:`calling<how to call a function with input>` the ``function_name`` :ref:`function<what is a function?>` which is :ref:`None<what is None?>`.

* I add :ref:`else to the try statement<how to use try...except...else>` for if ``a_function()`` runs and does NOT :ref:`raise an Exception<how to raise an Exception>`, to make it clearer

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 6-7

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return None

  the terminal_ still shows :ref:`AssertionError<what causes AssertionError?>`.

* I change the :ref:`return statement<the return statement>` in the `else clause`_ to give the test what it wants

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 7

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the test passes.

* I can be more :ref:`explicit with the Exception<test_catching_exceptions>` in the :ref:`except<how to handle Exceptions>` block

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4-5

    def an_exception_handler(a_function):
        try:
            a_function()
        # except Exception:
        except ModuleNotFoundError:
            return 'failed'
        else:
            return 'succeeded'

  the terminal_ is my friend, and shows :ref:`Exception<how to test that an Exception is raised>` for ``test_catching_failure``

  .. code-block:: shell

    Exception: BOOM!!!

  because :ref:`Exception<how to test that an Exception is raised>` is not :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` and I cannot use a :ref:`child<how to test if something is a subclass>` :ref:`Exceptions<how to test that an Exception is raised>` to catch its parent :ref:`Exception<how to test that an Exception is raised>`.

  The :ref:`try statement<how to handle Exceptions>` only catches the :ref:`Exception<how to test that an Exception is raised>` given in the :ref:`except<how to handle Exceptions>` clause and its :ref:`children (subclasses)<how to test if something is a subclass>`, all other :ref:`Exceptions are raised<how to raise an Exception>`.

* I change it back to what works

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 4

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the test is green again!

* I add a git_ commit message

  .. code-block:: python
    :emphasize-lines:

    git commit -am 'add test_catching_success'

----

The :ref:`try statement<how to handle Exceptions>` is used to :ref:`catch or handle Exceptions<how to handle Exceptions>` in Python_. It allows the program_ to choose what to do if it runs into an :ref:`Exception<how to test that an Exception is raised>`. I think of it as

- ``try`` **something**
- ``except Exception`` - if **something** raises :ref:`Exception<how to test that an Exception is raised>`, run the code in this block
- ``else`` - **something** does NOT raise :ref:`Exception<how to test that an Exception is raised>`, run the code in this block

In this case

- ``try`` **a_function()**

  .. code-block:: shell

    def an_exception_handler(a_function):
    └── try:
        └── a_function()
        ...

- ``except Exception`` - if **a_function()** :ref:`raises Exception<how to raise an Exception>` return ``'failed'``

  .. code-block:: shell

      src.exceptions.an_exception_handler(
          src.exceptions.raise_exception
      )
      └── def an_exception_handler(a_function):
          └── try:
              └── a_function()
                  └── def raise_exception():
          ┌───────────┴── raise Exception('BOOM!!!')
          └── except Exception:
              └── return 'failed'
              else:
                  return 'succeeded'

- ``else`` - if **a_function()** does NOT :ref:`raise Exception<how to raise an Exception>` return ``'succeeded'``

  .. code-block:: shell

    src.exceptions.an_exception_handler(
        src.exceptions.function_name
    )
    └── def an_exception_handler(a_function):
        └── try:
        ┌───┴── a_function()
        │       └── def function_name():
        │           └── return None
        │   except Exception:
        │       return 'failed'
        └── else:
            └── return 'succeeded'

The :ref:`try statement<how to handle Exceptions>` is how I think of `Test Driven Development`_ or the scientific method

-  Try something
-  if it fails, try something else
-  do this as many times as you can until you get what you want

or in the words of a famous singer ...

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``src/exceptions/__init__.py`` and ``tests/test_exceptions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.
* I `change directory`_ to the parent of ``exceptions``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that

* I can use assertRaisesRegex_ to catch :ref:`Exceptions<how to test that an Exception is raised>` with messages.
* I can use :ref:`try..except...else<how to use try...except...else>` to make programs that can choose what to do when :ref:`Exceptions are raised<how to raise an Exception>`.

----

:ref:`How many questions can you answer after going through this chapter?<questions about testing Exceptions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<Exception Handling in programs tests and solutions>`

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
* :ref:`I know how Python groups objects into False or True<what are booleans?>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically<how to make a Python Test Driven Development environment automatically>`.
* :ref:`I know how to write programs that make decisions<truth table>`.
* :ref:`I know how to make a Python Test Driven Development environment automatically with variables<how to make a Python Test Driven Development environment automatically with variables>`.
* :ref:`I know how to make a person with Exceptions<how to make a person with Exceptions>`.
* :ref:`I know how to test that an Exception is raised<how to test that an Exception is raised>`.
* :ref:`I know how to use Exception handlers in programs<how to handle Exceptions in programs>`.

:ref:`Would you like to test making a Person with loops?<how to make a person with loops>`

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