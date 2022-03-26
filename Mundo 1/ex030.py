numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} e PAR.'.format(numero))
else:
    print('O número {} IMPAR.'.format(numero))