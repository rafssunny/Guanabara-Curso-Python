n = 0
while True:
    n = int(input('Qual valor você quer ver a tabuada? '))
    if n < 0:
        break
    for c in range(0,11):
        print(f'{n}x{c}={n*c}', end = ' ➜ ')
    print('FIM')