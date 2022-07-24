import pygame
from pygame.locals import *
from math import floor
import ReversiGame
import time
import Mediador
import MiniMax

pygame.init()

screen =  pygame.display.set_mode((1000, 750))
pygame.display.set_caption('Reversi')
pos = pygame.image.load(r'Sprites/Posicao.png')
peca_branca = pygame.image.load(r'Sprites/Peca_branca.png')
peca_preta = pygame.image.load(r'Sprites/Peca_preta.png')
possibilidades = pygame.image.load(r'Sprites/Possibilidade.png')
font = pygame.font.Font('freesansbold.ttf', 16)
botao_jogar = pygame.image.load(r'Sprites/Botao.png')
botao_jogar_click = pygame.image.load(r'Sprites/Botao2.png')
reversi_escrita = pygame.image.load(r'Sprites/REVERSI.png')



    
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


def reversiInterface():
    display(game.estado, game.getTodasPoss())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                if(game.estado !="FIN"):
                    X, Y = pygame.mouse.get_pos()
                    if Y <= 650 and Y >=50 and X <= 820 and X >= 220:
                        i = floor((X-220)/75)
                        j = floor((Y-50)/75)
                        
                    if(game.jogar(i, j)):
                        display(game.estado)
                        jogadaAdv = MiniMax.escolheJogada(game)
                        game.jogar(jogadaAdv[0], jogadaAdv[1])
                        time.sleep(0.5)
                        display(game.estado, game.getTodasPoss())
                    

def tela_inicial():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                X, Y = pygame.mouse.get_pos()
                if (X >= 375 and X <= 625 and Y >= 332 and Y <= 419):
                    screen.fill((225, 225, 225))
                    screen.blit(reversi_escrita, (280, 175))
                    screen.blit(botao_jogar_click, (375, 332))
                    pygame.display.update()
                    time.sleep(0.2)
                    reversiInterface()
        screen.fill((225, 225, 225))
        screen.blit(reversi_escrita, (280, 175))
        screen.blit(botao_jogar, (375, 332))
        pygame.display.update()

tela_inicial()
print("FIM DE JOGO")

