#################################################################################
dot notation
#################################################################################

You have made it through the end of the book. Do you understand the following?

*********************************************************************************
AClass.attribute
*********************************************************************************

in the same file

.. code-block:: python

    class AClass(object):

        attribute = None

or

.. code-block:: python

    class AClass(object):

        def __init__(self, attribute):
            self.attribute = attribute

*********************************************************************************
AClass.method()
*********************************************************************************

in the same file

.. code-block:: python

    class AClass(object):

        def method(self):
            return None

*********************************************************************************
AClass.method(*args, **kwargs)
*********************************************************************************

in the same file

.. code-block:: python

    class AClass(object):

        def method(self, *args, **kwargs):
            return None

*********************************************************************************
module.attribute
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      attribute = None

- how to use in a different file

  .. code-block:: python

      import module

      module.attribute

*********************************************************************************
module.function()
*********************************************************************************

- the definiton in ``module.py``

  .. code-block::  python

      def function():
          return None

- how to use in a different file

  .. code-block:: python

      import module

      module.function()

*********************************************************************************
module.function(*args, **kwargs)
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      def function(*args, **kwargs)

- how to use in a different file

  .. code-block:: python

      import module

      module.function(*args, **kwargs)

*********************************************************************************
module.AClass.attribute
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      class AClass(object):

          attribute = None

 how to use in a different file

  .. code-block:: python

      import module

      instance = module.AClass()
      instance.attribute

- or the definition in ``module.py``

  .. code-block:: python

      class AClass(object):

          def __init__(self, attribute):
              self.attribute = attribute

  how to use in a different file

  .. code-block:: python

      import module

      instance = module.AClass(attribute='Attribute')
      instance.attribute

*********************************************************************************
module.AClass.method()
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      class AClass(object):

          def method(self):
              return None

- how to use in a different file

  .. code-block:: python

      import module

      instance = module.AClass()
      instance.method()

*********************************************************************************
module.AClass.method(*args, **kwargs)
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

      class AClass(object):

          def method(self, *args, **kwargs):
              return None

- how to use in a different file

  .. code-block:: python

      import module

      instance = module.AClass()
      instance.method(*args, **kwargs)