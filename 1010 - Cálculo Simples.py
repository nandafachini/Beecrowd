#1010 - Cálculo Simples

i = 0

codigo = []
qtde = []
valor = []

codigos = []
qtdes = []
valores = []

int_codigos = []
int_qtdes = []
float_valores = []

while i < 2:
    codigo, qtde, valor = input().split()
    codigos.append(codigo)
    qtdes.append(qtde)
    valores.append(valor)
    i = i + 1

for a in codigos:
    int_codigos.append(int(a))

for b in qtdes:                    
    int_qtdes.append(int(b))

for c in valores:
    float_valores.append(float(c))

c = 0
valor_pagar = 0
while c < len(float_valores):
    for d in int_qtdes:
        valor_pagar = valor_pagar + (d * float_valores[c])
        c = c + 1
print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")
