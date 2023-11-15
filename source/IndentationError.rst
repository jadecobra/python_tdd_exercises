IndentationError
================

Spacing/Indentation matters in python. Where code is placed and how it is spaced has an effect on how the code is interpreted as well as how a human being comprehends the intention behind the code. Some people indent with 2 spaces, others indent with 4. This exercises uses 4 spaces to indent as it is the `recommended convention <https://peps.python.org/pep-0008/#indentation>`_

An `<https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndentationError>`_ is raised when indentation is not correct

The exercises in this chapter are intended to get you familiar with proper Inden



Prerequisites
-------------

:doc:`How to Setup a Test Driven Development Environment`

----


Solve the IndentationError
--------------------------

RED: make it fail
^^^^^^^^^^^^^^^^^


* Open a new file in the editor and save it as ``tests/test_indentation_error.py`` in the ``tests`` folder you created in :doc:`How to Setup a Test Driven Development Environment`\ , then type the following lines in the file *paying attention to the spacing*

  .. code-block:: python

       'a'
        'b'

    the terminal updates to show

  .. code-block:: python

       E       'b'
       E   IndentationError: unexpected indent

    add ``IndentationError`` to the running list of Exceptions encountered

  .. code-block:: python

       # Exceptions Encountered
       # AssertionError
       # IndentationError

    python raises an ``IndentationError`` for line 2 because it was not expecting the indentation there. Indentation has meaning in python and in this case it does not meet the predefined rules for indentation

GREEN: make it pass
^^^^^^^^^^^^^^^^^^^


* update ``test_indentation_error.py`` by making the lines match up in spacing
  .. code-block:: python

       'a'
       'b'
    the terminal updates to show passing tests

REFACTOR: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

add more indentation errors to ``test_indentation_error.py``

.. code-block:: python

   'a'
   'b'
       'c'
               'd'

The terminal updates to show

.. code-block:: python

   E       'c'
   E   IndentationError: unexpected indent

fix the offending lines until all tests are green.

Solve the IndentationError for functions
----------------------------------------

add more tests, this time indentation errors with functions *noting the difference in spacing*

RED: make it fail
^^^^^^^^^^^^^^^^^


*
  add the :doc:`functions` below to ``test_indentation_error.py``

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

add more tests, this time to raise indentation errors for :doc:`Class` definitions *noting the difference in spacing*

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

    the terminal shows an ``IndentationError`` and the offending line

  .. code-block:: python

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
  building on what I have done so far, I will add failing tests for :doc:`methods`\ , update ``test_indentation_error.py``

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

  .. code-block:: python

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
    the terminal shows an IndentationError and the offending line
  .. code-block:: python

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

The point of this exercise was to get familiar with python spacing convention to help understand the ``IndentationError`` and its solution.

Indentation matters in python because it is how blocks of code are segmented. Whena :doc:`functions` is defined, all the statements that belong to the it are indented, same witha :doc:`class`\ , all the statements that belong to the it, its :doc:`methods <functions>` and attributes are indented underneath it.

This helps with reading the code so I can tell what belongs to a namespace the same way curly braces do for languages that use them for that purpose. Interactive Development Environments have gotten a lot better and automatically indent code for you using the convention of the language you are writing, which saves time spent counting the number of spaces to indent.
