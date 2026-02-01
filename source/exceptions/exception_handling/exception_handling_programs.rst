.. meta::
  :description: Master Python exception handling with try-except-else. Learn to catch specific errors, handle multiple exceptions, and write robust code. Watch the tutorial.
  :keywords: Jacob Itegboje, python exception handling tutorial for beginners, python try except else explained, how to handle multiple exceptions in python, python assert_raises_regex example, python custom exception best practices, python exception handling real world example, python unittest exception handling, python clean error handling

.. include:: ../../links.rst

#################################################################################
how to handle Exceptions (Errors) in programs
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/xjfTE33FZyM?si=QGhkDEvHmMaJKLXB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

*********************************************************************************
preview
*********************************************************************************

These are the tests I have by the end of the chapter

.. literalinclude:: ../../code/tests/test_exceptions.py
  :language: python
  :linenos:

----

*********************************************************************************
questions about handling Exceptions
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`how can I make sure an Exception is raised?<how to test that an Exception is raised>`
* :ref:`what causes ModuleNotFoundError?<test_catching_module_not_found_error_in_tests>`
* :ref:`what causes NameError?<test_catching_name_error_in_tests>`
* :ref:`what causes AttributeError?<test_catching_attribute_error_in_tests>`
* :ref:`what causes TypeError?<test_catching_type_error_in_tests>`
* :ref:`what causes IndexError?<test_catching_index_error_in_tests>`
* :ref:`what causes KeyError?<test_catching_key_error_in_tests>`
* :ref:`what causes ZeroDivisionError?<test_catching_zero_division_error_in_tests>`
* :ref:`what Exception do all the other Exceptions come from<test_catching_exceptions_in_tests>`
* :ref:`how can I test an Exception with a specific message<test_catching_exceptions_w_messages>`
* :ref:`How can a program handle an Exception so it does not stop when one is raised?<how to use try...except...else>`

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`how to test that an Exception is raised`

----

=================================================================================
open the project
=================================================================================

----

