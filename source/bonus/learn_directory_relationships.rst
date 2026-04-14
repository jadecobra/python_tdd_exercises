:orphan:

.. include:: ../links.rst

.. _Excel Spreadsheet: https://grokipedia.com/page/Microsoft_Excel
.. _Word Document: https://grokipedia.com/page/Microsoft_Word
.. _make directories: mkdir_
.. _change directories: cd_
.. _Get-ChildItem: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.6


#################################################################################
BONUS: learn directory relationships
#################################################################################

This exercise shows directories_ (folders_) and files_ on my computer and how they are related. Everything that happens on the computer ends up in a file_ in a directory_.

----

*************************************************************************************
preview
*************************************************************************************

I use these commands in the chapter to build each part of the tree below step by step to see how files_ and folders_ are related.

* mkdir_ to `make directories`_
* cd_ to `change directories`_
* ls_ to show what is in directories_
* tree_ to show the relationships between directories_
* touch_ to make empty files_
* mv_ to rename or move files_
* rm_ to remove directories_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTree
        :language: shell

    .. tab-item:: no WSL
      :sync: no_wsl

      .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTreeNoWsl
        :language: none

----

*********************************************************************************
questions about directory relationships
*********************************************************************************

There are answers to these questions in this chapter

* :ref:`what is a folder (directory)?<what is a folder?>`
* :ref:`what is a file?<what is a file?>`
* :ref:`how can I tell what directory I am in?<how to see what directory I am in>`
* :ref:`how can I change directories?<how to change directory>`
* :ref:`how can I make a directory?<how to make a directory>`
* :ref:`how can I see directory relationships?<how to look at directory relationships>`
* :ref:`how can I see what is in a directory?<how to see what is in a directory>`
* :ref:`how can I make an empty file?<how to make an empty file>`
* :ref:`how can I rename a file or directory?<how to rename a file or directory>`
* :ref:`how can I move a file or directory?<how to rename a file or directory>`
* :ref:`how can I use directory relationships?<how to use directory relationships>`
* :ref:`how can I remove a directory and everything inside it?<how to remove a directory and all the things in it>`

----

*********************************************************************************
what is a folder?
*********************************************************************************

A `folder (directory)`_ is a box for files_, it can also have other `folders (directories)`_. It helps keep things that should be together, in one place, the same way a folder in a file cabinet keeps files that should be together in one place.

I keep every project I work on in its own directory_. All the code in this book is kept in a folder_ named ``pumping_python``.

----

*********************************************************************************
what is a file?
*********************************************************************************

A file_ is a collection or container for text, like paper we write or print on and keep in a folder. Everything that happens on the computer ends up in files_. The name of a file_ can end with an extension to show what type of file_ it is. For example

* ``.py`` for a :ref:`Python module<what is a module?>`
* ``.txt`` for a `plain text file`_
* ``.sh`` for a `bash file`_
* ``.ps1`` for a `PowerShell file`_
* ``.doc`` for a `Word Document`_
* ``.xls`` for an `Excel Spreadsheet`_
* ``.html`` for a `HyperText Markup Language file`_
* ``.json`` for a `JavaScript Object Notation file`_
* ``.md`` for a `Markdown file`_

----

*********************************************************************************
note
*********************************************************************************

* The code I type is ``highlighted`` and comes after something like ``I type this in the terminal``
* The result of the code I type after I press :kbd:`enter/return` on the keyboard comes after something like ``the terminal shows ...``
* if you get a different result from what I promise then one of two things happened

  - I made a mistake or
  - You made a mistake

  To make sure it is my mistake check that you typed the same thing I typed. If you still have a different result after you check, email jacobitegboje@gmail.com or text 1-469-751-7595 with the error

* commands are given to the computer with space between arguments or options, for example

  .. code-block:: python

    command argument
    command --option
    command argument_1 argument_2 ... argument_N
    command --option_1 --option_2 ... --option_N
    command argument --option
    command --option

  .. NOTE::

    the space is important, it is how the computer knows what command you mean and what arguments or options you are giving, for example

    .. code-block:: python

      commandargument_1 argument_2

    tells the computer to run a command named ``commandargument_1`` with ``argument_2`` as the argument, while

    .. code-block:: python

      command argument_1 argument_2

    tells the computer to run a command named ``command`` with ``argument_1`` and ``argument_2`` as the arguments

* options for commands sometimes have a long and short form, for example ``--long_option`` could have ``-l`` as the short option, which means I can put many short options together like this

  .. code-block:: python

    command -abcd

  where ``a``, ``b``, ``c`` and ``d`` are different options

.. admonition:: if you have Windows_ without `Windows Subsystem for Linux`_, some of the commands and terminal_ output will be different, click on the tab where it shows `no WSL`, for example

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      You clicked on ``WSL/Linux/Mac``

    .. tab-item:: no WSL
      :sync: no_wsl

      You clicked on ``no WSL``

----

*********************************************************************************
requirements
*********************************************************************************

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I type this in a terminal_ to make sure the `tree program`_ is installed

      .. code-block:: python
        :emphasize-lines: 1

        tree

    * If it is not installed on the computer, the terminal_ shows

      .. code-block:: python

          tree: command not found

      see :ref:`how to install tree` to install tree_

    * If it is installed and there is nothing in the directory_, the terminal_ shows


      .. code-block:: python

        .

        0 directories, 0 files

    * If it is installed and there is something in the directory_, the terminal_ shows how they are related.

  .. tab-item:: no WSL
    :sync: no_wsl

    I type tree_

    .. code-block:: python

      Folder PATH listing
      Volume serial number is ABCD:EFGH
      C:.
      No subfolders exist

The `tree program`_ shows how files_ and folders_ on a computer are related, this helps to know how to go from one folder_ to another, because it shows the way I can go.

It is easier to go where I want, if I know where I am.

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

********************************************************************************************
how to install tree
********************************************************************************************

* :ref:`how to install tree on Linux/Windows Subsystem for Linux`
* :ref:`how to install tree on Windows without Windows Subsystem for Linux`
* :ref:`how to install tree on Mac OS`

----

---------------------------------------------------------------------------------
how to install tree on Linux/Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. ATTENTION:: Do this only if you are using Linux_ or `Windows Subsystem for Linux`_ and tree_ is not installed.

  :ref:`Click here if you have MacOS<how to install tree on Mac OS>`

.. code-block:: python
  :emphasize-lines: 1

  sudo apt update

I always do a full upgrade (you do not have to)

.. code-block:: python
  :emphasize-lines: 1

  sudo apt full-upgrade --yes

type this in the terminal_ to install tree_

.. code-block:: python
  :emphasize-lines: 1

  sudo apt install tree

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

---------------------------------------------------------------------------------
how to install tree on Windows without Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. ATTENTION:: Do this only if you are using Windows_ and could not install `Windows Subsystem for Linux`_

  :ref:`Click here if you have MacOS<how to install tree on Mac OS>`

no need to install tree_ because it comes with Windows_.

Click on the tab that says ``no WSL`` to see the commands or results if you have Windows_ without `Windows Subsystem for Linux`_. These are the commands I use

* `New-Item`_ for touch_
* ``tree /F`` for tree_ to show files_ and folders_
* ``tree`` for ``tree -d`` to show only directories_
* ``dir`` or `Get-ChildItem`_ or ``ls`` for ``ls --all/-a``
* `Remove-Item`_ for rm_

when you type pwd_ or tree_, the terminal_ shows ``\`` between folder_ names, not ``/``. Click the ``no WSL`` tab for an example

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. code-block:: python

      .../pumping_python/doe

  .. tab-item:: no WSL
    :sync: no_wsl

    .. code-block:: python

      Path
      ----
      C:\...\pumping_python\doe

Your tree will also look different because of different ways of drawing and sorting.

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

---------------------------------------------------------------------------------
how to install tree on Mac OS
---------------------------------------------------------------------------------

----

.. ATTENTION:: Do this only if you have MacOS_ and tree_ is not installed.

  If you have Windows_

  * :ref:`click here for how to install tree on Linux/Windows SubSystem for Linux<how to install tree on Linux/Windows Subsystem for Linux>` or
  * :ref:`click here for how to install tree on Windows without Windows SubSystem Linux<how to install tree on Windows without Windows Subsystem for Linux>`

type this in the terminal_ to install tree_

.. code-block:: python
  :emphasize-lines: 1

  brew install tree

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

********************************************************************************************
how to see what directory I am in
********************************************************************************************

I start with a check of where I am in the terminal_ because It is easier to go where I want, if I know where I am. I can do this with the pwd_ program

.. code-block:: python
  :emphasize-lines: 1

  pwd

the terminal_ shows

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. code-block:: python

      .../pumping_python

  .. tab-item:: no WSL
    :sync: no_wsl

    .. code-block:: python

      Path
      ----
      C:\...\pumping_python

if I am in the ``pumping_python`` folder_

