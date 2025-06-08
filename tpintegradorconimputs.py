# Trabajo integrador 2 - version con ingreso de dnis y textos con ñ

from datetime import datetime

# Parte A: ingreso de dnis por teclado
print("===== Parte A: ingreso de DNIs =====")
dnis = {}
etiquetas = ["A", "B", "C", "D", "E"]

for etiqueta in etiquetas:
    while True:
        entrada = input(f"Ingrese el DNI de la persona {etiqueta} (solo números): ")
        if entrada.isdigit() and len(entrada) == 8:
            dnis[etiqueta] = int(entrada)
            break
        else:
            print("DNI inválido. Debe tener 8 dígitos numéricos.")

# Crear conjuntos de dígitos únicos por cada DNI
conjuntos = {}
for persona, dni in dnis.items():
    digitos = set(int(d) for d in str(dni))
    conjuntos[persona] = digitos

# Asignar a variables individuales
A = conjuntos["A"]
B = conjuntos["B"]
C = conjuntos["C"]
D = conjuntos["D"]
E = conjuntos["E"]

# Operaciones de conjunto
union_total = A | B | C | D | E
interseccion_total = A & B & C & D & E
diferencia_AE = A - E
simetrica_AE = A ^ E

# Conjuntos con alta diversidad (6 o más dígitos)
alta_diversidad = [nombre for nombre, conjunto in conjuntos.items() if len(conjunto) >= 6]

# Evaluar condición de combinación amplia
condicion_amplia = len(A) > len(B) and any(x % 2 != 0 for x in C)

# Verificar si hay un único dígito representativo
representativo = len(interseccion_total) == 1

# Mostrar resultados parte A
print("\n===== Parte A: resultados =====")
for nombre, conjunto in conjuntos.items():
    print(f"{nombre} = {conjunto}")

print("\nUnión total:", union_total)
print("Intersección total:", interseccion_total)
print("Diferencia A - E:", diferencia_AE)
print("Diferencia simétrica A △ E:", simetrica_AE)
print("Conjuntos con alta diversidad:", alta_diversidad)
print("¿Condición de combinación amplia?:", "Sí" if condicion_amplia else "No")
if representativo:
    print("Dígito representativo único:", list(interseccion_total)[0])
else:
    print("No hay un único dígito representativo.")

# Parte B: años de nacimiento (fijos por ahora)
nacimientos = {
    "A": 2003,
    "B": 2001,
    "C": 1999,
    "D": 2000,
    "E": 1998
}

anio_actual = datetime.now().year
grupo_z = []
bisiestos = []
pares = 0
impares = 0
cartesiano = []

for nombre, anio in nacimientos.items():
    if anio > 2000:
        grupo_z.append(nombre)
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        bisiestos.append(nombre)
    if anio % 2 == 0:
        pares += 1
    else:
        impares += 1
    edad = anio_actual - anio
    cartesiano.append((anio, edad))

# Mostrar resultados parte B
print("\n===== Parte B: años de nacimiento =====")
print("Integrantes en el Grupo Z:", grupo_z)
print("Integrantes nacidos en año bisiesto:", bisiestos)
print("Cantidad de años pares:", pares)
print("Cantidad de años impares:", impares)
print("Producto cartesiano (año, edad):", cartesiano)
