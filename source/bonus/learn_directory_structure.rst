:orphan:

.. include:: ../links.rst

#################################################################################
BONUS: learn directory structure
#################################################################################

This is an exercise in how your computer is organized into directories_ (folders_) and files_

*************************************************************************************
preview
*************************************************************************************

I will build the structure below step by step to see how files_ and folders_ are related like a family tree, and at the end will know how to move around in the structure because I will understand the relationships.

.. code-block:: shell

  doe
  ├── a_file_in_doe
  ├── aka_grandparent_of_baby
  ├── aka_grandparent_of_lil
  ├── aka_parent_of_jane
  ├── aka_parent_of_john
  ├── jane
  │   ├── a_child_of_doe
  │   ├── a_file_in_jane
  │   ├── aka_aunt_of_lil
  │   ├── aka_sibling_of_john
  │   └── baby
  │       ├── a_file_in_baby
  │       ├── a_grandchild_of_doe
  │       ├── aka_child_of_jane
  │       └── aka_cousin_of_lil
  └── john
      ├── a_file_in_john
      ├── aka_sibling_of_jane
      ├── aka_uncle_of_baby
      ├── another_child_of_doe
      └── lil
          ├── a_file_in_lil
          ├── aka_child_of_john
          ├── aka_cousin_of_baby
          └── another_grandchild_of_doe

You will become familiar with these commands

* mkdir_
* cd_
* ls_
* tree_
* touch_
* rm_

*********************************************************************************
questions about directory structure
*********************************************************************************

Here are questions you can answer after going through this chapter

* :ref:`what is a folder (directory)?<what is a folder?>`
* :ref:`what is a file?<what is a file?>`
* :ref:`how can I tell what directory I am in?<how to see the directory I am in>`
* :ref:`how can I change directories?<how to change directory>`
* :ref:`how can I make a directory?<how to make a directory>`
* :ref:`how can I see directory relationships?<how to look at directory structure>`
* :ref:`how can I see what is in a directory?<how to see what is in a directory>`
* :ref:`how can I make an empty file?<how to make an empty file>`
* :ref:`how can I use directory relationships?<how to use directory relationships>`
* :ref:`how can I remove a directory and everything inside it?<how to remove a directory and all its contents>`

*********************************************************************************
what is a folder?
*********************************************************************************

A `folder (directory)`_ is a container for files_. It helps organize things, just like a folder in a file cabinet is used to put files that belong together in one place.

I keep every project I work on in its own `folder (directory)`_. All the code from this book is kept in a folder_ named ``pumping_python``

*********************************************************************************
what is a file?
*********************************************************************************

A file_ is a collection or container for text, like paper we write or print on and keep in a folder. Their names usually end with an extension (optionally) to show the type of file_. For example

* ``.txt`` for a `plain text`_ file_
* ``.sh`` for a bash_ file_
* ``.ps1`` for a PowerShell_ file_
* ``.py`` for a :ref:`Python module<ModuleNotFoundError>`

*********************************************************************************
requirements
*********************************************************************************

I open a terminal_ to make sure the tree_ program_ is installed by typing this

.. code-block:: shell
  :emphasize-lines: 1

  tree

when it is not installed on the computer, the terminal_ shows

.. code-block:: shell

    tree: command not found

when it is installed, the terminal_ shows a tree of directories_ and files_. The tree_ program_ shows how files_ and folders_ on a computer are related.

=================================================================================
how to install tree
=================================================================================

* :ref:`how to install tree on Linux/Windows Subsystem for Linux`
* :ref:`how to install tree on Mac OS`
* :ref:`how to install tree on Windows without Windows Subsystem for Linux`

---------------------------------------------------------------------------------
how to install tree on Linux/Windows Subsystem for Linux
---------------------------------------------------------------------------------

.. code-block:: shell
  :emphasize-lines: 1

  sudo apt update

optionally, you can do a full upgrade if you want

.. code-block:: shell
  :emphasize-lines: 1

  sudo apt full-upgrade --yes

type this in the terminal_ to install tree_

.. code-block:: shell
  :emphasize-lines: 1

  sudo apt install tree

continue in :ref:`how to work in directories`

---------------------------------------------------------------------------------
how to install tree on Windows without Windows Subsystem for Linux
---------------------------------------------------------------------------------

tree_ comes with Windows_ you do not have to do anything. The following are things you would type in place of what I have in the chapter

* `New-Item`_ instead of touch_
* ``tree /F`` instead of tree_
* ``dir`` instead of ``ls --all/-a``

