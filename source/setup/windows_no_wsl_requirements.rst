.. include:: ../links.rst

.. _download and install Python: https://www.python.org/downloads/

#################################################################################
Windows without Windows Subsystem Linux requirements
#################################################################################

.. ATTENTION:: Do this only if you are using Windows_ and could not install `Windows Subsystem for Linux`_

* `download and install Python`_

* `download and install git`_, a program_ for keeping track of changes I make in a project

* open PowerShell_ then copy and paste the text below to install the `uv Python package manager`_

  .. code-block:: PowerShell
    :emphasize-lines: 1

    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

  uv_ is a program_ that is used to install `Python packages`_

----

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Click Here to setup your Integrated Development Environment the same way I set mine up<how I set up my Integrated Development Environment (IDE)>`
