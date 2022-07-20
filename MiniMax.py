#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MiniMax.py
#  
#  Copyright 2022 João Paulo Paiva Lima <joao.lima1@estudante.ufla.br>
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
import Mediador 


maxRec = 4

def escolheJogada(game):
    possibilidades = Mediador.getPoss(game)
    
    possMax = -64
    movimento = (-1, -1)
    
    for poss in possibilidades:
        auxMax = miniMax("MINI", 1, poss, Mediador.cloneGame(game))
        if(auxMax > possMax):
            possMax = auxMax
            movimento = poss
    
    return movimento



def miniMax(tipo, rec, poss, game):
    if(rec >= maxRec):
        return Mediador.avaliaJogo(game)
    
    
    Mediador.joga(poss, game)
    possibilidades = Mediador.getPoss(game)
    
    if(tipo == "MAX"):
        possMax = -64
        for poss in possibilidades:
            auxMax = miniMax("MINI", rec+1, poss, Mediador.cloneGame(game))
            if(auxMax > possMax):
                possMax = auxMax
                
        return possMax
                
    elif(tipo == "MINI"):
        possMini = 64
        for poss in possibilidades:
            auxMini = miniMax("MAX", rec+1, poss, Mediador.cloneGame(game))
            if(auxMini < possMini):
                possMini = auxMini
        
        return possMini
        
