#Questão 1I - Fibonacci
serie=int(input("Informe até onde deseja ver a série: "))
final=2
num1=0
num2=1
print(num1)
print(num2)
while final<=serie:
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
    final+=1
    
