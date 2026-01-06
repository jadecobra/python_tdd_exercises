.. include:: /links.rst

#################################################################################
can we measure learning?
#################################################################################

What follows is an exercise in measuring learning. It is somewhat philosophical in its meaning but arithmetic_ in its representation. I am curious to know what you think and what solutions you come up with

*********************************************************************************
An Infinite Learning Model
*********************************************************************************

=================================================================================
:red:`RED`: make it fail
=================================================================================

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``learning`` as the name of the project

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.sh learning

  .. attention:: on Windows without `Windows Subsystem for Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: shell

      ./makePythonTdd.ps1 learning

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_learning.py:7: AssertionError

* I hold :kbd:`ctrl` (Windows_/Linux_) or ``option or command`` (MacOS_) on the keyboard and use the mouse to click on ``tests/test_learning.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change :ref:`True<test_what_is_true>` to :ref:`False<test_what_is_false>` to make the test pass
* and change the text in ``test_learning.py`` with

  .. literalinclude:: /code/tests/test_learning_models.py

* the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.learning' has no attribute 'model'


=================================================================================
:green:`GREEN`: make it pass
=================================================================================

If you've gone through any of the other exercises in this book, then you have what you need to solve these problems

I would love to see your solutions, please send them to `jacobitegboje@gmail.com <jacobitegboje@gmail.com>`_

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