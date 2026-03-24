:orphan:

.. include:: ../links.rst

#################################################################################
BONUS: learn directory structure
#################################################################################

This is an exercise in how your computer is organized into directories_ (folders_) and files_

----

*************************************************************************************
preview
*************************************************************************************

I build the structure below step by step to see how files_ and folders_ are related like a family tree, and at the end know how to move around in the structure because I understand the relationships.

.. literalinclude:: ../code/bonus/learnDirectoryStructureTree
  :language: shell

These are all the commands used in this chapter

* mkdir_
* cd_
* ls_
* tree_
* touch_
* mv_
* rm_

----

*********************************************************************************
questions about directory structure
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a folder (directory)?<what is a folder?>`
* :ref:`what is a file?<what is a file?>`
* :ref:`how can I tell what directory I am in?<how to see what directory I am in>`
* :ref:`how can I change directories?<how to change directory>`
* :ref:`how can I make a directory?<how to make a directory>`
* :ref:`how can I see directory relationships?<how to look at directory structure>`
* :ref:`how can I see what is in a directory?<how to see what is in a directory>`
* :ref:`how can I make an empty file?<how to make an empty file>`
* :ref:`how can I rename a file or directory?<how to rename a file or directory>`
* :ref:`how can I use directory relationships?<how to use directory relationships>`
* :ref:`how can I remove a directory and everything inside it?<how to remove a directory and all its contents>`

----

*********************************************************************************
what is a folder?
*********************************************************************************

A `folder (directory)`_ is a box for files_. It helps organize things, just like a folder in a file cabinet is used to put files that belong together in one place.

I keep every project I work on in its own `folder (directory)`_. All the code in this book is done in a folder_ named ``pumping_python``.

----

*********************************************************************************
what is a file?
*********************************************************************************

A file_ is a collection or container for text, like paper we write or print on and keep in a folder. Their names can end with an extension (not always) to show the type of file_. For example

* ``.txt`` for a `plain text file`_
* ``.sh`` for a `bash file`_
* ``.ps1`` for a `PowerShell file`_
* ``.py`` for a :ref:`Python module<what is a module?>`

----

*********************************************************************************
requirements
*********************************************************************************

I open a terminal_ to make sure the `tree program`_ is installed by typing this

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

if there is nothing in the directory_. If there is something in the directory_ it shows a structure of the relationships.

The `tree program`_ shows how files_ and folders_ on a computer are related, this helps to know how to get from one folder_ to another, because it shows the paths I can take.

It is easier to get to where I want to go if I know where I am.

----

=================================================================================
how to install tree
=================================================================================

----

* :ref:`how to install tree on Linux/Windows Subsystem for Linux`
* :ref:`how to install tree on Mac OS`
* :ref:`how to install tree on Windows without Windows Subsystem for Linux`

----

---------------------------------------------------------------------------------
how to install tree on Linux/Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. code-block:: python
  :emphasize-lines: 1

  sudo apt update

you can do a full upgrade if you want, I always do

.. code-block:: python
  :emphasize-lines: 1

  sudo apt full-upgrade --yes

type this in the terminal_ to install tree_

.. code-block:: python
  :emphasize-lines: 1

  sudo apt install tree

continue in :ref:`how to work in directories`

----

---------------------------------------------------------------------------------
how to install tree on Windows without Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

You do not have to do anything because tree_ comes with Windows_ . These are things you would type in place of what I have in the chapter

* `New-Item`_ instead of touch_
* ``tree /F`` instead of tree_
* ``dir`` instead of ``ls --all/-a``

The path shown when you call pwd_ or tree_ shows ``\`` instead of ``/``, for example

.. code-block:: PowerShell

  ...\pumping_python

instead of

.. code-block:: python

  .../pumping_python

Your tree will also look different because of different ways of drawing and sorting. Continue with :ref:`how to work in directories`

----

---------------------------------------------------------------------------------
how to install tree on Mac OS
---------------------------------------------------------------------------------

----

type this in the terminal_

.. code-block:: python

  brew install tree

continue with :ref:`how to work in directories`

----

********************************************************************************************
how to work in directories
********************************************************************************************

----

=================================================================================
how to see what directory I am in
=================================================================================

----

I start by checking where I am in the terminal_ because it is easier to get to where I want to go if I know where I am. I can do this with the pwd_ program

.. code-block:: python
  :emphasize-lines: 1

  pwd

the terminal_ shows

.. code-block:: python

  .../pumping_python

because I am in the ``pumping_python`` folder_

