:orphan:

.. include:: ../links.rst

.. _Excel Spreadsheet: https://grokipedia.com/page/Microsoft_Excel
.. _Word Document: https://grokipedia.com/page/Microsoft_Word
.. _make directories: mkdir_
.. _change directories: cd_


#################################################################################
BONUS: learn directory relationships
#################################################################################

This is an exercise in how your computer is setup as directories_ (folders_) and files_. Everything that happens on the computer ends up in a file_ in a directory_.

----

*************************************************************************************
preview
*************************************************************************************

I build the relationships below step by step to see how files_ and folders_ are related like a family tree, and at the end know how to move around them because I understand the relationships.

.. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTree
  :language: shell

These are all the commands used in this chapter

* mkdir_ to `make directories`_
* cd_ to `change directories`_
* ls_ to show what is in directories_
* tree_ to show the relationships between directories_
* touch_ to make empty files_
* mv_ to rename or move files_
* rm_ to remove directories_

----

*********************************************************************************
questions about directory relationships
*********************************************************************************

Here are questions you can answer after going through this chapter

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

A `folder (directory)`_ is a box for files_, it can also have other `folders (directories)`_. It helps keep things that should be together, in one place, the same way a folder in a file cabinet is used to keep files that should be together in one place.

I keep every project I work on in its own directory_. All the code in this book is kept in a folder_ named ``pumping_python``.

----

*********************************************************************************
what is a file?
*********************************************************************************

A file_ is a collection or container for text, like paper we write or print on and keep in a folder. The name of a file can end with an extension to show what type of file_ it is. For example

* ``.py`` for a :ref:`Python module<what is a module?>`
* ``.txt`` for a `plain text file`_
* ``.sh`` for a `bash file`_
* ``.ps1`` for a `PowerShell file`_
* ``.doc`` for a `Word Document`_
* ``.xls`` for an `Excel Spreadsheet`_

----

*********************************************************************************
requirements
*********************************************************************************

.. NOTE:: The code you type is highlighted and usually follows something like ``I type this in the terminal``

I type this in a terminal_ to make sure the `tree program`_ is installed

.. code-block:: python
  :emphasize-lines: 1

  tree

if it is not installed on the computer, the terminal_ shows

.. code-block:: python

    tree: command not found

if it is installed, the terminal_ shows

.. code-block:: python

  .

  0 directories, 0 files

if there is nothing in the directory_ or if there is something in the directory_, it shows the relationships.

The `tree program`_ shows how files_ and folders_ on a computer are related, this helps to know how to go from one folder_ to another, because it shows the way I can go. If I know where I am it is easier to go where I want.

----

********************************************************************************************
how to install tree
********************************************************************************************

* :ref:`how to install tree on Linux/Windows Subsystem for Linux`
* :ref:`how to install tree on Mac OS`
* :ref:`how to install tree on Windows without Windows Subsystem for Linux`

----

---------------------------------------------------------------------------------
how to install tree on Linux/Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. ATTENTION:: Do this only if you are using Linux_ or `Windows Subsystem for Linux`_. :ref:`MacOS users go here instead<how to install tree on Mac OS>`

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

continue with :ref:`how to see what directory I am in`

----

---------------------------------------------------------------------------------
how to install tree on Windows without Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. ATTENTION:: Do this only if you are using Windows_ and could not install `Windows Subsystem for Linux`_

tree_ comes with Windows_, no need to install anything.

You are going to use the commands below for the ones I have in the chapter

* `New-Item`_ for touch_
* ``tree /F`` for tree_
* dir_ for ``ls --all/-a``
* `Remove-Item`_ for rm_

when you call pwd_ or tree_ it shows ``\`` as the separator, not ``/``. For example

.. code-block:: PowerShell

  ...\pumping_python\doe

not

.. code-block:: python

  .../pumping_python/doe

Your tree will also look different because of different ways of drawing and sorting. Continue with :ref:`how to see what directory I am in`

----

---------------------------------------------------------------------------------
how to install tree on Mac OS
---------------------------------------------------------------------------------

----

.. ATTENTION:: Do this only if you are using a MacOS_ computer. Windows_ users do :ref:`how to install tree on Linux/Windows Subsystem for Linux` or :ref:`how to install tree on Windows without Windows Subsystem for Linux`

type this in the terminal_

.. code-block:: python

  brew install tree

continue with :ref:`how to see what directory I am in`

----

********************************************************************************************
how to see what directory I am in
********************************************************************************************

I start by checking where I am in the terminal_ because It is easier to go where I want, if I know where I am. I can do this with the pwd_ program

.. code-block:: python
  :emphasize-lines: 1

  pwd

the terminal_ shows

.. code-block:: python

  .../pumping_python

because I am in the ``pumping_python`` folder_

* pwd_ shows the path/address of the folder_ I am in
* pwd_ means ``print working directory``, it prints the directory_ I am in, to the terminal_
* each ``/`` shows a parent-child relationship
* the first ``/`` is for ``root`` which is the first folder_ on the computer
* the first ``/`` is the highest level

  .. CAUTION::

    do you want to see every file_ and folder_ on your computer as a tree? Type this in the terminal_

    .. code-block:: python

      tree /

    it runs for a while because there are many files_ and folders_.

    Use :kbd:`ctrl+c` on the keyboard if you want to stop it when it is running.

.. NOTE::

  - If you see ``pumping_python`` when you type ``pwd``, skip to the part where I create ``doe``
  - If you see a different name, continue to the next step - :ref:`how to change directory`

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

