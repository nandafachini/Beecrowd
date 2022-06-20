#1164 - Triângulo alfabético

lista = ['0','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z']

n = int(input())
i = 1

while i <= n:
    print (lista[i]*i)
    i = i+1