* pwd_ shows the path/address of the current folder_ I am in at the moment
* pwd_ means ``print working directory``, it prints the directory I am in, to the terminal_
* each ``/`` shows a parent-child relationship
* the first ``/`` is for ``root`` which is the starting ancestor of all the folders_ on the computer, it is at the highest level

It is easier to get to where I want to go if I know where I am.

.. NOTE::

  - If you see the same name, skip to the part where I create ``doe``
  - If you see a different name, continue to the next step - :ref:`how to change directory`


----

=================================================================================
how to change directory
=================================================================================

----

I use the `cd program`_ to change directories_

.. code-block:: python
  :emphasize-lines: 1

  cd pumping_python

`cd`_ means ``change directory``

the terminal_ shows

.. code-block:: python

  cd: no such file or directory: pumping_python

this means the folder_ does not exist where I am

----

=================================================================================
how to make a directory
=================================================================================

----

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

  ``doe`` does not exist in the ``pumping_python`` directory_, yet

* I make ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

* I `change directory`_ to ``doe`` to do some work in it

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

It is easier to get to where I want to go if I know where I am. :ref:`I know how to make a directory<how to make a directory>`

----

=================================================================================
how to see what is in a directory
=================================================================================

----

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


  - ``--all/-a`` tells ls_ to show all the things in the directory even those that start with ``.`` ( they are hidden by default)
  - I can hide a file_ or directory_ by putting ``.`` before its name, for example ``.hidden``

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
  - ``.`` is the current working directory

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

=================================================================================
how to look at directory structure
=================================================================================

----

* I can use the `tree program`_ to see what files_ and folders_ are in a directory_. I type it in the terminal_ to see what is in the ``doe`` directory_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: python

    .

    0 directories, 0 files

  ``doe`` is empty, there is nothing in it

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

* I try to `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: jane

  ``jane`` is not a child of ``doe``, yet

* I make the folder_

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
    └── jane

    2 directories, 0 files

  - ``jane`` is a child of ``doe``
  - the line shows I can go directly from ``doe`` to ``jane``

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane

  I am in ``jane``

* I `change directory`_ back to ``doe`` (the parent of ``jane``)

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I try to `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: john

  ``john`` is not a child of ``doe``, yet

* I make a new folder_

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

* I use tree_ to show the ``doe`` family tree

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

  - ``jane`` and ``john`` are children of ``doe``
  - the lines shows I can go directly from ``doe`` to ``jane`` and ``john``

* I `change directory`_ to ``john``

  .. code-block::
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john

  I am in ``john``

* I `change directory`_ back to ``doe`` (the parent of ``john``)

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I try to `change directory`_ to ``.a_hidden_folder_in_doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_doe

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: .a_hidden_folder_in_doe

  ``.a_hidden_folder`` is not in ``doe``, yet

* I make a hidden folder_

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

    jane  john

  - ``.a_hidden_folder_in_doe`` is hidden
  - I can hide a file_ or directory_ if I put ``.`` before its name

* I use ls_ with the ``-a`` option to see everything that is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .  ..  .a_hidden_folder_in_doe  jane  john

* I use tree_ to show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── jane
    └── john

    3 directories, 0 files

* I use tree_ with the ``-a`` option

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

  - ``.a_hidden_folder_in_doe``, ``jane`` and ``john`` are inside ``doe``
  - the lines shows I can go directly from ``doe`` which is ``.`` to all 3 of them

* I `change directory`_ to ``.a_hidden_folder_in_doe``

  .. code-block::
    :emphasize-lines: 1

    cd .a_hidden_folder_in_doe

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/.a_hidden_folder_in_doe

  I am in ``.a_hidden_folder_in_doe``

* I `change directory`_ back to ``doe`` (the parent of ``.a_hidden_folder_in_doe``)

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

----

* I change directory_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane

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

* I `change directory`_ to a child of ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: baby

  ``jane`` has no children, yet

* I make ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir baby

  the terminal_ goes back to the command line

* I try to go to ``baby`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/baby

  - I am in the ``baby`` folder_
  - ``baby`` is a child of ``jane``
  - ``jane`` is a child of ``doe``

* I go up a level to the parent of ``baby`` - ``jane``

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

    cd: no such file or directory: .a_hidden_folder_in_jane

  there is no folder_ named ``.a_hidden_folder_in_jane`` in ``jane``

* I make a ``.a_hidden_folder_in_jane``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_jane

  the terminal_ goes back to the command line

* I try to go to ``.a_hidden_folder_in_jane`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_jane

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/.a_hidden_folder_in_jane

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

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── baby

    2 directories, 0 files

* I use ``tree -a``

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    ├── .a_hidden_folder_in_jane
    └── baby

    3 directories, 0 files

  the lines show I can `change directories`_ directly from ``jane`` to ``.a_hidden_folder_in_jane`` and ``baby``

