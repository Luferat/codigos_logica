produtos = [
    {
        "nome": "camiseta",
        "codigo": "5y6fjyj26dyjd6j6d",
        "preco": 99.9,
        "quantidade": 4,
        "categoria": "vestimentas"
    },
    {
        "nome": "Trakinas",
        "codigo": "yy874qt7d8qth",
        "preco": 6.90,
        "quantidade": 35,
        "categoria": "alimentos"
    },
    {
        "nome": "Fusca",
        "codigo": "9783yt4943hjwe",
        "preco": 5800.0,
        "quantidade": 2,
        "categoria": "carro"
    },
]

print()

# Todos os dados de "Trakinas"
print(produtos[1]["categoria"])

# Todos os produtos
print(produtos)

print('\n-----------\n')

# todos os produtos usando "for"
for produto in produtos:
    print(f"{produto["nome"]} - R${produto["preco"]}")