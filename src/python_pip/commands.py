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
    def _clear_cache(cls):
        return cls._create_cmd('pip', 'cache', 'purge')

    @classmethod
    def _show_cache(cls):
        return cls._create_cmd('pip', 'cache', 'list')