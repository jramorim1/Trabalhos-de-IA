from random import choice
from board import *
from math import inf
import Jogo
from tkinter import *    
import time 

e = None

class janela():
    
    def __init__(self):
        
        self.janela = Tk()
        self.janela.title("Jogo da velha")
        self.janela.geometry("700x600+100+50")
        self.janela.configure(bg='black')
        self.wait_state = False
        self.jogo = None
        self.novo = 0
        self.begin()
    
    def begin(self):
        
        lbmenu = Label(self.janela, text="Escolha quem jogará primeiro: ",width='25',fg='red',bg='black')
        lbmenu.config(font=("Arial", 20))
        lbmenu.place(x=150, y=125)
        
        btIA = Button(self.janela,width=20,text="Computador", command = self.firstIA)
        btIA.place(x=270,y=250)
        
        btHumano = Button(self.janela,width=20,text="Humano", command = self.firstHum)
        btHumano.place(x=270,y=300)
        
    def firstIA(self):
        
        if(self.novo==0):
            
            for widget in self.janela.winfo_children():
                widget.destroy()    
            self.jogo = Jogo.jogo()
            self.desenhaTela(self.jogo)
            
        self.novo = 1
        
        if not (len(self.jogo.board.empty()) and not self.jogo.fimDeJogo()):
            
            self.novo = 0
            time.sleep(1)
            self.resultadoTela(self.jogo)
        
        else:
            self.jogo.vezPC()
            self.desenhaTela(self.jogo)
        
        if not (len(self.jogo.board.empty()) and not self.jogo.fimDeJogo()):
            
            self.novo = 0
            time.sleep(1)
            self.resultadoTela(self.jogo)


    def firstHum(self):
        
        if(self.novo==0):
            
            for widget in self.janela.winfo_children():
                widget.destroy()    
            self.jogo = Jogo.jogo()
            self.desenhaTela(self.jogo)
        '''
        while len(self.jogo.board.empty()) and not self.jogo.fimDeJogo():
            
            self.jogo.vezHumano(self.janela)
            self.desenhaTela(self.jogo)
            
            self.jogo.vezPC()
            self.desenhaTela(self.jogo)
                    
            
        time.sleep(1)
        self.resultadoTela(self.jogo)
        '''
    
    def desenhaTela(self, jogo):
        
        global e
        
        w = Canvas(self.janela, width=700, height=600, bg="black")
        
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
        
        e = Entry(self.janela, bd =2,width=8)
        e.place(x=583,y=200)
        
        lbjogada = Label(self.janela, text="Digite a posição de jogada:",width='20',fg='red',bg = 'black')
        lbjogada.config(font=("Arial", 10))
        lbjogada.place(x=530,y=160)
        
        lbjog = Label(self.janela, text="1 - 9",width='4',fg='red',bg = 'black')
        lbjog.config(font=("Arial", 10))
        lbjog.place(x=590,y=180)
        
        btPlay = Button(self.janela,width=20,text="Confirme sua Jogada", command = self.getPosition)
        btPlay.place(x=540,y=230)
        self.desenhaXeO(jogo)
        
        self.janela.update()
        
    def desenhaXeO(self, jogo):
        
        lbX0 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX0.config(font=("Arial", 60))
        lbO0 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO0.config(font=("Arial", 60))

        lbX1 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX1.config(font=("Arial", 60))
        lbO1 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO1.config(font=("Arial", 60))
        
        lbX2 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX2.config(font=("Arial", 60))
        lbO2 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO2.config(font=("Arial", 60))
    
        lbX3 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX3.config(font=("Arial", 60))
        lbO3 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO3.config(font=("Arial", 60))
        
        lbX4 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX4.config(font=("Arial", 60))
        lbO4 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO4.config(font=("Arial", 60))
        
        lbX5 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX5.config(font=("Arial", 60))
        lbO5 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO5.config(font=("Arial", 60))
        
        lbX6 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX6.config(font=("Arial", 60))
        lbO6 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO6.config(font=("Arial", 60))
        
        lbX7 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX7.config(font=("Arial", 60))
        lbO7 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO7.config(font=("Arial", 60))
        
        lbX8 = Label(self.janela, text="x",width='1',fg='red',bg = 'black')
        lbX8.config(font=("Arial", 60))
        lbO8 = Label(self.janela, text="o",width='1',fg='red',bg = 'black')
        lbO8.config(font=("Arial", 60))
        
        if jogo.board.estado[0][0] == 1:
            lbX0.place(x=120, y=100)
        elif jogo.board.estado[0][0] == -1:
            lbO0.place(x=120, y=100)
        
        if jogo.board.estado[0][1] == 1:
            lbX1.place(x=280, y=100)
        elif jogo.board.estado[0][1] == -1:
            lbO1.place(x=280, y=100)
            
        if jogo.board.estado[0][2] == 1:
            lbX2.place(x=430, y=100)
        elif jogo.board.estado[0][2] == -1:
            lbO2.place(x=430, y=100)
            
        if jogo.board.estado[1][0] == 1:
            lbX3.place(x=120, y=250)
        elif jogo.board.estado[1][0] == -1:
            lbO3.place(x=120, y=250)
        
        if jogo.board.estado[1][1] == 1:
            lbX4.place(x=280, y=250)
        elif jogo.board.estado[1][1] == -1:
            lbO4.place(x=280, y=250)
            
        if jogo.board.estado[1][2] == 1:
            lbX5.place(x=430, y=250)
        elif jogo.board.estado[1][2] == -1:
            lbO5.place(x=430, y=252)

        if jogo.board.estado[2][0] == 1:
            lbX6.place(x=120, y=400)
        elif jogo.board.estado[2][0] == -1:
            lbO6.place(x=120, y=400)
        
        if jogo.board.estado[2][1] == 1:
            lbX7.place(x=280, y=400)
        elif jogo.board.estado[2][1] == -1:
            lbO7.place(x=280, y=400)
            
        if jogo.board.estado[2][2] == 1:
            lbX8.place(x=430, y=400)
        elif jogo.board.estado[2][2] == -1:
            lbO8.place(x=430, y=400)

    def resultadoTela(self,jogo):
        
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        l = Canvas(self.janela, width=700, height=600, bg="black")
        l.pack()
        
        if jogo.board.estadoVencedor(jogo.pc):
            
            lbmenu = Label(self.janela, text="Você Perdeu: ",width='25',fg='red',bg='black')
            lbmenu.config(font=("Arial", 20))
            lbmenu.place(x=150, y=125)
        
        elif jogo.board.estadoVencedor(jogo.humano):
          
            lbmenu = Label(self.janela, text="Você Venceu",width='25',fg='red',bg='black')
            lbmenu.config(font=("Arial", 20))
            lbmenu.place(x=150, y=125)
        
        else:
            
            lbmenu = Label(self.janela, text="Empatou",width='25',fg='red',bg='black')
            lbmenu.config(font=("Arial", 20))
            lbmenu.place(x=150, y=125)
        
        btHumano = Button(self.janela,width=20,text="Jogador Novamente", command = self.begin)
        btHumano.place(x=270,y=300)
        
        self.janela.update()

    def getPosition(self):
        
        global e
        
        if not (len(self.jogo.board.empty()) and not self.jogo.fimDeJogo()):

            self.novo = 0
            time.sleep(1)
            self.resultadoTela(self.jogo)
            
        else:
            
            while True:
                k = int(e.get())
            
                if k==1:
                    x,y = 0,0
                elif k==2:    
                    x,y = 0,1
                elif k==3:    
                    x,y = 0,2
                elif k==4:    
                    x,y = 1,0
                elif k==5:    
                    x,y = 1,1
                elif k==6:    
                    x,y = 1,2
                elif k==7:    
                    x,y = 2,0
                elif k==8:    
                    x,y = 2,1
                elif k==9:    
                    x,y = 2,2
                    
                if self.jogo.board.movimentoValido(x,y):
                    break
                else:
                    e.delete(first=0,last=100)
                    e.insert(0,"Inválido")
                    
            
            self.jogo.vezHumano(self.janela,x,y)
            self.desenhaTela(self.jogo)
            self.novo = 1
            self.firstIA()

        
        