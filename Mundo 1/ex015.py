dias = int(input('Quuantos dias alugados: '))
km = float(input('Quantos Km rodados: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de  R$ {:.2f}'.format(pago))