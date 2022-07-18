#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ReversiGame.py
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
class ReversiGame:
    
    def __init__(self):
        self.tipoJog = "BLACK"
        self.estado = "NORMAL"
        
        self.placar = {"WHITE": 2,
                       "BLACK": 2,
                       "BLANK": 60} 
        
        self.tabuleiro = []
        for i in range(8):
            if(i < 3 or i > 4):
                self.tabuleiro.append(["BLANK"]*8)
            elif(i == 3):
                self.tabuleiro.append(["BLANK"]*3 + ["WHITE", "BLACK"] + ["BLANK"]*3)
            else:
                self.tabuleiro.append(["BLANK"]*3 + ["BLACK", "WHITE"] + ["BLANK"]*3)
        
        
        self.alteradas = {(2, 2), (2, 3), (2, 4), (2, 5),
                          (3, 2), (3, 5),
                          (4, 2), (4, 5),
                          (5, 2), (5, 3), (5, 4), (5, 5)}
    
    @staticmethod
    def negTipo(tipo):
        if(tipo == "WHITE"):
            return "BLACK"
        else:
            return "WHITE"


    def transformaPeca(self, x, y):
        self.tabuleiro[x][y] = self.tipoJog
        self.placar[self.tipoJog] += 1
        self.placar[ReversiGame.negTipo(self.tipoJog)] -= 1 

    def getTodasPoss(self):
        todasPoss = []
        for loc in self.alteradas:
            if(self.possJogar(loc[0], loc[1])):
                todasPoss.append(loc)
        if(len(todasPoss) == 0):
            if(self.estado == "NORMAL"):
                self.estado = "PASS"
            else:
                self.estado = "FIN"
        return todasPoss


    def possLinha(self, x, y, desX, desY):
        neg = ReversiGame.negTipo(self.tipoJog)
        if(self.tabuleiro[x][y] != neg):
            return False
        
        while(self.tabuleiro[x][y] == neg):
            x, y = x + desX, y + desY
            if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7))):
                return False
        
        if(self.tabuleiro[x][y] == self.tipoJog):
            return True
        
        return False
    
    
    def possJogar(self, x, y):
        if(not self.tabuleiro[x][y] == "BLANK"):
            return False
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x+i >= 0 and y+j >= 0) and (x+i <= 7 and y+j <= 7)):
                    if(self.possLinha(x+i, y+j, i, j)):
                        return True;
        return False
    
    
    def transformarLinha(self, x, y, desX, desY):     
            
        neg = ReversiGame.negTipo(self.tipoJog)
        if(self.tabuleiro[x][y] != neg):
            return False
        
        while(self.tabuleiro[x][y] == neg):
            x, y = x + desX, y + desY
            if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7))):
                return False
        
        if(self.tabuleiro[x][y] == self.tipoJog):
            x, y = x - desX, y - desY
            while(self.tabuleiro[x][y] == neg):
                self.transformaPeca(x, y)
                x, y = x - desX, y - desY

    
    def jogar(self, x, y):
        if(not self.possJogar(x, y)):
            return False
            
        self.tabuleiro[x][y] = self.tipoJog
        self.alteradas.discard((x, y))
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x+i >= 0 and y+j >= 0) and (x+i <= 7 and y+j <= 7)):
                    if(self.tabuleiro[x+i][y+j] == "BLANK"):
                        self.alteradas.add((x+i, y+j))
                    self.transformarLinha(x+i, y+j, i, j)
        
        self.tipoJog = ReversiGame.negTipo(self.tipoJog)
        return True
        

    def main(self):                        
        
        while(True):
            poss = self.getTodasPoss()
            for i in range(8):
                for j in range(8):
                    if(self.tabuleiro[i][j] == "WHITE"):
                        print("●" , end = ' ')
                    elif(self.tabuleiro[i][j] == "BLACK"):
                        print("○", end = ' ')
                    elif ((i,j) in poss):
                        print("⧈", end = ' ') #⧈
                    else:
                        print("⛶", end = ' ') #⧈
                    
                print()
            
            if(self.tipoJog == "BLACK"):
                x, y = map(int, input("[PRETAS]Digite as coordenadas: ").split())
            else:
                x, y = map(int, input("[BRANCAS]Digite as coordenadas: ").split())
            
            if(not self.jogar(x, y)):
                print("Jogada Inválida! Tente novamente")


#game = ReversiGame()

#game.main()
