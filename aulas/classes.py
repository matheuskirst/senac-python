class Usuario():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"O nome do objeto usuário é {self.nome}"
    
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}")

usuario = Usuario()

print(usuario.idade)

usuario.idade = 21

print(f"nova idade {usuario.idade}")

usuario.apresentar()
