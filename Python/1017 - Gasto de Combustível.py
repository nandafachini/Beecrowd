#1017 - Gasto de Combustível

#automóvel faz 12 KM/L.

tempo = int(input())
velocidade = int(input())

km_rodados = tempo * velocidade

litros = km_rodados/12

print(f"{litros:.3f}")