* pwd_ shows the path/address of the folder_ I am in
* pwd_ means ``print working directory``, it prints the path/address of the directory_ I am in, to the terminal_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * each ``/`` shows a parent-child relationship
      * the first ``/`` is for ``root`` which is the first folder_ on the computer
      * the first ``/`` is the highest level


    .. tab-item:: no WSL
      :sync: no_wsl

      * each ``\`` shows a parent-child relationship
      * ``C:\`` is for ``root`` which is the first folder_ on the computer
      * ``C:\`` is the highest level

  .. ADMONITION:: do you want to see every file_ and folder_ on your computer as a tree?

    Type this in the terminal_

    .. tab-set::
      :sync-group: os

      .. tab-item:: WSL/Linux/Mac
        :sync: unix

        .. code-block:: python

          tree /

      .. tab-item:: no WSL
        :sync: no_wsl

        .. code-block:: python

          tree C:/

    it runs for a while because there are many files_ and folders_.

    Use :kbd:`ctrl+c` on the keyboard to stop it.

.. NOTE::

  - If you see ``pumping_python`` when you type ``pwd``, :ref:`click here to make 'doe'<the part where I make doe>`
  - If you see a different name, go to the next step - :ref:`how to change directory`

----

********************************************************************************************
how to change directory
********************************************************************************************

I use the `cd program`_ to change directories_

.. code-block:: python
  :emphasize-lines: 1

  cd pumping_python

`cd`_ means ``change directory``

the terminal_ shows

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    .. code-block:: python

      cd: no such file or directory: pumping_python

  .. tab-item:: no WSL
    :sync: no_wsl

    .. code-block:: python

      Set-Location: Cannot find path
                    'C:\...\pumping_python'
                    because it does not exist

this means the folder_ I want to go to is not in the folder_ where I am.

----

********************************************************************************************
how to make a directory
********************************************************************************************

* I use the `mkdir program`_ to make a `folder (directory)`_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir pumping_python

  - ``mkdir`` means ``make directory``
  - the terminal_ shows

    .. tab-set::
      :sync-group: os

      .. tab-item:: WSL/Linux/Mac
        :sync: unix

        .. code-block:: python

          .../pumping_python

      .. tab-item:: no WSL
        :sync: no_wsl

        .. code-block:: python

              Directory: C:\...

          Mode            LastWriteTime   Length  Name
          ----            -------------   ------  ----
          d-----    MM/DD/YYYY HH:MM A/PM         pumping_python

* I use cd_ to `change directory`_ to ``pumping_python``

  .. code-block:: python
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am in the ``pumping_python`` `folder (directory)`_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        .../pumping_python

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Path
        ----
        C:\...\pumping_python

  .. TIP:: I open the ``pumping_python`` folder_ to make sure I can see it in my `Integrated Development Environment (IDE)`_. Here is how to do that with `Visual Studio Code`_ from the terminal_

    .. code-block:: python
      :emphasize-lines: 1

      code .

    * A new `Visual Studio Code`_ window opens in the ``pumping_python`` directory_
    * I close the window I had before the new window to work only in the new window.
    * I open another terminal_ to continue

.. _the part where I make doe:

* I want to work in a directory_ named ``doe``, I try to `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        cd: no such file or directory: doe

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Set-Location: Cannot find path
                      'C:\...\pumping_python\doe'
                      because it does not exist

  ``doe`` is not in the ``pumping_python`` directory_, yet

* I use mkdir_ to make ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir doe

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        .../pumping_python

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

            Directory: C:\...

        Mode            LastWriteTime   Length  Name
        ----            -------------   ------  ----
        d-----    MM/DD/YYYY HH:MM A/PM

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am in the ``doe`` folder_ I just made

* I use pwd_ to see where I am

  .. code-block:: python
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        .../pumping_python/doe

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Path
        ----
        C:\...\pumping_python\doe

It is easier to go where I want, if I know where I am.

* :ref:`I know how to change directory<how to change directory>`
* :ref:`I know how to make a directory<how to make a directory>`

----

********************************************************************************************
how to see what is in a directory
********************************************************************************************

* I can use ls_ to see what is in a directory_ and see more information about the files_ and folders_ in it

  .. code-block:: python
    :emphasize-lines: 1

    ls

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      the terminal_ shows

      .. code-block:: python

        .../pumping_python/doe

      this directory_ is empty

      * ls_ has a few options. I try ls_ again with one of them

        .. code-block:: python
          :emphasize-lines: 1

          ls --all

        the terminal_ shows

        .. code-block:: python
          :emphasize-lines: 1

          .  ..

      .. attention::

        * on MacOS_ the terminal_ shows

          .. code-block:: none

            ls: unrecognized option `--all'

          ``--all`` is the long form of the option, use ``-a`` which is the short form of the option

          .. code-block:: python
            :emphasize-lines: 1

            ls -a

      - ``--all`` or ``-a`` tells ls_ to show all the things in the directory_ even those that start with ``.`` ( they are hidden by default)
      - I can hide a file_ or folder_ if I put ``.`` before its name, for example ``.hidden``

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        C:\...\pumping_python\doe

* I try to `change directory`_ to ``.``

  .. code-block:: python
    :emphasize-lines: 1

    cd .

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  - I am still in the same directory_
  - ``.`` is for the directory_ I am in
  - ``.`` is ``doe`` when I am in ``doe``
  - ``.`` is the working directory_

* I try cd_ with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  - I am back in the ``pumping_python`` directory_
  - ``..`` is for the parent of the directory_ I am in
  - ``..`` is ``pumping_python`` when I am in ``doe``
  - ``pumping_python`` is the parent of ``doe``
  - I can `change directory`_ from the directory_ I am in to its parent with ``cd ..``

:ref:`I know how to see what is in a directory<how to see what is in a directory>`

----

********************************************************************************************
how to look at directory relationships
********************************************************************************************

* I use cd_ to go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

* I can use the `tree program`_ to see the files_ and folders_ in a directory_ and how they are related. I type it in the terminal_ to see what is in the ``doe`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        .

        0 directories, 0 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Folder PATH listing
        Volume serial number is ABCD:EFGH
        C:.
        No subfolders exist

  there is nothing in ``doe``, it is empty

* I try to `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        cd: no such file or directory: jane

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Set-Location: Cannot find path
                      'C:\...\pumping_python\doe\jane'
                      because it does not exist

  ``jane`` is not a child of ``doe``, yet

* I use mkdir_ to make ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir jane

  the terminal_ goes back to the command line

* I use ls_ to see what is now in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: python

    jane

* I use tree_ to show what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 1-2

        .
        └── jane

        2 directories, 0 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 1-2

        C:.
        └── jane

  - ``jane`` is a child of ``doe``
  - ``.`` is the working directory_, which is ``doe`` in this case
  - the line in the tree that goes from ``.`` to ``jane`` shows I can go from ``doe`` right to ``jane``

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane

  I am in ``jane``

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  - ``doe`` is not a child of ``jane``
  - I cannot go from ``jane`` to ``doe`` this way

* I `change directory`_ back to the parent of ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  - I am back in ``doe``
  - ``..`` is for the parent of the directory_ I am in
  - I can `change directory`_ from the directory_ I am in to its parent with ``cd ..``
  - ``..`` is ``doe`` when I am in ``jane``

----

