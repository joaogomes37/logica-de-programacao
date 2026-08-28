# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: João Vítor Monzani Gomes
# Data: 28/08/2026
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
    "  pedro henrique alves;11988887777  ",
    "  juliana ferreira costa;21977776666  ",
    "  lucas gabriel martins;31966665555  ",
    "  beatriz oliveira santos;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

# Laço de repetição usando for e range()
for i in range(len(cadastros_brutos)):

    # 1. Remover espaços extras
    cadastro = cadastros_brutos[i].strip()

    # 2. Separar nome e telefone
    nome, telefone = cadastro.split(";")

    # 3. Converter o nome para MAIÚSCULAS
    nome = nome.upper()

    # 4. Extrair o DDD usando fatiamento
    ddd = telefone[0:2]

    # 5. Exibir resultado formatado
    print(f"Funcionário: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("            PROCESSAMENTO CONCLUÍDO               ")
print("==================================================")
