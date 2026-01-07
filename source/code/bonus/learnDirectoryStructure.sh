#!bin/bash
# Learn Directory Structure
cd doe
mkdir doe
cd doe
pwd
ls
ls --all
ls -a
cd .
cd ..
cd doe
tree
cd jane
mkdir jane
ls -a
tree
cd john
mkdir john
tree
cd jane
ls
ls -a
tree
cd baby
mkdir baby
cd baby
cd ..
cd john
ls
ls -a
tree
cd lil
mkdir lil
cd lil
cd ..
tree
touch a_file_in_doe
ls -a
cd jane
touch a_file_in_jane
ls -a
cd ..
cd john
touch a_file_in_john
ls -a
cd ..
tree
cd jane
cd baby
touch a_file_in_baby
ls -a
cd ..
cd john
cd lil
touch a_file_in_lil
ls -a
cd ..
tree
cd baby
cd jane/baby
cd ../..
cd lil
cd john/lil
cd ../..
cd jane/baby
touch aka_child_of_jane
ls -a
cd ../..
cd john/lil
touch aka_child_of_john
ls -a
cd ../..
touch aka_parent_of_jane aka_parent_of_john
tree
touch jane/a_child_of_doe jane/aka_sibling_of_john
touch john/another_child_of_doe john/aka_sibling_of_jane
touch jane/baby/a_grandchild_of_doe
touch john/lil/another_grandchild_of_doe
cd ..
tree doe
pwd
ls -a doe
ls -a doe/jane
ls -a doe/jane/baby
ls -a doe/john
ls -a doe/john/lil
cd doe/jane/baby
ls -a ../../john/lil
touch ../../john/lil/aka_cousin_of_baby
tree ../../john/lil
touch ../../aka_grandparent_of_baby ../../john/aka_uncle_of_baby
cd ../../john/lil
ls -a ../../jane/baby
touch ../../jane/baby/aka_cousin_of_lil
tree ../../jane/baby
touch ../../aka_grandparent_of_lil ../../jane/aka_aunt_of_lil
tree ../../../doe
cd ../../..
pwd
rm -rf doe
cd doe