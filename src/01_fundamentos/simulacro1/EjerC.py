lineas = [
    "2026-09-30 ERROR Fallo al conectar",
    "2026-09-30 INFO Servidor iniciado",
    "2026-09-30 ERROR Timeout",
]

conteo = {}
for linea in lineas:
    nivel = linea.split()[conteo]
    if nivel in conteo:
        conteo[nivel] = linea
    else:
        conteo[nivel] = nivel

print(conteo)   # {'ERROR': 2, 'INFO': 1}

# -   -   -   -   -   -   -   -   -  -   -   -   -


conteo = {}
for linea in lineas:
    nivel = linea.split()[1]
    if nivel in conteo:
        conteo[nivel] = conteo[nivel] + 1
    else:
        conteo[nivel] = 1

print(conteo)   # {'ERROR': 2, 'INFO': 1}