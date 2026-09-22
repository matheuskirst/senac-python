contador = 1

# while contador <= 5:
#     print(contador)
#     contador += 1

# while contador <= 10:
#     if contador == 3:
#         contador += 1
#         continue

#     if contador == 7:
#         break

#     print(contador)
#     contador += 1


# Usando somente número final
print("Usando somente número final")
for numero in range(5):
    print(f"Número: {numero}")

# Usando número inicial e número final
print("Usando número inicial e número final")
for numero in range(1, 6):
    print(f"Número: {numero}")

# Usando número inicial, número final e incremento
print("Usando número inicial, número final e incremento")
sequencia = range(0, 11, 2)
for numero in sequencia:
    print(f"Número: {numero}")

# Contador negativo usando número inicial, número final e incremento
print("Contador negativo usando número inicial, número final e incremento")
sequencia = range(10, -1, -1)
for numero in sequencia:
    print(f"Número: {numero}")

for letra in "Matheus":
    print(f"Letra: {letra}")


frutas = ["Maça", "Banana", "Mamão"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

for indice, fruta in enumerate(frutas):
    print(f"Indíce {indice}: {fruta}")
