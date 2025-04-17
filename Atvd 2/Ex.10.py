n = int(input("Digite quantos números primos deseja ver: "))
contador = 0
num = 2
while contador < n:
    if num == 2:
        print(num)
        contador += 1
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                break  
        else:
            print(num)  
            contador += 1
    num += 1