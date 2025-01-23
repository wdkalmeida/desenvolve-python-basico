import random

def embaralhar_palavras(frase):
    """
    Embaralha as letras internas de cada palavra de uma frase, 
    mantendo a primeira e a última letra no lugar.
    
    :param frase: Uma string representando a frase original.
    :return: Uma string com as palavras modificadas.
    """
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Função para embaralhar uma palavra
    def embaralhar(palavra):
        if len(palavra) <= 3:  # Palavras pequenas não precisam ser embaralhadas
            return palavra
        # Separa a primeira e última letras
        primeira, ultima = palavra[0], palavra[-1]
        # Embaralha as letras do meio
        meio = list(palavra[1:-1])
        random.shuffle(meio)  # Embaralha as letras internas
        # Reconstrói a palavra
        return primeira + ''.join(meio) + ultima

    # Aplica a função de embaralhar em cada palavra da frase
    palavras_embaralhadas = [embaralhar(palavra) for palavra in palavras]
    
    # Junta as palavras novamente em uma frase
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
frase = input("Digite uma frase: ")
frase_embaralhada = embaralhar_palavras(frase)
print(frase_embaralhada)

