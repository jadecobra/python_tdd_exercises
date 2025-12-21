.. meta::
  :description: Learn how to set up your VS Code for Python Test-Driven Development (TDD) with this step-by-step guide. Optimize your workflow and start writing cleaner code.
  :keywords: Jacob Itegboje, how to set up vscode for python tdd, python tdd workflow in vscode, best vscode extensions for python tdd, python test driven development setup, vscode python testing configuration, python tdd tutorial for beginners, visual studio code python tdd guide, automate python tests in vscode

.. include:: ../links.rst

#################################################################################
how I setup my Integrated Development Environment (IDE)
#################################################################################

.. raw:: html

  <iframe style="border-radius:12px" width="560"  height="315" src="https://www.youtube-nocookie.com/embed/pA9ko4xdkXI?si=hKDaMAPeZydgLDCn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

----

As of this writing I use `Visual Studio Code`_, you can download and install it or any `Integrated Development Environment (IDE)`_ of your choice. Here are a few options

* `Visual Studio Code`_
* `Sublime Text`_
* PyCharm_
* `other Integrated Development Environment (IDE) options`_

*********************************************************************************
Screen Layout
*********************************************************************************

I split my screen in the following ways depending on the use case, try different layouts to see what works best for you.

=================================================================================
for references
=================================================================================

I put references on the left and the `Integrated Development Environment (IDE)`_ on the right

.. image:: /_static/setup_my_ide/reference_on_left.png
  :width: 600
  :align: center
  :alt: Reference on the left

this helps when I do not have an extra screen. I can stack two editors on top of one another, `source code`_ on top, tests below, and the terminal_ below the tests

=================================================================================
for testing
=================================================================================

When working with just the `Integrated Development Environment (IDE)`_, I have the following Windows open

---------------------------------------------------------------------------------
explorer on left
---------------------------------------------------------------------------------
explorer on the left to see files/folder structure at once, and I can drag and drop files directly into the editor

.. image:: /_static/setup_my_ide/explorer_w_editors.png
  :width: 600
  :align: center
  :alt: Explorer with Editors

---------------------------------------------------------------------------------
2 editors
---------------------------------------------------------------------------------
editors side by side - `source code`_ on the left with tests on the right

.. image:: /_static/setup_my_ide/2_editors.png
  :width: 600
  :align: center
  :alt: Editors side by side

---------------------------------------------------------------------------------
the terminal
---------------------------------------------------------------------------------

the terminal_ to show results of the tests

* at the bottom - for most cases

  .. image:: /_static/setup_my_ide/terminal_on_bottom.png
    :width: 600
    :align: center
    :alt: terminal_ Window at the bottom

* to the right - when the results I am looking at in the terminal_ are too long to see in the bottom, for example when working with documentation, JSON_ or :ref:`dictionaries`

  .. image:: /_static/setup_my_ide/terminal_on_right.png
    :width: 600
    :align: center
    :alt: terminal_ Window on the right

This setup helps me answer 2 questions

* what is the same?
* what is different?

----

*********************************************************************************
Visual Studio Extensions
*********************************************************************************

Here are extensions I use in `Visual Studio Code`_

* `Code Spell Checker`_ - to catch spelling mistakes
* `indent-rainbow`_ - I like pretty colors and this makes indentation easier to see from a distance
* `Python Extension`_ - Python_ language support with Pylance_ and a Python_ debugger
* `Dark Rainbow Theme`_  - did I mention I like pretty colors?
* `Remote Development`_ - This allows me to work with `Windows Subsystem for Linux`_ or Linux_ on any computer

----

*********************************************************************************
BONUS!!!
*********************************************************************************

I have a :ref:`GIFT<BONUS: learn directory structure>` for you, since you made it this far. It makes going through your computer easier and :ref:`the next chapter<how to make a test driven development environment>` as well. This is how your computer is organized. :ref:`Click HERE for the BONUS!<BONUS: learn directory structure>`

----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->