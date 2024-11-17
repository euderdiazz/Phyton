#Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
A=int(input("Informe o dividendo: "))
B=(int(input("informe o divisor: ")))
x=0
while A>=B:
    A=A-B
    x=x+1
resto=A
print(x)
print(resto)