n1 = float(input('escolha o primeiro número: '))
n2 = float(input('escolha o segundo número: '))
n3 = float(input('escolha o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é maior número da sequencia')
if n2 > n1 and n2 > n3:
        print(f'{n2} é o maior número da sequencia')
if n3 > n2 and n3 > n1:
            print(f'{n3} é o maior número da sequencia')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número da sequencia')
if n2 < n1 and n2 < n3:
        print(f'{n2} é o menor número da sequencia')
if n3 < n1 and n3 < n2:
            print(f'{n3} é o menor número da sequencia')
