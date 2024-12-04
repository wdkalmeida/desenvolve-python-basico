#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores),
#os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … ) 

#Recebendo a quantidade de elementos e seus valores
n = int(input("Digite a quantidade de elementos: "))
lista = []
for _ in range(n):
    elemento = int(input())
    lista.append(elemento)

#Imprime a lista original
print("Lista original:", lista)

#Imprime os 3 primeiros elementos
print("Os 3 primeiros elementos:", lista[:3])

#Imprime os 2 ultimos elementos 
print("Os 2 ultimos elementos:", lista[-2:])

#Imprime a lista invertida (do fim para o começo)
print("A lista invertida:", lista[::-1])

#Imprime os elementos de índice par (0, 2, 4…)
print("Os elementos de índice par:", lista[::2])

#Imprime os elementos de índice ímpar (1, 3, 5…)...)
print("Os elementos de índice ímpar:", lista[1::2]) 
