.. include:: ../links.rst

.. _Xcode Command Line Tools: https://developer.apple.com/xcode/resources/

#################################################################################
MacOS requirements
#################################################################################

.. ATTENTION:: Do this only if you are using a MacOS_ computer. Windows_ users do :ref:`Linux/Windows Subsystem for Linux requirements` or :ref:`Windows without Windows Subsystem Linux requirements`

* copy and paste this in a terminal_ to install brew_ (The Missing Package Manager for MacOS), if you do not have it already

  .. code-block:: shell
    :emphasize-lines: 1

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  the terminal_ is my friend, and shows instructions about how to add brew_ to your path

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

  tree_ is a program for showing :ref:`directory structure<BONUS: learn directory relationships>` as a tree

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Click Here to setup your Integrated Development Environment the same way I set mine up<how I setup my Integrated Development Environment (IDE)>`