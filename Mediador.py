#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Mediador.py
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

'''
    Este arquivo contém as funções e as variáveis utilizadas para adaptar
a IA (MinMax ou outras) para o jogo Reversi. Ela é utilizada para que possamos
reutilizar ambos dos códigos (IA e Reversi).
'''

import random
import ReversiGame

#Define os pesos de cada posição.
pesos = [
        [120, -20, 20, 5],
        [-20, -40, -5, -5],
        [20, -5, 15, 3],
        [5, -5, 3, 3]
        ]

#Define a constate de peso das possibilidades.
pesoPoss = 0.5

#Define o tipo de peça da IA(cor).
tipoIA = "WHITE"

#Joga em uma posição aleatória (para debug).
def jogaAleatorio(possibilidades):
    if(len(possibilidades) == 0):
        return (-1, -1)
    return random.choice(possibilidades)


#Joga a posição dada no jogo dado.
def joga(jogada, game):
    game.jogar(jogada[0], jogada[1])


#Avalia o potencial da determinada configuração do jogo. 
def avaliaJogo(game):    
    aval = 0
    avalPoss = -400
    
    #Soma os pesos de cada peça (IA como positivas e do adversário como negativas)
    for i in range(8):
        for j in range(8):
            if(game.tabuleiro[i][j] == tipoIA):
                aval += pesos[i][j]
            elif(game.tabuleiro[i][j] == ReversiGame.ReversiGame.negTipo(tipoIA)):
                aval -= pesos[i][j]
    
    #O fim de jogo, positivo ou negativo, vale mais que a soma dos pesos.
    if(game.estado == "FIN"):
        return 500*(game.placar[tipoIA] - game.placar[ReversiGame.ReversiGame.negTipo(tipoIA)])
    
    #Encontra a melhor possibilidade para a avaliação
    for poss in game.getTodasPoss():
    	avalPoss = max(avalPoss, pesos[poss[0]][poss[1]])
    
    #Calcula e retorna a avaliação (pesos das posições + peso da melhor possibilidade)
    if(game.tipoJog == tipoIA):
        return aval + pesoPoss * avalPoss
    else:
        return aval - pesoPoss * avalPoss
    

#retorna as possibilidades de determinado jogo.
#Retorna um 'movimento básico' caso seja necessário passar a vez
def getPoss(game):
    if(len(game.getTodasPoss()) == 0):
        return [(4,4)]
    else:
        return game.getTodasPoss();
    

#Clona o jogo e retorna. Usado para iterar na árvore.
def cloneGame(game):
    clone = ReversiGame.ReversiGame()
    clone.tipoJog = game.tipoJog
    clone.estado = game.estado
    
    clone.placar["BLACK"] = game.placar["BLACK"]
    clone.placar["WHITE"] = game.placar["WHITE"]
    clone.placar["BLANK"] = game.placar["BLANK"]
    
    for i in range(8):
        for j in range(8):
            clone.tabuleiro[i][j] = game.tabuleiro[i][j]
    
    clone.alteradas.clear()
    for alt in game.alteradas:
        clone.alteradas.add(alt)
    
    return clone
      

#Espelha a matriz de pesos duas vezes. (De 4x4 para 8x8).
for i in range(4):
    pesos[i] = pesos[i] + list(reversed(pesos[i]))

for i in range(3, -1, -1):
    pesos.append(pesos[i])

