#Tabuada soma
i=int(input("Informe o valor para ver a tabuada: "))
x=1
while x<=10:
    print(i,"+",x,"=",i+x)
    x+=1
#Tabuada até onde o usuário desejar    
inicio=int(input("Informe o valor onde deseja começar a tabuada (1-10): "))
fim=int(input("Informe o valor onde deseja terminar a tabuada (2-10): "))
numero=int(input("Informe o número para ver a tabuada: "))

while inicio<=fim:
        print(f"{numero} x {inicio} = {numero*inicio}")
        inicio+=1
