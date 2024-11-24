#Questão 5.21


while True:
    atual=50
    cedulas=0
    valor=int(input("Informe o valor do pagamento: "))
    apagar=valor
    
    if valor==0:
        break    
    while True:
        if atual<=apagar:
            apagar=apagar-atual
            cedulas+=1
        else:
            print("%d cédula(s) de R$%d"%(cedulas,atual))
            if apagar==0:
                break
            if atual==50:
                atual=20
            elif atual==20:
                atual=10
            elif atual==10:
                atual=5
            elif atual==5:
                atual=1
            cedulas=0        
    