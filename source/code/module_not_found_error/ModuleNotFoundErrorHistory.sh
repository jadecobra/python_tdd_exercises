cd module_not_found_error
uv init module_not_found_error
cd module_not_found_error
mkdir src
mv main.py src/main.py
mkdir tests
touch tests/module_not_found_error.py
python3 -m unittest
mv tests/module_not_found_error.py tests/test_module_not_found_error.py
python3 -m unittest
touch tests/__init__.py
python3 -m unittest
mv src/main.py src/module_00.py
python3 -m unittest
touch src/module_01.py
python3 -m unittest
touch src/module_02.py
python3 -m unittest
touch src/module_03.py
python3 -m unittest
touch src/module_04.py
python3 -m unittest
touch src/module_05.py
python3 -m unittest
mkdir src/doe
python3 -m unittest
touch src/doe/john.py
python3 -m unittest
touch src/doe/jane.py
python3 -m unittest
touch magic.py
python3 -m unittest
git add .
git commit --all --message 'test ModuleNotFoundError'
cd ..