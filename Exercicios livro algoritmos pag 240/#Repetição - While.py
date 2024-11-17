#Repetição - While
x=10
while x>=0:
    print(x,end=",")
    x=x-1
print(" e Fogo!")
num=int(input("Informe até quanto deseja contar: "))
x=0
while x<=num:
    if x%2==0:
        print(x,end=",")
    x=x+1
#While sem if
print()
num=int(input("Informe até quanto deseja contar: "))
x=0
while x<=num:
    print(x,end=",")
    x=x+2
 

#Números ímpares
print()
num=int(input("Informe até quanto deseja (ímpares) contar: "))
x=0
while x<=num:
    if x%2!=0:
        print(x,end=",")
    x=x+1   
    
#múltiplos de 3
num=int(input("Informe um número: "))
x=0
while x<=num:
    if x%3==0:
        print(x,end=",")
    x=x+1       
       
