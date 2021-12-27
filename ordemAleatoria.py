from random import shuffle

n1 = str(input('digite o nome do primeiro participante: '))
n2 = str(input('digite o nome do segundo participante: '))
n3 = str(input('digite o nome do terceiro participante: '))
n4 = str(input('digite o nome do quarto participante: '))

lista = [n1,n2,n3,n4]
shuffle(lista)

print('A order a ser seguida será ')
print(lista)