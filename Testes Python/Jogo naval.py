#Solicita ao usúario que informe o valor de N e M
N = int(input("Digite o número de linhas (N): "))
M = int(input("Digite o número de Colunas (M): "))

#Imprime o cabeçalho da coluna
print(" ", end=" ") # Espaço inicial para alinhamento do cabeçalho com coluna
for col in range(1, M +1):
    print(col, end=" ") #vai imprimir um número de colunas seguido de um espaço
print() #Pula para proxima linha

#Imprime o tabuleiro de batalha naval
for row in range(1, N + 1):
    print (row, end=" ") #Imprime um número da liha seguido de um espaço
    for col in range(M):
        print("/", end=" ") #Imprime a barra("/")para cada coluna, seguido de um espaço 
    print() #Pula para proxima linha após imprimir todas as colunas