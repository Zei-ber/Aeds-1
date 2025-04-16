try:
    a = int(input('Digite um número:'))
    b = int(input('Digite outro número:'))
    c = a + b
    print('A soma desses números é', c)
except (ValueError):
    print('Você não digitou um número')