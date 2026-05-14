.. include:: ../../links.rst

#################################################################################
makePythonTdd
#################################################################################

*********************************************************************************
makePythonTdd with no variables
*********************************************************************************

* Here is the program_ from :ref:`how to make a Python Test Driven Development environment automatically`

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: makePythonTddNoVariables.sh
        :language: python
        :linenos:
        :emphasize-lines: 2-3, 5, 12, 20

      * use chmod_ in the terminal_ to make the program_ executable

        .. code-block:: python
          :emphasize-lines: 1

          chmod +x makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: makePythonTddNoVariables.ps1
        :language: python
        :linenos:
        :emphasize-lines: 1-2, 4, 11, 19

* change ``more_magic`` to the name of your Project and when the program_ is called to make a `Test Driven Development`_ any time you want

* type this in the terminal_ to run the program_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.ps1

----

*********************************************************************************
makePythonTdd with variables
*********************************************************************************

* Here is the program_ from :ref:`how to make a Python test driven development environment 3`

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: makePythonTdd.sh
        :language: shell
        :linenos:

      * use ``chmod`` to make the program_ executable

        .. code-block:: python
          :emphasize-lines: 1

          chmod +x makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: makePythonTdd.ps1
        :language: PowerShell
        :linenos:

* give a name for the ``PROJECT_NAME`` :ref:`variable<what is a variable?>` when the program_ is called to make a `Test Driven Development`_ any time you want. For example typing this command in the terminal_ in the folder_ where the program_ is saved makes a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project with the name :ref:`person<how to make a person>`

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.sh person

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ./makePythonTdd.ps1 person

----

*********************************************************************************
BONUS: makePythonTdd.sh Pro
*********************************************************************************

Since you are the adventurous type and made it this deep in the book, I have added extra lines that

* make the project with ``PROJECT_NAME`` as the name if you do not give a name
* make the class name in :ref:`CapWords format<CapWords>`
* open the test file_ and source file_ in your editor

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: makePythonTddPro.sh
        :language: shell
        :linenos:
        :emphasize-lines: 2-6, 8-10, 12-15, 21, 29, 31-32

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: makePythonTddPro.ps1
        :language: shell
        :linenos:
        :emphasize-lines: 2, 3, 5, 12, 20, 22-23

``code src/$PROJECT_NAME.py`` and ``code tests/test_$PROJECT_NAME.py`` work with `Visual Studio Code`_ you can change ``code`` to use the command for any `Integrated Development Environment (IDE)`_ you like