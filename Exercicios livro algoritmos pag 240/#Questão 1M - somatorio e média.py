#Questão 1M - somatorio e média

cont=1
soma=0

while cont<=10:
    num=int(input("Informe um número: "))
    soma+=num
    cont+=1    
media=soma/10
print(soma)
print(media)