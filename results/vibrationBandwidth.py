import pandas as pd
import matplotlib.pyplot as plt

# Load the data from Excel
data = pd.read_excel("vibrationBandwidth.xlsx", sheet_name='Sheet1')

# Clean the data and rename columns for easier handling
data.columns = ['vibration type', 'GT', 'LLM', 'read/write']

# Fill NaN values in the 'vibration type' column by propagating the previous value forward
data['vibration type'].fillna(method='ffill', inplace=True)

# Group the data for plotting
grouped_data = data.groupby(['vibration type', 'read/write']).mean()

# Create a bar plot for ground truth and predicted bandwidth
fig, ax = plt.subplots(figsize=(15, 13))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create the bar plot with custom colors
ax = grouped_data[['GT', 'LLM']].plot(
    kind='bar',
    ax=ax,
    color=['chocolate', 'green'],
    width=0.60  # Reduce bar width
)

# Apply hatches to bars
hatch_styles = ['\/\/X', '*']  # Hatches for Ground Truth and Predicted (LLM)
for bars, hatch in zip(ax.containers, hatch_styles):
    for bar in bars:
        bar.set_hatch(hatch)

# Set custom x-axis labels
x_labels = ['parallel', 'parallel', 'vertical', 'vertical']
ax.set_xticklabels(x_labels, rotation=0, ha='center', fontsize=55)

# Reduce space between bars by adjusting the margin
ax.margins(x=0.05)  # Reduces the space between the bars

# Add custom text annotations to specify read and write
plt.text(0.16, 0.70, 'read', horizontalalignment='right', verticalalignment='top',
         transform=plt.gca().transAxes, color='darkorange', fontsize=50)

plt.text(0.42, 1.02, 'write', horizontalalignment='right', verticalalignment='top',
         transform=plt.gca().transAxes, color='green', fontsize=50)

plt.text(0.64, 0.46, 'read', horizontalalignment='right', verticalalignment='top',
         transform=plt.gca().transAxes, color='darkorange', fontsize=50)

plt.text(0.9, 0.70, 'write', horizontalalignment='right', verticalalignment='top',
         transform=plt.gca().transAxes, color='green', fontsize=50)

# Add labels and title
plt.xlabel('Vibration Type', fontweight='bold', fontsize=70)
plt.ylabel('Mean Bandwidth \n Degradation(%)', fontweight='bold', fontsize=70)
plt.gca().spines['bottom'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)
# Customize the legend
legend = ax.legend(
    title_fontsize=10,
    fontsize=8,
    loc='upper right',  # Place the legend inside the plot
    ncol=1,  # Single column legend
    bbox_to_anchor=(1, 1),  # Adjust legend position inside the plot
    prop={'size':50}
    # edgecolor='black'  # Add border to the legend box
)

# Tighten the layout and show the plot
plt.tight_layout()

plt.savefig('plots/vibrationbandwidthF.png', dpi=300)
plt.show()
