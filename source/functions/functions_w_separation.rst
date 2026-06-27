.. meta::
  :description: Master Python functions step-by-step using Test-Driven Development (TDD) with functions. Learn how to make functions take input with def, identity function, positional vs keyword arguments (order independence with names), default/optional values, *args and **kwargs, argument unpacking (*tuple **dict), return statements. See real errors: "NameError: name 'identity' is not defined", "TypeError: ... takes 0 positional arguments but 1 was given", "takes 1 positional argument but 2 were given", AssertionError on wrong returns. Practice bare assert == / is, constant functions "assert constant() == 'the same thing'", swapping calls like keyword(last_input=0, first_input=1) == (1, 0), unknown_number_of_arguments(*a_tuple, **a_dictionary) == (tuple, dict). Part of Jacob Itegboje's Pumping Python TDD series for beginners.
  :keywords: Jacob Itegboje, Pumping Python, Python functions for beginners, learn Python functions with TDD, positional vs keyword arguments Python, keyword_arguments, what does a function return by default, Python *args **kwargs, optional arguments default value, test identity function return the_input, "takes 0 positional arguments but 1 was given", "NameError: name 'identity' is not defined", constant function "the same thing", argument unpacking python, bare assert in tests, functions that take input, red green refactor functions, Python TDD positional keyword, how to call python function with input, return first_input last_input tuple

.. include:: ../links.rst

#################################################################################
separate and equal functions
#################################################################################

All the :ref:`functions<what is a function?>` in :ref:`the functions project<what is a function?>` were written in ``test_functions.py``. I want to move them to ``functions.py`` in the ``src`` folder_ so that I can keep the tests and solutions separate like I did with the other projects.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/functions/tests/test_functions_separate_and_equal.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd functions

  the terminal_ shows I am in the ``functions`` folder_

  .. code-block:: python

    .../pumping_python/functions

* I open ``test_functions.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_functions.py ............                      [100%]



    =================== 12 passed in X.YZs ===================

----

*********************************************************************************
move w_pass
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_making_a_function_w_pass` to use the result of a call to the :ref:`w_pass function<test_making_a_function_w_pass>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`w_pass function<test_making_a_function_w_pass>` in ``test_functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def test_making_a_function_w_pass():
      def w_pass():
          pass

      # assert w_pass() is None
      assert src.functions.w_pass() is None


  def test_making_a_function_w_return():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'src' is not defined

because ``src`` is not defined in ``test_functions.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``test_functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.functions


    def test_making_a_function_w_pass():

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src'

  because there is nothing named ``src`` in this project.

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 255
    :emphasize-lines: 6
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # ModuleNotFoundError

* I open another terminal_ then make sure I am in the ``functions`` folder_

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir src

* I go back to the terminal_ where the tests are running.

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) on the keyboard in ``test_functions.py`` to run the test again and it shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    ModuleNotFoundError: No module named 'src.functions'

  because there is nothing in the ``src`` folder_ named ``functions``.

* I go to the second terminal_ I opened, then use touch_ to make ``functions.py`` in the ``src`` folder_

  .. code-block:: python
    :emphasize-lines: 1

    touch src/functions.py

* I go back to the terminal_ where the tests are running and it shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions' has no attribute 'w_pass'

  because there is nothing in ``functions.py`` in the ``src`` folder_ with the name ``w_pass``.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen, in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 255
    :emphasize-lines: 7
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # SyntaxError
    # ModuleNotFoundError
    # AttributeError

* I open ``functions.py`` from the ``src`` folder.

