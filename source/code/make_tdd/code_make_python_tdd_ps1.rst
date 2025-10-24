.. include: ../../../links.rst

#################################################################################
makePythonTdd.ps1
#################################################################################

* Here is the ``./makePythonTdd.ps1`` script from :doc:`/how_to/make_tdd_environment`

  .. literalinclude:: makePythonTdd.ps1
    :language: PowerShell

* give a name for the ``$PROJECT_NAME`` variable when the program is called to make a `Test Driven Development`_ on demand. for example typing this command in the terminal in the folder where ``makePythonTdd.ps1`` is saved will make a `Test Driven Development`_ environment for a project called ``calculator``

  .. code-block:: shell

    ./makePythonTdd.ps1 calculator