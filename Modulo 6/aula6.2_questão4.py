#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores.
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da 
# primeira lista, adicionando ao final os elementos remanescentes da maior lista.
#Exemplo de interação via terminal (entradas em negrito):
#Digite a quantidade de elementos da lista 1: 4
#Digite os 4 elementos da lista 1:
#1
#2
#3
#4Digite a quantidade de elementos da lista 2: 6
#Digite os 6 elementos da lista 2:
#5
#6
#7
#8
#9
#10Lista intercalada: 1 5 2 6 3 7 4 8 9 10

#Recebendo a quantidade de elementos para a primeira lista e seus valores
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {n1} elementos da lista 1:")
for _ in range(n1):
    elemento = int(input())
    lista1.append(elemento)

#Recebendo a quantidade de elementos para a segunda lista e seus valores
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {n2} elementos da lista 2:")
for _ in range(n2):
    elemento = int(input())
    lista2.append(elemento)

#Combina as listas de forma alternada
lista_intercalada = []
for i in range(max(n1, n2)): #Itera até o tamanho da maior lista
    if i < n1: #Adiciona o elemento da lista1 se houver
        lista_intercalada.append(lista1[i])
    if i < n2: #Adiciona o elemento da lista2 se houver
        lista_intercalada.append(lista2[i])

#Imprime a lista intercalada
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))  
