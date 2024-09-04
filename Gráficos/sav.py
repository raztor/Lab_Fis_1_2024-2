import matplotlib.pyplot as plt
import json
import os
from datetime import datetime
from scipy.signal import savgol_filter

# Cargar los datos desde el archivo JSON
with open('config/datos.JSON', 'r') as file:
    data = json.load(file)

# Crear la figura
plt.figure(figsize=(8, 6))

# Configurar título y etiquetas para el gráfico original
plt.title(data['title'])
plt.xlabel(data['xlabel'])
plt.ylabel(data['ylabel'])

# Graficar cada línea en los datos originales
for line in data['lines']:
    plt.plot(line['x'], line['y'], label=line['label'], marker=line.get('marker', ''), linestyle=line.get('linestyle', '-'))

# Mostrar la leyenda
plt.legend(loc='best')

# Crear la carpeta './graficos' si no existe
output_dir = 'imagenes'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Contar archivos existentes con el mismo título en la carpeta 'graficos'
title_sanitized = data['title'].replace(" ", "_")
existing_files = [f for f in os.listdir(output_dir) if f.startswith(title_sanitized) and f.endswith('.pdf')]
graph_number = len(existing_files) + 1

# Obtener la fecha y hora actual
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generar el nombre del archivo para el gráfico original
file_name_original = f"{data['title']}|N°{graph_number}|{current_time}.pdf"

# Reemplazar caracteres no válidos en el nombre del archivo
file_name_original = file_name_original.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")

# Ruta completa del archivo para el gráfico original
file_path_original = os.path.join(output_dir, file_name_original)

# Guardar el gráfico original como PDF
plt.savefig(file_path_original, format='pdf')

# Mostrar el gráfico original
plt.show()

# Crear una nueva figura para el gráfico filtrado
plt.figure(figsize=(8, 6))

# Configurar título y etiquetas para el gráfico filtrado
plt.title(data['title'] + " (Filtro Sav. Golay)")
plt.xlabel(data['xlabel'])
plt.ylabel(data['ylabel'])

# Graficar cada línea en los datos con filtro Savitzky-Golay aplicado
for line in data['lines']:
    y_filtered = savgol_filter(line['y'], window_length=11, polyorder=2)  # Ajusta window_length y polyorder según sea necesario
    plt.plot(line['x'], y_filtered, label=line['label'] + ' (filtered)', marker=line.get('marker', ''), linestyle=line.get('linestyle', '-'))

# Mostrar la leyenda
plt.legend(loc='best')

# Generar el nombre del archivo para el gráfico filtrado
file_name_filtered = f"{data['title']} (Filtro Sav. Golay)|N°{graph_number}|{current_time}.pdf"

# Reemplazar caracteres no válidos en el nombre del archivo
file_name_filtered = file_name_filtered.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")

# Ruta completa del archivo para el gráfico filtrado
file_path_filtered = os.path.join(output_dir, file_name_filtered)

# Guardar el gráfico filtrado como PDF
plt.savefig(file_path_filtered, format='pdf')

# Mostrar el gráfico filtrado
plt.show()

