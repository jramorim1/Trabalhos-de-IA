from random import choice
from board import *
from math import inf
from tkinter import * 


class jogo():
    
    def __init__(self):
        
        self.humano = 1 #Identificação dos jogadores
        self.pc = -1
        self.board = board()
        
    
    def fimDeJogo(self):
        
        return self.board.estadoVencedor(self.humano) or self.board.estadoVencedor(self.pc)
    
    def avaliação(self):
        
        if self.board.estadoVencedor(self.humano):
            aval = -1
            
        elif self.board.estadoVencedor(self.pc):
            aval = 1
        
        else:
            aval = 0
            
        return aval
    
    def miniMax(self, profundidade, jogador):
        
        if jogador == self.pc:
            melhor = [-1,-1,-inf]
            
        elif jogador == self.humano:
            melhor = [-1,-1,+inf]
            
        if profundidade == 0 or self.fimDeJogo():
            return [-1,-1,self.avaliação()]
            
        for posVazia in self.board.empty():
            Z=0
            x,y = posVazia[0],posVazia[1]
            self.board.estado[x][y]=jogador
            parcial = self.miniMax(profundidade-1,-jogador)
            if self.board.estadoVencedor(self.pc):
                Z = 1
            self.board.estado[x][y]=0
            parcial[0],parcial[1] = x,y
            
            if jogador == self.pc:
                if Z == 1:
                    melhor = parcial
                elif parcial[2] > melhor[2]:
                    melhor = parcial
            else:
                if parcial[2] < melhor[2]:
                    melhor = parcial
       
        return melhor
    
    def vezPC(self):
        
        profundidade = len(self.board.empty())
        if profundidade == 0 or self.fimDeJogo():
            return
        
        elif profundidade == 9:
            x = choice([0,1,2])
            y = choice([0,1,2])
        else:
            movimento = self.miniMax(profundidade, self.pc)
            x,y = movimento[0],movimento[1]
        
        self.board.marcarPosicao(x,y,self.pc)
        
    def vezHumano(self, janela, x, y):
        
        profundidade = len(self.board.empty())
        if profundidade == 0 or self.fimDeJogo():
            return
        
        self.board.estado[x][y] = self.humano
        
        
                
        