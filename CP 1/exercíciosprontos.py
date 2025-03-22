#solicite um número inteiro ao usuário e exiba-o sempre com 5 dígitos, preenchendo com zeros à esquerda.
x = int(input('Digite um valor: '))
print(f'{x:05d}')
# 0 : preenche com zeros à esquerda
# 5 : indica que o número terá sempe 5 dígitos
# d : indica que é um número inteiro decimal

#preencha com zeros à direita
x = int(input('Digite um número: '))
print(f'{x:<5}'.replace(" ", "0"))

#Exiba um número em notação científica
x = float(input('Digite um número: '))
print(f'{x:.2e}')
# e : formata o número em notação científica
# .2 : exibe duas casas decimais antes de e

#Exibir um número com separadores de milhar
x = int(input('Digite um valor: '))
print(f'{x:,}') 
# , : insre o separador de milha automaticamente

texto = input('Digite um texto: ')
maiusculas = texto.upper()
minusculas = texto.lower()
capitalizado = texto.capitalize()
print(f'maiusculas: {maiusculas}')
print(f'minusculas: {minusculas}')
print(f'capitalizado: {capitalizado}')


 #Peça ao usuário para digitar uma cor do semáforo ("vermelho", "amarelo" ou "verde") e exiba a ação correspondente: - "Vermelho" → "Pare!" - "Amarelo" → "Atenção!" - "Verde" → "Siga!" - Qualquer outra entrada → "Cor inválida! "Dica: Use match - case para comparar as cores.  
 
cor = input('Digite uma cor do semáforo: ')
match cor:
    case 'vermelho':
        print('Pare')
    case 'verde':
        print('Continue')
    case 'amarelo':
        print('Atenção')
    case _ :
        print('Cor inválida')