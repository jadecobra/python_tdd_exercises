.. include:: ../links.rst

#################################################################################
learn directory structure
#################################################################################


*********************************************************************************
requirements
*********************************************************************************

I open a terminal_ to make sure the tree_ program is installed by typing this

.. code-block:: shell

  tree

when it is not installed on the computer, the terminal_ shows

.. code-block:: shell

    tree: command not found

when it is installed, the terminal_ shows a tree of directories_ and files_. The tree_ program shows how files_ and folders_ on a computer are related.

A `folder/directory`_ is a container for files_. It helps organize things, just like a folder in a file cabinet is used to put files that belong together in one place.

I keep every project I work on in its own `folder/directory`_. All the code from this book will be kept in a folder_ named ``pumping_python``

A file_ is a collection or container for text, like paper we write or print on and keep in a folder. Their names usually end with an extension (optionally) to show the type of file_. For example

* `.txt` for a `plain text`_ file_
* `.sh` for a bash_ file_
* `.ps1` for a PowerShell_ file_
* `.py` for a :ref:`Python module<ModuleNotFoundError>`

.. TIP:: to make sure I can see the ``pumping_python`` folder_ in my `Integrated Development Environment (IDE)`_ I have to open the folder. Here's how to do that with `Visual Studio Code`_

  .. code-block:: shell
    :emphasize-lines: 1

    code .

  a new `Visual Studio Code`_ window opens in the ``pumping_python`` directory_

how to install tree on linux/Windows Subsystem Linux requirements
#################################################################################

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

.. ADMONITION:: On Windows_ without `Windows SubSystem Linux`_ use the following substitions

  * `New-Item`_ instead of touch_
  * ``tree /F`` instead of tree_
  * ``ls -Force`` instead of ``ls --all/-a``

  The path shown when you call pwd_ or tree_ will show ``\`` instead of ``/`` for example

  .. code-block:: PowerShell

    ...\pumping_python

  instead of

  .. code-block:: shell

    .../pumping_python

********************************************************************************************
how to work with/in directories
********************************************************************************************

how to see the current directory
#################################################################################################

I start by checking where I am in the terminal_. I can do this with the pwd_ program

.. code-block:: shell
  :emphasize-lines: 1

  pwd

the terminal_ shows

.. code-block:: shell

  .../pumping_python

because I am in the ``pumping_python`` folder_. pwd_ shows the path/address to the current folder_ I am in at the moment

.. NOTE:: If you see a different name, you can go to the next step :ref:`how to change directory`

how to change directory
#################################################################################################

I use the cd_ program_ to change directories_

.. code-block:: shell
  :emphasize-lines: 1

  cd pumping_python

the terminal_ shows

.. code-block:: shell

  cd: pumping_python: No such file or directory

this means the folder_ does not exist where I am

how to make a directory
#################################################################################################

* I use the mkdir_ program_ to make a `folder/directory`_

  .. code-block:: shell
    :emphasize-lines: 1

    mkdir pumping_python

  the terminal_ goes back to the command line

* I use cd_ to `change directory`_ again

  .. code-block:: shell
    :emphasize-lines: 1

    cd pumping_python

  the terminal_ shows I am now in the ``pumping_python`` `folder/directory`_

  .. code-block:: shell

    .../pumping_python

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
    :emphasize-lines: 1

    .../pumping_python/parent

  I am in the ``parent`` folder_ I just made

* I use pwd_ to see where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

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

  .. ATTENTION:: on MacOS_ you may get this error

    .. code-block:: shell

      ls: unrecognized option '--all'

    ``--all`` is the long form of the option, and there is usually a short form, use it instead

    .. code-block:: shell
      :emphasize-lines: 1

      ls -a

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``ls -Force`` instead of ``ls -a``

    .. code-block:: python
      :emphasize-lines: 1

      ls -Force

    the terminal will not show ``.`` and ``..``

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

how to look at directory structure
#################################################################################################

