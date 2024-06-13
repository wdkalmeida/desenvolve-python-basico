#Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python
#que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False)
#e quantas vezes venceu um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:
# a- tiver entre 16 e 18 anos
# b- já tiver jogado pelo menos 3 jogos
# c- já ter vencido pelo menos 1 jogo, 
#Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal,
#com entradas de dados destacadas em negrito e as impressões de seu código em itálico (apenas para facilitar sua
#visualização).

#entrada de dados
#Idade: 16 a 18
idade  = int(input("Digite sua idade: "))

#Já jogou pelo menos 3 jogos:
Numero_jogos = int(input("Número de jogos: "))

#jogos vencidos: minimo 1
vitorias = int(input("Jogos vencidos: "))

#processamento
a = idade >=16 and 18
b = Numero_jogos >= 3
c = vitorias >= 1
#apto a entrar no clube: True
apto = a and b and c

#saida
print(f"Apto para entrar no time de jogos de tabuleiro: {apto}")

