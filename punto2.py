# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 00:19:12 2020

@author: Cristian Arango
"""

print("Bienvenido al BOING 747.\n")
l=[]  # Crear lista vacía para el ingreso de los pesos de los bultos
v=[]  # Crear lista vacía para almacenar los valores 
k=0   # contador
my = 0  #Número mayor
mn = 0  #Número menor
s = 0   #sumatoria de los pesos
p=0     #sumatoria de los precios
# Bucle con iteraciones infinitas hasta que el usuario no introduzca más valores
while True:
    while True: #Para salir de este bucle, se debe ingresar un valor correcto
        nv=float(input("Ingresa el peso del bulto en kg, y si tiene un valor decimal, separarlo con punto(.): "))
        if nv>500:
            print("Peso del bulto excede el permitido. Vuelva a intentar")
        else:
            break
    #Condicionales para los calcular los valores
    if nv<=25:
        valor=0
    elif nv>25 and nv <=300:
        valor=nv*1500
    elif nv>300 and nv<=500:
        valor=nv*2500
    print("Se debe pagar por concepto de carga del bulto de",nv,"kg, un total de $",valor)
    l.append(nv)     # Se adiciona el bulto en la lista l
    v.append(valor)  #se adiciona el valor en la lista v
    k +=1            #contador aumenta a 1
    # preguntar si se desea ingresar un bulto adicional
    r12=input("Si deseas ingresar otro bulto ingresa 1, de lo contrario presiona cualquier tecla:")
    if r12 != '1': 
       break    #si presionan cualquier número, se sale del loop
# Mostrar en pantalla la cantidad de bultos cargados
print("\nEl número total de bultos cargados es:",len(l))
#Calculo del mayor y de la sumatoria de los pesos y precios
for d in range (len(l)):
    s = s+l[d]     # Sumatoria de pesos para el cálculo del promedio
    p = p+v[d]     # Sumatoria de los precios para el valor total
    if l[d]>my:    # Ordenar mayor
        my = l[d]
        mn=my
# ordenar el menor
for f in range (len(l)):
    if l[f]<mn:
        mn=l[f]
#Mostrar el bulto con mayor y menor peso
print("El bulto más pesado tiene un peso de",my,"kg, y el bulto más liviano tiene un peso de",mn,"kg.")
#Mostrar el promedio de los pesos de los bultos ingresados
print("El promedio de los pesos de todos los bultos es:",s/len(l),"kg.")
# Muestra el valor del total a pagar
print("Se debe pagar un total de $",p,"por la cantidad de bultos enviados.\n\t ¡Vuelve pronto!")
    