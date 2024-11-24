#Questão 5.22
#Tabuada

def menu():
    print("""
        TABUADA
           
    [1] ADIÇÃO       
    [2] SUBTRAÇÃO    
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO      
    [0] SAIR         
    """)

while True:
    
    tabuada=1
    menu()
    print()
    opcao=int(input("Escolha a opção desejada: "))
    
    if opcao==0:
        break
    elif opcao>=1 and opcao<5:
        numero=int(input("Tabuada de qual valor:"))
        tabuada=1
        while tabuada<=10:
            if opcao==1:
                print(f"{numero} + {tabuada} = {numero+tabuada}")
            elif opcao==2:
                print(f"{numero} - {tabuada} = {numero-tabuada}")
            elif opcao==3:
                print(f"{numero} * {tabuada} = {numero*tabuada}")
            elif opcao==4:
                print(f"{numero} / {tabuada} = {numero/tabuada:5.2f}")
            tabuada+=1
    else:
        print("Opção inválida! Escolha um valor entre 1 e 5")
            
                
        