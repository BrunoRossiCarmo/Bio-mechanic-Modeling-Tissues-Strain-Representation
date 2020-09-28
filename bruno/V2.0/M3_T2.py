from vpython import *
from numpy import *
import matplotlib.pyplot as plt
from drawnow import *
import math
import time

# Parâmetros principais:
L = 0.2 # em metros
H = 0.2 # em metros
W = 0.2 # em metros

# Propriedades Iniciais:
e = 8000            #Módulo de Young (kPa)
E = 0               #Deformação
M = 0               #Movimento Atuador
S = 0               #Stress
X = 0

# Parâmetros para movimento do atuador:
I = H           #Posição Inicial
Ly = I          #Deslocamento pelo eixo Y.

# Definindo o material (bloco).
bloco = box(pos = vector(0, 0, 0), size = vector(L, H, W), color = color.blue);

# Definindo o atuador que irá realizar a compressão do material.
atuador = cylinder(pos=vector(0, 0.1 ,0), axis=vector(0,5,0), radius=0.20, size = vector(L, 0.01, W), color = color.red)

# Caixas de texto.
forceL=label(pos = vec(0,0.6,0), text = 'E = %1.1f N' %(e))
tensaoL=label(pos = vec(0.7,0.6,0), text = 'Tensao = %1.1f ' %(0))
deformaL=label(pos = vec(-0.7,0.6,0), text = 'Desloc. = %1.1f ' %(E))

# Definindo a plataforma de apoio de nosso bloco.
ground = box(pos = vector(0, -(H/2) , 0), size = vector(2, 0.01, 1))

# Seta que indica a força
pointer = arrow(pos=vector(0.5, 0.5 ,0),  axis = vector(0, -0.2, 0), shaftwidth = 0, color = color.red)

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
for cont in range(0, 100):
    
    #Movimentação:
    M =  M + (math.sin(math.pi/12*(cont)))*0.01
    
    # Deslocamento:
    Ly = Ly + (math.sin(math.pi/12*(cont)))*0.01
     
    # Deformação:
    E = (I-Ly)/I 
    
    # Estresse
    S = E*e          #Não conseguimos representar o comportamento viscoelástico (histerese)
                     #Então vamos apresentar um comportamente elástico linear oscilante.
    
    # Movimento do Atuador:
    atuador.pos = vector(0, 0.1 - M,0)
    
    # Compressão do Bloco:
    bloco.size = vector(L + M, (H - M), W + 2*(M))   #Compressão em (X, Y, Z) de acordo com Coef. Poiss.
    bloco.pos = vector(0,-M/2 ,0)
    
    # Posição da Seta:
    pointer.pos = vector(0.5, 0.5 - M ,0)
    
    # Atualizando demais parâmetros
    pointer.pos = vector(0.5, 0.5 - M ,0)
    forceL.text = 'E = %1.0f ' %(e)
    tensaoL.text = 'Tensao = %1.0f N ' %(S)      #Seu valor deve ser apresentado em módulo.
    deformaL.text = 'Deform. = %1.2f ' %(E)      #Seu valor deve ser apresentado em módulo.
    
    # Atualizando os vetores para o gráfico mostrado em tempo real
    Stress.append(S*-1) 
    Strain.append(E*-1)
    drawnow(makeFig)
    
    # Representar a movimentação de modo devagar
    time.sleep(0.005)
