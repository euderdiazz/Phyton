#questão 50 pag 84
#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir
consumo=int(input("Informe a quantidade consumida (em KWh): "))
print("Instalações")
print("indústria   - I")
print("Comércio    - C")
print("Residencial - R")
tipo=input("informe o tipo de instalação: ")
if tipo==("R" or"r"):
        if consumo<=500:
            preco=consumo*0.40
        else:
            preco=consumo*0.65
elif tipo==("c" or "C"):
        if consumo <=1000:
            preco=consumo*0.55
        else:
            preco=consumo*0.60
elif tipo=="I":
        if consumo<=5000:
            preco=consumo*0.55
        else:
            preco=consumo*0.70
else:
        print("Tipo de instalação inválido! Escolha outro tipo.")
        preco=0
        
print(f"O consumo {consumo:d} kW/h para um estabelecimento do tipo {tipo:s} fica com um valor total de R${preco:.2f}")
print("O consumo %d do tipo comercial %s fica num valor de %.2f"%(consumo,tipo,preco))