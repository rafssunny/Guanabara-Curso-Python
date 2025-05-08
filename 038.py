n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número: '))
if n1 > n2:
    print('O \033[36mprimeiro\033[m valor é \033[32mmaior\033[m')
elif n1 < n2:
    print('O \033[36msegundo\033[m valor é \033[32mmaior\033[m')
else:
    print('\033[36mAmbos\033[m os valores são \033[33miguais\033[m')
