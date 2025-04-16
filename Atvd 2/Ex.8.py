parada = 1
while(parada != 0):
    Menu = ["Adição", "Subtração", "Divisão", "Multiplicação", "Sair"]
    print("menu = [Adição, Subtração, Divisão, Multiplicação, Sair]")
    oper = str(input("Digite qual a operação você gostaria de ver a tabuada:"))
    if oper not in Menu:
        print("Confira se digitou uma operação do menu e se não há erros ortográficos.")
    else:
    
        if oper == "Adição":
            print("="*50)
            print("+ |  1  2  3  4  5  6  7  8  9 10")
            print("--+------------------------------")
            print("1 |  2  3  4  5  6  7  8  9 10 11")
            print("2 |  3  4  5  6  7  8  9 10 11 12")
            print("3 |  4  5  6  7  8  9 10 11 12 13")
            print("4 |  5  6  7  8  9 10 11 12 13 14")
            print("5 |  6  7  8  9 10 11 12 13 14 15")
            print("6 |  7  8  9 10 11 12 13 14 15 16")
            print("7 |  8  9 10 11 12 13 14 15 16 17")
            print("8 |  9 10 11 12 13 14 15 16 17 18")
            print("9 | 10 11 12 13 14 15 16 17 18 19")
            print("10| 11 12 13 14 15 16 17 18 19 20")
            print("="*50)
            
        if oper == "Subtração":
            print("="*50)
            print("-  |  1   2   3   4   5   6   7   8   9  10")
            print("---+--------------------------------------")
            print("1  |  0  -1  -2  -3  -4  -5  -6  -7  -8  -9")
            print("2  |  1   0  -1  -2  -3  -4  -5  -6  -7  -8")
            print("3  |  2   1   0  -1  -2  -3  -4  -5  -6  -7")
            print("4  |  3   2   1   0  -1  -2  -3  -4  -5  -6")
            print("5  |  4   3   2   1   0  -1  -2  -3  -4  -5")
            print("6  |  5   4   3   2   1   0  -1  -2  -3  -4")
            print("7  |  6   5   4   3   2   1   0  -1  -2  -3")
            print("8  |  7   6   5   4   3   2   1   0  -1  -2")
            print("9  |  8   7   6   5   4   3   2   1   0  -1")
            print("10 |  9   8   7   6   5   4   3   2   1   0")
            print("="*50)
            
        if oper == "Divisäo":
            print("="*50)
            print("÷  |  1     2     3     4     5     6     7     8     9    10")
            print("---+---------------------------------------------------------")
            print("1  | 1.0   0.5   0.3   0.3   0.2   0.2   0.1   0.1   0.1   0.1")
            print("2  | 2.0   1.0   0.7   0.5   0.4   0.3   0.3   0.2   0.2   0.2")
            print("3  | 3.0   1.5   1.0   0.8   0.6   0.5   0.4   0.4   0.3   0.3")
            print("4  | 4.0   2.0   1.3   1.0   0.8   0.7   0.6   0.5   0.4   0.4")
            print("5  | 5.0   2.5   1.7   1.3   1.0   0.8   0.7   0.6   0.6   0.5")
            print("6  | 6.0   3.0   2.0   1.5   1.2   1.0   0.9   0.8   0.7   0.6")
            print("7  | 7.0   3.5   2.3   1.8   1.4   1.2   1.0   0.9   0.8   0.7")
            print("8  | 8.0   4.0   2.7   2.0   1.6   1.3   1.1   1.0   0.9   0.8")
            print("9  | 9.0   4.5   3.0   2.3   1.8   1.5   1.3   1.1   1.0   0.9")
            print("10 |10.0   5.0   3.3   2.5   2.0   1.7   1.4   1.3   1.1   1.0")
            print("="*50)
            
        if oper == "Multiplicação":
            print("="*50)
            print("×  |  1   2   3   4   5   6   7   8   9  10")
            print("---+-------------------------------------")
            print("1  |  1   2   3   4   5   6   7   8   9  10")
            print("2  |  2   4   6   8  10  12  14  16  18  20")
            print("3  |  3   6   9  12  15  18  21  24  27  30")
            print("4  |  4   8  12  16  20  24  28  32  36  40")
            print("5  |  5  10  15  20  25  30  35  40  45  50")
            print("6  |  6  12  18  24  30  36  42  48  54  60")
            print("7  |  7  14  21  28  35  42  49  56  63  70")
            print("8  |  8  16  24  32  40  48  56  64  72  80")
            print("9  |  9  18  27  36  45  54  63  72  81  90")
            print("10 | 10  20  30  40  50  60  70  80  90 100")
            print("="*50)
            
        if oper == "Sair":
            parada = 0
    