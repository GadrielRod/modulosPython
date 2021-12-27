from math import cos, tan, sin, radians
n = int(input('Digite um angulo qualquer: '))

print('O seno de {} é igual a: {:.2f}'.format(n, sin(radians(n))))
print('A tangente de {} é igual a: {:.2f}'.format(n, tan(radians(n))))
print('O cosseno de {} é igual a: {:.2f}'.format(n, cos(radians(n))))