.. include:: ../links.rst

#################################################################################
how to install Windows Subsystem Linux on a Windows Machine
#################################################################################

Here is a manual way to install to install Linux_ with `Windows Subsystem Linux`_

----

Make sure your computer runs `Windows 11 <https://www.microsoft.com/en-us/software-download/windows11>`_

As of October 14th, 2025, `Microsoft stopped supporting Windows 10, Windows 8.1 and Windows 7 <https://www.microsoft.com/en-us/windows/end-of-support?r=1>`_

* search for ``Turn on windows features``
* click ``Search`` at bottom of screen
* click ``Turn on or off Windows Features``
* Make sure the following have check marks to the left of them

  - Hyper V
  - Virtual Machine Platform
  - Windows Subsystem Linux
  - Windows Hypervisor Platform

  Click ``OK`` to apply the changes

* Open Microsoft Store
* Search for ``Debian``

  .. TIP:: You can use any Linux Distribution you want, `Windows Subsystem Linux`_ installs Ubuntu by default

* Click ``Get`` to install

* When the installation is successful the computer will ask you for a ``USERNAME``, use something you will remember

* Next it will ask for a password, use something you will remember

  .. IMPORTANT:: the terminal will not show any test while you type your password, hit ``enter/return`` when done and it will ask you to retype the password to confirm it

* after installing `Windows Subsystem Linux`_ open `Visual Studio Code`_ and install the `WSL extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_
* Press ``F1`` on the keyboard and select ``WSL:Connect to WSL`` to open a terminal in `Windows Subsystem Linux`_
* type this in the terminal to update the linux_ package manager

  .. code-block:: shell

    sudo apt update

* type this in the terminal to install Python_

  .. code-block:: shell

    sudo apt install python3 python3-venv --yes

----

:ref:`makePythonTdd.sh`
:ref:`makePythonTdd.ps1`