* I try to `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        cd: no such file or directory: john

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Set-Location: Cannot find path
                      'C:\...\pumping_python\doe\john'
                      because it does not exist

  ``john`` is not a child of ``doe``, yet

* I use mkdir_ to make ``john``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir john

  the terminal_ goes back to the command line

* I use ls_ to see what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: python

    jane  john

* I use tree_ to show the folders_ inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 3

    .
    ├── jane
    └── john

    3 directories, 0 files

  - ``john`` is a child of ``doe``
  - ``.`` is the working directory_, which is ``doe`` in this case
  - the line in the tree that goes from ``.`` to ``john`` shows I can go from ``doe`` right to ``john``

* I `change directory`_ to ``john``

  .. code-block::
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john

  I am in ``john``

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  - ``doe`` is not a child of ``john``
  - I cannot go from ``john`` to ``doe`` this way

* I `change directory`_ back to the parent of ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  - I am back in ``doe``
  - ``..`` is for the parent of the directory_ I am in
  - I can `change directory`_ from the directory_ I am in to its parent with ``cd ..``
  - ``..`` is ``doe`` when I am in ``john``

* I `change directory`_ to a hidden folder_ in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory:
        .a_hidden_folder_in_doe

  ``.a_hidden_folder_in_doe`` is not in ``doe``, yet

* I use mkdir_ to make ``.a_hidden_folder_in_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_doe

  the terminal_ goes back to the command line

* I use ls_ to see what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        jane  john

      - ``.a_hidden_folder_in_doe`` is hidden
      - I can hide a file_ or folder_ if I put ``.`` before its name
      - I use ls_ with the ``-a`` option to see everything that is in ``doe`` even things that are hidden

        .. code-block:: python
          :emphasize-lines: 1

          ls -a

        the terminal_ shows

        .. code-block:: python

          .  ..  .a_hidden_folder_in_doe  jane  john

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Mode            LastWriteTime         Length  Name
        ----            -------------         ------  ----
        d-----    MM/DD/YYYY HH:MM A/PM               .a_hidden_folder_in_doe
        d-----    MM/DD/YYYY HH:MM A/PM               jane
        d-----    MM/DD/YYYY HH:MM A/PM               john

      ``.a_hidden_folder_in_doe`` is not hidden on Windows_ without `Windows Subsystem for Linux`_

* I use tree_ to show the folders_ inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell

        .
        ├── jane
        └── john

        3 directories, 0 files

      - ``.a_hidden_folder_in_doe`` is hidden
      - I can hide a file_ or folder_ if I put ``.`` before its name

      * I can also use tree_ with the ``-a`` option to show things that are hidden

        .. code-block:: python
          :emphasize-lines: 1

          tree -a

        the terminal_ shows

        .. code-block:: shell
          :emphasize-lines: 2

          .
          ├── .a_hidden_folder_in_doe
          ├── jane
          └── john

          4 directories, 0 files

        - ``.`` is the working directory_, which is ``doe`` in this case
        - the line in the tree that goes from ``.`` to ``.a_hidden_folder_in_doe`` shows I can go from ``doe`` right to ``.a_hidden_folder_in_doe``

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 2

        C:.
        ├── .a_hidden_folder_in_doe
        ├── jane
        └── john

      ``.a_hidden_folder_in_doe`` is not hidden on Windows_ without `Windows Subsystem for Linux`_

* I `change directory`_ to ``.a_hidden_folder_in_doe``

  .. code-block::
    :emphasize-lines: 1

    cd .a_hidden_folder_in_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/.a_hidden_folder_in_doe

  I am in ``.a_hidden_folder_in_doe``

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        cd: no such file or directory: doe

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: Powershell

        Set-Location: Cannot find path
                      `C:\...\pumping_python\doe\john\lil\doe`
                      because it does not exist

  - ``doe`` is not a child of ``.a_hidden_folder_in_doe``
  - I cannot go from ``.a_hidden_folder_in_doe`` to ``doe`` this way

* I `change directory`_ back to the parent of ``.a_hidden_folder_in_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  - I am back in ``doe``
  - ``..`` is for the parent of the directory_ I am in
  - I can `change directory`_ from the directory_ I am in to its parent with ``cd ..``
  - ``..`` is ``doe`` when I am in ``.a_hidden_folder_in_doe``

----

* I change directory_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane

* I use ls_ to show what is in ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      the terminal_ goes back to the command line

      - I use ls_ with the short form of the ``--all`` option

        .. code-block:: python
          :emphasize-lines: 1

          ls -a

        the terminal_ shows

        .. code-block:: python

          .  ..

    .. tab-item:: no WSL
      :sync: no_wsl

      the terminal_ goes back to the command line

  ``jane`` has no children

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: python

    .

    0 directories, 0 files

  ``jane`` has no children

* I `change directory`_ to ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd mary

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: mary

  ``jane`` has no children, yet

* I use mkdir_ to make ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir mary

  the terminal_ goes back to the command line

* I try to `change directory`_ to ``mary`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd mary

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/mary

  - I am in the ``mary`` folder_
  - ``mary`` is a child of ``jane``
  - ``jane`` is a child of ``doe``

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: jane

  - ``jane`` is not a child of ``mary``
  - I cannot go from ``mary`` to ``jane`` this way

* I go up a level to the parent of ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/jane

  I am back in ``jane``

* I `change directory`_ to a hidden folder_ in ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_jane

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory:
        .a_hidden_folder_in_jane

  there is no folder_ named ``.a_hidden_folder_in_jane`` in ``jane``

* I make ``.a_hidden_folder_in_jane``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_jane

  the terminal_ goes back to the command line

* I try to `change directory`_ to ``.a_hidden_folder_in_jane`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_jane

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/.a_hidden_folder_in_jane

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: jane

  - ``jane`` is not a child of ``.a_hidden_folder_in_jane``
  - I cannot go from ``.a_hidden_folder_in_jane`` to ``jane`` this way

* I go up a level to the parent of ``.a_hidden_folder_in_jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/jane

  I am back in ``jane``

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 2

        .
        └── mary

        2 directories, 0 files

      * I use tree_ with the ``-a`` option

        .. code-block:: python
          :emphasize-lines: 1

          tree -a

        the terminal_ shows

        .. code-block:: shell
          :emphasize-lines: 2

          .
          ├── .a_hidden_folder_in_jane
          └── mary

          3 directories, 0 files


        - ``.`` is ``jane`` when I am in ``jane``
        - the line in the tree that goes from ``.`` to ``mary`` shows I can go from ``jane`` right to ``mary``
        - the line in the tree that goes from ``.`` to ``.a_hidden_folder_in_jane`` shows I can go from ``jane`` right to ``.a_hidden_folder_in_jane``

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 2

        C:.
        ├── .a_hidden_folder_in_jane
        └── mary

* I go up a level to the parent of ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

----

* I change directory_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john

  ``john`` is a child of ``doe``

* I use ls_ to show what is in ``john``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      the terminal_ goes back to the command line

      - I use ls_ with the short form of the ``--all`` option

        .. code-block:: python
          :emphasize-lines: 1

          ls -a

        the terminal_ shows

        .. code-block:: python

          .  ..

    .. tab-item:: no WSL
      :sync: no_wsl

      the terminal_ goes back to the command line

  ``john`` has no children

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: python

    .

    0 directories, 0 files

  ``john`` has no children, yet

* I `change directory`_ to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: lil

  ``john`` has no children

* I use mkdir_ to make ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir lil

  the terminal_ goes back to the command line

* I try to `change directory`_ to ``lil`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  - I am in the ``lil`` folder_
  - ``lil`` is a child of ``john``
  - ``john`` is a child of ``doe``

* I `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: john

  - ``john`` is not a child of ``lil``
  - I cannot go from ``lil`` to ``john`` this way

* I go up a level to the parent of ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/john

  I am back in ``john``

* I `change directory`_ to a hidden folder_ in ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_john

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory:
        .a_hidden_folder_in_john

  there is no folder_ named ``.a_hidden_folder_in_john`` in ``john``

* I use mkdir_ to make ``.a_hidden_folder_in_john``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_john

  the terminal_ goes back to the command line

* I try to `change directory`_ to ``.a_hidden_folder_in_john`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_john

  the terminal_ shows

  .. code-block:: python

    .../doe/john/.a_hidden_folder_in_john

