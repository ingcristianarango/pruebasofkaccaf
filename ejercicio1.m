%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                    Prueba técnica Sofka                   %
%               Cristian Camilo Arango Ferández             %
%                     Septiembre de 2020                    %
%                    Medellín - Colombia                    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clc;
clear all;
close all;

fprintf('Cálculo de tiquete de avión. \n\n')

distancia=input('Ingrese la distancia del recorrido en km (si la distancia tiene cifras decimales se deben separan con punto (.)): \n');
tiempo=input('Ingrese los días de su estadía: \n');

v = (distancia*35);

if distancia >1000 && tiempo >7
    v = v*0.7;
    disp('Su tiquete tiene un 30% de descuento.');
end
formatSpec = 'El valor a pagar es de $ %6.2f \n';
fprintf(formatSpec,v)


