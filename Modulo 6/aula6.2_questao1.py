#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
#A lista ordenada, sem modificar a lista original
#A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

import random

# Gera 20 valores inteiros aleatórios entre -100 e 100 e os armazena em uma lista
lista = [random.randint(-100, 100) for _ in range(20)]

# Exibe a lista ordenada, sem modificar a lista original
lista_ordenada = sorted(lista)
print("Lista ordenada (sem modificar a original):", lista_ordenada)

# Exibe a lista original
print("Lista original:", lista)

# Encontra o índice do maior valor da lista
indice_maior_valor = lista.index(max(lista))
print("Índice do maior valor da lista:", indice_maior_valor)

# Encontra o índice do menor valor da lista
indice_menor_valor = lista.index(min(lista))
print("Índice do menor valor da lista:", indice_menor_valor)
