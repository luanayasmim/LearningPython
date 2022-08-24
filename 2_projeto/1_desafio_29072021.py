#Aula 29/07/2021 - Luana Yasmim - DS II


''' DESAFIO 1: Crie um programa que receba um valor em metros e converta-o 
exibindo, convertido em milímetros '''
# Solicitando o valor de metros 
metros= float(input("Informe o valor em metros:"))
# Fazendo o cálculo da conversão
conversao= (metros*1000)
# Informando os valores obtidos
print("{:.0f} X {} = {:.0f}".format(metros, 1000,conversao))
print("O valor em milímetros será: {:.0f}".format(conversao))
print("_"*30)


''' DESAFIO 2: Escreva um programa que calcule o aumento de  salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento. Então
retornar o valor do aumento e do novo salário. '''
# Solicitando o valor do antigo salário
salario= float(input("Infome o valor do salário: R$"))
# Solicitando o valor da porcentagem de aumento
porcentagem= float(input("Digite o valor do aumento (em %):"))
#Transformando a porcentagem em número decimal
porcentagem= porcentagem/100
# Calculando o aumento e o novo salário
aumento= salario*porcentagem
novo_salario= salario+aumento
#Exibindo informações para o usuário
print("O valor do aumento será: R$", aumento)
print("O novo salário será de: R$", novo_salario)
print("_"*30)


''' DESAFIO 3: Faça um programa que solicite o preço de uma mercadoria
e o percentual de desconto. Então calcule e xiba o valor do desconto
e o preço a pagar '''
# Recebendo o preço do produto e do desconto
preco= float(input("Digite o preço do produto: R$"))
desconto= float(input("Informe o desconto (em %):"))
# Transformando a porcentagem em número decimal
desconto= desconto/100 
# Calculando o valor do desconto e do novo preço do produto
valor_desconto= preco*desconto
novo_preco= preco-valor_desconto
# Exibindo as informações obtidas para o usuário
print("Valor do desconto: R$", valor_desconto)
print("Valor à pagar: R$", novo_preco)
print("_"*30)



