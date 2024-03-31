#############################################################################
dot notation
#############################################################################

You have made it through the end of the book. Do you understand the following?

.. contents:: table of contents
  :local:

*****************************************************************************
Class.attribute
*****************************************************************************

in the same file

.. code-block:: python

    class Class(object):

        attribute = None

or

.. code-block:: python

    class Class(object):

        def __init__(self, attribute):
            self.attribute = attribute

*****************************************************************************
Class.method()
*****************************************************************************

in the same file

.. code-block:: python

    class Class(object):

        def method(self):
            return None

*****************************************************************************
Class.method(*args, **kwargs)
*****************************************************************************

in the same file

.. code-block:: python

    class Class(object):

        def method(self, *args, **kwargs):
            return None

*****************************************************************************
module.attribute
*****************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      attribute = None

- how to use in a different file

  .. code-block:: python

      import module

      module.attribute

*****************************************************************************
module.function()
*****************************************************************************

- the definiton in ``module.py``

  .. code-block::  python

      def function():
          return None

- how to use in a different file

  .. code-block:: python

      import module

      module.function()

*****************************************************************************
module.function(*args, **kwargs)
*****************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      def function(*args, **kwargs)

- how to use in a different file

  .. code-block:: python

      import module

      module.function(*args, **kwargs)

*****************************************************************************
module.Class.attribute
*****************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      class Class(object):

          attribute = None

  or

  .. code-block:: python

      class Class(object):

          def __init__(self, attribute):
              self.attribute = attribute

- how to use in a different file

  .. code-block:: python

      import module

      instance = module.Class(attribute='Attribute')
      instance.attribute

*****************************************************************************
module.Class.method()
*****************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      class Class(object):

          def method(self):
              return None

- how to use in a different file

  .. code-block:: python

      import module

      instance = module.Class()
      instance.method()

*****************************************************************************
module.Class.method(*args, **kwargs)
*****************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      class Class(object):

          def method(self, *args, **kwargs):
              return None

- how to use in a different file

  .. code-block:: python

      import module

      instance = module.Class()
      instance.method(*args, **kwargs)