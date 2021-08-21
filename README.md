# Python PIP Wrapper

## Installation
---
### 1 pip install python-pip


### 2. Create a virtual environment
```
>>> python -m venv venn
```

### 3. Activate the virtual environment
```
>>> ./venv/Scripts/activate
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
See LICENSE file