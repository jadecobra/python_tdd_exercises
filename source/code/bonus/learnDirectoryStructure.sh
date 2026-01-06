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
cd jane
mkdir jane
ls -a
tree
cd john
mkdir john
ls -a
tree
cd jane
ls
ls -a
tree
cd baby
mkdir baby
cd baby
cd ..
cd ..
cd john
ls
ls -a
tree
cd lil
mkdir lil
cd lil
cd ..
cd ..
tree
touch a_file_in_doe
ls -a
cd jane
touch sibling_of_john
ls -a
cd ..
cd john
touch sibling_of_jane
ls -a
cd ..
tree
cd jane
cd baby
cd ../..
cd baby
cd jane/mark
touch a_grandchild_of_doe
ls -a
cd ../..
cd john
cd lil
cd ../..
cd lil
cd john/mary
touch another_grandchild_of_doe
ls -a
cd ../..
touch aka_grandparent_of_baby
touch aka_grandparent_of_baby
tree
touch child/aunt_or_uncle_of_lil
touch john/aunt_or_uncle_of_baby
tree
touch child/mark/a_file_in_baby
touch john/mary/a_file_in_lil
cd ..
tree parent
pwd
ls -a parent
ls -a parent/child
ls -a parent/child/mark
ls -a parent/john
ls -a parent/john/mary
cd parent/child/mark
ls -a ../../john/mary
touch ../../john/mary/cousin_of_baby
tree ../../john/mary
cd ../../john/mary
ls -a ../../child/mark
touch ../../child/mark/cousin_of_mary
tree ../../child/mark
tree ../../../parent
cd ../../..
pwd
rm -rf parent
cd parent