.. code-block:: python

  cd: no such file or directory: pumping_python

this means the folder_ I want to go to is not in the folder_ where I am

----

********************************************************************************************
how to make a directory
********************************************************************************************

* I use the `mkdir program`_ to make a `folder (directory)`_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir pumping_python

  - the terminal_ goes back to the command line
  - ``mkdir`` means ``make directory``

* I use cd_ to `change directory`_ again

  .. code-block:: python
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am in the ``pumping_python`` `folder (directory)`_

  .. code-block:: python

    .../pumping_python

  .. TIP:: to make sure I can see the ``pumping_python`` folder_ in my `Integrated Development Environment (IDE)`_ I have to open it. Here is how to do that with `Visual Studio Code`_

    .. code-block:: python
      :emphasize-lines: 1

      code .

    a new `Visual Studio Code`_ window opens in the ``pumping_python`` directory_

* I want to work in a directory_ named ``doe``, I try to `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  ``doe`` is not in the ``pumping_python`` directory_, yet

* I make ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

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

  .. code-block:: python

    .../pumping_python/doe

It is easier to go where I want, if I know where I am.

* :ref:`I know how to change directory<how to change directory>`
* :ref:`I know how to make a directory<how to make a directory>`

----

********************************************************************************************
how to see what is in a directory
********************************************************************************************

* I can use ls_ to show what is in a directory_ and see information about the files_ in it

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

  .. code-block:: python

    .../pumping_python/doe

  this directory_ is empty

* ls_ has a few options. I try ls_ again with one of them

  .. code-block:: python
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: python

    .  ..

  .. attention::

    on MacOS_ you may get this error

    .. code-block:: python

      ls: unrecognized option '--all'

    ``--all`` is the long form of the option, and there is usually a short form, use ``-a`` instead

    .. code-block:: python
      :emphasize-lines: 1

      ls -a

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

    the terminal_ does not show ``.`` and ``..`` on Windows_ without `Windows Subsystem for Linux`_


  - ``--all`` or ``-a`` tells ls_ to show all the things in the directory_ even those that start with ``.`` ( they are hidden by default)
  - I can hide a file_ or folder_ if I put ``.`` before its name, for example ``.hidden``

* I try to `change directory`_ to the ``.``

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

* I try cd_ with ``..`` to see what happens

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

* I go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

:ref:`I know how to see what is in a directory<how to see what is in a directory>`

----

********************************************************************************************
how to look at directory relationships
********************************************************************************************

* I can use the `tree program`_ to see the files_ and folders_ in a directory_ and how they are related. I type it in the terminal_ to see what is in the ``doe`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: python

    .

    0 directories, 0 files

  there is nothing in ``doe``, it is empty

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

* I try to `change directory`_ to ``jane_doe``, a child of ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: jane_doe

  ``jane_doe`` is not a child of ``doe``, yet

* I make ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir jane_doe

  the terminal_ goes back to the command line

* I use ls_ to see what is now in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: python

    jane_doe

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

* I use tree_ to show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1-2

    .
    └── jane_doe

    2 directories, 0 files

  - ``jane_doe`` is a child of ``doe``
  - ``.`` is the working directory_, which is ``doe`` in this case
  - the line in the tree that goes from ``.`` to ``jane_doe`` shows I can go from ``doe`` right to ``jane_doe``

* I `change directory`_ to ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane_doe

  I am in ``jane_doe``

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  ``doe`` is not a child of ``jane_doe``

* I `change directory`_ back to the parent of ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  - I am back in ``doe``
  - ``..`` is for the parent of the directory_ I am in
  - ``..`` is ``doe`` when I am in ``jane_doe``

* I try to `change directory`_ to ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd john_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: john_doe

  ``john_doe`` is not a child of ``doe``, yet

* I make ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir john_doe

  the terminal_ goes back to the command line

* I use ls_ to see what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: python

    jane_doe  john_doe

* I use tree_ to show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 3

    .
    ├── jane_doe
    └── john_doe

    3 directories, 0 files

  - ``john_doe`` is a child of ``doe``
  - ``.`` is the working directory_, which is ``doe`` in this case
  - the line in the tree that goes from ``.`` to ``john_doe`` shows I can go from ``doe`` right to ``john_doe``

* I `change directory`_ to ``john_doe``

  .. code-block::
    :emphasize-lines: 1

    cd john_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john_doe

  I am in ``john_doe``

* I `change directory`_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  ``doe`` is not a child of ``john_doe``

* I `change directory`_ back to the parent of ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

  - ``..`` is for the parent of the directory_ I am in
  - ``..`` is ``doe`` when I am in ``john_doe``

* I `change directory`_ to a hidden folder_ in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: .a_hidden_folder_in_doe

  ``.a_hidden_folder_in_doe`` is not in ``doe``, yet

* I make ``.a_hidden_folder_in_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_doe

  the terminal_ goes back to the command line

* I use ls_ to see what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: python

    jane_doe  john_doe

  - ``.a_hidden_folder_in_doe`` is hidden
  - I can hide a file_ or folder_ if I put ``.`` before its name

* I use ls_ with the ``-a`` option to see everything that is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .  ..  .a_hidden_folder_in_doe  jane_doe  john_doe

* I use tree_ to show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── jane_doe
    └── john_doe

    3 directories, 0 files

  - ``.a_hidden_folder_in_doe`` is hidden
  - I can hide a file_ or folder_ if I put ``.`` before its name

