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
        
        #variáveis de estado do jogo (quem joga e como está o jogo)
        self.tipoJog = "BLACK"
        self.estado = "NORMAL"
        
        #guarda a quantidade de peças de cada jogador 
        self.placar = {"WHITE": 2,
                       "BLACK": 2,
                       "BLANK": 60} 
        
        #lista de possibilidades
        self.todasPoss = []
        
        #cria o tabuleiro e estabelece a configuração inicial
        self.tabuleiro = []
        for i in range(8):
            if(i < 3 or i > 4):
                self.tabuleiro.append(["BLANK"]*8)
            elif(i == 3):
                self.tabuleiro.append(["BLANK"]*3 + ["WHITE", "BLACK"] + ["BLANK"]*3)
            else:
                self.tabuleiro.append(["BLANK"]*3 + ["BLACK", "WHITE"] + ["BLANK"]*3)
        
        
        #guarda quais espaços são potenciais jogadas
        self.alteradas = {(2, 2), (2, 3), (2, 4), (2, 5),
                          (3, 2), (3, 5),
                          (4, 2), (4, 5),
                          (5, 2), (5, 3), (5, 4), (5, 5)}
        
        #já descobre as possibilidades do primeiro a jogar na criação do jogo
        self.setTodasPoss();
    
    
    #Função auxiliar para descobrir o tipo do adversário.
    # Para melhor leitura. 
    @staticmethod
    def negTipo(tipo):
        if(tipo == "WHITE"):
            return "BLACK"
        else:
            return "WHITE"
    
    
    #Função para mudar a cor de uma peça ou  coloca ela num espaço em branco.
    def transformaPeca(self, x, y):
        self.placar[self.tipoJog] += 1
        if(self.tabuleiro[x][y] == "BLANK"):
            self.placar["BLANK"] -= 1
        else:
            self.placar[ReversiGame.negTipo(self.tipoJog)] -= 1 
        self.tabuleiro[x][y] = self.tipoJog


    #Retorna as possibilidades do jogador(lista de tuplas)
    def getTodasPoss(self):
        return self.todasPoss
    
    
    #Descobre todas as possibilidades que o jogador atual tem.
    # Se as possibilidade são zero, muda o estado do jogo (pular vez ou finalizar)
    def setTodasPoss(self):
        self.todasPoss.clear()
        for loc in self.alteradas:
            if(self.possJogar(loc[0], loc[1])):
                self.todasPoss.append(loc)
        
        #Altera o estado do jogo (passa a vez ou finaliza)
        if(len(self.todasPoss) == 0):
            if(self.estado == "NORMAL" and self.placar["BLANK"] > 0):
                self.estado = "PASS"
            else:
                self.estado = "FIN"
        else:
            self.estado = "NORMAL"
    
    
    #Checa se a linha de algum dos oito vizinhos da peça define uma possibilidade.
    # Uma peça do jogador após N do adversário, sem nenhum epaço em branco entre elas.
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
    
    
    #Checa se aquele espaço em branco pode ser jogado.
    # Testa todas as oito linhas que podem definir uma possibilidade.
    def possJogar(self, x, y):
        if(not self.tabuleiro[x][y] == "BLANK"):
            return False
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x+i >= 0 and y+j >= 0) and (x+i <= 7 and y+j <= 7)):
                    if(self.possLinha(x+i, y+j, i, j)):
                        return True;
        return False
    
    
    #Trasforma todas as peças do adversário na linha para suas
    # Usado quando as peças são viradas em uma jogada.
    def transformarLinha(self, x, y, desX, desY):     
        neg = ReversiGame.negTipo(self.tipoJog)
        if(self.tabuleiro[x][y] != neg):
            return False
        
        #caminha nas peças do adversário até encontrar uma peça do jogador.
        while(self.tabuleiro[x][y] == neg):
            x, y = x + desX, y + desY
            if(not((x >= 0 and y >= 0) and (x <= 7 and y <= 7))):
                return False
                
        #volta até o início trocando a cor das peças.
        if(self.tabuleiro[x][y] == self.tipoJog):
            x, y = x - desX, y - desY
            while(self.tabuleiro[x][y] == neg):
                self.transformaPeca(x, y)
                x, y = x - desX, y - desY

    
    #Função para a jogadas. Joga em uma posição, troca de jogador
    ## e calcula novas possibilidades.
    #Recebe uma tupla como posição e retorna um bool dizendo se a jogada foi válida.
    def jogar(self, x, y):
        #Se for a passada de vez, qualquer entrada passa de vez.
        if(self.estado == "PASS"):
            self.tipoJog = ReversiGame.negTipo(self.tipoJog)
            self.setTodasPoss()
            return True
        
        #Se não for possível jogar, retorna falso.
        if(not self.possJogar(x, y)):
            return False
            
        #Coloca a peça no lugar.
        self.transformaPeca(x, y)
        
        #Altera as potenciais jogadas.
        self.alteradas.discard((x, y))
        
        #Altera as linhas.
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x+i >= 0 and y+j >= 0) and (x+i <= 7 and y+j <= 7)):
                    if(self.tabuleiro[x+i][y+j] == "BLANK"):
                        self.alteradas.add((x+i, y+j))
                    self.transformarLinha(x+i, y+j, i, j)
        
        
        #Altera o jogador atual e calcula as possibilidades dele.
        self.tipoJog = ReversiGame.negTipo(self.tipoJog)
        self.setTodasPoss()
        
        #Se tudo acontecer bem, retorna True.
        return True
        

    #Função para testar o funcionamento do jogo em terminal.
    # Diretamente do back-end
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


##USADO PARA TESTES. DESCOMENTE PARA JOGAR NO TERMINAL.

#game = ReversiGame()
#game.main()
