'''
Questão 5 – Sistema de notas 

Crie uma variável chamada `nota`. 

Utilize `if...elif...else` para classificar: 

Nota                 Resultado 
--------------------------------------
9 a 10          Excelente      >= 9
7 a 8.9         Aprovado       >= 7
5 a 6.9         Recuperação    >= 5
Menor que 5     Reprovado      < 5
'''

nota = 4.9

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")           