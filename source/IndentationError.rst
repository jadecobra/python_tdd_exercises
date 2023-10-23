IndentationError
================

In the beginning of our journey with python we will make many mistakes, one of which will cause the ``(IndentationError)`` if we do not understand the indentation rules of python. We will step through solving this error in python using Test Driven Development

Prerequisites
-------------


* `How I setup a Test Driven Development Environment.md <./How I How I setup a Test Driven Development Environment.md.md>`_

----

Indentation Matters
-------------------

Spacing/Indentation matters in python. Where you place code and how you space them out have an effect on how the code is interpreted as well as how a human being comprehends your intention. Some people indent with 2 spaces, others indent with 4. In this exercise we will indent with 4 as that is the `recommended convention <https://peps.python.org/pep-0008/#indentation>`_

Solve the IndentationError
--------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


*
  Open a new file in the editor and save it as ``tests/test_indentation_error.py`` in the ``(tests)`` folder you created in `How I setup a Test Driven Development Environment.md <./How I How I setup a Test Driven Development Environment.md.md>`_\ , then type the following lines in the file *paying attention to the spacing*

  .. code-block:: python

       'a'
        'b'

    the terminal updates to show

  .. code-block:: shell

       E       'b'
       E   IndentationError: unexpected indent

    add ``(IndentationError)`` to the running list of Exceptions encountered

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # IndentationError

    python raises an ``(IndentationError)`` for line 2 because it was not expecting the indentation there. Indentation has meaning in python and in this case it does not meet the predefined rules for indentation

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``test_indentation_error.py`` by making the lines match up in spacing
  .. code-block:: python

       'a'
       'b'
    the terminal updates to show passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

let us add more indentation errors to ``test_indentation_error.py``

.. code-block:: python

   'a'
   'b'
       'c'
               'd'

The terminal updates to show

.. code-block:: shell

   E       'c'
   E   IndentationError: unexpected indent

fix the offending lines until all tests are green.

Solve the IndentationError for functions
----------------------------------------

let us add more tests, this time indentation errors with functions *noting the difference in spacing*

RED: make it fail
^^^^^^^^^^^^^^^^^


*
  add the `functions <./FUNCTIONS.md>`_ below to ``test_indentation_error.py``

  .. code-block:: python

       def function():
       pass

           def function():
           pass

        def function():
           pass

         def function():
           pass

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


*
  update ``test_indentation_error.py`` to make the spacing/indentation match for each function

  .. code-block:: python

       def function():
           pass

       def function():
           pass

       def function():
           pass

       def function():
           pass

    all the tests pass

Solve the IndentationError in Classes
-------------------------------------

let us add more tests, this time to raise indentation errors for `Class <./CLASSES.md>`_ definitions *noting the difference in spacing*

RED: make it fail
^^^^^^^^^^^^^^^^^


*
  update ``test_indentation_error.py``

  .. code-block:: python

       class Class():
       pass

       class Class():
            pass

           class Class():
                   pass

    the terminal will update to show an ``(IndentationError)`` and the offending line

  .. code-block:: shell

       E    IndentationError: expected an indented block after class definition on line 18

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


*
  update ``test_indentation_error.py`` to make the spacing/indentation match

  .. code-block:: python

       class Class():
           pass

       class Class():
           pass

       class Class():
           pass

Solve the IndentationError in Classes with Methods
--------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


*
  building on what we have done so far, we will add failing tests for `methods <./CLASSES.md>`_\ , update ``test_indentation_error.py``

  .. code-block:: python

       class Class():
            def method():
           return

       class Class():
            def method():
                return

       class Class():
        def method():
            return

    the terminal displays an IndentationError and the line that caused the exception

  .. code-block:: shell

       E    IndentationError: expected an indented block after function definition on line 28

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


*
  update ``test_indentation_error.py`` to make the spacing/indentation match

  .. code-block:: python

       class Class():
           def method():
               return

       class Class():
           def method():
               return

       class Class():
           def method():
               return

Solve the IndentationError in Classes with Attributes
-----------------------------------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


* update ``test_indentation_error.py``
  .. code-block:: python

       class Class():
        attribute = None
         attribute = None
              attribute = None
          attribute = None
    the terminal will update to show an IndentationError and the offending line
  .. code-block:: shell

       E    IndentationError: unexpected indent

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``test_indentation_error.py`` to make the spacing/indentation match
  .. code-block:: python

       class Class():
           attribute = None
           attribute = None
           attribute = None
           attribute = None

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

The point of this exercise was to get familiar with python spacing convention to help understand the ``(IndentationError)`` and its solution.

Indentation matters in python because it is how blocks of code are segmented. When a `function <./FUNCTIONS.md>`_ is defined, all the statements that belong to the it are indented, same with a `class <./CLASSES.md>`_\ , all the statements that belong to the it, its methods and attributes are indented underneath it.

This helps with reading the code so we can tell what belongs to a namespace the same way curly braces do for languages that use them for that purpose. Interactive Development Environments have gotten a lot better and automatically indent code for you using the convention of the language you are writing, which saves time spent counting the number of spaces to indent.
