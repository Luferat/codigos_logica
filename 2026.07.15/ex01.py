'''
Questão 1 – Cadastro simples 

Crie um programa que: 

 - Armazene o nome de uma pessoa em uma variável `name`. 
 - Armazene a idade em outra variável `age`.
 - Exiba a seguinte mensagem, em que os valores devem vir das variáveis:  

Olá João, você tem 20 anos. 
 
'''

name = "Joca da Silva"
age = 35

# Interpolando usando "f" (string formatada) Recomendado
print(f"Olá {name}, você tem {age} anos.")

# Contatenando usando "+"
print("Olá " + name + ", você tem " + str(age) + " anos.")

# Argumentos da função "print()"
print("Olá", name, ", você tem", age, "anos.")

# Em produção, armazene em uma variável
saida = f"Olá {name}, você tem {age} anos."
print(saida)
