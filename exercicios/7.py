'''
7 - Solicitar a idade de uma pessoa em dias e informar na tela a idade em anos, meses e dias.
'''
print(f'{"IDADE FORMATADA":-^40}')
idade = int(input('Quantos anos você tem? '))
meses = idade * 12
dias = idade * 365
print(f'Você tem {idade} anos ou {meses} meses ou {dias} dias')