* I can use the tree_ program_ to see what files_ and folders_ are in a directory_. I type it in the terminal_ to see what is in the ``parent`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
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

    2 directories

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

  the terminal_ goes back to the command line. I try to go to ``child_of_child`` again

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

* I `change directory`_ to a child

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

  the terminal_ goes back to the command line. I try to go to ``child_of_sibling_of_child`` again

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

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3, 6

    .
    ├── child
    │   └── child_of_child
    └── sibling_of_child
        └── child_of_sibling_of_child

    5 directories, 0 files

how to make an empty file
#################################################################################################

I can make empty files_ in a folder_ with the touch_ program

* I add an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_parent

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: python
      :emphasize-lines: 1

      New-Item a_file_in_parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I use ls_ to see what is in the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_parent  child  sibling_of_child

* I `change directory` to one of the children of ``parent``

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

    .  ..  a_file_in_child

* I `change directory`_ to the parent of ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I `change directory` to the other child of ``parent``

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

    .  ..  a_file_in_sibling_of_child

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

* I can go from ``child_of_child`` to ``parent`` in 1 step by using ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

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

    .../parent/sibling_of_child/child_of_sibling_child

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

* I go back to ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

* I add an empty file_

  .. code-block:: shell

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

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
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

* I can add an empty file_ in 1 step in any directory_ as long as I know its path and its relation to where I am and as long as I have permission to write to the folder_. I add an empty file_ in ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch child/child_of_child/a_file_in_child_of_child

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use `New-Item`_ instead of ``touch``

    .. code-block:: python
      :emphasize-lines: 1

      New-Item child/child_of_child/a_file_in_child_of_child

  the terminal_ goes back to the command line

* I add another empty file_ in ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch sibling_of_child/child_of_sibling_of_child/a_file_in_child_of_sibling_of_child

  the terminal_ goes back to the command line

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 8, 13

    .
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_child_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 9 files




  I use touch_ to make another empty file

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_grandchild_of_parent

  the terminal_ goes back to the command line. I use tree_ to see what I have now

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell

    .
    ├── a_file_in_child_of_child
    └── a_grandchild_of_parent

    1 directory, 2 files

* I try to go back to the ``parent`` directory_ I started from

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: parent

  I try to go to a directory_ in the ``parent`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: child

  I try to go to another directory_ in the ``parent`` folder

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: sibling_of_child

  I try to go to a folder_ that does not exist

  .. code-block:: shell
    :emphasize-lines: 1

    cd does_not_exist

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: does_not_exist

  I list all the files_ and folders_ where I am at the moment

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child_of_child  a_grandchild_of_parent

  I cannot go to those directories_ the way I tried, because they are not children of this directory_. I use pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

  - ``child`` is the parent of ``child_of_child``
  - ``parent`` is the parent of ``child``
  - ``parent`` is the grand parent of ``child_of_child``

* I go to the parent of the directory_ I am in with ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  ``..`` is used for the parent of the directory_ I am in. the terminal_ shows

  .. code-block:: shell

    /workspaces/…/pumping_python/parent/child

  I use pwd_ to see where I am at the moment

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../parent/child

  I use ls_ to list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  child_of_child

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    └── child_of_child
        ├── a_file_in_child_of_child
        └── a_grandchild_of_parent

    2 directories, 2 files

* I go up another level

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am back at the first directory_ I made - ``parent``

* I can go to ``child_of_child`` in one step instead of 2 by using its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

  I can also go to ``parent`` from ``child_of_child`` in one step instead of 2 by using ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am back at the first directory_ I made - ``parent``

  .. NOTE:: Since ``..`` is for the parent of a directory_, ``../..`` is for the parent of a parent, that is a grandparent. I can use as many ``..``'s I need for each parent, for example ``../../../..`` would be the great great grand parent

* I type pwd_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_parent  child  sibling_of_child

  I look at the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell

    .
    ├── a_file_in_parent
    ├── child
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child

    4 directories, 3 files

* I `change directory`_ to the other child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I list the contents of the directory_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    .

    0 directories, 0 files

  I `make a directory`_

  .. code-block:: shell

    mkdir child_of_sibling_of_child

  the terminal_ goes back to the command line. I `change directory`_ to the folder_ I just made

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_child_of_sibling_of_child

  the terminal_ goes back to the command line. I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch another_grandchild_of_parent

  the terminal_ goes back to the command line. I list the contents of the folder_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_child_of_sibling_of_child  another_grandchild_of_parent

  I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell

    .
    ├── a_file_in_child_of_sibling_of_child
    └── another_grandchild_of_parent

    1 directory, 2 files

* I try to go back to the ``parent`` directory_ I started from

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: parent

  I try to go to a directory_ in the ``parent`` folder_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: child

  I try to go to another directory_ in the ``parent`` folder

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: sibling_of_child

  I try to go to another folder_ in the ``child`` directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: child_of_child

  I try to go to a folder_ that does not exist

  .. code-block:: shell
    :emphasize-lines: 1

    cd does_not_exist

  the terminal_ shows

  .. code-block:: shell

    cd: no such file or directory: does_not_exist

  I cannot go to a directory_ that is not a child of this directory_ this way. I use pwd_ to show where I am

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

  - ``sibling_of_child`` is the parent of ``child_of_sibling_of_child``
  - ``parent`` is the parent of ``sibling_of_child``
  - ``parent`` is the grand parent of ``child_of_sibling_of_child``

