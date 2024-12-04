### Q4.

#Você vai criar um sistema que registra os resultados dos jogos do Atlético MG ao longo de um campeonato. Seu sistema vai receber os resultados de todos os jogos
#do Galo, e deve calcular a pontuação do time sabendo que vitórias valem 3 pontos, empates 1 ponto e derrotas 0 pontos.
#Entrada: <br>
#A primeira linha de entrada é um inteiro N com a quantidade jogos do galo. Para cada jogo você deve ler 2 inteiros, o primeiro com a quantidade de gols 
#do galo e o segundo com a quantidade de gols do time oponente. 
#Saída: <br>
#Apresente a soma de vitórias, empates e derrotas do galo, junto com o cálculo da pontuação total.
#Ex:
#Entrada:
#4
#2
#0
#1
#1
#0
#3
#1
#0
#Saída:
#Vitórias: 2
#Empates: 1
#Derrotas: 1
#Pontuação: 7

### Escreva e execute seu código aqui

#Entrada de quantidade de jogos
n = int(input("Digite a quantidade de jogos do Galo: "))

#contadores iniciais
soma_vitorias, soma_empates, soma_derrotas = 0, 0, 0

#Comando/laço for para processar cada jogo
#jogo é inicializado e atualizado de acordo com range (intervalo), 0-n-1
for jogo in range(n):
    #solicita a quantidade de gols do galo e do oponente
    gols_galo = int(input("Digite a quantidade de gols do Galo no jogo: "))
    gols_adversario = int(input("Digite a quantidade de gols do Adversário no jogo: "))

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

