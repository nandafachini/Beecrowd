#1284 - Segunda Chance

alunos = int(input())

notas_orig = []
notas_novas = []
notas_finais = []

i = 0
i2 = 0
c = 0
posição = 1
notas_alteradas = 0


while i < alunos:
    nota_orig = float(input())
    notas_orig.append(nota_orig)
    i = i + 1

while i2 < alunos:
    nota_nova = float(input())
    notas_novas.append(nota_nova)
    i2 = i2 + 1

while c <= alunos - 1:
    if notas_novas[c] == 10 and notas_orig[c] < 10:
        notas_finais.append(notas_orig[c] + 2)
        if notas_finais[c] > 10:
            notas_finais[c] = 10.00
        notas_alteradas += 1
        #print(f" * ({posição:03d}) original: {notas_orig[c]:05.2f} | final: {notas_finais[c]:05.2f}")
        c += 1
        posição += 1

    else:
        notas_finais.append(notas_orig[c])
        #print(f" - ({posição:03d}) original: {notas_orig[c]:05.2f} | final: {notas_finais[c]:05.2f}")
        c += 1
        posição += 1

c = 0
posição = 1
print(f"NOTAS ALTERADAS: {notas_alteradas}")

while c <= alunos - 1:
    if notas_novas[c] == 10 and notas_orig[c] < 10:
        notas_finais.append(notas_orig[c] + 2)
        if notas_finais[c] > 10:
            notas_finais[c] = 10.00
        notas_alteradas += 1
        print(f"*({posição:03d}) original: {notas_orig[c]:05.2f} | final: {notas_finais[c]:05.2f}")
        c += 1
        posição += 1

    else:
        notas_finais.append(notas_orig[c])
        print(f"-({posição:03d}) original: {notas_orig[c]:05.2f} | final: {notas_finais[c]:05.2f}")
        c += 1
        posição += 1
