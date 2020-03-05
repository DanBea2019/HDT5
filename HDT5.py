#Universidad del Valle de Guatemala
#ALgoritmos y estrucutura de datos
#Daniela Batz 19214
import simpy
import random

#new
#1=ocupado
#0=libre
def tiempo(num):
    puestos=[0,0,0,0,0,0,0,0,0,0]
    puesto1=[]
    num=random.random(0,10)
    for elemento in puestos:
        elemento = 1
    puesto1.append(elemento)
    print ("Su numero es: ", num)
    if puesto1 == 1:
        print ("Pasara al sigueinte")
    elif puesto1 == 0:
        print ("Espere esta ocupado")
