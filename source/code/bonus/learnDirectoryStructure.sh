#!bin/bash
# Learn Directory Structure
cd parent
mkdir parent
cd parent
pwd
ls
ls --all
ls -a
cd .
cd ..
cd parent
tree
cd child
mkdir child
ls -a
tree
cd sibling_of_child
mkdir sibling_of_child
ls -a
tree
cd child
ls
ls -a
tree
cd child_of_child
mkdir child_of_child
cd child_of_child
cd ..
cd ..
cd sibling_of_child
ls
ls -a
tree
cd child_of_sibling_of_child
mkdir child_of_sibling_of_child
cd child_of_sibling_of_child
cd ..
cd ..
tree
touch a_file_in_parent
ls -a
cd child
touch a_file_in_child
ls -a
cd ..
cd sibling_of_child
touch a_file_in_sibling_of_child
ls -a
cd ..
tree
cd child
cd child_of_child
cd ../..
cd child_of_child
cd child/child_of_child
touch a_grandchild_of_parent
ls -a
cd ../..
cd sibling_of_child
cd child_of_sibling_of_child
cd ../..
cd child_of_sibling_of_child
cd sibling_of_child/child_of_sibling_of_child
touch another_grandchild_of_parent
ls -a
cd ../..
touch aka_grandparent_of_child_of_child
touch aka_grandparent_of_child_of_sibling_of_child
tree
touch child/aunt_or_uncle_of_another_grandchild_of_parent
touch sibling_of_child/aunt_or_uncle_of_a_grandchild_of_parent
tree
touch child/child_of_child/a_file_in_child_of_child
touch sibling_of_child/child_of_sibling_of_child/a_file_in_child_of_sibling_of_child
cd ..
tree parent
pwd
ls parent -a
ls -a parent/child
ls -a parent/child/child_of_child
ls -a parent/sibling_of_child
ls -a parent/sibling_of_child/child_of_sibling_of_child
cd parent/child/child_of_child
ls -a ../../sibling_of_child/child_of_sibling_of_child
touch ../../sibling_of_child/child_of_sibling_of_child/cousin_of_child_of_child
tree ../../sibling_of_child/child_of_sibling_of_child
cd ../../sibling_of_child/child_of_sibling_of_child
ls -a ../../child/child_of_child
touch ../../child/child_of_child/cousin_of_child_of_sibling_of_child
tree ../../child/child_of_child
tree ../../../parent
cd ../../..
pwd
rm -rf parent
cd parent