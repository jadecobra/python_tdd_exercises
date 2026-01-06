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
cd jane/baby
touch a_grandchild_of_doe
ls -a
cd ../..
cd john
cd lil
cd ../..
cd lil
cd john/lil
touch another_grandchild_of_doe
ls -a
cd ../..
touch aka_grandparent_of_baby
touch aka_grandparent_of_baby
tree
touch child/aunt_or_uncle_of_lil
touch john/aunt_or_uncle_of_baby
tree
touch child/baby/a_file_in_baby
touch john/lil/a_file_in_lil
cd ..
tree parent
pwd
ls -a parent
ls -a doe/jane
ls -a doe/jane/baby
ls -a doe/john
ls -a doe/john/lil
cd doe/jane/baby
ls -a ../../john/lil
touch ../../john/lil/cousin_of_baby
tree ../../john/lil
cd ../../john/lil
ls -a ../../jane/baby
touch ../../jane/baby/cousin_of_mary
tree ../../jane/baby
tree ../../../parent
cd ../../..
pwd
rm -rf parent
cd parent