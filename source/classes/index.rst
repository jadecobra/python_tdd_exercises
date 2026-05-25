.. meta::
  :description: Master Python classes and Object-Oriented Programming (OOP) with this beginner-friendly TDD guide. Learn to define classes using the class keyword, implement class attributes (variables) and methods (functions), and follow CapWords naming conventions. Explore step-by-step concepts of objects, functions vs methods, and inheritance. Features hands-on tests and solutions to help novice programmers build strong foundational coding habits.
  :keywords: Jacob Itegboje, Pumping Python, Python classes, what is a class Python, OOP for beginners, Object-Oriented Programming Python, Python class syntax, class attribute, Python class methods, class vs object Python, how to make a class in Python, CapWords format, Python inheritance, function vs method, Python programming tutorial for beginners, Python TDD exercises, test-driven development class

.. include:: ../links.rst

.. _class: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
.. _classes: class_

#################################################################################
what is a class?
#################################################################################

A class_ is a definition for something. I think of it as :ref:`attributes (variables)<what causes AttributeError?>` and :ref:`methods (functions) <what is a function?>` that belong together.

Everything in Python_ is an object_, which is a class_. This means that everything in Python_ has a class_ definition somewhere. Knowing how classes_ work and how to make them shows how everything in Python_ works.

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
* :ref:`attributes<what is a class attribute?>` (optional)
* :ref:`methods<what is a method?>` (optional)

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

----

*************************************************************************************
what is next?
*************************************************************************************


* :ref:`classes`
* :ref:`inheritance<family ties>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->