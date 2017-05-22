"""
Hack to save current virtualenv libraries into "dependencies.txt"

Just think that it's nice to have the code notice more libraries have been
installed and have it save to the file that tracks that stuff.
"""
from contextlib import redirect_stdout
import pip
import os

def main():
    dependencies_file = os.path.join(os.path.dirname(__file__), 'dependencies.txt')

    print('Saving dependencies file')
    with open(dependencies_file, 'w') as f:
        with redirect_stdout(f):
            pip.main(['freeze'])

    # Go ahead and print the newly minted dependencies file
    print()
    print('Libraries in current virtualenv:')
    with open(dependencies_file, 'r') as f:
        print(f.read())

if __name__ == '__main__':
    main()