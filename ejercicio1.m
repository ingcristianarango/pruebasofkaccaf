%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                    Prueba t�cnica Sofka                   %
%               Cristian Camilo Arango Fer�ndez             %
%                     Septiembre de 2020                    %
%                    Medell�n - Colombia                    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc;
clear all;
close all;

fprintf('C�lculo de tiquete de avi�n. \n\n')

distancia=input('Ingrese la distancia del recorrido en km (si la distancia tiene cifras decimales se deben separan con punto (.)): \n');
tiempo=input('Ingrese los d�as de su estad�a: \n');

v = (distancia*35);

if distancia >1000 && tiempo >7
    v = v*0.7;
    disp('Su tiquete tiene un 30% de descuento.');
end
formatSpec = 'El valor a pagar es de $ %6.2f \n';
fprintf(formatSpec,v)


