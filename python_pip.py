import subprocess

# # Main DOD contact
# # FPA53 - non blue green updates

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
    def _install(cls, pack_name:str):
        return cls._create_cmd('pip', 'install', pack_name)

    @classmethod
    def _uninstall(cls, pack_name:str):
        return cls._create_cmd('pip', 'uninstall', pack_name, '-y')

    @classmethod
    def _bulk_install(cls, pack_names:list):
        """ TO DO """
        pass

    @classmethod
    def _bulk_uninstall(cls, pack_names:list):
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

class PIP():
    """ Python wrapper for PIP installer """

    __version__ = '0.2'
    __author__ = 'Jordan Raychev'
    __email__ = 'jpraychev at gmail dot com'
    __license__ = 'MIT' # To be implemented from file

    @property
    def version(self):
        return self.__version__

    def __str__(self):
        return 'A Python wrapper of the pip installer'

    @staticmethod
    def list_packages(pretty=False):
        """ List all installed packages nicely formatted """
        packs = dict()
        packages = Commands._list_packages()
        installed_packages = packages.stdout.split('\n')[:-1]

        for package in installed_packages:
            name, version = package.split('==')[0], package.split('==')[1]
            packs[name] = version
        
        if pretty:
            import json
            return json.dumps(packs, sort_keys=True, indent=4)
        return packs

    @staticmethod
    def install(name:str) -> str:
        """ Install PIP package """

        if not isinstance(name, str):
            raise TypeError(f'Expected {name} to be a string')
        try:
            package = Commands._install(pack_name=name)
        except subprocess.CalledProcessError:
            return f'{name} package does not exist\n'
        return package.stdout

    @staticmethod
    def uninstall(name:str) -> str:
        """ Uninstall PIP package """

        if not isinstance(name, str):
            raise TypeError(f'Expected {name} to be a string')
        try:
            package = Commands._uninstall(pack_name=name)
        except Exception:
            return f'{name} could not be uninstalled'
        return package.stdout if package.stdout else package.stderr

    def bulk_install(names:list) -> str:
        """ TO DO """
        raise NotImplementedError

    def _bulk_uninstall(names):
        """ TO DO """
        raise NotImplementedError

    def _install_from_file(file):
        """ TO DO """
        raise NotImplementedError

    def _uninstall_from_file(file):
        """ TO DO """
        raise NotImplementedError