* I add a copy of :ref:`the w_pass function<test_making_a_function_w_pass>` to ``functions.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def w_pass():
        pass

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the w_pass function<test_making_a_function_w_pass>` from :ref:`test_making_a_function_w_pass` in ``test_functions.py``

  .. code-block:: python
    :linenos:

    import src.functions


    def test_making_a_function_w_pass():
        assert src.functions.w_pass() is None


    def test_making_a_function_w_return():

  the test is still green because the call that was made to :ref:`the w_pass function<test_making_a_function_w_pass>` that was in ``test_functions.py`` is now to :ref:`the w_pass function<test_making_a_function_w_pass>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.w_pass`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── functions.py
        └── def w_pass():
                pass

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move w_pass to functions.py'

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*********************************************************************************
move w_return
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_making_a_function_w_return` to use the result of a call to the :ref:`w_return function<test_making_a_function_w_return>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`w_return function<test_making_a_function_w_return>` in ``test_functions.py``

.. code-block:: python
  :lineno-start: 8
  :emphasize-lines: 5-6

  def test_making_a_function_w_return():
      def w_return():
          return

      # assert w_return() is None
      assert src.functions.w_return() is None


  def test_making_a_function_w_return_none():

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.functions'
                  has no attribute 'w_return'

because ``functions.py`` in the ``src`` folder_ does not have anything named ``w_return`` in it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the w_return function<test_making_a_function_w_return>` to ``functions.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def w_pass():
      pass


  def w_return():
      return

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the w_return function<test_making_a_function_w_return>` from :ref:`test_making_a_function_w_return` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 8

    def test_making_a_function_w_return():
        assert src.functions.w_return() is None


    def test_making_a_function_w_return_none():

  the test is still green because the call that was made to :ref:`the w_return function<test_making_a_function_w_return>` that was in ``test_functions.py`` is now to :ref:`the w_return function<test_making_a_function_w_return>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.w_return`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── functions.py
        └── def w_return():
                return

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move w_return to functions.py'

----

*********************************************************************************
move w_return_none
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_making_a_function_w_return_none` to use the result of a call to the :ref:`w_return_none function<test_making_a_function_w_return_none>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`w_return_none function<test_making_a_function_w_return_none>` in ``test_functions.py``

.. code-block:: python
  :lineno-start: 12
  :emphasize-lines: 5-6

  def test_making_a_function_w_return_none():
      def w_return_none():
          return None

      # assert w_return_none() is None
      assert src.functions.w_return_none() is None


  def test_what_happens_after_functions_return():

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.functions'
                  has no attribute 'w_return_none'

because ``functions.py`` in the ``src`` folder_ does not have anything named ``w_return_none`` in it.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the w_return_none function<test_making_a_function_w_return_none>` to ``functions.py``

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def w_return():
      return


  def w_return_none():
      return None

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the w_return_none function<test_making_a_function_w_return_none>` from :ref:`test_making_a_function_w_return_none` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 12

    def test_making_a_function_w_return_none():
        assert src.functions.w_return_none() is None


    def test_what_happens_after_functions_return():

  the test is still green because the call that was made to :ref:`the w_return_none function<test_making_a_function_w_return_none>` that was in ``test_functions.py`` is now to :ref:`the w_return_none function<test_making_a_function_w_return_none>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.w_return_none`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── functions.py
        └── def w_return_none():
                return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move w_return_none to functions.py'

----

*********************************************************************************
move return_leaves_the_function
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_what_happens_after_functions_return` to use the result of a call to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` in ``test_functions.py``

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 6-10

  def test_what_happens_after_functions_return():
      def return_leaves_the_function():
          return None
          return 'only one way for this line to run'

      # assert return_leaves_the_function() is None
      assert (
          src.functions
             .return_leaves_the_function()
      ) is None


  def test_constant_function():

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.functions'
                  has no attribute 'return_leaves_the_function'

because I have not added ``return_leaves_the_function`` to ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` to ``functions.py``

.. code-block:: python
  :lineno-start: 9
  :emphasize-lines: 5-7

  def w_return_none():
      return None


  def return_leaves_the_function():
      return None
      return 'only one way for this line to run'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` from :ref:`test_what_happens_after_functions_return` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 16

    def test_what_happens_after_functions_return():
        assert (
            src.functions
               .return_leaves_the_function()
        ) is None


    def test_constant_function():

  the test is still green because the call that was made to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` that was in ``test_functions.py`` is now to :ref:`return_leaves_the_function<test_what_happens_after_functions_return>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.return_leaves_the_function`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── functions.py
        └── def return_leaves_the_function():
                return None

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move return_leaves_the_function to functions.py'

----

*********************************************************************************
move constant function
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_constant_function` to use the result of a call to the :ref:`constant function<test_constant_function>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a call to the :ref:`constant function<test_constant_function>` in ``test_functions.py``

.. code-block:: python
  :lineno-start: 23
  :emphasize-lines: 5-6

  def test_constant_function():
      def constant():
          return 'the same thing'

      # assert constant() == 'the same thing'
      assert src.functions.constant() == 'the same thing'


  def test_identity_function():

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.functions'
                  has no attribute 'constant'

because there is nothing named ``constant`` in ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the constant function<test_constant_function>` to ``functions.py``

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 6-7

  def return_leaves_the_function():
      return None
      return 'only one way for this line to run'


  def constant():
      return 'the same thing'

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the constant function<test_constant_function>` from :ref:`test_constant_function` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 23

    def test_constant_function():
        assert src.functions.constant() == 'the same thing'


    def test_identity_function():

  the test is still green because the call that was made to :ref:`the constant function<test_constant_function>` that was in ``test_functions.py`` is now to :ref:`the constant function<test_constant_function>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.constant`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── functions.py
        └── def constant():
                return 'the same thing'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move constant function to functions.py'

----

