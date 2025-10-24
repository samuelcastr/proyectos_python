import pandas as pd

# Crear un DataFrame con datos de estudiantes
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofía', 'María'],
    'Edad': [23, 31, 19, 27, 22],
    'Nota': [4.5, 3.8, 5.0, 2.9, 4.2]
}

df = pd.DataFrame(datos)

# Filtrar estudiantes con nota mayor a 4.0
destacados = df[df['Nota'] > 4.0]

# Ordenar por nota descendente
ordenados = destacados.sort_values(by='Nota', ascending=False)

print("Estudiantes destacados:")
print(ordenados)
