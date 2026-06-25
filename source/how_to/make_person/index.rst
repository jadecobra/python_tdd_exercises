.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): how to make a person with strings. Use strings to represent a person (first name, last name, sex, year of birth) for a contact list by writing module-level functions that return formatted strings. Starts with pytest-watcher showing "no tests ran". RED: add test calling undefined name → NameError: name 'joe' is not defined. GREEN: point name at None (TypeError: 'NoneType' object is not callable), make function return None (AssertionError: assert None == 'joe, blow, M, 1996'), fix return value. Repeat the cycle. REFACTOR: remove the commented lines, git commit -am. Review shows the problem: I made a function for each person. What happens if I have to make 10 or 100 or 1000 people? Each test is repetition of the information for each person. Leads to wanting one function that can take input instead. Uses bare assert, uv run pytest-watcher, red green refactor.
  :keywords: Jacob Itegboje, Pumping Python, how to make a person with strings, strings to represent a person, contact list python, first functions returning strings, NameError: name 'joe' is not defined, TypeError: 'NoneType' object is not callable, AssertionError: assert None == 'joe, blow, M, 1996', bare assert, pytest-watcher "no tests ran", red green refactor, remove the commented lines, git commit -am, one function per person, repetition of the information for each person, functions do not scale, 10 or 100 or 1000 people, functions that take input, module level functions, writing test functions, tdd repetition problem, uv run pytest-watcher . --now

.. include:: ../../links.rst

#################################################################################
how to make a person with strings
#################################################################################

----

I want to make a contact list of people. I can use strings_ to represent a person, for example

* First Name
* Last Name (Surname)
* Sex
* Year of Birth

can be placed in a string_ (anything in :ref:`quotes`).

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/person/tests/test_person_w_strings.py
  :language: python
  :linenos:

-----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: shell
    :emphasize-lines: 1

    cd person

  the terminal_ shows I am in the ``person`` folder_

  .. code-block:: shell

    .../pumping_python/person

* I open ``test_person.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows ``no tests ran``.

----

*********************************************************************************
test_joe
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I remove the :ref:`assertion<what is an assertion?>` and comments then add a new test :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'joe' is not defined

  because there is no definition for ``joe`` in ``test_person.py``.

* I add :ref:`NameError<test_catching_name_error_in_tests>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 3
    :emphasize-text: NameError

    # Exceptions seen
    # AssertionError
    # NameError

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``joe`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    joe = None


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``joe`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    joe = None # point the name to the object
    joe()      # call the name
    None()     # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I add :ref:`TypeError<what causes TypeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 7
    :emphasize-lines: 4
    :emphasize-text: TypeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I change ``joe`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-3

    # joe = None
    def joe():
        return None


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'joe, blow, M, 1996'

  because when I call ``joe`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert joe() == 'joe, blow, M, 1996'
    assert None  == 'joe, blow, M, 1996'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``joe``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # joe = None
    def joe():
        # return None
        return 'joe, blow, M, 1996'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_joe'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_jane
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a test :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 5
  :emphasize-lines: 5-6

  def test_joe():
      assert joe() == 'joe, blow, M, 1996'


  def test_jane():
      assert jane() == 'jane, doe, F, 1991'



  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'jane' is not defined

