#lê os números e apresenta o maior 
n1=int(input('Informe um número 1 >'))
n2=int(input('Informe um número 2 >'))
n3=int(input('Informe um número 3 >'))
#Determina qual é o maior para printar na tela 
if n1>n2 and n1>n3:
    print(f'{n1} é o maior número')
elif n2>n1 and n2>n3:
    print(f'{n2} é o maior número')
elif n3>n1 and n3>n2:
    print(f'{n3} é o maior número')
#verificar se realmente são número diferentes 
else:
    print('São números iguais')




