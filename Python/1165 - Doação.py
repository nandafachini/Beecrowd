#1165 - Doação

n = float(input())
soma = 0

while n != -1:
    soma = soma + n
    n = float(input())


print(f"VC$ {soma :.2f}")
print(f"R$ {soma*2.5 :.2f}")
