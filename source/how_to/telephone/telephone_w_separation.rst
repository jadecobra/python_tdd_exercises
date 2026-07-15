.. meta::
  :description: Beginner Python TDD tutorial (Jacob Itegboje, Pumping Python): telephone with separation — keep tests and solution separate and equal. Move the module-level text function from test_telephone.py into src/telephone.py. RED: call src.telephone.text(None) before import → NameError: name 'src' is not defined. GREEN: import src → ModuleNotFoundError: No module named 'src'; mkdir src → AttributeError: module 'src' has no attribute 'telephone'; import src.telephone → ModuleNotFoundError: No module named 'src.telephone'; touch src/telephone.py → AttributeError: module 'src.telephone' has no attribute 'text'; copy def text(the_input) into src/telephone.py until green. REFACTOR: reroute every test (None, booleans, int 1234, float 5.678, string 'hello', tuple/list/set/dict, classes object/bool/int/…) to src.telephone.text with reality == my_expectation, remove the commented lines, delete local text from the test file. Then close tests and rebuild telephone.py from failures only: text = None → TypeError NoneType not callable; def text() → takes 0 positional arguments but 1 was given; return f'I got: {value}'. uv run pytest-watcher . --now; git commits. Review: I can write solutions in a different module from the tests. Ends with 10 tests + Exceptions seen AssertionError NameError TypeError ModuleNotFoundError AttributeError.
  :keywords: Jacob Itegboje, Pumping Python, telephone with separation, separate and equal telephone, separate tests from solutions, src/telephone.py, import src.telephone, src.telephone.text, NameError name 'src' is not defined, ModuleNotFoundError No module named 'src', ModuleNotFoundError No module named 'src.telephone', AttributeError module 'src' has no attribute 'telephone', AttributeError module 'src.telephone' has no attribute 'text', TypeError NoneType object is not callable, takes 0 positional arguments but 1 was given, return f'I got: {value}', I got: None, I got: hello, I got: <class 'object'>, reality == my_expectation, remove the commented lines, uv run pytest-watcher . --now, red green refactor, git commit -am separate solution from tests, test_telephone_w_separation, telephone TDD src package layout, I can write solutions in a different module from the tests

.. include:: ../../links.rst

#################################################################################
separate and equal telephone
#################################################################################

The ``text`` :ref:`function<what is a function?>` in :ref:`the telephone project<telephone>` was written in ``test_telephone.py``. I want to move it to ``telephone.py`` in the ``src`` folder_ so that I can keep the tests and solution separate.

----

*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/telephone/tests/test_telephone_w_separation.py
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

    cd telephone

  the terminal_ shows I am in the ``telephone`` folder_

  .. code-block:: python

    .../pumping_python/telephone

* I open ``test_telephone.py``

* I use `pytest-watcher`_ to run the tests automatically

  .. code-block:: python
    :emphasize-lines: 1
    :emphasize-text: .

    uv run pytest-watcher . --now

  the terminal_ shows

  .. code-block:: python

    test_telephone.py ..........                        [100%]

    =================== 10 passed in A.BCs ===================

----

