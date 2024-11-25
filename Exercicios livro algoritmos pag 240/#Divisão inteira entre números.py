#Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
dividendo=int(input("Informe o valor a ser dividido: "))
divisor=int(input("Informe o valor do divisor: "))
divisao=dividendo
cont=0
while divisao>divisor:
    divisao=divisao-divisor
    cont+=1
print(f"A divisão inteira é {cont} " + "e resto da divisão é %d"%divisao)
    