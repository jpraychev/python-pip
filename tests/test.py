import sys
sys.path.append("D:\Personal Projects\python-pip\src")
from python_pip import pip

pip = pip.PIP()

names = ['pyotp', 'requests', 'python-pip']
bulk_install = pip.bulk_install(package_names=names)
print(bulk_install)
# print(pip.version)