cd module_not_found_error
uv init module_not_found_error
cd module_not_found_error
mkdir tests
New-Item tests/module_not_found_error.py
python -m unittest
Move-Item tests/module_not_found_error.py tests/test_module_not_found_error.py
python -m unittest
New-Item tests/__init__.py
python -m unittest
python -m unittest
git add .
git commit --all --message 'setup project'
python -m unittest
New-Item src/module_00.py
python -m unittest
python -m unittest
New-Item src/module_01.py
python -m unittest
python -m unittest
New-Item src/module_02.py
python -m unittest
python -m unittest
New-Item src/module_03.py
python -m unittest
python -m unittest
New-Item src/module_04.py
python -m unittest
python -m unittest
New-Item src/module_05.py
python -m unittest
python -m unittest
python -m unittest
mkdir src/doe
python -m unittest
python -m unittest
New-Item src/doe/john.py
python -m unittest
python -m unittest
New-Item src/doe/jane.py
python -m unittest
python -m unittest
New-Item magic.py
python -m unittest
python -m unittest
git add .
git commit --all --message 'test ModuleNotFoundError'
cd ..