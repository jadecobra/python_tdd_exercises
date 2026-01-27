.. meta::
  :description: Here are the Python coding conventions used in Pumping Python
  :keywords: Jacob Itegboje, Python conventions, Python naming conventions, Python data structures, Python style guide, Python best practices, Python code quality, PEP 8 Python

.. include:: /links.rst

#################################################################################
conventions
#################################################################################

The following are a few conventions to know in Python_

----

*********************************************************************************
names
*********************************************************************************

----

=================================================================================
CapWords
=================================================================================

----

:ref:`class<what is a class?>` names in Python_ are written in the CapWords format, where the first letter of every word in the name is capitalized, for example

.. code-block:: python

  class AClassName(object):

I can use any case I want but :ref:`CapWords` keeps things consistent

----

=================================================================================
how to use class methods and attributes
=================================================================================

----

:ref:`class<what is a class?>` :ref:`attributes<test_attribute_error_w_class_attributes>` and :ref:`methods<what is a function?>` can be used inside a :ref:`class<what is a class?>` with ``self``

for example

.. code-block:: python
  :emphasize-text: self

  class AClass(object):

      an_attribute

      def a_method(self):
          return self.an_attribute

      def another_method(self):
          return self.a_method()

* ``a_method`` can use the ``an_attribute`` :ref:`class attribute<test_attribute_error_w_class_attributes>` with ``self.an_attribute`` instead of ``AClass.an_attribute``
* ``another_method`` can use the ``a_method`` :ref:`method<what is a function?>` with ``self.method`` instead of ``AClass.a_method()``

.. NOTE:: ``self`` is Python_ convention, I can use any name I want

----

=================================================================================
snake_case
=================================================================================

----

:ref:`variables<what is a variable?>` and :ref:`function/method<what is a function?>` names are in lowercase with underscores in between when it is more than one word, for example

* :ref:`variables<what is a variable?>`

  .. code-block:: python

    variable_name = None

* :ref:`functions<what is a function?>`

  .. code-block:: python

    def function_name(*arguments, **keyword_arguments):

for more details see the :PEP:`Python Style Guide <8>`

----

*********************************************************************************
comments
*********************************************************************************

----

Comments are made with a hashtag/pound before the thing that is commented for example

.. code-block:: python

  # This is a comment

comments do not do anything, they are notes

----

*********************************************************************************
enclosures
*********************************************************************************

----

Enclosures must be closed once open, which means they happen in pairs for example

* quotes

  .. code-block:: python

    ""
    """"""
    ''
    ''''''

* parentheses

  .. code-block:: python

    ()

* square brackets/braces

  .. code-block:: python

    []

* curly brackets/braces

  .. code-block:: python

    {}

The `Integrated Development Environment (IDE)`_ takes care of this, it automatically closes them when you open one

----

*********************************************************************************
quotes
*********************************************************************************

----

Quotes are for strings_ and can be

* single

  .. code-block:: python

    'Single Quotes'

* double

  .. code-block:: python

    "Double Quotes"

* triple single which allows writing one string_ on many lines

  .. code-block:: python

    '''Text on different lines
    with
    triple double quotes
    '''

* triple double which allows writing one string_ on many lines

  .. code-block:: python

    """Text on different lines
    with
    triple double quotes
    """

----

.. _conventions_tuples:

*********************************************************************************
tuples
*********************************************************************************

----


A tuple_ is a sequence or container of :ref:`objects<what is a class?>` that cannot be changed later, this means it is immutable. They are represented with parentheses/brackets (``()``), for example

.. code-block:: python

  ()
  (0)
  (1, 2.5, "three", [4, 'five'])

----

.. _conventions_lists:

*********************************************************************************
lists
*********************************************************************************

----

A :ref:`list/array<lists>` is a sequence or container of :ref:`objects<what is a class?>` that can be changed after it is defined, it is mutable. They are represented with square brackets (``[]``) and the things in them are separated by commas, for example

.. code-block:: python

  []
  [0,]
  [1, 2.5, 'three', (4, "five")]

----

*********************************************************************************
sets
*********************************************************************************

----

A set_ is a container of :ref:`objects<what is a class?>` that have no duplicates, and are represented with curly braces/brackets (``{}``), for example

.. code-block:: python

  {1, 2.5, 'three', (4, 'five')}

----

*********************************************************************************
dictionaries/mappings
*********************************************************************************

----

:ref:`Dictionaries/Mappings<dictionaries>` are also represented with curly braces/brackets (``{}``) but have :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`, for example

.. code-block:: python

  {}
  {
      'integer': 1,
      'floating_point': 2.5,
      'string': 'three',
      'tuple': (1, 2.5, "three", [4, 'five'])
      'list': [1, 2.5, 'three', (4, "five")]
      'set': {1, 2.5, 'three', (4, 'five')}
      'dictionary': {
          'integer': 1,
          'floating_point': 2.5,
          'string': 'three',
          'tuple': (1, 2.5, "three", [4, 'five'])
          'list': [1, 2.5, 'three', (4, "five")]
          'set': {1, 2.5, 'three', (4, 'five')},
          'dictionary': ...
      }
  }

----

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