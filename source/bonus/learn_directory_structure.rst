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

  parent
  ├── a_file_in_parent
  ├── aka_grandparent_of_child_of_child
  ├── aka_grandparent_of_child_of_sibling_of_child
  ├── child
  │   ├── a_file_in_child
  │   ├── aunt_or_uncle_of_another_grandchild_of_parent
  │   └── child_of_child
  │       ├── a_file_in_child_of_child
  │       ├── a_grandchild_of_parent
  │       └── cousin_of_child_of_sibling_of_child
  └── sibling_of_child
      ├── a_file_in_sibling_of_child
      ├── aunt_or_uncle_of_a_grandchild_of_parent
      └── child_of_sibling_of_child
          ├── a_file_in_child_of_sibling_of_child
          ├── another_grandchild_of_parent
          └── cousin_of_child_of_child

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

* :ref:`What is a folder (directory)?<what is a folder?>`
* :ref:`what is a file?<what is a file?>`
* :ref:`How can I tell what directory I am in?<how to see the directory I am in>`
* :ref:`How can I change directories?<how to change directory>`
* :ref:`How can I make a directory?<how to make a directory>`
* :ref:`How can I see directory relationships?<how to look at directory structure>`
* :ref:`How can I list what is in a directory?<how to list what is in a directory>`
* :ref:`How can I make an empty file?<how to make an empty file>`
* :ref:`How can I use directory relationships?<how to use directory relationships>`
* :ref:`How can I remove a directory and everything inside it?<how to remove a directory and all its contents>`

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

* copy and paste the 3 lines it shows in the terminal_ then hit ``return`` to run it, the terminal_ will not show anything if the commands run successfully

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

.. NOTE:: If you see the same name, skip to the part where I create ``parent``. If you see a different name, continue to the next step :ref:`how to change directory`.

=================================================================================
how to change directory
=================================================================================

I use the `cd program`_ to change directories_

.. code-block:: shell
  :emphasize-lines: 1

  cd pumping_python

the terminal_ shows

.. code-block:: shell

  cd: pumping_python: No such file or directory

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

  .. TIP:: to make sure I can see the ``pumping_python`` folder_ in my `Integrated Development Environment (IDE)`_ I have to open the folder. Here's how to do that with `Visual Studio Code`_

    .. code-block:: shell
      :emphasize-lines: 1

      code .

    a new `Visual Studio Code`_ window opens in the ``pumping_python`` directory_

* I want to work in a directory named ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: parent

* I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

* I `change directory`_ to the folder_ to do some work in it

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am in the ``parent`` folder_ I just made

* I use pwd_ to see where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

=================================================================================
how to list what is in a directory
=================================================================================

* I can use ls_ to show what is in a directory_ and see information about the files_ in it

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line

  .. code-block:: shell

    .../pumping_python/parent

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

    .../pumping_python/parent

  - I am still in the same folder_
  - ``.`` is used for the directory_ I am in, which is ``parent`` in this case

* I try cd_ with ``..`` to see what happens

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  - ``..`` is used for the parent of a directory_ where I am
  - ``pumping_python`` is the parent of ``parent``

* I go back to ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

=================================================================================
how to look at directory structure
=================================================================================

* I can use the `tree program`_ to see what files_ and folders_ are in a directory_. I type it in the terminal_ to see what is in the ``parent`` directory_

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

    cd child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: child

  the directory_ does not exist

* I make the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child

  the terminal_ goes back to the command line

* I use ls_ to see what is now in ``parent``

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

    .  ..  child

* I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2

    .
    └── child

    2 directories, 0 files

* I try to go to a different directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: sibling_of_child

  the directory_ does not exist

* I make a new folder_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir sibling_of_child

  the terminal_ goes back to the command line

* I use ls_ to see what is in ``parent`` now

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  child  sibling_of_child

* I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3

    .
    ├── child
    └── sibling_of_child

    3 directories, 0 files

* I change directory_ to one of the children of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    …/pumping_python/parent/child

* I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line. I use ls_ with the short form of the ``--all`` option

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..

  I use tree_

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

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: child_of_child: No such file or directory

  I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child_of_child

  the terminal_ goes back to the command line

* I try to go to ``child_of_child`` again

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

* I go up a level to the parent of ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../parent/child

  I am back in ``child``

* I go up another level to the parent of ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am back in ``parent``

* I change directory_ to the other child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    …/pumping_python/parent/sibling_of_child

* I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ goes back to the command line. I use ls_ with the short form of the ``--all`` option

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..

  I use tree_

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

    cd child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: child_of_sibling_of_child: No such file or directory

  I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child_of_sibling_of_child

  the terminal_ goes back to the command line

