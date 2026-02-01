.. include:: ../links.rst

.. _download and install Python: https://www.python.org/downloads/
.. _Xcode Command Line Tools: https://developer.apple.com/xcode/resources/
.. _download and install git: https://git-scm.com/install/windows

#################################################################################
how I setup my computer for development
#################################################################################

I spend some time to set up my computer to make it easier to write programs_

----

*********************************************************************************
what is covered?
*********************************************************************************

These chapters show how I setup any computer for development

.. toctree::
  :titlesonly:
  :maxdepth: 1

  setup my computer<setup_my_ide>
  install WSL on Windows<install_wsl>

they cover the following

* :ref:`Windows requirements`
* :ref:`Linux/Windows Subsystem for Linux requirements`
* :ref:`Windows without Windows Subsystem Linux requirements`
* :ref:`MacOS requirements`

----

=================================================================================
Windows requirements
=================================================================================

----

* If you are using a Windows_ computer, :ref:`install Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>`
* If you cannot :ref:`install Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>`, do not worry, every chapter of the book has something for you

----

=================================================================================
Linux/Windows Subsystem for Linux requirements
=================================================================================

----

.. ATTENTION:: Do this only if you are using Linux_ or `Windows Subsystem for Linux`_. MacOS_ users should not do this section

* Open a terminal_ then type this to update the `Linux package manager`_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt update

  .. TIP:: you can do a full upgrade if you want

  .. code-block:: shell

    sudo apt full-upgrade --yes

* type this in the terminal_ to install Python_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt install python3 python3-venv --yes

* type this to install the `uv Python package manager`_

  .. code-block:: shell
    :emphasize-lines: 1

    python3 -m pip install uv

  uv_ is a program_ that is used to install `Python packages`_

* use apt_ to install tree_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt install tree --yes

  tree_ is a program for showing :ref:`directory structure<BONUS: learn directory structure>` as a tree

* use apt_ to install git_

  .. code-block:: python
    :emphasize-lines: 1

    sudo apt install git --y

  git_ is a program for keeping track of changes I make in a project, it might already be installed

:ref:`Click HERE to see how I setup my Integrated Development Environment (IDE)<how I setup my Integrated Development Environment (IDE)>`

----

=================================================================================
Windows without Windows Subsystem Linux requirements
=================================================================================

----

.. ATTENTION:: Do this only if you are using Windows_ and could not install `Windows Subsystem for Linux`_

* `download and install Python`_

* `download and install git`_, git_ is a program_ for keeping track of changes I make in a project

* open PowerShell_ and copy and paste the text below to install the `uv Python package manager`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

  uv_ is a program_ that is used to install `Python packages`_

:ref:`Click HERE to see how I setup my Integrated Development Environment (IDE)<how I setup my Integrated Development Environment (IDE)>`

----

=================================================================================
MacOS requirements
=================================================================================

----

.. ATTENTION:: Do this only if you are using a MacOS_ computer. Windows_ users should not do this section

* `download and install Python`_

* copy and paste this in a terminal_ to install brew_ (The Missing Package Manager for MacOS), if you do not have it already

  .. code-block:: shell
    :emphasize-lines: 1

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  the terminal_ shows instructions about how to add brew_ to your path

* after installation it has instructions, copy and paste the 3 lines it shows in the terminal_ then use :kbd:`return` on the keyboard to run it, the terminal_ will not show anything if the commands run successfully

* Open a terminal_ then type this to install the `uv Python package manager`_

  .. code-block:: python
    :emphasize-lines: 1

    brew install uv

  uv_ is a program_ that is used to install `Python packages`_

* use brew_ to install tree_

  .. code-block:: shell
    :emphasize-lines: 1

    brew install tree

  tree_ is a program for showing :ref:`directory structure<BONUS: learn directory structure>` as a tree

* install git_ with `Xcode Command Line Tools`_

  .. code-block:: shell
    :emphasize-lines: 1

    xcode-select --install

  git_ is a program for keeping track of changes I make in a project

:ref:`Click HERE to see how I setup my Integrated Development Environment (IDE)<how I setup my Integrated Development Environment (IDE)>`

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Click Here to setup your Integrated Development Environment the same way I set mine up<how I setup my Integrated Development Environment (IDE)>`

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->