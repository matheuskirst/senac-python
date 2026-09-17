soma = 6 + 5
multiplicacao = 2 * 5

# E
if soma > 10 and multiplicacao > 10:
    print("a soma e a multiplicação são maiores que 10")
else:
    print("a soma ou a multiplicação não são maiores que 10")

# Ou
if soma > 11 or multiplicacao > 11:
    print("a soma ou a multiplicação são maiores que 11")
else:
    print("nem a soma nem a multiplicação são maiores que 11")

# Negação
if not soma > 10:
    print("A soma não é maior que 10")
