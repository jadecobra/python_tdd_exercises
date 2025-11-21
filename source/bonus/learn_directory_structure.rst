.. include:: ../links.rst

#################################################################################
learn directory structure
#################################################################################


*********************************************************************************
requirements
*********************************************************************************

I open a terminal_ to make sure tree_ is installed by typing this

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

* I want to work in a directory named ``parent``

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

* I use pwd_ to see where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../pumping_python/parent

  pwd_ shows the path/address to the current folder_ I am in at the moment

* I can use ls_ to list what is in the directory_ and see information about the files in it

  .. code-block:: shell
    :emphasize-lines: 1

    ls

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent $

  the directory_ is empty. ls_ has a few options, I try it again with one of them

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..

  - ``--all`` tells ls_ to show things in the directory that start with ``.``, these are hidden by default

  .. TIP:: options like ``--all`` are the long form and usually have a short form e.g.

    .. code-block:: shell

      ls -a

  - ``.`` represents the current directory

* I try to `change directory`_ to the ``.``

  .. code-block:: shell
    :emphasize-lines: 1

    cd .

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent $

  I am still in the same folder_. ``.`` is use for the directory_ I am in, which is ``parent`` in this case

* I try cd_ with ``..`` to see what happens

  .. code-block:: shell

    cd ..

  the terminal shows

  .. code-block:: shell

    .../pumping_python $

  I am in the parent of ``parent``. ``..`` is used for the parent of the directory_ I am in. I go back to ``parent``

  .. code-block:: shell

    cd parent

  the terminal shows

  .. code-block:: shell

    .../pumping_python/parent

* I can use tree_ to show the directory_ structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

  there is nothing in it, it is empty

* I use touch_ to make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_a_file_in_parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent $

* I use ls_ to see what is in the folder

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  a_a_file_in_parent

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── a_a_file_in_parent

    1 directory, 1 file

  I have ``.`` which is the directory_ I am in, and the file_ I made with touch_

* I `change directory`_ to a different folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: child

  the directory_ does not exist. I make it

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child

  the terminal_ goes back to the command line. I use ls_ to see what is in the folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: shell

    .  ..  child  a_a_file_in_parent

  .. NOTE:: Your terminal might use colors to show the difference between a file_ and a `folder/directory`_

  I use tree_ to see the current structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── child
    └── a_a_file_in_parent

    2 directories, 1 file

  this folder_ has 2 directories_

  - ``.`` which means the directory_ I am in
  - ``child``

  and 1 file - ``a_a_file_in_parent``

* I try to go to a different directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: sibling_of_child

  the directory_ does not exist. I make it

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir sibling_of_child

  the terminal_ goes back to the command line. I use ls_ to see what is in the folder_ now

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: shell

    .  ..  child  a_a_file_in_parent  sibling_of_child

  I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── child
    ├── a_a_file_in_parent
    └── sibling_of_child

    3 directories, 1 file

* I change directory_ to one of the children of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    …/pumping_python/parent/child $

  I list the contents of the folder_

  .. code-block:: shell

    ls

  the terminal_ goes back to the command line. I use the short form of the ``--all`` option

  .. code-block:: shell

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..

  I use tree_

  .. code-block:: shell

    tree

  the terminal_ shows

  .. code-block:: shell

    .

    0 directories, 0 files

* I `make a directory`_ inside it

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir child_of_child

  the terminal_ goes back to the command line. I `change directory`

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child $

  I `change directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    cd .

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child $

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

    touch a_a_file_in_child_of_child

  the terminal_ goes back to the command line. I use touch_ to make another empty file

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_grandchild_of_parent

  the terminal_ goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch child_of_child

  the terminal_ goes back to the command line. I use tree_ to see what I have now

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── child_of_child
    ├── a_grandchild_of_parent
    └── a_a_file_in_child_of_child

    1 directory, 3 files

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

    cd child

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: child

  I try to go to another directory_ in the ``parent`` folder

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: sibling_of_child

  I try to go to a folder_ in the ``child`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: child_of_sibling_of_child

  I try to go to a folder_ that does not exist

  .. code-block:: shell
    :emphasize-lines: 1

    cd does_not_exist

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: does_not_exist

  I list all the files_ and folders_ where I am at the moment

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal_ shows

  .. code-block:: shell

    .   child_of_child      a_a_file_in_child_of_child
    ..  a_grandchild_of_parent

  none of the directories_ I tried to go to are in this directory_. I use pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../parent/child/child_of_child

