num1 = int(input("Digite o primero número: "))
divisor = int(input("Digite o divisor deste número: "))
sinal = 1
if num1 < 0:
    num1 = -num1
    sinal *= -1
if divisor < 0:
    divisor = -divisor   
resto = num1
while resto >= divisor:
    resto = resto - divisor
if sinal == -1:
    resto = -resto
print(f"O resto da divisão inteira é: {resto}")