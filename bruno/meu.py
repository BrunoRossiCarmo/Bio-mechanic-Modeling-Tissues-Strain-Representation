from numpy import *
from vpython import *
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *
import time

# Parâmetros para definir o bloco e a mola
m = 0.01 # em kg
L = 0.02 # em metros
H = 0.02 # em metros
W = 0.02 # em metros
x = 0.1  # em metros

# Constrante elástica da mola
k = 80 # em N/m
# Parâmetros para definir a plataforma de apoio
d = 0.1 # em metros
LG  = 0.2

canvas()
#Definindo a plataforma
ground = box(pos = vector(0, 0, 0), size = vector(LG, 0.002, d));

# Definindo o bloco (massa-mola) vermelho que será apertado
block = box(pos = vector(0, H/2, 0), size = vector(L, H, W), color = color.red);

cilindro = cylinder(pos = vector(0, 5*H, 0), size = vector(L/3, H/3, W/3), axis = vector(0, H, 0),radius = 0.03, color = color.blue);

F = -5 # em Newtons

# Definindo a posição inicial do segundo sistema massa-mola de acordo com a lei de Hooke
x1 = x + F/k;

posCM = []
Forca = []

for cont in range(-50,50):
    F = F + 0.1
    x1 = x + F/k
    cilindro.pos = vector(0, -H/2, 0)
    Forca.append(F)
    posCM.append(x1)
    #drawnow(makeFig)
    time.sleep(0.3)
