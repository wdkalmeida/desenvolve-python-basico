# Solicitar os dados para o produto 1
nome_produto1 = input("Digite o nome do primeiro produto: ")
preco_unitario1 = float(input("Digite o preço unitário do primeiro produto: "))
quantidade1 = int(input("Digite a quantidade do primeiro produto: "))

# Solicitar os dados para o produto 2
nome_produto2 = input("Digite o nome do segundo produto: ")
preco_unitario2 = float(input("Digite o preço unitário do segundo produto: "))
quantidade2 = int(input("Digite a quantidade do segundo produto: "))

# Solicitar os dados para o produto 3
nome_produto3 = input("Digite o nome do terceiro produto: ")
preco_unitario3 = float(input("Digite o preço unitário do terceiro produto: "))
quantidade3 = int(input("Digite a quantidade do terceiro produto: "))

# Calcular o preço total de cada produto
total_produto1 = preco_unitario1 * quantidade1
total_produto2 = preco_unitario2 * quantidade2
total_produto3 = preco_unitario3 * quantidade3

# Calcular o preço total da compra
total_compra = total_produto1 + total_produto2 + total_produto3

# Imprimir o preço total da compra formatado
print(f"Total: R${total_compra:,.2f}")