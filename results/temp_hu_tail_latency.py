# Correcting and implementing editable subplot titles

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the Excel file
file_path = 'results_data/temp_hu_tail_latency.xlsx'  # Replace with the correct file path
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Clean the data and assign experiments
data['Experiment'] = data['Temperature and Humidity Conditions'].ffill().astype(int)

# Number of experiments
experiments = data['Experiment'].unique()
num_experiments = len(experiments)

# Example custom titles for subplots (editable)
custom_titles = [
    "Temperature: 22.5-22.5 to 60-60\u00B0C\nHumidity: 50%-20% to 80%-50%RH",
    "Temperature: 60\u00B0C\nHumidity: 80%-50%RH",
    "Temperature: 60\u00B0C\nHumidity: 20%-50%RH",
    "Temperature: 60-60-60\u00B0C\nHumidity: 50%-80%-50%RH",
    "Temperature: 22.5-50-22.5\u00B0C\nHumidity: 50%-50%-50%RH"
]

# Example additional labels for below the x-axis

additional_labels = [

    "(I) Running: Positive",

    "(II) Running Positive",

    "(III) Running: Negative",

    "(IV) Post: Negative",

    "(V) Post: Negative"

]

# Custom colors for ground truth and prediction

custom_colors = {

    "ground_truth": "blue",  # Change this color string as needed

    "prediction": "green"  # Change this color string as needed

}

# Set up subplots

fig, axes = plt.subplots(1, num_experiments, figsize=(15, 4), sharey=True)

# Define x-tick labels

custom_xticks = [99, 99.9, 99.99, 99.999, 99.9999]

for i, experiment in enumerate(experiments):

    # Filter data for the current experiment and clean missing values

    experiment_data = data[data['Experiment'] == experiment].dropna(subset=["Ground Truth", "Prediction (LLM)"])

    x = np.linspace(0, len(custom_xticks) - 1, len(experiment_data))

    ax = axes[i]

    # Plot Ground Truth with customizable color and markers

    ax.plot(

        x,

        experiment_data["Ground Truth"],

        color=custom_colors["ground_truth"],

        marker='o',

        markersize=5,

        linestyle='-',

        label='Ground Truth',
        linewidth=3

    )

    # Plot Prediction (LLM) with customizable color and markers

    ax.plot(

        x,

        experiment_data["Prediction (LLM)"],

        color=custom_colors["prediction"],

        marker='x',

        markersize=5,

        linestyle=(0, (1, 1)),

        label='Prediction',
        linewidth=3

    )

    # Set x-ticks and labels

    ax.set_xticks(np.linspace(0, len(custom_xticks) - 1, len(custom_xticks)))

    ax.set_xticklabels(custom_xticks, rotation=0, fontsize=10)

    # Set custom title for each subplot

    ax.set_title(custom_titles[i], fontsize=13)

    # Add an additional label below the x-axis for each subplot

    ax.set_xlabel(additional_labels[i], fontsize=16)

    # Add legend for each subplot

    ax.legend(fontsize=15)

    # Set grid and labels for the first subplot

    if i == 0:
        ax.set_ylabel('Performance (%)', fontweight='bold', fontsize=18)

    ax.grid(True, axis='y')

# Set a shared xlabel for all subplots

fig.text(0.5, 0.02, 'Tail Latency Percentile', ha='center', fontweight='bold', fontsize=18)

# Adjust layout

plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Add a title for the entire figure

# fig.suptitle('Ground Truth vs Prediction (LLM) for Experiments', fontsize=14, fontweight='bold')
# plt.savefig('temp_tail_latencyTH.png')
# Display the plot

plt.show()
