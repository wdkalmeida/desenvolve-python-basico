def validar_cpf(cpf):
    # Remove os pontos e o hífen
    cpf = cpf.replace(".", "").replace("-", "")

    # Verifica se o CPF tem 11 dígitos numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # Função para calcular os dígitos verificadores
    def calcular_digito(cpf, peso_inicial):
        soma = sum(int(cpf[i]) * (peso_inicial - i) for i in range(len(cpf)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Calcula o primeiro e o segundo dígito
    primeiro_digito = calcular_digito(cpf[:9], 10)
    segundo_digito = calcular_digito(cpf[:9] + str(primeiro_digito), 11)

    # Verifica se os dígitos calculados são iguais aos informados
    if cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
        return "Válido"
    else:
        return "Inválido"

# Solicita o CPF ao usuário
cpf = input("Digite o CPF (no formato XXX.XXX.XXX-XX): ")

# Valida e imprime o resultado
resultado = validar_cpf(cpf)
print("CPF", resultado)