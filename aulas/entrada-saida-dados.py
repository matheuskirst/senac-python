print("Primeira entrada de dados no Python")

nome = input("Qual é o seu nome? ")

try:
    idade = int(input("Qual é a sua idade? "))
    print(f"Olá, {nome}. Você tem {idade} anos.")
    if idade <= 12:
        print("É criança")
    elif idade <= 18:
        print("É adolescente")
    else:
        print("É adulto")

except Exception:
    print("Valor de idade inválido!")

    print(f"Tipo do nome {type(nome)}")
    print(f"Tipo da idade {type(idade)}")