* I go up a level to the parent of ``jane`` - ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I change directory_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john

  ``john`` is a child of ``doe``

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

* I `change directory`_ to a child of ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: lil

  ``john`` has no children

* I `make the directory`_

  .. code-block:: python
    :emphasize-lines: 1

    mkdir lil

  the terminal_ goes back to the command line

* I try to go to ``lil`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  - I am in the ``lil`` folder_
  - ``lil`` is a child of ``john``
  - ``john`` is a child of ``doe``

* I go up a level to the parent of ``lil`` - ``john``

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

    cd: no such file or directory: .a_hidden_folder_in_john

  there is no folder_ named ``.a_hidden_folder_in_john`` in ``john``

* I make ``.a_hidden_folder_in_john``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_john

  the terminal_ goes back to the command line

* I try to go to ``.a_hidden_folder_in_john`` again

  .. code-block:: python
    :emphasize-lines: 1

    cd .a_hidden_folder_in_john

  the terminal_ shows

  .. code-block:: python

    .../doe/john/.a_hidden_folder_in_john

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

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── lil

    2 directories, 0 files

* I use ``tree -a``

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

  the lines show I can `change directories`_ directly from ``john`` to ``.a_hidden_folder_in_john`` and ``lil``

* I go up a level to the parent of ``john`` - ``doe``

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
    ├── jane
    │   └── baby
    └── john
        └── lil

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
    ├── jane
    │   ├── .a_hidden_folder_in_jane
    │   └── baby
    └── john
        ├── .a_hidden_folder_in_john
        └── lil

    8 directories, 0 files

  the lines show that

  - ``baby`` and ``lil`` are grandchildren of ``doe``
  - I can go from ``doe`` to ``.a_hidden_folder_in_doe``
  - I can go from ``doe`` to ``jane``
  - I can go from ``doe`` to ``john``
  - I can go from ``jane`` to ``.a_hidden_folder_in_jane``
  - I can go from ``jane`` to ``baby``
  - I can go from ``john`` to ``.a_hidden_folder_in_john``
  - I can go from ``john`` to ``lil``

:ref:`I know how to look at directory structure<how to look at directory structure>`

----

=================================================================================
how to make an empty file
=================================================================================

----

I can make empty files_ in a folder_ with the `touch program`_

* I add an empty file_ to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch an_empty_file_in_doe

  the terminal_ goes back to the command line

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item an_empty_file_in_doe

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

    an_empty_file_in_doe  jane  john

* I use ls_ with the ``-a`` option

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .   .a_hidden_file_in_doe    an_empty_file_in_doe  john
    ..  .a_hidden_folder_in_doe  jane

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

    the terminal_ does not show ``.`` and ``..`` and always shows hidden folder_ and files_

* I `change directory`_ to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/jane

* I add an empty file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch an_empty_file_in_jane

  the terminal_ goes back to the command line

* I add an empty hidden file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_jane

  the terminal_ goes back to the command line

* I show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .   .a_hidden_file_in_jane    an_empty_file_in_jane
    ..  .a_hidden_folder_in_jane  baby

* I `change directory`_ to the parent of ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

* I `change directory`_ to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe/john

* I add an empty file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch an_empty_file_in_john

  the terminal_ goes back to the command line

* I add an empty hidden file_ with touch_

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_john

  the terminal_ goes back to the command line

* I show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .   .a_hidden_file_in_john    an_empty_file_in_john
    ..  .a_hidden_folder_in_john  lil

* I `change directory`_ to the parent of ``john``

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
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── an_empty_file_in_jane
    │   └── baby
    └── john
        ├── an_empty_file_in_john
        └── lil

    5 directories, 3 files

  .. TIP:: Your terminal_ may use colors to show the difference between directories_ and files_

* I use tree_ with the ``-a`` option

  .. code-block:: python
    :emphasize-lines: 1

    tree -a

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 6, 11

    .
    ├── .a_hidden_file_in_doe
    ├── .a_hidden_folder_in_doe
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── .a_hidden_file_in_jane
    │   ├── .a_hidden_folder_in_jane
    │   ├── an_empty_file_in_jane
    │   └── baby
    └── john
        ├── .a_hidden_file_in_john
        ├── .a_hidden_folder_in_john
        ├── an_empty_file_in_john
        └── lil

    8 directories, 6 files
* I want to make a file_ in ``baby``. I use cd_ to go to its parent first

  .. code-block:: python
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: python

    /pumping_python/doe/jane

  I am in ``jane``

* I `change directory`_ to ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/baby

  I am in ``baby``

* I make an empty file_ in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch an_empty_file_in_baby

  the terminal_ goes back to the command line

* I make an empty hidden file_ in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_baby

  the terminal_ goes back to the command line

* I make a hidden folder_ in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_baby

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .   .a_hidden_file_in_baby    an_empty_file_in_baby
    ..  .a_hidden_folder_in_baby

* I go back to the parent of ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/

  I am in ``jane``

* I go back to the parent of ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    ...pumping_python/doe

  I am back in ``doe``

* I want to make a file_ in ``lil``. I use cd_ to go to its parent first

  .. code-block:: python
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: python

    /pumping_python/doe/john

  I am in ``john``

* I `change directory`_ to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I am in ``lil``

* I make an empty file_ in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch an_empty_file_in_lil

  the terminal_ goes back to the command line

* I make an empty hidden file_ in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch .a_hidden_file_in_lil

  the terminal_ goes back to the command line

* I make a hidden folder_ in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    mkdir .a_hidden_folder_in_lil

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .   .a_hidden_file_in_lil    an_empty_file_in_lil
    ..  .a_hidden_folder_in_lil

* I go back to the parent of ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../doe/john/

  I am in ``john``

* I go back to the parent of ``john``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

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
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       └── an_empty_file_in_baby
    └── john
        ├── an_empty_file_in_john
        └── lil
            └── an_empty_file_in_lil

    5 directories, 5 files

* I use tree_ with the ``-a`` option

  .. code-block:: shell
    :emphasize-lines: 10-11, 18-19

    .
    ├── .a_hidden_file_in_doe
    ├── .a_hidden_folder_in_doe
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── .a_hidden_file_in_jane
    │   ├── .a_hidden_folder_in_jane
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── .a_hidden_file_in_baby
    │       ├── .a_hidden_folder_in_baby
    │       └── an_empty_file_in_baby
    └── john
        ├── .a_hidden_file_in_john
        ├── .a_hidden_folder_in_john
        ├── an_empty_file_in_john
        └── lil
            ├── .a_hidden_file_in_lil
            ├── .a_hidden_folder_in_lil
            └── an_empty_file_in_lil

    10 directories, 10 files

:ref:`I know how to add empty files to folders<how to make an empty file>`

----

=================================================================================
how to use directory relationships
=================================================================================

----

* I try to go from ``doe`` to ``baby`` in 1 step

  .. code-block:: python
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: baby

  - ``baby`` is not a child of ``doe``
  - there is no line from ``doe`` to ``baby``
  - there is a line from ``jane`` to ``baby``
  - there is a line from ``doe`` to ``jane``
  - I can go from ``doe`` to ``jane`` to ``baby``

* I try to go from ``doe`` to ``baby`` in 1 step with its parent

  .. code-block:: python
    :emphasize-lines: 1

    cd jane/baby

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/baby

  I cannot get to ``baby`` without its parent

* I can go from ``baby`` back to ``doe`` in 1 step with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``.

  Since ``..`` is for the parent of a directory_

  - ``../..`` is for the parent of the parent, that is a grandparent. I can use as many as I need for each parent, for example ``../../../..`` is the great great grand parent
  - ``..`` from ``baby`` is ``jane``
  - ``..`` from ``jane`` is ``doe``

* I try to go from ``doe`` to ``lil`` in 1 step

  .. code-block:: python
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: python

    cd: no such file or directory: lil

  - ``lil`` is not a child of ``doe``
  - there is no line from ``doe`` to ``lil``
  - there is a line from ``john`` to ``lil``
  - there is a line from ``doe`` to ``john``
  - I can go from ``doe`` to ``john`` to ``lil``

* I try to go from ``doe`` to ``lil`` in 1 step with its parent

  .. code-block:: python
    :emphasize-lines: 1

    cd john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I cannot get to ``lil`` without its parent

* I go back to ``doe`` in 1 step with ``..``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  - I can only go directly to folders_ that are where I am (children)
  - I can use the path to the folder_ I want to go to. It is easier to get to where I want to go if I know where I am.

----

=================================================================================
how to use directory relationships with touch
=================================================================================

----

* I add an empty file_ to ``jane`` from ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch jane/a_child_of_doe

* I add an empty file_ to ``baby`` from ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch jane/baby/a_grandchild_of_doe

* I add an empty file_ to ``john`` from ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch john/a_child_of_doe

* I add an empty file_ to ``lil`` from ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch john/lil/a_grandchild_of_doe

* I show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4, 7, 10, 13

    .
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── a_child_of_doe
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── a_grandchild_of_doe
    │       └── an_empty_file_in_baby
    └── john
        ├── a_child_of_doe
        ├── an_empty_file_in_john
        └── lil
            ├── a_grandchild_of_doe
            └── an_empty_file_in_lil

    5 directories, 9 files

----

* I `change directory`_ to ``jane``

  .. code-blokc


* I go from ``doe`` to ``baby`` in 1 step with its parent

  .. code-block:: python
    :emphasize-lines: 1

    cd jane/baby

  the terminal_ shows

  .. code-block:: python

    .../doe/jane/baby

  I am in ``baby``

* I make an empty file_ in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch aka_child_of_jane

  the terminal_ goes back to the command line

* I make another empty file_ in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch aka_child_of_janes_sibling

* I use ls_ to show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .                         aka_child_of_jane
    ..                        aka_child_of_janes_sibling
    .a_hidden_file_in_baby    an_empty_file_in_baby
    .a_hidden_folder_in_baby

* I go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

* I go from ``doe`` to ``lil`` in 1 step with its parent

  .. code-block:: python
    :emphasize-lines: 1

    cd john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I am in ``lil``

* I make an empty file_ in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch aka_child_of_john

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .                        aka_child_of_john
    ..                       aka_child_of_johns_sibling
    .a_hidden_file_in_lil    an_empty_file_in_lil
    .a_hidden_folder_in_lil

* I go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python/doe

  I am back in ``doe``

* I add 2 empty files_

  .. code-block:: python
    :emphasize-lines: 1

    touch aka_parent_of_jane

  the terminal_ goes back to the command line

  .. code-block:: python
    :emphasize-lines: 1

    touch aka_parent_of_john

  the terminal_ goes back to the command line

* I use tree_ to show the ``doe`` family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2-3, 8-9, 14-15

    .
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_janes_sibling
    │       └── an_empty_file_in_baby
    └── john
        ├── an_empty_file_in_john
        └── lil
            ├── aka_child_of_john
            ├── aka_child_of_johns_sibling
            └── an_empty_file_in_lil

    5 directories, 11 files

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

  wait a minute! How is ``lil`` a child of ``john`` and a child of ``john's sibling``, and how is ``baby`` a child of ``jane`` and a child of ``jane's`` sibling? I made mistakes.

----

=================================================================================
how to rename a file or directory
=================================================================================

----

* I go back to ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    cd jane/baby

* I use the `mv program`_ to change ``aka_child_of_janes_sibling`` to ``aka_child_of_johns_sibling``

  .. code-block:: python
    :emphasize-lines: 1

    mv aka_child_of_janes_sibling aka_child_of_johns_sibling

  mv_ means move, it takes two arguments

  - the original file_ or folder_
  - the file_ or folder_ I want the original to be moved to

* I go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

* I go to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd john/lil

* I use the `mv program`_ to change ``aka_child_of_johns_sibling`` to ``aka_child_of_janes_sibling``

  .. code-block:: python
    :emphasize-lines: 1

    mv aka_child_of_johns_sibling aka_child_of_janes_sibling

  the terminal_ goes back to the command line

* I go back to ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../..

* I show the family tree

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 9, 14

    .
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_johns_sibling
    │       └── an_empty_file_in_baby
    └── john
        ├── an_empty_file_in_john
        └── lil
            ├── aka_child_of_janes_sibling
            ├── aka_child_of_john
            └── an_empty_file_in_lil

    5 directories, 11 files

----

I can add a file_ to any folder_ when I know its path or relation to where I am, and I have permission to write to the folder_. It is easier to get to where I want to go if I know where I am

* I add an empty file_ to ``jane`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch jane/a_child_of_doe

