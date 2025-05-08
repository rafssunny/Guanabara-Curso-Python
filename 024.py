cidade = str(input('insira o nome da sua cidade: '))
cidade = cidade.lower()
cidade = cidade.strip(' ')
print(f'Sua cidade começa com santos? {cidade.startswith('santo')}')