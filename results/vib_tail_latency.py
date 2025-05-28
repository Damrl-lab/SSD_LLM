import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the provided data
file_path = 'results_data/vib_tail_latency.xlsx'  # Replace with the correct file path
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Data preparation and cleaning
# Forward fill missing values to ensure all rows have data for operation type (read/write)
data['read/write'] = data['read/write'].ffill()

# Separate data into read and write operations
read_data = data[data['read/write'] == 'read']
write_data = data[data['read/write'] == 'write']

# Generate x-axis based on the index of the data points
x_read = np.arange(len(read_data))
x_write = np.arange(len(write_data))

# Define custom x-ticks and y-ticks
custom_xticks = [99, 99.9, 99.99, 99.999, 99.9999]

# Plot configuration
plt.figure(figsize=(6, 6), dpi=100)
# plt.gca().spines['bottom'].set_linewidth(4)  # X-axis
# plt.gca().spines['left'].set_linewidth(4)
# plt.gca().spines['right'].set_linewidth(4)
# plt.gca().spines['top'].set_linewidth(4)

# Plot read operations
plt.plot(
    x_read,
    read_data['ground truth\nparallel vibration'],
    color='slateblue',
    linestyle='-',
    marker='o',
    label='Read Ground Truth',
linewidth=3
)
plt.plot(
    x_read,
    read_data['LLM\nparallel vibration'],
    color='slateblue',
    linestyle='--',
    marker='o',
    label='Read Prediction',
linewidth=3
)

# Plot write operations
plt.plot(
    x_write,
    write_data['ground truth\nparallel vibration'],
    color='darkorange',
    linestyle='-',
    marker='x',
    label='Write Ground Truth',
linewidth=3

)
plt.plot(
    x_write,
    write_data['LLM\nparallel vibration'],
    color='darkorange',
    linestyle='--',
    marker='x',
    label='Write Prediction',
linewidth=3
)

# Add labels, title, and legend

plt.xlabel('Tail Latency Percentile', fontsize=12)
plt.ylabel('Read/Write Impact', fontsize=12)

# Set custom x-ticks
plt.xticks(np.linspace(0, len(custom_xticks) - 1, len(custom_xticks)), custom_xticks, fontsize=12)

# Set y-axis limit and ticks
plt.ylim(0, 40)
plt.yticks(np.arange(0, 41, 5), fontsize=12)

# Add grid and legend
plt.grid(axis='y', linestyle='--', alpha=0.9)
# plt.legend(fontsize=35)
plt.legend(ncol=1, prop={'size': 12}, frameon=True)

# Adjust layout and display the plot
#parallel_short term running
# plt.savefig('vibrations/parallel_short term running.png')
plt.tight_layout()
plt.show()
