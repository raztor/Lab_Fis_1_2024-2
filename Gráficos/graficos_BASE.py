import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

# Cargar los datos desde el archivo JSON
with open('config/datos.JSON', 'r') as file:
    data = json.load(file)

# Crear la figura
plt.figure(figsize=(8, 6))

# Configurar título y etiquetas
plt.title(data['title'])
plt.xlabel(data['xlabel'])
plt.ylabel(data['ylabel'])

# Graficar cada línea en los datos
for line in data['lines']:
    plt.plot(line['x'], line['y'], label=line['label'], marker=line.get('marker', ''), linestyle=line.get('linestyle', '-'))

# Mostrar la leyenda
plt.legend(loc='best')

# Contar archivos existentes con el mismo título en la carpeta actual
title_sanitized = data['title'].replace(" ", "_")
existing_files = [f for f in os.listdir() if f.startswith(title_sanitized) and f.endswith('.pdf')]
graph_number = len(existing_files) + 1

# Obtener la fecha y hora actual
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generar el nombre del archivo
file_name = f"{data['title']}|N°{graph_number}|{current_time}.pdf"

# Reemplazar caracteres no válidos en el nombre del archivo
file_name = file_name.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")

# Guardar el gráfico como PDF
plt.savefig(file_name, format='pdf')

# Mostrar el gráfico
plt.show()
