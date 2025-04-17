n = float(input("Digite um número para calcular a raiz: "))
b = 2.0
precisao = 0.0001
while True:
    p = (b + (n / b)) / 2
    quadrado_p = p * p
    if abs(n - quadrado_p) < precisao:
        break
    b = p 
print(f"A raiz quadrada aproximada de {n:.0f} é {p:.2f}")