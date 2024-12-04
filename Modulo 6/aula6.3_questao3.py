#Crie e explique o código de uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
#Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
#Você deve imprimir a lista antes e depois da deleção. 
#Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
#Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

import random

# Cria uma lista com 20 elementos entre -10 e 10, gerados aleatoriamente
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontra o intervalo que possui a maior quantidade de números negativos
intervalo_negativos = []
for i in range(1, len(lista)):
    if lista[i] < 0:
        intervalo_negativos.append(i)
    else:
        if intervalo_negativos:
            break           
print("Intervalo de negativos:", intervalo_negativos)

# Deleta o intervalo de negativos da lista
for i in intervalo_negativos:
    del lista[i]

# Imprime a lista antes e depois da deleção
print("Editada:", lista)    
