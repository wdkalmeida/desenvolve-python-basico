#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores.
#Peça ao usuário o valor de n
import random
import math

#Solicita ao usuário o valor de n
n=int(input("Digite o valor de n: "))

#Gera n valores inteiros aleatórios entre 0 e 100 e calcula a soma dos valores
valores = [random.randint(0, 100) for i in range(n)]
soma_valores = sum(valores)

#Calcula a raíz quadrada da soma dos valores
raiz_quadrada = math.sqrt(soma_valores)

#imprime(exibe) o resultado5
print("Os valores gerados foram:", valores)
print("A soma dos valores:", soma_valores)
print("A raíz quadrada da soma dos valores:", round(raiz_quadrada,2))

