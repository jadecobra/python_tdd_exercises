.. meta::
   :description: Learn Python functions with TDD! Explore arguments, defaults, and testing techniques in this practical guide. Start coding now!
   :keywords: Jacob Itegboje, Python functions, Test-Driven Development, Python programming, keyword arguments, positional arguments, coding tutorial

.. include:: ../links.rst

.. _function: https://docs.python.org/3/glossary.html#term-function
.. _functions: :ref:`function<what is a function?>`
.. _argument: https://docs.python.org/3/glossary.html#term-argument
.. _arguments: argument_
.. _keyword arguments: arguments_
.. _positional arguments: arguments_

#################################################################################
functions 2
#################################################################################

Since I know how to use :ref:`variables<what is a variable?>`, I can do better with the results of :ref:`test_why_use_a_function`

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``functions`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: shell

    .../pumping_python/functions

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher --now --delay 0 .

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    rootdir: .../pumping_python/functions
    configfile: pyproject.toml
    collected 12 items

    tests/test_functions.py ............                          [100%]

    ======================= 12 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_functions.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
a better way to handle the results changing
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I add 2 :ref:`variables<what is a variable?>` to :ref:`test_why_use_a_function`

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 5-6

        def test_why_use_a_function(self):
            def add_x(x=3, y=0):
                return x + y

            x = 3
            y = 0
            self.assertEqual(add_x(y=0), 3)

* I use the :ref:`variables<what is a variable?>` in the :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 3-4

            x = 3
            y = 0
            # self.assertEqual(add_x(y=0), 3)
            self.assertEqual(add_x(x, y), x+x)
            self.assertEqual(add_x(y=1), 4)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 3 != 6

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change the expectation

.. code-block:: python
  :lineno-start: 14
  :emphasize-lines: 4

            x = 3
            y = 0
            # self.assertEqual(add_x(y=0), 3)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=1), 4)

the test passes

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the comment then do the same thing for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 11
    :emphasize-lines: 4-6

            x = 3
            y = 0
            self.assertEqual(add_x(x, y), x+y)
            y = 1
            # self.assertEqual(add_x(y=1), 4)
            self.assertEqual(add_x(x, y), x+x)
            self.assertEqual(add_x(y=2), 5)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 4 != 6

* I change the expectation

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3

            y = 1
            # self.assertEqual(add_x(y=1), 4)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=2), 5)

  the test passes. Wait a minute, ``self.assertEqual(add_x(x, y), x+y)`` is also a repetition!

* I remove the commented line then add a :ref:`variable<what is a variable?>` for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 3-5

            y = 1
            self.assertEqual(add_x(x, y), x+y)
            y = 2
            # self.assertEqual(add_x(y=2), 5)
            self.assertEqual(add_x(x, y), y+y)
            self.assertEqual(add_x(y=3), 6)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 5 != 4

* I change the expectation to the right calculation

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3

            y = 2
            # self.assertEqual(add_x(y=2), 5)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=3), 6)

  the test passes, this is the same as the :ref:`add function<test_addition>` from :ref:`how to make a calculator<how to make a calculator 1>`

* I remove the comment, then add a :ref:`variable<what is a variable?>` for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 16
    :emphasize-lines: 3-5

            y = 2
            self.assertEqual(add_x(x, y), x+y)
            y = 3
            # self.assertEqual(add_x(y=3), 6)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=4), 7)

  the test is still green because ``x`` and ``y`` are both ``3``

* on to the next one

  .. code-block:: python
    :lineno-start: 18
    :emphasize-lines: 3-5

            y = 3
            self.assertEqual(add_x(x, y), x+y)
            y = 4
            # self.assertEqual(add_x(y=4), 7)
            self.assertEqual(add_x(x, y), y+y)
            self.assertEqual(add_x(y=5), 8)

  the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: 7 != 8

* I change the expectation

  .. code-block:: python
    :lineno-start: 20

            y = 4
            # self.assertEqual(add_x(y=4), 7)
            self.assertEqual(add_x(x, y), x+y)
            self.assertEqual(add_x(y=5), 8)

  the test passes



:ref:`I can use a variable to remove duplication<what is a variable?>`

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py`` in the :ref:`editor<2 editors>`
* I click in the terminal_ and use :kbd:`q` on the keyboard to leave the tests and the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python/functions (main)

* I `change directory`_ to the parent of ``functions``

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

I ran tests to show that I can make functions_ with

* the def_ keyword
* :ref:`positional arguments<test_functions_w_positional_arguments>`
* :ref:`keyword arguments<test_functions_w_keyword_arguments>`
* :ref:`positional and keyword arguments<test_functions_w_positional_and_keyword_arguments>`
* :ref:`default values<test_functions_w_default_arguments>`
* :ref:`can take any number of inputs<test_functions_w_unknown_arguments>`

as a reminder

* :ref:`I can use '*args' when I do not know how many positional arguments the function has to take<test_functions_w_unknown_arguments>`
* :ref:`positional arguments are taken as a tuple<how Python reads positional arguments>`
* :ref:`positional arguments must come before keyword arguments<test_functions_w_default_arguments>`
* :ref:`I can use '**kwargs' when I do not know how many keyword arguments the function<test_functions_w_unknown_arguments>`
* :ref:`keyword arguments are taken as a dictionary<how Python reads keyword arguments>`
* :ref:`the identity function returns its input<test_identity_function>`
* :ref:`constant functions always return the same thing<test_constant_function>`
* :ref:`nothing runs after the return statement in a function<test_what_happens_after_a_function_returns>`
* :ref:`functions return None by default<test_making_a_function_w_return_none>`

:ref:`How many questions can you answer about functions?<questions about functions>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<functions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have covered a bit so far and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>` and
* :ref:`how to make functions<what is a function?>`

:ref:`Would you like to know what causes AttributeError?<what causes AttributeError?>`

----

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