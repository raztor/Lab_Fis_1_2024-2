import matplotlib.pyplot as plt
import json
import os
from datetime import datetime
from scipy.signal import savgol_filter

# Load the data from the JSON file
with open('config/subplot.JSON', 'r') as file:
    data = json.load(file)

# Create the output directory './graficos' if it does not exist
output_dir = 'imagenes'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Count existing files with the same title in the 'graficos' directory
title_sanitized = "Filtered_Graphs"  # New title for overall plot series
existing_files = [f for f in os.listdir(output_dir) if f.startswith(title_sanitized) and f.endswith('.pdf')]
graph_number = len(existing_files) + 1

# Get current date and time
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generate the filename for the filtered graph
file_name_filtered = f"{title_sanitized}|N°{graph_number}|{current_time}.pdf"
file_name_filtered = file_name_filtered.replace(":", "-").replace("/", "-").replace("\\", "-").replace("|", "-")
file_path_filtered = os.path.join(output_dir, file_name_filtered)

# Number of subplots required (one for each subplot in the JSON)
num_subplots = len(data['subplots'])

# Create a figure with subplots for the filtered data
fig, axs = plt.subplots(1, num_subplots, figsize=(5 * num_subplots, 6))

# Ensure axs is iterable (handle single subplot case)
if num_subplots == 1:
    axs = [axs]

# Plot each subplot's lines
for i, subplot in enumerate(data['subplots']):
    ax = axs[i]
    ax.set_title(subplot.get('title', f'Subplot {i + 1}'))
    ax.set_xlabel(data['xlabel'])
    ax.set_ylabel(data['ylabel'])

    # Plot each line in the subplot with Savitzky-Golay filter applied
    for line in subplot['lines']:
        if line['x'] and line['y']:  # Ensure there is data to plot
            # Determine window_length dynamically
            y_length = len(line['y'])
            window_length = min(11, y_length) if y_length % 2 != 0 else min(11, y_length - 1)
            if window_length >= 3:  # Savitzky-Golay filter requires at least window length of 3
                y_filtered = savgol_filter(line['y'], window_length=window_length,
                                           polyorder=2)  # Adjust polyorder as needed
                ax.plot(line['x'], y_filtered, label=line['label'] + ' (filtered)', marker=line.get('marker', ''),
                        linestyle=line.get('linestyle', '-'))

    ax.legend(loc='best')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Save the filtered data figure as a PDF
plt.savefig(file_path_filtered, format='pdf')

# Show the figure with all subplots
plt.show()