*********************************************************************************
move test_passing_none
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I change the :ref:`call<how to call a function with input>` in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_none` to use the result of a :ref:`call<how to call a function with input>` to the ``text`` :ref:`function<what is a function?>` of the ``telephone`` :ref:`module<what is a module?>` in the ``src`` folder_ instead of a :ref:`call<how to call a function with input>` to the ``text`` :ref:`function<what is a function?>` in ``test_telephone.py``

.. code-block:: python
  :linenos:
  :emphasize-lines: 6-9

  def text(the_input):
      return f'I got: {the_input}'


  def test_passing_none():
      reality = src.telephone.text(None)
      my_expectation = 'I got: None'
      # assert text(None) == 'I got: None'
      assert reality == my_expectation


  def test_passing_booleans():

the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

.. code-block:: python

  NameError: name 'src' is not defined

because there is nothing with that name in ``test_telephone.py``.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add an `import statement`_ at the top of ``test_telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    import src


    def text(the_input):
        return f'I got: {the_input}'

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    E   ModuleNotFoundError: No module named 'src'

  because there is nothing named ``src`` in the project.

* I add :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 5
    :emphasize-text: ModuleNotFoundError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError

* I open another terminal_ and make sure I am in the ``telephone`` folder_

* I use mkdir_ to make a folder_ named ``src``

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir src

  the terminal_ goes back to the command line.

* I go back to the terminal_ where the tests are running.

* I use :kbd:`ctrl/command+s` (Windows_ & Linux_/MacOS_) in ``test_telephone.py`` to run the test again, and the terminal_ shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src'
                    has no attribute 'telephone'

  because there is nothing named ``telephone`` in the ``src`` folder_.

* I add :ref:`AttributeError<what causes AttributeError?>` to the list of :ref:`Exceptions<errors>` seen

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 6
    :emphasize-text: AttributeError

    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

* I change the `import statement`_ to make it import ``telephone.py`` from the ``src`` folder_

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    # import src
    import src.telephone


    def text(the_input):

  the terminal_ is my friend, and shows :ref:`ModuleNotFoundError<what causes ModuleNotFoundError?>`

  .. code-block:: python

    E   ModuleNotFoundError: No module named 'src.telephone'

  because Python_ cannot find ``telephone.py`` in the ``src`` folder_ since I have not made it yet.

* I go to the other terminal_

* I use touch_ to make ``telephone.py`` in the ``src`` folder_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1

        touch src/telephone.py

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1

        New-Item src/telephone.py

  the terminal_ goes back to the command line.

* I add the new file_ to git_ for tracking

  .. code-block:: python

    git add src/telephone.py

  the terminal_ goes back to the command line.

* I go back to the terminal_ where the tests are running and it shows :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    AttributeError: module 'src.telephone' has no attribute 'text'

  because ``telephone.py`` in the ``src`` folder_ does not have anything named ``text`` inside it.

* I open ``telephone.py`` from the ``src`` folder_
* I add a copy of the ``text`` :ref:`function<what is a function?>` to ``telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1-2

    def text(the_input):
        return f'I got: {the_input}'

  the test passes because

  - when ``import src.telephone`` runs, Python_ brings in an :ref:`object<everything is an object>` for the ``telephone.py`` file_ from the ``src`` folder_ so I can use it in ``test_telephone.py`` as ``src.telephone``
  - when ``src.telephone.text(None)`` runs, Python_ calls the ``text`` :ref:`function<what is a function?>` from the :ref:`object<everything is an object>` it imported for the ``telephone.py`` file_ from the ``src`` folder_ (``src.telephone``)

  I think of ``src.telephone.text`` like an address

  .. code-block:: shell

    src.telephone.text
    src
    └── telephone.py
        └── def text(the_input):
            └── return f'I got: {the_input}'

  - ``text`` is something in ``telephone``, in this case it is a :ref:`function<what is a function?>` in ``telephone``
  - ``telephone`` is something in ``src``, in this case it is ``telephone.py`` (a :ref:`module<what is a module?>`) in the ``src`` folder_
  - ``src`` is something Python_ can import (a :ref:`module<what is a module?>`, `Python package`_ or folder_)


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----

* I remove the commented lines from ``test_telephone.py``

  .. code-block:: python
    :linenos:

    import src.telephone


    def text(the_input):
        return f'I got: {the_input}'


    def test_passing_none():
        reality = src.telephone.text(None)
        my_expectation = 'I got: None'
        assert reality == my_expectation


    def test_passing_booleans():

* I change the call in the first :ref:`assertion<what is an assertion?>` of :ref:`test_passing_booleans` to ``src.telephone.text``

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 2-5

    def test_passing_booleans():
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        # assert text(False) == 'I got: False'
        assert reality == my_expectation
        assert text(True) == 'I got: True'


    def test_passing_an_integer():

  the test is still green because when ``src.telephone.text`` is called, Python_ follows this path

  .. code-block:: shell

    src.telephone.text
    src
    └── telephone.py
        └── def text(the_input):
            └── return f'I got: {the_input}'

  using the string_ representation of the :ref:`object<everything is an object>` in the curly braces ``{ }``

  .. code-block:: python

    text(None)
        text(the_input)
            the_input = None
            return f'I got: {the_input}'
            return  'I got:  None      '

* I make the same change for the next :ref:`assertion<what is an assertion?>`

  .. code-block:: python
    :lineno-start: 14
    :emphasize-lines: 7-10

    def test_passing_booleans():
        # assert text(False) == 'I got: False'
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        assert reality == my_expectation

        reality = src.telephone.text(True)
        my_expectation = 'I got: True'
        # assert text(True) == 'I got: True'
        assert reality == my_expectation


    def test_passing_an_integer():

  still green.

* I remove the commented lines from :ref:`test_passing_booleans`

  .. code-block:: python
    :lineno-start: 14

    def test_passing_booleans():
        reality = src.telephone.text(False)
        my_expectation = 'I got: False'
        assert reality == my_expectation

        reality = src.telephone.text(True)
        my_expectation = 'I got: True'
        assert reality == my_expectation


    def test_passing_an_integer():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_an_integer` to ``src.telephone.text``

  .. code-block:: python
    :lineno-start: 24
    :emphasize-lines: 4-7

    def test_passing_an_integer():
        an_integer = 1234

        reality = src.telephone.text(an_integer)
        my_expectation = f'I got: {an_integer}'
        # assert text(an_integer) == f'I got: {an_integer}'
        assert reality == my_expectation


    def test_passing_a_float():

  green.

