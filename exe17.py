ca= float(input('comprimento do cateto oposto: '))
co = float(input('comprimento do cateto adjacente: '))
hi =( co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))


# ou importando a clase math

from math import hypot
ca= float(input('comprimento do cateto oposto: '))
co = float(input('comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
