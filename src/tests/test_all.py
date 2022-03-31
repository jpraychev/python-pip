from python_pip import pip
from pytest import fixture

pip = pip.PIP()

@fixture(scope='session', autouse=True)
def cleanup(request):
    print('\nSetting up...')
    def fin():
        print('\nCleaning up...')
        pip.uninstall('requests')
    request.addfinalizer(fin)

@fixture
def package_list():
    return pip.list_packages()

def install_package(package):
    return pip.install(package)

def uninstall_package(package):
    return pip.uninstall(package)

def test_version():
    assert pip.version == '0.33'

def test_package_list(package_list):
    """ If pip is installed, underlying pip freeze command that is used from 
    list_packages() should return atleast one package """
    assert len(package_list) >= 1

def test_package_install_fail():
    """ Try to install unreleased requests version """
    output = pip.install('requests==0.001')
    assert 'could not be installed' in output

def test_package_install(package_list):
    """ Test to install latest version of requests library """
    if not 'requests' in package_list:
        output = pip.install('requests')
        print(output)
        assert 'Successfully installed requests' in output
    else:
        uninstall_package('requests')
        output = pip.install('requests')
        assert 'Successfully installed requests' in output
    
def test_package_uninstall(package_list):
    """ Test to uninstall latest version of requests library """
    if 'requests' in package_list:
        output = uninstall_package('requests')
        print(output)
        assert 'Successfully uninstalled requests' in output
    else:
        install_package('requests')
        output = uninstall_package('requests')
        assert 'Successfully uninstalled requests' in output

def test_package_already_installed(package_list):
    """ Test if latest version of requests library is already installed """
    if 'requests' in package_list:
        output = install_package('requests')
        assert 'Requirement already satisfied' in output
    else:
        install_package('requests')
        output = install_package('requests')
        assert 'Requirement already satisfied' in output