#Informar a temperatura em C° para fazer a conversão em F°
print('Informe uma temperatura em graus Celsius')
tempc=float(input('>'))
#Converti a temperatua em Celsius para Fahrenheit
convert=tempc*(9/5)+32
#Apresenta a temperatura convertida
print(f'A temperatura convertida é de {convert}F°')