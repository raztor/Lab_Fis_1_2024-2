import numpy as np
import pandas as pd

# Parámetros iniciales
v0 = 0  # Velocidad inicial en m/s (supuesto de que el objeto empieza desde el reposo)
theta = 14  # Ángulo de pendiente en grados
g = 9.81  # Gravedad en m/s^2
T_total = 2  # Tiempo total en segundos
mediciones_por_segundo = 10  # Número de mediciones por segundo

# Convertir ángulo a radianes
theta_rad = np.radians(theta)

# Aceleración en la dirección del plano inclinado
a = g * np.sin(theta_rad)

# Crear array de tiempos con 5 mediciones por cada segundo hasta 3 segundos
t = np.linspace(0, T_total, T_total * mediciones_por_segundo)

# Velocidad en función del tiempo para un objeto en pendiente sin roce
v = v0 + a * t

# Crear DataFrame con los resultados
df = pd.DataFrame({'Tiempo (s)': t, 'Velocidad (m/s)': v})

# Mostrar el DataFrame
print(df)