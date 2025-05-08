print('É número primo? ')
numero = int(input('Insira o número: '))
prova = 0
for x in range(1, numero+1):
    calculo = numero%x
    if calculo == 0:
        prova+=1
if prova == 2:
    print('É primo')
else:
    print('Não é primo')