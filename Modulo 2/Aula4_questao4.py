#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 

#Ler o valor inteiro em Reais
valor = int(input("Digite um valor em reais: "))

# Iniciar as variáveis para cada nota
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = notas1 = 0

# Calcular a quantidade de cada nota ##começar da maior nota quantas notas
notas100 = valor // 100  #576 // 100 = 5
##atualizar quanto falta depois da maior nota
valor = valor % 100 #576 - 5*100 = 76

notas50 = valor // 50  #76 // 50= 1
valor = valor % 50 #valor -50*notas50 #26

notas20 = valor // 20  #26 // 20= 1
valor = valor % 20 ## falta 6

notas10 = valor // 10  #6 // 10= 0
valor = valor % 10 ## falta 6

notas5 = valor // 5  #6 // 5= 1
valor = valor % 5 #valor -5*notas5 #1

notas2 = valor // 2 #1 // 2= 0
valor = valor % 2 ## falta 1

notas1 = valor // 1 #1 // 2= 1
valor = valor % 1 #valor -2*notas50 #0

# Imprimir a quantidade de cada nota
print(f"Notas de 100: {notas100}")
print(f"Notas de 50: {notas50}")
print(f"Notas de 20: {notas20}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 5: {notas5}")
print(f"Notas de 2: {notas2}")
print(f"Notas de 1: {notas1}")