# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 00:19:12 2020

@author: asus
"""

print("Bienvenido al BOING 747.\n")
l=[]
v=[]
k=0
my = 0
mn = 0
s = 0
p=0
#l.append(1)
while True:
    while True:
        nv=float(input("Ingresa el peso del bulto en kg, y si tiene un valor decimal, separarlo con punto(.): "))
        if nv>500:
            print("Peso del bulto excede el permitido. Vuelva a intentar")
        else:
            break
    if nv<=25:
        valor=0
    elif nv>25 and nv <=300:
        valor=nv*1500
    elif nv>300 and nv<=500:
        valor=nv*2500
    print("Se debe pagar por concepto de carga del bulto de",nv,"kg, un total de $",valor)
    l.append(nv)
    v.append(valor)
    k +=1
   # print("\n\tSi deseas ingresar otro bulto, ingresa 1, de lo contrario ingresa 2:")
    r12=int(input("Si deseas ingresar otro bulto, ingresa 1, de lo contrario ingresa 2:"))
    if r12 == 2:
       break
print("\nEl número total de bultos cargados es:",len(l))
for d in range (len(l)):
    s = s+l[d]
    p = p+v[d]
    if l[d]>my:
        my = l[d]
        mn=my
for f in range (len(l)):
    if l[f]<mn:
        mn=l[f]

print("El bulto más pesado tiene un peso de",my,"kg, y el bulto más liviano tiene un peso de",mn,"kg.")
print("El promedio de los pesos de todos los bultos es:",s/len(l),"kg.")
print("Se debe pagar un total de $",p,"por la cantidad de bultos enviados.\n\t ¡Vuelve pronto!")
    