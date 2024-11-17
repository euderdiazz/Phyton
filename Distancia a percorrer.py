#Distancia a percorrer
distancia=float(input("Informe a distância a percorrer em km: "))
if distancia<=200:
    preco=distancia*0.5
    print(f"O preço a ser pago para uma distância de {distancia:.2f} km é de R$ {preco:.2f}")
    print("O preço a ser pago por uma distância de %.2f km é de R$%.2f"%(distancia,preco))
else:
    preco=distancia*0.45
    print(f"Para uma distância de {distancia:.2f} km o valor a ser pago será de R$ {preco:.2f}")
    print("Para a distância de %.2f km o valor a ser pago será de R$ %.2f"%(distancia,preco))