* I add an empty file_ to ``john`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch john/a_child_of_doe

* I add an empty file_ to ``baby`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch jane/baby/a_grandchild_of_doe

* I add an empty file_ to ``lil`` from inside ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    touch john/lil/a_grandchild_of_doe

* I `change directory`_ to the parent of ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am in the ``pumping_python`` folder_

* I use tree_ to show the ``doe`` family tree (what is in ``doe``)

  .. code-block:: python
    :emphasize-lines: 1

    tree doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 6, 9, 14, 17

    doe
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── a_child_of_doe
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── a_grandchild_of_doe
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_johns_sibling
    │       └── an_empty_file_in_baby
    └── john
        ├── a_child_of_doe
        ├── an_empty_file_in_john
        └── lil
            ├── a_grandchild_of_doe
            ├── aka_child_of_janes_sibling
            ├── aka_child_of_john
            └── an_empty_file_in_lil

    5 directories, 15 files

* I type pwd_ to see where I am

  .. code-block:: python
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am in the ``pumping_python`` folder_

----

* I go to ``john``

  .. code-block:: python

    cd doe/john

* I add an empty file_ to ``lil`` from inside ``john``

  .. code-block:: python

    touch lil/a_child_of_john

* I add an empty file_ to ``doe`` from inside ``john``

  .. code-block:: python

    touch ../aka_parent_of_john

