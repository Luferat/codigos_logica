'''
Questão 1 – Cadastro simples 

Crie um programa que: 

 - Armazene o nome de uma pessoa em uma variável name. 
 - Armazene a idade em outra variável age.
 - Exiba a seguinte mensagem, em que os valores devem vir das variáveis:  

Olá João, você tem 20 anos. 
 
'''

name = "Joca da Silva"
age = 35

print(f"Olá {name}, você tem {age} anos.")
print("Olá " + name + ", você tem " + str(age) + " anos.")
print("Olá", name, ", você tem", age, "anos.")
