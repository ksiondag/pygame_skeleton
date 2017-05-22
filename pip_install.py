from contextlib import redirect_stdout
from importlib import reload
import os
import pip

import install_dependencies

libs_to_install = [
    # All the libs to install to the current virtualenv
    # Use this if your game needs some other python library
    #'pygame',
    #'pyinstaller',
    #'pillow',
]

pip.main(['install'] + libs_to_install)

dependencies_file = os.path.join(os.path.dirname(__file__), 'dependencies.txt')

print()
print('Installing libraries already in dependencies file')
# This will update the dependencies file
# make sure we already have everything in it installed
install_dependencies.main()