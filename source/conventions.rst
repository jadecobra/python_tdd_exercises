.. meta::
  :description: Master Python coding conventions, including naming rules and data structure usage! Improve your code style and readability with these essential Python best practices.
  :keywords: Jacob Itegboje, Python conventions, Python naming conventions, Python data structures, Python style guide, Python best practices, Python code quality, PEP 8 Python

.. include:: /links.rst

#################################################################################
conventions
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

The following are a few conventions to know in Python

*********************************************************************************
names
*********************************************************************************

- class names are usually in ``CamelCase`` for example

  .. code-block:: python

    class AClassName(object):

  you can use any case you like but TitleCase keeps things consistent

- variables (attributes) and :ref:`function (method)<functions>` names are in ``snake_case`` for example

  .. code-block:: python

    def function_name(argument_1, argument_2, keyword_argument=None):
    ...

    variable_name = None

for more details see :PEP:`Python Style Guide <8>`

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

Your Integrated Development Environment (IDE) will take care of this for you

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

A tuple is a sequence or container of data that cannot be changed later, it is immutable and represented with parentheses/brackets for example

.. code-block:: python

  (1, 2.5, "three", [4, 'five'])

.. _conventions_lists:

*********************************************************************************
lists
*********************************************************************************

A list/array is a sequence or container of data that can be changed after it is defined, it is mutable and represented with square brackets for example

.. code-block:: python

  [1, 2.5, 'three', (4, "five")]

.. _conventions_sets:

*********************************************************************************
sets
*********************************************************************************

Sets are represented with curly braces/brackets

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
