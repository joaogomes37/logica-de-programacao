# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: João Vítor Monzani Gomes
# Data:
# Link do Repositório:
# ==============================================================================

# Lista inicial de dados brutos
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]

# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    Remove espaços e converte para MAIÚSCULAS.
    """
    return texto.strip().upper()


def extrair_codigo_ou_ddd(dado):
    """
    Extrai os 2 primeiros dígitos do telefone (DDD).
    """
    dado = dado.strip()
    return dado[0:2]


def processar_e_exibir_cadastros(lista_dados):
    """
    Processa os registros utilizando FOR e exibe os dados formatados.
    """
    total = 0

    for cadastro in lista_dados:
        partes = cadastro.strip().split(";")

        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])
        ddd = extrair_codigo_ou_ddd(partes[2])

        print(f"Nome : {nome}")
        print(f"Cargo: {cargo}")
        print(f"DDD  : ({ddd})")
        print("-" * 40)

        total += 1

    return total


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("      SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("           PROCESSAMENTO CONCLUÍDO")
    print("==================================================")


# Execução do programa
if __name__ == "__main__":
    main()
