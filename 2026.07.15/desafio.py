'''
Questão Desafio 

Crie uma lista contendo nomes de alunos: 

["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"] 

Verifique se um determinado nome está na lista. 

Se estiver: 

Aluno matriculado. 

 

Caso contrário: 

Aluno não encontrado. 

 

> Objetivo: utilizar lista, variável, operador in e estrutura if...else em uma única solução.  
'''

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "André"]

nome = input("Digite o nome do aluno (case-sensitive): ")

if nome in nomes:
    print("Aluno matriculado.")
else:
    print("Aluno não encontrado.")

print('\n--------------------------------\n')

if nome.lower() in (n.lower() for n in nomes):
    print("Aluno matriculado.")
else:
    print("Aluno não encontrado.")    


print('\n--------------------------------\n')

for n in nomes:
    print(n.lower())


print('\n--------------------------------\n')   

lista_nomes_minusculas = []
for n in nomes:
    lista_nomes_minusculas.append(n.lower())

print(nomes)
print(lista_nomes_minusculas)

print()
if nome.lower() in lista_nomes_minusculas:
    print("Aluno matriculado.")
else:
    print("Aluno não encontrado.")           