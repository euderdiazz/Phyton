#Caixa pagamento - criar programa que diga quantas cédulas são necessárias para pagar
print("cédulas disponíveis: R$1, R$5, R$10, R$20 e R$50")
apagar=int(input("Informe o valor da compra: "))
pago=int(input("Informe o valor pago: "))
troco=0

while pago>apagar:
    troco=pago-apagar
    if troco>=100:
        centena=troco//100
        resto_centena=troco-(centena*100)
        print(resto_centena)
        dezena=resto_centena//10
        if centena>0:
            print(f"Você receberá {centena*2} notas de R$50")
        if resto_centena<50:
            nota=int(input("Escolha o tipo de nota para troco (R$10, R$20): "))
            if nota==10:
               print(f"Você recebrá {(resto_centena//10)} notas de R$10")
            elif nota==20:
                nota10=((resto_centena//10)-(resto_centena//20))
                print(f"Você recebrá {(resto_centena//20)} notas de R$20 e {nota10-(resto_centena//20)} notas de R$10")
            
        elif resto_centena>=50:
            if (resto_centena >=60 and resto_centena<=69):
                nota10=((resto_centena//10)-(resto_centena//50))
                print(f"Você recebrá {(resto_centena//50)} notas de R$50 e {(resto_centena//10)-nota10} nota de R$10")
            elif (resto_centena>=80 and resto_centena<=89):
                nota10=((resto_centena//10)-(resto_centena//50))
                print(f"Você recebrá {(resto_centena//50)} notas de R$50, {resto_centena//50} notas de R$ 20 e {(resto_centena//10)-nota10} notas de R$10")
            elif (resto_centena//20)-(resto_centena//50)==1:
                print(f"Você recebrá {(resto_centena//50)} notas de R$50")
            else:
                print(f"Você recebrá {(resto_centena//50)} notas de R$50 e {(resto_centena//20)-((resto_centena//20)-(resto_centena//50))} notas de R$20")
        resto_centena=troco-(centena*100)-(dezena*10)
        print(resto_centena)
        print(f"Você recebrá {resto_centena} notas de R$1")
    else:
        dezena=troco//10
        resto_dezena=troco-(dezena*10)
        if resto_dezena<50:
            nota=int(input("Escolha o tipo de nota para troco (ABC) (R$10, R$20): "))
            if nota==10:
               print(f"Você recebrá {(troco//10)} notas de R$10")
            elif nota==20:
                nota10=((troco//10)-(troco//20))
                print(f"Você recebrá {(troco//20)} notas de R$20 e {nota10-(troco//20)} notas de R$10")
        elif resto_dezena>=50:
            if (troco >=60 and troco<=69):
                nota10=((troco//10)-(troco//50))
                print(f"Você recebrá {(troco//50)} notas de R$50 e {(troco//10)-nota10} nota de R$10")
            elif (troco>=80 and troco<=89):
                nota10=((troco//10)-(troco//50))
                print(f"Você recebrá {(troco//50)} notas de R$50, {troco//50} notas de R$ 20 e {(troco//10)-nota10} notas de R$10")
            elif (troco//20)-(troco//50)==1:
                print(f"Você recebrá {(troco//50)} notas de R$50")
            else:
                print(f"Você recebrá {(troco//50)} notas de R$50 e {(troco//20)-((troco//20)-(troco//50))} notas de R$20")
        resto_dezena=troco-(dezena*10)
        print(resto_dezena)
        print(f"Você recebrá {resto_dezena} notas de R$1")
    break