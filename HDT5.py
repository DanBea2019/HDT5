#Universidad del Valle de Guatemala
#ALgoritmos y estrucutura de datos
#Daniela Batz 19214
import simpy
import random

#new
#1=ocupado
#0=libre
def espera(numero,env,memoria):
    puestos=[0,0,0,0,0,0,0,0,0,0]
    puesto1=[]
    RAM = simpy.Container(env, init=100, capacity=100)

    RAM: RAM.get(memoria)

    RAM: RAM.put(memoria)
    while True:
        numero = random.randint(0,10)
        for elemento in puestos:
            elemento = 1
            puesto1.append(elemento)
            print ("Su numero es: ", num)
        if puesto1 == 1:
            print ("Pasara al sigueinte")
        elif puesto1 == 0:
            print ("Espere esta ocupado")
 
        while memoria <= 100:
            
#
env = simpy.Environment() #crear ambiente de simulacion
bcs = simpy.Resource(env, capacity=10)

#crear
for i in range(1):
    env.process(espera(env, 'Car %d' % i, bcs, i*10, 1))
#correr el programa
env.run()