* I `change directory`_ to the ``exceptions`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd exceptions

  the terminal_ shows I am in the ``exceptions`` folder_

  .. code-block:: shell

    .../pumping_python/exceptions

* I activate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    source .venv/bin/activate

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``.venv/bin/activate.ps1`` NOT ``source .venv/bin/activate``

    .. code-block:: shell
      :emphasize-lines: 1

      .venv/scripts/activate.ps1

  the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/exceptions

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher --now --delay 0 .

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/exceptions
    configfile: pyproject.toml
    collected 8 items

    tests/test_exceptions.py ....                                        [100%]

    ======================== 8 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_exceptions.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_catching_exceptions_w_messages
*********************************************************************************

I can use the `assertRaisesRegex method`_ to test the message that is included with an :ref:`Exception<errors>`, this helps me to tell the difference when I have two :ref:`Exceptions<errors>` that have the same name

* I add a failing test to ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 38
    :emphasize-lines: 5-6

        def test_catching_exceptions_in_tests(self):
            with self.assertRaises(Exception):
                raise Exception

        def test_catching_exceptions_w_messages(self):
            src.exceptions.raise_exception()

  the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: shell

    AttributeError: module 'src.exceptions' has no attribute 'raise_exception'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``exceptions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def function_name():
        return None


    raise_exception

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'raise_exception' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1

    raise_exception = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* when I make ``raise_exception`` a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 1-2

    def raise_exception():
        return None

  the test passes

* I want the :ref:`function<what is a function?>` to raise :ref:`Exception<errors>` when it is called, I add assertRaises_ to the test in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2-3

        def test_catching_exceptions_w_messages(self):
            with self.assertRaises(Exception):
                src.exceptions.raise_exception()

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: Exception not raised

* I add a `raise statement`_ to the ``raise_exception`` :ref:`function<what is a function?>` in ``exceptions.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def raise_exception():
        raise Exception

  the test passes

* I can be more specific when testing for an :ref:`Exception<errors>`, I add assertRaisesRegex_ in ``test_exceptions.py``

  .. code-block:: python
    :lineno-start: 42
    :emphasize-lines: 2-4

        def test_catching_exceptions_w_messages(self):
            with self.assertRaisesRegex(
                Exception, 'BOOM!!!'
            ):
                src.exceptions.raise_exception()

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: "BOOM!!!" does not match ""

  the `assertRaisesRegex method`_ checks that the code in its context raises_ the :ref:`Exception<errors>` it is given, with the message it is given. The default message of the :ref:`Exception<errors>` is the empty string_ (``''``) and the test expects ``"BOOM!!!"``

* the :ref:`Exception<errors>` is right, the message is not, I add the expected message in ``exceptions.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 2

    def raise_exception():
        raise Exception('BOOM!!!')

  the test passes. Time to add an :ref:`Exception<errors>` to the program

----

*********************************************************************************
test_catching_failure
*********************************************************************************


----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new failing test in ``test_exceptions.py``

.. code-block:: python
  :lineno-start: 42
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

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block::

  AttributeError: module 'src.exceptions' has no attribute 'an_exception_handler'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``exceptions.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5

    def raise_exception():
        raise Exception('BOOM!!!')


    an_exception_handler

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'an_exception_handler' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    an_exception_handler = None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: 'NoneType' object is not callable

* I make it a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-2

    def an_exception_handler():
        return None

  the terminal_ shows :ref:`TypeError`

  .. code-block:: shell

    TypeError: an_exception_handler() takes 0 positional arguments but 1 was given

* I make the :ref:`function<what is a function?>` take input

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    def an_exception_handler(the_input):
        return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 'failed'

  the result of the call to ``src.exceptions.an_exception_handler`` is :ref:`None<what is None?>` and the test expects ``'failed'``

* I change the `return statement`_ to match the expectation

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 2

    def an_exception_handler(the_input):
        return 'failed'

  the test passes.

----

*********************************************************************************
test_catching_success
*********************************************************************************

I want ``an_exception_handler`` to process its input and return ``failed`` when an :ref:`Exception<errors>` happens or return ``success`` when an :ref:`Exception<errors>` is NOT raised.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test to ``test_exceptions.py``

.. code-block:: python
  :lineno-start: 48
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
                    src.exceptions.does_not_raise_exception
                ),
                'succeeded'
            )

the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: shell

  AttributeError: module 'src.exceptions' has no attribute 'does_not_raise_exception'

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``exceptions.py``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5

    def raise_exception():
        raise Exception('BOOM!!!')


    does_not_raise_exception


    def an_exception_handler(the_input):
        return 'failed'

  the terminal_ shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: shell

    NameError: name 'does_not_raise_exception' is not defined

* I point it to :ref:`None<what is None?>` to define it

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1

    does_not_raise_exception = None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block::

    AssertionError: 'failed' != 'succeeded'

  ``src.exceptions.an_exception_handler`` still returns ``'failed'``, the test expects ``'succeeded'``

* I make ``an_exception_handler``, remember the :ref:`identity function<test_identity_function>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

    does_not_raise_exception = None


    def an_exception_handler(the_input):
        return the_input
        return 'failed'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    ...::test_catching_failure - AssertionError: <function raise_exception at 0xabcd12e34567> != 'failed'
    ...::TestExceptions::test_catching_success - AssertionError: None != 'succeeded'

  - ``test_catching_failure`` fails because ``an_exception_handler`` returns the name (``raise_exception``) and address in the computer(``0xabcd12e34567``) of the :ref:`function<what is a function?>` it gets
  - ``test_catching_success`` fails because ``an_exception_handler`` returns ``does_not_raise_exception`` which points to :ref:`None<what is None?>`

* I change the name of the input parameter to be clearer

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 1-2

    def an_exception_handler(a_function):
        return a_function
        return 'failed'

* I make ``an_exception_handler`` return the result of a call to its input as a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 12
    :emphasize-lines: 2

    def an_exception_handler(a_function):
        return a_function()
        return 'failed'

  the terminal_ shows :ref:`TypeError`

  .. code-block:: python

    a_function = None

        def an_exception_handler(a_function):
    >       return a_function()
    E       TypeError: 'NoneType' object is not callable

  because ``does_not_raise_exception`` points to :ref:`None<what is None?>`, which is not callable_

* I make it a :ref:`function<what is a function?>` to make it callable_

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 1-2

    def does_not_raise_exception():
        return None


    def an_exception_handler(a_function):
        return a_function()
        return 'failed'

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: None != 'succeeded'

  the result of calling ``src.exceptions.raise_exception`` in ``test_catching_failure`` is an :ref:`Exception<errors>` with a message

  .. code-block:: python

    Exception: 'BOOM!!!'

I need a way for the :ref:`function<what is a function?>` to choose what to do when an :ref:`Exception<errors>` is raised and when one is NOT raised. I can use the `try statement`_ to do this

---------------------------------------------------------------------------------
how to use try...except...else
---------------------------------------------------------------------------------

