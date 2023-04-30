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