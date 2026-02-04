.. include:: ../../links.rst

#################################################################################
makePythonTdd.ps1
#################################################################################

*********************************************************************************
makePythonTdd.sh program
*********************************************************************************

* Here is the ``makePythonTdd.ps1`` program_ from :ref:`how to make a python test driven development environment on Windows without Windows Subsystem for Linux`

  .. literalinclude:: makePythonTdd.ps1
    :language: PowerShell
    :linenos:

* give a name for the ``$PROJECT_NAME`` :ref:`variable<what is a variable?>` when the program_ is called to make a `Test Driven Development`_ any time you want. For example typing this command in the terminal_ in the folder_ where ``makePythonTdd.ps1`` is saved makes a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project with the name :ref:`person<how to make a person>`

  .. code-block:: PowerShell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 person

----

*********************************************************************************
BONUS: makePythonTdd.ps1 Pro
*********************************************************************************

Since you are the adventurous type and made it in here, I have added 2 lines for you that automate opening the test file_ and source file for the projects

.. literalinclude:: makePythonTddPro.ps1
  :language: shell
  :linenos:
  :emphasize-lines: 22-23

this works with `Visual Studio Code`_ you can change it to use the command for any `Integrated Development Environment (IDE)`_ you like