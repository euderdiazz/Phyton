# Função para calcular a redução do tempo de vida
def calcular_reducao_vida(cigarros_por_dia, anos_fumando):
    # Cada cigarro reduz 10 minutos de vida
    minutos_perdidos_por_cigarro = 10
    # Calcula o total de cigarros fumados no período
    total_cigarros = cigarros_por_dia * (anos_fumando * 365)
    # Calcula o total de minutos perdidos
    total_minutos_perdidos = total_cigarros * minutos_perdidos_por_cigarro
    # Converte os minutos perdidos para dias (1 dia = 1440 minutos)
    dias_perdidos = total_minutos_perdidos / 1440
    return dias_perdidos

# Entrada de dados
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

# Calcula a redução do tempo de vida
dias_perdidos = calcular_reducao_vida(cigarros_por_dia, anos_fumando)

# Exibe o resultado
print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida devido ao fumo.")