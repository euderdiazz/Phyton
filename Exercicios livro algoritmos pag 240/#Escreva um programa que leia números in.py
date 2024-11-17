#Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética
soma=0
media=0
c=1
while c!=0:
    num=int(input("Informe um número ou 0 para sair: "))
    if num==0:
        break
    soma=soma+num
    c+=1
media=soma/(c-1)
print(c)
print("Soma %d"%soma)
print("Média: %.2f"%media)
print("Total de números digitados: %d"%(c-1))
    
