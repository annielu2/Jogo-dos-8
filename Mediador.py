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

tipoIA = "WHITE"

def jogaAleatorio(possibilidades):
    if(len(possibilidades) == 0):
        return (-1, -1)
    return random.choice(possibilidades)

def joga(jogada, game):
    game.jogar(jogada[0], jogada[1])

def avaliaJogo(game):
    if(game.estado == "FIN"):
        return 100*(game.placar[tipoIA] - game.placar[ReversiGame.ReversiGame.negTipo(tipoIA)])
    
    if(game.tipoJog == tipoIA):
        return len(game.getTodasPoss())*game.placar[tipoIA] - game.placar[ReversiGame.ReversiGame.negTipo(tipoIA)]
    else:
        return game.placar[tipoIA] - len(game.getTodasPoss())*game.placar[ReversiGame.ReversiGame.negTipo(tipoIA)]
    

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
            
