print("Digite dois números inteiros: ")
A=int(input("Digite o primeiro número: "))
B=int(input("Digite o segundo número: "))
C=A+B
print("Os números digitados foram %d e %d e sua soma foi de %d"%(A,B,C))
print("Converter metros em milímetros")
A=float(input("Informe o valor (em m) a ser convertido: "))
B=A*1000
print("O valor de %2.2f metros em milímetros é de %2.2f milímetros"%(A,B))
print("Calcular os segundos")
A=int(input("Informe o valor das horas: "))
B=int(input("Informe o valor dos minutos: "))
C=int(input("informe o valor dos segundos: "))
D=A*3600
E=B*60
F=C+D+E
print("O tempo informado em horas (%d),minutos(%d) e segundos(%d) representa um total de %d segundos"%(A,B,C,F))
print("------------------")
print("Cálculo do salário")
print("------------------")
salario=float(input("informe o valor do salário: "))
aumento=int(input("Informe o valor do aumento: "))
salarioReal=salario+(salario*aumento/100)
print("O salário de %5.2f com um aumento de %d é de %5.2f"%(salario,aumento,salarioReal))
print("-------------------")
print("Cálculo de desconto")
print("-------------------")
preco=float(input("Informe o preço do produto: "))
desconto=int(input("Informe o valor do desconto: "))
novoPreco=preco-(preco*desconto/100)
print("o produto com o preço %3.2f e com desconto de %3.2f custará %3.2f"%(preco, (preco*desconto/100),novoPreco))
print("----------------")
print("Cálculo do tempo")
print("----------------")
distanciaPercorrida=float(input("Informe a distância percorrida (em m): "))
velocidadeMedia=float(input("Informe a velocidade (em m/s): "))
print("O tempo gasto (em segundos) foi de %2.1f segundos"%(distanciaPercorrida/velocidadeMedia))
print("O tempo gasto (em horas) foi de %2.2f horas"%((distanciaPercorrida/velocidadeMedia)/3600))
print("---------------------")
print("CONVERTER TEMPERATURA")
print("---------------------")
C=float(input("Informe a temperatura (ºC): "))
F=((9*C/5)+32)
print("O valor da temperatura %3.2f convertida em Fahrenheit é de %3.2F"%(C,F))