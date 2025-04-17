n = float(input("Digite um número para calcular a raiz: "))
b = 2.0
precisao = 0.0001
while True:
    p = (b + (n / b)) / 2
    quadrado_p = p * p
    #abs = a um módulo
    if abs(n - quadrado_p) < precisao:
        break
    b = p  # Atualiza b 
print(f"A raiz quadrada aproximada de {n:.0f} é {p:.2f}")