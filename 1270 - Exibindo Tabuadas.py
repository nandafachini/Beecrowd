#1270 - Exibindo Tabuadas

a = int(input())
b = int(input())

i = 1

if a > b:
    print("Nenhuma tabuada no intervalo!")

for x in range(a,b+1):
    i = 1
    while i <= 10:
        print(x, "x", i,"=", x*i)
        i = i + 1
    print("-"*10)
