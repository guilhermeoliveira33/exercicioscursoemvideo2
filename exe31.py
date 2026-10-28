d = int(input('qual a distância da viagem? '))

p1=200 *0.50
p2=d*0.45

print('Você esá prestes a começar uma viagem de {:.2f}km.'.format(d))
if d <=200:
    print('E o preço da sua passagem será de R${:.2f}'.format(p1))

else:
    print('E o preço da sua passagem será de R${:.2f}'.format(p2))