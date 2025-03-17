
#identação : e da enter; o curso vai para a outra linha
#input : é o comando que recebe dados do usuário
#f-strings, que são strings formatadas, permitem incorporar expressões ou variáveis dentro de uma string de maneira clara e concisa. As expressões dentro de f-strings são delimitadas por chaves {}.
#número é sempre alinhado a direita 
#replace reposicionar 

nome= input("Digite seu nome: ")
print(f"Olá, {nome}, !")

nome = "Ana"
idade = 25
print(f"Meu nome é {nome} e tenho {idade} anos.")

preco = 123.45678
print(f'Preço formatado: {preco:.3f}')

nome = 'Python'
print(f'.{nome:.<10}.') #Alinhado à esquerda
print(f'.{nome:.^10}.') #Alinhado à Centralizado
print(f'.{nome:.>10}.') #Alinhado à direita

#1) número interio com zeros à esquerda (4 casas)
num_int = 10
print(f'{num_int:04d}') #0010

A= 11
B= 3
print(A+B*A)
print(B*A+B)
print(A//B)
print(B%A)
print(A%B)
print(B//A)
print(B-A/B)
print(A/B-A*B)
print(10+A%B)
print(10-B//A)
print(B//A-50)
print(A+B%A-A//B*2)
print(A*(B+A)-(A-B)/2)

x= True
y= False
print(x,y)
print(x or y)
print(y or x)