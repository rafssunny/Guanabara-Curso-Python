print('sequencia fibonacci')
n1 = 1
n3 = 0
contagem = int(input('Digite um número: '))
fim = 0
print('0')
print('1')
while fim != contagem-2:
    print(n1+n3)
    if fim % 2 == 0:
        n3 += n1
    else:
        n1+=n3
    fim += 1
