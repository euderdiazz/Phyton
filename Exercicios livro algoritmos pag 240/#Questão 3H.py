#Questão 3H
#Questão 3G
A=int(input("Informe A:"))
B=int(input("Informe B:"))
C=int(input("Informe C:"))
D=int(input("Informe D:"))
RA2=A-2*(A//2)
RA3=A-3*(A//3)
RB2=B-2*(B//2)
RB3=B-3*(B//3)
RC2=C-2*(C//2)
RC3=C-3*(C//3)
RD2=D-2*(D//2)
RD3=D-3*(D//3)
print("números divisíveis por 2 e 3: ")
if RA2==0 or RA3==0:
    print("%d"%A)
if (RB2==0) or (RB3==0):
    print("%d"%B)
if (RC2==0) or (RC3==0):
    print("%d"%C)
if (RD2==0) or (RD3==0):
    print("%d"%D)