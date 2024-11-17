print("imprimir maior e menor")
A=int(input("Informe o primeiro número: "))
B=int(input("Informe o segundo número: "))
C=int(input("Informe o terceiro número: "))

if A>B and A>C and B<C:
    print("%d é o maior e %d o menor"%(A,B))
if A>B and A>C and B>C:
    print("%d é o maior e %d o menor"%(A,C))
if B>A and B>C and A>C:
    print("%d é o maior e %d o menor"%(B,C))
if B>A and B>C and A<C:
    print("%d é o maior e %d o menor"%(B,A))
if C>A and B<C and A<B:
   print("%d é o maior e %d o menor"%(C,A))
if C>A and B<C and A>B:
    print("%d é o maior e %d o menor"%(C,B))