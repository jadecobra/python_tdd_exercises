:orphan:

.. include:: ../links.rst

.. _Excel Spreadsheet: https://grokipedia.com/page/Microsoft_Excel
.. _Word Document: https://grokipedia.com/page/Microsoft_Word
.. _make directories: mkdir_
.. _change directories: cd_
.. _Get-ChildItem: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.6


#################################################################################
BONUS: learn git
#################################################################################

This exercise shows how to use git_ which is a program_ that keeps track of changes I make in a codebase.

----

*************************************************************************************
preview
*************************************************************************************



----

*********************************************************************************
requirements
*********************************************************************************

* I type this in a terminal_ to make sure git_ is installed

  .. code-block:: python
    :emphasize-lines: 1

    git

* If it is not installed on the computer, the terminal_ is my friend, and shows

  .. tab-set::
    :sync-group: os

    .. tab-item:: WSL/Linux/Mac
      :sync: unix

      .. code-block:: python

        git: command not found

    .. tab-item:: no WSL
      :sync: no_wsl

      .. code-block:: python

        git: The term 'git' is not recognized as a name of a cmdlet,
        function, script file, or executable program.
        Check the spelling of the name, or if a path was included,
        verify that the path is correct and try again.

  see :ref:`how to install git` to install git_

* If it is installed on the computer, the terminal_ is my friend, and shows the manual for git_ so I know how to use it

----

********************************************************************************************
how to install git
********************************************************************************************

* :ref:`how to install git on Linux/Windows Subsystem for Linux`
* :ref:`how to install git on Windows without Windows Subsystem for Linux`
* :ref:`how to install git on Mac OS`

----

---------------------------------------------------------------------------------
how to install git on Linux/Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. attention:: Do this only if you are using Linux_ or `Windows Subsystem for Linux`_ and git_ is not installed.

  :ref:`Click here if you have MacOS<how to install tree on Mac OS>`

.. code-block:: python
  :emphasize-lines: 1

  sudo apt update

I always do a full upgrade (you do not have to)

.. code-block:: python
  :emphasize-lines: 1

  sudo apt full-upgrade --yes

type this in the terminal_ to install git_

.. code-block:: python
  :emphasize-lines: 1

  sudo apt install git

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

---------------------------------------------------------------------------------
how to install git on Windows without Windows Subsystem for Linux
---------------------------------------------------------------------------------

----

.. attention:: Do this only if you are using Windows_ and could not install `Windows Subsystem for Linux`_

  :ref:`Click here if you have MacOS<how to install tree on Mac OS>`

`download and install git`_

Click on the tab that says ``no WSL`` to see the commands or results if you have Windows_ without `Windows Subsystem for Linux`_

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

---------------------------------------------------------------------------------
how to install git on Mac OS
---------------------------------------------------------------------------------

----

.. attention:: No need to do anything. git_ comes with MacOS_.

  If you have Windows_

  * :ref:`click here for how to install git on Linux/Windows SubSystem for Linux<how to install git on Linux/Windows Subsystem for Linux>` or
  * :ref:`click here for how to install git on Windows without Windows SubSystem Linux<how to install git on Windows without Windows Subsystem for Linux>`

:ref:`Click here to see what directory I am in<how to see what directory I am in>`

----

********************************************************************************************
how to see what directory I am in
********************************************************************************************






##########################################################################
#                             How to use Git                             #
##########################################################################

git help
git help --all
q
git help --guides
git help attributes
q
git help everyday
q
git help glossary
q
git help ignore
q
git help modules
q
git help revisions
q
git help tutorial
q
git help workflows
q
git help init
q
git init --help
q
git help add
q
git add --help
q
git help commit
q
git commit --help
q
git help status
q
git status --help
clear

PROJECTNAME=Name of Project

###############################################################
#                  Create A New Repository                    #
# go to https://github.com > Start A Project > $PROJECTNAME   #
# Click Create repository                                     #
###############################################################

mkdir $PROJECTNAME && cd $PROJECTNAME
echo "# $PROJECTNAME" >> README.md

git init                # mkdir .git and add important files
git status
git diff
git diff --cached
git diff HEAD
git commit --all --message "I cannot commit since I have not told git to track anything yet"
git log
git log --oneline
git log --merges
git log --graph

