Num = int(input("Digite aqui o número que deseja saber se é primo:"))                
if Num == 1 or Num == 0:
    print("Caso especial")
else:
    if Num == 2:
        print("O número digitado é primo")
    elif Num % 2 == 0:
        print("O número digitado não é primo")
    else:
        x = 3
        while x<Num:
            if Num%x == 0:
                break
            x = x+2
        if x == Num:
            print("Este número é primo")
        else:
            print("Este número não é primo")