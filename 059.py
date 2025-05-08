n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
resposta = ''
while resposta != '5':
    print('MENU \n[1]somar [2]multiplicar [3]maior [4]novos números [5]sair')
    resposta = str(input('O que você deseja fazer? '))
    if resposta == '1':
        print(20*'=')
        print(f'{n1}+{n2}={n1+n2}')
        print(20*'=')
    if resposta == '2':
        print(20*'=')
        print(f'{n1}x{n2}={n1*n2}')
        print(20*'=')
    if resposta == '3':
        if n1 > n2:
            print(20*'=')
            print(f'{n1} é maior que {n2}')
            print(20*'=')
        elif n1 == n2:
            print(20*'=')
            print(f'Os valores são iguais')
            print(20*'=')
        else:
            print(f'{n2} é maior que {n1}')
    if resposta == '4':
        n1 = int(input('Insira o novo valor do primeiro número: '))
        n2 = int(input('Insira o novo valor do segundo número:'))
    elif resposta == '5':
        print('Encerrado.')

