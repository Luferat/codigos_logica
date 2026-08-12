############################################
# 2026.08.10.Funcoes\agenda_furreca.py     #
# AGENDA FURRECA.PY                        #
# Versão 2026.08.10                        #
# By Luferat - https://github.xonm/Luferat #
############################################

# Importa "subprocess" que permite executar comandos do sistema
import subprocess
import random
import os

# Banco de dados em memória (dict)
database = {
    "1": { "name": "Joca da Silva", "contact": "(21) 998877665"},
    "120": { "name": "Mariana Sirilampo", "contact": "mariana@sirilampo.com.br"}
}

# Limpa a tela
def cls():
    if os.name == "nt":
        # Se o sistema é Windows
        subprocess.run("cls", shell=True)
    else:
        # Outros sistemas como Linux e MacOS
        subprocess.run("clear", shell=True)

# Cadastra novo contato
def new_contact():
    # Limpa a tela
    cls()

    # Cabeçalho
    print("[ AGENDA FURRECA - NOVO CONTATO ]")
    print("\nDigite os dados do contato:\n")

    # Recebe os dados do usuário
    name = input(" • Nome: ")
    contact = input(" • Contato: ")

    # Gera o ID aleatório
    key = str(random.randint(1, 1000))

    # Salva o novo cadastro no formato "dict"
    database[key] = dict(name = name, contact = contact)

    # Confirmação
    print(f"\nUsuário com ID {key} adicionado!")
    input("Tecle [Enter] para continuar")

    # Chama o menu principal
    main()

# Lista todos os registros
def list_contacts():
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
        print("\t• Nome:", value['name'])
        print("\t• Contato:", value['contact'])
        print()

    # Confirma e chama o menu principal
    input("Tecle [Enter] para continuar")
    main()

def edit_contact():
    cls()
    print("[ AGENDA FURRECA - EDITA CONTATO ]")

    # ...
    
    input("Tecle [Enter] para continuar")
    main()

def delete_contact():
    cls()
    print("[ AGENDA FURRECA - APAGA CONTATO ]")

    # ...
    
    input("Tecle [Enter] para continuar")
    main()

# Programa principal
def main(erro = str()):
    # Main loop
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

        # Exibe mensagem de erro se existir
        if erro:
            print("-----", erro, "-----")
            
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
                erro = "Digite uma opção válida!"
                main(erro)

# "Roda" o programa
main()     