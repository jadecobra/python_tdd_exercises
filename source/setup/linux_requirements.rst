.. include:: ../links.rst

#################################################################################
Linux/Windows Subsystem for Linux requirements
#################################################################################

----

.. ATTENTION:: Do this only if you are using Linux_ or `Windows Subsystem for Linux`_. :ref:`MacOS users go here instead<MacOS requirements>`

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

    sudo apt install python3 python3-venv curl --yes

* type this to install the `uv Python package manager`_

  .. code-block:: shell
    :emphasize-lines: 1

    curl -LsSf https://astral.sh/uv/install.sh | sh

  after it installs, there is a message about adding it to your path, run this in the terminal_

  .. code-block:: shell
    :emphasize-lines: 1

    source $HOME/.local/bin/env

  uv_ is a program_ that is used to install `Python packages`_

* use apt_ to install tree_

  .. code-block:: shell
    :emphasize-lines: 1

    sudo apt install tree --yes

  tree_ is a program for showing :ref:`directory structure<BONUS: learn directory relationships>` as a tree

* use apt_ to install git_

  .. code-block:: python
    :emphasize-lines: 1

    sudo apt install git --yes

  git_ is a program for keeping track of changes I make in a project, it might already be installed

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Click Here to setup your Integrated Development Environment the same way I set mine up<how I setup my Integrated Development Environment (IDE)>`