# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:32:08 2020

@author: Cristian Camilo Arango Fernández
"""
# Programa para calcular el valor del pasaje de un avión 
# dependiendo de la cantidad de los km del recorrido
print("Cálculo del valor del tiquete de avión")
# ENTRADA DE DATOS POR CONSOLA. 
km=float(input("Ingresa la distancia en km y si tiene cifras decimales, separar con punto(.): "))
t=int(input("Ingresa la cantidad de días de tu estancia: "))
# CALCULA EL VALOR DEL PASAJE V 1 KM CUESTA 35
v = km*35
# CONDICIONAL PARA VER SI EL PASAJE APLICA AL DESCUENTO
if km>1000 and t>7:
    v=v*0.7
    print("Su tiquete tiene un 30% de descuento")
# MUESTRA EN PANTALLA EL VALOR DEL PASAJE
print("El valor del tiquete es: $",v)