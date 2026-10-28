import math

a = float(input('digite o ângulo: '))

radianos = math.radians(a)

# calcular seno, cosseno e tangente

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('seno de {}°: {:.2f}'.format(a,seno))
print('cosseno de {}°: {:2f}'.format(a,cosseno))
print('tangente de {}: {:.2f}'.format(a,tangente))