The path shown when you call pwd_ or tree_ shows ``\`` instead of ``/``, for example

.. code-block:: PowerShell

  ...\pumping_python

instead of

.. code-block:: shell

  .../pumping_python

continue with :ref:`how to work in directories`

---------------------------------------------------------------------------------
how to install tree on Mac OS
---------------------------------------------------------------------------------

* install brew_ (The Missing Package Manager for MacOS), if you do not have it already

  .. code-block:: shell
    :emphasize-lines: 1

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  the terminal_ shows instructions about how to add brew_ to your path

* copy and paste the 3 lines it shows in the terminal_ then use :kbd:`return` on the keyboard to run it, the terminal_ will not show anything if the commands run successfully

* use brew_ to install tree_

  .. code-block:: shell
    :emphasize-lines: 1

    brew install tree

* continue with :ref:`how to work in directories`

********************************************************************************************
how to work in directories
********************************************************************************************

=================================================================================
how to see the directory I am in
=================================================================================

I start by checking where I am in the terminal_. I can do this with the pwd_ program

.. code-block:: shell
  :emphasize-lines: 1

  pwd

the terminal_ shows

.. code-block:: shell

  .../pumping_python

because I am in the ``pumping_python`` folder_

pwd_ shows the path/address to the current folder_ I am in at the moment

.. NOTE::

  - If you see the same name, skip to the part where I create ``doe``
  - If you see a different name, continue to the next step :ref:`how to change directory`

=================================================================================
how to change directory
=================================================================================

I use the `cd program`_ to change directories_

.. code-block:: shell
  :emphasize-lines: 1

  cd pumping_python

the terminal_ shows

.. code-block:: shell

  cd: no such file or directory: pumping_python

this means the folder_ does not exist where I am

=================================================================================
how to make a directory
=================================================================================

* I use the `mkdir program`_ to make a `folder (directory)`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir pumping_python

  the terminal_ goes back to the command line

* I use cd_ to `change directory`_ again

  .. code-block:: shell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am now in the ``pumping_python`` `folder (directory)`_

  .. code-block:: shell

    .../pumping_python

  .. TIP:: to make sure I can see the ``pumping_python`` folder_ in my `Integrated Development Environment (IDE)`_ I have to open the folder. Here is how to do that with `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code .

    a new `Visual Studio Code`_ window opens in the ``pumping_python`` directory_

* I want to work in a directory named ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: doe

* I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir doe

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the folder_ to do some work in it

  .. code-block:: shell
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  I am in the ``doe`` folder_ I just made

* I use pwd_ to see where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

:ref:`I know how to make a directory<how to make a directory>`

----

=================================================================================
how to see what is in a directory
=================================================================================

* I can use ls_ to show what is in a directory_ and see information about the files_ in it

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/doe

  this directory_ is empty. ls_ has a few options, I try it again with one of them

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  .. attention::

    on MacOS_ you may get this error

    .. code-block:: shell

      ls: unrecognized option '--all'

    ``--all`` is the long form of the option, and there is usually a short form, use it instead

    .. code-block:: shell
      :emphasize-lines: 1

      ls -a

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

    the terminal_ does not show ``.`` and ``..``

  the terminal_ shows

  .. code-block:: shell

    .  ..

  - ``--all/-a`` tells ls_ to show things in the directory that start with ``.``, these are hidden by default
  - ``.`` represents the current directory

* I try to `change directory`_ to the ``.``

  .. code-block:: shell
    :emphasize-lines: 1

    cd .

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  - I am still in the same folder_
  - ``.`` is used for the directory_ I am in, which is ``doe`` in this case

* I try cd_ with ``..`` to see what happens

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  - ``..`` is used for the parent of a directory_ where I am
  - ``pumping_python`` is the parent of ``doe``

* I go back to ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

:ref:`I know how to see what is in a directory<how to see what is in a directory>`

----

=================================================================================
how to look at directory structure
=================================================================================

* I can use the `tree program`_ to see what files_ and folders_ are in a directory_. I type it in the terminal_ to see what is in the ``doe`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  it is empty

* I `change directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: jane

  the directory_ does not exist

* I make the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir jane

  the terminal_ goes back to the command line

* I use ls_ to see what is now in ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

  the terminal_ shows

  .. code-block:: shell

    .  ..  jane

* I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── jane

    2 directories, 0 files

* I try to go to a different directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: john

  the directory_ does not exist

* I make a new folder_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir john

  the terminal_ goes back to the command line

* I use ls_ to see what is in ``doe`` now

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  jane  john

* I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3

    .
    ├── jane
    └── john

    3 directories, 0 files

* I change directory_ to one of the children of ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: shell

    …/pumping_python/doe/jane

* I show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

* I use ls_ with the short form of the ``--all`` option

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

* I `change directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: baby

  I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir baby

  the terminal_ goes back to the command line

