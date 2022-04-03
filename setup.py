import setuptools
import re

with open('src/python_pip/pip.py', 'r', encoding='utf-8') as file:
    content = file.readlines()

with open('README.md', 'r', encoding='utf-8') as file:
    long_desc = file.read()

setup_vars = {}
regex = "__(\w+)__(\s\=\s)'([\w\.@\s\-]+)'"

for line in content:
    if line.startswith('__'):
        m = re.search(regex, line)
        key, val = m.group(1), m.group(3)
        setup_vars[key] = val

setuptools.setup(
    name=setup_vars['package_name'],
    version=setup_vars['version'],
    author=setup_vars['author'],
    author_email=setup_vars['author_email'],
    description='Python PIP thin wrapper',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/jpraychev/python-pip',
    project_urls={
        'Bug Tracker': 'https://github.com/jpraychev/python-pip/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)