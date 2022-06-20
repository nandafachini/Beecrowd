#1126 - Dia da entrega

dia_semana =input()
prazo = int(input())
dia = ""

if dia_semana == "segunda":
    dia = 1
elif dia_semana == "terca":
    dia = 2
elif dia_semana == "quarta":
    dia = 3
elif dia_semana == "quinta":
    dia = 4
elif dia_semana == "sexta":
    dia = 5
elif dia_semana == "sabado":
    dia = 6
elif dia_semana == "domingo":
    dia = 7
    
entrega = ((dia + prazo) % 7)

if prazo == 0:
	print("chega hoje!")
elif entrega == 1:
	print("sera entregue segunda")
elif entrega == 2:
	print("sera entregue terca")
elif entrega == 3:
	print("sera entregue quarta")
elif entrega == 4:
	print("sera entregue quinta")
elif entrega == 5:
	print("sera entregue sexta")
elif entrega == 6:
	print("sera entregue sabado")
elif entrega == 0:
	print("sera entregue domingo")