* I `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: john

  - ``john`` is not a child of ``.a_hidden_folder_in_john``
  - I cannot go from ``.a_hidden_folder_in_john`` to ``john`` this way

* I go up a level to the parent of ``.a_hidden_folder_in_john``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/john

  I am back in ``john``

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 2

        .
        └── lil

        2 directories, 0 files

      * I use tree_ with the ``-a`` option

        .. code-block:: python
          :emphasize-lines: 1

          tree -a

        the terminal_ shows

        .. code-block:: shell
          :emphasize-lines: 2

          .
          ├── .a_hidden_folder_in_john
          └── lil

          3 directories, 0 files


        - ``.`` is ``john`` when I am in ``john``
        - the line in the tree that goes from ``.`` to ``lil`` shows I can go from ``john`` right to ``lil``
        - the line in the tree that goes from ``.`` to ``.a_hidden_folder_in_john`` shows I can go from ``john`` right to ``.a_hidden_folder_in_john``

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 2

        C:.
        ├── .a_hidden_folder_in_john
        └── lil

* I go up a level to the parent of ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I use tree_ to show the files_ and folders_ related to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: shell
        :emphasize-lines: 3, 5

        .
        ├── jane
        │   └── mary
        └── john
            └── lil

        5 directories, 0 files

      * I use the ``-a`` option with tree_

        .. code-block:: python
          :emphasize-lines: 1

          tree -a

        the terminal_ shows

        .. code-block:: shell
          :emphasize-lines: 2, 4, 7

          .
          ├── .a_hidden_folder_in_doe
          ├── jane
          │   ├── .a_hidden_folder_in_jane
          │   └── mary
          └── john
              ├── .a_hidden_folder_in_john
              └── lil

          8 directories, 0 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: shell
        :emphasize-lines: 2, 4, 7

        C:.
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        └── john
            ├── .a_hidden_folder_in_john
            └── lil

  the lines show that

  - I can go from ``doe`` right to ``.a_hidden_folder_in_doe``
  - I can go from ``doe`` right to ``jane``
  - I can go from ``doe`` right to ``john``
  - I can go from ``jane`` right to ``.a_hidden_folder_in_jane``
  - I can go from ``jane`` right to ``mary``
  - I can go from ``john`` right to ``.a_hidden_folder_in_john``
  - I can go from ``john`` right to ``lil``

:ref:`I know how to look at directory relationships<how to look at directory relationships>`

----

********************************************************************************************
how to make an empty file
********************************************************************************************

I can use the touch_ or `New-Item`_ program to make empty files_ in a folder_

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I use touch_ to make an empty file_ in ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        touch a_file_in_doe

      the terminal_ goes back to the command line

      .. ADMONITION:: on Windows_ without `Windows Subsystem for Linux`_

        use `New-Item`_ in place of ``touch``

        .. code-block:: PowerShell
          :emphasize-lines: 1

          New-Item a_file_in_doe

    * I use touch_ to make an empty hidden file_ in ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        touch .a_hidden_file_in_doe

    * I use ls_ to see what is in the folder_

      .. code-block:: python
        :emphasize-lines: 1

        ls

      the terminal_ shows

      .. code-block:: python

        a_file_in_doe  jane  john

    * I use ls_ with the ``-a`` option

      .. code-block:: python
        :emphasize-lines: 1

        ls -a

      the terminal_ shows

      .. code-block:: python

        .
        ..
        a_file_in_doe
        .a_hidden_file_in_doe
        .a_hidden_folder_in_doe
        jane
        john

  .. tab-item:: no WSL
    :sync: no_wsl

    * I use `New-Item`_ to make an empty file_ in ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item a_file_in_doe

      the terminal_ goes back to the command line

    * I use `New-Item`_ to make an empty hidden file_ in ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item .a_hidden_file_in_doe

    * I use ls_ to show what is in ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        ls

      the terminal_ shows

      .. code-block:: python

        Mode            LastWriteTime   Length  Name
        ----            -------------   ------  ----
        d-----    MM/DD/YYYY HH:MM A/PM         .a_hidden_folder_in_doe
        d-----    MM/DD/YYYY HH:MM A/PM         jane
        d-----    MM/DD/YYYY HH:MM A/PM         john
        -a----    MM/DD/YYYY HH:MM A/PM      0  .a_hidden_file_in_doe
        -a----    MM/DD/YYYY HH:MM A/PM      0  a_file_in_doe

      the terminal_ does not show ``.`` and ``..`` and always shows hidden folders_ and files_ on Windows_ without `Windows Subsystem for Linux`_

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          touch aka_jane_doe

        the terminal_ goes back to the command line

      * I use touch_ to make an empty hidden file_ in ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          touch .a_hidden_file_in_jane

        the terminal_ goes back to the command line

      * I use ls_ to show what is in ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          ls -a

        the terminal_ shows

        .. code-block:: python

          .
          ..
          .a_hidden_file_in_jane
          .a_hidden_folder_in_jane
          aka_jane_doe
          mary

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item aka_jane_doe

        the terminal_ goes back to the command line

      * I use `New-Item`_ to make an empty hidden file_ in ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item .a_hidden_file_in_jane

        the terminal_ goes back to the command line

      * I use ls_ to show what is in ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          ls

        the terminal_ shows

        .. code-block:: python

          Mode            LastWriteTime   Length  Name
          ----            -------------   ------  ----
          d-----    MM/DD/YYYY HH:MM A/PM         .a_hidden_folder_in_jane
          d-----    MM/DD/YYYY HH:MM A/PM         mary
          -a----    MM/DD/YYYY HH:MM A/PM      0  .a_hidden_file_in_jane
          -a----    MM/DD/YYYY HH:MM A/PM      0  aka_jane_doe

        the terminal_ does not show ``.`` and ``..`` and always shows hidden folders_ and files_ on Windows_ without `Windows Subsystem for Linux`_

* I `change directory`_ to the parent of ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

----

* I `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``john``

        .. code-block:: python
          :emphasize-lines: 1

          touch aka_john_doe

        the terminal_ goes back to the command line

      * I use touch_ to make an empty hidden file_ in ``john``

        .. code-block:: python
          :emphasize-lines: 1

          touch .a_hidden_file_in_john

        the terminal_ goes back to the command line

      * I use ls_ to show what is in ``john``

        .. code-block:: python
          :emphasize-lines: 1

          ls -a

        the terminal_ shows

        .. code-block:: python

          .
          ..
          .a_hidden_file_in_john
          .a_hidden_folder_in_john
          aka_john_doe
          lil

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``john``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item aka_john_doe

        the terminal_ goes back to the command line

      * I use `New-Item`_ to make an empty hidden file_ in ``john``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item .a_hidden_file_in_john

        the terminal_ goes back to the command line

      * I use ls_ to show what is in ``john``

        .. code-block:: python
          :emphasize-lines: 1

          ls

        the terminal_ shows

        .. code-block:: python

          Mode            LastWriteTime   Length  Name
          ----            -------------   ------  ----
          d-----    MM/DD/YYYY HH:MM A/PM         .a_hidden_folder_in_john
          d-----    MM/DD/YYYY HH:MM A/PM         lil
          -a----    MM/DD/YYYY HH:MM A/PM      0  .a_hidden_file_in_john
          -a----    MM/DD/YYYY HH:MM A/PM      0  aka_john_doe

        the terminal_ does not show ``.`` and ``..`` and always shows hidden folders_ and files_ on Windows_ without `Windows Subsystem for Linux`_

* I `change directory`_ to the parent of ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I use tree_ to show the files_ and folders_ related to ``doe``

  .. TIP:: Your terminal_ may use colors to show the difference between directories_ and files_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 2, 4, 7

        .
        ├── a_file_in_doe
        ├── jane
        │   ├── aka_jane_doe
        │   └── mary
        └── john
            ├── aka_john_doe
            └── lil

        5 directories, 3 files

      I use tree_ with the ``-a`` option

      .. code-block:: python
        :emphasize-lines: 1

        tree -a

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 3, 6, 11

        .
        ├── a_file_in_doe
        ├── .a_hidden_file_in_doe
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   ├── .a_hidden_file_in_jane
        │   ├── .a_hidden_folder_in_jane
        │   ├── aka_jane_doe
        │   └── mary
        └── john
            ├── .a_hidden_file_in_john
            ├── .a_hidden_folder_in_john
            ├── aka_john_doe
            └── lil

        8 directories, 6 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 2, 4, 7

        C:.
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        └── john
            ├── .a_hidden_folder_in_john
            └── lil

      I use tree_ with the ``/F`` option to show files_ and folders_

      .. code-block:: python
        :emphasize-lines: 1

        tree /F

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 2, 7, 13

        C:.
        │   .a_hidden_file_in_doe
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil

:ref:`I know how to make an empty file<how to make an empty file>`

----

********************************************************************************************
how to use directory relationships
********************************************************************************************

* I try to `change directory`_  from ``doe`` to ``mary`` in one step

  .. code-block:: python
    :emphasize-lines: 1

    cd mary

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        cd: no such file or directory: mary

      * I use tree_ with the ``-d`` option to show only the directories_

        .. code-block:: python
          :emphasize-lines: 1

          tree -d

        the terminal_ shows

        .. code-block:: shell
          :emphasize-text: jane mary

          .
          ├── jane
          │   └── mary
          └── john
              └── lil

          5 directories

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Set-Location: Cannot find path
                      'C:\...\pumping_python\doe\mary'
                      because it does not exist

      * I use tree_ to show only the directories_

        .. code-block:: python
          :emphasize-lines: 1

          tree

        the terminal_ shows

        .. code-block:: shell

          C:.
          ├── .a_hidden_folder_in_doe
          ├── jane
          │   ├── .a_hidden_folder_in_jane
          │   └── mary
          └── john
              ├── .a_hidden_folder_in_john
              └── lil

  - there is no line from ``doe`` to ``mary`` because ``mary`` is not a child of ``doe``
  - there is a line from ``jane`` to ``mary`` because ``mary`` is a child of ``jane``
  - there is a line from ``doe`` to ``jane`` because ``jane`` is a child of ``doe``

* I can go from ``doe`` to ``jane`` to ``mary`` in one step with

  .. code-block:: python
    :emphasize-lines: 1

    cd jane/mary

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/mary

  I cannot go to ``mary`` without its parent. How do I get back to ``doe``?

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  - ``doe`` is not a child of ``mary``
  - I cannot go from ``mary`` to ``doe`` this way

* I can go from ``mary`` back to ``doe`` in one step with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

  - ``..`` is for the parent of a directory_
  - ``../..`` is for the parent of the parent, that is a grandparent. I can use as many as I need for each parent, for example ``../../../..`` is the great great grand parent
  - ``..`` from ``mary`` is ``jane``
  - ``..`` from ``jane`` is ``doe``

----

