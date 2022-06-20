#1166 - Pague o aluguel!

total = int(input())
parcela = int(input())

c = 1

while total > 0:
    print(f"pagamento: {c}")
    print(f"antes = {total}")
    total = total - parcela
    if total < 0:
        total = 0
    print(f"depois = {total}")
    print("-" * 5)
    c =  c + 1
