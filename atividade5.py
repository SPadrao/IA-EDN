from datetime import datetime
import unicodedata
import re

def calculadora_gorjeta():
    print("\n--- Calculadora de Gorjeta ---")
    try:
        conta = float(input("Digite o valor da conta: R$ "))
        porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))
        gorjeta = conta * (porcentagem / 100)
        print(f"Gorjeta: R$ {gorjeta:.2f}\n")
    except ValueError:
        print("Entrada inválida. Use números válidos.\n")

def verificador_palindromo():
    print("\n--- Verificador de Palíndromos ---")
    texto = input("Digite uma palavra ou frase: ")
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn' and c.isalnum()
    )
    if texto == texto[::-1]:
        print("Sim\n")
    else:
        print("Não\n")

def calculadora_desconto():
    print("\n--- Calculadora de Desconto ---")
    try:
        preco = float(input("Digite o preço original do produto: R$ "))
        desconto = float(input("Digite o percentual de desconto: "))
        preco_final = preco * (1 - desconto / 100)
        print(f"Preço com desconto: R$ {preco_final:.2f}\n")
    except ValueError:
        print("Entrada inválida. Use números válidos.\n")

def idade_em_dias():
    print("\n--- Calculadora de Idade em Dias ---")
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = datetime.now().year
        idade_anos = ano_atual - ano_nascimento
        idade_dias = idade_anos * 365
        print(f"Idade aproximada em dias: {idade_dias} dias\n")
    except ValueError:
        print("Ano inválido. Digite um valor numérico.\n")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Calculadora de Gorjeta")
        print("2 - Verificador de Palíndromos")
        print("3 - Calculadora de Desconto em Produto")
        print("4 - Calculadora de Idade em Dias")
        print("0 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            calculadora_gorjeta()
        elif escolha == "2":
            verificador_palindromo()
        elif escolha == "3":
            calculadora_desconto()
        elif escolha == "4":
            idade_em_dias()
        elif escolha == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()