* I add an empty file_ to ``jane`` from inside ``john``

  .. code-block:: python

    touch ../jane/aka_sibling_of_john

* I add an empty file_ to ``baby`` from inside ``john``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../jane/aka_child_of_janes_sibling

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1-2

      New-Item jane/aka_sibling_of_john

* I use tree_ to show the ``doe`` family tree (what is in ``doe``)

  .. code-block:: python
    :emphasize-lines: 1

    tree ../doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 6, 9, 14, 17

    ../doe
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── a_child_of_doe
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── a_grandchild_of_doe
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_johns_sibling
    │       └── an_empty_file_in_baby
    └── john
        ├── a_child_of_doe
        ├── an_empty_file_in_john
        └── lil
            ├── a_grandchild_of_doe
            ├── aka_child_of_janes_sibling
            ├── aka_child_of_john
            └── an_empty_file_in_lil

    5 directories, 15 files

* I type pwd_ to see where I am

  .. code-block:: python
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am in the ``pumping_python`` folder_

----

* I go to ``jane``

  .. code-block:: python

    cd ../jane

* I add an empty file_ to ``baby`` from inside ``jane``

  .. code-block:: python

    touch baby/a_child_of_jane

* I add an empty file_ to ``doe`` from inside ``jane``

  .. code-block:: python

    touch ../aka_parent_of_jane

