from math import cos, sin, tan, radians
angulo1 = float(input('Digite o valor do Ângulo que você deseja:'))
angulo = radians(angulo1)
print(f'O ângulo {angulo1} possui\n seno: {sin(angulo):.2f}\n cosseno: {cos(angulo):.2f}\n tangente: {tan(angulo):.2f}')