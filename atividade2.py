def conversor_moeda():
    valor_reais = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    valor_em_dolar = valor_reais / taxa_dolar
    valor_em_euro = valor_reais / taxa_euro

    print("\n--- Conversor de Moeda ---")
    print(f"Valor em reais: R$ {valor_reais:.2f}")
    print(f"Convertido em dólares: US$ {valor_em_dolar:.2f}")
    print(f"Convertido em euros: € {valor_em_euro:.2f}")


def calculadora_desconto():
    nome_produto = "Camiseta"
    preco_original = 50.00
    desconto_percentual = 20

    valor_desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - valor_desconto

    print("\n--- Calculadora de Desconto ---")
    print(f"Produto: {nome_produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {desconto_percentual}% (R$ {valor_desconto:.2f})")
    print(f"Preço final: R$ {preco_final:.2f}")


def calculadora_media():
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5

    media = (nota1 + nota2 + nota3) / 3

    print("\n--- Calculadora de Média Escolar ---")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média final: {media:.2f}")


def consumo_combustivel():
    distancia = 300
    combustivel = 25
    consumo_medio = distancia / combustivel

    print("\n--- Calculadora de Consumo de Combustível ---")
    print(f"Distância percorrida: {distancia} km")
    print(f"Combustível gasto: {combustivel} litros")
    print(f"Consumo médio: {consumo_medio:.2f} km/l")


while True:
    print("\nEscolha uma opção:")
    print("1 - Conversor de Moeda")
    print("2 - Calculadora de Desconto")
    print("3 - Calculadora de Média Escolar")
    print("4 - Calculadora de Consumo de Combustível")
    print("0 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        conversor_moeda()
    elif opcao == "2":
        calculadora_desconto()
    elif opcao == "3":
        calculadora_media()
    elif opcao == "4":
        consumo_combustivel()
    elif opcao == "0":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