* I try to go to ``child_of_sibling_of_child`` again

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

* I go up a level to the parent of ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I am back in ``sibling_of_child``

* I go up another level to the parent of ``sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am back in ``parent``

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
    ├── child
    │   └── child_of_child
    └── sibling_of_child
        └── child_of_sibling_of_child

    5 directories, 0 files

=================================================================================
how to make an empty file
=================================================================================

I can make empty files_ in a folder_ with the touch_ program

* I add an empty file_ to ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_parent

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item a_file_in_parent

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

    .  ..  a_file_in_parent  child  sibling_of_child

* I `change directory`_ to one of the children of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent/child

* I add an empty file_ with touch_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_child

  the terminal_ goes back to the command line

* I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child  child_of_child

* I `change directory`_ to the parent of ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I `change directory`_ to the other child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent/sibling_of_child

* I add an empty file_ with touch_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_sibling_of_child

  the terminal_ goes back to the command line

* I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_sibling_of_child  child_of_sibling_of_child

* I `change directory`_ to the parent of ``sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 2, 4, 7

    .
    ├── a_file_in_parent
    ├── child
    │   ├── a_file_in_child
    │   └── child_of_child
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        └── child_of_sibling_of_child

    5 directories, 3 files

  .. TIP:: Your terminal_ may use colors to show the difference between directories_ and files_

* I want to make a file in ``child_of_child``. I use `change directory`_ to go to its parent first

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    /pumping_python/parent/child

  I `change directory`_ to ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

=================================================================================
how to use directory relationships
=================================================================================

* I can go from ``child_of_child`` to ``parent`` in 1 step by using ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  Since ``..`` is for the parent of a directory_, ``../..`` is for the parent of a parent, that is a grandparent. I can use as many ``..``'s I need for each parent, for example ``../../../..`` would be the great great grand parent

* I try to go from ``parent`` to ``child_of_child`` in 1 step

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: child_of_child: No such file or directory

  I cannot get to ``child_of_child`` without its parent

* I try to go from ``parent`` to ``child_of_child`` in 1 step with its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_grandchild_of_parent

  the terminal_ goes back to the command line

* I use ls_ to list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_grandchild_of_parent

* I go back to ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I want to make a file in ``child_of_sibling_of_child``. I use `change directory`_ to go to its parent first

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    /pumping_python/parent/sibling_of_child

  I `change directory`_ to ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

* I go from ``child_of_sibling_of_child`` to ``parent`` in 1 step

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I try to go from ``parent`` to ``child_of_sibling_of_child`` in 1 step

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: child_of_sibling_of_child: No such file or directory

  I can only go directly to folders_ that exist where I am or use the path to the folder_ I want to go to

* I go from ``parent`` to ``child_of_sibling_of_child`` in 1 step with its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch another_grandchild_of_parent

  the terminal_ goes back to the command line

* I use ls_ to list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  another_grandchild_of_parent

* I go back to ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I add an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_grandparent_of_child_of_child

  the terminal_ goes back to the command line

* I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_grandparent_of_child_of_sibling_of_child

  the terminal_ goes back to the command line

* I use tree_ to see what ``parent`` looks like now

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
    :emphasize-lines: 3-4, 8, 12

    .
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_child_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   └── child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        └── child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 7 files

* I can add an empty file_ in 1 step in any directory_ as long as

  - I know its path
  - I know its relation to where I am and
  - I have permission to write to the folder_

  I add another empty file_ in ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch child/aunt_or_uncle_of_another_grandchild_of_parent

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item child/aunt_or_uncle_of_another_grandchild_of_parent

  the terminal_ goes back to the command line

* I add another empty file_ in ``sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch sibling_of_child/aunt_or_uncle_of_a_grandchild_of_parent

  the terminal_ goes back to the command line

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 7, 12

    .
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_child_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   ├── aunt_or_uncle_of_another_grandchild_of_parent
    │   └── child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        ├── aunt_or_uncle_of_a_grandchild_of_parent
        └── child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 9 files

* I add an empty file_ in ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch child/child_of_child/a_file_in_child_of_child

  the terminal_ goes back to the command line

* I add an empty file_ in ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch sibling_of_child/child_of_sibling_of_child/a_file_in_child_of_sibling_of_child

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use `New-Item`_ instead of touch_

    .. code-block:: PowerShell
      :emphasize-lines: 1

      New-Item sibling_of_child/child_of_sibling_of_child/a_file_in_child_of_sibling_of_child

  the terminal_ goes back to the command line

* I `change directory`_ to the parent of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

