#1283 - Corra Forrest!

tempos = []

tempo = int(input())

while tempo > 0:
    tempos.append(tempo)
    tempo = int(input())

c = 0
soma_tempos = 0

for tempo in tempos:
    soma_tempos = sum(tempos)
    media = soma_tempos/len(tempos)

print(f"MEDIA: {media :.2f}")

for tempo in tempos:
    if tempo < media:
        print(tempo)
