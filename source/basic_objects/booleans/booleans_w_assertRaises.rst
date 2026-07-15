.. meta::
  :description:
  :keywords:

.. include:: ../../links.rst

#################################################################################
booleans with assertRaises
#################################################################################

----


*********************************************************************************
preview
*********************************************************************************

I have these tests by the end of the chapter

.. literalinclude:: ../../code/booleans/test_booleans_w_assertRaises.py
  :language: python
  :linenos:

----

*********************************************************************************
open the project
*********************************************************************************



----

*********************************************************************************
use assertRaises
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

----



----

=================================================================================
:green:`GREEN`: make it pass
=================================================================================

----


----

=================================================================================
:yellow:`REFACTOR`: make it better
=================================================================================

----


----

*********************************************************************************
close the project
*********************************************************************************

* I close ``test_booleans.py``
* I click in the terminal_ where the tests are running
* I use :kbd:`q` on the keyboard to leave the tests. The terminal_ goes back to the command line.

* I `change directory`_ to the parent of ``booleans``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am back in the ``pumping_python`` directory_.

----

*********************************************************************************
review
*********************************************************************************

I know that :ref:`bool is an object<test_is_a_boolean_an_object>`
* bool_ only has two instances - :ref:`False<test_what_is_false>` and :ref:`True<test_what_is_true>`

In Python_ the following :ref:`objects<everything is an object>` are grouped as

* :ref:`False<test_what_is_false>`

  * an empty container (strings_, tuples_, :ref:`lists<what is a list?>`, sets_, :ref:`dictionaries<what is a dictionary?>`)
  * ``0``
  * ``0.0``
  * :ref:`None<what is None?>`

* :ref:`True<test_what_is_true>`

  * a container with things is :ref:`True<test_what_is_true>`
  * positive and negative numbers are :ref:`True<test_what_is_true>`

These things come in handy when I want :ref:`programs to make decisions<if statements>`, because they can choose what to do based on if the :ref:`data<basic objects>` is grouped as :ref:`False<test_what_is_false>` (``0``, empty or :ref:`None<what is None?>` ) or is grouped as :ref:`True<test_what_is_true>` (positive and negative numbers or has something in it).

:ref:`How many questions can you answer after going through this chapter?<questions about Booleans>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<booleans: tests>`

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
* :ref:`I know how to make a person say hello with f-strings<how to make a person with f-strings>`.
* :ref:`I know how to separate tests from solutions<separate and equal>`.
* :ref:`I know what causes AttributeError<what causes AttributeError?>`.
* :ref:`I know how to make a person with a class<how to make a person with a class>`.
* :ref:`I know that everything in Python is an object<everything is an object>`.
* :ref:`I know how to use the unittest library<another way to write tests>`.
* :ref:`I know how to use the datetime library<test person with datetime>`.
* :ref:`I know what None is<what is None?>`.
* :ref:`I know how to make a person with conditions<how to make a person with conditions>`.

:ref:`Would you like to test the truth table?<truth table>` It helps understand writing programs_ that make decisions based on :ref:`conditions<if statements>`.

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