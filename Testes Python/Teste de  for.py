## Escreva e execute seu código aqui

#Entrada de quantidade de jogos
n = int(input("Digite a quantidade de jogos do Galo: "))

#contadores iniciais    
soma_vitorias, soma_empates, soma_derrotas = 0, 0, 0

#Comando/laço for para processar cada jogo
#jogo é inicializado e atualizado de acordo com range (intervalo), 0-n-1
for jogo in range(n):
    #solicita a quantidade de gols do galo e do oponente
    gols_galo = int(input("Digite a quantidade de gols do Galo: "))
    gols_adversario = int(input("Digite a quantidade de gols do Adversário: "))

#Verifica resultados
    if gols_galo > gols_adversario:
        soma_vitorias += 1
    elif gols_galo < gols_adversario:
        soma_derrotas += 1
    else: # não é maior, não é menor sobra:
        soma_empates += 1

#imprimindo o resultado
    print(f"Vitórias: {soma_vitorias}")
    print(f"Empates: {soma_empates}")
    print(f"Derrotas: {soma_derrotas}")
    print("Pontuação: ", 3*soma_vitorias+soma_empates)