#Calculo de Fatorial

cont=0
soma=0
while cont<15:
    fat=1
    num=int(input("Informe o valor para calcular fatorial: "))
    import os
    os.system('cls')
    while num>1:
        fat=fat*num
        num-=1
    soma+=fat
    cont+=1
print(soma)