* I try to go to ``baby`` again

  .. code-block:: shell
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: shell

    .../doe/jane/baby

  I am in the ``baby`` folder_ which is in the ``jane`` folder_ which is in the ``doe`` folder_

* I go up a level to the parent of ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../doe/jane

  I am back in ``jane``

* I go up another level to the parent of ``jane``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  I am back in ``doe``

* I change directory_ to the other child of ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: shell

    …/pumping_python/doe/john

* I show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

* I use ls_ with the short form of the ``--all`` option

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

* I `change directory`_ to a child of this folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: lil

  I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir lil

  the terminal_ goes back to the command line

* I try to go to ``lil`` again

  .. code-block:: shell
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: shell

    .../doe/john/lil

  I am in the ``lil`` folder_

* I go up a level to the parent of ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../doe/john

  I am back in ``john``

* I go up another level to the parent of ``john``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  I am back in ``doe``

* I show the directory_ structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3, 5

    .
    ├── jane
    │   └── baby
    └── john
        └── lil

    5 directories, 0 files

:ref:`I know how to look at directory structure<how to look at directory structure>`

----

=================================================================================
how to make an empty file
=================================================================================

I can make empty files_ in a folder_ with the touch_ program

* I add an empty file_ to ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_doe

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item a_file_in_doe

  the terminal_ goes back to the command line

* I use ls_ to see what is in the folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``dir /ah`` instead of ``ls -a``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      dir /ah

    the terminal_ does not show ``.`` and ``..``

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_doe  jane  john

* I `change directory`_ to one of the children of ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe/jane

* I add an empty file_ with touch_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_jane

  the terminal_ goes back to the command line

* I show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_jane  baby

* I `change directory`_ to the parent of ``jane``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

* I `change directory`_ to the other child of ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe/john

* I add an empty file_ with touch_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_john

  the terminal_ goes back to the command line

* I show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_john  lil

* I `change directory`_ to the parent of ``john``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  I am back in ``doe``

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 7

    .
    ├── a_file_in_doe
    ├── jane
    │   ├── a_file_in_jane
    │   └── baby
    └── john
        ├── a_file_in_john
        └── lil

    5 directories, 3 files

  .. TIP:: Your terminal_ may use colors to show the difference between directories_ and files_

* I want to make a file_ in ``baby``. I use `change directory`_ to go to its parent first

  .. code-block:: shell
    :emphasize-lines: 1

    cd jane

  the terminal_ shows

  .. code-block:: shell

    /pumping_python/doe/jane

  I `change directory`_ to ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: shell

    .../doe/jane/baby

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_baby

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_baby

* I go back to the parent of ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../doe/jane/

* I go back to the parent of ``jane``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    ...pumping_python/doe

* I want to make a file_ in ``lil``. I use `change directory`_ to go to its parent first

  .. code-block:: shell
    :emphasize-lines: 1

    cd john

  the terminal_ shows

  .. code-block:: shell

    /pumping_python/doe/john

  I `change directory`_ to ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: shell

    .../doe/john/lil

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_lil

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_lil

* I go back to the parent of ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../doe/john/

* I go back to the parent of ``john``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    ...pumping_python/doe

  I am back in ``doe``

* I use tree_ to see what I have so far

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 6, 8, 10

    .
    ├── a_file_in_doe
    ├── jane
    │   ├── a_file_in_jane
    │   └── baby
    │       └── a_file_in_baby
    └── john
        ├── a_file_in_john
        └── lil
            └── a_file_in_lil

    5 directories, 5 files

:ref:`I know how to add empty files to folders<how to make an empty file>`

----

=================================================================================
how to use directory relationships
=================================================================================

* I try to go from ``doe`` to ``baby`` in 1 step

  .. code-block:: shell
    :emphasize-lines: 1

    cd baby

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: baby

  I cannot get to ``baby`` without its parent

* I try to go from ``doe`` to ``baby`` in 1 step with its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd jane/baby

  the terminal_ shows

  .. code-block:: shell

    .../doe/jane/baby

