from datetime import date
ano = int(input('Digite o ano de nascimento: '))

idade = date.today().year - ano

print('você nasceu no ano de {} e tem {} anos'.format(ano,idade))
if idade <=9:
   print('Sua categoria é MIRIM')
elif idade <=14:
    print('Sua categoria é INFANTIL')
elif idade <=19:
    print('Sua categoria é SÊNIOR')
elif idade == 19:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER ')