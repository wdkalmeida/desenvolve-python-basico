#4) Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. 
#O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. 
#Reescreva esse código usando apenas duas variáveis. 

#juros = 1.01
#saldo = 500
#rendimento1 = saldo * juros
#rendimento2 = rendimento1 * juros
#rendimento3 = rendimento2 * juros
#print ("Após 3 meses meu novo saldo é")
#print (rendimento3)

juros = 1.01
saldo = 500.0
print (saldo)
saldo = saldo * juros #505 rendimento 1
print (saldo)
saldo = saldo * juros #510 rendimento 2
print (saldo)
saldo = saldo * juros #515 rendimento 3
print (saldo)

print (type(saldo))
