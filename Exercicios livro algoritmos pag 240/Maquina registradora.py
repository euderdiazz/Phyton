#Escreva um programa para controlar uma pequena máquina registradora.
print("Máquina registradora")
print("Lista dos produtos disponíveis")
print("Código - Produto - Preço")
print("[1] |    Pão (unid) | R$0.50")
print("[2] |    Arroz (kg) | R$1.00")
print("[3] |    Leite (L)  | R$4.00")
print("[5] |    Feijão (kg)| R$7.00")
print("[9] |    Carne (kg) | R$8.00")
print("[0] | Sair                  ")

total=0
produto1=0
produto2=0
produto3=0
produto5=0
produto9=0
while True:
    produto=int(input("Informe a opção desejada: "))
    if produto==0:
        break
    if produto!=1 and produto!=2 and produto!=3 and produto!=5 and produto!=9:
        print("Código Inválido!")
        produto=int(input("Informe a opção desejada: "))
    quantidade=int(input("Informe a quantidade desejada: "))
    if produto==1:
        total=total+(quantidade*0.5)
        produto1=produto1+quantidade
    if produto==2:
        total=total+(quantidade*1.00)
        produto2=produto2+quantidade
    if produto==3:
        total=total+(quantidade*4.00)
        produto3=produto3+quantidade
    if produto==5:
        total=total+(quantidade*7.00)
        produto5=produto5+quantidade
    if produto==9:
        total=total+(quantidade*8.00)
        produto9=produto9+quantidade
    
print(f"Sua compra totalizou R${total:.2f} e sua lista inclui:")
print(f"Pão:    {produto1} unidade(s);") 
print(f"Arroz:  {produto2} quilo(s);")
print(f"Leite:  {produto3} litro(s);")   
print(f"Feijão: {produto5} quilo(s);")
print(f"Carne:  {produto9} quilo(s).")