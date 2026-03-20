#!bin/bash
# Learn Directory Structure
tree
pwd
cd doe
mkdir doe
cd doe
pwd
ls
ls --all
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
touch an_empty_file_in_doe
ls -a
cd jane
touch an_empty_file_in_jane
ls -a
cd ..
cd john
touch an_empty_file_in_john
ls -a
cd ..
tree
cd jane
cd baby
touch an_empty_file_in_baby
ls -a
cd ..
cd ..
cd john
cd lil
touch an_empty_file_in_lil
ls -a
cd ..
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
touch aka_child_of_janes_sibling
ls -a
cd ../..
cd john/lil
touch aka_child_of_john
touch aka_child_of_johns_sibling
ls -a
cd ../..
touch aka_parent_of_jane
touch aka_parent_of_john
tree
touch jane/a_child_of_doe
touch jane/aka_sibling_of_john
touch john/another_child_of_doe
touch john/aka_sibling_of_jane
touch jane/baby/a_grandchild_of_doe
touch john/lil/another_grandchild_of_doe
cd ..
tree doe
pwd
ls -a
ls -a doe
ls -a doe/jane
ls -a doe/jane/baby
ls -a doe/john
ls -a doe/john/lil
cd doe/jane/baby
ls -a ../../john/lil
touch ../../john/lil/aka_cousin_of_baby
mv aka_child_of_janes_sibling ../../john/lil/aka_child_of_janes_sibling
tree ../../john/lil
touch ../../aka_grandparent_of_baby
touch ../../jane/aka_uncle_of_baby
cd ../../john/lil
ls -a ../../jane/baby
touch ../../jane/baby/aka_cousin_of_lil
mv aka_child_of_janes_sibling ../../jane/baby/aka_child_of_janes_sibling
tree ../../jane/baby
touch ../../aka_grandparent_of_lil
touch ../../john/aka_aunt_of_lil
tree ../../../doe
cd ../../..
mv doe/jane/aka_uncle_of_baby doe/john/aka_uncle_of_baby
mv doe/john/aka_aunt_of_lil doe/jane/aka_aunt_of_lil
tree doe
rm doe
rm --recursive doe
cd doe