* I can go to the parent of a directory_ with ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  ``..`` is shorthand for the parent of the directory_ I am in. the terminal shows

  .. code-block:: shell

    /workspaces/…/pumping_python/parent/child $

  I use pwd_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../parent/child

  I use ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  child_of_child

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    .
    └── child_of_child
        ├── child_of_child
        ├── a_grandchild_of_parent
        └── a_a_file_in_child_of_child

    2 directories, 3 files

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

    .  ..  child  a_a_file_in_parent  sibling_of_child

  I view the structure

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal shows

  .. code-block:: shell

  .
  ├── child
  │   └── child_of_child
  │       ├── child_of_child
  │       ├── a_grandchild_of_parent
  │       └── a_a_file_in_child_of_child
  ├── a_a_file_in_parent
  └── sibling_of_child

  4 directories, 4 files

* I `change directory`_ to the other child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child $

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

    mkdir child_of_sibling_of_child

  the terminal goes back to the command line. I `change directory`_ to the folder_ I just made

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_sibling_of_child

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child $

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_child_of_sibling_of_child

  the terminal goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch another_grandchild_of_parent

  the terminal goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch child_of_sibling_of_child

  the terminal goes back to the command line. I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .   child_of_sibling_of_child            another_grandchild_of_parent
    ..  a_file_in_child_of_sibling_of_child

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── child_of_sibling_of_child
    ├── a_file_in_child_of_sibling_of_child
    └── another_grandchild_of_parent

    1 directory, 3 files

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

    cd child

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: child

  I try to go to another directory_ in the ``parent`` folder

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: sibling_of_child

  I try to go to another folder_ in the ``child`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: child_of_child

  I try to go to a folder_ that does not exist

  .. code-block:: shell
    :emphasize-lines: 1

    cd does_not_exist

  the terminal shows

  .. code-block:: shell

    cd: no such file or directory: does_not_exist

  I use pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child $

* I can go to the parent of the directory_ I am in

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child $

  I use pwd_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child $

  I use ls_

  .. code-block:: shell
    :emphasize-lines: 1

    ls --all

  the terminal shows

  .. code-block:: shell

    .  ..  child_of_sibling_of_child

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    .
    └── child_of_sibling_of_child
        ├── child_of_sibling_of_child
        ├── a_file_in_child_of_sibling_of_child
        └── another_grandchild_of_parent

    2 directories, 3 files

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

    .  ..  child  a_a_file_in_parent  sibling_of_child

  I use tree_ to see the structure

  .. code-block:: python
    :emphasize-lines: 1

    tree

  the terminal shows

  .. code-block:: shell

    .
    ├── child
    │   └── child_of_child
    │       ├── child_of_child
    │       ├── a_grandchild_of_parent
    │       └── in_child_of_child
    ├── a_a_file_in_parent
    └── sibling_of_child
        └── child_of_sibling_of_child
            ├── child_of_sibling_of_child
            ├── another_grandchild_of_parent
            └── in_child_of_sibling_of_child

    5 directories, 7 files

* I `change directory`_ to a child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal goes back to the command line. I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_child

  the terminal goes back to the command line. I make another empty file

  .. code-block:: shell
    :emphasize-lines:

    touch aunt_or_uncle_of_another_grandchild_of_parent

  the terminal goes back to the command line

* I want to `change directory` to ``sibling_of_child``, I can use the path of a folder_ and the short forms to get to it, once I know its relation to where I am. I use cd_ with ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../sibling_of_child

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child $

  I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch in_sibling_of_child

  the terminal goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aunt_or_uncle_of_a_grandchild_of_parent

* I `change directory`_ back to the parent of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../...

  the terminal shows

  .. code-block:: shell

    ../pumping_python $

  I show the directory_ structure of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    tree parent

  the terminal shows

  .. code-block:: shell

    parent
    ├── child
    │   ├── a_file_in_child
    │   ├── aunt_or_uncle_of_another_grandchild_of_parent
    │   └── child_of_child
    │       ├── child_of_child
    │       ├── a_grandchild_of_parent
    │       └── a_file_in_child_of_child
    ├── a_file_in_parent
    └── sibling_of_child
        ├── aunt_or_uncle_of_a_grandchild_of_parent
        ├── child_of_sibling_of_child
        │   ├── child_of_sibling_of_child
        │   ├── a_file_in_child_of_sibling_of_child
        │   └── another_grandchild_of_parent
        └── in_sibling_of_child

    5 directories, 11 files

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