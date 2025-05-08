valores = []
for c in range(0,5):
    n = int(input('insira um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('valor inserido no final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'valor inserido na posição {pos}')
                break
            pos+=1
print(f'A lista em ordem crescente é de {valores}')



