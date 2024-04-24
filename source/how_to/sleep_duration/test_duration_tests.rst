.. include:: ../../links.rst

.. _test_duration_tests:

#################################################################################
how to measure sleep duration: test_duration_tests
#################################################################################

This is part 5 of a program that calculates the difference between a given wake and sleep time.

.. contents:: table of contents
  :local:
  :depth: 2

----

I want to write the program that makes the tests in ``test_sleep_duration.py`` pass

.. _test_duration_tests_red:

*********************************************************************************
red: make it fail
*********************************************************************************

I delete all the text in ``sleep_duration.py`` and the terminal shows an :ref:`AttributeError`

.. _test_duration_tests_green:

*********************************************************************************
green: make it pass
*********************************************************************************

* I add the name

  .. code-block:: python

    duration

  and get a NameError_

* then assign the name to :ref:`None`

  .. code-block:: python

  and get a :ref:`TypeError`

  .. code-block:: python

    TypeError: 'NoneType' object is not callable

* I change ``duration`` to a :ref:`function<functions>` to make it callable_

  .. code-block:: python

    def duration():
        return None

  which gives me another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'wake_time'

  and I add the name to the :ref:`function<functions>` signature with a default value of :ref:`None`

  .. code-block:: python

    def duration(wake_time=None):

  the terminal shows another :ref:`TypeError`

  .. code-block:: python

    TypeError: duration() got an unexpected keyword argument 'sleep_time'

  which I add to the signature with a default value of :ref:`None`
