def calculadora_simples():
    print("\n--- Calculadora Simples ---")
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Escolha a operação (+, -, *, /): ").strip()
            if operacao == "+":
                print(f"Resultado: {num1 + num2}\n")
                break
            elif operacao == "-":
                print(f"Resultado: {num1 - num2}\n")
                break
            elif operacao == "*":
                print(f"Resultado: {num1 * num2}\n")
                break
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: divisão por zero.\n")
                else:
                    print(f"Resultado: {num1 / num2}\n")
                    break
            else:
                print("Operação inválida.\n")
        except ValueError:
            print("Entrada inválida. Digite números válidos.\n")

def registro_notas():
    print("\n--- Registro de Notas e Cálculo da Média ---")
    notas = []
    while True:
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip()
        if entrada.lower() == "fim":
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota fora do intervalo (0-10).\n")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.\n")
    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
        print(f"Total de notas válidas: {len(notas)}\n")
    else:
        print("Nenhuma nota válida foi registrada.\n")

def verificador_senhas():
    print("\n--- Verificador de Senhas Fortes ---")
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()
        if senha.lower() == "sair":
            print("Encerrando o verificador.\n")
            break
        if len(senha) < 8:
            print("Senha fraca: menos de 8 caracteres.\n")
            continue
        if not any(char.isdigit() for char in senha):
            print("Senha fraca: não contém número.\n")
            continue
        print("Senha forte!\n")
        break

def analisador_pares_impares():
    print("\n--- Analisador de Números Pares e Ímpares ---")
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip()
        if entrada.lower() == "fim":
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print("Número par.\n")
                pares += 1
            else:
                print("Número ímpar.\n")
                impares += 1
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'fim'.\n")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}\n")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Calculadora Simples")
        print("2 - Registro de Notas e Cálculo da Média")
        print("3 - Verificador de Senhas Fortes")
        print("4 - Analisador de Números Pares e Ímpares")
        print("0 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            calculadora_simples()
        elif escolha == "2":
            registro_notas()
        elif escolha == "3":
            verificador_senhas()
        elif escolha == "4":
            analisador_pares_impares()
        elif escolha == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()

