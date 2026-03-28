#!/bin/bash
# Learn Directory Relationships
# Make sure you are in the `pumping_python` directory
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

cd jane_doe
mkdir jane_doe
ls
tree
cd jane_doe
cd doe
cd ..

cd john_doe
mkdir john_doe
ls
tree
cd john_doe
cd doe
cd ..

cd .a_hidden_folder_in_doe
mkdir .a_hidden_folder_in_doe
ls
ls -a
tree
tree -a
cd .a_hidden_folder_in_doe
cd doe
cd ..

cd jane_doe
ls
ls -a
tree
cd mary_jane_doe
mkdir mary_jane_doe
cd mary_jane_doe
cd ..
cd .a_hidden_folder_in_jane_doe
mkdir .a_hidden_folder_in_jane_doe
cd .a_hidden_folder_in_jane_doe
cd ..
tree
tree -a

cd ..
cd john_doe
ls
ls -a
tree
cd lil_john_doe
mkdir lil_john_doe
cd lil_john_doe
cd ..
cd .a_hidden_folder_in_john_doe
mkdir .a_hidden_folder_in_john_doe
cd .a_hidden_folder_in_john_doe
cd ..
tree
tree -a

cd ..
tree
tree -a
touch a_file_in_doe
touch .a_hidden_file_in_doe
ls
ls -a

cd jane_doe
touch a_file_in_jane_doe
touch .a_hidden_file_in_jane_doe
ls -a
cd ..

cd john_doe
touch a_file_in_john_doe
touch .a_hidden_file_in_john_doe
ls -a
cd ..
tree
tree -a

cd mary_jane_doe
tree -d
cd jane_doe/mary_jane_doe
cd ../..

cd lil_john_doe
tree -d
cd john_doe/lil_john_doe
cd ../..
tree

cd jane_doe/mary_jane_doe
touch a_file_in_mary_jane_doe
touch .a_hidden_file_in_mary_jane_doe
mkdir .a_hidden_folder_in_mary_jane_doe
ls -a
cd ../..

cd john_doe/lil_john_doe
touch a_file_in_lil_john_doe
touch .a_hidden_file_in_lil_john_doe
mkdir .a_hidden_folder_in_lil_john_doe
ls -a
cd ../..
tree
tree -a

touch jane_doe/a_child_of_doe
touch jane_doe/mary_jane_doe/a_grandchild_of_doe
touch john_doe/a_child_of_doe
touch john_doe/lil_john_doe/a_grandchild_of_doe
tree

cd jane_doe
touch mary_jane_doe/a_child_of_jane_doe
touch ../aka_parent_of_jane_doe
touch ../john_doe/aka_sibling_of_jane_doe
touch ../john_doe/lil_john_doe/child_of_sibling_of_john_doe
cd ../john_doe/lil_john_doe
mv child_of_sibling_of_john_doe child_of_sibling_of_jane_doe
cd ../..
tree

cd john_doe
touch lil_john_doe/a_child_of_john_doe
touch ../aka_parent_of_john_doe
touch ../jane_doe/aka_sibling_of_john_doe
touch ../jane_doe/mary_jane_doe/child_of_sibling_of_jane_doe
cd ../jane_doe/mary_jane_doe
mv child_of_sibling_of_jane_doe child_of_sibling_of_john_doe
cd ../..
tree

cd jane_doe/mary_jane_doe
touch ../aka_parent_of_mary_jane_doe
touch ../../aka_grandparent_of_mary_jane_doe
touch ../../john_doe/aka_aunt_of_mary_jane_doe
cd ../../john_doe
mv aka_aunt_of_mary_jane_doe aka_uncle_of_mary_jane_doe
cd ../jane_doe/mary_jane_doe
touch ../../john_doe/lil_john_doe/cousin_of_mary_jane_doe
tree ../..

cd ../../john_doe/lil_john_doe
touch ../aka_parent_of_lil_john_doe
touch ../../aka_grandparent_of_lil_john_doe
touch ../../jane_doe/aka_uncle_of_lil_john_doe
cd ../../jane_doe
mv aka_uncle_of_lil_john_doe aka_aunt_of_lil_john_doe
cd ../john_doe/lil_john_doe
touch ../../jane_doe/mary_jane_doe/cousin_of_lil_john_doe
tree ../../../doe

cd ../../..
ls -a doe
ls -a doe/jane_doe
ls -a doe/jane_doe/mary_jane_doe

cd doe/jane_doe/mary_jane_doe
ls -a ../../john_doe
ls -a ../../john_doe/lil_john_doe
tree ../../john_doe/lil_john_doe
tree ../../john_doe

cd ../../john_doe/lil_john_doe
ls -a ../../jane_doe/mary_jane_doe
tree ../../jane_doe/mary_jane_doe
tree ../../jane_doe
cd ../../..
tree doe -ad
tree -a doe

rm doe
rm --recursive doe
cd doe