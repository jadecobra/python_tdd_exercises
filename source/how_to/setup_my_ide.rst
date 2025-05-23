.. include:: ../links.rst

#################################################################################
how I setup my Integrated Development Environment (IDE)
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/pA9ko4xdkXI?si=hKDaMAPeZydgLDCn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

As of this writing I use `Visual Studio Code`_

.. contents:: table of contents
  :local:
  :depth: 2

*********************************************************************************
Screen Layout
*********************************************************************************

I split my screen in the following ways depending on the use case, try different layouts to see what works best for you.

for references
#################################################################################

I put references on the left and the Integrated Development Environment on the right

.. image:: /_static/setup_my_ide/reference_on_left.png
  :width: 600
  :alt: Reference on the left

this helps when I do not have an extra screen


for testing
#################################################################################

When working with just the Integrated Development Environment, I have the following windows open

* explorer on the left to see files/folder structure at once, and I can drag and drop files directly into the editor

  .. image:: /_static/setup_my_ide/explorer_w_editors.png
    :width: 600
    :alt: Explorer with Editors

* editors side by side - source code on the left with tests on the right

  .. image:: /_static/setup_my_ide/2_editors.png
    :width: 600
    :alt: Editors side by side

* the terminal to show results of the tests

  - at the bottom - for most cases

    .. image:: /_static/setup_my_ide/terminal_on_bottom.png
      :width: 600
      :alt: Terminal Window at the bottom

  - to the right - when the results I am looking at in the terminal are too long to see in the bottom, for example when working with documentation, JSON or :ref:`dictionaries`

    .. image:: /_static/setup_my_ide/terminal_on_right.png
      :width: 600
      :alt: Terminal Window on the right

This setup helps me answer 2 questions

* what is the same?
* what is different?

*********************************************************************************
Visual Studio Extensions
*********************************************************************************

Here are extensions I use in `Visual Studio Code`_

* `Code Spell Checker`_ - to catch spelling mistakes
* `indent-rainbow`_ - I like pretty colors and this makes indentation easier to see from a distance
* `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_ - Python language support with Pylance and a Python debugger
* `Dark Rainbow Theme`_  - did I mention I like pretty colors?

----