* I add an empty file_ to ``john`` from inside ``jane``

  .. code-block:: python

    touch ../jane/aka_sibling_of_john

* I add an empty file_ to ``baby`` from inside ``john``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../john/baby/aka_child_of_johns_sibling

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1-2

      touch ../john/baby/aka_child_of_johns_sibling

* I use tree_ to show the ``doe`` family tree (what is in ``doe``)

  .. code-block:: python
    :emphasize-lines: 1

    tree ../doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 6, 9, 14, 17

    doe
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── a_child_of_doe
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── a_grandchild_of_doe
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_johns_sibling
    │       └── an_empty_file_in_baby
    └── john
        ├── a_child_of_doe
        ├── an_empty_file_in_john
        └── lil
            ├── a_grandchild_of_doe
            ├── aka_child_of_janes_sibling
            ├── aka_child_of_john
            └── an_empty_file_in_lil

    5 directories, 15 files

* I type pwd_ to see where I am

  .. code-block:: python
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am in the ``pumping_python`` folder_

----

* I can see what is in any folder_ when I know its path or relation to where I am. It is easier to get to where I want to go if I know where I am

  .. code-block:: python
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: python

    .  ..  doe

* I show what is in ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe

  the terminal_ shows

  .. code-block:: python

    .                        aka_parent_of_john
    ..                       an_empty_file_in_doe
    .a_hidden_file_in_doe    jane
    .a_hidden_folder_in_doe  john
    aka_parent_of_jane

* I show what is in ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe/jane

  the terminal_ shows

  .. code-block:: python

    .                       .a_hidden_folder_in_jane
    ..                      aka_sibling_of_john
    a_child_of_doe          an_empty_file_in_jane
    .a_hidden_file_in_jane  baby

* I show what is in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe/jane/baby

  the terminal_ shows

  .. code-block:: python

    .                       .a_hidden_folder_in_baby
    ..                      aka_child_of_jane
    a_grandchild_of_doe     aka_child_of_janes_sibling
    .a_hidden_file_in_baby  an_empty_file_in_baby

* I show what is in ``john``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe/john

  the terminal_ shows

  .. code-block:: python

    .                       .a_hidden_folder_in_john
    ..                      aka_sibling_of_jane
    a_child_of_doe          an_empty_file_in_john
    .a_hidden_file_in_john  lil

* I show what is in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    ls -a doe/john/lil

  the terminal_ shows

  .. code-block:: python

    .                      .a_hidden_folder_in_lil
    ..                     aka_child_of_john
    a_grandchild_of_doe    aka_child_of_johns_sibling
    .a_hidden_file_in_lil  an_empty_file_in_lil

----

* I `change directory`_ from ``pumping_python`` to ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    cd doe/jane/baby

  - I am in ``baby``
  - ``baby`` is a child of ``jane``
  - ``jane`` is a child of ``doe``
  - ``doe`` is a child of ``pumping_python``

