#1013 - O Maior

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

def maior_num(numero1, numero2):
    if numero1 - numero2 < 0:
        y = -1
    else:
        y = 1
    maior_num = ((numero1 + numero2) + ((numero1 - numero2)*y))/2 
    return maior_num

maior = maior_num(a, b)

maior_final = maior_num(maior, c)

print(f"{maior_final:.0f} eh o maior")
