#Questão 1B - Tabuada
print("""
         TABUADA
          
      [1] ADIÇÃO
      [2] SUBTRAÇÃO
      [3] MULTIPLICAÇÃO
      [4] DIVISÃO
      [5] SAIR     
      """)

while True:
    opcao=int(input("Qual operação deseja apresentar: "))
    if opcao==5:
            break
    elif opcao>=1 and opcao<5:
            num=int(input("Informe o valor para exibir a tabuada: "))
            tabuada=1
            while tabuada<=10:
                if opcao==1:
                    print(f"{num} + { tabuada} = {num + tabuada}")
                elif opcao==2:
                    print(f"{num} - { tabuada} = {num - tabuada}")
                elif opcao==3:
                    print(f"{num} * { tabuada} = {num * tabuada}")
                elif opcao==4:
                    print(f"{num} / { tabuada} = {(num/tabuada):.2f}")
                tabuada+=1
    else:
            print("Escolha outro número!")
