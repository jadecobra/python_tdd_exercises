.. include:: /links.rst

#################################################################################
can we measure learning?
#################################################################################

What follows is an exercise in measuring learning. It is somewhat philosophical in its meaning but arithmetic_ in its representation. I am curious to know what you think and what solutions you come up with

*********************************************************************************
An Infinite Learning Model
*********************************************************************************

red: make it fail
#################################################################################

* I open a terminal_ to run :ref:`makePythonTdd.sh` with ``learning`` as the name of the project

  .. code-block:: python
    :emphasize-lines: 1

    ./makePythonTdd.sh learning

  .. admonition:: on Windows without `Windows Subsystem Linux`_ use :ref:`makePythonTdd.ps1` instead of :ref:`makePythonTdd.sh`

    .. code-block:: python

      ./makePythonTdd.ps1 learning

  it makes the folders_ and files_ that are needed, installs packages_, runs the first test, and the terminal_ shows :ref:`AssertionError`

  .. code-block:: python

    E       AssertionError: True is not false

    tests/test_learning.py:7: AssertionError

* I hold ``ctrl`` (windows/linux) or ``option`` (mac) on the keyboard and use the mouse to click on ``tests/test_learning.py:7`` to open it in the :ref:`editor<2 editors>`
* then I change ``True`` to ``False`` to make the test pass
* and change the text in ``test_learning.py`` with

  .. literalinclude:: /code/tests/test_learning_models.py

* the terminal_ shows :ref:`AttributeError`

  .. code-block:: shell

    AttributeError: module 'src.learning' has no attribute 'model'


green: make it pass
#################################################################################

If you've gone through any of the other exercises in this, then you have what you need to solve these problems

Please send me your solutions. I would love to see them