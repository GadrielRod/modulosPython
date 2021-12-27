from random import choice
n1 = str(input('digite o nome do primeiro participante: '))
n2 = str(input('digite o nome do segundo participante: '))
n3 = str(input('digite o nome do terceiro participante: '))
n4 = str(input('digite o nome do quarto participante: '))

venc = choice([n1, n2, n3 , n4])
print('O vencedor ou vencedora do sorteio é o(a): "{}"'.format(venc))