* I go to the parent of the directory_ I am in

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I use pwd_ to show where I am at the moment

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I use ls_ to show the files_ and folders_ in this directory_

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  the terminal_ shows

  .. code-block:: shell

    .  ..  child_of_sibling_of_child

  I use tree_ to show the structure

  .. code-block:: shell
    :emphasize-lines: 1

    .
    └── child_of_sibling_of_child
        ├── a_file_in_child_of_sibling_of_child
        └── another_grandchild_of_parent

    2 directories, 2 files

* I go up another level

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am back at the first directory_ I made - ``parent``

* I can go to ``child_of_sibling_of_child`` in one step instead of 2 by using its parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

  I can also go to ``parent`` from ``child_of_sibling_of_child`` in one step instead of 2 by using ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I am back at the first directory_ I made - ``parent``

* I type pwd_

  .. code-block:: shell
    :emphasize-lines: 1

    pwd

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I list the contents

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``ls -Force`` instead of ``ls -a``

    .. code-block:: python
      :emphasize-lines: 1

      ls -Force

    the terminal will not show ``.`` and ``..``

  the terminal_ shows

  .. code-block:: shell

    .  ..  a_file_in_parent  child  sibling_of_child

  I use tree_ to see the structure

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
      :emphasize-lines: 1

      tree /F

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 4-6, 8-10

    .
    ├── a_file_in_parent
    ├── child
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 5 files

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_grandparent_of_child_of_child

  the terminal_ goes back to the command line

* I make another empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch aka_grandparent_of_child_of_sibling_of_child

  the terminal_ goes back to the command line

* I use tree_

  .. code-block:: shell
    :emphasize-lines: 1

    tree

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 3-4

    .
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_sibling_of_child
    ├── child
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 7 files

* I `change directory`_ to a child of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ goes back to the command line

* I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_child

  the terminal_ goes back to the command line

* I want to `change directory`_ to ``sibling_of_child`` in one step. I can use the path of a folder_ to get to it, once I know its relation to where I am. I use cd_ with ``..``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I make an empty file_

  .. code-block:: shell
    :emphasize-lines: 1

    touch a_file_in_sibling_of_child

  the terminal_ goes back to the command line

* I `change directory`_  to the parent of ``parent`` in one step

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../..

  the terminal_ shows

  .. code-block:: shell

    ../pumping_python

  I show the directory_ structure of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    tree parent

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``tree /F`` instead of ``tree``

    .. code-block:: python
      :emphasize-lines: 1

      tree /F parent

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 6, 11

    parent
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       └── a_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            └── another_grandchild_of_parent

    5 directories, 9 files

* I can make a file_ in children directories_ by using the path to go through the parents. I make an empty file_ in ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch parent/child/aunt_or_uncle_of_another_grandchild_of_parent

  the terminal_ goes back to the command line

* I make another empty file_, this time in ``sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch parent/sibling_of_child/aunt_or_uncle_of_a_grandchild_of_parent

  the terminal_ goes back to the command line

* I show the structure of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    tree parent

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 7, 13

    parent
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_sibling_of_child
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

* I make an empty file in ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    touch parent/child/child_of_child/cousin_of_another_grandchild_of_parent

  the terminal_ goes back to the command line

* I make an empty file_ in ``child_of_sibling_of_child``

  .. code-block:: shell

    touch parent/sibling_of_child/child_of_sibling_of_child/cousin_of_a_grandchild_of_parent

  the terminal_ goes back to the command line

* I show the directory_ structure of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    tree parent

  the terminal_ shows

  .. code-block:: shell
    :emphasize-lines: 11, 18

    parent
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   ├── aunt_or_uncle_of_another_grandchild_of_parent
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       ├── a_grandchild_of_parent
    │       └── cousin_of_another_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        ├── aunt_or_uncle_of_a_grandchild_of_parent
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            ├── another_grandchild_of_parent
            └── cousin_of_a_grandchild_of_parent

    5 directories, 13 files

* I can "visit" any folder_ as long as I know its path/address and how it is "related" to where I am. I want to go see ``child_of_sibling_of_child``. I start with ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  then I `change directory`_ to the child directory_

  .. code-block:: shell
    :emphasize-lines: 1

    cd sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I `change directory`_ one more time

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

  I cannot get to a child without its parent. I go back to the parent of ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../..

  the terminal_ shows

  .. code-block::

    .../pumping_python

  I can go to ``child_of_sibling_of_child`` with one command instead of 3 and still go through the parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent/sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

  knowing where I am in relation to where I want to go, helps me get there

* I want to go see ``child_of_child``, first I go to the parent of ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../parent/sibling_of_child

  I go to ``parent``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent

  I go to ``child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child

  I go to ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

  I go back to the parent of ``parent``, the great grandparent of ``child_of_child``

  .. code-block:: shell

    cd ../../..

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python

  I go back to ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd parent/sibling_of_child/child_of_sibling_of_child

  the terminal shows

  .. code-block:: shell

    .../parent/sibling_of_child/child_of_sibling_of_child

  I can go to ``child_of_child`` with one command instead of 3 and still go through each parent

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

  .. NOTE:: ``child_of_child`` and ``child_of_sibling_of_child`` have the same grandparent, since ``..`` is for the parent ``../..`` is for the grandparent

