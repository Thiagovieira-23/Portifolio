'''4 – F.U.P que leia números até que o usuário digite 0. Armazene os números
em uma lista e, ao final, mostre a soma total.'''
numeros = []  # lista para armazenar os números

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break  
    numeros.append(num)  

soma_total = sum(numeros)

print("\nNúmeros digitados:", numeros)
print("Soma total:", soma_total)