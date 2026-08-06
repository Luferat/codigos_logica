aluno = {
    "matricula": "101214bc",
    "nome": "Joca da Silva",
    "serie": 4,
    "nacimento": "10/04/1999",
    "nome": "Maria da Silva"
}
print()
print("--->", aluno)
print("Quantos itens?", len(aluno))
print(aluno["serie"])

aluno["serie"] = 5
print(aluno["serie"])

aluno["nome"] = "Joca Silva"
print(aluno)

aluno["nota"] = 8.5
print(aluno)

print(aluno["nome"])
print(aluno)

del aluno["nome"]
print(aluno)

aluno["nacimento"] = ''
print(aluno)

# print(aluno[0]) ERRRRROOOOO!

# Exemplificando com conjuntos (set)
conjunto = {"casa", "carro", "peteca"}
print(conjunto)