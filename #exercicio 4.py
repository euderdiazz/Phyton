#exercicio 4.8 pag 84
A=int(input("Informe o valor do primeiro número: "))
B=int(input("Informe o segundo número:"))
print("Escolha a categoria:")
print("Multiplicação - 1")
print("Divisão - 2")
print("Adição - 3")
print("Subtração - 4")
categoria=int(input("informe a categoria desejada:"))
if categoria==1:
    res=A*B
elif categoria==2:
    if B!=0:
        res=A/B
    else:
        print("Valor inválido!")
elif categoria==3:
    res=A+B
elif categoria==4:
    res=A-B
else:
    print("Escolha outra categoria entre 1 e 4!")
print(f"O valor da soma de {A:d} e {B:d} é {res:f}")
print("O valor da soma de %d e %d é %f"%(A,B,res))    
    