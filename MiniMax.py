#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MiniMax.py
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
import Mediador 



infit = 1000000 #Placeholder para inito
#maxRec = 4      #Número máximo de recursão.



#Função que escolhe a jogada. Resultado do MiniMax.
def escolheJogada(game, maxRec):
    possibilidades = Mediador.getPoss(game)
    
    possMax = -infit
    alpha = -infit
    beta = infit
    
    #O melhor 'galho' da árvore é o escolhido.
    for poss in possibilidades:
        auxMax = miniMax("MINI", 1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
        if(auxMax > possMax):
            possMax = auxMax
            movimento = poss
    
    return movimento


#Função MiniMax para escolher a melhor jogada.
def miniMax(tipo, rec, poss, game, alpha, beta, maxRec):
    
    #Faz a jogada.
    Mediador.joga(poss, game)
    
    #Se for a última recursão, avalia o estado.
    if(rec >= maxRec):
        return Mediador.avaliaJogo(game)
    
    #Considera as próximas possibilidades.
    possibilidades = Mediador.getPoss(game)
    
    #Se for necessário passa a vez, passa de nível diretamente
    if(len(possibilidades) == 0):
        if(tipo == "MAX"):
            return miniMax("MINI", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
        else:
            return miniMax("MAX", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
    
    #Executa a recursão de maximação.
    if(tipo == "MAX"):
        possMax = -infit
        for poss in possibilidades:
            auxMax = miniMax("MINI", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
            possMax = max(possMax, auxMax)
            
            alpha = max(alpha, auxMax)
            if(beta <= alpha):
                break
                
        return possMax
    
    
    #Executa a recursão de minimazação
    elif(tipo == "MINI"):
        possMini = infit
        for poss in possibilidades:
            auxMini = miniMax("MAX", rec+1, poss, Mediador.cloneGame(game), alpha, beta, maxRec)
            possMini = min(possMini, auxMini)
            
            beta = min(beta, auxMini)
            if(beta <= alpha):
                break
    
        return possMini
        

