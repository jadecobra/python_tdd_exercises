# Learn Directory Structure# Learn Directory Structure
cd parent
mkdir parent
cd parent
pwd
ls
ls --all
cd .
cd ..
cd parent
touch a_file_in_parent
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
ls -a
tree
mkdir child_of_child
cd child_of_child
cd .
tree
touch a_file_in_child_of_child
touch a_grandchild_of_parent
tree
cd parent
cd child
cd sibling_of_child
cd does_not_exist
pwd
cd ..
ls -a
tree
cd ..
cd child/child_of_child
cd ../..
pwd
ls -a
tree
cd sibling_of_child
ls -a
tree
mkdir child_of_sibling_of_child
cd child_of_sibling_of_child
touch a_file_in_child_of_sibling_of_child
touch another_grandchild_of_parent
ls -a
tree
cd parent
cd child
cd sibling_of_child
cd child_of_child
cd does_not_exist
pwd
cd ..
pwd
ls -a
tree
cd ..
cd sibling_of_child/child_of_sibling_of_child
cd ../..
pwd
ls -a
tree
touch aka_grandparent_of_child_of_child
touch aka_grandparent_of_child_of_sibling_of_child
tree
cd child
touch a_file_in_child
cd ../sibling_of_child
touch a_file_in_sibling_of_child
cd ../..
tree parent
touch parent/child/aunt_or_uncle_of_another_grandchild_of_parent
touch parent/sibling_of_child/aunt_or_uncle_of_a_grandchild_of_parent
tree parent
touch parent/child/child_of_child/cousin_of_another_grandchild_of_parent
touch parent/sibling_of_child/child_of_sibling_of_child/cousin_of_a_grandchild_of_parent
tree parent
cd parent
cd sibling_of_child
cd child_of_sibling_of_child
cd ../../..
cd parent/sibling_of_child/child_of_sibling_of_child
cd ../../child/child_of_child
tree ../../sibling_of_child
tree ../../sibling_of_child/child_of_sibling_of_child
cd ../../sibling_of_child/child_of_sibling_of_child
tree ../../child
tree ../../child/child_of_child
ls -a ../../child/child_of_child
ls -a ../../child
cd ../../child/child_of_child
ls -a ../../sibling_of_child/child_of_sibling_of_child
ls -a ../../sibling_of_child
tree ../../../parent
cd ../../..
pwd
rm -rf parent
cd parent