git add README.md
git commit --all --message "made my first commit"
ls
cd .git
tree
cat description
nano description
$PROJECTNAME; a Git Repository
# hit ctrl+x on the keyboard
Y
cat description
cd ..
clear

git remote add origin git@github.com:$GITHUB_USERNAME/$PROJECTNAME.git

git remote --verbose
git push --set-upstream origin main
clear

###############################################################
#          Keeping Files And Directories Private              #
###############################################################

cat .gitignore
ls -a
ls
mkdir DirectoryNotToBeShared
ls
echo "DirectoryNotToBeShared/" >> .gitignore
cat .gitignore
ls -a
touch FileNotToBeShared.extension
echo "FileNotToBeShared.extension" >> .gitignore
cat .gitignore
ls
ls -a
git status
git add .gitignore
git diff
git diff --cached
git diff HEAD
git commit --all --message "created files and directories for git to not track"
git log
git log --oneline
git log --merges
git log --graph
git status
git add DirectoryNotToBeShared/
git add FileNotToBeShared.extension
git status
git push
git status
git log
git log --oneline
git log --merges
git log --graph
clear

# Managing Files and Directories
touch File{1,2,3,N}InThisDirectory.extension
ls
tree
mkdir Directory{1,2,3,N}
ls

##########################################################################################################
#                                                                                                        #
#   Are you on using MacOS - install brew with this command                                              #
#      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"   #
#   install tree with this command                                                                       #
#      brew install tree                                                                                 #
#                                                                                                        #
#   Are you on a Linux Machine or using WSL?                                                             #
#      sudo apt install tree                                                                             #
#                                                                                                        #
##########################################################################################################

tree
touch Directory{1,2,3,N}/File{1,2,3,N}InThisDirectory.extension
ls
tree
touch Directory2/python_file.py
touch Directory2/java_file.java
touch Directory2/java_file.war
touch Directory3/html_file.html
touch Directory3/javscriptFile.js
touch DirectoryN/compressed_file.zip
touch DirectoryN/compressed_file.bz2
touch DirectoryN/compressed_file.xz
touch DirectoryN/tape_archive_file.tar
tree
cd Directory3
pwd
mkdir ChildOfDirectory3
cd ChildOfDirectory3
mkdir ChildOfChildOfDirectory3
cd ChildOfChildOfDirectory3
pwd
touch textfile{1,2,3,N}.txt
ls
tree
cd ../..
pwd
ls
tree
cd ..
ls
tree
clear

###############################################################
#    How to add Files and Directories for Git to Track        #
###############################################################

tree
git status
nano File1InThisDirectory.extension
I am modifying File1InThisDirectory.extension in $PROJECTNAME
# hit ctrl+x on the keyboard
y
git add File1InThisDirectory.extension
git status
git commit --all --message "I modified File1InThisDirectory.extension in $PROJECTNAME"
git push
git status

nano Directory1/FileInThisDirectory.extension
I am modifying File1InThisDirectory.extension in Directory1
# hit ctrl+x on the keyboard
y
git add Directory1/File1InThisDirectory.extension
git addDirectory1/FileNInThisDirectory.extension
git commit --all --message "I modified File1InThisDirectory.extension in Directory1"
git status
git push
git status

git add Directory2/File2InThisDirectory.extension
nano Directory2/File2InThisDirectory.extension
What happens if I modify a file after adding it to tracking?
# hit ctrl+x on the keyboard
y
git commit --all --message "I modified File2InThisDirectory.extension in Directory2"
git status
git add Directory2/File2InThisDirectory.extension
git status
git commit -am "I Modified File2InThisDirectory.extension in Directory2"
git status
git push
git status

nano Directory3/File3InThisDirectory.extension
I Always add after modifying a file and commit
# hit ctrl+x on the keyboard
y
git add Directory3/File3InThisDirectory.extension
git commit --all --message "I modified File3InThisDirectory.extension in Directory3"
git push
git status
git add Directory3/

git status
nano DirectoryN/FileNInThisDirectory.extension
I will ALWAYS BE COMMITTING
# hit ctrl+x on the keyboard
y
git add DirectoryN/FileNInThisDirectory.extension
git commit --all --message "I modified FileNInThisDirectory.extension in DirectoryN"
git push

git status
git add .
git status
tree
git diff
git diff --cached
q
git diff HEAD
q
git commit -am "I added new Ffives to be tracked by git"
git log
q
git log --oneline
git log --graph
q
git commit -amend --message "I Added new Files and Directories in $PROJECTNAME for git to track"
git log
q
git log --oneline
git log --merges
git log --graph
q
git push
git log --oneline
git log --merges
git log --graph
git diff
git status
clear

