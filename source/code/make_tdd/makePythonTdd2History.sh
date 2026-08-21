cd person
tree -a -L 2
uv run pytest-watcher
tree -a -L 2
echo "Hello, my name is Jacob"
echo "pytest" > requirements.txt
tree -a -L 1
cat requirements.txt
echo "pytest-watcher" >> requirements.txt
cat requirements.txt
cat pyproject.toml
uv add --requirement requirements.txt
tree -a -L 1
cat pyproject.toml
source .venv/bin/activate
deactivate
uv run pytest-watcher . --now
git add .
git commit --all --message 'automate tests'
cd ..
