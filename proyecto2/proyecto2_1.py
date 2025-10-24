import pandas as pd

# Datos de ventas por vendedor
ventas = {
    'Vendedor': ['Ana', 'Luis', 'Ana', 'Carlos', 'Luis', 'Sofía'],
    'Mes': ['Ene', 'Ene', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Ventas': [1200, 1500, 1300, 1100, 1600, 1700]
}

df = pd.DataFrame(ventas)

# Agrupar por vendedor y calcular promedio de ventas
promedios = df.groupby('Vendedor')['Ventas'].mean()

print("Promedio de ventas por vendedor:")
print(promedios)