* I want to see what is in ``lil`` from inside ``baby`` in 1 step. ``../..`` is ``doe`` and I can go from ``doe`` to ``lil``. I use this relationship with ls_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a ../../john/lil

  - ``..`` from ``baby`` is ``jane``
  - ``..`` from ``jane`` is ``doe``
  - ``john`` is a child of ``doe``
  - ``lil`` is a child of ``john``

  the terminal_ shows

  .. code-block:: python

    .                      .a_hidden_folder_in_lil
    ..                     aka_child_of_john
    a_grandchild_of_doe    aka_child_of_johns_sibling
    .a_hidden_file_in_lil  an_empty_file_in_lil

* I add an empty file_ to ``lil`` from inside ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../john/lil/aka_cousin_of_baby

  the terminal_ goes back to the command line

* I use tree_ to show what is in ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../john/lil

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 5

    ../../john/lil
    ├── a_grandchild_of_doe
    ├── aka_child_of_john
    ├── aka_child_of_johns_sibling
    ├── aka_cousin_of_baby
    └── an_empty_file_in_lil

    1 directory, 5 files

* I add an empty file_ to ``jane`` from inside ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../aka_parent_of_baby

  the terminal_ goes back to the command line

  ``..`` from ``baby`` is ``jane``

* I add an empty file_ to ``john`` from inside ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../jane/aka_uncle_of_baby

  the terminal_ goes back to the command line

  - ``..`` from ``baby`` is ``jane``
  - ``..`` from ``jane`` is ``doe``
  - ``john`` is a child of ``doe``

  I made a mistake. ``john`` is the uncle of ``baby`` not ``jane``

* I move ``aka_uncle_of_baby`` from ``jane`` to ``john``

  .. code-block:: python
    :emphasize-lines: 1

    mv ../aka_uncle_of_baby ../../john/aka_uncle_of_baby

  the terminal_ goes back to the command line

* I add an empty file_ to ``doe`` from inside ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../aka_grandparent_of_baby

  the terminal_ goes back to the command line

----

* I can use the relationships to `change directories`_ from ``baby`` to ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../john/lil

  the terminal_ shows

  .. code-block:: python

    .../doe/john/lil

  I am in ``lil``

  - ``..`` from ``baby`` is ``jane``
  - ``..`` from ``jane`` is ``doe``
  - ``john`` is a child of ``doe``
  - ``lil`` is a child of ``john``

* I want to see what is in ``baby`` from inside ``lil`` in 1 step. I use their relationship with ls_

  .. code-block:: python
    :emphasize-lines: 1

    ls -a ../../jane/baby

  the terminal_ shows

  .. code-block:: python

    .                       .a_hidden_folder_in_baby
    ..                      aka_child_of_jane
    a_grandchild_of_doe     aka_child_of_johns_sibling
    .a_hidden_file_in_baby  an_empty_file_in_baby

  - ``..`` from ``lil`` is ``john``
  - ``..`` from ``john`` is ``doe``
  - ``jane`` is a child of ``doe``
  - ``baby`` is a child of ``jane``

* I add an empty file_ to ``baby`` from inside ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../jane/baby/aka_cousin_of_lil

  the terminal_ goes back to the command line

* I use tree_ to show what is in ``baby``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../jane/baby

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 4-5

    ../../jane/baby
    ├── a_grandchild_of_doe
    ├── aka_child_of_jane
    ├── aka_child_of_johns_sibling
    ├── aka_cousin_of_lil
    └── an_empty_file_in_baby

    1 directory, 5 files

* I add an empty file_ to ``john`` from inside ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../aka_parent_of_lil

  the terminal_ goes back to the command line

* I add an empty file_ to ``jane`` from inside ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../john/aka_aunt_of_lil

  the terminal_ goes back to the command line

  - ``..`` from ``lil`` is ``john``
  - ``..`` from ``john`` is ``doe``
  - ``jane`` is a child of ``doe``

  I made a mistake. ``jane`` is the aunt of ``lil`` not ``john``

* I move ``aka_aunt_of_lil`` from ``john`` to ``jane``

  .. code-block:: python
    :emphasize-lines: 1

    mv ../aka_aunt_of_lil ../../jane/aka_aunt_of_lil

  the terminal_ goes back to the command line

* I add an empty file_ to ``doe`` from inside ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    touch ../../aka_grandparent_of_lil

  the terminal_ goes back to the command line

