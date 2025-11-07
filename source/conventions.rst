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

- variables (:ref:`attributes<AttributeError>`) and :ref:`function (method)<functions>` names are in ``snake_case`` for example

  .. code-block:: python

    def function_name(argument_1, argument_2, keyword_argument=None):
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

The Integrated Development Environment (IDE) takes care of this

.. _conventions_quotes:

*********************************************************************************
quotes
*********************************************************************************

Quotes represent strings_ and can be single, double, triple single or triple double for example

.. code-block:: python

  "Double Quotes"

  'Single Quotes'

  """Multiline Text
  with
  triple double quotes
  """

  '''Multiline Text
  with
  triple single quotes
  '''

.. _conventions_tuples:

*********************************************************************************
tuples
*********************************************************************************

A tuple_ is a sequence or container of objects_ that cannot be changed later, it is immutable and represented with parentheses/brackets for example

.. code-block:: python

  (1, 2.5, "three", [4, 'five'])

.. _conventions_lists:

*********************************************************************************
lists
*********************************************************************************

A :ref:`list/array<lists>` is a sequence or container of objects_ that can be changed after it is defined, it is mutable and represented with square brackets for example

.. code-block:: python

  [1, 2.5, 'three', (4, "five")]

.. _conventions_sets:

*********************************************************************************
sets
*********************************************************************************

A set_ is a container of objects_ that have no duplicates, are represented with curly braces/brackets

.. code-block:: python

  {1, 2.5, 'three', (4, 'five')}

.. _conventions_dictionaries:

*********************************************************************************
dictionaries/mappings
*********************************************************************************

:ref:`Dictionaries/Mappings<dictionaries>` are also represented with curly braces/brackets but have key/value pairs

.. code-block:: python

  {
      'integer': 1,
      'floating_point': 2.5,
      'string': 'three',
      'tuple': (1, 2.5, "three", [4, 'five'])
      'list': [1, 2.5, 'three', (4, "five")]
      'set': {1, 2.5, 'three', (4, 'five')}
  }
