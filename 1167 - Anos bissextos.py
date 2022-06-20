#1167 - Anos bissextos

inicio = int(input())
fim = int(input())

c = 0
i = 0

for x in range(inicio,fim+1):
    if x % 4 == 0 and x % 100 > 0 or x % 400 == 0:
        print(x)
        c = c + 1
        i = i + 1


print(f"bissextos: {c}")
