.. include:: links.rst

#################################################################################
dot notation
#################################################################################

You have made it to the end of this book. Do you understand these?

* :ref:`module`
* :ref:`module.variable`
* :ref:`module.function()`
* :ref:`module.function(*args, **kwargs)`
* :ref:`module.AClass.attribute`
* :ref:`module.AClass.method()`
* :ref:`module.AClass.method(*args, **kwargs)`

----

*********************************************************************************
module
*********************************************************************************

- a file_ in ``module.py``

- used in a different file_

  .. code-block:: python

    import module

----

*********************************************************************************
module.variable
*********************************************************************************

- defined in ``module.py``

  .. code-block:: python

    variable = None

- used in a different file_

  .. code-block:: python

    import module

    module.variable

----

*********************************************************************************
module.function()
*********************************************************************************

- defined in ``module.py``

  .. code-block::  python

    def function():
        return None

- called in a different file_

  .. code-block:: python

    import module

    module.function()

----

*********************************************************************************
module.function(*args, **kwargs)
*********************************************************************************

- defined in ``module.py``

  .. code-block:: python

    def function(*args, **kwargs):

- called in a different file_

  .. code-block:: python

    import module

    module.function(*args, **kwargs)

----

*********************************************************************************
module.AClass.attribute
*********************************************************************************

- defined in ``module.py``

  .. code-block:: python

    class AClass(object):

        attribute = None

  used in a different file_

  .. code-block:: python

    import module

    child = module.AClass()
    child.attribute

- defined in ``module.py`` with ``__init__()`` :ref:`method<what is a function?>`

  .. code-block:: python

    class AClass(object):

        def __init__(self, attribute=None):
            self.attribute = attribute

  used in a different file_ and setting the value for ``attribute``

  .. code-block:: python

    import module

    child = module.AClass(attribute='Attribute')
    child.attribute

----

*********************************************************************************
module.AClass.method()
*********************************************************************************

- defined in ``module.py``

  .. code-block:: python

    class AClass(object):

        def method(self):
            return None

- used in a different file_

  .. code-block:: python

    import module

    child = module.AClass()
    child.method()

----

*********************************************************************************
module.AClass.method(*args, **kwargs)
*********************************************************************************

- defined in ``module.py``

  .. code-block:: python

    class AClass(object):

        def method(self, *args, **kwargs):
            return None

- used in a different file_

  .. code-block:: python

    import module

    child = module.AClass()
    child.method(*args, **kwargs)

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