* I can also use tree_ with the ``-a`` option

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    ├── .a_hidden_folder_in_doe
    ├── jane_doe
    └── john_doe

    4 directories, 0 files

  - ``.`` is the working directory_, which is ``doe`` in this case
  - the line in the tree that goes from ``.`` to ``.a_hidden_folder_in_doe`` shows I can go from ``doe`` right to ``.a_hidden_folder_in_doe``

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

  .. code-block:: python

    cd: no such file or directory: doe

  ``doe`` is not a child of ``.a_hidden_folder_in_doe``

* I `change directory`_ back to the parent of ``.a_hidden_folder_in_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  - I am back in ``doe``
  - ``..`` is for the parent of the directory_ I am in
  - ``..`` is ``doe`` when I am in ``.a_hidden_folder_in_doe``

----

* I change directory_ to ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane_doe

* I show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

* I use ls_ with the short form of the ``--all`` option

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .  ..

  ``jane_doe`` has no children

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: python

    .

    0 directories, 0 files

  ``jane_doe`` has no children

* I `change directory`_ to a child of ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: mary_jane_doe

  ``jane_doe`` has no children, yet

* I make ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir mary_jane_doe

  the terminal_ goes back to the command line

* I try to go to ``mary_jane_doe`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/jane_doe/mary_jane_doe

  - I am in the ``mary_jane_doe`` folder_
  - ``mary_jane_doe`` is a child of ``jane_doe``
  - ``jane_doe`` is a child of ``doe``

* I go up a level to the parent of ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/jane_doe

  I am back in ``jane_doe``

* I `change directory`_ to a hidden folder_ in ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_jane_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: .a_hidden_folder_in_jane_doe

  there is no folder_ named ``.a_hidden_folder_in_jane_doe`` in ``jane_doe``

* I make a ``.a_hidden_folder_in_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_jane_doe

  the terminal_ goes back to the command line

* I try to go to ``.a_hidden_folder_in_jane_doe`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_jane_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/jane_doe/.a_hidden_folder_in_jane_doe

* I go up a level to the parent of ``.a_hidden_folder_in_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/jane_doe

  I am back in ``jane_doe``

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── mary_jane_doe

    2 directories, 0 files

* I use ``tree -a``

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    ├── .a_hidden_folder_in_jane_doe
    └── mary_jane_doe

    3 directories, 0 files

  - ``.`` is ``jane_doe`` when I am in ``jane_doe``
  - the line in the tree that goes from ``.`` to ``mary_jane_doe`` shows I can go from ``jane_doe`` right to ``mary_jane_doe``
  - the line in the tree that goes from ``.`` to ``.a_hidden_folder_in_jane_doe`` shows I can go from ``jane_doe`` right to ``.a_hidden_folder_in_jane_doe``

* I go up a level to the parent of ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

----

* I change directory_ to ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd john_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john_doe

  ``john_doe`` is a child of ``doe``

* I show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

* I use ls_ with the short form of the ``--all`` option

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .  ..

  ``john_doe`` has no children

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: python

    .

    0 directories, 0 files

  ``john_doe`` has no children, yet

* I `change directory`_ to a child of ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd lil_john_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: lil_john_doe

  ``john_doe`` has no children

* I make ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir lil_john_doe

  the terminal_ goes back to the command line

* I try to go to ``lil_john_doe`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd lil_john_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe/lil_john_doe

  - I am in the ``lil_john_doe`` folder_
  - ``lil_john_doe`` is a child of ``john_doe``
  - ``john_doe`` is a child of ``doe``

* I go up a level to the parent of ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe

  I am back in ``john_doe``

* I `change directory`_ to a hidden folder_ in ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_john_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: .a_hidden_folder_in_john_doe

  there is no folder_ named ``.a_hidden_folder_in_john_doe`` in ``john_doe``

* I make ``.a_hidden_folder_in_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_john_doe

  the terminal_ goes back to the command line

* I try to go to ``.a_hidden_folder_in_john_doe`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_john_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe/.a_hidden_folder_in_john_doe

* I go up a level to the parent of ``.a_hidden_folder_in_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe

  I am back in ``john_doe``

* I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── lil_john_doe

    2 directories, 0 files

* I use ``tree -a``

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    ├── .a_hidden_folder_in_john_doe
    └── lil_john_doe

    3 directories, 0 files

  - ``.`` is ``john_doe`` when I am in ``john_doe``
  - the line in the tree that goes from ``.`` to ``lil_john_doe`` shows I can go from ``john_doe`` right to ``lil_john_doe``
  - the line in the tree that goes from ``.`` to ``.a_hidden_folder_in_john_doe`` shows I can go from ``john_doe`` right to ``.a_hidden_folder_in_john_doe``

* I go up a level to the parent of ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3, 5

    .
    ├── jane_doe
    │   └── mary_jane_doe
    └── john_doe
        └── lil_john_doe

    5 directories, 0 files

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

