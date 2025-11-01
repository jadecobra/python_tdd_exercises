.. include:: ../../links.rst

#################################################################################
how to install Windows Subsystem Linux on Windows
#################################################################################

This is one way `Windows Subsystem Linux`_ on a Windows computer so you can use Linux_

----

Make sure your computer runs `Windows 11 <https://www.microsoft.com/en-us/software-download/windows11>`_

As of October 14th, 2025, `Microsoft stopped supporting Windows 10, Windows 8.1 and Windows 7 <https://www.microsoft.com/en-us/windows/end-of-support?r=1>`_

* click ``Search`` at bottom of your screen
* search for ``Turn on windows features``
* click ``Turn on or off Windows Features`` from the results
* Make sure the following have check marks to the left of them in the dialog box that opens up

  - Hyper V
  - Virtual Machine Platform
  - Windows Subsystem Linux
  - Windows Hypervisor Platform

  Click ``OK`` to apply the changes if any

* Open the `Microsoft Store`_
* Search for ``Debian``

  .. image:: /_static/setup_my_ide/microsoft_store_debian.png
    :width: 600
    :alt: Terminal Window on the right

  .. TIP:: You can use any Linux Distribution you want, `Windows Subsystem Linux`_ installs Ubuntu by default

* Click ``Get`` to install

* When the installation is successful the computer will ask you for a ``USERNAME``, use something you will remember

* Next it will ask for a password, use something you will remember

  .. attention:: the terminal will not show any text while you type your password, hit ``enter/return`` when done and it will ask you to retype the password to confirm it

* after installing `Windows Subsystem Linux`_ open `Visual Studio Code`_ and install the `WSL extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_
* Press ``F1`` on the keyboard while is `Visual Studio Code`_ and select ``WSL:Connect to WSL`` to open a terminal in `Windows Subsystem Linux`_
* Open a terminal then type this to update the Linux_ package manager

  .. code-block:: shell

    sudo apt update

* type this in the terminal to install Python_

  .. code-block:: shell

    sudo apt install python3 python3-venv --yes

you can continue with :ref:`how to manually make a python test driven development environment`. If installing `Windows Subsystem Linux`_ does not work, you can use :ref:`how to make a python test driven development environment on Windows without Windows Subsystem Linux` instead

----