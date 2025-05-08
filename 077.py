palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programar', 'futuro'
for c in palavras:
    print(f'\nA palavra {c} tem ', end = '')
    for n in c:
        if n in 'aeiou':
            print(n, end = ' ')