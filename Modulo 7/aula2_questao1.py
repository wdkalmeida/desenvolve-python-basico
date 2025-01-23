#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
#Dica: usando listas você não precisa fazer um "if" para cada mês.
#Ex:Digite uma data de nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

# Solicita a data de nascimento ao usuário
data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

# Divide a data em dia, mês e ano
dia, mes, ano = data_nascimento.split("/")

# Define uma lista com os nomes dos mês
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Imprime a data com o nome do mês por extenso
print("Voce nasceu em", dia, "de", meses[int(mes) - 1], "de", ano)

