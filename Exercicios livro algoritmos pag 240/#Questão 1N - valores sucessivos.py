#Questão 1N - valores sucessivos
tot=0
soma=0

while True:
    num=(int(input("Informe um valor: ")))
    if num<0:
        break
    else:
        soma+=num
        tot+=1
    
media=soma/tot
print("A soma dos valores lidos é %d"%soma)
print(f"O total de valores lidos foi de {tot}")
print("A média dos valores lidos foi de %d"%media)

    