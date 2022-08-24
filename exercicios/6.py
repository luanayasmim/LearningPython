'''
6 - Ler dois números inteiros e exibir o quociente e o resto da divisão inteira entre eles.
'''

print(f'{"QUOCIENTE E DIVISÃO":-^40}')
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
quociente = numero1 // numero2
resto = numero1 % numero2

print(f'O quociente e o resto da divisão de {numero1}/{numero2} é respectivamente {quociente} e {resto}')