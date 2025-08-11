#arquivo = open('test.txt', 'w')#Abrindo um arquio e executando o modo de leitua 
#print(arquivo.readable())# Saber em resposta booleana se um arquivo pode ser lido ; TRUE pode ser lido False não pode
#print(arquivo.read())#lê o arquivo todo
#print(arquivo.readline()) #lê a primeira linha
#print(arquivo.readlines())#retorna uma lista do arquivo e assim vc pode anipular a lista
#arquivo.write('Sql')
#arquivo.close() # Fechar o arquivo


#Se vc executar a abertura do arquivo com w e escrever novas coisas nele, ele apaga o que já tinha e só fica no arquivo o q vc escreveu no código, com r+ ele fica o q já tinha e o que vc escreveu, só que precisa colocar um read depois de add novas informações.
#arquivo = open('test.txt', 'r+')
#print(arquivo.readable())
#print(arquivo.read())
#arquivo.write('Sql')
#print(arquivo.read())
#arquivo.close()

#Modo 'w' escreve no arquivo, apaga todo o conteúdo anterior assim que o arquivo é aberto, se o arquivo não existir ele cria.
#Modo 'r+' abre o arquivo para ler e escrever, não apaga o conteúdo existente, mas quando você escreve, ele sobrescreve a partir da posição atual do cursor,Se o arquivo não existir, dá erro.
#Modo a+ escreve no final e permite ler.
#Modo x cria um arquivo novo 
#Remover arquivos precisa importar biblioteca os
import os
if os.path.exists('text.txt'):
 os.remove('text.txt')
else:
 print('Esse arquivo não existe')

#Só remove se a pasta estiver vazia
os.redir('nova_pasta')

#PIP é o gerenciador de pacotes do pt; instalar, atualizar e remover bibliotecas e módulos, que são pacotes de funções e variáveis