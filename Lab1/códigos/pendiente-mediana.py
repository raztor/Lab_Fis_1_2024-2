import json
import pandas as pd
import numpy as np

# Load the JSON file
with open('datos.JSON', 'r', encoding="UTF-8") as file:
    data = json.load(file)

# List to store slopes for each angle
angle_slopes = []

# Calculate slopes for each subplot
for subplot in data['subplots']:
    title = subplot['title']
    slopes = []
    for line in subplot['lines']:
        x = np.array(line['x'])
        y = np.array(line['y'])
        if len(x) > 1 and len(y) > 1:
            slope, _ = np.polyfit(x, y, 1)
            slopes.append(slope)

    # Calculate median slope for the subplot (angle)
    if slopes:
        median_slope = np.median(slopes)
        angle_slopes.append((title, median_slope))

# Convert to DataFrame for better visualization
slopes_df = pd.DataFrame(angle_slopes, columns=['Angulo', 'Pendiente Mediana'])

print(slopes_df)
