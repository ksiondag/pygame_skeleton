from contextlib import redirect_stdout
import pip
import os

def main():
    dependencies_file = os.path.join(os.path.dirname(__file__), 'dependencies.txt')
    
    if os.path.exists(dependencies_file):
        pip.main(['install', '-r', dependencies_file])
    else:
        print('No dependencies file, create one using pip_install.py')

    return dependencies_file

if __name__ == '__main__':
    main()
    
    