.. _conventions:

#############################################################################
conventions
#############################################################################

----

.. contents:: table of contents
  :local:
  :depth: 1

----

The following are a few conventions to know in Python

.. _convention_comments:

*****************************************************************************
comments
*****************************************************************************

Comments are represented by the hashtag or pound before the thing that is commented for example

.. code-block::

  # This is a comment

.. _convention_enclosures:

*****************************************************************************
enclosures
*****************************************************************************

Enclosures must be closed once open, which means they happen in pairs for example

.. code-block:: python

  ""
  """"""
  ''
  ''''''
  ()
  []
  {}

Your Interactive Development Environment (IDE) will take care of this for you

.. _convention_quotes:

*****************************************************************************
quotes
*****************************************************************************

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

.. _convention_tuples:

*****************************************************************************
tuples
*****************************************************************************

A tuple is a sequence or container of data that cannot be changed later, it is immutable and represented with parentheses/brackets for example

.. code-block:: python

  (1, 2.5, "three", [4, 'five'])

.. _convention_lists:

*****************************************************************************
lists
*****************************************************************************

A list/array is a sequence or container of data that can be changed after it is defined, it is mutable and represented with square brackets for example

.. code-block:: python

  [1, 2.5, 'three', (4, "five")]

.. _convention_sets:

*****************************************************************************
sets
*****************************************************************************

Sets are represented with curly braces/brackets

.. code-block:: python

  {1, 2.5, 'three', (4, 'five')}

.. _convention_dictionaries:

*****************************************************************************
dictionaries
*****************************************************************************

Dictionaries/Mappings are also represented with curly braces/brackets but have key/value pairs

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