#Informar os n primeiros números primos
num=int(input("Informe um número: "))
cont=0
i=2 #2 pq o 1 não é primo
j=1
while i<=num:
    while j<=i:
        if i%j==0:
            cont+=1
        j+=1
    if cont==2:
        print(i)
    i+=1
    j=1
    cont=0

        
            