#Questão 1H - expoente de um número qualquer
num=int(input("Informe o valor da base: "))
exp=int(input("Informe o valor do expoente:"))
exp2=1
valor=0
num2=1
while exp2<=exp:
      valor=num*num2
      num2=valor
      exp2+=1
print(valor)  
