T = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = T[0]
maior = T[0]
soma = 0
for temp in T:
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma += temp
media = soma / len(T)
print(f"Menor temperatura: {menor}")
print(f"Maior temperatura: {maior}")
print(f"Temperatura média: {media}")