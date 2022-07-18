import pygame
from pygame.locals import *
#import Reversi

#Teste tela inicial
pygame.init()

screen =  pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Reversi inicio')

font = pygame.font.Font('freesansbold.ttf', 48)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        txt = font.render("BEM-VINDO AO REVERSI!", 1, (255, 255, 255))
        screen.blit(txt, txt.get_rect(center=screen.get_rect().center))
        pygame.display.update()




