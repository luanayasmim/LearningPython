''' 3. Dado o tamanho do raio de uma circunferência, calcular a área e o 
perímetro da mesma.'''

import math

raio=float(input("Informe a medida do raio de uma circunferência: "))
diametro= raio*2
area= (math.pi*diametro**2)/4
perimetro= (math.pi*2)*raio

print("A base do quadrado será: {:.0f}, e a altura será: {:.0f}".format(area, perimetro))