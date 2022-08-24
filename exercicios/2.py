''' 2. Dado o tamanho do lado de um quadrado, calcular a área e o perímetro 
do mesmo. '''

lado=float(input("Informe a medida do lado de um quadrado: "))
area=lado**2
perimetro=lado*4

print("A base do quadrado será: {:.0f}, e a altura será: {:.0f}".format(area, perimetro))