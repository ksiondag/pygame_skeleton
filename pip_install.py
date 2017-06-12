from contextlib import redirect_stdout
from importlib import reload
import os
import pip

libs_to_install = [
    # All the libs to install to the current virtualenv
    # Use this if your game needs some other python library
    'pygame==1.9.3',
    'PyInstaller==3.1.1',
    'Pillow==4.1.1',
    'git+https://github.com/pyjs/pyjs.git#egg=pyjs',
]

# TODO: save stdout somewhere and parse out what new things were successfully installed
# That way we can update dependencies.txt in the same instance of installing
pip.main(['install'] + libs_to_install)
