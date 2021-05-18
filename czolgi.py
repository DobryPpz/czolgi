import tkinter as tk
import math
import time
import random
random.seed()

root = tk.Tk()
root.geometry("700x500")

l = 0
tura = 0
rura = 0

C = tk.Canvas(root,width=700,height=500)
C.pack()

def start():
    global C
    global tura
    global rura
    okno = tk.Toplevel(root)
    lab = tk.Label(okno,text="Witaj w grze czołgi")
    lab.pack()
    tura = 0
    rura = random.randint(150,400)
    C.create_line(350,500,350,rura,fill="red",width=20)

def zmiana():
    global tura
    global C
    global cz1
    global cz2
    tura = (tura+1)%2
    if(tura == 0):
        C.bind("<Motion>",cz1.rotacja)
        C.bind("<ButtonPress-1>",cz1.strzal)
    else:
        C.bind("<Motion>",cz2.rotacja)
        C.bind("<ButtonPress-1>",cz2.strzal)

class kula():
    global C
    def __init__(self,czolg,event):
        self.k = C.create_oval(czolg.strzal_x-10,czolg.strzal_y-10,czolg.strzal_x+10,czolg.strzal_y+10,fill="orange")
        self.pos_x = czolg.strzal_x
        self.pos_y = czolg.strzal_y
        self.vel_x = event.x - self.pos_x
        self.vel_y = event.y - self.pos_y
        self.ciezar = 0
        C.after(3000,self.destruktor)
        self.ruch(event)

    def destruktor(self):
        C.delete(self.k)
        del self

    def ruch(self,event):
        C.move(self.k,self.vel_x/8,self.vel_y/8+self.ciezar)
        self.ciezar += 5
        self.pos_x += self.vel_x/8
        self.pos_y += self.vel_y/8 + self.ciezar
        C.after(50,lambda:self.ruch(event))
        if((self.pos_x>=330 and self.pos_x<=370) and (self.pos_y<=500 and self.pos_y >= rura)):
            self.destruktor()
        elif(tura == 0 and self.pos_x>= 10 and self.pos_x<=110 and self.pos_y<=500 and self.pos_y>=460):
            self.destruktor()
            t = tk.Toplevel(root)
            lab = tk.Label(t,text="wygrywa gracz po prawej")
            lab.pack()
            start()
            return
        elif(tura == 1 and self.pos_x>=590 and self.pos_x<=690 and self.pos_y<=500 and self.pos_y>= 460):
            self.destruktor()
            t = tk.Toplevel(root)
            lab = tk.Label(t,text="Wygrywa gracz po lewej")
            lab.pack()
            start()
            return
    
        

class czolg():
    def __init__(self,position_x,position_y):
        global C
        C.create_rectangle(position_x,position_y,position_x+80,position_y+50,fill="brown")
        self.strzal_x = position_x+40
        self.strzal_y = position_y
        self.l = C.create_line(self.strzal_x,self.strzal_y,self.strzal_x,self.strzal_y-40,fill="black",width=10)

    def rotacja(self,event):
        global C
        x = event.x - self.strzal_x
        y = event.y - self.strzal_y
        h = math.sqrt(x**2+y**2)
        stosunek = h/40
        C.delete(self.l)
        self.l = C.create_line(self.strzal_x,self.strzal_y,self.strzal_x+x/stosunek,self.strzal_y+y/stosunek,fill="black",width=10)
        
    def strzal(self,event):
        global C
        print("puf")
        k = kula(self,event)
        zmiana()

cz1 = czolg(20,450)
cz2 = czolg(600,450)
C.bind("<Motion>",cz1.rotacja)
C.bind("<ButtonPress-1>",cz1.strzal)
start()




root.mainloop()