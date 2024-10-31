#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e 
# peça ao usuário para adivinhar o número.  Forneça feedback se o palpite é muito alto, muito baixo ou correto.
# Interrompa a execução somente quando o usuário acertar o palpite.
#Exemplo de interação:
#Adivinhe o número entre 1 e 10: 5
#Muito alto, tente novamente!
#Adivinhe o número entre 1 e 10: 3
#Correto! O número é 3.

import random

#Gera um número aleatorio entre 1 e 10
numero_aleatorio = random.randint(1, 10)

#Solicita ao usuário que adivinhe o número
palpite = int(input("Adivinhe o número entre 1 e 10: "))

#Verifica se o palpite é correto
while palpite != numero_aleatorio:
    if palpite > numero_aleatorio:
        print("Muito alto, tente novamente!")
    else:
        print("Muito baixo, tente novamente!")
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

#Exibe o resultado
print("Correto! O número é", numero_aleatorio)