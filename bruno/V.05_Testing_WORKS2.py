#!/usr/bin/env python
# coding: utf-8

# In[31]:


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:52:05 2020

@author: bruno
"""

from vpython import *
from numpy import *
from matplotlib import *
from drawnow import *
import time

# Parâmetros principais:
L = 0.02 # em metros
H = 0.02 # em metros
W = 0.02 # em metros

# Propriedades Iniciais:
e = 10000           #Módulo de Young (kPa)
T = 0
E = 0

# Parâmetros para movimento do atuador:
F = 0 
I = H           #Posição Inicial
Ly = I          #Deslocamento pelo eixo Y.

canvas()
# Definindo o material (bloco).
bloco = box(pos = vector(0, 0, 0), size = vector(L, H, W), color = color.blue);

# Definindo o atuador que irá realizar a compressão do material.
atuador = cylinder(pos=vector(0, 0.01 ,0), axis=vector(0,5,0), radius=0.020, size = vector(L, 0.001, W), color = color.red)

# Caixas de texto.
forceL=label(pos = vec(0,0.06,0), text = 'E = %1.1f N' %(E))
tensaoL=label(pos = vec(0.07,0.06,0), text = 'Tensao = %1.1f ' %(T))
deformaL=label(pos = vec(-0.07,0.06,0), text = 'Desloc. = %1.1f ' %(E))

# Definindo a plataforma de apoio de nosso bloco.
ground = box(pos = vector(0, -(H/2) , 0), size = vector(0.2, 0.001, 0.1))

# Seta que indica a força
pointer = arrow(pos=vector(0.05, 0.05 ,0),  axis = vector(0, -0.02, 0), shaftwidth = 0, color = color.red)

#Movimento de Compressão:
for cont in range(0, 18):
    # Incremento na força
    F = F + 0.0005    #Por conta de nossas medidas, se trata de 0.0005kN
    
    # Parametros atualizados:
    Ly = Ly + 0.0005               #Deslocamento Y total = 0.009
    E = (I-Ly)/Ly                  #Deformação
    S = E*e                        #Estresse (Tensão)
    # Movimento do Atuador:
    atuador.pos = vector(0, 0.01 - F,0)
    
    # Compressão do Bloco:
    bloco.size = vector(L + F, (H - F), W + 2*(F))   #Compressão em (X, Y, Z) de acordo com Coef. Poiss.
    bloco.pos = vector(0,-F/2 ,0)
    
    # Nova posição de acordo com a Tensão/Deformação:
    
    # Atualizando demais parâmetros
    pointer.pos = vector(0.05, 0.05 - F ,0)
    forceL.text = 'E = %1.0f N' %(e)
    tensaoL.text = 'Tensao = %1.0f N ' %(S*-1)
    deformaL.text = 'Deform. = %1.2f ' %(E)
    # Representar a movimentação de modo devagar
    time.sleep(0.4)

    


# In[ ]:




