 # Implemente sua solução aqui
def avalia_tabuleiro(tabuleiro):
    """
    Avalia o estado do tabuleiro do jogo da velha e retorna o vencedor ou 'Empate'.

    :param tabuleiro: Lista de listas representando o tabuleiro.
    :return: 'X', 'O' ou 'Empate'.
    """
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

    # Verifica colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    # Se ninguém venceu
    return "Empate"


# Exemplos de uso
tabuleiro1 = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'O']
]
print(avalia_tabuleiro(tabuleiro1))  # Saída: "Empate"

tabuleiro2 = [
    ['O', 'X', 'O'],
    ['X', 'O', 'X'],
    ['X', ' ', 'O']
]
print(avalia_tabuleiro(tabuleiro2))  # Saída: "O"

tabuleiro3 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]
print(avalia_tabuleiro(tabuleiro3))  # Saída: "X"