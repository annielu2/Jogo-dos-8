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
import random
import ReversiGame

pesos = [
        [120, -20, 20, 5],
        [-20, -40, -5, -5],
        [20, -5, 15, 3],
        [5, -5, 3, 3]
        ]

pesoPoss = 1

tipoIA = "WHITE"

def jogaAleatorio(possibilidades):
    if(len(possibilidades) == 0):
        return (-1, -1)
    return random.choice(possibilidades)

def joga(jogada, game):
    game.jogar(jogada[0], jogada[1])

def avaliaJogo(game):    
    aval = 0
    avalPoss = 0
    
    for i in range(8):
        for j in range(8):
            if(game.tabuleiro[i][j] == tipoIA):
                aval += pesos[i][j]
            elif(game.tabuleiro[i][j] == ReversiGame.ReversiGame.negTipo(tipoIA)):
                aval -= pesos[i][j]
    
    
    for poss in game.getTodasPoss():
    	avalPoss += pesos[poss[0]][poss[1]]
    
    
    if(game.tipoJog == tipoIA):
        return aval + pesoPoss * avalPoss
    else:
        return aval - pesoPoss * avalPoss
    

def getPoss(game):
    return game.getTodasPoss();
    
    
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
      
      
for i in range(4):
    pesos[i] = pesos[i] + list(reversed(pesos[i]))

for i in range(3, -1, -1):
    pesos.append(pesos[i])

