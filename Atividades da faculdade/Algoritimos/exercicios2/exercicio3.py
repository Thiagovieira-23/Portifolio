'''– F.U.P que peça a idade de várias pessoas e classifique-as como "Criança"
(0 a12), "Adolescente" (13 a 17), "Adulto" (18 a 59) ou "Idoso" (60+). Use
funções, if/elif/else e listas. No final a saída seria assim:
'''
q=int(input('Quantas Idades deseja cadastrar ?'))
idades=[]
classe=[]
for i in range(q):
    idade=int(input(f'Digite a idade da pessoa ! {i+1}: '))
    idades.append
    if idade <=12:
        classe.append(f'A pessoa {i+1} com a idade de {idade} é uma criança!')
       # print(f'A pessoa {i+1} com a idade de {idade} é uma criança!')
    elif idade>12 and idade<=17:
        classe.append(f'A pessoa {i+1} com a idade de {idade} é uma adolescente!')
       #print(f'A pessoa {i+1} com a idade de {idade} é uma adolescente!')
    elif idade>17 and idade<=59:
        classe.append(f'A pessoa {i+1} com a idade de {idade} é uma adulto!')
       #print(f'A pessoa {i+1} com a idade de {idade} é uma adulto!')
    elif idade>59:
       classe.append
       #print(f'A pessoa {i+1} com a idade de {idade} é uma idoso!')
    else:
        classe.append(f'A pessoa {i+1} com a idade de {idade} ta com a idade inválida!')
       # print(f'A pessoa {i+1} com a idade de {idade} ta com a idade inválida!')
print(f'\nResultado: {classe}')
