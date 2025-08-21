'''1 – F.U.P que solicite ao usuário digitar números e armazene-os em uma lista.
Pode ser 5 números. E depois pergunte ao usuário qual número deseja
procurar e diga se ele está ou não na lista. Use if e else.
'''
l=[]
for i in range(5):
    n=int(input(f'Digite 5 números {i+1} >'))
    l.append(n)

print('Qual número você deseja encontrar ?')
achar=int(input('digiter o número desejado > '))
if achar in l:
    print(f'O número {achar} está armazenado')
else:
    print(f'O número {achar} NÃO está armazenado')


