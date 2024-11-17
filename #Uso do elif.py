#Uso do elif
categoria=int(input("Informe a categoria do produto: "))
if categoria==1:
    preco=10
elif categoria==2:
    preco=18
elif categoria==3:
    preco=23
elif categoria==4:
    preco=26
elif categoria==5:
    preco=31
print(f"O valor do produto da categoria {categoria:d} escolhido é de R${preco:d}")
print("O valor do produto da categoria %d custa R$ %d"%(categoria,preco))    

    