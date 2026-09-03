.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): separate and equal telephone — move the module-level text function from tests/test_telephone.py into src/telephone/__init__.py. Open telephone; uv run pytest-watcher . --now (10 passed). Comment out local def text → NameError: name 'text' is not defined. Alias text = src.telephone.text → NameError: name 'src' is not defined. import src.telephone → AttributeError: module 'src.telephone' has no attribute 'text'. Copy def text(the_input) into the package __init__.py until green; remove the commented lines. Then close the tests, wipe __init__.py, and rebuild from failures without looking at the test file: bare name text → NameError; text = None → TypeError 'NoneType' object is not callable; def text() → TypeError takes 0 positional arguments but 1 was given; hardcoded "I got: <class 'object'>" then return value then return 'I got: value' until return f'I got: {value}'. git commit -am 'move text function to src' then git commit --all --message 'test telephone'. Review: I can write solutions in a different module from the tests. Ends with 10 tests calling the alias plus # Exceptions seen AssertionError, NameError, TypeError, AttributeError.
  :keywords: Jacob Itegboje, Pumping Python, telephone with separation, separate and equal telephone, separate tests from solutions, src/telephone/__init__.py, import src.telephone, text = src.telephone.text, NameError name 'src' is not defined, NameError name 'text' is not defined, AttributeError module 'src.telephone' has no attribute 'text', TypeError NoneType object is not callable, TypeError takes 0 positional arguments but 1 was given, return f'I got: {value}', I got: None, I got: hello, I got: <class 'object'>, remove the commented lines, uv run pytest-watcher . --now, red green refactor, git commit -am move text function to src, test_telephone_w_separation, telephone TDD src package layout, I can write solutions in a different module from the tests

.. include:: ../../links.rst

#################################################################################
separate and equal telephone
#################################################################################

The ``text`` :ref:`function<what is a function?>` in :ref:`the telephone project<telephone>` was written in ``tests/test_telephone.py``. I want to move it to ``__init__.py`` in the ``telephone`` folder_ in the ``src`` folder_ so that I can keep the tests and solution separate.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_separation.py
  :language: python
  :linenos:
  :caption: telephone/tests/test_telephone.py
  :lines: 1-12

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_separation.py
  :language: python
  :lineno-start: 15
  :caption: telephone/tests/test_telephone.py
  :lines: 15-27

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_separation.py
  :language: python
  :lineno-start: 30
  :caption: telephone/tests/test_telephone.py
  :lines: 30-42

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_separation.py
  :language: python
  :lineno-start: 45
  :caption: telephone/tests/test_telephone.py
  :lines: 45-57

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_separation.py
  :language: python
  :lineno-start: 60
  :caption: telephone/tests/test_telephone.py
  :lines: 60-

----

*********************************************************************************
open the project
*********************************************************************************

* I open a terminal_
* I change directory_ to the project

  .. code-block:: python
    :emphasize-lines: 1

    cd telephone

  the terminal_ shows I am in the ``telephone`` folder_

  .. code-block:: python

    .../pumping_python/telephone

* I open ``test_telephone.py`` from the ``tests`` folder

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_telephone.py ..........                        [100%]

    =================== 10 passed in A.BCs ===================

----

