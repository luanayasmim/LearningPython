# Luana Yasmim - DS 2º módulo - Python

# Lista de exercícios

''' 1. Dado o tamanho da base e da altura de um retângulo, calcular a sua área 
e o seu perímetro. '''

base=float(input("Informe a base do retângulo:"))
altura=float(input("Informe a altura do retângulo:"))
area=base*altura
perimetro=base*2+altura*2

print("A área do retângulo será: {:.0f}, e a altura será: {:.0f}".format(area, perimetro))