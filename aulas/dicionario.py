usuario = {
    "nome": "João",
    "email": "joao@email.com",
    "idade": 20,
    "ativo": True,
    "pets": ["Cão", "Gato"]
}

print(usuario)

print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")

usuario["idade"] = 21

print(f"Idade: {usuario['idade']}")

usuario["cidade"] = "Santa Cruz do Sul"

print (f"Cidade: {usuario['cidade']}")

del usuario["idade"]
usuario.pop("pets")

print(usuario)

print(usuario.keys())

for chave in usuario.keys():
    print(chave)

for valor in usuario.values():
    print(valor)

for chave, valor in usuario.items():
    print(f"Chave: {chave}, Valor: {valor}")
