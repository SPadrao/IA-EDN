def classificador_idade():
    print("\n--- Classificador de Idade ---")
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade inválida.")
        elif idade <= 12:
            print("Classificação: Criança\n")
        elif idade <= 17:
            print("Classificação: Adolescente\n")
        elif idade <= 59:
            print("Classificação: Adulto\n")
        else:
            print("Classificação: Idoso\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")

def calculadora_imc():
    print("\n--- Calculadora de IMC ---")
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser positivos.\n")
            return
        imc = peso / (altura ** 2)
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        print(f"IMC: {imc:.2f} - Classificação: {classificacao}\n")
    except ValueError:
        print("Entrada inválida. Use números válidos com ponto (.) no lugar da vírgula.\n")

def conversor_temperatura():
    print("\n--- Conversor de Temperatura ---")
    try:
        temp = float(input("Digite a temperatura: "))
        origem = input("Unidade de origem (C/F/K): ").strip().upper()
        destino = input("Unidade de destino (C/F/K): ").strip().upper()

        if origem == destino:
            print(f"A temperatura permanece {temp}°{destino}.\n")
            return

        if origem == "C":
            celsius = temp
        elif origem == "F":
            celsius = (temp - 32) * 5 / 9
        elif origem == "K":
            celsius = temp - 273.15
        else:
            print("Unidade de origem inválida.\n")
            return

        if destino == "C":
            resultado = celsius
        elif destino == "F":
            resultado = celsius * 9 / 5 + 32
        elif destino == "K":
            resultado = celsius + 273.15
        else:
            print("Unidade de destino inválida.\n")
            return

        print(f"Temperatura convertida: {resultado:.2f}°{destino}\n")
    except ValueError:
        print("Valor inválido.\n")

def verificador_ano_bissexto():
    print("\n--- Verificador de Ano Bissexto ---")
    try:
        ano = int(input("Digite o ano: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é um ano bissexto.\n")
        else:
            print(f"{ano} não é um ano bissexto.\n")
    except ValueError:
        print("Entrada inválida. Digite um ano numérico.\n")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Classificador de Idade")
        print("2 - Calculadora de IMC")
        print("3 - Conversor de Temperatura")
        print("4 - Verificador de Ano Bissexto")
        print("0 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            classificador_idade()
        elif escolha == "2":
            calculadora_imc()
        elif escolha == "3":
            conversor_temperatura()
        elif escolha == "4":
            verificador_ano_bissexto()
        elif escolha == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()

