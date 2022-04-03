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

### 4. Install all required libraries
```
There are no requirements at the moment
```

### 5. Usage
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