*********************************************************************************
move identity function
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the calls in the :ref:`assertions<what is an assertion?>` of :ref:`test_identity_function` to use the results of calls to the :ref:`identity function<test_identity_function>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of calls to the :ref:`identity function<test_identity_function>` in ``test_functions.py``

.. code-block:: python
  :lineno-start: 27
  :emphasize-lines: 5-8

  def test_identity_function():
      def identity(the_input):
          return the_input

      # assert identity(None) == None
      # assert identity(object) == object
      assert src.functions.identity(None) == None
      assert src.functions.identity(object) == object


  def test_why_use_a_function():

the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

.. code-block:: python

  AttributeError: module 'src.functions'
                  has no attribute 'identity'

because ``identity`` is not a name in ``functions.py`` in the ``src`` folder_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I add a copy of :ref:`the identity function<test_identity_function>` to ``functions.py``

.. code-block:: python
  :lineno-start: 18
  :emphasize-lines: 5-6

  def constant():
      return 'the same thing'


  def identity(the_input):
      return the_input

the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented line and :ref:`the identity function<test_identity_function>` from :ref:`test_identity_function` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 23

    def test_identity_function():
        assert src.functions.identity(None) == None
        assert src.functions.identity(object) == object


    def test_why_use_a_function():

  the test is still green because the call that was made to :ref:`the identity function<test_identity_function>` that was in ``test_functions.py`` is now to :ref:`the identity function<test_identity_function>` in ``functions.py`` in the ``src`` folder_. When ``src.functions.identity`` is called, Python_ follows this path

  .. code-block:: shell

    src
    └── functions.py
        └── def identity(the_input):
                return the_input

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move identity function to functions.py'

----

*********************************************************************************
move positional_arguments function
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I comment out the :ref:`positional_arguments function<test_positional_arguments>` in ``test_functions.py``

.. code-block:: python
  :lineno-start: 32
  :emphasize-lines: 17-18

  def test_why_use_a_function():
      def add_x(number):
          return 3 + number

      assert add_x(0) == 3
      assert add_x(1) == 4
      assert add_x(2) == 5
      assert add_x(3) == 6
      assert add_x(4) == 7
      assert add_x(5) == 8
      assert add_x(6) == 9
      assert add_x(7) == 10
      assert add_x(8) == 11
      assert add_x(9) == 12


  # def positional_arguments(first_input, last_input):
  #     return first_input, last_input


  def test_positional_arguments():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'positional_arguments'
             is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`positional arguments function<test_positional_arguments>` in :ref:`test_positional_arguments` to the :ref:`positional_arguments function<test_positional_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 52
    :emphasize-lines: 2-4

    def test_positional_arguments():
        positional_arguments = (
            src.functions.positional_arguments
        )
        first, last = 'first', 'last'

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'positional_arguments'
               is not defined

  because :ref:`test_keyword_arguments` also calls :ref:`the positional_arguments functions<test_positional_arguments>` of ``test_functions.py``. This is a risky change.

* I use a :ref:`variable<what is a variable?>` to reroute the calls to the :ref:`positional arguments function<test_positional_arguments>` in :ref:`test_keyword_arguments` to the :ref:`positional_arguments function<test_positional_arguments>` of the ``functions`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 92
    :emphasize-lines: 2-4

    def test_keyword_arguments():
        positional_arguments = (
            src.functions.positional_arguments
        )
        first, last = 'first', 'last'

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.functions'
                    has no attribute 'positional_arguments'

  because ``positional_arguments`` does not exist in ``functions.py``.

* I add a copy of :ref:`the positional_arguments function<test_positional_arguments>` to ``functions.py``

  .. code-block:: python
    :lineno-start: 22
    :emphasize-lines: 5-6

    def identity(the_input):
        return the_input


    def positional_arguments(first_input, last_input):
        return first_input, last_input

  the test passes because the call that was made to :ref:`the positional_arguments function<test_positional_arguments>` that was in ``test_functions.py`` is now rerouted to :ref:`the positional_arguments function<test_positional_arguments>` in ``functions.py`` in the ``src`` folder_.

  When ``positional_arguments`` is called in :ref:`test_positional_arguments` and :ref:`test_keyword_arguments`, Python_ follows this path

  .. code-block:: shell

    positional_arguments = src.functions.positional_arguments

    src
    └── functions.py
        └── def positional_arguments(the_input):
                return the_input

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented :ref:`positional_arguments function<test_positional_arguments>` from :ref:`test_positional_arguments` in ``test_functions.py``

  .. code-block:: python
    :lineno-start: 32

    def test_why_use_a_function():
        def add_x(number):
            return 3 + number

        assert add_x(0) == 3
        assert add_x(1) == 4
        assert add_x(2) == 5
        assert add_x(3) == 6
        assert add_x(4) == 7
        assert add_x(5) == 8
        assert add_x(6) == 9
        assert add_x(7) == 10
        assert add_x(8) == 11
        assert add_x(9) == 12


    def test_positional_arguments():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move positional_arguments to functions.py'

----

----
BOOM
----
----
BOOM
----
BOOM
----
BOOM
----
BOOM
----



















----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_functions.py`` and ``functions.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``functions``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

:ref:`I can write solutions in a different module from the tests<separate and equal>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<separate and equal functions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have covered a bit so far and know

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`
* :ref:`how to make functions that take input<functions that take input>`
* :ref:`how to place values in strings<telephone>`
* :ref:`how to make a person say hi with f-strings<how to make a person with f-strings>`
* :ref:`how to separate tests from solutions<separate and equal functions>`

:ref:`Would you like to test using a class to remove repetition of inputs between functions?<telephone>`

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