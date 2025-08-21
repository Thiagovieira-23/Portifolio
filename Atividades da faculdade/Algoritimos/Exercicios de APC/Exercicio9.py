#Lê as idades apresentadas e determina a classe 
p1=int(input('Idade da pessoa 1 > '))
p2=int(input('Idade da pessoa 2 > '))
p3=int(input('Idade da pessoa 3 > '))
#Definir as classes da p1
if p1>=0 and p1<=12 :
    print(f'Pessoa 1 com {p1} é uma criança. ')
elif p1>12 and p1<18:
    print(f'Pessoa 1 com {p1} é uma adolescente. ')
elif p1>=18:
    print(f'Pessoa 1 com {p1} é uma adulto. ')
elif p1<0:
    print('idade inválida')
#Definir classe da p2
if p2>=0 and p2<=12 :
    print(f'Pessoa 2 com {p2} é uma criança. ')
elif p2>12 and p2<18:
    print(f'Pessoa 2 com {p2} é uma adolescente. ')
elif p2>=18:
    print(f'Pessoa 2 com {p2} é uma adulto. ')
elif p2<0:
    print('idade inválida')    
#Definir classe da p3
if p3>=0 and p3<=12 :
    print(f'Pessoa 3 com {p3} é uma criança. ')
elif p3>12 and p3<18:
    print(f'Pessoa 3 com {p3} é uma adolescente. ')
elif p3>=18:
    print(f'Pessoa 3 com {p3} é uma adulto. ')
elif p3<0:
    print('idade inválida')