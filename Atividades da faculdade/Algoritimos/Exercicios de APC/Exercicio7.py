#Lê  o número informado
n=int(input('Informe um número inteiro > '))
#Verifica se ele é ìmpar ou par 
v=n%2
if v==0:
    print(f'{n} é um número par')
elif v==1:
    print(f'{n} é um número ímpar')
