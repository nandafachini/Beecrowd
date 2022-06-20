#1168 - Intervalo de primos!

inicio = int(input())
fim = int(input())

if inicio == 1:
    inicio = 2
    
counter = 0

for x in range(inicio, fim + 1):
    found = False
    for y in range(2, x, 1):
        if x % y == 0:
            found = True
    if not found:
        print(x)
        counter = counter + 1
print(f'primos: {counter}')
