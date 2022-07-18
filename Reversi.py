import pygame
from pygame.locals import *
from math import floor
import ReversiGame

pygame.init()

screen =  pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Reversi')
pos = pygame.image.load(r'Sprites/Posicao.png')
peca_branca = pygame.image.load(r'Sprites/Peca_branca.png')
peca_preta = pygame.image.load(r'Sprites/Peca_preta.png')
possibilidades = pygame.Surface((40, 40))
possibilidades.fill((255, 0, 0))
estado = {}


for i in range(8):
    for j in range(8):
       x = 220 + i*75
       y = 50 + j*75
       aux = (x, y)
       estado[aux] = 'VAZIO'

game = ReversiGame.ReversiGame()
             
while True:
    for event in pygame.event.get():
        if event.type == QUIT:  
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            X, Y = pygame.mouse.get_pos()
            if Y <= 650 and Y >=50 and X <= 820 and X >= 220:
                i = floor((X-220)/75)
                j = floor((Y-50)/75)
                game.jogar(i, j, game.tipoJog)
                
    
    list_pos = estado.keys()
    screen.fill((225,225,225))
    for i in range(8):
        for j in range(8):
            auxX = 220 + i*75
            auxY = 50 + j*75
            posicao = (auxX, auxY)
            screen.blit(pos, posicao)
            if game.tabuleiro[i][j] == 'WHITE':
                screen.blit(peca_branca, posicao)
            elif game.tabuleiro[i][j] == 'BLACK':
                screen.blit(peca_preta, posicao)
     
    for poss in game.getTodasPoss():
        screen.blit(possibilidades, poss) 
     
    pygame.display.update()    



