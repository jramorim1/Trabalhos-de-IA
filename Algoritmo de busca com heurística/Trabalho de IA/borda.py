class Borda:
    def __init__(self, no):
        self.b = [no]
       
    def vazia(self):
        if not self.b:
            return False
        return True
    
    def retirar(self):
        c = len(self.b)
        min = 100000
        
        v=0
        
        for i in range(0,c):
            if min>self.b[i].h + self.b[i].pr:
                min = self.b[i].h + self.b[i].pr
                v=i
                
        return self.b.pop(v)
            
    
    def addNodes(self,nodesList):
        self.b = nodesList + self.b
            