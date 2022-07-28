#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Reversi.py
#  
#  Copyright 2022 João Paulo Paiva Lima <joao.lima1@estudante.ufla.br> e Ana Luiza Faria Calixto <ana.calixto@estudante.ufla.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import pygame
from pygame.locals import *
from math import floor
import ReversiGame
import time
import Mediador
import MiniMax

# Utilizamos o método init para inicializar o jogo
pygame.init()

# Aqui será criado o display, uma tela de 1000x750
screen =  pygame.display.set_mode((1000, 750))
pygame.display.set_caption('Reversi')
screen_rect = screen.get_rect()

# Cria-se objetos para carregar os sprites que serão utilizados no jogo.
# É passado o path dos sprites para o carregamento.
backgroundReversi = pygame.image.load(r'Sprites/wood.jpg')
logo = pygame.image.load(r'Sprites/logo.png')
fim_jogo = pygame.image.load(r'Sprites/fim_jogo.png')
dificuldade = pygame.image.load(r'Sprites/Dificuldade.png').convert_alpha()

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
botao_jogar_novamente_click = pygame.image.load(r'Sprites/novo_jogo2.png').convert_alpha()
botao_sair_click = pygame.image.load(r'Sprites/Sair2.png').convert_alpha()
botao_facil = pygame.image.load(r'Sprites/Facil.png').convert_alpha()
botao_medio = pygame.image.load(r'Sprites/Medio.png').convert_alpha()
botao_dificil = pygame.image.load(r'Sprites/Dificil.png').convert_alpha()
facil_selected = pygame.image.load(r'Sprites/Facil_selected.png').convert_alpha()
medio_selected = pygame.image.load(r'Sprites/Medio_selected.png').convert_alpha()
dificil_selected = pygame.image.load(r'Sprites/Dificil_selected.png').convert_alpha()

# Esta função é responsável por criar o background do jogo e desenhar o placar
def background_display(game):
    screen.fill((225,225,225))
    
    screen.blit(backgroundReversi, (0, 0))
    
    screen.blit(borda, (160, 35))
    
    # É carregada a imagem da peça juntamente com a quantidade dela nesta jogada.
    placarPretas = str(game.placar["BLACK"])
    txt = font.render(placarPretas, 1, (20, 20, 20))
    pecaP = pygame.image.load(r'Sprites/Peca_preta_res.png')
    screen.blit(pecaP,(25, 75)) 
    screen.blit(txt,(75, 85)) 
    
    placarBrancas = str(game.placar["WHITE"])
    txt = font.render(placarBrancas, 1, (20, 20, 20))
    pecaB =  pygame.image.load(r'Sprites/Peca_branca_res.png')
    screen.blit(pecaB,(25, 125)) 
    screen.blit(txt,(75, 135))

    
#game = ReversiGame.ReversiGame()

# No display construiremos o tabuleiro juntamente com as pessas que forem setadas.
# É também escrita uma mensagem para avisar ao jogador que deverá passar a vez.
def display(game, todasPoss = []):
    
    background_display(game)
    

    #Aqui é desenhado o tabuleiro do jogo.
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
     
    # São desenhadas todas as possibilidades do jogador nesta jogada.
    for poss in todasPoss:
        screen.blit(possibilidades, ((200 + poss[0]*75), (75 + poss[1]*75))) 
     
    # Caso o jogador não seja capaz de realizada nenhuma jogada, será carregada uma mensagem.
    if(game.estado =="PASS"):
        passar = "Nenhuma jogada possível! Clicke para passar a jogada."
        txt = font.render(passar, 1, (145, 0, 0))
        text_rect = txt.get_rect(center=(500, 725))
        screen.blit(txt, text_rect)
    	
    pygame.display.update() 


