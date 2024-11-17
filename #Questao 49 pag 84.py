#Questao 49 pag 84
#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
casa=float(input("Informe o valor da casa (em R$): "))
salario=float(input("Informe o salário (em R$): "))
anos=float(input("Informe o tempo (em anos) para pagamento: "))
prestacao=casa/(anos*12)
if prestacao>(salario*30/100):
    print(f"O valor da casa R$ {casa:.2f} para ser pago em parcelas de R$ {prestacao:.2f}/mês não é permitido com esse salário (R${salario:.2f})")
else:
    print("O valor da casa (R$%.2f) com o salário de %.2f será pago em parcelas de R$%.2F/mês"%(casa,salario,prestacao))