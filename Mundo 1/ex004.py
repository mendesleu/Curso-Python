#mostra o tipo de variavel
n = (input ('Digite algo: '))
print ('O tipo primitivo da variavel e', type(n))
print ('Só tem espaço', n.isspace())
print ('E um numero', n.isnumeric())
print ('E alfabetico', n.isalpha())
print ('E alfanumerico', n.isalnum())
print ('Esta em maiusculo', n.isupper())
print ('Esta em minusculas', n.islower())
print ('Esta capitlizada', n.istitle())