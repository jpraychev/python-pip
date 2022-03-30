from python_pip import pip

pip = pip.PIP()

def test_version():
    assert pip.version == '0.33'

def test_package_list():
    """ If pip is installed, underlying pip freeze command that is used from 
    list_packages() should return atleast one package """
    assert len(pip.list_packages()) >= 1

def test_package_install_fail():
    """ Try to install unreleased requests version """
    output = pip.install('requests==0.001')
    assert 'could not be installed' in output

def test_package_install_success():
    """ Try to install latest version of requests """
    output = pip.install('requests')
    assert 'Successfully installed requests' in output

def test_package_already_installed():
    """ Try to install latest version of requests """
    output = pip.install('requests')
    assert 'Requirement already satisfied' in output

def test_package_uninstall_success():
    output = pip.uninstall('requests')
    assert 'Successfully uninstalled requests' in output