* I remove the commented line from :ref:`test_passing_an_integer`

  .. code-block:: python
    :lineno-start: 24

    def test_passing_an_integer():
        an_integer = 1234

        reality = src.telephone.text(an_integer)
        my_expectation = f'I got: {an_integer}'
        assert reality == my_expectation


    def test_passing_a_float():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_float`

  .. code-block:: python
    :lineno-start: 32
    :emphasize-lines: 4-7

    def test_passing_a_float():
        a_float = 5.678

        reality = src.telephone.text(a_float)
        my_expectation = f'I got: {a_float}'
        # assert text(a_float) == f'I got: {a_float}'
        assert reality == my_expectation


    def test_passing_a_string():

  still green because when ``src.telephone.text`` is called, Python_ follows this path

  .. code-block:: shell

    src.telephone.text
    src
    └── telephone.py
        └── def text(the_input):
            └── return f'I got: {the_input}'

  using the string_ representation of the :ref:`object<everything is an object>` in the curly braces ``{ }``

  .. code-block:: python

    a_float = 5.678

    text(a_float)
        text(the_input)
            the_input = 5.678
            return f'I got: {the_input}'
            return  'I got:  5.678     '

* I remove the commented line

  .. code-block:: python
    :lineno-start: 32

    def test_passing_a_float():
        a_float = 5.678

        reality = src.telephone.text(a_float)
        my_expectation = f'I got: {a_float}'
        assert reality == my_expectation


    def test_passing_a_string():

  the test is still green.

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_string`

  .. code-block:: python
    :lineno-start: 40
    :emphasize-lines: 4-7

    def test_passing_a_string():
        a_string = 'hello'

        reality = src.telephone.text(a_string)
        my_expectation = f'I got: {a_string}'
        # assert text(a_string) == f'I got: {a_string}'
        assert reality == my_expectation


    def test_passing_a_tuple():

  still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 40

    def test_passing_a_string():
        a_string = 'hello'

        reality = src.telephone.text(a_string)
        my_expectation = f'I got: {a_string}'
        assert reality == my_expectation


    def test_passing_a_tuple():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_tuple`

  .. code-block:: python
    :lineno-start: 48
    :emphasize-lines: 4-7

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')

        reality = src.telephone.text(a_tuple)
        my_expectation = f'I got: {a_tuple}'
        # assert text(a_tuple) == f'I got: {a_tuple}'
        assert reality == my_expectation


    def test_passing_a_list():

  green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 48

    def test_passing_a_tuple():
        a_tuple = (0, 1, 2, 'n')

        reality = src.telephone.text(a_tuple)
        my_expectation = f'I got: {a_tuple}'
        assert reality == my_expectation


    def test_passing_a_list():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_list`

  .. code-block:: python
    :lineno-start: 56
    :emphasize-lines: 4-7

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']

        reality = src.telephone.text(a_list)
        my_expectation = f'I got: {a_list}'
        # assert text(a_list) == f'I got: {a_list}'
        assert reality == my_expectation


    def test_passing_a_set():

  still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 56

    def test_passing_a_list():
        a_list = [0, 1, 2, 'n']

        reality = src.telephone.text(a_list)
        my_expectation = f'I got: {a_list}'
        assert reality == my_expectation


    def test_passing_a_set():

