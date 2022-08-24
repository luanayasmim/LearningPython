''' 9. Faça um algoritmo que calcule e apresente o valor do volume de uma lata de óleo, dado 
seu raio e sua altura. '''
import math

raio=float(input("Informe o raio: "))
altura=float(input("Informe a altura: "))
volume=math.pi*(raio**2)*altura
print("O volume será {}".format(volume))