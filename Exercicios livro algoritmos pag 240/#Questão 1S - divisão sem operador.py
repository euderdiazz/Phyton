#Questão 1S - divisão sem operador
dividendo=int(input("Informe o valor do dividendo: "))
divisor=int(input("Informe o valor do divisor: "))
quociente=0
while dividendo>divisor:
      dividendo=dividendo-divisor
      quociente+=1
print("O resto da divisão é %d"%dividendo)
print("O quociente da divisão é %d"%quociente)
        