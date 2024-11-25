num=float(input("Informe o valor para calcular a raiz quadrada:"))
b=2
while abs(num-(b*b))>0.00001:
    p=1/2*(b+(num/b))
    b=p
print(f"A raiz do número {num} é {b:5.2f}")