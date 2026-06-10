.. meta::
  :description: Beginner Python TDD tutorial on None — the simplest data structure / singleton. Step-by-step red-green-refactor with unittest: test_what_is_none using assertIs / assertIsNone / assertIsNotNone, then exhaustive "is None a boolean / int / float / str / tuple / list / set / dict?" tests using assertIsNotNone + assertIsInstance + assertNotIsInstance. Learn exactly why None is not False, not 0, not '', not [], not {}, not 0.0; identity ("is") vs equality ("=="); common None gotchas; and how to test for absence of value. Reproduces real AssertionError messages including "unexpectedly identical: None", "unexpectedly None", and "X is not None". Builds directly on the AssertionError chapters (bare assert, assertIs, test_failure patterns) before booleans/truthiness. Full uv init + pytest-watcher + git workflow. Part of Jacob Itegboje's Pumping Python series.
  :keywords: Jacob Itegboje, Pumping Python, python None, what is None python, NoneType, python None vs False, python None vs 0, python None vs empty list, python None vs empty dict, is None vs == None, assertIsNone, assertIsNotNone, assertIs, assertIsNot, assertIsInstance, assertNotIsInstance, testing for None, None singleton, None identity, None in unittest, TDD None, None is not False, unexpectedly identical None, AssertionError unexpectedly None, False is not None, 0 is not None, simplest data structure python, python data structures TDD, red green refactor None, python None best practices, None vs falsy values, uv pytest-watcher none project

.. include:: ../../links.rst

.. _None: https://docs.python.org/3/library/constants.html?highlight=none#None

#################################################################################
what is None?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/NKvM2yqyIrQ?si=rXBUptys2D9ns9d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

None_ is used when there is no value. In Mathematics_ we use ``0`` to represent no quantity. In some languages or domains we use ``NULL``, in forms we use ``N/A`` when the options do not apply. In Python_ we can use None_.

I used :ref:`assertIs<another way to test if something is the same object as None>` and :ref:`assertIsNot<another way to test if something is NOT the same object as None>` in the :ref:`assertion_error project<what is an assertion?>` :ref:`test_assertion_error_w_none` in :ref:`AssertionError<what causes AssertionError?>`, where I saw that

* :ref:`True<test_what_is_true>` is NOT :ref:`None<what is None?>` and NOT equal to :ref:`None<what is None?>`
* :ref:`False<test_what_is_false>` is NOT :ref:`None<what is None?>` and NOT equal to :ref:`None<what is None?>`
* :ref:`None is None<what is None?>` and equal to :ref:`None<what is None?>`

----

*********************************************************************************
the chapters
*********************************************************************************

.. toctree::
  :titlesonly:
  :maxdepth: 1

  none
  AssertionError 3: use assertIsNotNone and assertIsNone<../../exceptions/AssertionError/AssertionError_3>

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`None (the simplest object)`