* I can go from ``baby`` to ``doe`` in 1 step with ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  Since ``..`` is for the parent of a directory_, ``../..`` is for the parent of a parent, that is a grandparent. I can use as many as I need for each parent, for example ``../../../..`` is the great great grand parent

* I try to go from ``doe`` to ``lil`` in 1 step

  .. code-block:: shell
    :emphasize-lines: 1

    cd lil

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: lil

  I cannot get to ``lil`` without its parent

* I try to go from ``doe`` to ``lil`` in 1 step with its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd john/lil

  the terminal_ shows

  .. code-block:: shell

    .../doe/john/lil

* I go back to ``doe`` in 1 step with ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

  I can only go directly to folders_ that are where I am or use the path to the folder_ I want to go to

* I go from ``doe`` to ``baby`` in 1 step with its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd jane/baby

  the terminal_ shows

  .. code-block:: shell

    .../doe/jane/baby

* I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_child_of_jane

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_baby  aka_child_of_jane

* I go back to ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

* I go from ``doe`` to ``lil`` in 1 step with its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd john/lil

  the terminal_ shows

  .. code-block:: shell

    .../doe/john/lil

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_child_of_john

  the terminal_ goes back to the command line

* I use ls_ to show what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_lil  aka_child_of_john

* I go back to ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/doe

* I add 2 empty files_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_parent_of_jane aka_parent_of_john

  the terminal_ goes back to the command line

* I use tree_ to see what ``doe`` looks like now

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3-4, 9, 14

    .
    ├── a_file_in_doe
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── jane
    │   ├── a_file_in_jane
    │   └── baby
    │       ├── a_file_in_baby
    │       └── aka_child_of_jane
    └── john
        ├── a_file_in_john
        └── lil
            ├── a_file_in_lil
            └── aka_child_of_john

    5 directories, 9 files

* I can add empty files_ in 1 step in any directory_ as long as

  - I know its path
  - I know its relation to where I am and
  - I can :ref:`write to the folder<how to view the permissions of a file>`

  I add 2 empty files_ in ``jane``

  .. code-block:: shell
    :emphasize-lines: 1

    touch jane/a_child_of_doe jane/aka_sibling_of_john

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item jane/a_child_of_doe jane/aka_sibling_of_john

  the terminal_ goes back to the command line

* I add 2 empty files_ in ``john``

  .. code-block:: shell
    :emphasize-lines: 1

    touch john/another_child_of_doe john/aka_sibling_of_jane

  the terminal_ goes back to the command line

* I add an empty file_ in ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    touch jane/baby/a_grandchild_of_doe

  the terminal_ goes back to the command line

* I add an empty file_ in ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    touch john/lil/another_grandchild_of_doe

  the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

* I use tree_ to show what is in ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    tree doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 6, 8, 11, 15-16, 20

    doe
    ├── a_file_in_doe
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── jane
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane
    │   ├── aka_sibling_of_john
    │   └── baby
    │       ├── a_file_in_baby
    │       ├── a_grandchild_of_doe
    │       └── aka_child_of_jane
    └── john
        ├── a_file_in_john
        ├── aka_sibling_of_jane
        ├── another_child_of_doe
        └── lil
            ├── a_file_in_lil
            ├── aka_child_of_john
            └── another_grandchild_of_doe

    5 directories, 15 files

* I type pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I am in the ``pumping_python`` folder_

* I can see what is in any folder_ when I know its path or relation to where I am

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a doe

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_doe  aka_parent_of_jane  aka_parent_of_john  jane  john

* I show what is in ``jane``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a doe/jane

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_child_of_doe  a_file_in_jane  aka_sibling_of_john  baby

* I show what is in ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a doe/jane/baby

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_baby  a_grandchild_of_doe  aka_child_of_jane

* I show what is in ``john``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a doe/john

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_john  aka_sibling_of_jane  another_child_of_doe  lil

* I show what is in ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a doe/john/lil

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_lil  aka_child_of_john  another_grandchild_of_doe

* I `change directory`_ to ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    cd doe/jane/baby

* I want to see what is in ``lil`` from inside ``baby`` in 1 step. ``../..`` is ``doe`` and I can go from ``doe`` to ``lil``, I use this relationship with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../john/lil

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_lil  aka_child_of_john  another_grandchild_of_doe

* I add an empty file_ to ``lil`` from ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    touch ../../john/lil/aka_cousin_of_baby

  the terminal_ goes back to the command line

* I use tree_ to show the structure of ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../john/lil

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    ../../john/lil
    ├── a_file_in_lil
    ├── aka_child_of_john
    ├── aka_cousin_of_baby
    └── another_grandchild_of_doe

    1 directory, 4 files

