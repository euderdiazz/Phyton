#Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
A=int(input("Informe o primeiro número: "))
B=int(input("Informe o segundo número: "))
count=1
X=0
while count<=B:
        X=A+X
        count+=1
print(X)