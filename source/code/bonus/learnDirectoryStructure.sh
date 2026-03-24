#!bin/bash
# Learn Directory Structure
# Make sure you are in the pumping_python directory
cd doe
mkdir doe
cd doe
pwd
ls
cd .
cd ..
cd doe
tree

cd jane
mkdir jane
ls
tree
cd jane
cd ..

cd john
mkdir john
ls
tree
cd john
cd ..

cd .a_hidden_folder_in_doe
mkdir .a_hidden_folder_in_doe
ls
ls -a
tree
tree -a
cd .a_hidden_folder_in_doe
cd ..

cd jane
ls
ls -a
tree
cd baby
mkdir baby
cd baby
cd ..
cd .a_hidden_folder_in_jane
mkdir .a_hidden_folder_in_jane
cd .a_hidden_folder_in_jane
cd ..
tree
tree -a
cd ..

cd john
ls
ls -a
tree
cd lil
mkdir lil
cd lil
cd ..
cd .a_hidden_folder_in_john
mkdir .a_hidden_folder_in_john
cd .a_hidden_folder_in_john
cd ..
cd ..
tree
tree -a
touch an_empty_file_in_doe
touch .a_hidden_file_in_doe
ls
ls -a
cd jane
touch an_empty_file_in_jane
touch .a_hidden_file_in_jane
ls -a
cd ..
cd john
touch an_empty_file_in_john
touch .a_hidden_file_in_john
ls -a
cd ..
tree
tree -a
cd ..
tree
tree -a

touch an_empty_file_in_doe
touch .a_hidden_file_in_doe
ls
ls -a

cd jane
touch an_empty_file_in_jane
touch .a_hidden_file_in_jane
ls -a
cd ..

cd john
touch an_empty_file_in_john
touch .a_hidden_file_in_john
ls -a
cd ..
tree
tree -a

cd jane
cd baby
touch an_empty_file_in_baby
touch .a_hidden_file_in_baby
mkdir .a_hidden_folder_in_baby
ls -a
cd ..
cd ..

cd john
cd lil
touch an_empty_file_in_lil
touch .a_hidden_file_in_lil
mkdir .a_hidden_folder_in_lil
ls -a
cd ..
cd ..
tree
tree -a

cd baby
cd jane/baby
cd ../..

cd lil
cd john/lil
cd ../..

touch jane/a_child_of_doe
touch jane/baby/a_grandchild_of_doe
touch john/a_child_of_doe
touch john/lil/a_grandchild_of_doe
tree

cd jane
touch baby/aka_child_of_jane
touch ../aka_parent_of_jane
touch ../john/aka_sibling_of_jane
touch ../john/lil/aka_child_of_johns_sibling
cd ..
tree

cd john
touch lil/aka_child_of_john
touch ../aka_parent_of_john
touch ../jane/aka_sibling_of_john
touch ../jane/baby/aka_child_of_janes_sibling
cd ..
tree

cd jane/baby
mv aka_child_of_janes_sibling aka_child_of_johns_sibling
cd ../..
cd john/lil
mv aka_child_of_johns_sibling aka_child_of_janes_sibling
cd ../..
tree

cd jane/baby
touch ../aka_parent_of_baby
touch ../../aka_grandparent_of_baby
touch ../../john/aka_aunt_of_baby
touch ../../john/lil/aka_cousin_of_baby
tree ../..

cd ../../john/lil
touch ../aka_parent_of_lil
touch ../../aka_grandparent_of_lil
touch ../../jane/aka_uncle_of_lil
touch ../../jane/baby/aka_cousin_of_lil
tree ../../../doe
mv ../../jane/aka_uncle_of_lil ../../jane/aka_aunt_of_lil
mv ../aka_aunt_of_baby ../aka_uncle_of_baby
cd ../..
tree

cd ..
ls -a doe
ls -a doe/jane
ls -a doe/jane/baby

cd doe/jane/baby
ls -a ../../john
ls -a ../../john/lil
tree ../../john/lil
tree ../../john

cd ../../john/lil
ls -a ../../jane/baby
tree ../../jane/baby
tree ../../jane

cd ../../..
tree -a