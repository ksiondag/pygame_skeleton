"""
General helper functions for pygame/pyinstaller functionality.
"""
import os
import sys

import pygame

import save_dependencies

def dev_mode():
    return not hasattr(sys, "_MEIPASS")


def path(*args):
    if not dev_mode():
        return os.path.join(sys._MEIPASS, *args)
    return os.path.join(*args)


def load_image(basename, size=None):
    fullname = path('data', basename)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise message

    rect = image.get_rect()

    if size:
        rect.width = size[0]
        rect.height = size[1]
        image = pygame.transform.scale(image, rect.size)    

    return image, image.get_rect()


def load_image_as_icon(basename):
    fullname = path('data', basename)
    image = pygame.image.load(fullname)

    rect = image.get_rect()

    rect.width = 32
    rect.height = 32
    image = pygame.transform.scale(image, rect.size)

    return image, image.get_rect()


def size():
    return 500, 400


def main(play, caption='Caption!'):
    """
    This is a generic main that can be used by the main game
    (vitality_person.py) or any subgame you create (breakfast.py).
    
    This way you have an easy way to test subgames while developing them without
    running the main game.
    """    
    # set up pygame
    pygame.init()

    # set window icon before setting display mode
    # some systems don't let you change it after it is set
    # (according to documentation)
    # pygame defaults to a generic python icon if not set yet
    icon, _ = load_image_as_icon('icon.png')
    pygame.display.set_icon(icon)

    # set up the window
    screen = pygame.display.set_mode(size(), 0, 32)

    # Note: if you want to play with changing the icon after setting mode
    # any display set with images saved via the PIL module will not work
    # I don't know why
    # ICO files will cause error
    # Other files will just not load (icon will be white/blank)
    # TODO: Will make an issue on pygame and link to it here
    # Anyways, load icon image the same way you do above
    # If you want to make an ICO file that pygame likes
    # the website X-Icon Editor worked for me:
    # http://www.xiconeditor.com/
    #icon, _ = load_image_as_icon('icon.png')
    #pygame.display.set_icon(icon)

    pygame.display.set_caption(caption)

    play()
    pygame.quit()

# Save installed libraries if this isn't the executable version of game
if dev_mode():
    save_dependencies.main()

