.. include:: ../links.rst


#################################################################################
classes: test_classes_w_initializers
#################################################################################

.. contents:: table of contents
  :local:
  :depth: 1

----

*********************************************************************************
requirements
*********************************************************************************

:ref:`test_classes`

----

So far I have gone over how to define classes, attributes and methods. I now expand on this to show how to use classes.

When making a new class, we can define an initializer which is a :ref:`method<functions>` that can receive inputs to be used to customize instances/copies of the class

*********************************************************************************
red: make it fail
*********************************************************************************

I add a failing test to ``test_classes.py``

.. code-block:: python

  def test_classes_w_initializers(self):
      self.assertEqual(classes.Boy().sex, 'M')

the terminal shows :ref:`AttributeError`

*********************************************************************************
green: make it pass
*********************************************************************************

* I add a definition for the ``Boy`` class

  .. code-block:: python


    class Boy(object):

        pass

  the terminal shows another :ref:`AttributeError`

* I make the ``Boy`` class with an attribute called ``sex``

  .. code-block:: python


    class Boy(object):

        sex

  the terminal produces NameError_


* I add a definition for the ``sex`` attribute

  .. code-block:: python


    class Boy(object):

        sex = 'M'

  the terminal shows passing tests

*********************************************************************************
refactor: make it better
*********************************************************************************

* I add another assertion to ``test_classes_w_initializers`` this time for a ``Girl`` class but with a difference, I provide the value for the ``sex`` attribute when I call the class

  .. code-block:: python

    def test_classes_w_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')

  the terminal shows :ref:`AttributeError`

* I try the same solution I used for the ``Boy`` class then add a definition for the ``Girl`` class to ``classes.py``

  .. code-block:: python


    class Girl(object):

        sex = 'M'

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

    TypeError: Girl() takes no arguments

  - ``classes.Girl(sex='F')`` looks like a call to a :ref:`function<functions>`
  - I can define classes that take values by using an initializer
  - An initializer is a class :ref:`method<functions>` that allows customization of instances/copies of a `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_

* I add the initializer :ref:`method<functions>` called ``__init__`` to the ``Girl`` class

  .. code-block:: python


    class Girl(object):

        sex = 'F'

        def __init__(self):
            pass

  and the terminal shows :ref:`TypeError`

  .. code-block:: python

   TypeError: __init__() got an unexpected keyword argument 'sex'

* I make the signature of the ``__init__`` :ref:`method<functions>` take a keyword argument

  .. code-block:: python

    def __init__(self, sex=None):
        pass

  and the terminal shows passing tests

* I add another assertion

  .. code-block:: python

    def test_classes_w_initializers(self):
        self.assertEqual(classes.Boy().sex, 'M')
        self.assertEqual(classes.Girl(sex='F').sex, 'F')
        self.assertEqual(classes.Other(sex='?').sex, '?')

  and the terminal shows :ref:`AttributeError`

* I add a class definition to ``classes.py``

  .. code-block:: python


    class Other(object):

        sex = '?'

        def __init__(self, sex=None):
            pass

  the terminal shows passing tests

* Wait a minute, I just repeated the same thing twice.

  - I defined a `class <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ with a name
  - I defined an attribute called ``sex``
  - I defined an ``__init__`` :ref:`method<functions>` which takes in a ``sex`` keyword argument

* I am going to make it a third repetition by redefining the ``Boy`` class to match the ``Girl`` and ``Other`` class because it is fun to do bad things

  .. code-block:: python


    class Boy(object):

        sex = 'M'

        def __init__(self, sex=None):
            pass

  the terminal shows all tests still passing and I have now written the same thing 3 times. Earlier on I mentioned inheritance, and will now try to use it to remove this duplication so `I do not repeat myself`_

* I add a new class called ``Human`` to ``classes.py`` before the definition for ``Boy`` with the same attribute and :ref:`method<functions>` of the classes I am trying to abstract

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            pass

  the terminal still shows passing tests

* I change the definitions for ``Boy`` to inherit from the ``Human`` class and all tests are still passing

  .. code-block:: python


    class Boy(Human):

        sex = 'M'

        def __init__(self, sex=None):
            pass

* I remove the ``sex`` attribute from the ``Boy`` class and the tests continue to pass
* I remove the ``__init__`` method, then add the `pass <https://docs.python.org/3/reference/lexical_analysis.html#keywords>`_ placeholder

  .. code-block:: python


    class Boy(Human):

        pass

  all tests are still passing. Lovely

* What if I try the same thing with the ``Girl`` class and change its definition to inherit from the ``Human`` class?

  .. code-block:: python

    class Girl(Human):

        sex = 'F'

        def __init__(self):
            pass

* I remove the ``sex`` attribute and the terminal shows :ref:`AssertionError`
* I make the ``Human`` class to set the ``sex`` attribute in the parent initializer instead of at the child level

  .. code-block:: python


    class Human(object):

        sex = 'M'

        def __init__(self, sex='M'):
            self.sex = sex

  the terminal still shows :ref:`AssertionError`

* when I remove the ``__init__`` :ref:`method<functions>` from the ``Girl`` class

  .. code-block:: python


    class Girl(Human):

        pass

  the terminal shows passing tests. Lovely

* I wonder if I can do the same with the ``Other`` class? I change the definition to inherit from the ``Human`` class

  .. code-block:: python


    class Other(Human):

        pass

  the terminal shows passing tests

* One More Thing! I remove the ``sex`` attribute from the ``Human`` class

  .. code-block:: python

    class Human(object):

      def __init__(self, sex='M'):
          self.sex = sex

  all tests are passing, I have successfully refactored the 3 classes and abstracted a ``Human`` class from them

----


*********************************************************************************
review
*********************************************************************************

Why did that work?

* the ``Boy``, ``Girl`` and ``Other`` class now inherit from the ``Human`` class which means they all get the same :ref:`methods<functions>` and attributes that the ``Human`` class has, including the ``__init__`` method
* ``self.sex`` in each class is the ``sex`` attribute in the class, allowing its definition from inside the ``__init__`` method
* since ``self.sex`` is defined as a class attribute, it is accessible from outside the class as I do in the tests i.e ``classes.Girl(sex='F').sex`` and ``classes.Other(sex='?').sex``

----

:doc:`/code/code_classes`