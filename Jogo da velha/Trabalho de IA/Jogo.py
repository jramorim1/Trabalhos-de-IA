import numpy as np 
import time

from borda import *
from node import *
from embaralhar import *

from tkinter import * 

nodosPesquisados = []
EI = None
borda = None
k = None
Y = 0
ordem = []

def emb():
    
    global EI
    global k
    global borda
    global nodosPesquisados
    global Y
    global ordem
    
    ordem = []
    Y = 0
    nodosPesquisados = []
    EI = None
    borda = None
    k = None

    EI = embaralhar()

    if(EI[0][0]==0):
        a = ""
    else:
        a = EI[0][0]
    
    lb1 = Label(janela, text=a,width='2')
    lb1.config(font=("Arial", 20))
    lb1.place(x=130, y=125)
    
    if(EI[0][1]==0):
        a = ""
    else:
        a = EI[0][1]
    
    lb2 = Label(janela, text=a,width='2')
    lb2.config(font=("Arial", 20))
    lb2.place(x=280, y=125)
    
    if(EI[0][2]==0):
        a = ""
    else:
        a = EI[0][2]
        
    lb3 = Label(janela, text=a,width='2')
    lb3.config(font=("Arial", 20))
    lb3.place(x=430, y=125)
    
    if(EI[1][0]==0):
        a = ""
    else:
        a = EI[1][0]
    
    lb4 = Label(janela, text=a,width='2')
    lb4.config(font=("Arial", 20))
    lb4.place(x=130, y=280)
    
    if(EI[1][1]==0):
        a = ""
    else:
        a = EI[1][1]
    
    lb5 = Label(janela, text=a ,width='2')
    lb5.config(font=("Arial", 20))
    lb5.place(x=280, y=280)
    
    if(EI[1][2]==0):
        a = ""
    else:
        a = EI[1][2]
    
    lb6 = Label(janela, text=a,width='2')
    lb6.config(font=("Arial", 20))
    lb6.place(x=430, y=280)
    
    if(EI[2][0]==0):
        a = ""
    else:
        a = EI[2][0]
        
    lb7 = Label(janela, text=a,width='2')
    lb7.config(font=("Arial", 20))
    lb7.place(x=130, y=430)
    
    if(EI[2][1]==0):
        a = ""
    else:
        a = EI[2][1]
    
    lb8 = Label(janela, text=a,width='2')
    lb8.config(font=("Arial", 20))
    lb8.place(x=280, y=430)
    
    if(EI[2][2]==0):
        a = ""
    else:
        a = EI[2][2]
        
    lb9 = Label(janela, text=a,width='2')
    lb9.config(font=("Arial", 20))
    lb9.place(x=430, y=430)
    
    textBox = Text(janela, height=2, width=22,font=("Helvetica", 10))
    textBox.insert(INSERT, "Busque uma Solução")
    textBox.place(x=535,y=350)
    
def bus():
    
    global EI
    global k
    global borda
    global nodosPesquisados
   
    node = n(EI,False,0) #Criação do primeiro Nó (Estado Inicial)
    
    borda = Borda(node) #Inserção do estado inicial na Borda

    textBox = Text(janela, height=2, width=22,font=("Helvetica", 10))
    textBox.insert(INSERT, "Buscando Solução...\nAguarde.")
    textBox.place(x=535,y=350)
    janela.update()
    
    while(1):
    
        k = borda.retirar()
    
        nodosPesquisados = nodosPesquisados + [k]
    
        if(k.test_obj()):
            break
    
        neighbor = k.funcao_sucessora()
    
        c = len(neighbor)
        z = len(nodosPesquisados)
   
        for v in range(0,z):
            h=0
            d=0
            for l in range(0,c):
                if(neighbor[h].m == nodosPesquisados[v].m):
                    neighbor.pop(h)
                    h = h-1
                    d = d + 1
                h = h+1
        
            c=c-d

        borda.addNodes(neighbor)
     
    textBox = Text(janela, height=2, width=22,font=("Helvetica", 10))
    textBox.insert(INSERT, "Solução Encontrada.\nVerifique os Passos.")
    textBox.place(x=535,y=350)
    
