salario=1200
imposto=salario>1200
print(imposto)
materia1=7.0
materia2=8.0
materia3=6.0
media=(materia1+materia2+materia3)/3
aprovado=media>=7.0

print(aprovado)
print(len("casa"))

S="abc"
print(S+"D")
print(S+"D"*4)
print("X"+"-"*10+"x")
print(S+"x4="+S*4)

idade=22
print("[%d]"%idade)
print("[%3d]"%idade)
print("[%03d]"%idade)
print("[%-3d]"%idade)
#Exibir 5 reais
print("R$%f"%5)
#Exibir com número reduzido de casas decimais
print("[%4.2F]"%5)

#Combinação entre diferentes tipos de dados
print("%s tem %d anos e apenas R$%5.2f no bolso"%("João",22,51.34))
print("%12s tem %05d anos e apenas R$%8.7f no bolso"%("João",22,51.34))

S="ABCDEFGI"
print(S[0:3])#o índice do último caractere não o inclui na string (não aparece)
print(S[2:7])
print(S[1:5])
print(S[2:3])
print(S[0:4])
print(S[-2:])
print(S[:3])
X=input("Digite um número: ")
print(X)
nome=input("Digite seu nome: ")
print("Você digitou %s"%nome)
print("Olá,%s!"%nome)

anos=int(input("Anos de serviço: "))
valor_por_ano=float(input("Valor por ano: "))
bonus=anos*valor_por_ano
print("Bônus de R$%5.2f por ano"%bonus)