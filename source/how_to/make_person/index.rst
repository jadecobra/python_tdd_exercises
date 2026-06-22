.. meta::
  :description: A step-by-step Python Test-Driven Development (TDD) tutorial for beginners building a person dictionary factory function. Learn modern project setup with uv init and git; automate testing with pytest-watcher and unittest; and systematically resolve AssertionError, NameError, AttributeError, TypeError, and SyntaxError. Covers advanced refactoring using datetime.datetime.now(), random.choice, random.randint, starred parameter lists (*args), and double-star (**) dictionary unpacking.
  :keywords: Jacob Itegboje, Python TDD tutorial for beginners, step by step python test driven development, how to use uv python package manager, pytest-watcher automatic test runner, unittest assertEqual AssertionError, datetime.datetime.now year calculation, how to use random.choice in tests, random.randint test parameters, python unexpected keyword argument TypeError, python parameters without default values order, python double star dictionary unpacking, red green refactor example, catching NameError and AttributeError in python tests, how to fix TypeError: 'NoneType' object is not callable, why blows my test show NameError: name 'src' is not defined, python SyntaxError: parameter without a default follows parameter with a default, testing python factory function returning dict, starred expression

.. include:: ../../links.rst

.. _now: https://docs.python.org/3/library/datetime.html#datetime.datetime.now
.. _now method: now_
.. _today: https://docs.python.org/3/library/datetime.html#datetime.date.today
.. _today method: today_
.. _random.choice: https://docs.python.org/3/library/random.html#random.choice
.. _choice method: `random.choice`_
.. _random.choice method: `random.choice`_

#################################################################################
how to make a person with variables
#################################################################################

----

I want to make a contact list of people. I can use variables to represent the :ref:`attributes<what is a class attribute?>` of a person, for example

* First Name
* Last Name (Surname)
* Sex
* Year of Birth

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../code/person/tests/test_person.py
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

  because there is no definition for ``joe`` in ``test_person.py``

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

  because when I call ``w_return_none`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

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

* I remove the :ref:`assertion<what is an assertion?>` and comments then add a new test :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    # Exceptions seen
    # AssertionError

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'jane' is not defined

  because there is no definition for ``jane`` in ``test_person.py``

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

* I add a :ref:`variable<what is a variable?>` for ``jane`` and point it to :ref:`None<what is None?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    jane = None

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because I called ``jane`` which points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`. Using substitution

  .. code-block:: python

    jane = None # point the name to the object
    jane()      # call the name
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

* I change ``jane`` to a :ref:`function<what is a function?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-3

    # jane = None
    def jane():
        return None

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    # Exceptions seen

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    AssertionError: assert None == 'jane, doe, F, 1991'

  because when I call ``w_return_none`` it returns :ref:`None<what is None?>`. Using substitution since :ref:`I can treat a call to a function as the object it returns<test_what_happens_after_functions_return>`

  .. code-block:: python

    assert jane() == 'jane, doe, F, 1991'
    assert None  == 'jane, doe, F, 1991'

  which raises :ref:`AssertionError<what causes AssertionError?>` because :ref:`None is only equal to None<what is None?>`.

* I change :ref:`the return statement` of ``jane``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 3-4

    # jane = None
    def jane():
        # return None
        return 'jane, doe, F, 1991'

    def test_jane():
        assert jane() == 'jane, doe, F, 1991'


    # Exceptions seen

  the test passes.

----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines

  .. code-block:: python

    def jane():
        return 'jane, doe, F, 1991'

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
close the project
*********************************************************************************

* I close ``person.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``person``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    ...\pumping_python

  I am back in the ``pumping_python`` directory_

----

*************************************************************************************
review
*************************************************************************************

I ran tests to make

* a :ref:`function<what is a function?>` that takes in :ref:`keyword arguments<test_w_keyword_arguments>` as input, has :ref:`default values<test_w_optional_arguments>` for some of them, performs an action based on an input and returns a :ref:`dictionary<what is a dictionary?>` as output

* a :ref:`function<what is a function?>` that takes in a :ref:`dictionary<what is a dictionary?>` and returns a string_ as output with :ref:`values<test_values_of_a_dictionary>` of :ref:`keys<test_keys_of_a_dictionary>` from the :ref:`dictionary<what is a dictionary?>`

I also saw these :ref:`Exceptions<errors>`

* :ref:`AssertionError<what causes AssertionError?>`
* :ref:`NameError<test_catching_name_error_in_tests>`
* :ref:`AttributeError<what causes AttributeError?>`
* :ref:`TypeError<what causes TypeError?>`
* SyntaxError_

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

:ref:`how to make a Python test driven development environment manually`
* :ref:`what causes AssertionError?`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<telephone>`
* :ref:`how to make dictionaries with functions<how to make a person>`

:ref:`Would you like to see another way to make a person?<what is a class?>`

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