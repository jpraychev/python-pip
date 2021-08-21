import subprocess

class Commands():
    """ Class that specifies all PIP commands that are implemented
        For referece, please use pip --help """

    @staticmethod
    def _create_cmd(*args):
        exec_cmd = subprocess.run(
            list(args),
            check=True,
            capture_output=True,
            text=True)
        return exec_cmd

    @classmethod
    def _list_packages(cls):
        return cls._create_cmd('pip', 'freeze')
    
    @classmethod
    def _install(cls, name:str):
        return cls._create_cmd('pip', 'install', name)

    @classmethod
    def _uninstall(cls, name:str):
        return cls._create_cmd('pip', 'uninstall', name, '-y')

    @classmethod
    def _bulk_install(cls, name:list):
        """ TO DO """
        pass

    @classmethod
    def _bulk_uninstall(cls, name:list):
        """ TO DO """
        pass

    @classmethod
    def _install_from_file(cls, file:str):
        """ TO DO """
        pass

    @classmethod
    def _uninstall_from_file(cls, file:str):
        """ TO DO """
        pass

    @classmethod
    def _export(cls, file:str):
        """ TO DO """
        pass

class PIP():
    """ Python wrapper for PIP installer """

    __version__ = '0.2'
    __author__ = 'Jordan Raychev'
    __email__ = 'jpraychev at gmail dot com'
    __license__ = 'MIT. Please refer to LICENSE file'

    @property
    def version(self):
        return self.__version__

    @property
    def license(self):
        return self.__license__

    def __str__(self):
        return 'A Python wrapper of the pip installer'

    @staticmethod
    def list_packages(pretty=False):
        """ List all installed packages nicely formatted """
        packages = dict()
        lp = Commands._list_packages()
        inst_packages = lp.stdout.split('\n')[:-1]

        for package in inst_packages:
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
        except subprocess.CalledProcessError:
            return f'{package_name} package does not exist\n'
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
    def bulk_install(package_names:list):
        """ TO DO """
        raise NotImplementedError

    @staticmethod
    def bulk_uninstall(package_names):
        """ TO DO """
        raise NotImplementedError

    @staticmethod
    def install_from_file(file):
        """ TO DO """
        raise NotImplementedError

    @staticmethod
    def uninstall_from_file(file):
        """ TO DO """
        raise NotImplementedError

    @staticmethod
    def export(file):
        """ TO DO """
        raise NotImplementedError