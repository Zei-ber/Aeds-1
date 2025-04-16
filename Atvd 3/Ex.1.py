valor = 0.0
parada = 1
while(parada != 0):
    lista = [1, 2, 3, 4, 5]
    list = [0.5, 1, 4, 7, 8]
    code = int(input('Digite o código do produto comprado:'))
    if code == 0:
        print(valor)
        parada = 0
    elif code not in lista:
        print('Código inválido.')
        parada = 0
    else:
        quant = int(input('Digite a quantidade do produto:'))
        for i in range (5):
            if code == lista[i]:
                valor += list[i] * quant
        
    
