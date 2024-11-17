#Preço telefone minutos
minutos=int(input("Informe o número de minutos utilizados:"))
if minutos<200:
    preco=0.2
    print(f"O valor a ser pago será de R$ {minutos*preco:.2f}")
    print("O valor a ser pago será de R$ %3.2f"%(minutos*preco))
else:
    if minutos<400:
        preco=0.18
        print(f"O valor a ser pago será de R$ {minutos*preco:.2f}")
        print("O valor a ser pago será de %3.2f"%(minutos*preco))
    else:
        preco=0.15
        print(f"O valor a sr pago será de R$ {minutos*preco:.2f}")
        print("O valor a ser pago será de R$ %3.2f"%(minutos*preco))