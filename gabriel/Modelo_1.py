# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:53:12 2020

@author: Gabriel
"""

from vpython import *
from numpy import *
import matplotlib.pyplot as plt
#from drawnow import *
import time

#PROPRIEDADES ELASTICAS DO CILINDRO
F = 5 #N. Positivo, portanto orientada no eixo positivo de y, com o ojetivo de tensionar
m = 0.01 #Kg
y = 0.1 #m
k = 80 #N/m
y1 = y + F/k
E = 10000 #Modulo de Young (Pa)
D = (y1-y)/y #Deformação
T = E*D #Tensão (Stress)

#mostrar a força
pointer = arrow(pos=vector(1.5,1.5,1.5), axis=vector(0,3,0), shaftwidth=0, color=color.cyan)

#criação cilindro
rod = cylinder(pos=vector(0,0,0),axis=vector(0,3,0),radius=0.5)
#foi criado um cilindro q começa em x=0, y=0, z=0 e foi alongado em y até a posição 3,
#portanto, ele termina em (0,3,0)
rod.color=vector(0,0,1) #cor azul pois no RGB, B is True

#caixas de texto
forceL=label(pos = vec(3,1,0), text = 'Força_T = %1.1f N' %(F))#Força Tensão
strain=label(pos = vec(-3,0.06,0), text = 'Deformação = %1.3f m' %(D))
young=label(pos = vec(0,0.06,0), text = 'E = %d Pa' %(E))
stress=label(pos = vec(6,0.06,0), text = 'Tensao = %1.3f ' %(T))

#criação base
floor=box(pos=vector(0,0,0),size=vector(9,0.1,9))#uma caixa bem fininha eh o chão
floor.color=color.gray(0.5)#cinza

#criação apurador
rodc = cylinder(pos=vector(0,0,0),axis=vector(0,0.1,0),radius=0.6)
rodc.pos = vector(0,3,0)
rodc.color=vector(1,1,0)

#Grafico

# Arrays para o gráfico
deformacao = []
tensao = []

plt.ion()#tempo real
def makeFig():#função de plotar
    plt.plot(deformacao, tensao, 'ro-')#plotar tensão por deformação do cilindro
    plt.xlabel('ɛ')
    plt.ylabel('σ (kPa)')
    plt.title('Ensaio Mecânico')
    
#Movimento Tensão
for cont in range(0, 30):
    #Incremento na força
    F = F + 0.5
    # Nova posição de acordo com a lei de Hooke
    y1 = y + F/k;
    # Atualizando demais parâmetros
    forceL.text = 'Força_T = %1.1f N' %(F)
    rod.axis = vector(0, 3+y1, 0)
    rod.radius = 0.5-(y1/2) #distensão de acordo com Coeficiente de Poisson
    D = (y1-y)/y
    T = E*D
    strain.text = 'Deform. = %1.3f ' %(D)
    young.text = 'E = %d Pa' %(abs(E))
    stress.text = 'Tensao = %1.3f Pa ' %(T/1000)
    rodc.pos = vector(0,3+y1,0)
    pointer.axis = vector(0, D, 0)  
    tensao.append(T/1000) 
    deformacao.append(D)
    makeFig()
    time.sleep(0.3)

    