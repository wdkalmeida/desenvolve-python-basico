#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
#Chave de criptografia: gere um valor n aleatório entre 1 e 10
#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

import random

def encrypt(strings):
    #Criptografa uma lista de strings com base em uma chave de criptografia aleatória.
    
    #:param strings: Lista de strings a serem criptografadas.
    #:return: Uma tupla contendo a lista criptografada e a chave de criptografia.
    
    # Gera a chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)

    # Função para criptografar uma única string
    def criptografar_string(s):
        return ''.join(
            chr((ord(c) + chave - 33) % 94 + 33) if 33 <= ord(c) <= 126 else c
            for c in s
        )

    # Criptografa cada string da lista usando a função
    criptografado = [criptografar_string(s) for s in strings]

    return criptografado, chave

# Exemplo de uso
nomes = ["Maria", "Jose", "Carla"]
resultado, chave = encrypt(nomes)
print("Nomes criptografados:", resultado)
print("Chave da criptografia:", chave)
