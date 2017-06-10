"""
Hack to save current virtualenv libraries into "dependencies.txt"

Just think that it's nice to have the code notice more libraries have been
installed and have it save to the file that tracks that stuff.

Note: this will save more libraries than you actually need to save. All dependencies
that a library is also locally installed and so will be saved into the dependencies.txt.
This can be problematic if developing on both Windows and Linux, as libraries may
have different dependencies on one than on another.

There may be a better means of remembering only the libraries one specifically
needs and letting pip install whatever dependencies are required, but for now
pruning the generated dependencies.txt when needed is the answer.
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