''' 8. Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), leu um 
valor de temperatura em Fahrenheit e exibi-lo em Celsius '''
fahrenheit=float(input("Digite a temperatura em fahrenheit: "))
celsius=5/9*(fahrenheit-32)
print("A temperatura em celsius será {}".format(celsius))