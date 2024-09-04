import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

# Load data from JSON file
with open('config/datos.JSON', 'r') as file:
    data = json.load(file)

# Create the output directory './graficos' if it does not exist
output_dir = 'imagenes'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Calculate the number of subplots needed (one per line)
num_plots = len(data['lines'])

# Create a figure with a grid of subplots (1 row, num_plots columns)
fig, axs = plt.subplots(1, num_plots, figsize=(4 * num_plots, 6))

# Loop through each series in the data and create a subplot for each
for i, line in enumerate(data['lines']):
    ax = axs[i] if num_plots > 1 else axs  # Handle single subplot case
    ax.plot(line['x'], line['y'], label=line['label'], marker=line.get('marker', ''), linestyle=line.get('linestyle', '-'))
    ax.set_title(line.get('label', 'Graph ' + str(i+1)))
    ax.set_xlabel(data['xlabel'])
    ax.set_ylabel(data['ylabel'])
    ax.legend(loc='best')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Count existing files with the same title in the 'graficos' directory
title_sanitized = data['title'].replace(" ", "_")
existing_files = [f for f in os.listdir(output_dir) if f.startswith(title_sanitized) and f.endswith('.pdf')]
graph_number = len(existing_files) + 1

# Get current date and time
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generate the filename
file_name = f"{data['title']}|N°{graph_number}|{current_time}.pdf"

# Replace invalid characters in the filename
file_name = file_name.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")

# Full path for the file
file_path = os.path.join(output_dir, file_name)

# Save the figure as a PDF
plt.savefig(file_path, format='pdf')

# Show the figure with all subplots
plt.show()