* I look at the family tree of ``doe`` again, this time from inside ``lil``

  .. code-block:: python
    :emphasize-lines: 1

    tree ../../../doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 2-3, 10, 15-16, 20, 25, 27

    ../../../doe
    ├── aka_grandparent_of_baby
    ├── aka_grandparent_of_lil
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── a_child_of_doe
    │   ├── aka_sibling_of_john
    │   ├── aka_uncle_of_baby
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── a_grandchild_of_doe
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_johns_sibling
    │       ├── aka_cousin_of_lil
    │       └── an_empty_file_in_baby
    └── john
        ├── a_child_of_doe
        ├── aka_aunt_of_lil
        ├── aka_sibling_of_jane
        ├── an_empty_file_in_john
        └── lil
            ├── a_grandchild_of_doe
            ├── aka_child_of_janes_sibling
            ├── aka_child_of_john
            ├── aka_cousin_of_baby
            └── an_empty_file_in_lil

    5 directories, 23 files

* I `change directory`_ to the parent of ``doe``

  .. code-block:: python
    :emphasize-lines: 1

    cd ../../..

  the terminal_ shows

  .. code-block:: python

    .../pumping_python

  I am back in ``pumping_python``

* I show the ``doe`` family tree again

  .. code-block:: python
    :emphasize-lines: 1

    tree doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1, 9, 21

    doe
    ├── aka_grandparent_of_baby
    ├── aka_grandparent_of_lil
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── an_empty_file_in_doe
    ├── jane
    │   ├── a_child_of_doe
    │   ├── aka_aunt_of_lil
    │   ├── aka_sibling_of_john
    │   ├── an_empty_file_in_jane
    │   └── baby
    │       ├── a_grandchild_of_doe
    │       ├── aka_child_of_jane
    │       ├── aka_child_of_johns_sibling
    │       ├── aka_cousin_of_lil
    │       └── an_empty_file_in_baby
    └── john
        ├── a_child_of_doe
        ├── aka_sibling_of_jane
        ├── aka_uncle_of_baby
        ├── an_empty_file_in_john
        └── lil
            ├── a_grandchild_of_doe
            ├── aka_child_of_janes_sibling
            ├── aka_child_of_john
            ├── aka_cousin_of_baby
            └── an_empty_file_in_lil

    5 directories, 23 files

* I show the ``doe`` family tree and all its hidden secrets

  .. code-block:: python
    :emphasize-lines: 1

    tree -a doe

  the terminal_ shows

  .. literalinclude:: ../code/bonus/learnDirectoryStructureTree
    :language: shell

I can do things with files_ and directories_ in 1 step as long as

- I know their path (address)
- I know their relation to where I am and
- I can :ref:`write to the folder<how to view the permissions of a file>`

It is easier to get to where I want to go if I know where I am. :ref:`I know how to use directory relationships<how to use directory relationships>`

----

=================================================================================
how to remove a directory and all its contents
=================================================================================

----

* I try to remove ``doe`` and all its children and their children

  .. code-block:: python

    rm doe

  the terminal_ shows

  .. code-block:: python

    rm: cannot remove 'doe': Is a directory

  I cannot remove a directory_ this way

* I remove ``doe`` and all its children and their children with the ``-r/--recursive`` option

  .. DANGER:: This is a destructive operation takes a lot of effort and time to undo on MacOS_ or Linux_/`Windows Subsystem for Linux`_. Do you want to do it?

  .. code-block:: python
    :emphasize-lines: 1

    rm --recursive doe

  the terminal_ goes back to the command line

  .. NOTE::

    on Windows_ without `Windows Subsystem for Linux`_ use ``Remove-Item -Recurse -Force`` instead of ``rm --recursive``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      Remove-Item -Path doe -Recurse -Force


  - rm_ is used to remove files_ and folders_
  - ``rm`` means ``remove``
  - ``-r/--recursive/-Recurse`` means remove child directories_ and what is in them until there is nothing left, it goes through each child directory_ and removes everything including their children
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

I ran these commands to play with `folder (directory)`_ structure

* mkdir_ to make directories_
* cd_ to change directories_
* ls_ to show what is in a directory_
* tree_ to show a directory_ and its sub directories_ as a tree
* touch_ to make empty files_
* mv_ to rename a file_ and to move a file_
* rm_ to remove directories_

:ref:`How many questions do you think you can answer after going through this chapter?<questions about Directory Structure>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<learnDirectoryStructure.sh>`

----

*****************************************************************************************
what is next?
*****************************************************************************************

You know

* :ref:`how to make a directory`
* :ref:`how to see what is in a directory`
* :ref:`how to look at directory structure`
* :ref:`how to make an empty file`
* :ref:`how to use directory relationships`

Homework: use what you have learned - mkdir_, cd_, ls_, tree_ and touch_ to make your family tree. Send me the final thing when you are done.

:ref:`Click Here to see me make a Python Test Driven Development Environment<how to make a test driven development environment>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->