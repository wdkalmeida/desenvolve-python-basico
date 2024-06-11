#leitura das dimensões do terreno em metros (inteiros)
comprimento = int(input("Digite o comprimento do terreno (em metros): "))
largura = int(input("Digite a largura do terreno (em metros): "))

#leitura do preço do metro quadrado da região (ponto flutuante)
preco_m2 = float(input("Digite o preço do metro quadrado (em reais): "))

#cálculo da área do terreno em metros quadrados
area_m2 = comprimento * largura

#cálculo do preço total do tereno
preco_total = preco_m2 * area_m2

#impressão do resultado formatado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
