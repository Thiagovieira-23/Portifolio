'''5 – F.U.P que leia as notas de alunos até que o usuário digite uma nota
negativa. Armazene as notas em uma lista. No final do programa deverá
mostrar:
 A soma total das notas
 A média das notas
 A maior e menor nota
'''
numeros = [] 

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break  
    numeros.append(num)  

soma_total = sum(numeros)
media=soma_total/len(numeros)
maior = max(numeros)
menor = min(numeros)
print(f'A soma total das notas é : {soma_total}. \n A média das Notas é: {media} \n A maior nota é : {maior}\n A menor nota é : {menor} ')