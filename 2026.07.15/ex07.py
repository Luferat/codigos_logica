'''
Questão 7 – Acesso ao sistema (operador AND) 

Crie as variáveis: 

 - usuario = "admin" 
 - senha = "1234" 

Utilize o operador `and` para verificar se: 

 - usuário é "admin"
 - senha é "1234" 

Se ambas as condições forem verdadeiras: 

	Acesso permitido. 

Caso contrário: 

	Acesso negado. 
'''

usuario = "admin"
senha = "1234"

if usuario == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")    


''' Experimental

if usuario != "admin": # False
    print("Usuário errado")
elif senha != "1234": # False
    print("Senha errada")
else:
    print("Acesso permitido")    
'''

