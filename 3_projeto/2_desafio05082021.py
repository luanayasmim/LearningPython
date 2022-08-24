#Aula 05/08/2021 - Luana Yasmim - DS II

''' Desafio 1: Crie um programa que receba dois números e então exiba, se o 
primeiro é maior, se o segundo é maior ou se são iguais '''
# Solicitando os números para o usuário
num1= float(input("Insira o primeiro valor:"))
num2= float(input("Insira o segundo valor:"))
# Comparando os números
if num1>num2:
    print("O primeiro número ({:.0f}) é maior!".format(num1))
elif num1<num2:
    print("O segundo número ({:.0f}) é maior!".format(num2))
else:
    print("Os dois números são iguais!")
print("_"*30)

  
''' Desafio 2: Crie um programa que solicite um salário ao usuário e calcule o 
desconto do INSS. Salário até R$ 1693,72 - 8%. Salário maior que R$ 1693,72 e 
menor que R$ 2822,90 - 9%. Salário a partir de R$ 2822,90 - 11% '''
# Solicitando o valor do salário
salario= float(input("Infome o valor do salário: R$"))
# Comparando o salário para obter o desconto do INSS
if salario<= 1693.72:
    inss= salario*0.08
    salario_inss= salario-inss
    print("O inss será de 8%, com o valor: R$ {:.0f}. E o salário será: R$ {:.0f}".format(inss,salario_inss))
elif salario>1693.72 and salario<2822.90:
    inss= salario*0.09
    salario_inss= salario-inss
    print("O inss será de 9%, com o valor: R$ {:.0f}. E o salário será: R$ {:.0f}".format(inss,salario_inss))
else:
    inss= salario*0.11
    salario_inss= salario-inss
    print("O inss será de 11%, com o valor: R$ {:.0f}. E o salário será: R$ {:.0f}".format(inss,salario_inss))
print("_"*30)   


''' Desafio 3: Faça um programa que solicite que o usuário digite um número, 
depois outro, e por ultimo a opção: 1 para Soma. 2 para Subtração. 3 para
Multiplicação. 4 para Divisão. Então calcule e exiba o resultado '''
# Obtendo valores e a opção do usuário
n1= float(input("Insira o primeiro valor:"))
n2= float(input("Insira o segundo valor:"))
print("Escolha dentre as seguintes opções:\n 1 para Soma\n 2 para Subtração\n 3 para Multiplicação\n 4 para Divisão")
opcao= int(input("Insira a sua opção:"))
# Fazendo comparações para calculo
if opcao==1:
    resultado=n1+n2
    print("{:.0f}+{:.0f}={:.0f}".format(n1, n2, resultado))
elif opcao==2:
    resultado=n1-n2
    print("{:.0f}-{:.0f}={:.0f}".format(n1, n2, resultado))
elif opcao==3:
    resultado=n1*n2
    print("{:.0f}x{:.0f}={:.0f}".format(n1, n2, resultado))
elif opcao==4:
    resultado=n1/n2
    print("{:.0f}/{:.0f}={:.0f}".format(n1, n2, resultado))
else:
    print("Opção inválida!")
print("_"*30)



