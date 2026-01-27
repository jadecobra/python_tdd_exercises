.. include:: links.rst

#################################################################################
dot notation
#################################################################################

You have made it through the end of the book. Do you understand the following?

----

*********************************************************************************
AClass.attribute
*********************************************************************************

in the same file_

.. code-block:: python

  class AClass(object):

      attribute = None

or

.. code-block:: python

  class AClass(object):

      def __init__(self, attribute):
          self.attribute = attribute

----

*********************************************************************************
AClass.method()
*********************************************************************************

in the same file_

.. code-block:: python

  class AClass(object):

      def method(self):
          return None

----

*********************************************************************************
AClass.method(*args, **kwargs)
*********************************************************************************

in the same file_

.. code-block:: python

  class AClass(object):

      def method(self, *args, **kwargs):
          return None

----

*********************************************************************************
module.attribute
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

    attribute = None

- how to use it in a different file_

  .. code-block:: python

    import module

    module.attribute

----

*********************************************************************************
module.function()
*********************************************************************************

- the definiton in ``module.py``

  .. code-block::  python

    def function():
        return None

- how to use it in a different file_

  .. code-block:: python

    import module

    module.function()

----

*********************************************************************************
module.function(*args, **kwargs)
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

    def function(*args, **kwargs)

- how to use it in a different file_

  .. code-block:: python

    import module

    module.function(*args, **kwargs)

----

*********************************************************************************
module.AClass.attribute
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

    class AClass(object):

        attribute = None

- how to use it in a different file_

  .. code-block:: python

    import module

    instance = module.AClass()
    instance.attribute

- or the name in ``module.py``

  .. code-block:: python

    class AClass(object):

        def __init__(self, attribute):
            self.attribute = attribute

- how to use it in a different file_

  .. code-block:: python

    import module

    instance = module.AClass(attribute='Attribute')
    instance.attribute

----

*********************************************************************************
module.AClass.method()
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

    class AClass(object):

        def method(self):
            return None

- how to use it in a different file_

  .. code-block:: python

    import module

    instance = module.AClass()
    instance.method()

----

*********************************************************************************
module.AClass.method(*args, **kwargs)
*********************************************************************************

- the definiton in ``module.py``

  .. code-block:: python

    class AClass(object):

        def method(self, *args, **kwargs):
            return None

- how to use it in a different file_

  .. code-block:: python

    import module

    instance = module.AClass()
    instance.method(*args, **kwargs)

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