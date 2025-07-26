def programa_saudacao():
    print("\n--- Programa de Saudação ---")
    print("Olá, mundo!\n")

def calculadora_soma():
    print("\n--- Calculadora de Soma ---")
    numero1 = 12
    numero2 = 14
    soma = numero1 + numero2
    print(f"{numero1} + {numero2} = {soma}\n")

def calculadora_volume():
    print("\n--- Calculadora de Volume ---")
    comprimento = 12
    largura = 14
    altura = 20
    volume = comprimento * largura * altura
    print(f"Volume da caixa retangular: {volume} cm³\n")

def calculadora_preco_total():
    print("\n--- Calculadora de Preço Total ---")
    nome_produto = "Cadeira Infantil"
    preco_unitario = 12.40
    quantidade = 3
    preco_total = preco_unitario * quantidade
    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R$ {preco_total:.2f}\n")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Programa de Saudação")
        print("2 - Calculadora de Soma")
        print("3 - Calculadora de Volume")
        print("4 - Calculadora de Preço Total")
        print("0 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            programa_saudacao()
        elif escolha == "2":
            calculadora_soma()
        elif escolha == "3":
            calculadora_volume()
        elif escolha == "4":
            calculadora_preco_total()
        elif escolha == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()

