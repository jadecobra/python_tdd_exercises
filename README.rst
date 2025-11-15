.. include:: source/links.rst


#################################################################################
pumping python: how I solve problems with test driven development
#################################################################################

`Watch this on YouTube <https://youtu.be/fxPgowISTA4?si=dluzEizJhlHXTSjX>`_

----

My name is Jacob Itegboje and this is a collection of `Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ exercises that have helped me use Python_for more than a decade.
`Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a way to write software with a focus on tests. I write tests for ideas to reach a goal or meet a requirement, and the results tell me if I am closer to the goal or not. I repeat the process until I get to the goal.

I recommend reading `Kent Beck’s <https://en.wikipedia.org/wiki/Kent_Beck>`_ `Test Driven Development by Example <https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_ and `Martin Fowler’s <https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)>`_ `Refactoring <https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/?_encoding=UTF8&pd_rd_w=dbNYL&content-id=amzn1.sym.579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_p=579192ca-1482-4409-abe7-9e14f17ac827&pf_rd_r=133-9769820-0728336&pd_rd_wg=bMVBp&pd_rd_r=c84a5de8-ec36-4bd1-9196-8fa05de41794&ref_=aufs_ap_sc_dsk>`_, they both influenced the way I write programs.

*********************************************************************************
who is this for?
*********************************************************************************

* If you are interested in Python_, this is for you
* If you just started your journey, CONGRATULATIONS! You picked Python_from the many `programming languages <https://en.wikipedia.org/wiki/Programming_language>`_ out there, Celebrate it, this is for you
* If you are new to `Test Driven Development <https://en.wikipedia.org/wiki/Test-driven_development>`_ in Python, this is for you
* If you already use Python_ but do not know any of the `Exceptions <https://www.pumpingpython.com/how_to/exception_handling_tests.html>`_ below, this is for you

  - `AssertionError <https://www.pumpingpython.com/exceptions/AssertionError.html>`_
  - `AttributeError <https://www.pumpingpython.com/exceptions/AttributeError.html>`_
  - `IndexError <https://www.pumpingpython.com/data_structures/lists/lists.html#test-index-error>`_
  - `KeyError <https://www.pumpingpython.com/data_structures/dictionaries/dictionaries.html#test-key-error>`_
  - `ModuleNotFoundError <https://www.pumpingpython.com/exceptions/ModuleNotFoundError.html>`_
  - `NameError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#NameError>`_
  - `TypeError <https://www.pumpingpython.com/exceptions/TypeError.html>`_
  - `ValueError <https://docs.python.org/3/library/exceptions.html?highlight=exceptions#ValueError>`_

*********************************************************************************
how can I use this?
*********************************************************************************

Start with `how to make a python test driven development environment <https://www.pumpingpython.com/how_to/make_tdd_environment.html>`_ because it is needed by the other chapters,  then choose how you go through the chapters based on what you like, or you could go through the **how tos** section step by step, the other chapters cover `errors <https://www.pumpingpython.com/exceptions/exceptions.html>`_, `data_structures <https://www.pumpingpython.com/data_structures/>`_, `functions <https://www.pumpingpython.com/functions.html>`_, and `classes <https://www.pumpingpython.com/classes.html>`_

Here are a few things I would do if I were in your shoes to make the process more fun

* type out the code portions of a chapter without copying and pasting
* at the end of a chapter, delete the tests and try to write them from memory or use the solution as a guide
* close the tests at the end of a chapter, delete the solution and try to write one with the terminal_ response as a guide
* try to write solutions using the tests from the `catalog of tests <https://www.pumpingpython.com/catalog_of_tests.html>`_ as a guide
* try adding tests for any ideas I get as I go through a chapter, the sooner you start writing tests the better since it requires a different way of thinking
* I would not quit until I get to the end of a chapter, especially when it is hard, this is part of the experience when learning to solve problems, things get harder before they are easier because there is a lot of failure. I can always walk away to go do something different for a while, then come back and try again. If you take one small step at a time you eventually get where you want to go

There are videos for every chapter, check them out here `Jacob Itegboje on YouTube <https://www.youtube.com/@JacobItegboje>`_

.. _how-tos:

*********************************************************************************
howtos
*********************************************************************************

* `how I setup my Integrated Development Environment <https://www.pumpingpython.com/how_to/setup_my_ide.html>`_
* `how to make a python test driven development environment <https://www.pumpingpython.com/how_to/make_tdd_environment.html>`_
* `how to make a calculator <https://www.pumpingpython.com/how_to/calculator.html>`_
* `how to pass values <https://www.pumpingpython.com/how_to/pass_values.html>`_
* `how to make a person <https://www.pumpingpython.com/how_to/make_person.html>`_
* `how to handle Exceptions in tests <https://www.pumpingpython.com/how_to/exception_handling_tests.html>`_
* `how to handle Exceptions in programs <https://www.pumpingpython.com/how_to/exception_handling_programs.html>`_
* `how to measure sleep duration <https://www.pumpingpython.com/how_to/sleep_duration/sleep_duration.html>`_

*********************************************************************************
table of contents
*********************************************************************************

* `conventions <https://www.pumpingpython.com/conventions.html>`_
* `errors <https://www.pumpingpython.com/exceptions/exceptions.html>`_
* `data_structures <https://www.pumpingpython.com/data_structures/>`_
* `truth_table <https://www.pumpingpython.com/data_structures/booleans/truth_table/truth_table.html>`_
* `functions <https://www.pumpingpython.com/functions.html>`_
* `classes <https://www.pumpingpython.com/classes.html>`_
* `catalog of tests <https://www.pumpingpython.com/catalog_of_tests.html>`_
* `tests and solutions <https://www.pumpingpython.com/catalog_of_code.html>`_
* `learning_models <https://www.pumpingpython.com/learning_models.html>`_
* `dot_notation <https://www.pumpingpython.com/dot_notation.html>`_
* `review <https://www.pumpingpython.com/review.html>`_

*********************************************************************************
music
*********************************************************************************

Here is a playlist I like to listen to when programming

* `BEATstrumentals on Apple Music <https://music.apple.com/us/playlist/beatstrumentals/pl.f54198ad42404535be13eabf3835fb22>`_
* `BEATstrumentals on Spotify <https://open.spotify.com/playlist/1uJ4BgylqE1PJ6Ua14laJf?utm_source=generator>`_
