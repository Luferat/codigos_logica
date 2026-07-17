'''
Questão 4 – Verificação de maioridade 

Crie uma variável chamada `age`.

Utilize uma estrutura `if...else` para verificar a idade. 

Se for maior ou igual a 18, exiba: 

	Maior de idade 

Caso contrário: 

	Menor de idade 
'''

age = input("Digite a idade: ")

age = int(age)

# age = 18

if age >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    