print("Cálculo de multa")
velocidade=float(input("Informe o valor da velocidade (em km/h): "))
if velocidade>80:
    multa=(velocidade-80)*5
    print("O usuário foi multado em R$ %4.2f" %multa)
if velocidade<=80:
    print("Usuário livre de multa!")