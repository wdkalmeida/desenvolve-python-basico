#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta
#entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para 
#arredondar o resultado para duas casas decimais.
#Exemplo de interação:
#Digite o primeiro número: 3.1415
#Digite o segundo número: 1.4142
#A diferença absoluta entre os números é: 1.73

#Solicitar ao usuário que insira dois números decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))    

#Calcular a diferença absoluta entre os números
diferenca = abs(num1 - num2)

#Arredondar o resultado para duas casas decimais
diferenca = round(diferenca, 2)

#Exibir o resultado
print("A diferença absoluta entre os números é:", diferenca)    
