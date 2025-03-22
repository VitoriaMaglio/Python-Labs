
        
operacao = input('Digite um símbolo de uma operação matemática básica: ')
num_1 = float(input('Digite um número:  '))    
num_2 = float(input('Digite um número: '))
adicao = num_1 + num_2
sub = num_1 - num_2
mul = num_1 * num_2
div = num_1 / num_2
match operacao:
    case '+':
        print(f'{adicao}')
    case '-':
        print(f'({sub})')
    case '*':
        print(f'({mul})')
    case '/':
        print(f'({div})')
    case _:
        print('Operação não reconhecida')

#Peça ao usuário um número decimal e exiba-o formatado com duas casas decimais. 
x = float(input('Digite um número: '))
print(f'{x:.2f}')
 
 #Peça ao usuário um valor e exiba-o formatado como moeda brasileira (R$). 
x = float(input('Digite um valor: '))
novo_x = f'R$ {x:,.2f}'.replace(",","X").replace(".", ",").replace("X", ".")
print(novo_x)

valor = float(input('Digite um valor: '))
valor_novo= f'R$ {x:,.2f}'.replace("," , "X").replace(".", ",").replace("X", ".")
#Primeiro começa com f de f-string para formatar e aspas
#Depois colooca a símbolo do real e abre colchetes; depois coloca a variável; (:,.) e quantas casas decimais o número tem(2)
#Coloca .replace para substituir a vírgula que separa o milhar por um X temporário
#O segundo .replace serve para substituir o ponto que separa o decimal por vírgula, que é o formato br
#O terceiro .replace serve para substituir o X por um ponto como separador de milhar.
# !! Ponto separa milhar (1.000) e vírgula separa decimal (1.000,87)
print(valor_novo)