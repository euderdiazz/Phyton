#QUestão 3E
a=float(input("Informe o valor de A: "))
b=float(input("Informe o valor de B: "))
c=float(input("Informe o valor de C: "))
#Cálculo do valor do delta
delta=b**2-4*a*c
#Cálculo das raízes
if (a!=0 and b!=0 and c!=0):
    if delta>0:
        raiz1=(-b+delta**1/2)/2*a
        raiz2=(-b-delta**1/2)/2*a
        print(f"A equação {a:.2f}X² + {b:.2f}x + {c:.2f} tem como raízes reais os valores {raiz1:.2f} e {raiz2:.2f}")
        print("Valor de delta %.2f"%delta)
    elif delta==0:
        raiz=-b/2*a
        print(f"A equação {a:.2f}X² + {b:.2f}x + {c:.2f} tem apenas uma raíz em R {raiz:.2f}")
    elif delta<0:
        print(f"Com o valor de delta negativo {delta:.2f} não existem raízes reais")
else:
    print("A equação de segundo grau não pode possuir índices zero.")