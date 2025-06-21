import pygame
from define import *
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()