#Aula 02 - 29/07/2021

#Exemplos de comandos:
'''Bloco de comentário'''

print ('Hello World') 
print('Hello\nWorld') # \n insere uma quebra de linha
print('='*10)         # Insere 10x o sinal de igual
print('3 + 4 = ',(3+4)) #Adição
print('3 - 4 = ',(3-4)) #Subtração
print('3 x 4 = ',(3*4)) #Multiplicação
print('3 / 4 = ',(3/4)) #Divisão
print('2 ^ 2 = ',(2**2)) #Potenciação
print("Nota:10\nNota:8 => média",(10+8)/2) #Média


#Exemplo de Variáveis
nome= "Luana" #Cria uma variável nome e atribui o valo entre as aspas
idade= 17 #Cria a variável idade e atribui 17
matriculado= True #Variável do tipo Boolean
mensalidade= 79.9 #Tipo float

print("A variável nome tem o tipo: ",type(nome)," e o valor: ", nome)
print("A variável idade tem o tipo: ",type(idade)," e o valor: ", idade)
print("A variável matriculado tem o tipo: ",type(matriculado)," e o valor: ",matriculado)
print("A variável mensalidade tem o tipo: ",type(mensalidade)," e o valor: ", mensalidade)


#Exemplo de entrada de dados
x=input("Digite um número: ")
# x receberá o valor digitado pelo usuário
print("Você digitou: ",x)
#Exibe na tela o valor de x
nome1= input("Digite o seu nome: ")
# nome receberá o valor digitado pelo usuário
print("Você digitou {}".format(nome1))
#Exibe na tela o valor obtido em nome
print("Bem-vindo(a) {}!".format(nome1))
#Exibe na tela o valor obtido em nome


#Conversão de tipos de dados
num1= int(input("Digite um número: ")) #Recebe o valor
num2= int(input("Digite um número: ")) #Recebe o valor
soma= (num1+num2)
print("A soma dos dois números é: ", soma)
print("{}+{}={}".format(num1, num2, soma))
'''PS.: Podemos utilizar o .format para facilitar o nosso print, podendo marcar
a posição onde aparecerá a variável com abre e fecha chaves {} substituindo:
print(num1, "+", num2, "=", soma)
Por isto: print("{}+{}={}".format(num1, num2, soma))'''

