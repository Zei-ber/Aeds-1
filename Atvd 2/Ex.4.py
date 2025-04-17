valor = 0.0
parada = 1
lista = [1, 2, 3, 5, 9]
precos = [0.5, 1, 4, 7, 8]
while parada != 0:
    code = int(input('Digite o código do produto comprado (0 para finalizar): '))    
    if code == 0:
        print(f"\nO valor total da compra é: R$ {valor:.2f}")
        pagamento = float(input("Digite o valor pago pelo cliente: R$ ")) 
        if pagamento < valor:
            print("Pagamento insuficiente.")
        else:
            troco = pagamento - valor
            print(f"Troco a ser devolvido: R$ {troco:.2f}")    
            troco_centavos = round(troco * 100)
            notas = [10000, 5000, 2000, 1000, 500, 200]
            moedas = [100, 50, 10, 5, 2, 1]
            print("\nNotas:")
            for nota in notas:
                qtd = troco_centavos // nota
                troco_centavos %= nota
                if qtd > 0:
                    print(f"R$ {nota / 100:.2f}: {int(qtd)}")
            print("\nMoedas:")
            for moeda in moedas:
                qtd = troco_centavos // moeda
                troco_centavos %= moeda
                if qtd > 0:
                    print(f"R$ {moeda / 100:.2f}: {int(qtd)}")
        parada = 0  
    elif code not in lista:
        print('Código inválido.')
        parada = 0  
    else:
        quant = int(input('Digite a quantidade do produto: '))
        for i in range(5):
            if code == lista[i]:
                valor += precos[i] * quant
        