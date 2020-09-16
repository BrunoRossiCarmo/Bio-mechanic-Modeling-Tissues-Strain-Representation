# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 01:00:06 2020

@author: filip
"""

from numpy import *
from vpython import *
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import time

m = 0.01 
L = 0.02 
H = 0.02 
W = 0.02 
x = 0.1
R = 0
E= 10000
Def = 0

d = 0.1
LG = 0.2

ground = box(pos = vector(0, -0.01, 0), size = vector(LG, 0.002, d));

block = box(pos = vector(-(LG/2)+x, H, W), size = vector(L, H, W), color = color.blue, axis=vector(0,0,0));
cylinderO = cylinder(pos = vector(-(LG/2)+x, H-0.01, W), size = vector(1.5*L, 1.5*H, 1.5*W), color = color.orange, axis=vector(0,1,0));
#arrow1 = arrow(pos = vector(-(LG/3)+x, H+0.01, W), size = vector(L, H, W), color = color.red);


EBox = label(pos = vec(-0.06, 0.06, 0), text = 'E = %d Pa' %(E))

tenPA = []
Deform = []

plt.ion()
def grafico():
    plt.plot(tenPA, Deform, '-bo')
    plt.xlabel('Deformação')
    plt.ylabel('Tensão (N)')
    plt.title('Ensaio Mecanico')


for cont in range(0, 20):
    rate(3)
    R = R + 0.0007
    #print(R)
    cylinderO.pos = vector(-(LG/2)+x, H-0.01-R, W)
    block.size = vector(L+R, (H - R), W+2*(R))
    block.pos = vector(-(LG/2)+x, -R/2, W)
    Def = ((L-(L+R))/L,(H-(H - R))/H, (W-(W+2*(R)))/W)
    Defy = (H-(H - R))/H
    #print(Defy)
    Tensao = E*Defy*exp(-5*E)
    print(Tensao)
    EBox = label(pos = vec(0, 0.06, 0), text = 'Deformacao = %1.2f' %(Defy))
    EBox = label(pos = vec(0.06, 0.06, 0), text = 'Tensao = %1.2f N' %(Tensao))
    tenPA.append(Tensao)
    Deform.append(Defy)
    drawnow(grafico)
    time.sleep(0.005)


    
    


    













    
        
        
        
        
        