* I add 2 empty files_ from inside ``baby``, one to ``doe`` and another to ``john``

  .. code-block:: shell
    :emphasize-lines: 1

    touch ../../aka_grandparent_of_baby ../../john/aka_uncle_of_baby

  the terminal_ goes back to the command line

* I can use the relationship to `change directory`_ to ``lil`` from ``baby``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../john/lil

  the terminal_ shows

  .. code-block:: shell

    .../doe/john/lil

* I want to see what is in ``baby`` from inside ``lil`` in 1 step. I use their relationship with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../jane/baby

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_baby  a_grandchild_of_doe  aka_child_of_jane

* I add an empty file_ to ``baby`` from ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    touch ../../jane/baby/aka_cousin_of_lil

  the terminal_ goes back to the command line

* I use tree_ to show what is in ``baby`` now

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../jane/baby

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 5

    ../../jane/baby
    ├── a_file_in_baby
    ├── a_grandchild_of_doe
    ├── aka_child_of_jane
    └── aka_cousin_of_lil

    1 directory, 4 files

* I add 2 empty files_ from inside ``lil``, one to ``doe`` and another to ``jane``

  .. code-block:: shell
    :emphasize-lines: 1

    touch ../../aka_grandparent_of_lil ../../jane/aka_aunt_of_lil

  the terminal_ goes back to the command line

* I look at the structure of ``doe`` again, this time from inside ``lil``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../../doe

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3-4, 10, 16, 20, 25

    ../../../doe
    ├── a_file_in_doe
    ├── aka_grandparent_of_baby
    ├── aka_grandparent_of_lil
    ├── aka_parent_of_jane
    ├── aka_parent_of_john
    ├── jane
    │   ├── a_child_of_doe
    │   ├── a_file_in_jane
    │   ├── aka_aunt_of_lil
    │   ├── aka_sibling_of_john
    │   └── baby
    │       ├── a_file_in_baby
    │       ├── a_grandchild_of_doe
    │       ├── aka_child_of_jane
    │       └── aka_cousin_of_lil
    └── john
        ├── a_file_in_john
        ├── aka_sibling_of_jane
        ├── aka_uncle_of_baby
        ├── another_child_of_doe
        └── lil
            ├── a_file_in_lil
            ├── aka_child_of_john
            ├── aka_cousin_of_baby
            └── another_grandchild_of_doe

    5 directories, 21 files

* I `change directory`_ to the parent of ``doe``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

:ref:`I know how to use directory relationships<how to use directory relationships>`

----

=================================================================================
how to remove a directory and all its contents
=================================================================================

* I remove ``doe`` and all its children and their children

  .. DANGER:: This is a desctructive operation that CANNOT be undone on MacOS_ or Linux_/`Windows Subsystem for Linux`_, use it wisely

  .. code-block:: shell
    :emphasize-lines: 1

    rm -rf doe

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``Remove-Item -Recurse -Force`` instead of ``rm -rf``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      Remove-Item -Path doe -Recurse -Force


  the terminal_ goes back to the command line

  - rm_ is used to remove files_ and folders_
  - ``-r/-Recurse`` means remove child directories_ and what is in them until there is nothing left, it goes through each child directory_ and removes everything including their children
  - ``-f/-Force`` means do not ask me any questions, just remove the file_ or folder_ and everything inside it until there is nothing left

* I try to go back to the ``doe`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd doe

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: doe

*************************************************************************************
review
*************************************************************************************

I ran the following commands to play with `folder (directory)`_ structure

* mkdir_
* cd_
* ls_
* tree_
* touch_
* rm_

:ref:`How many questions can you answer after going through this chapter?<questions about Directory Structure>`

----

*************************************************************************************
code from the chapter
*************************************************************************************

:ref:`Do you want to see all the CODE I typed in this chapter?<learnDirectoryStructure.sh>`

----

*****************************************************************************************
what is next?
*****************************************************************************************

Do you have a Windows_ computer with `Windows Subsystem for Linux`_? :ref:`Click Here to install Windows Subsystem for Linux<how to install Windows Subsystem for Linux on Windows>`

If you have MacOS_ or already have :ref:`Windows Subsystem for Linux installed<how to install Windows Subsystem for Linux on Windows>` then you can :ref:`Click Here to see me make a Python Test Driven Development Environment<how to make a test driven development environment>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please leave a 5 star review. It helps other people get into the book too

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->