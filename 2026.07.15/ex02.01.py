'''
Questão 2 – Identificando tipos de dados 

Crie variáveis contendo:  

 - Um texto
 - Um número inteiro
 - Um número decimal
 - Um valor booleano 

Depois, utilize a função type() para exibir o tipo de cada variável. 

Exemplo de saída: 

<class 'str'> 
<class 'int'>
<class 'float'> 
<class 'bool'> 
'''

texto = 'Coisa'
inteiro = 1
decimal = 1.0
booleano = True

print(type(texto))
print(type(inteiro))
print(type(decimal))
print(type(booleano))

entrada = int(input("digite um número: "))

if type(entrada) == int:
    print("O tipo não é 'string'")
