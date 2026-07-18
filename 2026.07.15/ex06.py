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

if quantidade_solicitada <= estoque:
    print("Pedido aprovado")
else:
    print("Pedido excede estoque")

print()

quantidade_solicitada = int(input("Digite a quantidade solicitada: "))

if quantidade_solicitada <= estoque:
    print("Pedido aprovado")
else:
    print("Estoque insuficiente")
    