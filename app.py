print("--- Calculadora de Consumo Elétrico Inteligente ---")

nome = input("Digite o nome do aparelho (ex.: Geladeira): ")
potencia = float(input(f"Qual a potência do(a) {nome} em watts (W)? "))
horas_dia = float(input("Quantas horas por dia o aparelho fica ligado? "))

# Cálculo
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75

# Exibição formatada
print("\n--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")