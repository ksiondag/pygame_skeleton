"""
Build any script into an executable!

Edit the spec file of choice to target your main python file (the file you run
to run your game).

build_exe_onefile.spec puts everything into a single executable

build_exe_onedir.spec puts everything into a single directory

The single directory can be useful for a variety of reasons including but not
limited to:
* Allowing user modifications (arbitrarily changing art/music assets)
* Having a known directory to save user-data too (game saves, user settings)
* Solving issues with pyinstaller not bundling all the necessary files
  * E.g. sometimes dlls are missing and you need to add them in
  * This is solvable in single-file mode, but is slightly more complicated than
    adding the dll to the dist directory

If something is wrong with your executable that isn't wrong with your dev code
and you want to print debug, go to the spec file you're building with and turn
console=False to console=True.

TODO: add better logging setup to better catch errors both in dev-mode and in
executable.
"""
from PyInstaller.__main__ import run

# Everything in executable build
run(["-y", "build_exe_onefile.spec"])


# To have pyinstaller create spec file of given main script, uncomment below
#run(["hello_world.py"])

