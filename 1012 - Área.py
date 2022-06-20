#1012 - Área

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

def area_triangulo_retangulo(base,altura):
    area = (base * altura) / 2
    return area

def area_circulo(raio):
    pi = 3.14159
    area = pi * raio**2
    return area

def area_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return area

def area_quadrado(lado):
    area = lado * lado
    return area

def area_retangulo(base, altura):
    area = base * altura
    return area


area1 = area_triangulo_retangulo(a,c)
print(f"TRIANGULO: {area1:.3f}")

area2 = area_circulo(c)
print(f"CIRCULO: {area2:.3f}")

area3 = area_trapezio(a, b, c)
print(f"TRAPEZIO: {area3:.3f}")

area4 = area_quadrado(b)
print(f"QUADRADO: {area4:.3f}")

area5 = area_retangulo(a, b)
print(f"RETANGULO: {area5:.3f}")
