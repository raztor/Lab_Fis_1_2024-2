import matplotlib.pyplot as plt
import json
import os
from datetime import datetime
from scipy.signal import savgol_filter

# Load the data from the JSON file
with open('datos.JSON', 'r') as file:
    data = json.load(file)

# Create the output directory './graficos' if it does not exist
output_dir = './graficos'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Count existing files with the same title in the 'graficos' directory
title_sanitized = data['title'].replace(" ", "_")
existing_files = [f for f in os.listdir(output_dir) if f.startswith(title_sanitized) and f.endswith('.pdf')]
graph_number = len(existing_files) + 1

# Get current date and time
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generate the filename for the filtered graph
file_name_filtered = f"{data['title']} (Filtro Sav. Golay)|N°{graph_number}|{current_time}.pdf"
file_name_filtered = file_name_filtered.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")
file_path_filtered = os.path.join(output_dir, file_name_filtered)

# Number of subplots required (one for each line)
num_plots = len(data['lines'])

# Create a figure with a row of subplots for the filtered data
fig, axs = plt.subplots(1, num_plots, figsize=(5 * num_plots, 6))

# Plot each series in its subplot with Savitzky-Golay filter applied
for i, line in enumerate(data['lines']):
    ax = axs[i] if num_plots > 1 else axs  # Handle single subplot case
    y_filtered = savgol_filter(line['y'], window_length=11, polyorder=2)  # Adjust window_length and polyorder as needed
    ax.plot(line['x'], y_filtered, label=line['label'] + ' (filtered)', marker=line.get('marker', ''), linestyle=line.get('linestyle', '-'))
    ax.set_title(f"Filtered - {line['label']}")
    ax.set_xlabel(data['xlabel'])
    ax.set_ylabel(data['ylabel'])
    ax.legend(loc='best')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Save the filtered data figure as a PDF
plt.savefig(file_path_filtered, format='pdf')

# Show the figure with all subplots
plt.show()
