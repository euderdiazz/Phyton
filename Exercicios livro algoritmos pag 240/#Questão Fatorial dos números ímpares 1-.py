#Questão 10 - Fatorial dos números ímpares 1-10
cont=1
while cont<=10:
    if cont%2!=0:
        fat=1
        num=cont
        while num>1:
            fat=fat*num
            num-=1
        print(fat) 
    cont+=1
    