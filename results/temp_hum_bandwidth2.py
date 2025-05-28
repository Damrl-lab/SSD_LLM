import matplotlib.pyplot as plt

# Data for box plots
data = {
    "GT": [-65, -62, -55, -50, -40],          # Minimum, Q1, Median, Q3, Maximum for GT
    "Prediction": [-62, -60, -45, -45, -40]   # Minimum, Q1, Median, Q3, Maximum for Prediction
}

# Prepare the data for plotting
box_data = [data["GT"], data["Prediction"]]

fig, ax = plt.subplots(figsize=(5, 6), dpi=400)
ax.boxplot(box_data, patch_artist=True, vert=False)

# Customize the y-tick labels
ax.set_yticklabels(labels=['GT', 'LLM'], rotation=0, ha='center', fontweight='bold', fontsize=20)

# Customize the x-tick font size
ax.tick_params(axis='x', labelsize=15)  # Increase font size for x-ticks

# Remove unnecessary spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Labels and title
ax.set_xlabel('Change in Bandwidth (%)', fontweight='bold', fontsize=20)

# Add a grid
plt.grid(axis='x', linestyle='--', alpha=0.3)

# Save and display the plot
# plt.savefig('plotsNew/temp_bandwidth2F.png')
plt.show()
