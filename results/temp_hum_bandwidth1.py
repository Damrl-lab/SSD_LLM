# Corrected data as per user input
import matplotlib.pyplot as plt
import numpy as np



group_names = ['50°C', '60°C', '50°C', '60°C']
group_names1 = ['TLC', 'TLC', 'MLC', 'MLC']
gt_values = [45, 60, 2, 3]
pred_values = [50, 55, 4, 3]

x = np.arange(len(group_names))  # Positions for groups
bar_width = 0.30

# Plotting
fig, ax = plt.subplots(figsize=(5, 5), dpi=400)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# GT Bars
ax.bar(x - bar_width/2, gt_values, width=bar_width, label='GT', hatch='**', color='chocolate')

# Prediction Bars
ax.bar(x + bar_width/2, pred_values, width=bar_width, label='LLM', hatch='\/\/\/X', color='green')
# Adding labels below the bars
for i in range(len(group_names)):
    ax.text(x[i], -9, f'{group_names1[i]}', ha='center', fontsize=20)

# Labels and title
ax.set_xlabel('Temperature', fontweight='bold', labelpad=20, fontsize=20)
ax.set_ylabel('Avg. Bandwidth \nChange (%)', fontweight='bold', fontsize=20)

ax.set_xticks(x)
ax.set_xticklabels(group_names, rotation=0, ha='right', fontsize=15)
ax.legend(fontsize=16)

# Display plot
plt.tight_layout()

# plt.savefig('plotsNew/temp_bandwidth1F.png')

plt.show()