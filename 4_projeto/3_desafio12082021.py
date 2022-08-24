#Aula 12/08/2021 - Luana Yasmim - DS II

''' Desafio 1: Utilizando o For crie um programa que solicita um número ao o 
usuário e exibe a tabuada deste número.'''
# Solicitando o número a ser calculado:
x= int(input("Digite o número à ser multiplicado:\n"))
# Declarando a Array para a tabuada
tabuada= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Utilizando o For para percorrer a Array e fazendo o calculado
for numero in tabuada:
    print("{} X {} = {}".format(x, numero, x*numero))
    
print("="*40)

''' Desafio 2: Utilizando o For crie um programa que solicita uma palavra
para o usuário e então retorna quantas letras ela tem.'''
# Solicitando a palavra para o usuário
palavra= input("Digite uma palavra para a contagem: \n Exemplo: Pastel.")
# Utilizando o For para percorrer a palavra e fazer a contagem
for letra in palavra:
    print(palavra.index(letra)+1)

print("="*40)

''' Desafio 3: Crie um programa que solicite o código do produto e a quantidade,
calcule e exiba o total do item, então solicite novamente código e quantidade 
até que o usuário digite 0 (zero). Então exiba o total da compra.'''
# Informando o usuário como sair do programa
print("Digite o código do produto ou (0) zero para sair.\n")

print("="*40)

# Utilizando o while para iniciar o laço de repetição
while True:
    # Solicitando o código do produto para continuar com o programa
    cod_produto= input("Informe o código do produto:")
    # Se o código do produto for maior que 0 o programa irá pedir as outras
    # informações e continuar com a aplicação até o usuário digitar 0
    if cod_produto.upper()=="0":
        break
    else:
        qntd_produto=input("Digite a quantidade do produto:")
        nome_produto=input("Digite o nome do produto:")
        preco_produto= float(input("Informe o preço do produto: R$"))
        print("="*40)
        print("Código {} - Quantidade {} - Produto {} - R$ {}".format(cod_produto, qntd_produto, nome_produto, preco_produto))
        print("="*40)


