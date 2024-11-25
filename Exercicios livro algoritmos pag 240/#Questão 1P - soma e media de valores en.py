#Questão 1P - soma e media de valores entre 50 e 70
cont=50
soma=0
tot=0
while cont<=70:
    print(cont)
    if cont%2==0:
        soma+=cont
        tot+=1
    cont+=1
print(cont)
media=soma/(tot)
print(soma)
print("%.2f"%media)