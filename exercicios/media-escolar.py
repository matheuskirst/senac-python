import os
import subprocess

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

divider = "--------------------"

while True:
    resultado = 0
    situacao = ""

    clear_screen()
    print("\n--- Calcular Média de Aluno ---")

    try:
        nome = input("\nNome do aluno: ")

        nota_1 = float(input("\nNota 1: "))
        nota_2 = float(input("Nota 2: "))
        nota_3 = float(input("Nota 3: "))

        resultado = (nota_1 + nota_2 + nota_3)/3

        if resultado >= 7:
            situacao = "Aprovado"
        elif resultado >= 5 and resultado < 7:
            situacao = "Recuperação"
        elif resultado < 5:
            situacao = "Reprovado"
        
        print()
        print("Resultado:")
        print(divider)
        print(f"\nNome do aluno: {nome}")
        print(f"Nota 1: {nota_1}")
        print(f"Nota 2: {nota_2}")
        print(f"Nota 3: {nota_3}")
        print(f"\nNota final: {round(resultado, 2)}")
        print(f"Situação: {situacao}")
        input("\nPressione para continuar... ")

    except:
        print("\nValor inválido!")
        input("\nPressione para continuar... ")
