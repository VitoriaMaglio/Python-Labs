
   # Solicitar o peso e altura do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Classificar o IMC
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}. Peso normal.")
elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f}. Sobrepeso.")
else:
    print(f"Seu IMC é {imc:.2f}. Obesidade.")
    
    
num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite um número: '))
num_3 = float(input('Digite um número: '))

# Comparar os números para encontrar o maior
if num_1 > num_2 and num_1 > num_3:
    print(f'O maior número é {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'O maior número é {num_2}')
else:
    print(f'O maior número é {num_3}')