#Questão 3C
aluno=input("Informe o nome do aluno: ")
N1=float(input("Informe a primeira nota: "))
N2=float(input("Informe a segunda nota:  "))
N3=float(input("Informe a terceira nota: "))
N4=float(input("Informe a quarta nota:   "))
media=(N1+N2+N3+N4)/4
if media>5:
    situacao="Aprovado"
else:
    situacao="Reprovado"
print(f"O aluno {aluno:s} obteve média {media:.2f} e está {situacao:s}")
print("O aluno %s obteve média de %.2f e está %s"%(aluno,media,situacao))
