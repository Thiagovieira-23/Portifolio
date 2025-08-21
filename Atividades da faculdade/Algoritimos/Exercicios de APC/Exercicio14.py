import random
segredo=random.randint(1,100)
# Outra pessoa (ou o próprio usuário) insere o número secreto
print("Digite um número de 1 a 100 (esconda da outra pessoa): ")
palpite = -1
cont=1

while palpite != segredo:
    palpite = int(input("Adivinhe o número: "))

    if palpite < segredo:
        print("Tente um número maior.")
        cont+=1
    elif palpite > segredo:
        print("Tente um número menor.")
        cont+=1

print("Parabéns, você acertou!")
print(f'você acertou em {cont} tentativas!')