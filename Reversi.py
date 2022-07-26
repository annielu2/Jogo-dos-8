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

backgroundReversi = pygame.image.load(r'Sprites/wood.jpg')
logo = pygame.image.load(r'Sprites/logo.png')

pos = pygame.image.load(r'Sprites/Posicao.png')
peca_branca = pygame.image.load(r'Sprites/Peca_branca.png')
peca_preta = pygame.image.load(r'Sprites/Peca_preta.png')
borda = pygame.image.load(r'Sprites/Borda.png')
possibilidades = pygame.image.load(r'Sprites/Possibilidade.png')

font = pygame.font.Font(r'Font/BD_Cartoon_Shout.ttf', 24)
font_placar = pygame.font.Font(r'Font/BD_Cartoon_Shout.ttf', 50)

botao_jogar = pygame.image.load(r'Sprites/Botao.png').convert_alpha()
botao_jogar_click = pygame.image.load(r'Sprites/Botao2.png').convert_alpha()
botao_jogar_novamente = pygame.image.load(r'Sprites/novo_jogo.png').convert_alpha()
botao_sair = pygame.image.load(r'Sprites/Sair.png').convert_alpha()

def background_display(game):
    screen.fill((225,225,225))
    
    screen.blit(backgroundReversi, (0, 0))
    
    screen.blit(borda, (160, 35))
    
    placarPretas = str(game.placar["BLACK"])
    txt = font.render(placarPretas, 1, (20, 20, 20))
    pecaP = peca_preta
    pecaP = pygame.transform.scale(pecaP, (40, 40))
    screen.blit(pecaP,(25, 75)) 
    screen.blit(txt,(75, 85)) 
    
    placarBrancas = str(game.placar["WHITE"])
    txt = font.render(placarBrancas, 1, (20, 20, 20))
    pecaB = peca_branca
    pecaB = pygame.transform.scale(pecaB, (40, 40))
    screen.blit(pecaB,(25, 125)) 
    screen.blit(txt,(75, 135))

    
#game = ReversiGame.ReversiGame()

def display(game, todasPoss = []):
    
    background_display(game)
    

    for i in range(8):
        for j in range(8):
            auxX = 200 + i*75
            auxY = 75 + j*75
            posicao = (auxX, auxY)
            screen.blit(pos, posicao)
            if game.tabuleiro[i][j] == 'WHITE':
                screen.blit(peca_branca, posicao)
            elif game.tabuleiro[i][j] == 'BLACK':
                screen.blit(peca_preta, posicao)
     
    for poss in todasPoss:
        screen.blit(possibilidades, ((200 + poss[0]*75), (75 + poss[1]*75))) 
     
    if(game.estado =="PASS"):
        passar = "Nenhuma jogada possível! Clicke para passar a jogada."
        txt = font.render(passar, 1, (145, 0, 0))
        screen.blit(txt,(50, 700))
    	
    pygame.display.update() 


def game_over(game):
    screen.blit(backgroundReversi, (0, 0))

    screen.blit(botao_jogar_novamente, (275, 350))
    screen.blit(botao_sair, (275, 500))

    screen.blit(peca_branca, (275, 250))
    screen.blit(peca_preta, (500, 250))

    placarPretas = str(game.placar["BLACK"])
    txt = font_placar.render(placarPretas, 1, (20, 20, 20))
    screen.blit(txt,(600, 262)) 
    
    placarBrancas = str(game.placar["WHITE"])
    txt = font_placar.render(placarBrancas, 1, (20, 20, 20))
    screen.blit(txt,(375, 262))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                X, Y = pygame.mouse.get_pos()
                if (X >= 275 and X <= 725 and Y >= 350 and Y <= 450):               
                    new_game = ReversiGame.ReversiGame()
                    time.sleep(0.2)
                    reversiInterface(new_game)
                elif (X >= 275 and X <= 725 and Y >= 500 and Y <= 600):
                    pygame.quit()
                    
                
        pygame.display.update()

                
def reversiInterface(game):
    display(game, game.getTodasPoss())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                if(game.estado !="FIN"):
                    X, Y = pygame.mouse.get_pos()
                    if Y <= 650 and Y >=75 and X <= 820 and X >= 200:
                        i = floor((X-200)/75)
                        j = floor((Y-75)/75)
                        
                    if(game.jogar(i, j)):
                        display(game)
                        jogadaAdv = MiniMax.escolheJogada(game)
                        game.jogar(jogadaAdv[0], jogadaAdv[1])
                        time.sleep(0.5)
                        display(game, game.getTodasPoss())
                
            if(game.estado == "FIN"):
                time.sleep(2.0)
                game_over(game)

                    

def tela_inicial(): 
    game = ReversiGame.ReversiGame()
    screen.blit(backgroundReversi, (0, 0))
    screen.blit(botao_jogar, (375, 400))
    screen.blit(logo, (250, 100))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                X, Y = pygame.mouse.get_pos()
                if (X >= 350 and X <= 650 and Y >= 400 and Y <= 550):               
                    #screen.blit(botao_jogar_click, (375, 400))
                    pygame.display.update()
                    time.sleep(0.2)
                    reversiInterface(game)
        pygame.display.update()

tela_inicial()
print("FIM DE JOGO")

