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

def acesso():
    while True:
        clear_screen()
        print("\nSistema de Login")
        print(divider)
        print("1. Para realizar login")
        print("2. Para se cadastrar")
        print(divider)
        choice = input("\nSelect an option: ")

        if choice == '1':
            login()
        elif choice == '2':
            cadastro()

def login():
    clear_screen()
    print("\nRealizar Login:")
    print(divider)
    email = input("Email: ")
    senha = input("Senha: ")
    for funcionario in funcionarios_cadastrados:
        if funcionario.email == email and funcionario.senha == senha:
            print(f"\nEmail: {funcionario.email}")
            print(f"\nSenha: {funcionario.senha}")
            input("\nPress Enter to go back.")

    else:
        print("\nFuncionário não encontrado!")
        input("\nPressione enter para voltar.")

def cadastro():
    clear_screen()
    print("\nRegistering:")
    print(divider)
    email = input("\nEmail: ")

    if email == "":
        print("Email inválido!")
        choice = input("\nTentar novamente? (Y/n)")
        if choice.lower() == "y":
            cadastro()
        else:
            acesso()

    senha = input("Senha (Mínimo 3 caracteres): ")
    if senha == "":
        print("\nSenha inválida!")
        choice = input("\nTentar novamente? (Y/n)")
        if choice.lower() == "y":
            cadastro()
        else:
            acesso()

    if len(senha) < 3:
        print("\nPassword is too short!")
        choice = input("\nTentar novamente? (Y/n)")
        if choice.lower() == "y":
            cadastro()
        else:
            acesso()

    if email and senha:
        funcionario = Funcionario(email=email, senha=senha)
        funcionarios_cadastrados.append(funcionario)
        acesso()

acesso()
