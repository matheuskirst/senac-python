frutas = ["Maça", "Banana", "Mamão"]

numeros = [1, 3, 5, 10]

booleanos = [True, False, True]

dados = ["Matheus", 20, True, "Programador"]

for dado in dados:
    print(f"Dado: {dado}")

alunos = []
alunos.append("Matheus")
alunos.append("Lucas")
alunos.append("Guilherme")

print(f"Aluno 0 {alunos[0]}")
print(f"Aluno 1 {alunos[1]}")
print(f"Aluno 2 {alunos[2]}")

alunos[1] = "João"
print(alunos)

alunos.insert(1, "Gabriel")

print(alunos)

alunos.remove("Guilherme")

print(alunos)

alunos.pop(1)

print(alunos)

tamanho_lista = len(alunos)

print(f"Tamanho da lista: {tamanho_lista} itens")
