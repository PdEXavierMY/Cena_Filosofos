# Cena_Filosofos

Pincha [aquí](https://github.com/Xavitheforce/Cena_Filosofos) para dirigirte a mi repositorio.

Esta entrega consta de 3 archivos de python, uno responsable del comportamiento de los filósofos, otro encargado de gestionar la interfaz gráfica con tkinter y el último encargado de correr el programa.

El código realizado para la GUI es:

```python
import tkinter as tk
from filosofos_samplecode import *
import math
class Ventana(): #VENTANA DE LA APLICACION
    def __init__(self):
        self.root=tk.Tk()
        alto=35
        ancho=60
        self.root.title("La comida de los filósofos")
        self.root.geometry("1000x800") #TAMAÑO DE LA VENTANA
        self.fondo="light blue"
        self.root.configure(bg=self.fondo)
        self.text = tk.Text(self.root, height=alto, width=ancho)
        self.scroll = tk.Scrollbar(self.root)
        self.caja =[]
        self.labels=[]
        self.tenedores=[]
        self.añadirCaja()
        self.text.configure(yscrollcommand=self.scroll.set)
        self.text.place(x=10, y=160, height=500, width=500)
        self.scroll.config(command=self.text.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        #Los siguientes labels son para la leyenda y el contador de comidas
        tk.Label(self.root, text="Leyenda ", font='Helvetica 18 bold', bg=self.fondo).place(x=275,y=0)
        tk.Label(self.root, text=" ",bg="pink").place(x=35,y=40)
        tk.Label(self.root, text="Filósofo entra a comer", bg=self.fondo).place(x=50,y=40)
        tk.Label(self.root, text=" ",bg="cyan").place(x=35,y=65)
        tk.Label(self.root, text="Filósofo está hambriento", bg=self.fondo).place(x=50,y=65)
        tk.Label(self.root, text=" ",bg="gold").place(x=35,y=90)
        tk.Label(self.root, text="Filósofo está comiendo", bg=self.fondo).place(x=50,y=90)
        tk.Label(self.root, text=" ",bg="pale green").place(x=260,y=40)
        tk.Label(self.root, text="Filósofo termina la comida", bg=self.fondo).place(x=275,y=40)
        tk.Label(self.root, text=" ",bg="white").place(x=260,y=65)
        tk.Label(self.root, text="Filósofo está pensando", bg=self.fondo).place(x=275,y=65)
        tk.Label(self.root, text=" ",bg="red").place(x=260,y=90)
        tk.Label(self.root, text="Filósofo se levanta de la mesa", bg=self.fondo).place(x=275,y=90)
        tk.Label(self.root, text=" ",bg="blue").place(x=495,y=40)
        tk.Label(self.root, text="Tenedor ocupado", bg=self.fondo).place(x=510,y=40)
        tk.Label(self.root, text=" ",bg="grey").place(x=495,y=65)
        tk.Label(self.root, text="Tenedor libre", bg=self.fondo).place(x=510,y=65)
        tk.Label(self.root, text="Cuántas veces han comido:", font='Helvetica 16 bold', bg=self.fondo).place(x=600,y=110)
    def añadirCaja(self):
        angulo=math.pi/N
        #Añade las cajas que representan a los filósofos
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
    def escribe(self,texto): #ESCRIBE EN LA VENTANA
        self.text.insert(tk.END, str(texto)+"\n")
        print(str(texto))
        self.text.see(tk.END)
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
```

El código realizado para el funcionamiento del problema es:

```python
import time
import random
import threading
from tkinter import END
N = 5
TIEMPO_TOTAL = 3

class filosofo(threading.Thread):
    semaforo = threading.Lock() #SEMAFORO BINARIO ASEGURA LA EXCLUSION MUTUA
    estado = [] #PARA CONOCER EL ESTADO DE CADA FILOSOFO
    tenedores = [] #ARRAY DE SEMAFOROS PARA SINCRONIZAR ENTRE FILOSOFOS, MUESTRA QUIEN ESTA EN COLA DEL TENEDOR
    count=0
    def __init__(self,ventana):
        super().__init__()      #HERENCIA
        filosofo.semaforo.acquire()  # Bloqueo con el semáforo
        self.id=filosofo.count #DESIGNA EL ID AL FILOSOFO
        self.comida=0
        self.vent=ventana

        self.vent.labels[self.id].config(bg="white")
        filosofo.count+=1 #AGREGA UNO A LA CANT DE FILOSOFOS
        filosofo.estado.append('PENSANDO') #EL FILOSOFO ENTRA A LA MESA EN ESTADO PENSANDO
        filosofo.tenedores.append(threading.Semaphore(0)) #AGREGA EL SEMAFORO DE SU TENEDOR( TENEDOR A LA IZQUIERDA)
        self.vent.escribe("FILOSOFO {0} - PENSANDO".format(self.id))
        filosofo.semaforo.release()  # Libero el semáforo

    def pensar(self):
        time.sleep(random.randint(0,5)) #CADA FILOSOFO SE TOMA DISTINTO TIEMPO PARA PENSAR, ALEATORIO

    def derecha(self,i):
        return (i-1)%N #BUSCAMOS EL INDICE DE LA DERECHA

    def izquierda(self,i):
        return(i+1)%N #BUSCAMOS EL INDICE DE LA IZQUIERDA

    def verificar(self,i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i]='COMIENDO'
            filosofo.tenedores[i].release()  #SI SUS VECINOS NO ESTAN COMIENDO AUMENTA EL SEMAFORO DEL TENEDOR Y CAMBIA SU ESTADO A COMIENDO

    def tomar(self):
        time.sleep(2)
        filosofo.semaforo.acquire() #SEÑALA QUE TOMARA LOS TENEDORES (EXCLUSION MUTUA)
        filosofo.estado[self.id] = 'HAMBRIENTO'
        self.vent.labels[self.id].config(bg="cyan")
        self.verificar(self.id) #VERIFICA SUS VECINOS, SI NO PUEDE COMER NO SE BLOQUEARA EN EL SIGUIENTE ACQUIRE
        filosofo.semaforo.release() #SEÑALA QUE YA DEJO DE INTENTAR TOMAR LOS TENEDORES (CAMBIAR EL ARRAY ESTADO)
        filosofo.tenedores[self.id].acquire() #SOLO SI PODIA TOMARLOS SE BLOQUEARA CON ESTADO COMIENDO

    def soltar(self):
        filosofo.semaforo.acquire() #SEÑALA QUE SOLTARA LOS TENEDORES
        filosofo.estado[self.id] = 'PENSANDO'
        self.vent.escribe("FILOSOFO {} PENSANDO".format(self.id))
        self.vent.labels[self.id].config(bg="white")
        self.verificar(self.izquierda(self.id))
        self.verificar(self.derecha(self.id))
        filosofo.semaforo.release() #YA TERMINO DE MANIPULAR TENEDORES

    def comer(self):
        self.vent.tenedores[self.id].config(bg="blue")
        self.vent.tenedores[(self.id-1)%N].config(bg="blue")
        print("FILOSOFO {} coge tenedor {} y {}".format(self.id, self.id,(self.id+1)%N))

        self.vent.escribe("FILOSOFO {} COMIENDO".format(self.id))

        self.vent.labels[self.id].config(bg="gold")
        self.vent.tenedores[self.id].config(bg="blue", fg="white")
        self.vent.tenedores[(self.id-1)%N].config(bg="blue", fg="white")
        time.sleep(4) #TIEMPO PARA COMER
        self.vent.escribe("FILOSOFO {} TERMINO DE COMER".format(self.id))

        print("FILOSOFO {} suelta tenedor {} y {}".format(self.id, self.id,(self.id+1)%N))
        self.vent.tenedores[self.id].config(bg="grey", fg="white")
        self.vent.tenedores[(self.id-1)%N].config(bg="grey", fg="white")

        self.comida+=1
        self.vent.caja[self.id].delete(0,END)
        self.vent.caja[self.id].insert(0,self.comida)

    def run(self):
        self.vent.labels[self.id].config(bg="pink")
        for i in range(random.randint(1,5)):
            self.pensar() #EL FILOSOFO PIENSA
            self.tomar() #AGARRA LOS TENEDORES CORRESPONDIENTES
            self.comer() #COME
            self.soltar() #SUELTA LOS TENEDORES
            self.vent.labels[self.id].config(bg="pale green")
        self.vent.escribe("FILOSOFO {} HA FINALIZADO".format(self.id))
        self.vent.labels[self.id].config(bg="red")     
```

Finalmente el main(archivo ejecutor) es:

```python
from interfaz import Ventana
from filosofos_samplecode import N, filosofo

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
```

Ahora vamos a ver la salida por terminal del main:

![Interfaz1](https://user-images.githubusercontent.com/91721699/235370893-f4090191-fbd6-4574-87d5-93c4c5ed7bef.png)

Esta sería la aparencia de la interfaz pasada unos segundos, es decir, cuando el código sigue en marcha. Y esta próxima imagen sería al final de la ejecución, cuando todos los filosofos están ya hinchados de comer y pensar:

![Interfaz2](https://user-images.githubusercontent.com/91721699/235370901-a2a1b21c-71cf-44b0-a870-f5e8065c29cc.png)
