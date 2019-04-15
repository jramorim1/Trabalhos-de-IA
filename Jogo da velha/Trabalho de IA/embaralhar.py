import numpy as np

def embaralhar():
    start = [[0,1,2],[3,4,5],[6,7,8]]
    
    for count in range(0,500):
        b = np.random.choice(range(0,4),1)
        if(b==0):
            start=cima(start)
        if(b==1):
            start=baixo(start)
        if(b==2):
            start=esquerda(start)
        if(b==3):
            start=direita(start)
      
    return start
    
def cima(pos):
   
    for l in range(0,3):
        for c in range(0,3):
            if(pos[l][c] == 0):
                i = l
                j = c
    if(i>0):
        aux = pos[i-1][j]
        pos[i][j] = aux
        pos[i-1][j] = 0
    
    return pos        
        
def baixo(pos):
    
    for l in range(0,3):
        for c in range(0,3):
            if(pos[l][c] == 0):
                i = l
                j = c
    if(i<2):
        aux = pos[i+1][j]
        pos[i][j] = aux
        pos[i+1][j] = 0
    
    return pos  
    
def esquerda(pos):

    for l in range(0,3):
        for c in range(0,3):
            if(pos[l][c] == 0):
                i = l
                j = c
    if(j>0):
        aux = pos[i][j-1]
        pos[i][j] = aux
        pos[i][j-1] = 0
    
    return pos  
    

def direita(pos):

    for l in range(0,3):
        for c in range(0,3):
            if(pos[l][c] == 0):
                i = l
                j = c
    if(j<2):
        aux = pos[i][j+1]
        pos[i][j] = aux
        pos[i][j+1] = 0
    
    return pos
