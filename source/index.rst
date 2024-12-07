.. pumping python documentation master file, made by
  sphinx-quickstart on Sun Oct 22 20:52:14 2023.
  You can adapt this file completely to your liking, but it should at least
  contain the root ``toctree`` directive.

.. include:: /links.rst

#################################################################################
pumping python: how I solve problems with test driven development
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/fxPgowISTA4?si=fHnq4SbtySWs696z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

My name is Jacob Itegboje and this is a collection of `Test Driven Development`_ exercises that have helped me use Python for more than a decade.
`Test Driven Development`_ is a way to write software with a focus on tests. I write tests for ideas to reach a goal or meet a requirement, and the results tell me if I am closer to the goal or not. I repeat the process until I get to the goal.

I recommend reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring`_, they both influenced the way I write programs.

*********************************************************************************
who is this book for?
*********************************************************************************

* If you are interested in Python, this book is for you
* If you just started your journey, CONGRATULATIONS! You picked Python from the many `programming languages <https://en.wikipedia.org/wiki/Programming_language>`_ out there, Celebrate it, this book is for you
* If you are new to `Test Driven Development`_ in Python, this book is for you
* If you already use Python but do not know any of the Exceptions_ below, this book is for you

  - :ref:`AssertionError`
  - :ref:`AttributeError`
  - IndexError_
  - KeyError_
  - :ref:`ModuleNotFoundError`
  - NameError_
  - :ref:`TypeError`
  - ValueError_

*********************************************************************************
how can I use this book?
*********************************************************************************

Start with :doc:`how to make a python test driven development environment </how_to/make_tdd_environment>` because it is needed by the other chapters,  then choose how you go through the chapters based on what you like, or you could go through the :ref:`how-tos` section step by step, the other chapters cover :ref:`exceptions<Exceptions>`, :doc:`data_structures/data_structures`, :ref:`functions`, and :ref:`classes`

Here are a few things I would do if I were in your shoes to make the process more fun

* type out the code portions of a chapter without copying and pasting
* at the end of a chapter, delete the tests and try to write them from memory or use the solution as a guide
* close the tests at the end of a chapter, delete the solution and try to write one with the terminal response as a guide
* try to write solutions using the tests from the :ref:`catalog_of_tests` as a guide
* try adding tests for any ideas I get as I go through a chapter, the sooner you start writing tests the better since it requires a different way of thinking
* I would not quit until I get to the end of a chapter, especially when it is hard, this is part of the experience when learning to solve problems, things get harder before they are easier because there is a lot of failure. I can always walk away to go do something different for a while, then come back and try again. If you take one small step at a time you eventually get where you want to go

If you like videos, there is one for each chapter at `<https://www.youtube.com/@JacobItegboje>`_

.. _how-tos:

*********************************************************************************
howtos
*********************************************************************************

.. toctree::
  :maxdepth: 1
  :titlesonly:

  how_to/setup_my_ide
  how_to/make_tdd_environment
  how_to/calculator
  how_to/pass_values
  how_to/make_person
  how_to/exception_handling_tests
  how_to/exception_handling_programs
  how_to/sleep_duration

*********************************************************************************
table of contents
*********************************************************************************

.. toctree::
  :maxdepth: 1
  :titlesonly:

  conventions
  exceptions/exceptions
  data_structures/data_structures
  functions/functions
  classes/classes
  tests<catalog_of_tests>
  tests and solutions<catalog_of_code>
  learning_models
  dot_notation
  review

*********************************************************************************
music
*********************************************************************************

Here are some music playlists I listen to while programming

.. raw:: html

  <iframe allow="autoplay *; encrypted-media *; fullscreen *; clipboard-write" frameborder="0" width="560" height="315" style="width:560;max-width:660px;overflow:hidden;border-radius:12px;" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation" src="https://embed.music.apple.com/us/playlist/beatstrumentals/pl.f54198ad42404535be13eabf3835fb22"></iframe>

----

.. raw:: html

  <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1uJ4BgylqE1PJ6Ua14laJf?utm_source=generator" width="560" height="375" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

----

.. raw:: html

  <iframe style="border-radius:12px" width="560" height="315" src="https://www.youtube-nocookie.com/embed/videoseries?si=4AjlrNFMuyInE1an&amp;list=PLWuEDVEvwXgqQZ-TPhLgmQSD7NsNlK_OW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


----

:ref:`search`
