import os
import re

# Nome dos arquivos
arquivo_origem = "frase.txt"
arquivo_destino = "palavras.txt"

# Verificar se o arquivo de origem existe
if not os.path.exists(arquivo_origem):
    print(f"Erro: O arquivo {arquivo_origem} não foi encontrado.")
else:
    # Ler o conteúdo do arquivo de origem
    with open(arquivo_origem, "r") as arquivo:
        conteudo = arquivo.read()
    
    # Remover espaços em branco e caracteres não alfabéticos, deixando apenas palavras
    palavras = re.findall(r"[a-zA-ZÀ-ÖØ-öø-ÿ]+", conteudo)

    # Salvar cada palavra em uma nova linha no arquivo de destino
    with open(arquivo_destino, "w") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")

    # Ler o conteúdo do arquivo de destino para exibir
    with open(arquivo_destino, "r") as arquivo:
        conteudo_palavras = arquivo.read()

    # Exibir o conteúdo do arquivo palavras.txt
    print(f"Conteúdo do arquivo {arquivo_destino}:\n")
    print(conteudo_palavras)
