import random
import string
import requests
from datetime import datetime

def gerador_senha():
    print("\n--- Gerador de Senhas Seguras ---")
    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        if tamanho < 4:
            print("A senha deve ter pelo menos 4 caracteres.\n")
            return
        caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        senha = ''.join(random.choices(caracteres, k=tamanho))
        print(f"Senha gerada: {senha}\n")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")

def gerador_usuario():
    print("\n--- Gerador de Usuário Aleatório ---")
    try:
        resposta = requests.get("https://randomuser.me/api/")
        if resposta.status_code != 200:
            print("Erro ao acessar a API.\n")
            return
        dados = resposta.json()["results"][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados["email"]
        pais = dados["location"]["country"]
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}\n")
    except Exception:
        print("Erro ao obter dados da API.\n")

def consulta_cep():
    print("\n--- Consulta de CEP ---")
    cep = input("Digite o CEP (apenas números): ").strip()
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Deve conter 8 dígitos numéricos.\n")
        return
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if resposta.status_code != 200:
            print("Erro ao acessar a API.\n")
            return
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.\n")
            return
        print(f"CEP: {dados.get('cep', 'N/A')}")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}\n")
    except Exception:
        print("Erro ao consultar o CEP.\n")

def conversor_moedas():
    print("\n--- Conversor de Moedas para BRL ---")
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR): ").upper().strip()
    try:
        resposta = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda}-BRL")
        if resposta.status_code != 200:
            print("Erro ao acessar a API.\n")
            return
        dados = resposta.json()
        chave = moeda + "BRL"
        if chave not in dados:
            print("Código de moeda inválido.\n")
            return
        cotacao = dados[chave]
        valor = cotacao["bid"]
        maximo = cotacao["high"]
        minimo = cotacao["low"]
        atualizacao = datetime.fromtimestamp(int(cotacao["timestamp"])).strftime("%d/%m/%Y %H:%M:%S")
        print(f"Moeda: {moeda}")
        print(f"Cotação atual: R$ {valor}")
        print(f"Valor máximo: R$ {maximo}")
        print(f"Valor mínimo: R$ {minimo}")
        print(f"Última atualização: {atualizacao}\n")
    except Exception:
        print("Erro ao consultar cotação.\n")

def menu():
    while True:
        print("Escolha uma opção:")
        print("1 - Gerador de Senhas Seguras")
        print("2 - Gerador de Usuário Aleatório")
        print("3 - Consulta de CEP")
        print("4 - Conversor de Moedas para BRL")
        print("0 - Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            gerador_senha()
        elif escolha == "2":
            gerador_usuario()
        elif escolha == "3":
            consulta_cep()
        elif escolha == "4":
            conversor_moedas()
        elif escolha == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()

