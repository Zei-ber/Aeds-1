a = float(input('Digite o preço do produto:'))
b = float(input('Digite o valor do desconto usando um valor entre 0 e 1:'))
c = a-a*b
d = b * 100
print(f'O valor a ser pago é {c:,.2f}', 'e o valor do desconto é de', d, '%')