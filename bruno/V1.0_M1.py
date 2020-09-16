#!/usr/bin/env python
# coding: utf-8

# In[23]:


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:52:05 2020

@author: bruno
"""

from vpython import *
from numpy import *
import matplotlib.pyplot as plt
from drawnow import *
import time

# Parâmetros principais:
L = 0.02 # em metros
H = 0.02 # em metros
W = 0.02 # em metros

# Propriedades Iniciais:
e = 10000           #Módulo de Young (Pa)
E = 0               #Deformação
M = 0               #Movimento Atuador
S = 0               #Stress

# Parâmetros para movimento do atuador:
I = H           #Posição Inicial
Ly = I          #Deslocamento pelo eixo Y.

canvas()
# Definindo o material (bloco).
bloco = box(pos = vector(0, 0, 0), size = vector(L, H, W), color = color.red);

# Definindo o atuador que irá realizar a compressão do material.
atuador = cylinder(pos=vector(0, 0.01 ,0), axis=vector(0,5,0), radius=0.020, size = vector(L, 0.001, W), color = color.blue)

# Caixas de texto.
forceL=label(pos = vec(0,0.06,0), text = 'E = %1.1f N' %(e))
tensaoL=label(pos = vec(0.07,0.06,0), text = 'Tensao = %1.1f ' %(0))
deformaL=label(pos = vec(-0.07,0.06,0), text = 'Desloc. = %1.1f ' %(E))

# Definindo a plataforma de apoio de nosso bloco.
ground = box(pos = vector(0, -(H/2) , 0), size = vector(0.2, 0.001, 0.1), color = color.white)

# Seta que indica a força
pointer = arrow(pos=vector(0.05, -0.04 ,0),  axis = vector(0, -0.05, 0), shaftwidth = 0, color = color.red)

# Arrays para o gráfico
Stress = []
Strain = []

# Gráficos do Matlib
plt.ion() 
def makeFig():
    plt.plot(Strain, Stress, 'D-')       #plotar força por posição do bloco
    plt.xlabel('Strain')
    plt.ylabel('Stress')
    plt.title('Stress/Strain Plot')


#Movimento de Compressão:
for cont in range(0, 18):
    # Incremento na força
    M = M + 0.0005    #Movimento de 0.0005.
    
    # Parametros atualizados:
    Ly = Ly + 0.0005               #Deslocamento Y total = 0.009
    E = (I-Ly)/I                  #Deformação
    S = E*e                        #Estresse (Tensão)
    
    # Movimento do Atuador:
    atuador.pos = vector(0, 0.01 - M,0)
    
    # Compressão do Bloco:
    bloco.size = vector(L + M, (H - M), W + 2*(M))   #Compressão em (X, Y, Z) de acordo com Coef. Poiss.
    bloco.pos = vector(0,-M/2 ,0)
    
    # Posição da Seta:
    pointer.pos = vector(0.05, 0.01 - M ,0)
    
    # Atualizando demais parâmetros
    pointer.pos = vector(0.05, 0.05 - M ,0)
    forceL.text = 'E = %1.0f N' %(e)
    tensaoL.text = 'Tensao = %1.0f N ' %(S*-1)      #Seu valor deve ser apresentado em módulo.
    deformaL.text = 'Deform. = %1.2f ' %(E*-1)      #Seu valor deve ser apresentado em módulo.
    
    # Atualizando os vetores para o gráfico mostrado em tempo real
    Stress.append(S*-1) 
    Strain.append(E*-1)
    drawnow(makeFig)  
    
    # Representar a movimentação de modo devagar
    time.sleep(0.005)

    
