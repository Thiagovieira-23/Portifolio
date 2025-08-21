'''F.U.P que receba uma lista de números. (Primeiramente faça uma lista) O
Programa deverá retornar o maior número da lista. Podem ser 5 números. Use
uma estrutura de repetição para percorrer os elementos
'''
l=[]
for i in range(5):
    n=int(input(f'Digite 5 números {i+1} >'))
    l.append(n)
m=l[0]
for n in l:
    if n>m:
        m=n
print(f"A lista digitada foi: {l}")
print(f"O maior número da lista é: {m}")