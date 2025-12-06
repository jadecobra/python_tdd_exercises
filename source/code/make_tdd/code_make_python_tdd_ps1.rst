.. include:: ../../links.rst

#################################################################################
makePythonTdd.ps1
#################################################################################

* Here is the ``./makePythonTdd.ps1`` program_ from :ref:`how to make a python test driven development environment on Windows without Windows Subsystem Linux`

  .. literalinclude:: makePythonTdd.ps1
    :language: PowerShell
    :linenos:

* give a name for the ``$PROJECT_NAME`` :ref:`variable<test_attribute_error_w_variables>` when the program_ is called to make a `Test Driven Development`_ any time you want. For example typing this command in the terminal_ in the folder where ``makePythonTdd.ps1`` is saved makes a `Test Driven Development`_ environment for a project called :ref:`calculator<how to make a calculator>`

  .. code-block:: shell
    :emphasize-lines: 1

    ./makePythonTdd.ps1 calculator