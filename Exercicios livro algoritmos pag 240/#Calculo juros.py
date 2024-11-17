#Calculo juros
deposito=float(input("Informe o valor do depósito: "))
juros=float(input("Informe o valor dos juros: "))
x=1
total=0
while x<=24:
    total=total+((deposito*juros)/100)
    print(f"No mês {x} o rendimento foi de {total}")
    x+=1
rendimento=deposito+total
print(f"O rendimento foi de {rendimento}")