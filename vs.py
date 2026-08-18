# higienizacao_cadastros.py

# ==============================
# Exercício 1: Nome e E-mail
# ==============================

nome = " joão vitor monzani gomes "
email = " joao.gomes37@eaportal "

nome_higienizado = nome.strip().upper()
email_higienizado = email.strip().lower()

print("Exercício 1")
print("Nome higienizado:", nome_higienizado)
print("E-mail higienizado:", email_higienizado)


# ==============================
# Exercício 2: CPF e Telefone
# ==============================

cpf = " 123.456.789-00 "
telefone = "(11) 99999-8888"

cpf_limpo = (
    cpf.strip()
    .replace(".", "")
    .replace("-", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
)

telefone_limpo = (
    telefone.strip()
    .replace(".", "")
    .replace("-", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
)

print("\nExercício 2")
print("CPF limpo:", cpf_limpo)
print("Telefone limpo:", telefone_limpo)


# ==============================
# Exercício 3: SKU / Código
# ==============================

codigo = " prod-1024-br-sp "

codigo_formatado = codigo.strip().upper().replace("-", "_")

print("\nExercício 3")
print("Código formatado:", codigo_formatado)