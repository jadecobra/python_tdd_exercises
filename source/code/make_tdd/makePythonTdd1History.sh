cd person
uv init person
cd person
tree
tree -a -L 2
cat .gitignore
cat pyproject.toml
cat python-version
cat .python-version
cat README.md
mkdir src
tree
tree -a -L 1
python3 src/person.py
mv main.py src/person.py
tree -a -L 2
python3 src/person.py
cat src/person.py
python3 -m unittest
mkdir tests
tree -a -L 1
touch tests/person.py
tree -a -L 2
python3 -m unittest
touch tests/__init__.py
tree -a -L 2
python3 -m unittest
mv tests/person.py tests/test_person.py
tree -a -L 2
python3 -m unittest
python3 -m unittest
git commit --all --message 'setup project'
cd ..