* I use the ``-a`` option with tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 7

    .
    ├── .a_hidden_folder_in_doe
    ├── jane_doe
    │   ├── .a_hidden_folder_in_jane_doe
    │   └── mary_jane_doe
    └── john_doe
        ├── .a_hidden_folder_in_john_doe
        └── lil_john_doe

    8 directories, 0 files

  the lines show that

  - I can go from ``doe`` right to ``.a_hidden_folder_in_doe``
  - I can go from ``doe`` right to ``jane_doe``
  - I can go from ``doe`` right to ``john_doe``
  - I can go from ``jane_doe`` right to ``.a_hidden_folder_in_jane_doe``
  - I can go from ``jane_doe`` right to ``mary_jane_doe``
  - I can go from ``john_doe`` right to ``.a_hidden_folder_in_john_doe``
  - I can go from ``john_doe`` right to ``lil_john_doe``
  - ``mary_jane_doe`` is a grandchild of ``doe``
  - ``lil_john_doe`` is a grandchild of ``doe``

:ref:`I know how to look at directory relationships<how to look at directory relationships>`

----

********************************************************************************************
how to make an empty file
********************************************************************************************

I can make empty files_ in a folder_ with the `touch program`_

* I make an empty file_ in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch a_file_in_doe

  the terminal_ goes back to the command line

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item a_file_in_doe

* I make an empty hidden file_ in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_doe

* I use ls_ to see what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: python

    a_file_in_doe  jane_doe  john_doe

* I use ls_ with the ``-a`` option

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .              .a_hidden_file_in_doe    john_doe
    ..             .a_hidden_folder_in_doe
    a_file_in_doe  jane_doe

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

    the terminal_ does not show ``.`` and ``..`` and always shows hidden folder_ and files_

* I `change directory`_ to ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane_doe

* I make an empty file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch a_file_in_jane_doe

  the terminal_ goes back to the command line

* I make an empty hidden file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_jane_doe

  the terminal_ goes back to the command line

* I show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .                   .a_hidden_file_in_jane_doe
    ..                  .a_hidden_folder_in_jane_doe
    a_file_in_jane_doe  mary_jane_doe

* I `change directory`_ to the parent of ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

----

* I `change directory`_ to ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd john_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john_doe

* I make an empty file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch a_file_in_john_doe

  the terminal_ goes back to the command line

* I make an empty hidden file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_john_doe

  the terminal_ goes back to the command line

* I show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .                   .a_hidden_file_in_john_doe
    ..                  .a_hidden_folder_in_john_doe
    a_file_in_john_doe  lil_john_doe

* I `change directory`_ to the parent of ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I use tree_ to show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 7

    .
    ├── a_file_in_doe
    ├── jane_doe
    │   ├── a_file_in_jane_doe
    │   └── mary_jane_doe
    └── john_doe
        ├── a_file_in_john_doe
        └── lil_john_doe

    5 directories, 3 files

  .. TIP:: Your terminal_ may use colors to show the difference between directories_ and files_

* I use tree_ with the ``-a`` option

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3, 7, 12

    .
    ├── a_file_in_doe
    ├── .a_hidden_file_in_doe
    ├── .a_hidden_folder_in_doe
    ├── jane_doe
    │   ├── a_file_in_jane_doe
    │   ├── .a_hidden_file_in_jane_doe
    │   ├── .a_hidden_folder_in_jane_doe
    │   └── mary_jane_doe
    └── john_doe
        ├── a_file_in_john_doe
        ├── .a_hidden_file_in_john_doe
        ├── .a_hidden_folder_in_john_doe
        └── lil_john_doe

    8 directories, 6 files

:ref:`I know how to make an empty file<how to make an empty file>`

----

********************************************************************************************
how to use directory relationships
********************************************************************************************

* I try to go from ``doe`` to ``mary_jane_doe`` in 1 step

  .. code-block:: python
    :emphasize-lines: 1

    cd mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: mary_jane_doe

* I use tree_ with the ``-d`` option to show only the directories_

  .. code-block:: python
    :emphasize-lines: 1

    tree -d

  the terminal_ shows

  .. code-block:: shell
    :emphasize-text: jane_doe mary_jane_doe

    .
    ├── jane_doe
    │   └── mary_jane_doe
    └── john_doe
        └── lil_john_doe

    5 directories

  - there is no line from ``doe`` to ``mary_jane_doe`` because ``mary_jane_doe`` is not a child of ``doe``
  - there is a line from ``jane_doe`` to ``mary_jane_doe`` because ``mary_jane_doe`` is a child of ``jane_doe``
  - there is a line from ``doe`` to ``jane_doe`` because ``jane_doe`` is a child of ``doe``

* I can go from ``doe`` to ``jane_doe`` to ``mary_jane_doe`` in 1 step with

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe/mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/jane_doe/mary_jane_doe

  I cannot go to ``mary_jane_doe`` without its parent

* I can go from ``mary_jane_doe`` back to ``doe`` in 1 step with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

  - ``..`` is for the parent of a directory_
  - ``../..`` is for the parent of the parent, that is a grandparent. I can use as many as I need for each parent, for example ``../../../..`` is the great great grand parent
  - ``..`` from ``mary_jane_doe`` is ``jane_doe``
  - ``..`` from ``jane_doe`` is ``doe``

* I try to go from ``doe`` to ``lil_john_doe`` in 1 step

  .. code-block:: python
    :emphasize-lines: 1

    cd lil_john_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: lil_john_doe

* I use tree_ with the ``-d`` option to show only the directories_

  .. code-block:: python
    :emphasize-lines: 1

    tree -d

  the terminal_ shows

  .. code-block:: shell
    :emphasize-text: john_doe lil_john_doe

    .
    ├── jane_doe
    │   └── mary_jane_doe
    └── john_doe
        └── lil_john_doe

    5 directories

  - there is no line from ``doe`` to ``lil_john_doe`` because ``lil_john_doe`` is not a child of ``doe``
  - there is a line from ``john_doe`` to ``lil_john_doe`` because ``lil_john_doe`` is a child of ``john_doe``
  - there is a line from ``doe`` to ``john_doe`` because ``john_doe`` is a child of ``doe``

