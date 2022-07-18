import pygame
from pygame.locals import *
from math import floor
import ReversiGame
import time
import Mediador

pygame.init()

screen =  pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Reversi')
pos = pygame.image.load(r'Sprites/Posicao.png')
peca_branca = pygame.image.load(r'Sprites/Peca_branca.png')
peca_preta = pygame.image.load(r'Sprites/Peca_preta.png')
possibilidades = pygame.image.load(r'Sprites/Possibilidade.png')
font = pygame.font.Font('freesansbold.ttf', 16)


game = ReversiGame.ReversiGame()

def display(estado, todasPoss = []):
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
     
    for poss in todasPoss:
        screen.blit(possibilidades, ((220 + poss[0]*75), (50 + poss[1]*75))) 
     
    if(estado =="PASS"):
        passar = "Nenhuma jogada possível! Clicke para passar a jogada."
        txt = font.render(passar, 1, (145, 0, 0))
        screen.blit(txt,(50, 700)) 
    
    elif(estado == "FIN"):
    	placarPretas = "PRETAS: "+str(game.placar["BLACK"])
    	txt = font.render(placarPretas, 1, (20, 20, 20))
    	screen.blit(txt,(25, 50)) 
    	placarBrancas = "BRANCAS: "+str(game.placar["WHITE"])
    	txt = font.render(placarBrancas, 1, (20, 20, 20))
    	screen.blit(txt,(25, 100)) 
    	
    pygame.display.update() 


display(game.estado, game.getTodasPoss())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if(game.estado =="NORMAL"):
                X, Y = pygame.mouse.get_pos()
                if Y <= 650 and Y >=50 and X <= 820 and X >= 220:
                    i = floor((X-220)/75)
                    j = floor((Y-50)/75)
                    
                if(game.jogar(i, j)):
                    display(game.estado)
                    jogadaAdv = Mediador.jogaAleatorio(game.getTodasPoss())
                    time.sleep(1)
                    game.jogar(jogadaAdv[0], jogadaAdv[1])
                    time.sleep(1)
                    display(game.estado, game.getTodasPoss()) 


print("FIM DE JOGO")