because there is no definition for ``jane`` in this file_.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``jane`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def joe():
        return 'joe, blow, M, 1996'


    jane = None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``jane`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    jane = None # point the name to the object
    jane()      # call the name
    None()      # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``jane`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-7

    def joe():
        return 'joe, blow, M, 1996'


    # jane = None
    def jane():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'jane, doe, F, 1991'

  because when I call ``jane`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert jane() == 'jane, doe, F, 1991'
    assert None   == 'jane, doe, F, 1991'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``jane``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    def joe():
        return 'joe, blow, M, 1996'


    # jane = None
    def jane():
        # return None
        return 'jane, doe, F, 1991'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def jane():
        return 'jane, doe, F, 1991'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_jane'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_john
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 13
  :emphasize-lines: 5-6

  def test_jane():
      assert jane() == 'jane, doe, F, 1991'


  def test_john():
      assert john() == 'john, smith, M, 1580'



  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'john' is not defined

because there is no definition for ``john`` in this file_, yet.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``john`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5

    def jane():
        return 'jane, doe, F, 1991'


    john = None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``john`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    john = None # point the name to the object
    john()      # call the name
    None()      # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``john`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 5-7

    def joe():
        return 'joe, blow, M, 1996'


    # john = None
    def john():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'john, smith, M, 1580'

  because when I call ``john`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert john() == 'john, smith, M, 1580'
    assert None   == 'john, smith, M, 1580'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``john``

  .. code-block:: python
    :lineno-start: 5
    :emphasize-lines: 7-8

    def jane():
        return 'jane, doe, F, 1991'


    # john = None
    def john():
        # return None
        return 'john, smith, M, 1580'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def jane():
        return 'jane, doe, F, 1991'


    def john():
        return 'john, smith, M, 1580'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    def test_john():
        assert john() == 'john, smith, M, 1580'


    # Exceptions seen

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_john'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_mary
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add another test :ref:`function<what is a function?>`

.. code-block:: python
  :lineno-start: 16
  :emphasize-lines: 5-6

  def test_john():
      assert john() == 'john, smith, M, 1580'


  def test_mary():
      assert mary() == 'mary, public, F, 2000'


  # Exceptions seen

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'mary' is not defined

because there is no definition for ``mary``, it is just a name.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add a :ref:`variable<what is a variable?>` for ``mary`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5

    def john():
        return 'john, smith, M, 1580'


    mary = None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``mary`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    mary = None # point the name to the object
    mary()      # call the name
    None()      # substitute the value for the name

  ``None()`` raises :ref:`TypeError<what causes TypeError?>`.

* I change ``mary`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 5-7

    def john():
        return 'john, smith, M, 1580'


    # mary = None
    def mary():
        return None


    def test_joe():

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'mary, public, F, 2000'

  because when I call ``mary`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert mary() == 'mary, public, F, 2000'
    assert None   == 'mary, public, F, 2000'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``mary``

  .. code-block:: python
    :lineno-start: 9
    :emphasize-lines: 7-8

    def john():
        return 'john, smith, M, 1580'


    # mary = None
    def mary():
        # return None
        return 'mary, public, F, 2000'


    def test_joe():

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def joe():
        return 'joe, blow, M, 1996'


    def jane():
        return 'jane, doe, F, 1991'


    def john():
        return 'john, smith, M, 1580'


    def mary():
        return 'mary, public, F, 2000'


    def test_joe():
        assert joe() == 'joe, blow, M, 1996'


    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    def test_john():
        assert john() == 'john, smith, M, 1580'


    def test_mary():
        assert mary() == 'mary, public, F, 2000'


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am 'add test_mary'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_person.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    ...\pumping_python

  I am back in the ``pumping_python`` directory_.

----

*************************************************************************************
review
*************************************************************************************

I ran tests to make :ref:`functions<what is a function?>` that return strings_ with information for people. There are a few problems with what I have so far

- I made a :ref:`function<what is a function?>` for each person. What happens if I have to make 10 or 100 or 1000 people? I am not ready to make 1000 :ref:`functions<what is a function?>`.
- Each test is basically a repetition of the information for each person.

I want something that will take in information for a person and return a string_ for the person. That way I can use one thing to make as many people as I want. I can do that with :ref:`functions that take input<functions that take input>`.

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<how to make a person: tests and solution>`

----

*************************************************************************************
what is next?
*************************************************************************************

you know:

* :ref:`how to make a Python test driven development environment manually`
* :ref:`what a Python module is<what is a module?>`
* :ref:`how to run tests automatically`
* :ref:`what causes AssertionError<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to make a person with strings`

:ref:`Would you like to test functions with input?<functions that take input>`

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