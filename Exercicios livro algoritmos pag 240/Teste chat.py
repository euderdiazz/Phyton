# Perguntar o depósito inicial, a taxa de juros e o depósito mensal
deposito_inicial = float(input("Digite o depósito inicial: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100  # Convertendo para decimal
deposito_mensal = float(input("Digite o valor do depósito mensal: R$ "))

# Variáveis de controle
saldo = deposito_inicial
total_juros = 0
mes = 1

# Exibe o saldo mês a mês
while mes <= 6:  # De 1 a 6 meses
    saldo_juros = saldo * taxa_juros
    saldo += saldo_juros  # Calcula o juros sobre o saldo
    saldo += deposito_mensal  # Adiciona o depósito mensal no saldo
    total_juros += saldo_juros
    print(f"Mês {mes}: R$ {saldo:.2f} (Juros: R$ {saldo_juros:.2f})")
    mes += 1  # Avança para o próximo mês

# Exibir o total ganho com juros
print(f"\nTotal ganho com juros no período de 6 meses: R$ {total_juros:.2f}")