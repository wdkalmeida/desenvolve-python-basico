def pares_unicos(numeros, soma_objetivo):
    """
    Encontra todos os pares únicos de números cuja soma seja igual ao valor objetivo.
    :param numeros: Lista de números inteiros.
    :param soma_objetivo: Valor objetivo da soma.
    :return: Lista de tuplas com os pares únicos.
    """
    vistos = set()
    pares = set()
    
    for numero in numeros:
        complemento = soma_objetivo - numero
        if complemento in vistos:
            # Adiciona o par na forma ordenada para evitar duplicatas
            pares.add(tuple(sorted((numero, complemento))))
        vistos.add(numero)
    
    return list(pares)

# Exemplo de uso:
nums = [3, 4, 5, 6, 7]
soma = 10
resultado = pares_unicos(nums, soma)
print("Pares únicos cuja soma é igual a", soma, ":", resultado)