# Cria-se a tela de selecionar nível, onde cada nível possuirá um valor.
def selecionar_nivel(game):
    screen.blit(backgroundReversi, (0, 0))

    screen.blit(dificuldade, (206, 50))

    screen.blit(botao_facil, (200, 200))
    screen.blit(botao_medio, (400, 200))
    screen.blit(botao_dificil, (600, 200))
    
    screen.blit(botao_jogar, (362, 450))
 


    #Dificuldade default
    dif = 4

    # Aqui o jogador poderá escolher a dificuldade do jogo.
    # Sendo: 2 - Fácil, 4 - Médio e 5 - difícil
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                screen.blit(backgroundReversi, (0, 0))
                screen.blit(dificuldade, (206, 50))
                screen.blit(botao_facil, (200, 200))
                screen.blit(botao_medio, (400, 200))
                screen.blit(botao_dificil, (600, 200))
                screen.blit(botao_jogar, (362, 450))
                X, Y = pygame.mouse.get_pos()
                if (X >= 200 and X <= 350 and Y >= 200 and Y <= 350):  
                    screen.blit(facil_selected, (199, 199))
                    dif = 2
                elif (X >= 400 and X <= 550 and Y >= 200 and Y <= 350):
                    screen.blit(medio_selected, (399, 199))
                    dif = 4
                elif(X >= 600 and X <= 750 and Y >= 200 and Y <= 350):
                    screen.blit(dificil_selected, (599, 199))
                    dif = 5
                elif(X >= 362 and X <= 612 and Y >= 450 and Y <= 570):
                    if(dif == 2):
                        screen.blit(facil_selected, (199, 199))
                    elif(dif == 4):
                        screen.blit(medio_selected, (399, 199))
                    else:
                        screen.blit(dificil_selected, (599, 199))
                    screen.blit(botao_jogar_click, (362, 450))
                    pygame.display.update()
                    time.sleep(0.2)
                    # O valor será passado como parâmetro para a função de interface do jogo.
                    reversiInterface(game, dif)
        
            pygame.display.update()
            
# Cria-se a tela de fim de jogo, onde o jogador escolhe se quer começar um jogo novo ou sair.
def game_over(game):
    screen.blit(backgroundReversi, (0, 0))

    screen.blit(fim_jogo, (206, 50))

    screen.blit(botao_jogar_novamente, (275, 350))
    screen.blit(botao_sair, (275, 500))

    screen.blit(peca_branca, (275, 250))
    screen.blit(peca_preta, (500, 250))

    # É mostrado o placar final e verificado qual das duas cores venceu o jogo.
    if game.placar["BLACK"] > game.placar["WHITE"]:
        texto = "PRETAS venceram!!"
        txt = font.render(texto, 1, (20, 20, 20))
        text_rect = txt.get_rect(center=(500, 200))
        screen.blit(txt, text_rect)
    else:
        texto = "BRANCAS venceram!!"
        txt = font.render(texto, 1, (20, 20, 20))
        text_rect = txt.get_rect(center=(500, 200))
        screen.blit(txt, text_rect)


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
                # Nesta opção o jogador poderá jogar um novo jogo.
                X, Y = pygame.mouse.get_pos()
                if (X >= 275 and X <= 725 and Y >= 350 and Y <= 450):               
                    screen.blit(botao_jogar_novamente_click, (275, 350))
                    pygame.display.update()
                    time.sleep(0.2)
                    # É criado um novo objeto game e é chamada a função de selecionar nível.
                    new_game = ReversiGame.ReversiGame()
                    selecionar_nivel(new_game)
                elif (X >= 275 and X <= 725 and Y >= 500 and Y <= 600):
                    # Nesta opção o jogo é fechado.
                    screen.blit(botao_sair_click, (275, 500))
                    pygame.display.update()
                    time.sleep(0.2)
                    pygame.quit()
                    
                
        pygame.display.update()

# Nesta função, é carregada a tela em que o jogador realizará as jogadas ao clicar nas posições.
def reversiInterface(game, dificuldade):
    display(game, game.getTodasPoss())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                if(game.estado !="FIN"):
                    X, Y = pygame.mouse.get_pos()
                    if Y <= 650 and Y >=75 and X <= 820 and X >= 200:
                        # Aqui será verificada qual linha e coluna o jogador escolheu.
                        i = floor((X-200)/75)
                        j = floor((Y-75)/75)

                    # O usuário é o primeiro a jogar.
                    if(game.jogar(i, j)):
                        display(game)
                        # Esta será a jogada da IA, e é passada a dificuldade (número de recursões).
                        jogadaAdv = MiniMax.escolheJogada(game, dificuldade)
                        game.jogar(jogadaAdv[0], jogadaAdv[1])
                        time.sleep(0.5)
                        display(game, game.getTodasPoss())
                
            #Caso o jogo chegue ao fim, será direcinado à tela de Game Over
            if(game.estado == "FIN"):
                time.sleep(2.0)
                game_over(game)

                    
# É criada a tela inicial do jogo.
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
                    screen.blit(botao_jogar_click, (375, 400))
                    pygame.display.update()
                    time.sleep(0.2)
                    selecionar_nivel(game)
        pygame.display.update()

tela_inicial()
print("FIM DE JOGO")

