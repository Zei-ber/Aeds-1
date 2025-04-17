numero = int(input("Digite um número: "))
original = numero
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10
if original == invertido:
    print(f"{original} é um palíndromo.")
else:
    print(f"{original} não é um palíndromo.")