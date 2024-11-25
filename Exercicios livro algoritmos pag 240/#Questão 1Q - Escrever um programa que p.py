#Questão 1Q - Escrever um programa que possibilite calcular a área total em metros de uma residência com os cômodos sala
areaTotal=0
soma=0
resp="s" or "S" or "sim" or "Sim" or "Sim" or "SIm" or "SIM" or "sIM" or "siM"
while resp=="s" or resp=="S" or resp=="sim" or resp=="Sim" or resp=="Sim" or resp=="SIm" or resp=="SIM" or resp=="sIM" or resp=="siM":
    areaTotal=0
    comodo=input("Informe o nome do cômodo que deseja calcular a área: ")
    largura=float(input("Informe a largura do %s :"%comodo))
    comprimento=float(input("Informe o comprimento do %s: "%comodo))
    areaTotal+=largura*comprimento
    soma+=areaTotal
    print("Deseja calcular a área e outro cômodo [S/N]?")
    resp=input()
print(f"A área total da residência se´ra de {soma}")