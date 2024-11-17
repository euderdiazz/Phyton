# Perguntar o valor inicial da dívida, a taxa de juros e o valor mensal de pagamento
valor_divida = float(input("Digite o valor inicial da dívida: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100  # Convertendo para decimal
valor_pagamento_mensal = float(input("Digite o valor que será pago mensalmente: R$ "))

# Variáveis de controle
total_pago = 0
total_juros_pago = 0
meses = 0

# Enquanto a dívida não for paga
while valor_divida > 0:
    meses += 1
    # Calcula os juros sobre a dívida atual
    juros_mes = valor_divida * taxa_juros
    valor_divida += juros_mes  # Atualiza a dívida com os juros

    # Verifica se o pagamento mensal é suficiente para quitar a dívida
    if valor_pagamento_mensal > valor_divida:
        valor_pagamento_mensal = valor_divida  # Ajusta o pagamento para o valor restante da dívida

    valor_divida -= valor_pagamento_mensal  # Subtrai o pagamento mensal da dívida
    total_pago += valor_pagamento_mensal  # Acumula o valor pago no total
    total_juros_pago += juros_mes  # Acumula os juros pagos no total

    # Exibe o progresso mês a mês (opcional)
    print(f"Mês {meses}: Dívida restante: R$ {valor_divida:.2f}")

# Exibir o número total de meses, o total pago e o total de juros pagos
print(f"\nA dívida foi paga em {meses} meses.")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pagos: R$ {total_juros_pago:.2f}")