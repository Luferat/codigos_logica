'''
Questão 3 – Lista de frutas 

Crie uma lista contendo pelo menos 5 frutas. 

Depois: 

 - Exiba a lista completa.
 - Exiba apenas a primeira fruta.
 - Exiba apenas a última fruta.

Adicione algumas frutas e exiba a última, independentemente da quantidade. 
'''

frutas = ['banana', 'maçã', "carambola", 'abacate', 'tomate']

print()
print(frutas)

print(frutas[0])

print(frutas[4])
# ou, independente da quantida de itens na coleção
print(frutas[-1])

# Adicionando mais frutas com o método list.extend()
frutas.extend(['uva', 'pêra', 'abacaxi'])
print(frutas) # Debug

print(frutas[-1])