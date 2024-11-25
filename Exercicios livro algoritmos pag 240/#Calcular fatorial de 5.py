#Calcular fatorial de n

while True: 
    num=int(input("Informe um número para calcular o fatorial: "))
    fat=1
    cont=num       
    while cont>1:
        fat=fat*cont
        cont-=1
    print(fat)
    if num==0:
        break
