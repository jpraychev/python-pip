# Python PIP Wrapper

## Installation
---
### 1. Clone or download the repository

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
from python_pip import PIP
```

```
# Initialize object
pip = PIP()
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