* I can go from ``doe`` to ``john_doe`` to ``lil_john_doe`` in 1 step with

  .. code-block:: python
    :emphasize-lines: 1

    cd john_doe/lil_john_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe/lil_john_doe

  I cannot go to ``lil_john_doe`` without its parent

* I can go from ``lil_john_doe`` back to ``doe`` in 1 step with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

  - ``..`` is for the parent of a directory_
  - ``../..`` is for the parent of the parent
  - ``..`` from ``lil_john_doe`` is ``john_doe``
  - ``..`` from ``john_doe`` is ``doe``

.. NOTE::

  * I can only go right to folders_ that are where I am (children)
  * I can use the path/address of a folder_ to go to it
  * It is easier to go where I want, if I know where I am

:ref:`I know how to use directory relationships<how to use directory relationships>`

----

********************************************************************************************
how to use touch with directory relationships
********************************************************************************************

* I show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── a_file_in_doe
    ├── jane_doe
    │   ├── a_file_in_jane_doe
    │   └── mary_jane_doe
    └── john_doe
        ├── a_file_in_john_doe
        └── lil_john_doe

    5 directories, 3 files

* I want to make a file_ in ``mary_jane_doe``. I `change directory`_ to ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe/mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/jane_doe/mary_jane_doe

  I am in ``mary_jane_doe``

* I make an empty file_ in ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch a_file_in_mary_jane_doe

  the terminal_ goes back to the command line

* I make an empty hidden file_ in ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_mary_jane_doe

  the terminal_ goes back to the command line

* I make a hidden folder_ in ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_mary_jane_doe

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .
    ..
    a_file_in_mary_jane_doe
    .a_hidden_file_in_mary_jane_doe
    .a_hidden_folder_in_mary_jane_doe

* I go back to the grandparent of ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    ...pumping_python/doe

  I am back in ``doe``

----

* I want to make a file_ in ``lil_john_doe``. I `change directory`_ to ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd john_doe/lil_john_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe/lil_john_doe

  I am in ``lil_john_doe``

* I make an empty file_ in ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch a_file_in_lil_john_doe

  the terminal_ goes back to the command line

* I make an empty hidden file_ in ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_lil_john_doe

  the terminal_ goes back to the command line

* I make a hidden folder_ in ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_lil_john_doe

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .                       .a_hidden_file_in_lil_john_doe
    ..                      .a_hidden_folder_in_lil_john_doe
    a_file_in_lil_john_doe

* I go back to the grandparent of ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    ...pumping_python/doe

  I am back in ``doe``

* I use tree_ to see what I have so far

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 6, 10

    .
    ├── a_file_in_doe
    ├── jane_doe
    │   ├── a_file_in_jane_doe
    │   └── mary_jane_doe
    │       └── a_file_in_mary_jane_doe
    └── john_doe
        ├── a_file_in_john_doe
        └── lil_john_doe
            └── a_file_in_lil_john_doe

    5 directories, 5 files

* I use tree_ with the ``-a`` option

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 11-12, 19-20

    .
    ├── a_file_in_doe
    ├── .a_hidden_file_in_doe
    ├── .a_hidden_folder_in_doe
    ├── jane_doe
    │   ├── a_file_in_jane_doe
    │   ├── .a_hidden_file_in_jane_doe
    │   ├── .a_hidden_folder_in_jane_doe
    │   └── mary_jane_doe
    │       ├── a_file_in_mary_jane_doe
    │       ├── .a_hidden_file_in_mary_jane_doe
    │       └── .a_hidden_folder_in_mary_jane_doe
    └── john_doe
        ├── a_file_in_john_doe
        ├── .a_hidden_file_in_john_doe
        ├── .a_hidden_folder_in_john_doe
        └── lil_john_doe
            ├── a_file_in_lil_john_doe
            ├── .a_hidden_file_in_lil_john_doe
            └── .a_hidden_folder_in_lil_john_doe

    10 directories, 10 files

----

* I make an empty file_ in ``jane_doe`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch jane_doe/a_child_of_doe

* I make an empty file_ in ``mary_jane_doe`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch jane_doe/mary_jane_doe/a_grandchild_of_doe

* I make an empty file_ in ``john_doe`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch john_doe/a_child_of_doe

* I make an empty file_ in ``lil_john_doe`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch john_doe/lil_john_doe/a_grandchild_of_doe

* I show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4, 8, 10, 13

    .
    ├── a_file_in_doe
    ├── jane_doe
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane_doe
    │   └── mary_jane_doe
    │       ├── a_file_in_mary_jane_doe
    │       └── a_grandchild_of_doe
    └── john_doe
        ├── a_child_of_doe
        ├── a_file_in_john_doe
        └── lil_john_doe
            ├── a_file_in_lil_john_doe
            └── a_grandchild_of_doe

    5 directories, 9 files

----

* I `change directory`_ to ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe

* I make an empty file_ in ``mary_jane_doe`` from inside ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch mary_jane_doe/a_child_of_jane_doe

* I make an empty file_ in ``doe`` from inside ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../aka_parent_of_jane_doe

