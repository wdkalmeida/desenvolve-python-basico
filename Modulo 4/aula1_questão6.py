
#Exercício 6
#Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano,
#quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório
#utiliza três tipos de cobaias: sapos, ratos e coelhos.
#Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados.
#As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas
#e um caractere Tipo ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).
#Saída: Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia e o percentual
#de cada uma em relação ao total de cobaias utilizadas.
  #Entradas de dados
qtdExperimentos = int(input("Quantos experimentos? "))
qtdCobaias = 0
qtdSapo = 0
qtdRato = 0
qtdCoelho = 0
i = 1
#for x in range(qtdExperimentos):
#    info = input("Qtd de cobaias e animal: ")
#    infos = info.split(" ")
#    qtd = int(infos[0])
#    tipo = infos[1].upper()[0]
  #Iterações
while i <= qtdExperimentos:    
    info = input("Qtd de cobaias e animal: ")
    infos = info.split(" ")
    qtd = int(infos[0])
    tipo = infos[1].upper()[0]
    if tipo == 'C':
        qtdCoelho += qtd
    elif tipo == 'R':
        qtdRato += qtd
    elif tipo == 'S':
        qtdSapo += qtd
    i = i + 1

qtdCobaias = qtdCoelho + qtdRato + qtdSapo
percCoelho = (qtdCoelho / qtdCobaias) *100
percRato = (qtdRato * 100) / qtdCobaias
percSapo = (qtdSapo * 100) / qtdCobaias

print(f"Total: {qtdCobaias} cobaias")
print(f"Total de coelhos: {qtdCoelho}")
print(f"Total de ratos: {qtdRato}")
print(f"Total de sapos: {qtdSapo}")
print(f"Percentual de coelhos: {percCoelho:.2f} %")
print(f"Percentual de ratos: {percRato:.2f} %")
print(f"Percentual de sapos: {percSapo:.2f} %")