* I change the call in the :ref:`assertion<what is an assertion?>` of :ref:`test_passing_a_set`

  .. code-block:: python
    :lineno-start: 64
    :emphasize-lines: 4-7

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}

        reality = src.telephone.text(a_set)
        my_expectation = f'I got: {a_set}'
        # assert text(a_set) == f'I got: {a_set}'
        assert reality == my_expectation


    def test_passing_a_dictionary():

  the test is still green.

* I remove the commented line

  .. code-block:: python
    :lineno-start: 64

    def test_passing_a_set():
        a_set = {0, 1, 2, 'n'}

        reality = src.telephone.text(a_set)
        my_expectation = f'I got: {a_set}'
        assert reality == my_expectation


    def test_passing_a_dictionary():

* I change the value the ``reality`` :ref:`variable<what is a variable?>` of :ref:`test_passing_a_dictionary` points to from the result of a :ref:`call<how to call a function with input>` to the ``text`` :ref:`function<what is a function?>` of the ``test_telephone`` :ref:`module<what is a module?>`, to the result of a :ref:`call<how to call a function with input>` to the ``text`` :ref:`function<what is a function?>` of the ``telephone`` :ref:`module<what is a module?>` in the ``src`` folder_

  .. code-block:: python
    :lineno-start: 72
    :emphasize-lines: 6-7

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }
        # reality = text(a_dictionary)
        reality = src.telephone.text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    def test_passing_a_class():

  still green because when ``src.telephone.text`` is called, Python_ follows this path

  .. code-block:: shell

    src.telephone.text
    src
    └── telephone.py
        └── def text(the_input):
            └── return f'I got: {the_input}'

  using the string_ representation of the :ref:`object<everything is an object>` in the curly braces ``{ }``

  .. code-block:: python

    a_dictionary = {
        'key0': 'value0',
        'keyN': [0, 1, 2, 'n'],
    }

    text(a_dictionary)
        text(the_input)
            the_input = {
                'key0': 'value0',
                'keyN': [0, 1, 2, 'n'],
            }
            return f'I got: {the_input}'
            return ("I got: {'key0': 'value0',"
                             'keyN': [0, 1, 2, 'n']}")

* I remove the commented line

  .. code-block:: python
    :lineno-start: 72

    def test_passing_a_dictionary():
        a_dictionary = {
            'key0': 'value0',
            'keyN': [0, 1, 2, 'n'],
        }

        reality = src.telephone.text(a_dictionary)
        my_expectation = f'I got: {a_dictionary}'
        assert reality == my_expectation


    def test_passing_a_class():

* I change the calls in the :ref:`assertions<what is an assertion?>` of :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 83
    :emphasize-lines: 2-5, 7-10, 12-15, 17-20, 22-25, 27-30, 32-35, 37-40, 42-45

    def test_passing_a_class():
        reality = src.telephone.text(object)
        my_expectation = "I got: <class 'object'>"
        # assert text(object) == "I got: <class 'object'>"
        assert reality == my_expectation

        reality = src.telephone.text(bool)
        my_expectation = "I got: <class 'bool'>"
        # assert text(bool) == "I got: <class 'bool'>"
        assert reality == my_expectation

        reality = src.telephone.text(int)
        my_expectation = "I got: <class 'int'>"
        # assert text(int) == "I got: <class 'int'>"
        assert reality == my_expectation

        reality = src.telephone.text(float)
        my_expectation = "I got: <class 'float'>"
        # assert text(float) == "I got: <class 'float'>"
        assert reality == my_expectation

        reality = src.telephone.text(str)
        my_expectation = "I got: <class 'str'>"
        # assert text(str) == "I got: <class 'str'>"
        assert reality == my_expectation

        reality = src.telephone.text(tuple)
        my_expectation = "I got: <class 'tuple'>"
        # assert text(tuple) == "I got: <class 'tuple'>"
        assert reality == my_expectation

        reality = src.telephone.text(list)
        my_expectation = "I got: <class 'list'>"
        # assert text(list) == "I got: <class 'list'>"
        assert reality == my_expectation

        reality = src.telephone.text(set)
        my_expectation = "I got: <class 'set'>"
        # assert text(set) == "I got: <class 'set'>"
        assert reality == my_expectation

        reality = src.telephone.text(dict)
        my_expectation = "I got: <class 'dict'>"
        # assert text(dict) == "I got: <class 'dict'>"
        assert reality == my_expectation


    # Exceptions seen

  the test is still green.