* I make an empty file_ in ``john_doe`` from inside ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../john_doe/aka_sibling_of_jane_doe

  - ``..`` is the parent of ``jane_doe`` which is ``doe``
  - ``john_doe`` is a child of ``doe``

* I make an empty file_ in ``lil_john_doe`` from inside ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../john_doe/lil_john_doe/child_of_sibling_of_john_doe

  - ``..`` is the parent of ``jane_doe`` which is ``doe``
  - ``john_doe`` is a child of ``doe``
  - ``lil_john_doe`` is a child of ``john_doe``

  I made a mistake - ``child_of_sibling_of_john_doe`` should be ``child_of_sibling_of_jane_doe``

----

********************************************************************************************
how to rename a file or directory
********************************************************************************************

I can use the `mv program`_ to move a file_ and rename it at the same time.

* I `change directory`_ to ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../john_doe/lil_john_doe

* I change ``child_of_sibling_of_john_doe`` to ``child_of_sibling_of_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mv child_of_sibling_of_john_doe child_of_sibling_of_jane_doe

  .. TIP::

    I can also do it with one line without cd_ (it is a long line)

    .. code-block:: python

      mv ../john_doe/lil_john_doe/child_of_sibling_of_john_doe \
         ../john_doe/lil_john_doe/child_of_sibling_of_jane_doe

  the terminal_ goes back to the command line

mv_ means move, it takes two arguments

.. code-block:: python

  mv source target

* ``source`` is the path/address I want to move the original file_ or folder_ from
* ``target`` is the path/address I want to move the original file_ or folder_ to
* this allows me to rename a file_ or folder_ in one step, the other way would be to

  - copy the original file_ or folder_
  - paste the copied file_ or folder_ at the target
  - delete the original file_ or folder_

  that is two steps too many, give me one step.

:ref:`I know how to rename a file<how to rename a file or directory>`

----

* I go back to the grandparent of ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

* I show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3, 8, 14, 16

    .
    ├── a_file_in_doe
    ├── aka_parent_of_jane_doe
    ├── jane_doe
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane_doe
    │   └── mary_jane_doe
    │       ├── a_child_of_jane_doe
    │       ├── a_file_in_mary_jane_doe
    │       └── a_grandchild_of_doe
    └── john_doe
        ├── a_child_of_doe
        ├── a_file_in_john_doe
        ├── aka_sibling_of_jane_doe
        └── lil_john_doe
            ├── a_grandchild_of_doe
            ├── a_file_in_lil_john_doe
            └── child_of_sibling_of_jane_doe

    5 directories, 13 files

----

* I `change directory`_ to ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd john_doe

* I make an empty file_ in ``lil_john_doe`` from inside ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch lil_john_doe/a_child_of_john_doe

* I make an empty file_ in ``doe`` from inside ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../aka_parent_of_john_doe

* I make an empty file_ in ``jane_doe`` from inside ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../jane_doe/aka_sibling_of_john_doe

  - ``..`` is the parent of ``john_doe`` which is ``doe``
  - ``jane_doe`` is a child of ``doe``

* I make an empty file_ in ``mary_jane_doe`` from inside ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../jane_doe/mary_jane_doe/child_of_sibling_of_jane_doe

  - ``..`` is the parent of ``john_doe`` which is ``doe``
  - ``jane_doe`` is a child of ``doe``
  - ``mary_jane_doe`` is a child of ``jane_doe``

  I made a mistake again ``child_of_sibling_of_jane_doe`` should be ``child_of_sibling_of_john_doe``

* I `change directory`_ to ``mary_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../jane_doe/mary_jane_doe

* I change ``child_of_sibling_of_jane_doe`` to ``child_of_sibling_of_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mv child_of_sibling_of_jane_doe child_of_sibling_of_john_doe

  .. TIP::

    I can also do it with one line without cd_ (it is a long line)

    .. code-block:: python

      mv ../jane_doe/mary_jane_doe/child_of_sibling_of_jane_doe \
         ../jane_doe/mary_jane_doe/child_of_sibling_of_john_doe

  the terminal_ goes back to the command line

* I go back to the grandparent of ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

* I show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4, 8, 13, 19

    .
    ├── a_file_in_doe
    ├── aka_parent_of_jane_doe
    ├── aka_parent_of_john_doe
    ├── jane_doe
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane_doe
    │   ├── aka_sibling_of_john_doe
    │   └── mary_jane_doe
    │       ├── a_child_of_jane_doe
    │       ├── a_file_in_mary_jane_doe
    │       ├── a_grandchild_of_doe
    │       └── child_of_sibling_of_john_doe
    └── john_doe
        ├── a_child_of_doe
        ├── a_file_in_john_doe
        ├── aka_sibling_of_jane_doe
        └── lil_john_doe
            ├── a_child_of_john_doe
            ├── a_file_in_lil_john_doe
            ├── a_grandchild_of_doe
            └── child_of_sibling_of_jane_doe

    5 directories, 17 files

----

* I `change directory`_ to ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane_doe/mary_jane_doe

* I make an empty file_ in ``jane_doe`` from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../aka_parent_of_mary_jane_doe

* I make an empty file_ in ``doe`` from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../aka_grandparent_of_mary_jane_doe

* I make an empty file_ in ``john_doe`` from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../john_doe/aka_aunt_of_mary_jane_doe

  I made a mistake - ``john_doe`` is not the aunt of ``mary_jane_doe`` he is the uncle

* I `change directory`_ to ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john_doe

