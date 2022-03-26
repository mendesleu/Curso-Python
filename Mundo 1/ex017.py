from math import hypot
co = float(input('Comprimento do Cateto Oposto '))
ca = float(input('COmprimento do Cateto Adijacente '))
hi = hypot(co, ca)
print('A impotenusa vai medir {:.2f}'.format(hi))