def prox():
    global EI
    global k
    global borda
    global nodosPesquisados
    global Y
    global ordem
       
 
        
    if(Y<1):
        while(k.p):
            ordem = ordem + [k]
            k=k.p
        ordem = ordem[::-1]
    
    tam = len(ordem)

    if(Y < tam):
        
        if(ordem[Y].m[0][0]==0):
            a = ""
        else:
            a = ordem[Y].m[0][0]

        lb1 = Label(janela, text=a,width='2')
        lb1.config(font=("Arial", 20))
        lb1.place(x=130, y=125)
    
        if(ordem[Y].m[0][1]==0):
            a = ""
        else:
            a = ordem[Y].m[0][1]
    
        lb2 = Label(janela, text=a,width='2')
        lb2.config(font=("Arial", 20))
        lb2.place(x=280, y=125)
        
        if(ordem[Y].m[0][2]==0):
            a = ""
        else:
            a = ordem[Y].m[0][2]
        
        lb3 = Label(janela, text=a,width='2')
        lb3.config(font=("Arial", 20))
        lb3.place(x=430, y=125)
        
        if(ordem[Y].m[1][0]==0):
            a = ""
        else:
            a = ordem[Y].m[1][0]
            
        lb4 = Label(janela, text=a,width='2')
        lb4.config(font=("Arial", 20))
        lb4.place(x=130, y=280)
        
        if(ordem[Y].m[1][1]==0):
            a = ""
        else:
            a = ordem[Y].m[1][1]
            
        lb5 = Label(janela, text=a ,width='2')
        lb5.config(font=("Arial", 20))
        lb5.place(x=280, y=280)
            
        if(ordem[Y].m[1][2]==0):
            a = ""
        else:
            a = ordem[Y].m[1][2]
                
        lb6 = Label(janela, text=a,width='2')
        lb6.config(font=("Arial", 20))
        lb6.place(x=430, y=280)
        
        if(ordem[Y].m[2][0]==0):
            a = ""
        else:
            a = ordem[Y].m[2][0]
                    
        lb7 = Label(janela, text=a,width='2')
        lb7.config(font=("Arial", 20))
        lb7.place(x=130, y=430)
        
        if(ordem[Y].m[2][1]==0):
            a = ""
        else:
            a = ordem[Y].m[2][1]
                        
        lb8 = Label(janela, text=a,width='2')
        lb8.config(font=("Arial", 20))
        lb8.place(x=280, y=430)
    
        if(ordem[Y].m[2][2]==0):
            a = ""
        else:
            a = ordem[Y].m[2][2]
        
        lb9 = Label(janela, text=a,width='2')
        lb9.config(font=("Arial", 20))
        lb9.place(x=430, y=430)
    else:
        textBox = Text(janela, height=2, width=22,font=("Helvetica", 10))
        textBox.insert(INSERT, ordem[tam-1].pr)
        textBox.insert(END," Passos Concluidos.\nEmbaralhe Novamente.")
        textBox.place(x=535,y=350)
    
    Y = Y + 1
      
   
    
janela = Tk()
janela.title("Quebra Cabeça de 8 Peças")
janela.geometry("700x600+100+50")

w = Canvas(janela, width=700, height=600, bg="black")

w.create_rectangle(75, 75, 225, 225, fill="black",outline='gray',width=3)
w.create_rectangle(225, 75, 375, 225, fill="black",outline='gray',width=3)
w.create_rectangle(375, 75, 525, 225, fill="black",outline='gray',width=3)
w.create_rectangle(75, 225, 225, 375, fill="black",outline='gray',width=3)
w.create_rectangle(225, 225, 375, 375, fill="black",outline='gray',width=3)
w.create_rectangle(375, 225, 525, 375, fill="black",outline='gray',width=3)
w.create_rectangle(75, 375, 225, 525, fill="black",outline='gray',width=3)
w.create_rectangle(225, 375, 375, 525, fill="black",outline='gray',width=3)
w.create_rectangle(375, 375, 525, 525, fill="black",outline='gray',width=3)
w.pack()

lb1 = Label(janela, text="",width='2')
lb1.config(font=("Arial", 20))
lb1.place(x=130, y=125)

lb2 = Label(janela, text="1",width='2')
lb2.config(font=("Arial", 20))
lb2.place(x=280, y=125)

lb3 = Label(janela, text="2",width='2')
lb3.config(font=("Arial", 20))
lb3.place(x=430, y=125)

lb4 = Label(janela, text="3",width='2')
lb4.config(font=("Arial", 20))
lb4.place(x=130, y=280)

lb5 = Label(janela, text="4",width='2')
lb5.config(font=("Arial", 20))
lb5.place(x=280, y=280)

lb6 = Label(janela, text="5",width='2')
lb6.config(font=("Arial", 20))
lb6.place(x=430, y=280)

lb7 = Label(janela, text="6",width='2')
lb7.config(font=("Arial", 20))
lb7.place(x=130, y=430)

lb8 = Label(janela, text="7",width='2')
lb8.config(font=("Arial", 20))
lb8.place(x=280, y=430)

lb9 = Label(janela, text="8",width='2')
lb9.config(font=("Arial", 20))
lb9.place(x=430, y=430)

lb10 = Label(janela, text="Console:",width='8',bg="gray")
lb10.config(font=("Arial", 10))
lb10.place(x=530, y=320)

textBox = Text(janela, height=2, width=22,font=("Helvetica", 10))
textBox.insert(INSERT, "Embaralhe")
textBox.place(x=535,y=350)

bt1 = Button(janela,width=20,text="Embaralhar",command = emb)
bt1.place(x=540,y=150)

bt2 = Button(janela,width=20,text="Buscar Solução", command = bus)
bt2.place(x=540,y=200)

bt3 = Button(janela,width=20,text="Próximo Passo", command = prox)
bt3.place(x=540,y=250)



janela.mainloop()