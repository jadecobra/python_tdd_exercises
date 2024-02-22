
#############################################################################****
Automatically Create a Test Driven Development Environment
#############################################################################****

createPythonTdd.sh
*****************************************************************************

* Here is the ``./createPythonTdd.sh`` script from :doc:`/how_to/create_tdd_environment`

  .. literalinclude:: createPythonTdd.sh
    :language: shell

* use ``chmod`` to make the program executable

  .. code-block:: python

    chmod +x createPythonTdd.sh

* give a name for the ``$PROJECT_NAME`` variable when the program is called to setup a Test Driven Development on demand. for example typing this command in the terminal in the folder where ``createPythonTdd.sh`` is saved will setup a Test Driven Development environment for a project called ``calculator``

  .. code-block:: shell

    ./createPythonTdd.sh calculator


createPythonTdd.ps1
*****************************************************************************

* Here is the ``./createPythonTdd.ps1`` script from :doc:`/how_to/create_tdd_environment`

  .. literalinclude:: createPythonTdd.ps1
    :language: PowerShell

* give a name for the ``$PROJECT_NAME`` variable when the program is called to setup a Test Driven Development on demand. for example typing this command in the terminal in the folder where ``createPythonTdd.ps1`` is saved will setup a Test Driven Development environment for a project called ``calculator``

  .. code-block:: shell

    ./createPythonTdd.ps1 calculator