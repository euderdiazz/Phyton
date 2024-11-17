#If e Else
idade=int(input("Informe a idade do veículo: "))
if idade>=10:
    print(f"Carro velho com idade de {idade:d} anos")
    print("Carro velho com %d anos"%idade)
else:
    print(f"Carro novo com idade de {idade:d} anos")