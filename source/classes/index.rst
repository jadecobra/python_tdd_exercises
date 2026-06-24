.. meta::
  :description: Master Python classes and Object-Oriented Programming (OOP) with this beginner-friendly TDD guide. Learn to define classes using the class keyword, implement class attributes (variables) and methods (functions), and follow CapWords naming conventions. Explore step-by-step concepts of objects, functions vs methods, and inheritance. Features hands-on tests and solutions to help novice programmers build strong foundational coding habits.
  :keywords: Jacob Itegboje, Pumping Python, Python classes, what is a class Python, OOP for beginners, Object-Oriented Programming Python, Python class syntax, class attribute, Python class methods, class vs object Python, how to make a class in Python, CapWords format, Python inheritance, function vs method, Python programming tutorial for beginners, Python TDD exercises, test-driven development class

.. include:: ../links.rst

.. _class: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
.. _classes: class_
.. _object: https://docs.python.org/3/glossary.html#term-object
.. _objects: object_

#################################################################################
what is a class?
#################################################################################

I think of classes_ as :ref:`attributes (variables)<what is a class attribute?>` and :ref:`methods (functions) <what is a method?>` that belong together.

Everything in Python_ is an object_, which is another word for a class_, it means that everything in Python_ has a class_ definition somewhere. Knowing how classes_ work and how to make them shows how everything in Python_ works or at least that they are :ref:`attributes (variables) <what is a class attribute?>` and :ref:`methods (functions)<what is a method?>` that belong together.

----

*********************************************************************************
what is a class attribute?
*********************************************************************************

A :ref:`class attribute<what is a class attribute?>` is a :ref:`variable<what is a variable?>` that belongs to a class_.

----

*********************************************************************************
what is a method?
*********************************************************************************

A :ref:`method<what is a method?>` is a :ref:`function<what is a function?>` that belongs to a class_.

----

*********************************************************************************
how to make a class
*********************************************************************************

classes_ are made with

* the class_ keyword
* a name in :ref:`CapWords format<CapWords>` (use a name that tells what the group of :ref:`attributes<what is a class attribute?>` and :ref:`methods<what is a method?>` does - naming things is its own challenge)
* parentheses and the parent class (optional) with a colon at the end
* :ref:`attributes<what is a class attribute?>`
* :ref:`methods<what is a method?>`

.. code-block:: python

  class NameOfClass(ParentClass):

      attribute = SOMETHING

      def method():
          the body of the method
          ...

----

*********************************************************************************
the chapters
*********************************************************************************

.. toctree::
  :titlesonly:
  :maxdepth: 1

  classes
  inheritance
  ../exceptions/AssertionError/AssertionError_2
  family_ties
  ../functions/functions_4

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`classes`