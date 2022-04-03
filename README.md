# Python PIP Wrapper
A thin wrapper around PIP which can be used at runtime.

![Run CI](https://github.com/jpraychev/python-pip/actions/workflows/CI.yml/badge.svg?branch=master)
## Installation
---
### 1. Install package from PyPi
```
pip install python-pip
```

### 2. Create a virtual environment
```
python -m venv venn
```

### 3. Activate the virtual environment
```
./venv/Scripts/activate
```

### 4. Running tests after installation
```
pip install -r requirements-tests.txt
pytest
```
### Example output
```
=================== test session starts ===================
platform win32 -- Python 3.9.2, pytest-7.1.1, pluggy-1.0.0
rootdir: D:\Personal Projects\python-pip
collected 6 items
src\tests\test_all.py ...... [100%] 
=================== 6 passed in 9.64s ===================
```

### 5. Install all required libraries
```
There are no requirements at the moment
```

### 6. Usage
```
from python_pip import pip
```

```
# Initialize object
pip = pip.PIP()
print(pip.version)
```

```
# Install a package
pip.install(package_name='requests')
```

```
# Uninstall a package
pip.uninstall(package_name='requests')
```

## Contributing
You are welcome to contribute to the repo as you like

## Authors and acknowledgment
Jordan Raychev

Email: jpraychev at gmail dot com

Website: https://jraychev.com

## License
MIT. Please refer to LICENSE file