a = float(input('Digite o seu salário:'))
b = float(input('Digite o valor do aumento usando um valor entre 0 e 1:'))
c = a+a*b
d = b * 100
print(f'Seu novo salário é {c:,.2f}', 'e o valor do aumento é de', d, '%')