#numeros primos
while True: 
    num=int(input("Informe um número para verificar se é primo: "))
    div=1
    totDiv=0
    if num==0 or num==1:
        print(f"{num} estes são casos especiais. ")
        print()
        break
    while div>=1 and div<=num:
        if num%div==0:
            totDiv+=1
        div+=1
    if totDiv==2: 
        print("O número %d é primo"%num)
    else:
        print("O número %d não é primo"%num)