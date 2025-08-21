#Ler o valor da compra 
compra=float(input('Insira o valor da compra > '))
#Verificar se o valor da compra é o suficiente para aplicar o desconto 
if compra>100:
    desconto= compra*0.1
    vf=compra-desconto
    print(f'Valor final da compra fica R${vf}, e foi dado o desconto de R${desconto}')
else:
    print('Valor de compra é de {compra}')