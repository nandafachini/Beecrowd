#1282 - ImpacTube

canais = int(input())

i = 0

nomes = []
inscritos = []
monetizações = []
premiuns = []
int_inscritos = []
float_monetizações = []


while i < canais:
    nome,inscrito,monetização,premium = input().split(";")
    nomes.append(nome)
    inscritos.append(inscrito)
    monetizações.append(monetização)
    premiuns.append(premium)
    i = i + 1
    
x = float(input())
y = float(input())

for a in inscritos:
    int_inscritos.append(int(a))
    
for b in monetizações:
    float_monetizações.append(float(b))


print("-"*5)
print("BÔNUS")
print("-"*5)

c = 0


for nome in nomes:
    if int_inscritos[c] >= 1000:
        if premiuns[c] == "sim":
            bonificação = ((int_inscritos[c] // 1000) * x) + float_monetizações[c]
            print(f"{nomes[c]}: R$ {bonificação :.2f}")
            c = c + 1
        elif premiuns[c] == "não":
            bonificação = ((int_inscritos[c] // 1000) * y) + float_monetizações[c]
            print(f"{nomes[c]}: R$ {bonificação :.2f}")
            c = c + 1
    else:
        bonificação = float_monetizações[c]
        print(f"{nomes[c]}: R$ {bonificação :.2f}")
        c = c + 1