* I change ``aka_aunt_of_mary_jane_doe`` to ``aka_uncle_of_mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mv aka_aunt_of_mary_jane_doe aka_uncle_of_mary_jane_doe

* I `change directory`_ back to ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../jane_doe/mary_jane_doe

* I make an empty file_ in ``lil_john_doe`` from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../john_doe/lil_john_doe/cousin_of_mary_jane_doe

* I look at the ``doe`` family tree from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../..

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 3, 9, 20, 26

    ../..
    ├── a_file_in_doe
    ├── aka_grandparent_of_mary_jane_doe
    ├── aka_parent_of_jane_doe
    ├── aka_parent_of_john_doe
    ├── jane_doe
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane_doe
    │   ├── aka_parent_of_mary_jane_doe
    │   ├── aka_sibling_of_john_doe
    │   └── mary_jane_doe
    │       ├── a_child_of_jane_doe
    │       ├── a_file_in_mary_jane_doe
    │       ├── a_grandchild_of_doe
    │       └── child_of_sibling_of_john_doe
    └── john_doe
        ├── a_child_of_doe
        ├── a_file_in_john_doe
        ├── aka_sibling_of_jane_doe
        ├── aka_uncle_of_mary_jane_doe
        └── lil_john_doe
            ├── a_child_of_john_doe
            ├── a_file_in_lil_john_doe
            ├── a_grandchild_of_doe
            ├── child_of_sibling_of_jane_doe
            └── cousin_of_mary_jane_doe

    5 directories, 21 files

----

* I `change directory`_ to ``lil_john_doe`` from ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john_doe/lil_john_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe/lil_john_doe

* I make an empty file_ in ``john_doe`` from inside ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../aka_parent_of_lil_john_doe

* I make an empty file_ in ``doe`` from inside ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../aka_grandparent_of_lil_john_doe

* I make an empty file_ in ``jane_doe`` from inside ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../jane_doe/aka_uncle_of_lil_john_doe

  I made another mistake - ``jane_doe`` is not the uncle of ``mary_jane_doe`` she is the aunt

* I `change directory`_ to ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../jane_doe

* I change ``aka_uncle_of_lil_john_doe`` to ``aka_aunt_of_lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    mv aka_uncle_of_lil_john_doe aka_aunt_of_lil_john_doe

* I `change directory`_ back to ``lil_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../john_doe/lil_john_doe

* I make an empty file_ in ``mary_jane_doe`` from inside ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../jane_doe/mary_jane_doe/cousin_of_lil_john_doe

* I look at the ``doe`` family tree from inside ``lil_john_doe`` through the parent of ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../../doe

  - ``..`` is for the parent of ``lil_john_doe`` which is ``john_doe``
  - ``../..`` is for the parent of the parent of ``lil_john_doe`` which is ``doe``
  - ``../../..`` is for the parent of the parent of the parent of ``lil_john_doe`` which is ``pumping_python``
  - ``doe`` is a child of ``pumping_python``

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 3, 10, 18, 22

    ../../../doe
    ├── a_file_in_doe
    ├── aka_grandparent_of_lil_john_doe
    ├── aka_grandparent_of_mary_jane_doe
    ├── aka_parent_of_jane_doe
    ├── aka_parent_of_john_doe
    ├── jane_doe
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane_doe
    │   ├── aka_aunt_of_lil_john_doe
    │   ├── aka_parent_of_mary_jane_doe
    │   ├── aka_sibling_of_john_doe
    │   └── mary_jane_doe
    │       ├── a_child_of_jane_doe
    │       ├── a_file_in_mary_jane_doe
    │       ├── a_grandchild_of_doe
    │       ├── child_of_sibling_of_john_doe
    │       └── cousin_of_lil_john_doe
    └── john_doe
        ├── a_child_of_doe
        ├── a_file_in_john_doe
        ├── aka_parent_of_lil_john_doe
        ├── aka_sibling_of_jane_doe
        ├── aka_uncle_of_mary_jane_doe
        └── lil_john_doe
            ├── a_child_of_john_doe
            ├── a_file_in_lil_john_doe
            ├── a_grandchild_of_doe
            ├── child_of_sibling_of_jane_doe
            └── cousin_of_mary_jane_doe

    5 directories, 25 files

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

* I show what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe

  the terminal_ shows

  .. code-block:: python

    .
    ..
    a_file_in_doe
    .a_hidden_file_in_doe
    .a_hidden_folder_in_doe
    aka_grandparent_of_lil_john_doe
    aka_grandparent_of_mary_jane_doe
    aka_parent_of_jane_doe
    aka_parent_of_john_doe
    jane_doe
    john_doe

* I show what is in ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe/jane_doe

  the terminal_ shows

  .. code-block:: python

    .                           .a_hidden_folder_in_jane_doe
    ..                          aka_aunt_of_lil_john_doe
    a_child_of_doe              aka_parent_of_mary_jane_doe
    a_file_in_jane_doe          aka_sibling_of_john_doe
    .a_hidden_file_in_jane_doe  mary_jane_doe

* I show what is in ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe/jane_doe/mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    .
    ..
    a_child_of_jane_doe
    a_file_in_mary_jane_doe
    a_grandchild_of_doe
    .a_hidden_file_in_mary_jane_doe
    .a_hidden_folder_in_mary_jane_doe
    child_of_sibling_of_john_doe
    cousin_of_lil_john_doe

* I `change directory`_ to ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe/jane_doe/mary_jane_doe

