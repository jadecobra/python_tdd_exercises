.. meta::
  :description: Beginner Python TDD tutorial on None — the simplest data structure / singleton. Step-by-step red-green-refactor with unittest in its own "none" project: test_what_is_none using assertIs + the new assertIsNone / assertIsNotNone (with real "unexpectedly identical: None", "unexpectedly None", "X is not None" AssertionErrors), then exhaustive "is None a boolean / int / float / str / tuple / list / set / dict?" tests using assertIsNotNone + assertIsInstance + assertNotIsInstance. Learn exactly why None is not False, not 0, not '', not [], not {}, not 0.0; identity ("is") vs equality ("=="); how to test for absence of value. Includes the caution box on assert* name ordering (IsNotNone vs NotIsInstance) because names match the statements they replace. Builds directly on AssertionError chapters (bare assert, assertIs, test_failure) before booleans/truthiness. Full uv init + pytest-watcher + git. Optional continuation in the assertion_error project (AssertionError 3) shows using assertIsNone/assertIsNotNone to clean test_assertion_error_w_none after class attributes. Part of Jacob Itegboje's Pumping Python series.
  :keywords: Jacob Itegboje, Pumping Python, python None, what is None python, NoneType, python None vs False, python None vs 0, python None vs empty list, python None vs empty dict, is None vs == None, assertIsNone, assertIsNotNone, assertIs, assertIsNot, assertIsInstance, assertNotIsInstance, testing for None, None singleton, None identity, None in unittest, TDD None, None is not False, unexpectedly identical None, AssertionError unexpectedly None, False is not None, 0 is not None, simplest data structure python, python data structures TDD, red green refactor None, python None best practices, None vs falsy values, uv pytest-watcher none project, assertIsNone unexpectedly None, assertIsNotNone unexpectedly identical, caution box assert methods name ordering, None not instance of bool int float str list dict set tuple

.. include:: ../../links.rst

.. _None: https://docs.python.org/3/library/constants.html?highlight=none#None

#################################################################################
what is None?
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/NKvM2yqyIrQ?si=rXBUptys2D9ns9d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

None_ is used when there is no value. In Mathematics_ we use ``0`` to represent no quantity. In some languages or domains we use ``NULL``, in forms we use ``N/A`` when the options do not apply. In Python_ we can use None_.

I used :ref:`assertIs<another way to test if something is the same object as None>` and :ref:`assertIsNot<another way to test if something is NOT the same object as None>` in :ref:`test_assertion_error_w_none` in :ref:`AssertionError<what causes AssertionError?>`, where I saw that

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
