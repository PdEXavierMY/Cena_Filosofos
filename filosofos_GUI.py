import tkinter as tk
from filosofos_samplecode import *
import math
class Ventana():
    def __init__(self):
        self.root=tk.Tk()
        alto=30
        ancho=80
        self.root.title("La comida de los filósofos")
        self.root.geometry("900x600")
        self.fondo="light steel blue"
        self.root.configure(bg=self.fondo)
        self.text = tk.Text(self.root, height=alto, width=ancho)
        self.scroll = tk.Scrollbar(self.root)
        self.caja =[]
        self.labels=[]
        self.tenedores=[]
        self.añadirCaja()
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=tk.LEFT)
        self.scroll.config(command=self.text.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tk.Label(self.root, text="Código de colores ", font='Helvetica 18 bold', bg=self.fondo).place(x=275,y=0)
        tk.Label(self.root, text=" ",bg="pink").place(x=35,y=30)
        tk.Label(self.root, text="Filósofo entra a comer", bg=self.fondo).place(x=50,y=30)
        tk.Label(self.root, text=" ",bg="cyan").place(x=35,y=55)
        tk.Label(self.root, text="Filósofo está hambriento", bg=self.fondo).place(x=50,y=55)
        tk.Label(self.root, text=" ",bg="gold").place(x=35,y=80)
        tk.Label(self.root, text="Filósofo está comiendo", bg=self.fondo).place(x=50,y=80)
        tk.Label(self.root, text=" ",bg="pale green").place(x=260,y=30)
        tk.Label(self.root, text="Filósofo termina la comida", bg=self.fondo).place(x=275,y=30)
        tk.Label(self.root, text=" ",bg="white").place(x=260,y=55)
        tk.Label(self.root, text="Filósofo está pensando", bg=self.fondo).place(x=275,y=55)
        tk.Label(self.root, text=" ",bg="red").place(x=260,y=80)
        tk.Label(self.root, text="Filósofo se levanta de la mesa", bg=self.fondo).place(x=275,y=80)
        tk.Label(self.root, text=" ",bg="blue").place(x=495,y=30)
        tk.Label(self.root, text="Tenedor ocupado", bg=self.fondo).place(x=510,y=30)
        tk.Label(self.root, text=" ",bg="grey").place(x=495,y=55)
        tk.Label(self.root, text="Tenedor libre", bg=self.fondo).place(x=510,y=55)
        tk.Label(self.root, text="Cuántas veces han comido:", font='Helvetica 16 bold', bg=self.fondo).place(x=600,y=110)
    def añadirCaja(self):
        angulo=math.pi/N
        for i in range(N):
            cajaaux= tk.Entry(self.root)
            cajaaux.place(x=700,y=140+i*20)
            tk.Label(self.root, text="Filósofo "+str(i)+":", bg=self.fondo).place(x=600,y=140+i*20)
            label=tk.Label(self.root, text="Filósofo "+str(i))
            label2=tk.Label(self.root, text="T. " +str(i))
            label2.config(bg="grey", fg="white")
            label.place(x=700+100*math.cos(2*angulo*i),y=400+100*math.sin(2*angulo*i))
            label2.place(x=700+100*math.cos(angulo*(2*i+1)),y=400+100*math.sin(angulo*(2*i+1)))
            self.caja.append(cajaaux)
            self.labels.append(label)
            self.tenedores.append(label2)
    def escribe(self,texto):
        self.text.insert(tk.END, str(texto)+"\n")
        print(str(texto))
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    V=Ventana()

    lista=[]
    for i in range(N):
        lista.append(filosofo(V)) #AGREGA UN FILOSOFO A LA LISTA


    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()
    V.run()
    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD