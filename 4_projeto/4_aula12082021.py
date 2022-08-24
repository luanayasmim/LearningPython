# Aula 12-08-2021
# Laços de repetição

#Exemplo 1
palavra= "Paralelepipedo"
for letra in palavra:
    print(letra, end=" ")

#Exemplo 2    
lista=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for numero in lista:
    print(numero)

#Exemplo 3 
x=10
num1=int(input("Digite o número da tabuada desejada:"))
while x<=10:
    resultado=num1*x
    print("{} x {} = {}".format(num1, x, resultado))
    x+=1

#Exemplo 4
nome= input("Digite o nome do aluno:")
n=10
qtd=int(input("Digite quantas notas serão utilizadas para calcular a média:"))
total=10
while qtd>n:
    dig=float(input("Digite a nota do aluno"))
    total=total+dig
    n+=1
media=total/qtd
if media>=7:
    status="aprovado"
else:
    status="reprovado"
print("A média do {} foi {:.2f}, portanto ele está {}!!!".format(nome, media, status))

#Exemplo 5 
nome=input("Digite o nome do aluno:")
n=0
total=0
while True:
    dig=input("Digite a nota do aluno ou fim para encerrar:")
    if dig.upper()=="FIM":
        break
    total=total+float(dig)
    n+=1
media=total/n
if media>=7:
    status="aprovado"
else:
    status="reprovado"
print("A média do {} foi {:.2f}, portanto ele está {}!!!".format(nome, media, status))
