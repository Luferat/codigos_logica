############################################
# 2026.08.10.Funcoes\agenda_furreca.py     #
# AGENDA FURRECA.PY                        #
# Versão 2026.08.10                        #
# By Luferat - https://github.xonm/Luferat #
############################################

import subprocess
import random

# Baco de dados
database = {
    "1": { "name": "Joca da Silva", "contact": "(21) 998877665"},
    "120": { "name": "Mariana Sirilampo", "contact": "mariana@sirilampo.com.br"}
}

def cls():
    subprocess.run("cls", shell=True)

def new_contact():
    cls()
    print("[ AGENDA FURRECA - NOVO CONTATO ]")
    
    print("\nDigite os dados do contato:\n")

    name = input(" • Nome: ")
    contact = input(" • Contato: ")
    key = str(random.randint(1, 1000))

    database[key] = dict(name = name, contact = contact)

    print(f"\nUsuário com ID {key} adicionado!")
    input("Tecle [Enter] para continuar")
    main()

def list_contacts():
    cls()
    print("[ AGENDA FURRECA - LISTA CONTATOS ]")
    print()
    print(len(database), "usuários encontrados!")
    print()

    for key, value in database.items():
        print("ID:", key)
        print("\t• Nome:", value['name'])
        print("\t• Contato:", value['contact'])
        print()
    
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
        cls() 
        print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
        if erro:
            print(erro)
        erro = str()
        print('''
Opções:

1 - Novo contato
2 - Listar contatos
3 - Editar contato
4 - Apagar contato
0 - Sair do programa
    ''')
        
        opcao = input("Escolha uma opção: ")

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
                cls()
                print("\nAcabou!")
                exit()
            case _:
                erro = "Digite uma opção válida!"
                main(erro)

# "Roda" o programa
main()     