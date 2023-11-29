
Conventions
===========

The following are a few conventions to know in python


* Comments are represented by the hashtag or pound before the thing that is commented for example

  .. code-block::

    # This is a comment

* Enclosures must be closed once open, which means they happen in pairs for example

  .. code-block:: python

    ""
    """"""
    ''
    ''''''
    ()
    []
    {}

  Your Interactive Development Environment (IDE) will take care of this for you

* Quotes represent strings and can be single, double, triple single or triple double for example

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

* A tuple is a sequence or collection of data that cannot be changed later, it is immutable and represented with parentheses/brackets for example

  .. code-block:: python

    (1, 2.5, "three", [4, 'five'])

* A list/array is a sequence or collection of data that can be changed after it is defined, it is mutable and represented with square brackets for example

  .. code-block:: python

    [1, 2.5, 'three', (4, "five")]

* Sets are represented with curly braces/brackets

  .. code-block:: python

    {1, 2.5, 'three', (4, 'five')}

* Dictionaries/Mappings are also represented with curly braces/brackets but contain key/value pairs

  .. code-block:: python

    {
        'integer': 1,
        'floating_point': 2.5,
        'string': 'three',
        'tuple': (1, 2.5, "three", [4, 'five'])
        'list': [1, 2.5, 'three', (4, "five")]
        'set': {1, 2.5, 'three', (4, 'five')}
    }