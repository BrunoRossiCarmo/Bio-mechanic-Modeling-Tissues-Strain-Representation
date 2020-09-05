#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:52:05 2020

@author: bruno
"""

from vpython import *
from numpy import *
from matplotlib import *
from drawnow import *

m = 0.01 #massa em kg
L = 0.02 # em metros
H = 0.02 # em metros
W = 0.02 # em metros
x = 0.1  # em metros

# Parâmetros para definir a plataforma de apoio
larg = 0.2 # em metros
compr  = 0.2

# Definindo a aceleração inicial externa (Atuador)
a = 0 
FO = H

# Propriedades do Bloco (Material V1)


canvas()
#Definindo a plataforma de apoio de nosso bloco.
ground = box(pos = vector(0, 0, 0), size = vector(compr, 0.001, larg), color = color.green);

#Definindo o material (bloco).
bloco = box(pos = vector(-(compr/2)+x, H/2, W), size = vector(L, H, W), color = color.blue);
atuador = cylinder(pos=vector(-(compr/2)+(x-0.0002),FO, W), axis=vector(0,5,0), radius=0.015, size = vector(L, 0.0005, W), color = color.red)

#Seta que indica a força
pointer = arrow(pos=vector(0.03, 0.02+H, W),  axis = vector(0, -0.02, 0), shaftwidth = 0, color = color.red)

for cont in range(-40, 40):
    # Incremento na força
    a = a + 0.01
    FO = H - m*a
    # Atualizando demais parâmetros
    atuador.pos = vector(-(compr/2)+(x-0.0002),FO, W)


# In[ ]:





# In[ ]:





# In[ ]:




