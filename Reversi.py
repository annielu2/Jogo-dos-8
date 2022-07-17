import pygame
from pygame.locals import *
from math import floor

pygame.init()

screen =  pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Reversi')
pos = pygame.image.load(r'Sprites/Posicao.png')
peca_branca = pygame.image.load(r'Sprites/Peca_branca.png')
posicoes = []
estado = {}


for i in range(8):
    for j in range(8):
       x = 220 + i*75
       y = 50 + j*75
       aux = (x, y)
       posicoes.append(aux)
       estado[aux] = 'VAZIO'
       
             
while True:
    for event in pygame.event.get():
        if event.type == QUIT:	
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            X, Y = pygame.mouse.get_pos()
            if Y <= 650 and Y >=50 and X <= 820 and X >= 220:
            	i = floor((X-220)/75)
            	j = floor((Y-50)/75)
            	auxX = 220 + i*75
            	auxY = 50 + j*75
            	estado[(auxX, auxY)] = 'WHITE'
            
            	
    
    list_pos = estado.keys()
    screen.fill((225,225,225))
    for posicao in list_pos:  
    	screen.blit(pos, posicao)
    	if estado[posicao] == 'WHITE':
    	    screen.blit(peca_branca, posicao)
    pygame.display.update()    



