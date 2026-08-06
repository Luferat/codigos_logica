

# uma lista
coisas = [
    "casa", 
    110, 
    99.9, 
    True, 
    ["a", 2, 3.3,], 
    (1, 2, 3,),
    {
        "nome": "João Silva",
        "id": 1,        
        "email": "joao@email.com",
        "senha": "..."
    },
    {
        "id": 2,
        "nome": "Maria Souza",
        "email": "maria@email.com",
        "senha": "..."
    }
]

print()
print(coisas[0])
print(coisas[4])
print(type(coisas[4]))
print(coisas[5])
print(type(coisas[5]))

# Acessar 3.3
print(coisas[4][2], [0])


print(coisas[6])
print(type(coisas[6]), len(coisas[6]))
print(coisas[6]["nome"])
print(coisas[7])

print(coisas[7]["email"])


