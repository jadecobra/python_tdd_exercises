.. include:: ../links.rst

#################################################################################
makePythonTdd
#################################################################################

*********************************************************************************
makePythonTdd with no variables
*********************************************************************************

* Here is the program_ from :ref:`how to run tests automatically`

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: make_tdd/makePythonTddNoVariables.sh
        :language: python
        :linenos:
        :caption: makePythonTdd.sh
        :emphasize-lines: 2-3, 10, 18

      * use chmod_ in the terminal_ to make the program_ executable

        .. code-block:: python
          :emphasize-lines: 1

          chmod +x makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: make_tdd/makePythonTddNoVariables.ps1
        :language: python
        :linenos:
        :caption: makePythonTdd.ps1
        :emphasize-lines: 1-2, 9, 17

* change ``more_magic`` to the name of your Project
* type this in the terminal_ to run the program_ to make a `Test Driven Development`_ any time you want

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

        .\makePythonTdd.ps1

----

*********************************************************************************
makePythonTdd with variables
*********************************************************************************

* Here is the program_ from :ref:`how to make a Python Test Driven Development environment automatically with variables`

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: make_tdd/makePythonTdd.sh
        :language: shell
        :caption: makePythonTdd.sh
        :linenos:

      * use chmod_ to make the program_ executable

        .. code-block:: python
          :emphasize-lines: 1

          chmod +x makePythonTdd.sh

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: make_tdd/makePythonTdd.ps1
        :language: PowerShell
        :caption: makePythonTdd.ps1
        :linenos:

* give a name for the ``NAME_OF_THE_PROJECT`` :ref:`variable<what is a variable?>` when the program_ is called to make a `Test Driven Development`_ any time you want. For example typing this command in the terminal_ in the folder_ where the program_ is saved makes a :ref:`Test Driven Development environment<what is a Test Driven Development Environment?>` for a project with the name :ref:`person<how to make a person>`

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

        .\makePythonTdd.ps1 person

----

*********************************************************************************
BONUS: makePythonTdd.sh Pro
*********************************************************************************

Since you are the adventurous type and made it this deep in the book, I have added extra lines that

* make the project with ``NAME_OF_THE_PROJECT`` as the name if you do not give a name
* make the class name in :ref:`CapWords format<CapWords>`

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: make_tdd/makePythonTddPro.sh
        :language: shell
        :linenos:
        :caption: makePythonTdd.sh
        :emphasize-lines: 2-3, 10-12, 22

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: make_tdd/makePythonTddPro.ps1
        :language: shell
        :linenos:
        :caption: makePythonTdd.ps1
        :emphasize-lines: 1-3, 7-9, 20