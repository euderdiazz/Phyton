#Categoria e preço
categoria=int(input("Informe a categoria do produto: "))
quantidade=int(input("Informe a quantidade adquirida: "))
if categoria==1:
    preco=10
else:
    if categoria==2:
       preco=18
    else:
        if categoria==3:
            preco=23
        else:
            if categoria==4:
                preco=26
            else:
                if categoria==5:
                    preco=31
                else:
                    print("Categoria inválida! Escolha outro valor.")
                    preco=0
print(f"O preço do produto na categoria {categoria:d} é o valor final é R$ {(preco*quantidade):d}")
print("O produto está na categoria %d e o valor total é de %d"%(categoria,(preco*quantidade)))           