import pandas as pd
import numpy as np

# 1) Load your data
df = pd.read_excel('Temprature HumidityTailLate.xlsx')

# 2) Specify the exact ground-truth column name
gt_col = 'Ground Truth'

# 3) How many augmentations per row, and how much noise
n_aug = 5
noise_scale = 0.05  # 5% stddev

# 4) Build the augmented rows
aug_rows = []
for _, row in df.iterrows():
    for _ in range(n_aug):
        new_row = row.copy()
        # multiply the GT value by x ~ N(1, noise_scale)
        new_row[gt_col] = row[gt_col] * np.random.normal(loc=1.0, scale=noise_scale)
        aug_rows.append(new_row)

# 5) Concatenate originals + augmentations
aug_df = pd.DataFrame(aug_rows)
augmented_df = pd.concat([df, aug_df], ignore_index=True)

# 6) Save out
augmented_df.to_excel('temp_hum_tail_latency_data_points.xlsx', index=False)
