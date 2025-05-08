def moeda(n):
    return f'R${n:.2f}'.replace('.',',')
def dobro(n,p = False):
    r = n*2
    if p == True:
        r = moeda(r)
    return r
def metade(n, p = False):
    r = n/2
    if p == True:
        r = moeda(r)
    return r
def aumentar(n, a, p = False):
    a = a/100
    r = n+(n*a)
    if p == True:
        r = moeda(r)
    return r
def diminuir(n, a , p = False):
    a = a/100
    r = n-(n*a)
    if p == True:
        r = moeda(r)
    return r
def resumo(n, a, r):
    print('-' * 40)
    print(f"{'RESUMO DO VALOR':^40}")
    print('-' * 40)
    print(f"{'Preço analisado:':<25}{moeda(n):>15}")
    print(f"{'Dobro do preço:':<25}{dobro(n, p=True):>15}")
    print(f"{'Metade do preço:':<25}{metade(n, p=True):>15}")
    print(f"{f'{a}% de aumento:':<25}{aumentar(n, a, p=True):>15}")
    print(f"{f'{r}% de redução:':<25}{diminuir(n, r, p=True):>15}")
    print('-' * 40)

