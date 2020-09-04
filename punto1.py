# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:32:08 2020

@author: asus
"""

print("Cálculo del valor del tiquete de avión")
km=float(input("Ingresa la distancia en km y si tiene cifras decimales, separar con punto(.): "))
t=int(input("Ingresa la cantidad de días de tu estancia: "))
v = km*35
if km>1000 and t>7:
    v=v*0.7
    print("Su tiquete tiene un 30% de descuento")
print("El valor del tiquete es: $",v)