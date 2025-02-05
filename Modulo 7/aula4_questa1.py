#Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" 
# no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.

import os

#solicita a frase do usuario
frase = input("Digite uma frase: ")

#nomeia o arquivo
nome_arquivo = "frase.txt"

#caminho completo do arquivo
caminho_arquivo = os.path.join(os.getcwd(), nome_arquivo)

#salva a frase em um arquivo
with open("frase.txt", "w") as arquivo:
    arquivo.write(frase)

#imprime o caminho completo do arquivo salvo
print("Frase salva em:", os.path.abspath("frase.txt"))
