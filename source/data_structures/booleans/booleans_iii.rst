.. include:: ../../links.rst

#################################################################################
booleans 3
#################################################################################

:ref:`Inheritance<family ties>` showed that a :ref:`class<what is a class?>` can have more than one parent, and the parents are not the same.

Earlier on, I tested if :ref:`booleans are Integers<is a boolean an integer or a float?>` and the tests showed that :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>` are both integers_ and :ref:`booleans<what are booleans?>` which begs the question - is bool_ a child of int_ or are they both parents of :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>`?

----

*********************************************************************************
open the project
*********************************************************************************

* I `change directory`_ to the ``booleans`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd booleans

  the terminal_ shows I am in the ``booleans`` folder_

  .. code-block:: shell

    .../pumping_python/booleans

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

    (.venv) .../pumping_python/booleans

* I use ``pytest-watcher`` to run the tests

  .. code-block:: python
    :emphasize-lines: 1

    uv run pytest-watcher --now  .

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    rootdir: .../pumping_python/booleans
    configfile: pyproject.toml
    collected 4 items

    tests/test_booleans.py ....                                      [100%]

    ======================== 4 passed in X.YZs =========================

* I hold :kbd:`ctrl` on the keyboard and click on ``tests/test_booleans.py`` to open it in the :ref:`editor<2 editors>`

----

*********************************************************************************
test_if_bool_is_an_int
*********************************************************************************

----

=================================================================================
:red:`RED`: make it fail
=================================================================================

----

I add a new test

.. code-block:: python
  :lineno-start: 49
  :emphasize-lines: 3-4

            self.assertEqual(True/1, 1)

        def test_if_bool_is_an_int(self):
            self.assertIsInstance(bool, int)


    # NOTES

the terminal_ shows :ref:`AssertionError<what causes AssertionError?>`

.. code-block:: shell

  AssertionError: <class 'bool'> is not an instance of <class 'int'>

the bool_ :ref:`class<what is a class?>` is not a child of the int_ :ref:`class<what is a class?>`

----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----

I change assertIsInstance_ to assertNotIsInstance_

.. code-block:: python
  :lineno-start: 51
  :emphasize-lines: 2

        def test_if_bool_is_an_int(self):
            self.assertNotIsInstance(bool, int)

the test passes

----

*********************************************************************************
review
*********************************************************************************

* :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are :ref:`booleans<what are booleans?>`
* :ref:`True<test_what_is_true>` and :ref:`False<test_what_is_false>` are also integers_
* bool_ is NOT a child of the int_ :ref:`class<what is a class?>`, they are different

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<data structures: list comprehensions: tests and solutions>`

----

*************************************************************************************
what is next?
*************************************************************************************

you have gone through a lot of things and know

* :ref:`how to make a test driven development environment manually<how to make a test driven development environment>`
* :ref:`how to raise AssertionError with assert methods<what causes AssertionError?>`
* :ref:`how to make functions<what is a function?>`
* :ref:`how to pass values from tests to functions<how to pass values>`
* :ref:`what is None and NOT None<what is None?>`
* :ref:`what is True and False in Python<what are booleans?>`
* :ref:`how to write programs that make decisions<truth table>`
* :ref:`how to make a calculator<how to make a calculator>`
* :ref:`how to test that an Exception is raised with assertRaises<how to test that an Exception is raised>`
* :ref:`how to handle Exceptions in programs with try...except...else<how to handle Exceptions (Errors) in programs>`
* :ref:`how to raise TypeError<TypeError>`
* :ref:`what you can do with Lists<lists>`
* :ref:`how to use list comprehensions<list comprehensions>`
* :ref:`how to make dictionaries with functions<how to make a person>`
* :ref:`what you can do with dictionaries<dictionaries>`
* :ref:`what you can do with classes<what is a class?>`

:ref:`Would you like to use one of the class methods with the calculator?<how to make a calculator 8>`

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