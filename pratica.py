from math import sqrt
import random
from random import triangular
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual {:.2f}'.format(num, raiz))

n = random.randint(1, 6)
print(n)

n1 = random.triangular(4, 5)
print('{:.2f}'.format(n1))