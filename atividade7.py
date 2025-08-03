import pandas as pd
import csv
import json
import os

def processamento_logs_treinamento():
    arquivo = input("Digite o nome do arquivo CSV (ex: logs_treinamento.csv): ")
    try:
        df = pd.read_csv(arquivo)
        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

def escrita_arquivo_csv():
    dados = [
        ["Maria", 25, "São Paulo"],
        ["João", 30, "Rio de Janeiro"],
        ["Ana", 28, "Curitiba"]
    ]
    arquivo = input("Digite o nome do arquivo CSV para salvar os dados: ")
    try:
        with open(arquivo, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["Nome", "Idade", "Cidade"])
            escritor.writerows(dados)
        print(f"Dados salvos no arquivo {arquivo}")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def leitura_arquivo_csv():
    arquivo = input("Digite o nome do arquivo CSV a ser lido: ")
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.reader(f)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro na leitura do arquivo: {e}")

def leitura_escrita_json():
    pessoa = {
        "nome": "Carlos",
        "idade": 40,
        "cidade": "Belo Horizonte"
    }
    arquivo = input("Digite o nome do arquivo JSON: ")
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(pessoa, f, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso.")
        
        with open(arquivo, "r", encoding="utf-8") as f:
            dados_carregados = json.load(f)
        print("Dados carregados do arquivo:")
        print(dados_carregados)
    except Exception as e:
        print(f"Erro ao manipular o arquivo JSON: {e}")

def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Processamento de Logs de Treinamento")
        print("2 - Escrita de Arquivo CSV")
        print("3 - Leitura de Arquivo CSV")
        print("4 - Leitura e Escrita de Arquivo JSON")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            processamento_logs_treinamento()
        elif opcao == "2":
            escrita_arquivo_csv()
        elif opcao == "3":
            leitura_arquivo_csv()
        elif opcao == "4":
            leitura_escrita_json()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

