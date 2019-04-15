class n:
    def __init__(self,matriz,pai,pronfundidade): #Custo Unitário
        self.m = matriz
        self.p = pai
        self.h = 0
        self.pr = pronfundidade
    
    def test_obj(self):
        matriz = [[0,1,2],[3,4,5],[6,7,8]]
        if matriz.copy() == self.m.copy():
            return True
        return False
    
    def manhattan(self):
      #  print("HEURISTICA")
       # print(self.m)
        for i in range(0,3):
            for j in range(0,3):
                if(self.m[i][j] == 1):
                    self.h = self.h + abs(i) + abs(j-1)
                 #   print(self.h)
                 #   input()
                if(self.m[i][j] == 2):
                    self.h = self.h + abs(i) + abs(j-2)
                 #   print(self.h)
                  #  input()
                if(self.m[i][j] == 3):
                    self.h = self.h + abs(i-1) + abs(j)
                 #   print(self.h)
                #   input()
                if(self.m[i][j] == 4):
                    self.h = self.h + abs(i-1) + abs(j-1)
                  #  print(self.h)
                  #  input()
                if(self.m[i][j] == 5):
                    self.h = self.h + abs(i-1) + abs(j-2)
                  #  print(self.h)
                   # input()
                if(self.m[i][j] == 6):
                    self.h = self.h + abs(i-2) + abs(j)
                  #  print(self.h)
                  #  input()
                if(self.m[i][j] == 7):
                    self.h = self.h + abs(i-2) + abs(j-1)
                  #  print(self.h)
                   # input()
                if(self.m[i][j] == 8):
                    self.h = self.h + abs(i-2) + abs(j-2)
                   # print(self.h)
                   # input()
    
    def funcao_sucessora(self):
        
        for i in range(0,3):
            for j in range(0,3):
                if self.m[i][j] == 0:
                    l=i
                    c=j
        matriz1 = [[0,0,0],[0,0,0],[0,0,0]]
        matriz2 = [[0,0,0],[0,0,0],[0,0,0]]
        matriz3 = [[0,0,0],[0,0,0],[0,0,0]]
        matriz4 = [[0,0,0],[0,0,0],[0,0,0]]
           
        for i in range(0,3):
            for j in range(0,3):
                
                matriz1[i][j] = self.m[i][j]
                matriz2[i][j] = self.m[i][j]
                matriz3[i][j] = self.m[i][j]
                matriz4[i][j] = self.m[i][j]
        
        if (l==0) and (c==0):
            #Primeiro Estado
            aux = matriz1[0][1]
            matriz1[0][1] = 0
            matriz1[0][0] = aux

            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[1][0]
            matriz2[1][0] = 0
            matriz2[0][0] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            return [node1,node2]
        
        if (l==0) and (c==1):
            #Primeiro Estado
            aux = matriz1[0][0]
            matriz1[0][0] = 0
            matriz1[0][1] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[0][2]
            matriz2[0][2] = 0
            matriz2[0][1] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            #Terceiro Estado
            aux = matriz3[1][1]
            matriz3[1][1] = 0
            matriz3[0][1] = aux
            
            node3 = n(matriz3,self,self.pr+1)
            node3.manhattan()
            
            return [node1,node2,node3]
        
        if (l==0) and (c==2):
            #Primeiro Estado
            aux = matriz1[0][1]
            matriz1[0][1] = 0
            matriz1[0][2] = aux
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[1][2]
            matriz2[1][2] = 0
            matriz2[0][2] = aux
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            return [node1,node2]
        
        if (l==1) and (c==0):
            #Primeiro Estado
            aux = matriz1[0][0]
            matriz1[0][0] = 0
            matriz1[1][0] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[1][1]
            matriz2[1][1] = 0
            matriz2[1][0] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            #Terceiro Estado
            aux = matriz3[2][0]
            matriz3[2][0] = 0
            matriz3[1][0] = aux
            
            node3 = n(matriz3,self,self.pr+1)
            node3.manhattan()
            
            return [node1,node2,node3]
        
        if (l==1) and (c==1):
            #Primeiro Estado
            aux = matriz1[1][0]
            matriz1[1][0] = 0
            matriz1[1][1] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[0][1]
            matriz2[0][1] = 0
            matriz2[1][1] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            #Terceiro Estado
            aux = matriz3[1][2]
            matriz3[1][2] = 0
            matriz3[1][1] = aux
            
            node3 = n(matriz3,self,self.pr+1)
            node3.manhattan()
            
            #Quarto Estado
            aux = matriz4[2][1]
            matriz4[2][1] = 0
            matriz4[1][1] = aux
            
            node4 = n(matriz4,self,self.pr+1)
            node4.manhattan()
            
            return [node1,node2,node3,node4]
        
        if (l==1) and (c==2):
            #Primeiro Estado
            aux = matriz1[0][2]
            matriz1[0][2] = 0
            matriz1[1][2] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[1][1]
            matriz2[1][1] = 0
            matriz2[1][2] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            #Terceiro Estado
            aux = matriz3[2][2]
            matriz3[2][2] = 0
            matriz3[1][2] = aux
            
            node3 = n(matriz3,self,self.pr+1)
            node3.manhattan()
            
            return [node1,node2,node3]
        
        if (l==2) and (c==0):
            #Primeiro Estado
            aux = matriz1[1][0]
            matriz1[1][0] = 0
            matriz1[2][0] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[2][1]
            matriz2[2][1] = 0
            matriz2[2][0] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            return [node1,node2]
        
        if (l==2) and (c==1):
            #Primeiro Estado
            aux = matriz1[2][0]
            matriz1[2][0] = 0
            matriz1[2][1] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[1][1]
            matriz2[1][1] = 0
            matriz2[2][1] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            #Terceiro Estado
            aux = matriz3[2][2]
            matriz3[2][2] = 0
            matriz3[2][1] = aux
            
            node3 = n(matriz3,self,self.pr+1)
            node3.manhattan()
            
            return [node1,node2,node3]
        
        if (l==2) and (c==2):
            #Primeiro Estado
            aux = matriz1[2][1]
            matriz1[2][1] = 0
            matriz1[2][2] = aux
            
            node1 = n(matriz1,self,self.pr+1)
            node1.manhattan()
            
            #Segundo Estado
            aux = matriz2[1][2]
            matriz2[1][2] = 0
            matriz2[2][2] = aux
            
            node2 = n(matriz2,self,self.pr+1)
            node2.manhattan()
            
            return [node1,node2]
                
                
        
        