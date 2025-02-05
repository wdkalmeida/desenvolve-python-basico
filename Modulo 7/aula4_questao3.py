#crie um script em Python que abra o arquivo para leitura e imprima: 
#O texto das primeiras 25 linhas
#O número de linhas do arquivo
#A linha com maior número de caracteres
#O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas 
# e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras)

import os
import re

# Nome do arquivo a ser lido
nome_arquivo = "estomago.txt"

try:
    # Abrir o arquivo em modo de leitura
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # Ler o conteúdo do arquivo
        conteudo = arquivo.read()

        # Imprimir o texto das primeiras 25 linhas
        linhas = conteudo.splitlines()  # Divide o conteúdo em linhas
        print("Texto das primeiras 25 linhas:")
        for i, linha in enumerate(linhas[:25], start=1):
            print(f"{i}: {linha}")

        # Imprimir o número de linhas do arquivo
        print("\nNúmero de linhas do arquivo:")
        print(len(linhas))

        # Encontrar a linha com o maior número de caracteres
        linha_maior_caracteres = max(linhas, key=len)
        print("\nLinha com o maior número de caracteres:")
        print(linha_maior_caracteres)

        # Contar o número de menções aos nomes "Nonato" e "Íria"
        # Inclui variações de maiúsculas/minúsculas e ignora substrings
        num_mensagens_nonato = len(re.findall(r"\bNonato\b", conteudo, re.IGNORECASE))
        num_mensagens_iria = len(re.findall(r"\bÍria\b", conteudo, re.IGNORECASE))
        print("\nNúmero de menções aos personagens Nonato e Íria:")
        print(f"Nonato: {num_mensagens_nonato}")
        print(f"Íria: {num_mensagens_iria}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")




