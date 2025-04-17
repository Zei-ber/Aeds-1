n = int(input("Digite quantos números primos deseja ver: "))
contador = 0
num = 2
while contador < n:
    if num == 2:
        print(num)
        contador += 1
    elif num % 2 != 0:
        x = 3
        eh_primo = True
        while x < num:
            if num % x == 0:
                eh_primo = False
                break
            x += 2
        if eh_primo:
            print(num)
            contador += 1
    num += 1