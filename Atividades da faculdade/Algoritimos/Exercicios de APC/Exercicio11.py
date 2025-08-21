#Estrutura de repetição pra a tabuada de 1 à 10
n = 1

while n <= 10:
    i = 1
    print(f"Tabuada do {n}:")
    while i <= 10:
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
        i += 1
    print()  # Pula linha entre tabuadas
    n += 1
    
    