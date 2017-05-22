"""
Note: Pygame fails to load ico files created via PIL

PyInstaller likes them just fine.

Pygame also doesn't like to use images saved via PIL as its icon. Setting a PIL-
generated PNG file as the pygame.display.set_icon will just lead to a blank
icon unless set_icon is called before set_mode.

PIL images otherwise render in pygame just fine.
"""
import os

from PIL import Image

filename = os.path.join('data', 'icon.png')

img = Image.open(filename)
img.save(os.path.join('data', 'icon.ico'))
