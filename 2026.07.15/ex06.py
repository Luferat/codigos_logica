'''
Questão 6 – Produto em estoque 

Crie as variáveis: 

 - estoque = 15 
 - quantidade_solicitada = 10 

Utilize uma estrutura `if` para verificar se existe quantidade suficiente no estoque. 

Se houver, exiba:

	Pedido aprovado. 

Caso contrário: 

	Estoque insuficiente. 
'''

estoque = 15
quantidade_solicitada = 10

print()

print(f"Estoque: {estoque}")

if quantidade_solicitada <= estoque:
    print("Pedido aprovado")
    # Atualiza o estoque
    estoque = estoque - quantidade_solicitada
else:
    print("Pedido excede estoque")

print()

print(f"Estoque: {estoque}")
quantidade_solicitada = int(input("Digite a quantidade solicitada: "))

if quantidade_solicitada <= estoque:
    print("Pedido aprovado")
else:
    print("Estoque insuficiente")
    