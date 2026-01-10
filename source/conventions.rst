.. meta::
  :description: Master Python coding conventions, including naming rules and data structure usage! Improve your code style and readability with these essential Python best practices.
  :keywords: Jacob Itegboje, Python conventions, Python naming conventions, Python data structures, Python style guide, Python best practices, Python code quality, PEP 8 Python

.. include:: /links.rst

#################################################################################
conventions
#################################################################################

The following are a few conventions to know in Python_

*********************************************************************************
CapWords
*********************************************************************************

:ref:`Class<classes>` names in Python_ are written in the CapWords format, where the first letter of every word in the name is capitalized

*********************************************************************************
names
*********************************************************************************

- class names are usually in :ref:`CapWords` for example

  .. code-block:: python

    class AClassName(object):

  I can use any case I want but :ref:`CapWords` keeps things consistent

- :ref:`variables<what is a variable?>` and :ref:`function/method<functions>` names are in ``snake_case`` for example

  .. code-block:: python

    def function_name(first_input, second_input, keyword_argument=None):
        ...


    variable_name = None

for more details see the :PEP:`Python Style Guide <8>`

.. _conventions_comments:

*********************************************************************************
comments
*********************************************************************************

Comments are represented by the hashtag or pound before the thing that is commented for example

.. code-block::

  # This is a comment

.. _conventions_enclosures:

*********************************************************************************
enclosures
*********************************************************************************

Enclosures must be closed once open, which means they happen in pairs for example

.. code-block:: python

  ""
  """"""
  ''
  ''''''
  ()
  []
  {}

The `Integrated Development Environment (IDE)`_ takes care of this

.. _conventions_quotes:

*********************************************************************************
quotes
*********************************************************************************

Quotes represent strings_ and can be single, double, triple single or triple double for example

.. code-block:: python

  "Double Quotes"

  'Single Quotes'

  """Text on different lines
  with
  triple double quotes
  """

  '''Text on different lines
  with
  triple double quotes
  '''

.. _conventions_tuples:

*********************************************************************************
tuples
*********************************************************************************

A tuple_ is a sequence or container of objects_ that cannot be changed later, it is immutable (cannot be changed later) and represented with parentheses/brackets (``()``), for example

.. code-block:: python

  (1, 2.5, "three", [4, 'five'])

.. _conventions_lists:

*********************************************************************************
lists
*********************************************************************************

A :ref:`list/array<lists>` is a sequence or container of objects_ that can be changed after it is defined, it is mutable (can change later) and represented with square brackets (``[]``), for example

.. code-block:: python

  [1, 2.5, 'three', (4, "five")]

.. _conventions_sets:

*********************************************************************************
sets
*********************************************************************************

A set_ is a container of objects_ that have no duplicates, and are represented with curly braces/brackets (``{}``)

.. code-block:: python

  {1, 2.5, 'three', (4, 'five')}

.. _conventions_dictionaries:

*********************************************************************************
dictionaries/mappings
*********************************************************************************

:ref:`Dictionaries/Mappings<dictionaries>` are also represented with curly braces/brackets (``{}``) but have :ref:`key-value pairs<test_items_returns_iterable_of_key_value_pairs_of_a_dictionary>`, for example

.. code-block:: python

  {
      'integer': 1,
      'floating_point': 2.5,
      'string': 'three',
      'tuple': (1, 2.5, "three", [4, 'five'])
      'list': [1, 2.5, 'three', (4, "five")]
      'set': {1, 2.5, 'three', (4, 'five')}
  }

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->