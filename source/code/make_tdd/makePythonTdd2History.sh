cd person
uv run pytest-watcher
echo "Hello, my name is Jacob"
echo "pytest" > requirements.txt
tree -a -L 1
cat requirements.txt
echo "pytest-watcher" >> requirements.txt
cat requirements.txt
uv add --requirement requirements.txt
tree -a -L 1
cat pyproject.toml
source .venv/bin/activate
deactivate
uv run pytest-watcher . --now
git add .
git commit --all --message 'automate tests'
cd ..