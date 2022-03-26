n1 = int(input('Um valor '))
n2 = int(input('Outro valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 #divisão inteira
e = n1 ** n2 #elevado ao quadrado
print('A soma e {}, o produto e {} e a divisão e {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))