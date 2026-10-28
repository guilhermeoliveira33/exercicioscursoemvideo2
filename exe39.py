from datetime import date

a= int(input('Ano de nascimento: '))

today=date.today().year
idade=today-a


print('Quem nasceu em {} tem {} anos em 2026'.format(a,idade))
if idade<18:
    print('Ainda faltam {} anos para o alistamento'.format(18-idade))
    print('Seu alistamento será em {}'.format(a+18))
elif idade>18:
    print('você já deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(a+18))
else:
    print('Você tem que ser alistar IMEDIATAMENTE')