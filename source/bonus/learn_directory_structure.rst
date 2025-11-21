.. include:: ../links.rst

#################################################################################
learn directory structure
#################################################################################


*********************************************************************************
requirements
*********************************************************************************

Open a terminal_ to make sure tree_ is installed by typing this

.. code-block:: shell

  tree

when it is not installed on the computer, the terminal_ shows

.. code-block:: shell

    tree: command not found

when it is installed, you will see a tree of directories_ and files_

how to install tree on linux/Windows Subsystem Linux requirements
#################################################################################

.. code-block:: shell
  :emphasize-lines: 1

  sudo apt update

optionally, you can do a full upgrade if you ant

.. code-block:: shell
  :emphasize-lines: 1

  sudo apt full-upgrade --yes

type this in the terminal_ to install tree_

.. code-block:: shell
  :emphasize-lines: 1

  sudo apt install tree

how to install tree on mac OS
#################################################################################

first install brew_ (The Missing Package Manager for macOS), if you do not have it already

.. code-block:: shell
  :emphasize-lines: 1

  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

then use brew_ to install tree_

.. code-block:: shell
  :emphasize-lines: 1

  brew install tree

----

how to work with/in directories
#################################################################################

* I open a terminal_ to work in a directory named ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: parent

* I `make the directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python $

* I `change directory`_ to the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 1

    .../pumping_python/parent $

  I am in the folder_ I just made

* I use tree_ to see what is in the directory_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  there is nothing in it, it is empty

* I try to `change directory`_ to the ``.`` since it showed up when I typed tree_

  .. code-block:: shell
    :emphasize-lines: 1

    cd .

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent $

  I am still in the same folder_. ``.`` is shorthand for the directory_ I am in, which is ``parent`` in this case

* I use touch_ to make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_current_working_directory

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent $

* I use the pwd_ program to print the directory_ I am in to the screen

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I use tree_ to see what I have in the folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── aka_current_working_directory

    1 directory, 1 file

  I have ``.`` which is the directory_ I am in, and the file_ I made with touch_

* I can also use ls_ to list what is in the directory_ and see information about the files in it

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: shell

    aka_current_working_directory

  there is only one file_ in the directory_. ls_ has a few options, I try it again with one of them

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  aka_current_working_directory

  - ``--all`` tells ls_ to show things in the directory that start with ``.``, these are hidden by default
  - ``.`` represents the current directory

* I try cd_ with ``..`` to see what happens

  .. code-block:: shell

    cd ..

  the terminal shows

  .. code-block:: shell

    .../pumping_python $

  I am in the parent of ``parent``. ``..`` is a shorthand for the parent of the directory_ I am in. I go back to ``parent``

  .. code-block:: shell

    cd parent

  the terminal shows

  .. code-block:: shell

    .../pumping_python/parent

* I `change directory`_ to a different folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_parent

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: child_n_of_parent

  the directory_ does not exist. I make it

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child_n_of_parent

  the terminal_ goes back to the command line. I use ls_ to see what is in the folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: shell

    .  ..  aka_current_working_directory  child_n_of_parent

  .. NOTE:: Your terminal might use colors to show the difference between a file_ and a `folder/directory`_

  I use tree_ to see the current structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── aka_current_working_directory
    └── child_n_of_parent

    2 directories, 1 file

  this folder_ has 2 directories_

  - ``.`` which means the directory_ I am in
  - ``child_n_of_parent``

  and 1 file - ``aka_current_working_directory``

* I try to go to a different directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_n_of_child_n_of_parent

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: sibling_n_of_child_n_of_parent

  the directory_ does not exist. I make it

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir sibling_n_of_child_n_of_parent

  the terminal_ goes back to the command line. I use ls_ to see what is in the folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: shell

    .  ..  aka_current_working_directory  child_n_of_parent  sibling_n_of_child_n_of_parent

  I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── aka_current_working_directory
    ├── child_n_of_parent
    └── sibling_n_of_child_n_of_parent

    3 directories, 1 file

* I change directory_ to one of the children of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_parent

  the terminal_ shows

  .. code-block:: shell

    …/pumping_python/parent/child_n_of_parent $

  I list the contents of the folder_

  .. code-block:: shell

    ls

  the terminal_ goes back to the command line. I use the ``--all`` option

  .. code-block:: shell

    ls -a

  ``-a`` is the shortform of ``--all``. The terminal_ shows

  .. code-block:: shell

    .  ..

  I use tree_

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  this directory_ is empty

* I `make a directory`_ inside it

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child_n_of_child_n_of_parent

  the terminal_ goes back to the command line. I `change directory`

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_child_n_of_parent

  the terminal_ shows

  .. code-block:: shell

    .../parent/child_n_of_parent/child_n_of_child_n_of_parent $

  I `change directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    cd .

  the terminal_ shows

  .. code-block:: shell

    .../parent/child_n_of_parent/child_n_of_child_n_of_parent $

  I am already in this directory. I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  I make an empty file_ with touch_

  .. code-block:: shell
    :emphasize-lines: 1

    touch in_child_n_of_child_n_of_parent

  the terminal_ goes back to the command line. I pwd_ to see what directory_ I am in

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent/child_n_of_parent/child_n_of_child_n_of_parent

  I use tree_ again

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── in_child_n_of_child_n_of_parent

    1 directory, 1

  I use touch_ to make another empty file

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_a_grandchild_of_parent

  the terminal_ goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_child_n_of_child_n

  the terminal_ goes back to the command line. I make one more empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_a_cousin_of_child_n_of_sibling_n_of_child_n_of_parent

  the terminal_ goes back to the command line. I use tree_ to see what I have now

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── aka_a_cousin_of_child_n_of_sibling_n_of_child_n_of_parent
    ├── aka_a_grandchild_of_parent
    ├── aka_child_n_of_child_n
    └── in_child_n_of_child_n_o

    1 directory, 4 files

* I try to go back to the ``parent`` directory_ I started from

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: parent

  I try to go to a directory_ in the ``parent`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: child_n_of_parent

  I try to go to another directory_ in the ``parent`` folder

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: sibling_n_of_child_n_of_parent

  I try to go to another folder_ in the ``child_n_of_parent`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_sibling_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: child_n_of_sibling_n_of_child_n_of_parent

  I try to go to a folder_ that does not exist

  .. code-block:: shell
    :emphasize-lines: 1

    cd non_existent_child_of_child_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: non_existent_child_of_child_n_of_child_n_of_parent

  I list all the files_ and folders_ where I am at the moment

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: shell

    .  ..  aka_a_cousin_of_child_n_of_sibling_n_of_child_n_of_parent  aka_a_grandchild_of_parent  aka_child_n_of_child_n  in_child_n_of_child_n_of_parent

  none of the directories_ I tried to go to are in this directory_. I use pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../parent/child_n_of_parent/child_n_of_child_n_of_parent $

* I can go to the parent of a directory_ with a shortcut

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  ``..`` is shorthand for the parent of the directory_ I am in. the terminal shows

  .. code-block:: shell

    /workspaces/…/pumping_python/parent/child_n_of_parent $

  I use pwd_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../parent/child_n_of_parent

  I use ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  child_n_of_child_n_of_parent

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    .
    └── child_n_of_child_n_of_parent
        ├── aka_a_cousin_of_child_n_of_sibling_n_of_child_n_of_parent
        ├── aka_a_grandchild_of_parent
        ├── aka_child_n_of_child_n
        └── in_child_n_of_child_n_of_parent

    2 directories, 4 files

* I go up another level

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: shell

    .../pumping_python/parent $

  I am back at the first directory_ I made - ``parent``. I type pwd_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../pumping_python/parent

  I list the contents

  .. code-block:: shell
    :emphasize-lines:

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  aka_current_working_directory  child_n_of_parent  sibling_n_of_child_n_of_parent

  I use tree_

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal shows

  .. code-block:: shell

    .
    ├── aka_current_working_directory
    ├── child_n_of_parent
    │   └── child_n_of_child_n_of_parent
    │       ├── aka_a_cousin_of_child_n_of_sibling_n_of_child_n_of_parent
    │       ├── aka_a_grandchild_of_parent
    │       ├── aka_child_n_of_child_n
    │       └── in_child_n_of_child_n_of_parent
    └── sibling_n_of_child_n_of_parent

    4 directories, 5 files

* I `change directory`_ to another child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_n_of_child_n_of_parent $

  I list the contents

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    .

    0 directories, 0 files

  I `make a directory`_

  .. code-block:: python

    mkdir child_n_of_sibling_n_of_child_n_of_parent

  the terminal goes back to the command line. I `change directory`_ to the folder_ I just made

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_sibling_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_n_of_child_n_of_parent/child_n_of_sibling_n_of_child_n_of_parent $

  I make another directory_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child_n_of_child_n_of_sibling_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_n_of_child_n_of_parent/child_n_of_sibling_n_of_child_n_of_parent $

  I `change directory`_ to it

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_n_of_child_n_of_sibling_n_of_child_n_of_parent

  the terminal shows

  .. code-block:: shell

    .../sibling_n_of_child_n_of_parent/child_n_of_sibling_n_of_child_n_of_parent/child_n_of_child_n_of_sibling_n_of_child_n_of_parent $

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch in_child_n_of_child_n_of_sibling_n_of_child_n_of_parent

  the terminal goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_another_grandchild_of_parent

  the terminal goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_child_n_of_child_n_sibling_n

  the terminal goes back to the command line. I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  aka_another_grandchild_of_parent  aka_child_n_of_child_n_sibling_n  in_child_n_of_child_n_of_sibling_n_of_child_n_of_parent



* I `change directory`_ to the parent of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: shell

    .../pumping_python $

  I show the current working directory (where I am)

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    /workspaces/pumping_python/pumping_python


* I remove the ``parent`` directory_ and all its children and grandchildren

  .. code-block:: shell
    :emphasize-lines: 1

    rm -rf parent

  the terminal_ goes back to the command line

  - rm_ is used to remove files_ and folders_
  - ``-r`` means remove directories_ and what is in them recursively, it goes through each child directory_ and removes everything
  - ``-f`` means "force", do not ask any questions, just remove the file_ or folder_

* I try to go to the ``parent`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: parent