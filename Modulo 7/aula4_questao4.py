#Escreva um programa em Python para executar o jogo, de acordo com as definições:
#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
#No início exiba o número de letras da palavra sorteada como underscores;
#Permita que o jogador insira letras para adivinhar a palavra;
#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
#Limite o número de tentativas para 6 (as partes do enforcado).

import random

# Função para imprimir o estado do enforcado
def imprime_enforcado(tentativas):
    enforcado = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(enforcado[tentativas])

# Lê o arquivo com palavras
with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = [palavra.strip() for palavra in arquivo if palavra.strip()]  # Ignora linhas vazias

# Escolhe uma palavra aleatória
palavra_secreta = random.choice(palavras)
tamanho = len(palavra_secreta)
palavra = "_" * tamanho
tentativas = 0  # Inicia o contador de tentativas como 0

# Loop principal do jogo
while palavra != palavra_secreta and tentativas < 6:
    print(f"\nPalavra: {palavra}")
    letra = input("Digite uma letra: ").strip().lower()

    if letra in palavra_secreta.lower():
        for i in range(tamanho):
            if palavra_secreta[i].lower() == letra:
                palavra = palavra[:i] + palavra_secreta[i] + palavra[i + 1:]
    else:
        tentativas += 1
        imprime_enforcado(tentativas)
        print(f"Tentativa errada! Você ainda tem {6 - tentativas} tentativas restantes.")

# Resultado do jogo
if palavra == palavra_secreta:
    print("\nParabéns! Você ganhou!")
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta)
