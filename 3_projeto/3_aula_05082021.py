''' Aula 05/08/2021
Estruturas condicionais'''

num= int(input("Informe um número: "))
if num%2==0:
    print("Esse número é par.")
else:
    print("Esse número é ímpar.")
    
#######################################
nota1= int(input("Digite a primeira nota:"))
nota2= int(input("Digite a segunda nota:"))
media=(nota1+nota2)/2
if media>=7:
    print("="*15)
    print("Aluno aprovado!")
elif media<5:
    print("="*15)
    print("Aluno Reprovado")
else:
    print("="*15)
    print("Aluno ficou de recuperação")
    
print("A média do aluno é de {}".format(media))

######################################

temp= float(input("Digite a temperatura atual:"))
if temp<= 10:
    print("O clima está muito frio!")
elif temp> 10 and temp<= 20:
    print("O clima está agradável!")
elif 20< temp<= 25:
    print("O clima está agradável!")
elif 25< temp<= 30:
    print("O clima está quente!")
else:
    print("O clima está muito quente!")

######################################
print("Você quer uma notícia boa ou ruim?")
verifica= (input("Digite B para notícia boa ou R para ruim:"))
if verifica== "B" or verifica== "b":
    print("Amanhã é sexta-feira =D")
elif verifica== "R" or verifica== "r":
    print("Você tem lição de casa e trabalhos para fazer =(")
else:
    print("Digite apenas B ou R!")


