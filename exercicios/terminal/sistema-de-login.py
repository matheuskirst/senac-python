import subprocess
import os
from dataclasses import dataclass

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

divider = "--------------------"

@dataclass
class Funcionario:
    email: str
    senha: str

funcionarios_cadastrados: list[Funcionario] = []

def access():
    while True:
        clear_screen()
        print("\nSistema de Login")
        print(divider)
        print("1. Para se cadastrar")
        print("2. Para realizar login")
        print(divider)
        choice = input("\nSelecione uma opção: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()

def register():
    clear_screen()
    print("\nCadastrar-se:")
    print(divider)
    email = input("\nEmail: ")

    if email == "":
        print("Email inválido!")
        choice = input("\nTentar novamente? (Y/n)")
        if choice.lower() == "y":
            register()
        else:
            access()

    senha = input("Senha (Mínimo 3 caracteres): ")
    if senha == "":
        print("\nSenha inválida!")
        choice = input("\nTentar novamente? (Y/n)")
        if choice.lower() == "y":
            register()
        else:
            access()

    if len(senha) < 3:
        print("\nA senha deve ter 3 ou mais caracteres!")
        choice = input("\nTentar novamente? (Y/n)")
        if choice.lower() == "y":
            register()
        else:
            access()

    if email and senha:
        funcionario = Funcionario(email=email, senha=senha)
        funcionarios_cadastrados.append(funcionario)

        print("\nCadastro realizado com sucesso!")
        print(f"Email: {funcionario.email}")
        print(f"Senha: {funcionario.senha}")
        
        input("\nPressione enter para voltar.")
        access()

def login():
    clear_screen()
    print("\nRealizar Login:")
    print(divider)
    email = input("Email: ")
    senha = input("Senha: ")

    for funcionario in funcionarios_cadastrados:
        if funcionario.email == email and funcionario.senha == senha:
            print("\nLogin realizado com sucesso!")
            print(f"Email: {funcionario.email}")
            print(f"Senha: {funcionario.senha}")
            input("\nPressione enter para voltar.")
            access()

    else:
        print("\nErro ao realizar o login.")
        print("Email ou senha incorretos!")
        input("\nPressione enter para voltar.")
        access()

access()
