#Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido".
#Dica: use o módulo string para trabalhar com as strings.

# Solicita o CPF ao usuário
def validar_cpf(cpf):
    import string
    
    # Remove os caracteres não numéricos
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verifica se o CPF tem 11 dígitos numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido: formato incorreto."
    
    # Separa os primeiros 9 dígitos
    primeiros_nove_digitos = cpf[:9]
    
    # Calcula o primeiro dígito verificador
    multiplicador = 10
    soma = 0
    for digito in primeiros_nove_digitos:
        soma += int(digito) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    primeiro_digito_verificador = 0 if resto < 2 else 11 - resto
    
    # Calcula o segundo dígito verificador
    segundo_nove_digitos = primeiros_nove_digitos + str(primeiro_digito_verificador)
    multiplicador = 11
    soma = 0
    for digito in segundo_nove_digitos:
        soma += int(digito) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    segundo_digito_verificador = 0 if resto < 2 else 11 - resto
    
    # Compara os dígitos verificadores calculados com os fornecidos
    if cpf[-2:] == f"{primeiro_digito_verificador}{segundo_digito_verificador}":
        return "CPF válido."
    else:
        return "CPF inválido."

# Solicita o CPF ao usuário
cpf_usuario = input("Digite um CPF no formato XXX.XXX.XXX-XX: ")

# Valida o CPF e imprime o resultado
resultado = validar_cpf(cpf_usuario)
print(resultado)