* I try to `change directory`_  from ``doe`` to ``lil`` in one step

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        cd: no such file or directory: lil

      * I use tree_ with the ``-d`` option to show only the directories_

        .. code-block:: python
          :emphasize-lines: 1

          tree -d

        the terminal_ shows

        .. code-block:: shell
          :emphasize-text: john lil

          .
          ├── jane
          │   └── mary
          └── john
              └── lil

          5 directories

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        Set-Location: Cannot find path
                      'C:\...\pumping_python\doe\lil'
                      because it does not exist

      * I use tree_ to show only the directories_

        .. code-block:: python
          :emphasize-lines: 1

          tree

        the terminal_ shows

        .. code-block:: shell

          C:.
          ├── .a_hidden_folder_in_doe
          ├── jane
          │   ├── .a_hidden_folder_in_jane
          │   └── mary
          └── john
              ├── .a_hidden_folder_in_john
              └── lil

  - there is no line from ``doe`` to ``lil`` because ``lil`` is not a child of ``doe``
  - there is a line from ``john`` to ``lil`` because ``lil`` is a child of ``john``
  - there is a line from ``doe`` to ``john`` because ``john`` is a child of ``doe``

* I can go from ``doe`` to ``john`` to ``lil`` in one step with

  .. code-block:: python
    :emphasize-lines: 1

    cd john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I cannot go to ``lil`` without its parent. How do I get back to ``doe``?

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  - ``doe`` is not a child of ``lil``
  - I cannot go from ``lil`` to ``doe`` this way

* I can go from ``lil`` back to ``doe`` in one step with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  🎶 that will bring us back to .../``doe`` a deer, a female deer...🎶

  - ``..`` is for the parent of a directory_
  - ``../..`` is for the parent of the parent
  - ``..`` from ``lil`` is ``john``
  - ``..`` from ``john`` is ``doe``

.. NOTE::

  * I can go right to folders_ that are where I am
  * I can go right from parent to child
  * I can use the path/address of a folder_ to go to it

:ref:`I know how to use directory relationships<how to use directory relationships>`

----

********************************************************************************************
how to use touch with directory relationships
********************************************************************************************

* I use tree_ to show the files_ and folders_ related to ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell

        .
        ├── a_file_in_doe
        ├── jane
        │   ├── aka_jane_doe
        │   └── mary
        └── john
            ├── aka_john_doe
            └── lil

        5 directories, 3 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        tree /F

      the terminal_ shows

      .. code-block:: shell

        C:.
        │   .a_hidden_file_in_doe
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil

* I `change directory`_ to ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane/mary

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/mary

  I am in ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          touch aka_mary_jane_doe

        the terminal_ goes back to the command line

      * I use touch_ to make an empty hidden file_ in ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          touch .a_hidden_file_in_mary

        the terminal_ goes back to the command line

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item aka_mary_jane_doe

        the terminal_ goes back to the command line

      * I use `New-Item`_ to make an empty hidden file_ in ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item .a_hidden_file_in_mary

        the terminal_ goes back to the command line

* I use mkdir_ to make a hidden directory_ in ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_mary

  the terminal_ goes back to the command line

* I use ls_ to show what is in ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a

      the terminal_ shows

      .. code-block:: python

        .
        ..
        .a_hidden_file_in_mary
        .a_hidden_folder_in_mary
        aka_mary_jane_doe

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: PowerShell
        :emphasize-lines: 1

        ls

      .. TIP:: I can also use ``dir``

      the terminal_ shows

      .. code-block:: python

        Mode            LastWriteTime   Length  Name
        ----            -------------   ------  ----
        d-----    MM/DD/YYYY HH:MM A/PM         .a_hidden_folder_in_mary
        -a----    MM/DD/YYYY HH:MM A/PM      0  .a_hidden_file_in_mary
        -a----    MM/DD/YYYY HH:MM A/PM      0  aka_mary_jane_doe

* I use cd_ to go back to the grandparent of ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    ...pumping_python/doe

  I am back in ``doe``

----

* I `change directory`_ to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I am in ``lil``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          touch aka_lil_john_doe

      * I use touch_ to make an empty hidden file_ in ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          touch .a_hidden_file_in_lil

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item aka_lil_john_doe

      * I use `New-Item`_ to make an empty hidden file_ in ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item .a_hidden_file_in_lil

* I use mkdir_ to make a hidden directory_ in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_lil

* I use ls_ to show what is in ``lil``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a

      the terminal_ shows

      .. code-block:: python

        .
        ..
        .a_hidden_file_in_lil
        .a_hidden_folder_in_lil
        aka_lil_john_doe

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: PowerShell
        :emphasize-lines: 1

        ls

      .. TIP:: I can also use ``dir``

      the terminal_ shows

      .. code-block:: python

        Mode            LastWriteTime   Length  Name
        ----            -------------   ------  ----
        d-----    MM/DD/YYYY HH:MM A/PM         .a_hidden_folder_in_lil
        -a----    MM/DD/YYYY HH:MM A/PM      0  .a_hidden_file_in_lil
        -a----    MM/DD/YYYY HH:MM A/PM      0  aka_lil_john_doe

* I use cd_ to go back to the grandparent of ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    ...pumping_python/doe

  I am back in ``doe``

* I use tree_ to see what I have so far

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 6, 10

        .
        ├── a_file_in_doe
        ├── jane
        │   ├── aka_jane_doe
        │   └── mary
        │       └── aka_mary_jane_doe
        └── john
            ├── aka_john_doe
            └── lil
                └── aka_lil_john_doe

        5 directories, 5 files

      I use tree_ with the ``-a`` option

      .. code-block:: python
        :emphasize-lines: 1

        tree -a

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 10-11, 18-19

        .
        ├── a_file_in_doe
        ├── .a_hidden_file_in_doe
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   ├── .a_hidden_file_in_jane
        │   ├── .a_hidden_folder_in_jane
        │   ├── aka_jane_doe
        │   └── mary
        │       ├── .a_hidden_file_in_mary
        │       ├── .a_hidden_folder_in_mary
        │       └── aka_mary_jane_doe
        └── john
            ├── .a_hidden_file_in_john
            ├── .a_hidden_folder_in_john
            ├── aka_john_doe
            └── lil
                ├── .a_hidden_file_in_lil
                ├── .a_hidden_folder_in_lil
                └── aka_lil_john_doe

        10 directories, 10 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 12-13, 15, 22-23, 25

        C:.
        │   .a_hidden_file_in_doe
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       │   .a_hidden_file_in_mary
        │       │   aka_mary_jane_doe
        │       │
        │       └── .a_hidden_folder_in_mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil
                │   .a_hidden_file_in_lil
                │   aka_lil_john_doe
                │
                └── .a_hidden_folder_in_lil

----

.. tab-set::
  :sync-group: os

  .. tab-item:: WSL/Linux/Mac
    :sync: unix

    * I use touch_ to make an empty file_ in ``jane`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        touch jane/child_of_doe

      the terminal_ goes back to the command line

    * I use touch_ to make an empty file_ in ``mary`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        touch jane/mary/grandchild_of_doe

      the terminal_ goes back to the command line

    * I use touch_ to make an empty file_ in ``john`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        touch john/child_of_doe

      the terminal_ goes back to the command line

    * I use touch_ to make an empty file_ in ``lil`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        touch john/lil/grandchild_of_doe

      the terminal_ goes back to the command line

  .. tab-item:: no WSL
    :sync: no_wsl

    * I use `New-Item`_ to make an empty file_ in ``jane`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item jane/child_of_doe

      the terminal_ goes back to the command line

    * I use `New-Item`_ to make an empty file_ in ``mary`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item jane/mary/grandchild_of_doe

      the terminal_ goes back to the command line

    * I use `New-Item`_ to make an empty file_ in ``john`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item john/child_of_doe

      the terminal_ goes back to the command line

    * I use `New-Item`_ to make an empty file_ in ``lil`` from inside ``doe``

      .. code-block:: python
        :emphasize-lines: 1

        New-Item john/lil/grandchild_of_doe

      the terminal_ goes back to the command line

* I use tree_ to show the files_ and folders_ related to ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 5, 8, 11, 14

        .
        ├── a_file_in_doe
        ├── jane
        │   ├── aka_jane_doe
        │   ├── child_of_doe
        │   └── mary
        │       ├── aka_mary_jane_doe
        │       └── grandchild_of_doe
        └── john
            ├── aka_john_doe
            ├── child_of_doe
            └── lil
                ├── aka_lil_john_doe
                └── grandchild_of_doe

        5 directories, 9 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 9, 15, 21, 27

        C:.
        │   .a_hidden_file_in_doe
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │   child_of_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       │   .a_hidden_file_in_mary
        │       │   aka_mary_jane_doe
        │       │   grandchild_of_doe
        │       │
        │       └── .a_hidden_folder_in_mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │   child_of_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil
                │   .a_hidden_file_in_lil
                │   aka_lil_john_doe
                │   grandchild_of_doe
                │
                └── .a_hidden_folder_in_lil

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``mary`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          touch mary/child_of_jane

      * I use touch_ to make an empty file_ in ``doe`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../aka_parent_of_jane

      * I use touch_ to make an empty file_ in ``john`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../john/aka_sibling_of_jane

        - ``..`` is the parent of ``jane`` which is ``doe``
        - ``john`` is a child of ``doe``

      * I use touch_ to make an empty file_ in ``lil`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1-2

          touch ../john/lil/child_of_sibling_of_john

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``mary`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item mary/child_of_jane

      * I use `New-Item`_ to make an empty file_ in ``doe`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../aka_parent_of_jane

      * I use `New-Item`_ to make an empty file_ in ``john`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../john/aka_sibling_of_jane

        - ``..`` is the parent of ``jane`` which is ``doe``
        - ``john`` is a child of ``doe``

      * I use `New-Item`_ to make an empty file_ in ``lil`` from inside ``jane``

        .. code-block:: python
          :emphasize-lines: 1-2

          New-Item ../john/lil/child_of_sibling_of_john

  - ``..`` is the parent of ``jane`` which is ``doe``
  - ``john`` is a child of ``doe``
  - ``lil`` is a child of ``john``

  I made a mistake - ``child_of_sibling_of_john`` should be ``child_of_sibling_of_jane``

