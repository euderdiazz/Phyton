#Questão 3a livro algoritmos
A=int(input("Informe o primeiro valor: "))
B=int(input("Informe o segundo valor: "))
max(A,B)
min(A,B)
if A>B:
    soma=A-B
else:
    soma=B-A
print(f"A diferença entre {A:d} e {B:d} é {soma:d}")