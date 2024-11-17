#cálculo de juros em montante (não consegui fazer sozinho)

deposito=float(input("Informe o valor (em R$) depositado:")) 

juros=float(input("Informe a taxa de juros (mensal) (em %): "))
deposito_mensal=float(input("Informe o valor do depósito mensal: "))
saldo=deposito
rendimento=0
rendimento_total=0
total_juros=0
mes=1
while mes<=6:
    saldo_juros=saldo*(juros/100)
    saldo=saldo+saldo_juros
    saldo=saldo+deposito_mensal
    total_juros=total_juros+saldo_juros
    print(f"Juros: {saldo_juros:.2f}")
    mes+=1
print(f"O juros no mês {mes} foi de {total_juros:0.2f}")