* I show what is in ``john_doe`` from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a ../../john_doe

  the terminal_ shows

  .. code-block:: python

    .                           .a_hidden_folder_in_john_doe
    ..                          aka_parent_of_lil_john_doe
    a_child_of_doe              aka_sibling_of_jane_doe
    a_file_in_john_doe          aka_uncle_of_mary_jane_doe
    .a_hidden_file_in_john_doe  lil_john_doe

* I show what is in ``lil_john_doe`` from inside ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a ../../john_doe/lil_john_doe

  the terminal_ shows

  .. code-block:: python

    .                       .a_hidden_file_in_lil_john_doe
    ..                      .a_hidden_folder_in_lil_john_doe
    a_child_of_john_doe     child_of_sibling_of_jane_doe
    a_file_in_lil_john_doe  cousin_of_mary_jane_doe
    a_grandchild_of_doe

----

********************************************************************************************
how to use tree with directory relationships
********************************************************************************************

* I use tree_ to show what is in ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../john_doe/lil_john_doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1

    ../../john_doe/lil_john_doe
    ├── a_child_of_john_doe
    ├── a_file_in_lil_john_doe
    ├── a_grandchild_of_doe
    ├── child_of_sibling_of_jane_doe
    └── cousin_of_mary_jane_doe

    1 directory, 5 files

* I use tree_ to show what is in ``john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../john_doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1

    ../../john_doe
    ├── a_child_of_doe
    ├── a_file_in_john_doe
    ├── aka_parent_of_lil_john_doe
    ├── aka_sibling_of_jane_doe
    ├── aka_uncle_of_mary_jane_doe
    └── lil_john_doe
        ├── a_child_of_john_doe
        ├── a_file_in_lil_john_doe
        ├── a_grandchild_of_doe
        ├── child_of_sibling_of_jane_doe
        └── cousin_of_mary_jane_doe

    2 directories, 10 files

* I `change directories`_ from ``mary_jane_doe`` to ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john_doe/lil_john_doe

  the terminal_ shows

  .. code-block:: python

    .../doe/john_doe/lil_john_doe

  I am in ``lil_john_doe``

* I look at what is in ``mary_jane_doe`` from inside ``lil_john_doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a ../../jane_doe/mary_jane_doe

  the terminal_ shows

  .. code-block:: python

    .
    ..
    a_child_of_jane_doe
    a_file_in_mary_jane_doe
    a_grandchild_of_doe
    .a_hidden_file_in_mary_jane_doe
    .a_hidden_folder_in_mary_jane_doe
    child_of_sibling_of_john_doe
    cousin_of_lil_john_doe

* I use tree_ to show what is in ``mary_jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../jane_doe/mary_jane_doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1

    ../../jane_doe/mary_jane_doe
    ├── a_child_of_jane_doe
    ├── a_file_in_mary_jane_doe
    ├── a_grandchild_of_doe
    ├── child_of_sibling_of_john_doe
    └── cousin_of_lil_john_doe

    1 directory, 5 files

* I use tree_ to show what is in ``jane_doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../jane_doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1

    ../../jane_doe
    ├── a_child_of_doe
    ├── a_file_in_jane_doe
    ├── aka_aunt_of_lil_john_doe
    ├── aka_parent_of_mary_jane_doe
    ├── aka_sibling_of_john_doe
    └── mary_jane_doe
        ├── a_child_of_jane_doe
        ├── a_file_in_mary_jane_doe
        ├── a_grandchild_of_doe
        ├── child_of_sibling_of_john_doe
        └── cousin_of_lil_john_doe

    2 directories, 10 files

* I go to the parent of ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

* I show all the ``doe`` family directories_ with the ``-a`` and ``-d`` options

  .. code-block:: python
    :emphasize-lines: 1

    tree doe -ad

  the terminal_ shows

  .. code-block:: shell

    doe
    ├── .a_hidden_folder_in_doe
    ├── jane_doe
    │   ├── .a_hidden_folder_in_jane_doe
    │   └── mary_jane_doe
    │       └── .a_hidden_folder_in_mary_jane_doe
    └── john_doe
        ├── .a_hidden_folder_in_john_doe
        └── lil_john_doe
            └── .a_hidden_folder_in_lil_john_doe

    10 directories

* I show the relationships of files_ and folders_ in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    tree -a doe

  the terminal_ shows

  .. literalinclude:: ../code/bonus/learnDirectoryRelationshipsTree
    :language: shell

I can do things with files_ and folders_ in 1 step as long as

- I know their paths/addresses
- I know their relation to where I am and
- I can :ref:`write to them<how to view the permissions of a file>`

It is easier to go where I want, if I know where I am. :ref:`I know how to use directory relationships<how to use directory relationships>`

----

********************************************************************************************
how to remove a directory and all the things in it
********************************************************************************************

* I try to remove ``doe`` and all its children and their children

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

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``Remove-Item -Recurse -Force`` instead of ``rm --recursive``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      Remove-Item -Path doe -Recurse -Force


  - rm_/`Remove-Item`_ are used to remove files_ and folders_
  - ``rm`` means ``remove``
  - ``--recursive`` or ``-r`` or ``-Recurse`` means remove child directories_ and what is in them until there is nothing left. It goes through every child directory_ and removes everything including their children
  - ``-Force`` means do not ask me any questions, just remove the file_ or folder_

* I try to go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: doe

  the ``doe`` family is gone!

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