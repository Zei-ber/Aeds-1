cig = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Há quantos anos você fuma?'))
cig1 = anos * 365
cig11 = cig * cig1
cig2 = cig11 * 10
cig3 = cig2 / 1440
print(f'Você já diminuiu sua expectativa de vida em {cig3:.0f}', 'dias')