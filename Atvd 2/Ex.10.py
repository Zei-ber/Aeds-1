x = 1
Num = int(input("Digite aqui o número que deseja saber se é primo (ou Sair para sair): "))  
while x <= Num:
    print(x)
                  
    if Num <= 1:
        print("O número digitado não é primo")
        continue
    if Num == 2:
        print("O número digitado é primo")
        continue
    if Num % 2 == 0:
        print("O número digitado não é primo")
        continue
        primo = True
    for i in range(3, int(Num**0.5) + 1, 2):
        if Num % i == 0:
            primo = False
            break
    if primo:
        print("O número digitado é primo")
    else:
        print("O número digitado não é primo")