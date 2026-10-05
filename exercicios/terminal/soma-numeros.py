# Exercicio While
# Crie um programa que peça 5 números ao usuário e no final exiba a soma dos 5 números

import subprocess
import os

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

divider = "--------------------"

def run():
    while True:
        clear_screen()
        print("\nSomar números")
        print(divider)

        try:
            contador = 1
            soma = 0
            quantidade_somas = int(input("Quantidade de números para somar (ex: 5): "))
            
            print("")
            while contador <= quantidade_somas:
                while True:
                    try:
                        numero = float(input(f"Número {contador}: "))
                        break
                    except:
                        print("Valor inválido! Tente novamente.")
                        input("")

                soma += numero
                contador += 1

            print("")
            print(f"Resultado: {soma}")
            input("")
        except: 
            print("Valor inválido!")
            input("")

run()
