uv init magic
cd magic
tree
tree -a -L 2
cat .gitignore
cat pyproject.toml
cat python-version
cat .python-version
cat README.md
mkdir src
tree
tree -a -L 2
python3 src/magic.py
mv main.py src/magic.py
tree -a -L 2
python3 src/magic.py
cat src/magic.py
python3 -m unittest
mkdir tests
tree -a -L 2
touch tests/magic.py
tree
python3 -m unittest
touch tests/__init__.py
tree -a -L 2
python3 -m unittest
mv tests/magic.py tests/test_magic.py
tree -a -L 2
python3 -m unittest
python3 -m unittest
uv run pytest-watcher
echo "pytest"
echo "pytest" > requirements.txt
echo "pytest-watcher" >> requirements.txt
tree -a -L 2
cat requirements.txt
uv add --requirement requirements.txt
tree -a -L 1
cat pyproject.toml
source .venv/bin/activate
deactivate
uv run pytest-watcher . --now
cd ..
history