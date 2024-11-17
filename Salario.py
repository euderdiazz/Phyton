print("Cálculo do salário")
salario=float(input("informe o valor do salário: "))
if salario>1250:
    print("O valor do aumento sobre o salário de %5.2f será de: R$%5.2f"%(salario,(salario+(salario*10/100))))
if salario <1250:
    aumento=salario*15/100
    print(f"O valor do aumento sobre o salário de {salario:.2f} será de {aumento:.2f}")