----

********************************************************************************************
how to rename a file or directory
********************************************************************************************

I can use the `mv program`_ to move a file_ and rename it at the same time.

* I `change directory`_ to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../john/lil

* I use mv_ to change ``child_of_sibling_of_john`` to ``child_of_sibling_of_jane``

  .. code-block:: python
    :emphasize-lines: 1-2

    mv child_of_sibling_of_john \
    child_of_sibling_of_jane

  the terminal_ goes back to the command line

  .. TIP::

    I can also rename the file_ with one line from inside ``jane`` without cd_ (it is a long line)

    .. code-block:: python

      mv ../john/lil/\
      child_of_sibling_of_john \
      ../john/lil/\
      child_of_sibling_of_jane

  ``\`` is a symbol that tells the computer I want to break up the line after I hit the :kbd:`enter/return` key on the keyboard

mv_ means move, it takes two arguments

.. code-block:: python

  mv source target

* ``source`` is the path/address I want to move the original file_ or folder_ from
* ``target`` is the path/address I want to move the original file_ or folder_ to
* this allows me to rename a file_ or folder_ in one step, the other way would be to

  - copy the original file_ or folder_ from the source
  - paste the copied file_ or folder_ at the target
  - delete the original file_ or folder_

  that is two steps too many, I leave that to the dancers, give me one step.

:ref:`I know how to rename a file<how to rename a file or directory>`

----

* I use cd_ to go back to the grandparent of ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

* I use tree_ to show the files_ and folders_ related to ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 3, 9, 13, 17

        .
        ├── a_file_in_doe
        ├── aka_parent_of_jane
        ├── jane
        │   ├── aka_jane_doe
        │   ├── child_of_doe
        │   └── mary
        │       ├── aka_mary_jane_doe
        │       ├── child_of_jane
        │       └── grandchild_of_doe
        └── john
            ├── aka_john_doe
            ├── aka_sibling_of_jane
            ├── child_of_doe
            └── lil
                ├── aka_lil_john_doe
                ├── child_of_sibling_of_jane
                └── grandchild_of_doe

        5 directories, 13 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 3, 16, 23, 30

        C:.
        │   .a_hidden_file_in_doe
        │   aka_parent_of_jane
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │   child_of_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       │   .a_hidden_file_in_mary
        │       │   aka_mary_jane_doe
        │       │   child_of_jane
        │       │   grandchild_of_doe
        │       │
        │       └── .a_hidden_folder_in_mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │   aka_sibling_of_jane
            │   child_of_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil
                │   .a_hidden_file_in_lil
                │   aka_lil_john_doe
                │   child_of_sibling_of_jane
                │   grandchild_of_doe
                │
                └── .a_hidden_folder_in_lil

----

* I `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``lil`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1

          touch lil/child_of_john

      * I use touch_ to make an empty file_ in ``doe`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../aka_parent_of_john

      * I use touch_ to make an empty file_ in ``jane`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../jane/aka_sibling_of_john

        - ``..`` is the parent of ``john`` which is ``doe``
        - ``jane`` is a child of ``doe``

      * I use touch_ to make an empty file_ in ``mary`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1-2

          touch ../jane/mary/child_of_sibling_of_jane

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``lil`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item lil/child_of_john

      * I use `New-Item`_ to make an empty file_ in ``doe`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../aka_parent_of_john

      * I use `New-Item`_ to make an empty file_ in ``jane`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../jane/aka_sibling_of_john

        - ``..`` is the parent of ``john`` which is ``doe``
        - ``jane`` is a child of ``doe``

      * I use `New-Item`_ to make an empty file_ in ``mary`` from inside ``john``

        .. code-block:: python
          :emphasize-lines: 1-2

          New-Item ../jane/mary/child_of_sibling_of_jane

  - ``..`` is the parent of ``john`` which is ``doe``
  - ``jane`` is a child of ``doe``
  - ``mary`` is a child of ``jane``

  I made a mistake again - ``child_of_sibling_of_jane`` should be ``child_of_sibling_of_john``

* I `change directory`_ to ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../jane/mary

* I use mv_ to change ``child_of_sibling_of_jane`` to ``child_of_sibling_of_john``

  .. code-block:: python
    :emphasize-lines: 1-2

    mv child_of_sibling_of_jane \
    child_of_sibling_of_john

  the terminal_ goes back to the command line

  .. TIP::

    I can also rename the file_ with one line from inside ``john`` without cd_ (it is a long line)

    .. code-block:: python

      mv ../jane/mary/\
      child_of_sibling_of_jane \
      ../jane/mary/\
      child_of_sibling_of_john

  ``\`` is the symbol that tells the computer I want to break up the line after I hit the :kbd:`enter/return` key on the keyboard

* I use cd_ to go back to the grandparent of ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

* I use tree_ to show the files_ and folders_ related to ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 4, 7, 12, 20

        .
        ├── a_file_in_doe
        ├── aka_parent_of_jane
        ├── aka_parent_of_john
        ├── jane
        │   ├── aka_jane_doe
        │   ├── aka_sibling_of_john
        │   ├── child_of_doe
        │   └── mary
        │       ├── aka_mary_jane_doe
        │       ├── child_of_jane
        │       ├── child_of_sibling_of_john
        │       └── grandchild_of_doe
        └── john
            ├── aka_john_doe
            ├── aka_sibling_of_jane
            ├── child_of_doe
            └── lil
                ├── aka_lil_john_doe
                ├── child_of_john
                ├── child_of_sibling_of_jane
                └── grandchild_of_doe

        5 directories, 17 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 4, 11, 19, 33

        C:.
        │   .a_hidden_file_in_doe
        │   aka_parent_of_jane
        │   aka_parent_of_john
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │   aka_sibling_of_john
        │   │   child_of_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       │   .a_hidden_file_in_mary
        │       │   aka_mary_jane_doe
        │       │   child_of_jane
        │       │   child_of_sibling_of_john
        │       │   grandchild_of_doe
        │       │
        │       └── .a_hidden_folder_in_mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │   aka_sibling_of_jane
            │   child_of_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil
                │   .a_hidden_file_in_lil
                │   aka_lil_john_doe
                │   child_of_john
                │   child_of_sibling_of_jane
                │   grandchild_of_doe
                │
                └── .a_hidden_folder_in_lil

* I `change directory`_ to ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane/mary

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``jane`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../aka_parent_of_mary

      * I use touch_ to make an empty file_ in ``doe`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../../aka_grandparent_of_mary

      * I use touch_ to make an empty file_ in ``john`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../../john/aka_aunt_of_mary

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``jane`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../aka_parent_of_mary

      * I use `New-Item`_ to make an empty file_ in ``doe`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../../aka_grandparent_of_mary

      * I use `New-Item`_ to make an empty file_ in ``john`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../../john/aka_aunt_of_mary

  I made a mistake - ``aka_aunt_of_mary`` should be ``aka_uncle_of_mary``

* I `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john

* I use mv_ to change ``aka_aunt_of_mary`` to ``aka_uncle_of_mary``

  .. code-block:: python
    :emphasize-lines: 1-2

    mv aka_aunt_of_mary aka_uncle_of_mary

* I `change directory`_ back to ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../jane/mary

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``lil`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1-2

          touch ../../john/lil/cousin_of_mary

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``lil`` from inside ``mary``

        .. code-block:: python
          :emphasize-lines: 1-2

          New-Item ../../john/lil/cousin_of_mary

