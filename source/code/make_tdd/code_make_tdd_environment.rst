
#############################################################################****
How to Automatically Make a Test Driven Development Environment
#############################################################################****

makePythonTdd.sh
*****************************************************************************

* Here is the ``./makePythonTdd.sh`` script from :doc:`/how_to/make_tdd_environment`

  .. literalinclude:: makePythonTdd.sh
    :language: shell

* use ``chmod`` to make the program executable

  .. code-block:: python

    chmod +x makePythonTdd.sh

* give a name for the ``$PROJECT_NAME`` variable when the program is called to setup a Test Driven Development on demand. for example typing this command in the terminal in the folder where ``makePythonTdd.sh`` is saved will setup a Test Driven Development environment for a project called ``calculator``

  .. code-block:: shell

    ./makePythonTdd.sh calculator


makePythonTdd.ps1
*****************************************************************************

* Here is the ``./makePythonTdd.ps1`` script from :doc:`/how_to/make_tdd_environment`

  .. literalinclude:: makePythonTdd.ps1
    :language: PowerShell

* give a name for the ``$PROJECT_NAME`` variable when the program is called to setup a Test Driven Development on demand. for example typing this command in the terminal in the folder where ``makePythonTdd.ps1`` is saved will setup a Test Driven Development environment for a project called ``calculator``

  .. code-block:: shell

    ./makePythonTdd.ps1 calculator