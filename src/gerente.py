from config_supabase import supabase

# Loop inicial dos gerentes (antes deles "logarem"):
def menu_inicial_g():
    print()
    print("Menu Inicial Gerente")
    while(True):
        print()
        print("Menu: ")
        print("1. Cadastrar")
        print("2. Logar")
        print("3. Excluir")
        print("4. Sair")
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            cadastrar_g()
        elif opcao == 2:
            print("Logar!")
        elif opcao == 3:
            print("Excluir!")
        elif opcao == 4:
            print("Tchau!")
            break
        else:
            print("Opção inválida!")

# Para gerenciar os gerentes (cadastrar e excluir) é preciso de uma chave de acesso fornecida pelo banco.
# Chave de acesso: 15072023
n_acesso = 15072023

# Verifica se o login que foi digitado bate com algum login na tabela gerente:
def consultar_login(login):
    resultado = supabase.table("gerente").select("login").eq("login", login).execute()
    if resultado.data:
        return True
    else:
        return False

# Cadastrar gerente:
def cadastrar_g():
    chave_acesso = int(input("Digite a chave de acesso do banco: "))
    if chave_acesso == n_acesso:
        nome = input("Insira o nome: ")
        login = input("Insira um login: ")
        consulta = consultar_login
        while consulta:
            login = input("Login já existente! digitar outro login: ")
            consulta = consultar_login
        senha = input("Insira uma senha: ")
        dados = {
            "nome": nome,
            "login": login,
            "senha": senha
        }
        # Insere os dados no banco de dados:
        resultado = supabase.table("gerente").insert(dados).execute()
        # Verifica se os dados foram inseridos com sucesso:
        if resultado.data:
            print("Gerente cadastrado com sucesso!")
        else:
            # Teoricamente era para mostrar qual foi o erro:
            print("Erro ao cadastrar gerente: ", resultado.error)
    else:
        print("Chave de acesso incorreta!")