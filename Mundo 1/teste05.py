import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual {}'.format(num, math.ceil(raiz))) #arredonda para cime
print('A raiz de {} é igual {}'.format(num, math.floor(raiz))) #arredonda para baixo