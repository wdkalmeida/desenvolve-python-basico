### Q5.

#Faça um programa que lê dois inteiros N e M, e imprime na tela um campo de batalha naval. O tabuleiro deve possuir N linhas e M colunas. 
#A primeira linha é composta por um espaço em branco e o cabeçalho das colunas, ou seja, valores de 1 a M. As N linhas seguintes iniciam com o cabeçalho da linha, 
#ou seja, seu número, seguido de M caracteres "/" (barra) indicando uma possível posição jogável. 
#Exemplo:
#Entrada:
#5
#4

#Saída:
#  1 2 3 4 
# 1 / / / / 
# 2 / / / / 
# 3 / / / / 
# 4 / / / / 
# 5 / / / / 

#Para esse exercício, precisamos lembrar que o comando print implicitamente adiciona uma quebra de linha ao final da impressão. 
#Podemos interferir no final da impressão adicionando mais uma entrada ao print. No exemplo, finalizamos cada linha com um espaço em branco:
#print("Texto qualquer", end = " ")

### Escreva e execute seu código aqui

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