*********************************************************************************
move text
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I comment out the ``text`` :ref:`function<what is a function?>` in ``tests/test_telephone.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 5-6

  def assert_equal(a, b):
      assert a == b


  # def text(the_input):
  #     return f'I got: {the_input}'


  def test_passing_none():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'text' is not defined

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I use a :ref:`variable<what is a variable?>` to reroute the :ref:`calls<how to call a function with input>` to the ``text`` :ref:`function<what is a function?>` to the ``text`` :ref:`function<what is a function?>` of the ``telephone`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text = src.telephone.text


    def assert_equal(a, b):

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

  .. code-block:: python

    NameError: name 'src' is not defined

  because there is nothing with that name in ``tests/test_telephone.py``.

* I add an `import statement`_ at the top of ``tests/test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src.telephone


    text = src.telephone.text

  the terminal_ is my friend, and shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.telephone'
                    has no attribute 'text'

  because the ``telephone`` :ref:`module<what is a module?>` in the ``src`` folder_ does not have anything named ``text`` inside it.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 78
    :emphasize-lines: 5
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # AttributeError

* I open ``__init__.py`` from the ``telephone`` folder_ in the ``src`` folder_
* I delete all the text in the file_ then add a copy of the ``text`` :ref:`function<what is a function?>` to ``src/telephone/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text(the_input):
        return f'I got: {the_input}'

  all the tests are green again because

  - Python_ brings in an :ref:`object<everything is an object>` for the ``__init__.py`` file_ from the ``telephone`` folder_ in the ``src`` folder_ so I can use it in ``tests/test_telephone.py`` as ``src.telephone`` when ``import src.telephone`` runs.
  - Python_ calls the ``text`` :ref:`function<what is a function?>` from the :ref:`object<everything is an object>` it imported for the ``src/telephone/__init__.py`` file_ (``src.telephone``) when ``src.telephone.text`` is :ref:`called<how to call a function with input>`.

  I think of ``src.telephone.text`` like an address

  .. code-block:: shell

    src.telephone.text
    src/
    └── telephone/
        └── __init__.py
            └── def text(the_input):
                └── return f'I got: {the_input}'

  - ``text`` is something in the ``telephone`` :ref:`module<what is a module>`, in this case it is a :ref:`function<what is a function?>` in the ``__init__.py`` file_.
  - ``telephone`` is something in ``src``, in this case it is a folder_ in the ``src`` folder_.
  - ``src`` is something Python_ can import (a :ref:`module<what is a module?>`, `Python package`_ or folder_).


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from ``tests/test_telephone.py``

  .. code-block:: python
    :linenos:

    import src.telephone


    text = src.telephone.text


    def assert_equal(a, b):
        assert a == b


    def test_passing_none():

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'move text function to src'

  the terminal_ shows a summary of the changes then goes back to the command line.

All the tests are passing because Python_ follows this path when the ``text`` :ref:`function<what is a function?>` is :ref:`called<how to call a function with input>`

* In :ref:`test_passing_none`

  .. code-block:: shell

    text = src.telephone.text
    text(None) -> 'I got: None'
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = None
                    └── return f'I got: {the_input}'
                        return  'I got:  None      '

* In :ref:`test_passing_booleans`

  .. code-block:: shell

    text = src.telephone.text
    text(False) -> 'I got: False'
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = False
                    └── return f'I got: {the_input}'
                        return  'I got:  False     '

* In :ref:`test_passing_an_integer`

  .. code-block:: shell

    text = src.telephone.text
    an_integer = 1234
    text(an_integer) -> 'I got: 1234'
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = 1234
                    └── return f'I got: {the_input}'
                        return  'I got: 1234       '

* In :ref:`test_passing_a_float`

  .. code-block:: shell

    text = src.telephone.text
    a_float = 5.678
    text(a_float) -> 'I got: 5.678'
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = 5.678
                    └── return f'I got: {the_input}'
                        return  'I got: 5.678      '

* In :ref:`test_passing_a_string`

  .. code-block:: shell

    text = src.telephone.text
    a_string = 'hello'
    text(a_string) -> 'I got: hello'
    src/
    └── telephone/
        └── __init__.py
            └── def text(the_input):
                ├── the_input = 'hello'
                └── return f'I got: {the_input}'
                    return  'I got:  hello     '

* In :ref:`test_passing_a_tuple`

  .. code-block:: shell

    text = src.telephone.text
    a_tuple = (0, 1, 2, 'n')
    text(a_tuple) -> "I got: (0, 1, 2, 'n')"
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = (0, 1, 2, 'n')
                    └── return f'I got: {  the_input  }'
                        return  "I got:  (0, 1, 2, 'n')"

* In :ref:`test_passing_a_list`

  .. code-block:: shell

    text = src.telephone.text
    a_list = [0, 1, 2, 'n']
    text(a_list) -> "I got: [0, 1, 2, 'n']"
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = [0, 1, 2, 'n']
                    └── return f'I got: {  the_input  }'
                        return  "I got:  [0, 1, 2, 'n']"

* In :ref:`test_passing_a_set`

  .. code-block:: shell

    text = src.telephone.text
    a_set = {0, 1, 2, 'n'}
    text(a_set) -> 'I got: {0, 1, 2, 'n'}'
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = {0, 1, 2, 'n'}
                    └── return f'I got: {  the_input  }'
                        return  'I got:  {0, 1, 2, 'n'}'

* In :ref:`test_passing_a_dictionary`

  .. code-block:: shell

    text = src.telephone.text
    a_dictionary = {
        'key0': 'value0', 'keyN': [0, 1, 2, 'n']
    }
    text(a_dictionary) -> ("I got: {'key0': 'value0',"
    │                               'keyN': [0, 1, 2, 'n']}")
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = {
                    │       'key0': 'value0', 'keyN': [0, 1, 2, 'n']
                    │   }
                    └── return f'I got: {       the_input        }'
                        return ("I got: {'key0': 'value0',"
                                         'keyN': [0, 1, 2, 'n']}")

* In :ref:`test_passing_a_class`

  .. code-block:: shell

    text = src.telephone.text
    text(object) -> "I got: <class 'object'>"
    └── src/
        └── telephone/
            └── __init__.py
                └── def text(the_input):
                    ├── the_input = object
                    └── return f'I got: {   the_input   }'
                        return  "I got:  <class 'object'>"

----

*********************************************************************************
test_telephone
*********************************************************************************

Since the solution is separate from the tests, I can write the program_ that makes the tests pass without looking at ``tests/test_telephone.py``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``tests/test_telephone.py``

* I delete the text in ``src/telephone/__init__.py`` and the terminal_ :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.telephone'
                    has no attribute 'text'

  Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``src/telephone/__init__.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error>`

  .. code-block:: python

    NameError: name 'text' is not defined

* I point it to :ref:`None (the simplest object)<what is None?>` to define it

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # text
    text = None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

  because ``text`` points to :ref:`None<what is None?>` and :ref:`I cannot call None like a function<test_type_error_w_the_uncallables>`.

