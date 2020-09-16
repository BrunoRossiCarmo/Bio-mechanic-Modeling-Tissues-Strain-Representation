from numpy import *
from vpython import *
import matplotlib.pyplot as plt
from drawnow import *


ground = box(pos=vector(0,0,0), size=vector(5,0.1,5))

caixa = box(pos=vector(0,0.5,0),size=vec(1,1,1), color=color.green)
cilindro = cylinder(pos=vec(0,1,0),radius=(0.5), color=color.yellow, axis=vector(0,1,0))

cilvec = vec(0,1.0,0)
caixavec = vec(1,1,1)
caixapos = vector(0,0.5,0)
E = 5000
Elabel = label(pos = vec(0,2.5,0), text = 'E = %d Pa' %(E))

deform = 0
tensao = 0
tensgraf = []
deformgraf = []
def makeFig():
    plt.plot(tensgraf, deformgraf, 'D-')
    plt.xlabel('Deformação')
    plt.ylabel('Tensão (N)')
    plt.title('Ensaio mecânico com tensão uniaxial')

while cilvec.y > 0.6:
    rate(100)
    cilindro.pos = cilvec
    cilvec.y = cilvec.y - 0.001
    
    
    caixa.size = caixavec
    caixavec.y = caixavec.y - 0.001
    
    caixa.size = caixavec
    caixavec.x = caixavec.x + 0.001
    
    
    caixa.size = caixavec
    caixavec.z = caixavec.z + 0.002
    
    caixa.pos = caixapos
    caixapos.y = caixapos.y - 0.0005
    
    deform = (0.5 - caixapos.y)/(caixapos.y)
    tensao = deform * 5000
    
    #tensgraf.append(tensao) 
    #deformgraf.append(deform)
    #drawnow(makeFig)
    
   
    
    Deformlabel = label(pos = vec(3,2.5,0), text ='Tensão = %.2f N' %(tensao))
    Deformlabel = label(pos = vec(-3,2.5,0), text ='Deformação = %.2f' %(deform))
    


    



