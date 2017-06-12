"""
This is a slightly modified version of Invent With Python's pygameHelloWorld.py

https://inventwithpython.com/pygameHelloWorld.py

Used without permission. I'm sorry. If the author is not okay with that, please
let me know and I'll remove it from the repository.

Read the Invent with Python book on pygame: Making Games with Python & Pygame
http://inventwithpython.com/pygame/
"""

import sys

import pygame

import resources

    
def play():
    windowSurface = pygame.display.get_surface()
    
    # set up the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    
    # set up fonts
    # NOTE: you have to load font from data area for pyinstaller executable to
    # work correctly
    basicFont = pygame.font.Font(resources.path('data', 'vgasys.fon'), 48)
    
    # set up the text
    text = basicFont.render('Hello world!', True, WHITE, BLUE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery
    
    # draw the white background onto the surface
    windowSurface.fill(BLACK)
    
    # draw a green polygon onto the surface
    pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    
    # draw some blue lines onto the surface
    pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
    pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)
    
    # draw a blue circle onto the surface
    pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)
    
    # draw a red ellipse onto the surface
    pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)
    
    # draw the text's background rectangle onto the surface
    pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
    
    # get a pixel array of the surface
    pixArray = pygame.PixelArray(windowSurface)
    pixArray[480][380] = BLACK
    del pixArray
    
    # draw the text onto the surface
    windowSurface.blit(text, textRect)
    
    # draw the window onto the screen
    pygame.display.update()
    
    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == '__main__':
    resources.main(play, 'Hello World!')
    
    