* I use tree_ to show the files_ and folders_ related to ``doe`` from inside ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree ../..

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 1, 3, 8, 19, 25

        ../..
        ├── a_file_in_doe
        ├── aka_grandparent_of_mary
        ├── aka_parent_of_jane
        ├── aka_parent_of_john
        ├── jane
        │   ├── aka_jane_doe
        │   ├── aka_parent_of_mary
        │   ├── aka_sibling_of_john
        │   ├── child_of_doe
        │   └── mary
        │       ├── aka_mary_jane_doe
        │       ├── child_of_jane
        │       ├── child_of_sibling_of_john
        │       └── grandchild_of_doe
        └── john
            ├── aka_john_doe
            ├── aka_sibling_of_jane
            ├── aka_uncle_of_mary
            ├── child_of_doe
            └── lil
                ├── aka_lil_john_doe
                ├── child_of_john
                ├── child_of_sibling_of_jane
                ├── cousin_of_mary
                └── grandchild_of_doe

        5 directories, 21 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree ../.. /F

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 3, 12, 29, 38

        C:.\...\PUMPING_PYTHON\DOE
        │   .a_hidden_file_in_doe
        │   aka_grandparent_of_mary
        │   aka_parent_of_jane
        │   aka_parent_of_john
        │   a_file_in_doe
        │
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   │   .a_hidden_file_in_jane
        │   │   aka_jane_doe
        │   │   aka_parent_of_mary
        │   │   aka_sibling_of_john
        │   │   child_of_doe
        │   │
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       │   .a_hidden_file_in_mary
        │       │   aka_mary_jane_doe
        │       │   child_of_jane
        │       │   child_of_sibling_of_john
        │       │   grandchild_of_doe
        │       │
        │       └── .a_hidden_folder_in_mary
        └── john
            │   .a_hidden_file_in_john
            │   aka_john_doe
            │   aka_sibling_of_jane
            │   aka_uncle_of_mary
            │   child_of_doe
            │
            ├── .a_hidden_folder_in_john
            └── lil
                │   .a_hidden_file_in_lil
                │   aka_lil_john_doe
                │   child_of_john
                │   child_of_sibling_of_jane
                │   cousin_of_mary
                │   grandchild_of_doe
                │
                └── .a_hidden_folder_in_lil

* I `change directory`_ to ``lil`` from ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``john`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../aka_parent_of_lil

      * I use touch_ to make an empty file_ in ``doe`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../../aka_grandparent_of_lil

      * I use touch_ to make an empty file_ in ``jane`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          touch ../../jane/aka_uncle_of_lil

        I made another mistake - ``aka_uncle_of_lil`` should be ``aka_aunt_of_lil``

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``john`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../aka_parent_of_lil

      * I use `New-Item`_ to make an empty file_ in ``doe`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../../aka_grandparent_of_lil

      * I use `New-Item`_ to make an empty file_ in ``jane`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1

          New-Item ../../jane/aka_uncle_of_lil

        I made another mistake - ``aka_uncle_of_lil`` should be ``aka_aunt_of_lil``

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../jane

* I use mv_ to change ``aka_uncle_of_lil`` to ``aka_aunt_of_lil``

  .. code-block:: python
    :emphasize-lines: 1-2

    mv aka_uncle_of_lil aka_aunt_of_lil

