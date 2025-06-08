# Trabajo integrador 2 - parte completa: dnis y anios de nacimiento

from datetime import datetime

# Parte A: operaciones con dnis

# Dnis del grupo
dnis = {
    "A": 42934557,
    "B": 33924737,
    "C": 40464247,
    "D": 26034888,
    "E": 37027334
}

# Crear conjuntos de digitos unicos por cada dni
conjuntos = {}
for persona, dni in dnis.items():
    digitos = set(int(d) for d in str(dni))
    conjuntos[persona] = digitos

# Asignar cada conjunto a una variable individual
A = conjuntos["A"]
B = conjuntos["B"]
C = conjuntos["C"]
D = conjuntos["D"]
E = conjuntos["E"]

# Operaciones entre conjuntos
union_total = A | B | C | D | E
interseccion_total = A & B & C & D & E
diferencia_AE = A - E
simetrica_AE = A ^ E

# Identificar conjuntos con al menos 6 elementos
alta_diversidad = [nombre for nombre, conjunto in conjuntos.items() if len(conjunto) >= 6]

# Verificar condicion de combinacion amplia
condicion_amplia = len(A) > len(B) and any(x % 2 != 0 for x in C)

# Verificar si hay un unico digito representativo
representativo = len(interseccion_total) == 1

# Mostrar resultados de la parte A
print("===== Parte A: dnis y conjuntos =====")
print("Conjuntos:")
for nombre, conjunto in conjuntos.items():
    print(f"{nombre} = {conjunto}")

print("\nUnion total:", union_total)
print("Interseccion total:", interseccion_total)
print("Diferencia A - E:", diferencia_AE)
print("Diferencia simetrica A △ E:", simetrica_AE)
print("Conjuntos con alta diversidad (6 o mas digitos):", alta_diversidad)
print("¿Condicion de combinacion amplia?:", "Si" if condicion_amplia else "No")
if representativo:
    print("Digito representativo unico:", list(interseccion_total)[0])
else:
    print("No hay un unico digito representativo.")

# Parte B: operaciones con anios de nacimiento

# Anios de nacimiento del grupo
nacimientos = {
    "A": 2003,
    "B": 2001,
    "C": 1999,
    "D": 2000,
    "E": 1998
}

# Anio actual
anio_actual = datetime.now().year

# Inicializar listas y contadores
grupo_z = []
bisiestos = []
pares = 0
impares = 0
cartesiano = []

# Recorrer cada anio de nacimiento
for nombre, anio in nacimientos.items():
    # Verificar grupo Z
    if anio > 2000:
        grupo_z.append(nombre)

    # Verificar si el anio es bisiesto
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        bisiestos.append(nombre)

    # Contar pares e impares
    if anio % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Calcular edad y agregar al producto cartesiano
    edad = anio_actual - anio
    cartesiano.append((anio, edad))

# Mostrar resultados de la parte B
print("\n===== Parte B: anios de nacimiento =====")
print("Integrantes en el grupo Z:", grupo_z)
print("Integrantes nacidos en anio bisiesto:", bisiestos)
print("Cantidad de anios pares:", pares)
print("Cantidad de anios impares:", impares)
print("Producto cartesiano (anio, edad):", cartesiano)
