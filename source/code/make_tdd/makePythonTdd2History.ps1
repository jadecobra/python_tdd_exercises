cd person
tree
uv run pytest-watcher
tree
echo "Hello, my name is Jacob"
"pytest" | Out-File requirements.txt -Encoding UTF8
tree
cat requirements.txt
"pytest-watcher" >> requirements.txt
cat requirements.txt
cat pyproject.toml
uv add --requirement requirements.txt
tree
cat pyproject.toml
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv/Scripts/activate.ps1
deactivate
uv run pytest-watcher . --now
git add .
git commit --all --message 'automate tests'
cd ..
