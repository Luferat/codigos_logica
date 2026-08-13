############################################
# 2026.08.10.Funcoes\agenda_furreca.py     #
# AGENDA FURRECA.PY                        #
# Versão 2026.08.11                        #
# By Luferat - https://github.xonm/Luferat #
############################################

# Importa "subprocess" e "os" que permitem executar comandos do sistema
import subprocess
import os

# Importa "random" para gerar números aleatórios
import random

# Banco de dados em memória (dict) (Moch)
database = {}


def cls():
    # Limpa a tela
    if os.name == "nt":
        # Se o sistema é Windows
        subprocess.run("cls", shell=True)
    else:
        # Outros sistemas como Linux e MacOS
        subprocess.run("clear", shell=True)


def new_contact():
    # Cadastra novo contato
    # Limpa a tela
    cls()

    # Cabeçalho
    print("[ AGENDA FURRECA - NOVO CONTATO ]")
    print("\nDigite os dados do contato:\n")

    # Recebe os dados do usuário

    # Recebe e valida o "name"
    while True:
        name = input(" • Nome: ")
        if name.strip() != "":
            break
        print("-----", "Digite um nome válido!", "-----")

    # Recebe e valida o "contact"
    while True:
        contact = input(" • Contato: ")
        if contact.strip() != "":
            break
        print("-----", "Digite um contato válido!", "-----")

    # Gera o ID aleatório e não repetido
    while True:
        key = str(random.randint(1, 1000))
        if key not in database:
            break

    # Salva o novo cadastro no formato "dict"
    database[key] = dict(name=name, contact=contact)

    # Confirmação
    print(f"\nUsuário com ID {key} adicionado!")
    input("Tecle [Enter] para continuar")

    # Chama o menu principal
    main()


def list_contacts():
    # Lista todos os registros
    # Limpa a tela
    cls()

    # Cabeçalho
    print("[ AGENDA FURRECA - LISTA CONTATOS ]")
    print()
    print(len(database), "usuários encontrados!")
    print()

    # Loop para iterar os registros usando o método `dict.items()`
    for key, value in database.items():
        # Formata a saída
        print("ID:", key)
        print(" • Nome:", value['name'])
        print(" • Contato:", value['contact'])
        print()

    # Confirma e chama o menu principal
    input("Tecle [Enter] para continuar")
    main()


def edit_contact():
    cls()
    print("[ AGENDA FURRECA - EDITA CONTATO ]")

    print()
    while True:
        key = input("Digite o ID do usuário: ")
        if key in database:
            break
        print("-----", "ID não encontrado!", "-----")

    print()
    print("ID:", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print()

    print("Digite os novos dados:")

    # Recebe e valida o "name"
    while True:
        name = input(" • Nome: ")
        if name.strip() != "":
            break
        print("-----", "Digite um nome válido!", "-----")

    # Recebe e valida o "contact"
    while True:
        contact = input(" • Contato: ")
        if contact.strip() != "":
            break
        print("-----", "Digite um contato válido!", "-----")

    # Atualizar
    database[key] = dict(name=name, contact=contact)

    print()
    print("Contato atualizado!")
    input("Tecle [Enter] para continuar")
    main()


def delete_contact():
    cls()
    print("[ AGENDA FURRECA - APAGA CONTATO ]")

    print()
    while True:
        key = input("Digite o ID do usuário: ")
        if key in database:
            break
        print("-----", "ID não encontrado!", "-----")

    print()
    print("ID:", key)
    print(" • Nome:", database[key]['name'])
    print(" • Contato:", database[key]['contact'])
    print()

    option = input("Tem certeza que deseja apagar [S/N]? ")
    if option.upper() == "S":
        del database[key]
        print("Contato apagado!")
    else:
        print()
        print("Não aconteceu nada!")

    input("Tecle [Enter] para continuar")
    main()


def main(error=str()):
    # Programa principal e "main loop"
    while True:
        # Limpa a tela
        cls()

        # Cabeçalho
        print("[ AGENDA FURRECA - MENU PRINCIPAL ]")

        # Exibe menu principal
        print('''
Opções:

1 - Novo contato
2 - Listar contatos
3 - Editar contato
4 - Apagar contato
0 - Sair do programa
    ''')

        # Exibe mensagem de error se existir
        if error:
            print("-----", error, "-----")

        # Recebe opção do usuário
        opcao = input("Escolha uma opção: ")

        # Executa a opção selecionada
        match opcao:
            case "1":
                new_contact()
            case "2":
                list_contacts()
            case "3":
                edit_contact()
            case "4":
                delete_contact()
            case "0":
                # Limpa a tela, exibe confirmação e termina o programa
                cls()
                print("\nAcabou!")
                exit()
            case _:
                # Se escolheu uma opção inválida, chama o menu novamente, mas, com a mensagem de erro.
                error = "Digite uma opção válida!"
                main(error)


# "Roda" o programa
main()

'''
DESAFIOS:
 • BÁSICO: adicionar seus comentários no código
 • BÁSICO: alterar / melhorar a interface
 • INTERMEDIÁRIO: Salvar os dados de forma persistente em um arquivo JSON 
 • AVANÇADO: salvar os dados de forma persistente em um banco de dados SQL como o SQLite
 • AVANÇADO: marcar o registro como "apagado" em vez de apagar realmente
'''
