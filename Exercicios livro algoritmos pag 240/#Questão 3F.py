#Questão 3F
A=int(input("Informe o valor de A: "))
B=int(input("Informe o valor de B: "))
C=int(input("Informe o valor de C: "))

if A>B:
    X=A
    A=B
    B=X
elif A>C:
    X=A
    A=C
    C=X
    if B>C:
        X=B
        B=C
        C=X
print("A ordem crescente é: %d, %d e %d"%(A,B,C))