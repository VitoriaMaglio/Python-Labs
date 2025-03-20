x = True
print(x)
print(int(x))
#0 = False
#1 = True
if x: #o que está dentro o bloco condicional é verdadeiro
    print('Hello')
else:
    print('X é false')

print(x ==0)
if x == 0:
    print('Verdadeiro')
else:
    print('Falso')


y = int(input('Digite um número: '))
print(f'Você digitou o número {y}') #   f pega o conteúdo do colchete e imprime
if y % 2 == 0:
    print('Par')
else:
    print('Ímpar')    
    
    
#conta +1 ?
#match case ?

nota = int(input('Digite uma nota de 0 a 10: '))
if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Bom')
elif nota >= 5:
    print('Regular')
else:
    print('Reprovado')
    

num = int(input('Digite um número: '))
if num == 0:
    print('Par')
elif num % 2 ==0:
    print('Par')
else:
    print('Ímpar')