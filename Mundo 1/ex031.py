distancia = float(input('Qual e a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km')

'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''

preço = distancia * 0.50 if distancia <= 200 else distancia *0.45

print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))