#Questão 1R - informar valores
maior=0
menor=99999999
while True:
    num=int(input("Informe um valor:"))
    if num<0:
        break
    elif num>maior:
        maior=num
    if num<menor:
        menor=num
print(maior)
print(menor)
    