* I `change directory`_ back to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../john/lil

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      * I use touch_ to make an empty file_ in ``mary`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1-2

          touch ../../jane/mary/cousin_of_lil

    .. tab-item:: no WSL
      :sync: no_wsl

      * I use `New-Item`_ to make an empty file_ in ``mary`` from inside ``lil``

        .. code-block:: python
          :emphasize-lines: 1-2

          New-Item ../../jane/mary/cousin_of_lil

* I use tree_ to show the files_ and folders_ related to ``doe`` from inside ``lil`` through the parent of ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../../doe

      the terminal_ shows

      .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTree
        :language: shell
        :emphasize-lines: 1, 3, 8, 17, 21

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../../doe /F

      the terminal_ shows

      .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTreeNoWsl
        :language: none
        :emphasize-lines: 3, 12, 24, 31

  - ``..`` is for the parent of ``lil`` which is ``john``
  - ``../..`` is for the parent of the parent of ``lil`` which is ``doe``
  - ``../../..`` is for the parent of the parent of the parent of ``lil`` which is ``pumping_python``
  - ``doe`` is a child of ``pumping_python``

I can add a file_ to any folder_ when I know its path or relation to where I am, if I have :ref:`permission to write to the folder<how to view the permissions of a file>`.

:ref:`I know how to use touch with directory relationships<how to use touch with directory relationships>`

----

********************************************************************************************
how to use ls with directory relationships
********************************************************************************************

I can see what is in any folder_ when I know its path or relation to where I am.

* I go to the parent of ``doe``

  .. code-block:: python

    cd ../../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am in ``pumping_python``

* I use ls_ to show what is in ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a doe

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ls doe

      .. TIP:: I can also use ``dir``

        .. code-block:: python
          :emphasize-lines: 1

          dir doe

  the terminal_ shows

  .. code-block:: python

    .
    ..
    a_file_in_doe
    .a_hidden_file_in_doe
    .a_hidden_folder_in_doe
    aka_grandparent_of_lil
    aka_grandparent_of_mary
    aka_parent_of_jane
    aka_parent_of_john
    jane
    john

* I use ls_ to show what is in ``jane``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a doe/jane

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ls doe/jane

  the terminal_ shows

  .. code-block:: python

    .
    ..
    .a_hidden_file_in_jane
    .a_hidden_folder_in_jane
    aka_aunt_of_lil
    aka_jane_doe
    aka_parent_of_mary
    aka_sibling_of_john
    child_of_doe
    mary

* I use ls_ to show what is in ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a doe/jane/mary

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ls doe/jane/mary

  the terminal_ shows

  .. code-block:: python

    .
    ..
    .a_hidden_file_in_mary
    .a_hidden_folder_in_mary
    aka_mary_jane_doe
    child_of_jane
    child_of_sibling_of_john
    cousin_of_lil
    grandchild_of_doe

* I `change directory`_ to ``mary``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe/jane/mary

* I use ls_ to show what is in ``john`` from inside ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a ../../john

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ls ../../john

  the terminal_ shows

  .. code-block:: python

    .
    ..
    .a_hidden_file_in_john
    .a_hidden_folder_in_john
    aka_john_doe
    aka_parent_of_lil
    aka_sibling_of_jane
    aka_uncle_of_mary
    child_of_doe
    lil

* I use ls_ to show what is in ``lil`` from inside ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a ../../john/lil

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ls ../../john/lil

  the terminal_ shows

  .. code-block:: python

    .
    ..
    .a_hidden_file_in_lil
    .a_hidden_folder_in_lil
    aka_lil_john_doe
    child_of_john
    child_of_sibling_of_jane
    cousin_of_mary
    grandchild_of_doe

:ref:`I know how to use ls with directory relations<how to use ls with directory relationships>`

----

********************************************************************************************
how to use tree with directory relationships
********************************************************************************************

* I use tree_ to show what is in ``lil``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../john/lil

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 1

        ../../john/lil
        ├── aka_lil_john_doe
        ├── child_of_john
        ├── child_of_sibling_of_jane
        ├── cousin_of_mary
        └── grandchild_of_doe

        1 directory, 5 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../john/lil /F

      the terminal_ shows

      .. code-block:: none
        :emphasize-lines: 1

        C:\...\PUMPING_PYTHON\DOE\JOHN\LIL
        │   .a_hidden_file_in_lil
        │   aka_lil_john_doe
        │   child_of_john
        │   child_of_sibling_of_jane
        │   cousin_of_mary
        │   grandchild_of_doe
        │
        └── .a_hidden_folder_in_lil

* I use tree_ to show what is in ``john``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../john

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 1

        ../../john
        ├── aka_john_doe
        ├── aka_parent_of_lil
        ├── aka_sibling_of_jane
        ├── aka_uncle_of_mary
        ├── child_of_doe
        └── lil
            ├── aka_lil_john_doe
            ├── child_of_john
            ├── child_of_sibling_of_jane
            ├── cousin_of_mary
            └── grandchild_of_doe

        2 directories, 10 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F ../../john

      the terminal_ shows

      .. code-block:: none
        :emphasize-lines: 1

        C:\...\PUMPING_PYTHON\DOE\JOHN
        │   .a_hidden_file_in_john
        │   aka_john_doe
        │   aka_parent_of_lil
        │   aka_sibling_of_jane
        │   aka_uncle_of_mary
        │   child_of_doe
        │
        ├── .a_hidden_folder_in_john
        └── lil
            │   .a_hidden_file_in_lil
            │   aka_lil_john_doe
            │   child_of_john
            │   child_of_sibling_of_jane
            │   cousin_of_mary
            │   grandchild_of_doe
            │
            └── .a_hidden_folder_in_lil

* I `change directories`_ from ``mary`` to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I am in ``lil``

* I look at what is in ``mary`` from inside ``lil``


  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        ls -a ../../jane/mary


    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        ls ../../jane/mary







  the terminal_ shows

  .. code-block:: python

    .
    ..
    .a_hidden_file_in_mary
    .a_hidden_folder_in_mary
    aka_mary_jane_doe
    child_of_jane
    child_of_sibling_of_john
    cousin_of_lil
    grandchild_of_doe

* I use tree_ to show what is in ``mary``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../jane/mary

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 1

        ../../jane/mary
        ├── aka_mary_jane_doe
        ├── child_of_jane
        ├── child_of_sibling_of_john
        ├── cousin_of_lil
        └── grandchild_of_doe

        1 directory, 5 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../jane/mary /F

      the terminal_ shows

      .. code-block:: none
        :emphasize-lines: 1

        C:\...\PUMPING_PYTHON\DOE\JANE\MARY
          │   .a_hidden_file_in_mary
          │   aka_mary_jane_doe
          │   child_of_jane
          │   child_of_sibling_of_john
          │   cousin_of_lil
          │   grandchild_of_doe
          │
          └── .a_hidden_folder_in_mary

* I use tree_ to show what is in ``jane``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree ../../jane

      the terminal_ shows

      .. code-block:: shell
        :emphasize-lines: 1

        ../../jane
        ├── aka_aunt_of_lil
        ├── aka_jane_doe
        ├── aka_parent_of_mary
        ├── aka_sibling_of_john
        ├── child_of_doe
        └── mary
            ├── aka_mary_jane_doe
            ├── child_of_jane
            ├── child_of_sibling_of_john
            ├── cousin_of_lil
            └── grandchild_of_doe

        2 directories, 10 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F ../../jane

      the terminal_ shows

      .. code-block:: none
        :emphasize-lines: 1

        C:\...\PUMPING_PYTHON\DOE\JANE
          │   .a_hidden_file_in_jane
          │   aka_aunt_of_lil
          │   aka_jane_doe
          │   aka_parent_of_mary
          │   aka_sibling_of_john
          │   child_of_doe
          │
          ├── .a_hidden_folder_in_jane
          └── mary
              │   .a_hidden_file_in_mary
              │   aka_mary_jane_doe
              │   child_of_jane
              │   child_of_sibling_of_john
              │   cousin_of_lil
              │   grandchild_of_doe
              │
              └── .a_hidden_folder_in_mary

* I go to the parent of ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

* I show all the ``doe`` family directories_

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree doe -ad

      the terminal_ shows

      .. code-block:: shell

        doe
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       └── .a_hidden_folder_in_mary
        └── john
            ├── .a_hidden_folder_in_john
            └── lil
                └── .a_hidden_folder_in_lil

        10 directories

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree doe

      the terminal_ shows

      .. code-block:: none

        C:\...\PUMPING_PYTHON\DOE
        ├── .a_hidden_folder_in_doe
        ├── jane
        │   ├── .a_hidden_folder_in_jane
        │   └── mary
        │       └── .a_hidden_folder_in_mary
        └── john
            ├── .a_hidden_folder_in_john
            └── lil
                └── .a_hidden_folder_in_lil

* I show the relationships of files_ and folders_ in ``doe``

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python
        :emphasize-lines: 1

        tree -a doe

      the terminal_ shows

      .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTree
        :language: shell

      * I show the path for each file_ and folder_ in ``doe`` with the ``-a`` and ``-f`` options

        .. code-block:: python

          tree -af doe

        the terminal_ shows

        .. code-block:: shell

          doe
          ├── doe/a_file_in_doe
          ├── doe/.a_hidden_file_in_doe
          ├── doe/.a_hidden_folder_in_doe
          ├── doe/aka_grandparent_of_lil
          ├── doe/aka_grandparent_of_mary
          ├── doe/aka_parent_of_jane
          ├── doe/aka_parent_of_john
          ├── doe/jane
          │   ├── doe/jane/.a_hidden_file_in_jane
          │   ├── doe/jane/.a_hidden_folder_in_jane
          │   ├── doe/jane/aka_aunt_of_lil
          │   ├── doe/jane/aka_jane_doe
          │   ├── doe/jane/aka_parent_of_mary
          │   ├── doe/jane/aka_sibling_of_john
          │   ├── doe/jane/child_of_doe
          │   └── doe/jane/mary
          │       ├── doe/jane/mary/.a_hidden_file_in_mary
          │       ├── doe/jane/mary/.a_hidden_folder_in_mary
          │       ├── doe/jane/mary/aka_mary_jane_Doe
          │       ├── doe/jane/mary/child_Of_jane
          │       ├── doe/jane/mary/child_of_sibling_of_john
          │       ├── doe/jane/mary/cousin_of_lil
          │       └── doe/jane/mary/grandchild_of_doe
          └── doe/john
              ├── doe/john/.a_hidden_file_in_john
              ├── doe/john/.a_hidden_folder_in_john
              ├── doe/john/aka_john_doe
              ├── doe/john/aka_parent_of_lil
              ├── doe/john/aka_sibling_of_jane
              ├── doe/john/aka_uncle_of_mary
              ├── doe/john/child_of_doe
              └── doe/john/lil
                  ├── doe/john/lil/.a_hidden_file_in_lil
                  ├── doe/john/lil/.a_hidden_folder_in_lil
                  ├── doe/john/lil/aka_lil_john_doe
                  ├── doe/john/lil/child_of_john
                  ├── doe/john/lil/child_of_sibling_of_jane
                  ├── doe/john/lil/cousin_of_mary
                  └── doe/john/lil/grandchild_of_doe

          10 directories, 30 files

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python
        :emphasize-lines: 1

        tree /F doe

      the terminal_ shows

      .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTreeNoWsl
        :language: none

I can do things with files_ and folders_ in one step as long as

- I know their paths/addresses
- I know their relation to where I am and
- I can :ref:`write to them<how to view the permissions of a file>`

It is easier to go where I want, if I know where I am.

:ref:`I know how to use directory relationships<how to use directory relationships>`

----

********************************************************************************************
how to remove a directory and all the things in it
********************************************************************************************

* I try to remove ``doe`` and all its children and their children

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        rm doe

      the terminal_ shows

      .. code-block:: python

        rm: cannot remove 'doe': Is a directory

      I cannot remove a directory_ this way

      * I remove ``doe`` and all its children and their children with the ``-r/--recursive`` option

        .. DANGER:: This is a destructive operation that takes a lot of work and time to undo on MacOS_ or Linux_/`Windows Subsystem for Linux`_. Do you want to do it?

        .. code-block:: python
          :emphasize-lines: 1

          rm --recursive doe

        the terminal_ goes back to the command line

        - ``rm`` means ``remove``
        - ``--recursive`` or ``-r`` means remove child directories_ and what is in them until there is nothing left. It goes through every directory_ in the tree and removes everything

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: PowerShell
        :emphasize-lines: 1

        Remove-Item doe

      the terminal_ shows

      .. code-block:: none

        Confirm
        The item at C:\...\pumping_python\doe has children
        and the Recurse parameter was not specified.
        If you continue, all children will be removed with the item.
        Are you sure you want to continue?
        [Y] Yes [A] Yes to All [N] No [L] No to All [S] Suspend
        [?] Help (default is "Y"):

      I could use :kbd:`A` on the keyboard to answer ``Yes to All`` or give one command to delete all the files_ and folders_ and ask me no questions.

      I use :kbd:`ctrl+c` to go back to the command line then give use the ``-Recurse`` and ``-Force`` options

      .. code-block:: PowerShell
        :emphasize-lines: 1

        Remove-Item -Path doe -Recurse -Force

      - `Remove-Item`_ is used to remove files_ and folders_
      - ``-Recurse`` means remove child directories_ and what is in them until there is nothing left. It goes through every directory_ in the tree and removes everything
      - ``-Force`` means do not ask me any questions, just remove the file_ or folder_

* I try to `change directory`_  back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  ``doe`` is gone!

*************************************************************************************
review
*************************************************************************************

I ran these commands to play with `folders (directories)`_

* mkdir_ to `make directories`_
* cd_ to `change directories`_
* ls_ to show what is in directories_
* tree_ to show the relationships between directories_
* touch_ to make empty files_
* mv_ to rename or move files_
* rm_ to remove directories_

:ref:`How many questions do you think you can answer after going through this chapter?<questions about directory relationships>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<learnDirectoryRelationships.sh>`

----

*****************************************************************************************
what is next?
*****************************************************************************************

You know

* :ref:`how to make a directory`
* :ref:`how to see what is in a directory`
* :ref:`how to look at directory relationships`
* :ref:`how to make an empty file`
* :ref:`how to use directory relationships`
* :ref:`how to use touch with directory relationships`
* :ref:`how to use ls with directory relationships`
* :ref:`how to use tree with directory relationships`
* :ref:`how to rename a file or directory`

.. admonition:: Homework

  use these commands - mkdir_, cd_, ls_, tree_ and touch_ - to make your family tree. Send it to me when you are done.

:ref:`Click Here to see me make a Python Test Driven Development Environment<how to make a test driven development environment>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->