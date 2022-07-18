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
        self.tabuleiro = []
        for i in range(8):
            #self.tabuleiro.append(random.choices(["WHITE", "BLACK", "BLANK"], k = 8))
            if(i < 3 or i > 4):
                self.tabuleiro.append(["BLANK"]*8)
            elif(i == 3):
                self.tabuleiro.append(["BLANK"]*3 + ["WHITE", "BLACK"] + ["BLANK"]*3)
            else:
                self.tabuleiro.append(["BLANK"]*3 + ["BLACK", "WHITE"] + ["BLANK"]*3)
        self.possPretas = []
        self.possBrancas = []
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


    def getTodasPoss(self, tipo):
        todasPoss = []
        for loc in self.alteradas:
            if(self.possJogar(loc[0], loc[1], tipo)):
                todasPoss.append(loc)
        return todasPoss


    def possLinha(self, x, y, desX, desY, tipo):
        neg = ReversiGame.negTipo(tipo)
        if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7)) or self.tabuleiro[x][y] != neg):
            return False
        
        while(self.tabuleiro[x][y] == neg):
            x, y = x + desX, y + desY
            if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7))):
                return False
        
        if(self.tabuleiro[x][y] == tipo):
            return True
        
        return False
    
    
    def possJogar(self, x, y, tipo):
        if(not self.tabuleiro[x][y] == "BLANK"):
            return False
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.possLinha(x+i, y+j, i, j, tipo)):
                    return True;
        return False
    
    
    def transformarLinha(self, x, y, desX, desY, tipo):     
            
        neg = ReversiGame.negTipo(tipo)
        if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7)) or self.tabuleiro[x][y] != neg):
            return False
        
        while(self.tabuleiro[x][y] == neg):
            x, y = x + desX, y + desY
            if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7))):
                return False
        
        if(self.tabuleiro[x][y] == tipo):
            x, y = x - desX, y - desY
            while(self.tabuleiro[x][y] == neg):
                self.tabuleiro[x][y] = tipo
                x, y = x - desX, y - desY

    
    def jogar(self, x, y, tipo):
        if(not self.possJogar(x, y, tipo)):
            print("Jogada Inválida! Tente novamente")
            return False
            
        self.tabuleiro[x][y] = tipo
        self.alteradas.discard((x, y))
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.tabuleiro[x+i][y+j] == "BLANK"):
                    self.alteradas.add((x+i, y+j))
                self.transformarLinha(x+i, y+j, i, j, tipo)
        
        self.tipoJog = ReversiGame.negTipo(self.tipoJog)
        return True
        

    def main(self):                        
        
        while(True):
            poss = self.getTodasPoss(self.tipoJog)
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
            
            self.jogar(x, y, self.tipoJog)


#game = ReversiGame()

#game.main()
