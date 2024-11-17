#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago
divida=float(input("Informe o valor da dívida: "))
juros=float(input("informe a taxa de juros mensal (em %): "))/100
mensalidade=float(input("Informe o valor a ser pago mensalmente: "))

mes=0
total_pago=0

total_juros=0

while divida>0: #errei isso 
    mes=mes+1 #errei isso
    tot_juros=divida*juros
    divida=divida+tot_juros
    if mensalidade>divida:#não coloquei isso
        mensalidade=divida
    divida=divida-mensalidade
    total_pago=total_pago+mensalidade
    total_juros=total_juros+tot_juros
    print(f"O mês {mes}: Dívida restante:{divida:.2f}")
    
print(f"O total de meses foi {mes} a um juros total de {total_juros:.2f} e um total pago de {total_pago:.2f}")    