* I remove the commented lines from :ref:`test_passing_a_class`

  .. code-block:: python
    :lineno-start: 83

    def test_passing_a_class():
        reality = src.telephone.text(object)
        my_expectation = "I got: <class 'object'>"
        assert reality == my_expectation

        reality = src.telephone.text(bool)
        my_expectation = "I got: <class 'bool'>"
        assert reality == my_expectation

        reality = src.telephone.text(int)
        my_expectation = "I got: <class 'int'>"
        assert reality == my_expectation

        reality = src.telephone.text(float)
        my_expectation = "I got: <class 'float'>"
        assert reality == my_expectation

        reality = src.telephone.text(str)
        my_expectation = "I got: <class 'str'>"
        assert reality == my_expectation

        reality = src.telephone.text(tuple)
        my_expectation = "I got: <class 'tuple'>"
        assert reality == my_expectation

        reality = src.telephone.text(list)
        my_expectation = "I got: <class 'list'>"
        assert reality == my_expectation

        reality = src.telephone.text(set)
        my_expectation = "I got: <class 'set'>"
        assert reality == my_expectation

        reality = src.telephone.text(dict)
        my_expectation = "I got: <class 'dict'>"
        assert reality == my_expectation


    # Exceptions seen
    # AssertionError
    # NameError
    # TypeError
    # ModuleNotFoundError
    # AttributeError

* I remove the ``text`` :ref:`function<what is a function?>` from ``test_telephone.py``

  .. code-block:: python
    :linenos:

    import src.telephone


    def test_passing_none():
        reality = src.telephone.text(None)
        my_expectation = 'I got: None'
        assert reality == my_expectation


    def test_passing_booleans():

  all the tests are still green because all the :ref:`calls<how to call a function with input>` that were to the ``text`` :ref:`function<what is a function?>` of ``test_telephone.py`` in the ``tests`` folder_, now go to the ``text`` :ref:`function<what is a function?>` of ``telephone.py`` in the ``src`` folder_. When ``src.telephone.text`` is called Python_ follows this path

  .. code-block:: shell

    src.telephone.text
    src
    └── telephone.py
        └── def text(the_input):
            └── return f'I got: {the_input}'

* I add a git_ commit message in the other terminal_

  .. code-block:: python
    :emphasize-lines: 1-2

    git commit -am \
    'separate solution from tests'

  the terminal_ shows a summary of the changes then goes back to the command line.

----

*********************************************************************************
test_telephone
*********************************************************************************

Since the solution is separate from the tests, I can write the program_ that makes the tests pass without looking at ``test_telephone.py``.

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

* I close ``test_telephone.py``

* I delete the text in ``telephone.py`` and the terminal_ shows 10 failures. I start with the last :ref:`AttributeError<what causes AttributeError?>`

  .. code-block:: python

    FAILED ...::test_passing_none -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_booleans -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_an_integer -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_float -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_string -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_tuple -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_list -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_set -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_dictionary -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    FAILED ...::test_passing_a_class -
        AttributeError: module 'src.telephone'
                        has no attribute 'text'
    =================== 10 failed in A.BCs ===================


  Can you make the tests pass without looking at how I solve it below? You can come back to compare solutions when you are done or if you get stuck.

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

* I add the name to ``telephone.py``

  .. code-block:: python
    :linenos:
    :emphasize-lines: 1

    text

  the terminal_ is my friend, and shows :ref:`NameError<test_catching_name_error_in_tests>`

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
    == "I got: {'key0': 'value0',...
    FAILED ...::test_passing_a_class -
        assert <class 'object'> == "I got: <class 'object'>"

  they all expect the input (``value``) as part of the message

* I add a :ref:`return statement<the return statement>` with an :ref:`f-string<what is string interpolation?>`

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

* I close ``telephone.py``
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