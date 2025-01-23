# Implemente uma função em Python chamada validador_senha() que verifica
#se uma senha fornecida atende todos os seguintes critérios:
#•Pelo menos 8 caracteres de comprimento.
#•Contém pelo menos uma letra maiúscula e uma letra minúscula.
#•Contém pelo menos um número.
#•Contém pelo menos um caractere especial (por exemplo, @, #, $).

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        return False
    # Verifica se a senha contém pelo menos uma letra minúscula
    if not any(char.islower() for char in senha):
        return False
    # Verifica se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    # Verifica se a senha contém pelo menos um caractere especial
    if not any(char in "!@#$%^&*()_+-=[]{}|;':,./<>?" for char in senha):
        return False
    # Se todas as verificações passarem, a senha é válida
    return True

# Solicita ao usuário uma senha
senha = input("Digite uma senha: ")

# Chama a função validador_senha() para verificar a senha
if validador_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida.")

# Programa Encerrado