* I add a `try statement`_ to ``an_exception_handler`` in ``exceptions.py``

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 2-5

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'

  ``test_catching_failure`` passes. The terminal_ still shows :ref:`AssertionError<what causes AssertionError?>` for ``test_catching_success``

  .. code-block:: shell

    AssertionError: None != 'succeeded'

  the `try statement`_ is used to handle :ref:`Exceptions<errors>` in programs

* I add an `else clause`_ for when ``a_function()`` runs without raising an :ref:`Exception<errors>`

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 6-7

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return None

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell

    AssertionError: None != 'succeeded'

  this is still the same :ref:`Exception<errors>` and message

* I change the `return statement`_ in the `else clause`_

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 7

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the test passes.

  The `try statement`_ is used to catch or handle :ref:`Exceptions<errors>` in Python_. It allows the program_ to choose what to do when it runs into an :ref:`Exception<errors>`. I think of it as

  - ``try`` running **this**
  - ``except Exception`` - when running **this** raises ``Exception``, run the code in this block
  - ``else`` - when running **this** does NOT raise ``Exception``, run the code in this block

  In this case

  - ``try`` **calling** ``a_function()``
  - ``except Exception`` - when **calling** ``a_function()`` raises ``Exception`` return ``'failed'``
  - ``else`` - when **calling** ``a_function()`` does NOT raise ``Exception`` return ``'succeeded'``

  the `try statement`_ is how I think of `Test Driven Development`_ or the scientific method

  -  Try something
  -  if it fails, try something else
  -  do this as many times as you can until you get what you want

  or in the words of a famous singer ...

* I can be more specific with the :ref:`Exception<errors>` in the ``except`` block, for example

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

    def an_exception_handler(a_function):
        try:
            a_function()
        except ModuleNotFoundError:
            return 'failed'
        else:
            return 'succeeded'

  the terminal_ shows :ref:`Exception<errors>` for ``test_catching_failures``

  .. code-block:: shell

    Exception: BOOM!!!!

  because :ref:`Exception<errors>` is not :ref:`ModuleNotFoundError<what is a module?>`. The `try statement`_ only catches the :ref:`Exception<errors>` given in the ``except`` block and its children, all others are raised

* I change it back to what works

  .. code-block:: python
    :lineno-start: 13
    :emphasize-lines: 4

    def an_exception_handler(a_function):
        try:
            a_function()
        except Exception:
            return 'failed'
        else:
            return 'succeeded'

  the terminal_ shows green again! I know :ref:`how to test that an Exception is raised` and :ref:`how to handle Exceptions (Errors) in programs`. I am a master!!

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``exceptions.py`` and ``test_exceptions.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`ctrl+c` on the keyboard to leave the tests, the terminal_ shows

  .. code-block:: shell

    (.venv) .../pumping_python/exceptions

* I deactivate the `virtual environment`_

  .. code-block:: shell
    :emphasize-lines: 1

    deactivate

  the terminal_ goes back to the command line, ``(.venv)`` is no longer on the left side

  .. code-block:: shell

    .../pumping_python/exceptions

* I `change directory`_ to the parent of ``exceptions``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_

----

*********************************************************************************
review
*********************************************************************************

I ran tests to show that

* I can cause any :ref:`Exception<errors>` I want with the raise_ keyword
* I can use the `assertRaises method`_ to catch :ref:`Exceptions<errors>` in tests and tested the following

  - :ref:`ModuleNotFoundError<what is a module?>`
  - :ref:`NameError<test_catching_name_error_in_tests>`
  - :ref:`AttributeError<what causes AttributeError?>`
  - :ref:`TypeError`
  - :ref:`IndexError<test_index_error>`
  - :ref:`KeyError<test_key_error>`
  - :ref:`ZeroDivisionError<test_catching_zero_division_error_in_tests>`
  - :ref:`The Mother of all Exceptions<test_catching_exceptions_in_tests>`

* I can use assertRaisesRegex_ to catch :ref:`Exceptions<errors>` with messages
* I can use :ref:`try..except...else<how to use try...except...else>` to make programs that can choose what to do when :ref:`Exceptions<errors>` are raised

----

:ref:`How many questions can you answer after going through this chapter?<questions about handling Exceptions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to handle Exceptions (Errors): tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`what causes AttributeError<what causes AttributeError?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to make a Python Test Driven Development environment automatically` or :ref:`how to make a Python Test Driven Development environment automatically on Windows without Windows Subsystem for Linux`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`

:ref:`Would you like to handle ZeroDivisionError in the Calculator?<how to make a calculator 2>`

-----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->