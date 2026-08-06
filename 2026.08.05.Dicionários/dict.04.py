usuario = {
    "id": 1,
    "nome": "Joca da Silva",
    "nacimento": "10/10/2000",
    "contatos": {
        "email": "joca@silva.com",
        "telefone": "(21) 998877665",
        "instagram": "@fumacinha"
    }
}

print()
print(usuario["contatos"]["instagram"])
print(type(usuario["contatos"]))


vazio = dict()
print(type(vazio))

print(usuario.get("email", "email@generico.com")) # Não gera erro se a chave não existe e mostra o "placeholder"
print(usuario["email"]) # Gera erro se a chave não existe