.. include:: ../../links.rst

#################################################################################
how to install Windows Subsystem for Linux on Windows
#################################################################################

This is one way to install `Windows Subsystem for Linux`_ on a Windows computer so you can use Linux_ on your Windows_ computer. It gives you more control, and your programming experience will be the same as mine in this book

----

*********************************************************************************
install Windows Subsystem for Linux
*********************************************************************************

Make sure your computer runs `Windows 11`_. If you cannot upgrade to `Windows 11`_, still try the steps below, if they do not work skip to :ref:`how to make a python test driven development environment on Windows without Windows Subsystem for Linux`

As of October 14th, 2025, `Microsoft stopped supporting Windows 10, Windows 8.1 and Windows 7 <https://www.microsoft.com/en-us/Windows/end-of-support?r=1>`_

* click ``Search`` at the bottom of your screen
* search for ``Turn on Windows features``
* click ``Turn on or off Windows Features`` from the results
* Make sure the following have check marks to the left of them in the dialog box that opens up

  - Hyper V (this might not be in the list, you can skip it if it is not)
  - Virtual Machine Platform
  - Windows Subsystem for Linux
  - Windows Hypervisor Platform

  Click ``OK`` to apply the changes if any
* Restart the computer when the installation finishes. You can go to the next steps while the above is installing

* click ``Search`` at the bottom of your screen
* type ``PowerShell``
* select ``Run as Administrator`` and a PowerShell_ terminal_ will open up
* type ``wsl --update`` to make sure you have the latest version of `Windows Subsystem for Linux`_
* Open the `Microsoft Store`_
* Search for Debian_

  .. image:: /_static/microsoft_store_debian.png
    :width: 600
    :align: center
    :alt: Debian in Microsoft Store

  .. TIP:: You can use any Linux Distribution you want, `Windows Subsystem for Linux`_ installs Ubuntu_ by default

* Click ``Get`` to install

* When the installation is successful the computer ask yous for a ``USERNAME``, use something that is easy for you to remember later

* Next it asks for a ``PASSWORD``, use something that is easy for you to remember later

  .. attention:: the terminal_ does not show any text while you type your password, hit ``enter/return`` when done and it asks you to type the password again to confirm it

* after installing `Windows Subsystem for Linux`_ open `Visual Studio Code`_ and install the `WSL extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_
* Press ``F1`` on the keyboard in `Visual Studio Code`_ and select ``WSL:Connect to WSL`` to open a terminal_ in `Windows Subsystem for Linux`_
* then type this in the terminal_ to update the Linux_ `package manager <https://manpages.debian.org/trixie/apt/apt.8.en.html>`_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt update

* type this to upgrade Linux_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt full-upgrade --yes

* type this in the terminal_ to install Python_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt install python3 python3-venv --yes

you can continue with :ref:`how to make a Python Test Driven Development environment manually`.

If installing `Windows Subsystem for Linux`_ does not work, you can use :ref:`how to make a python test driven development environment on Windows without Windows Subsystem for Linux` instead

.. NOTE::

  In some cases your `Windows Subsystem for Linux`_ installation might succeed and you will have errors with Debian_, you might have to enable virtualization from your BIOS, here's how to do that

  * restart your computer
  * as soon as it restarts, press the key to enter setup mode, this varies by manufacturer but is one of the following

    - Esc
    - F2
    - F10
    - F12
    - Alternately you can hold ``shift`` when your computer is restarting to enter ``Windows Recovery Mode`` then select ``UEFI Firmware Settings``

  * In BIOS mode select any variation of ``System Configuration`` and Enable ``Virtualization``

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to see me make a Python Test Driven Development environment?<how to make a Python Test Driven Development environment manually>`

----


.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->