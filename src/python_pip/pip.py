from typing import List, Dict
from python_pip.commands import Commands

__package_name__ = 'python-pip'
__version__ = '1.1.1'
__author__ = 'Jordan Raychev'
__author_email__ = 'jpraychev@gmail.com'
__license__ = 'MIT. Please refer to LICENSE file'

class PIP():
    """ Python wrapper for PIP installer """

    @property
    def version(self):
        return __version__

    @property
    def license(self):
        return __license__

    def __str__(self):
        return 'A Python wrapper of the pip installer'

    @staticmethod
    def list_packages(pretty=False) -> Dict:
        """ List all installed packages. If pretty argument is set to True, 
        formats the output with indent. """

        """ pip freeze command normal output follows the convention:
        pytest==7.1.1
        
        If package is install via pip install . from the root dir, the output is
        show below:
        python-pip @ file:///D:/Personal%20Projects/python-pip
        """
        packages = dict()
        lp = Commands._list_packages()
        inst_packages = lp.stdout.split('\n')[:-1]

        for package in inst_packages:
            """ Ignoring locally installed packages if @ is in package name """
            if not '@' in package:
                name, version = package.split('==')[0], package.split('==')[1]
                packages[name] = version
        
        if pretty:
            import json
            return json.dumps(packages, sort_keys=True, indent=4)
        return packages

    @staticmethod
    def install(package_name:str) -> str:
        """ Install PIP package """

        if not isinstance(package_name, str):
            raise TypeError(f'Expected {package_name} to be a string')
        try:
            package = Commands._install(name=package_name)
        except Exception:
            return f'{package_name} could not be installed\n'
        return package.stdout

    @staticmethod
    def uninstall(package_name:str) -> str:
        """ Uninstall PIP package """

        if not isinstance(package_name, str):
            raise TypeError(f'Expected {package_name} to be a string')
        try:
            package = Commands._uninstall(name=package_name)
        except Exception:
            return f'{package_name} could not be uninstalled'
        return package.stdout if package.stdout else package.stderr

    @staticmethod
    def bulk_install(package_names:List[str]) -> str:
        """ Bulk install of packages from a list """

        success = []
        failure = []

        if not isinstance(package_names, list):
            raise TypeError(f'Expected {package_names} to be a list of strings')
        for package_name in package_names:
            try:
                package = Commands._install(name=package_name)
            except Exception:
                failure.append(package_name)
                break
            success.append(package_name)
        return f'Installed packages: {success}\nNot installed packages: {failure}'


    @staticmethod
    def bulk_uninstall(package_names:List[str]) -> str:
        """ Bulk uninstall of packages from a list """

        success = []
        failure = []
        if not isinstance(package_names, list):
            raise TypeError(f'Expected {package_names} to be a list of strings')
        for package_name in package_names:
            try:
                package = Commands._uninstall(name=package_name)
            except Exception:
                failure.append(package_name)
                break
            success.append(package_name)
        return f'Uninstalled packages: {success}\nNot uninstalled packages: {failure}'

    @staticmethod
    def export() -> None:
        """ Exports installed packages to requirements.txt file """

        lp = Commands._list_packages()
        installed_packages = lp.stdout.split('\n')[:-1]

        try:
            with open(file='requirements.txt', mode='w') as file:
                for package in installed_packages:
                    file.write(package + '\n')
        except Exception:
            return 'Could not export python packages'
        return 'Python packages exported to requirements.txt'

    @staticmethod
    def clear_cache():
        """ Clears pip cache current environment """

        try:
            cache = Commands._clear_cache()
        except Exception:
            return 'Cache is probably empty. Please run show_cache to verify first.'
        return cache.stdout
    
    @staticmethod
    def show_cache():
        """ Shows pip cache for current environment """

        try:
            cache = Commands._show_cache()
        except Exception:
            return 'Something went wrong'
        return cache.stdout