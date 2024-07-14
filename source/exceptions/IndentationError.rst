.. include:: ../links.rst

IndentationError
================

----

.. contents:: table of contents
  :local:
  :depth: 1

----

Spacing/Indentation matters in Python. Where code is placed and how it is spaced has an effect on how the code is interpreted as well as how a human being comprehends the intention behind the code. Some people indent with 2 spaces, others indent with 4. This exercises uses 4 spaces to indent as it is the `recommended convention <https://peps.python.org/pep-0008/#indentation>`_

An `IndentationError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#IndentationError>`_ is raised when indentation is not right. The exercises in this chapter are intended to get you familiar with proper Indentation

****************
requirements
****************


:doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`

----

Solve the IndentationError
--------------------------

red: make it fail
^^^^^^^^^^^^^^^^^


* Open a new file in the editor and save it as ``tests/test_indentation_error.py`` in the ``tests`` folder you made in :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>`\ , then type the following lines in the file *paying attention to the spacing*

  .. code-block:: python

    'a'
     'b'

  the terminal shows

  .. code-block:: python

    E    'b'
    E  IndentationError: unexpected indent

  add ``IndentationError`` to the list of :ref:`Exceptions<Exceptions>` encountered

  .. code-block:: python

    # Exceptions Encountered
    # AssertionError
    # IndentationError

 Python raises an ``IndentationError`` for line 2 because it was not expecting the indentation there. Indentation has meaning in Python and in this case it does not meet the predefined rules for indentation

green: make it pass
^^^^^^^^^^^^^^^^^^^


* change ``test_indentation_error.py`` by making the lines match up in spacing

  .. code-block:: python

    'a'
    'b'

  the terminal shows passing tests

refactor: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

add more indentation errors to ``test_indentation_error.py``

.. code-block:: python

  'a'
  'b'
    'c'
       'd'

The terminal shows

.. code-block:: python

  E    'c'
  E  IndentationError: unexpected indent

fix the offending lines until all tests are green.

Solve the IndentationError for functions
----------------------------------------

add more tests, this time indentation errors with functions *noting the difference in spacing*

red: make it fail
^^^^^^^^^^^^^^^^^


* add the :doc:`/functions/functions` below to ``test_indentation_error.py``

  .. code-block:: python

    def function():
    pass

      def function():
      pass

     def function():
       pass

    def function():
     pass

green: make it pass
^^^^^^^^^^^^^^^^^^^


* change ``test_indentation_error.py`` to make the spacing/indentation match for each function

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

add more tests, this time to raise indentation errors for :ref:`classes` definitions *noting the difference in spacing*

red: make it fail
^^^^^^^^^^^^^^^^^

*
  change ``test_indentation_error.py``

  .. code-block:: python

    class Class():
    pass

    class Class():
       pass

      class Class():
         pass

  the terminal shows an ``IndentationError`` and the offending line

  .. code-block:: python

    E  IndentationError: expected an indented block after class definition on line 18

green: make it pass
^^^^^^^^^^^^^^^^^^^


* change ``test_indentation_error.py`` to make the spacing/indentation match

  .. code-block:: python

    class Class():
        pass

    class Class():
        pass

    class Class():
        pass

Solve the IndentationError in Classes with Methods
--------------------------------------------------

red: make it fail
^^^^^^^^^^^^^^^^^


* building on the previous tests, add failing tests for :ref:`methods<functions>` , to ``test_indentation_error.py``

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

  the terminal shows an IndentationError and the line that caused the exception

  .. code-block:: python

    E  IndentationError: expected an indented block after function definition on line 28

green: make it pass
^^^^^^^^^^^^^^^^^^^


* change ``test_indentation_error.py`` to make the spacing/indentation match

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

red: make it fail
^^^^^^^^^^^^^^^^^


* change ``test_indentation_error.py``

  .. code-block:: python

    class Class():
    attribute = None
     attribute = None
       attribute = None
      attribute = None

  the terminal shows an IndentationError and the offending line

  .. code-block:: python

    E  IndentationError: unexpected indent

green: make it pass
^^^^^^^^^^^^^^^^^^^


* change ``test_indentation_error.py`` to make the spacing/indentation match

  .. code-block:: python

    class Class():
        attribute = None
        attribute = None
        attribute = None
        attribute = None

refactor: make it better
^^^^^^^^^^^^^^^^^^^^^^^^

Indentation matters in Python because it is how blocks of code are segmented. When a :ref:`function<functions>` is defined, all the statements that belong to it are indented, same with a :ref:`class <classes>`, all the :ref:`methods<functions>` and attributes that belong to it are indented underneath the definition

This helps with reading the code so I can tell what belongs to a namespace the same way curly braces do for languages that use them for that purpose.

Integrated Development Environments have gotten a lot better and automatically indent code for you using the convention of the language you are writing, which saves time spent counting the number of spaces to indent
