numero = int(input('insira um número'))
base = str(input('escolha a base de conversão binário(1)/octal(2)/hexadecimal(3): ')).strip()
if base == '1':
    print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif base == '2':
    print(f'O número {numero} convertido para octal é {oct(numero)[2:]}')
elif base =='3':
    print(f'O número {numero} convertido para {hex(numero)[2:]}')
else:
    print('\033[1;31minsira um valor entre 1 a 3.')
