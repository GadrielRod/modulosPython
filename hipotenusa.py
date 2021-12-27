from math import hypot

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

print('A hipotenusa de {} e {} é igual a: {:.2f}'.format(ca, co, hypot(ca, co)))
