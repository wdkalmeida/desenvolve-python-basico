#2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.

#Leitura da temperatura em Fahrenheit (inteiro)
Fahrenheit = int(input("Digite a temperatura em graus fahrenheit: "))

#Convertendo para graus Celsius 
Celsius = (Fahrenheit - 32) * (5/9)

#Convertendo Celsius para inteiro
celsius_inteiro = int(Celsius)

#imprimindo resultado formatado
print(f"{Fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius.")
