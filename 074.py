from random import randint
numero = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print(f'Listagem: {numero}')
valores = sorted(numero)
print(f'Em ordem crescente: {valores}')
print(f'O menor valor da sequência foi {min(numero)} e o maior foi {max(numero)}  ')