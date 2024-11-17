#Questão 3D
aluno=input("Informe o nome do aluno: ")
N1=float(input("Informe a primeira nota do aluno %s :"%aluno))
N2=float(input("Informe a segunda nota do aluno %s :"%aluno))
N3=float(input("Informe a terceira nota do aluno %s :"%aluno))
N4=float(input("Informe a quarta nota do aluno %s :"%aluno))
media=((N1+N2+N3+N4)/4)
if media>=7.0:
    print(f"O aluno {aluno:s} está aprovado!")
else:
    print(f"O aluno {aluno:s} não obteve média suficiente para aprovação. Média: {media:.2f}")
    NE=float(input("Informe a nota do exame: "))
    media2=(media+NE)/2
    if media2>=5:
        print(f"O aluno {aluno:s} foi aprovado em exame com média de {media2:.2f}")
    else:
        print("O aluno %s foi reprovado em exame ficando com média insuficiente %.2f"%(aluno,media2))