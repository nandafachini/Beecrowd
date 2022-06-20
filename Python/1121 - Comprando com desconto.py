#1121 - Comprando com desconto

preco = float (input())
quantidade = int (input())

valor_compra = preco * quantidade
print("%.2f" % valor_compra)

valor_final = valor_compra - (valor_compra * ((quantidade + 10)/100))
print(f"%.2f" % valor_final)