* I use tree_ to show what is in ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    tree parent

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 9, 15

    parent
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_child_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   ├── aunt_or_uncle_of_another_grandchild_of_parent
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        ├── aunt_or_uncle_of_a_grandchild_of_parent
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 11 files

* I type pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

* I can list the contents of any folder_ once I know its path or relation to where I am

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a parent

  the terminal_ shows

  .. code-block:: shell

    .                 aka_grandparent_of_child_of_child             sibling_of_child
    ..                aka_grandparent_of_child_of_sibling_of_child
    a_file_in_parent  child

* I list the contents of ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a parent/child

  the terminal_ shows

  .. code-block:: shell

    .   a_file_in_child                                child_of_child
    ..  aunt_or_uncle_of_another_grandchild_of_parent

* I list the contents of ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a parent/child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child_of_child  a_grandchild_of_parent

* I list the contents of ``sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a parent/sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .   a_file_in_sibling_of_child               child_of_sibling_of_child
    ..  aunt_or_uncle_of_a_grandchild_of_parent

* I list the contents of ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a parent/sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child_of_sibling_of_child  another_grandchild_of_parent

* I `change directory`_ to ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent/child/child_of_child

* I want to list the contents of ``child_of_sibling_of_child`` from inside ``child_of_child`` in 1 step. ``../..`` is ``parent`` and I can go from ``parent`` to ``child_of_sibling_of_child``, I use the relationship with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child_of_sibling_of_child  another_grandchild_of_parent

* I add an empty file_ to ``child_of_sibling_of_child`` from ``child_of_child``

  .. code-block:: shell

    touch ../../sibling_of_child/child_of_sibling_of_child/cousin_of_child_of_child

  the terminal_ goes back to the command line

* I use tree_ this time

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    ../../sibling_of_child/child_of_sibling_of_child
    ├── a_file_in_child_of_sibling_of_child
    ├── another_grandchild_of_parent
    └── cousin_of_child_of_child

    1 directory, 3 files

* I can use the same thing to `change directory`_ to ``child_of_sibling_of_child`` from ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child $

* I want to list the contents of ``child_of_child`` from inside ``child_of_sibling_of_child`` in 1 step. Since ``../..`` is ``parent`` and I can go from ``parent`` to ``child_of_child``, I use the relationship with ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child_of_child  a_grandchild_of_parent

* I add an empty file_ to ``child_of_child`` from ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch ../../child/child_of_child/cousin_of_child_of_sibling_of_child

  the terminal_ goes back to the command line

* I use tree_ to show what is in ``child_of_child`` now

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../child/child_of_child

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4

    ../../child/child_of_child
    ├── a_file_in_child_of_child
    ├── a_grandchild_of_parent
    └── cousin_of_child_of_sibling_of_child

    1 directory, 3 files

* I look at the structure of ``parent`` again, this time from inside ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../../parent

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 11, 18

    ../../../parent
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_child_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   ├── aunt_or_uncle_of_another_grandchild_of_parent
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       ├── a_grandchild_of_parent
    │       └── cousin_of_child_of_sibling_of_child
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        ├── aunt_or_uncle_of_a_grandchild_of_parent
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            ├── another_grandchild_of_parent
            └── cousin_of_child_of_child

    5 directories, 13 files

* I `change directory`_ to the parent of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I show the current working directory (where I am)

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../

=================================================================================
how to remove a directory and all its contents
=================================================================================

* I remove ``parent`` and all its descendants

  .. DANGER:: This is a desctructive operation that CANNOT be undone on MacOS_ or Linux_/`Windows Subsystem for Linux`_, use it wisely

  .. code-block:: shell
    :emphasize-lines: 1

    rm -rf parent

  .. attention::

    on Windows_ without `Windows Subsystem for Linux`_ use ``Remove-Item -Recurse -Force`` instead of ``rm -rf``

    .. code-block:: PowerShell
      :emphasize-lines: 1

      Remove-Item -Path parent -Recurse -Force


  the terminal_ goes back to the command line

  - rm_ is used to remove files_ and folders_
  - ``-r/-Recurse`` means remove child directories_ and what is in them recursively, it goes through each child directory_ and removes everything include their children
  - ``-f/-Force`` means "force", do not ask me any questions, just remove the file_ or folder_ and all its children with extreme prejudice

* I try to go back to the ``parent`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: parent

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

*************************************************************************************
what is next?
*************************************************************************************

:ref:`Would you like to see me make a Test Driven Development Environment<how to make a test driven development environment>`

----

*********************************************************************************
please leave a review
*********************************************************************************

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review, if this has been a 5 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->