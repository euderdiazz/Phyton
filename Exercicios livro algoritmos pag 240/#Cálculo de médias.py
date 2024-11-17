#Cálculo de médias
n=1
soma=0
while n<=7:
    x=int(input("Informe o número %d: " %n))
    soma=soma+x
    n=n+1 #(ou n+=1)
media=soma/(n-1)
print(soma)
print(media)
print(str(soma))
print(str(media))
print(bool(soma))
print(bool(media))
print(float(media))
print(float(soma))
print(type(soma))
print(type(media))