###############################################################
#                           Branching                         #
###############################################################

git status
git branch
git branch --all
git branch --verbose
git branch -vv
git branch a_new_branch
git branch
git branch --delete a_new_branch
git branch
git branch an_old_branch_name
git branch --all
git branch --merge an_old_branch_name a_new_branch_name
git branch --all
git branch --verbose
git branch -vv

git branch a_branch
git branch --all
git checkout a_branch
git branch --all
git status
git checkout main
git status
git branch --all
git checkout a_new_branch_name
git branch --all
git status
git checkout -b a_new_branch
git branch --all
git status
git checkout main
git checkout -b a_dead_branch
git branch --all
git status
git checkout main
git branch --delete --force a_dead_branch
git branch --all
git status
ls
tree

git branch --all
git branch branch1
git branch branch2
git branch branch3
git branch branchN
git branch --all

git push origin a_branch
git branch --all
git push origin a_new_branch
git branch --all
git push origin branch1
git branch --all
git push origin branch2
git branch --all
git push origin branch3
git branch --all
git push origin branchN
git branch --all

###############################################################
#                       Merging Changes                       #
###############################################################

git checkout a_branch
touch file_from_a_branch.extension
mkdir new_directory_from_a_branch
touch new_directory_from_a_branch/File{1,2,3,N}InThisDirectory.extension
git status
git add .
git commit --all --message "I added a new File and Directory in a_branch"
git diff origin/a_branch
git push origin a_branch
git diff
git diff main
git checkout main
git diff origin/main
git diff a_branch
git merge a_branch
git diff
git diff a_branch
git diff origin/main
git status
git push origin main
git status

git checkout -b new_feature
git branch --all
git diff main
git merge main
nano FileInThisDirectory.extension
I had a Genius Idea and tested it in new_feature
# hit ctrl+x on the keyboard
y
git status
git add .
git commit -am "I had a Genius Idea and tested it in new_feature"
git diff main
git diff remotes/origin/new_feature
git push origin new_feature
git checkout main
git merge --no-ff new_feature
I Had a Genius idea, tested it in new_feature and merged it into main
# save and exit
git diff
git diff new_feature
git diff remotes/origin/main
git status
git push origin main
git log
git log --oneline
git log --merges
git log graph
git branch --delete --force new_feature
clear

###############################################################
#                               Tagging                       #
###############################################################

git tag
git tag --annotate v0.1 "Beta Test version 1"
git tag
git tag --annotate v0.1 -m "Beta Test version 1"
git tag
git tag --annotate v1.1 -m "Version 1.0 revision 1"
git tag
git tag v2.0 --message "Version 2.0"
git tag
git tag vN.M --message "Version N revision M"
git tag
git tag any_tag --message "Description/Comment for the Tag"
git status
clear

git show
git show v0.1
git show v1.1
git show v2.0
git show vN.M
git show any_tag
git show non_existent_tag
clear

git push origin v0.1
git push origin vN.M
git push origin --tags

git log
git log --oneline
git log --merges
git log --graph

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

:ref:`Do you want to see all the CODE I typed in this chapter?<learnGit.sh>`


----

*****************************************************************************************
what is next?
*****************************************************************************************

I know

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

:ref:`Click Here to see me make a Python Test Driven Development Environment<how to make a Python test driven development environment>`

----

*********************************************************************************
rate pumping python
*********************************************************************************

If this has been a 7 star experience for you, please `CLICK HERE to leave a 5 star review of pumping python`_. It helps other people get into the book too.

----

.. raw:: html

  <!-- TrustBox widget - Review Collector -->
  <div class="trustpilot-widget" data-locale="en-US" data-template-id="56278e9abfbbba0bdcd568bc" data-businessunit-id="69141d0f0902d6a2a1b2436b" data-style-height="52px" data-style-width="100%" data-token="5db17dde-bcdc-460f-81f3-d8ab689b6e4d">
    <a href="https://www.trustpilot.com/review/pumpingpython.com" target="_blank" rel="noopener">CLICK HERE to leave a 5 star review of pumping python, if this has been a 7 star experience for you</a>
  </div>
  <!-- End TrustBox widget -->