* I make ``text`` a :ref:`function<what is a function?>` to make it :ref:`callable<how to make a function>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 2-4

    # text
    # text = None
    def text():
        return None

  the terminal_ is my friend, and shows :ref:`TypeError<what causes TypeError?>`

  .. code-block:: python

    TypeError: text() takes 0 positional arguments
               but 1 was given

  because this :ref:`function definition<how to make a function that takes input>` does not allow any inputs, the parentheses are empty.

* I :ref:`make the function take input<how to make a function that takes input>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 4-5

    # text
    # text = None
    # def text():
    def text(value):
        return None

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert None == "I got: <class 'object'>"

* I copy the string_ from the terminal_ and paste it in the :ref:`return statement<the return statement>` to match the expectation of the test

  .. code-block:: python
    :linenos:
    :emphasize-lines: 5-6

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        return "I got: <class 'object'>"

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    E       assert "I got: <class 'object'>"
                == "I got: <class 'bool'>"

* I change the :ref:`return statement<the return statement>` to see the difference between the input and the expected output (remember :ref:`the identity function?<test_identity_function>`)

  .. code-block:: python
    :linenos:
    :emphasize-lines: 6-7

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        # return "I got: <class 'object'>"
        return value

  the test summary info shows that every test has :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: shell
    :emphasize-text: got:

    FAILED ...::test_passing_none -
        AssertionError: assert None == 'I got: None'
    FAILED ...::test_passing_booleans -
        AssertionError: assert False == 'I got: False'
    FAILED ...::test_passing_an_integer -
        AssertionError: assert 1234 == 'I got: 1234'
    FAILED ...::test_passing_a_float -
        AssertionError: assert 5.678 == 'I got: 5.678'
    FAILED ...::test_passing_a_string -
        AssertionError: assert 'hello' == 'I got: hello'
    FAILED ...::test_passing_a_tuple -
        assert (0, 1, 2, 'n') == "I got: (0, 1, 2, 'n')"
    FAILED ...::test_passing_a_list -
        assert [0, 1, 2, 'n'] == "I got: [0, 1, 2, 'n']"
    FAILED ...::test_passing_a_set -
        assert {0, 1, 2, 'n'} == "I got: {0, 1, 2, 'n'}"
    FAILED ...::test_passing_a_dictionary -
        assert {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}
    == "I got: {'key0': 'value0', 'keyN': [0, 1, 2, 'n']}"
    FAILED ...::test_passing_a_class -
        assert <class 'object'> == "I got: <class 'object'>"

  they all expect the input (``value``) as part of the message

* I add a :ref:`return statement<the return statement>` with the name of the input

  .. code-block:: python
    :linenos:
    :emphasize-lines: 7-8

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        # return "I got: <class 'object'>"
        # return value
        return 'I got: value'

  the terminal_ is my friend, and shows :ref:`AssertionError<what causes AssertionError?>`

  .. code-block:: python

    FAILED ...test_passing_none -
        AssertionError: assert 'I got: value' == 'I got: None'
    FAILED ...test_passing_booleans -
        AssertionError: assert 'I got: value' == 'I got: False'
    FAILED ...test_passing_an_integer -
        AssertionError: assert 'I got: value' == 'I got: 1234'
    FAILED ...test_passing_a_float -
        AssertionError: assert 'I got: value' == 'I got: 5.678'
    FAILED ...test_passing_a_string -
        AssertionError: assert 'I got: value' == 'I got: hello'
    FAILED ...test_passing_a_tuple -
        assert 'I got: value' == "I got: (0, 1, 2, 'n')"
    FAILED ...test_passing_a_list -
        assert 'I got: value' == "I got: [0, 1, 2, 'n']"
    FAILED ...test_passing_a_set -
        assert 'I got: value' == "I got: {0, 1, 2, 'n'}"
    FAILED ...test_passing_a_dictionary -
        assert 'I got: value' == "I got: {'key..., 1, 2, 'n']}"
    FAILED ...test_passing_a_class -
        assert 'I got: value' == "I got: <class 'object'>"

* I change the :ref:`return statement<the return statement>` to an :ref:`f-string<what is string interpolation?>`

  .. code-block:: python
    :linenos:
    :emphasize-lines: 8-9

    # text
    # text = None
    # def text():
    def text(value):
        # return None
        # return "I got: <class 'object'>"
        # return value
        # return 'I got: value'
        return f'I got: {value}'

  and all the tests are passing! I am a programmer!!

* I remove the commented lines

  .. code-block:: python
    :linenos:

    def text(value):
        return f'I got: {value}'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit --all --message \
    'test telephone'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
close the project
*********************************************************************************

* I close ``src/telephone/__init__.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``telephone``

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

:ref:`Do you want to see all the CODE I typed in this chapter?<separate and equal telephone: tests and solution>`

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
* :ref:`I know how to separate tests from solutions<separate and equal>`.

:ref:`would you like to separate the tests from the solution in the TypeError project?<separate and equal TypeError>`

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