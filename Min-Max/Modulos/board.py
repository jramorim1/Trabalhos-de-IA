class board():
    
    def __init__(self):
        
        self.estado = [[0,0,0],[0,0,0],[0,0,0]]
        
    def empty(self): #Retorna as uma lista com as posições livres
        
        livres = []
        
        for i in range(0,3):
            for j in range(0,3):
                if(self.estado[i][j] == 0):
                    livres.append([i, j])
        
        return livres 
    
    def movimentoValido(self,x,y): #Verifica se o movimento é válido
        
        if((x<0 and x>2) and (y<0 and y>2)):
            return False
        
        if self.estado[x][y] == 0:
            return True

        return False
    
    def marcarPosicao(self,x,y,jogador): #Marca a posição escolhida pelo jogador
        
        if self.movimentoValido(x,y):
            self.estado[x][y] = jogador
            return True
        
        else:
            print("Movimento Inválido")
            return False
    
    def estadoVencedor(self,jogador): #Verifica se o jogador venceu
        
        estadosVencedores = [
        [self.estado[0][0], self.estado[0][1], self.estado[0][2]],
        [self.estado[1][0], self.estado[1][1], self.estado[1][2]],
        [self.estado[2][0], self.estado[2][1], self.estado[2][2]],
        [self.estado[0][0], self.estado[1][0], self.estado[2][0]],
        [self.estado[0][1], self.estado[1][1], self.estado[2][1]],
        [self.estado[0][2], self.estado[1][2], self.estado[2][2]],
        [self.estado[0][0], self.estado[1][1], self.estado[2][2]],
        [self.estado[2][0], self.estado[1][1], self.estado[0][2]],]
        
        
        if [jogador,jogador,jogador] in estadosVencedores:
            return True
        
        return False
    
  
    
    
    
            
        
    
    