* I can do the same thing with tree_. I want to see the structure of ``sibling_of_child`` from inside ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    ../../sibling_of_child
    ├── a_file_in_sibling_of_child
    ├── aunt_or_uncle_of_a_grandchild_of_parent
    └── child_of_sibling_of_child
        ├── a_file_in_child_of_sibling_of_child
        ├── another_grandchild_of_parent
        └── cousin_of_a_grandchild_of_parent

    2 directories, 5 files

  I try the same thing with ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    ../../sibling_of_child/child_of_sibling_of_child
    ├── a_file_in_child_of_sibling_of_child
    ├── another_grandchild_of_parent
    └── cousin_of_a_grandchild_of_parent

    1 directory, 3 files

* I `change directory`_ to ``child_of_sibling_of_child`` from inside ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .../pumping_python/parent/sibling_of_child

  I want to see the structure of ``child`` from inside ``sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../child

  the terminal_ shows

  .. code-block:: shell

    ../../child
    ├── a_file_in_child
    ├── aunt_or_uncle_of_another_grandchild_of_parent
    └── child_of_child
        ├── a_file_in_child_of_child
        ├── a_grandchild_of_parent
        └── cousin_of_another_grandchild_of_parent

    2 directories, 5 files

  I try the same thing with ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    ../../child/child_of_child
    ├── a_file_in_child_of_child
    ├── a_grandchild_of_parent
    └── cousin_of_another_grandchild_of_parent

    1 directory, 3 files

* I can do the same thing with ls_. I list the contents of ``child_of_child`` from inside ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../child/child_of_child

  .. ADMONITION:: on Windows without `Windows Subsystem Linux`_ use ``ls -Force`` instead of ``ls -a``

    .. code-block:: python
      :emphasize-lines: 1

      ls -Force ../../child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .   a_file_in_child_of_child  cousin_of_another_grandchild_of_parent
    ..  a_grandchild_of_parent

  I list the contents of ``child`` from inside ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../child

  the terminal_ shows

  .. code-block:: shell

    .   a_file_in_child                                child_of_child
    ..  aunt_or_uncle_of_another_grandchild_of_parent

  I `change directory`_ to ``child_of_child`` from ``child_of_sibling_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    cd ../../child/child_of_child

  the terminal_ shows

  .. code-block:: shell

    .../parent/child/child_of_child

  I list the contents of ``child_of_sibling_of_child`` from inside ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../sibling_of_child/child_of_sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .   a_file_in_child_of_sibling_of_child  cousin_of_a_grandchild_of_parent
    ..  another_grandchild_of_pare

  I list the contents of ``sibling_of_child`` from inside ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    ls -a ../../sibling_of_child

  the terminal_ shows

  .. code-block:: shell

    .   a_file_in_sibling_of_child               child_of_sibling_of_child
    ..  aunt_or_uncle_of_a_grandchild_of_parent

* I look at the structure of ``parent`` again, this time from inside ``child_of_child``

  .. code-block:: shell
    :emphasize-lines: 1

    tree ../../../parent

  the terminal_ shows

  .. code-block:: shell

    ../../../parent
    ├── a_file_in_parent
    ├── aka_grandparent_of_child_of_child
    ├── aka_grandparent_of_sibling_of_child
    ├── child
    │   ├── a_file_in_child
    │   ├── aunt_or_uncle_of_another_grandchild_of_parent
    │   └── child_of_child
    │       ├── a_file_in_child_of_child
    │       ├── a_grandchild_of_parent
    │       └── cousin_of_another_grandchild_of_parent
    └── sibling_of_child
        ├── a_file_in_sibling_of_child
        ├── aunt_or_uncle_of_a_grandchild_of_parent
        └── child_of_sibling_of_child
            ├── a_file_in_child_of_sibling_of_child
            ├── another_grandchild_of_parent
            └── cousin_of_a_grandchild_of_parent

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

    .../pumping_python

* I remove ``parent`` and all its descendants

  .. code-block:: shell
    :emphasize-lines: 1

    rm -rf parent

  the terminal_ goes back to the command line

  - rm_ is used to remove files_ and folders_
  - ``-r`` means remove child directories_ and what is in them recursively, it goes through each child directory_ and removes everything include its children
  - ``-f`` means "force", do not me any questions, just remove the file_ or folder_

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

I ran the following commands to practice `folder/directory`_ structure

* mkdir_
* cd_
* ls_
* tree_
* touch_
* rm_

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">Click Here to leave a 5 star review on TrustPilot, if you found this helpful</a>
  </div>
  <!-- End TrustBox widget -->
