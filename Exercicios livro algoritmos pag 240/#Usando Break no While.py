#Usando Break no While
s=0
while True:
    v=int(input("informe um número para somar ou 0 para sair: "))
    if v==0:
        break
    s=s+v
print(s)