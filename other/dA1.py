import pandas as pd
import numpy as np

# 1) Load the parallel-vibration dataset
df = pd.read_excel('Parallel_Vibrations.xlsx')

# 2) (Optional) confirm your column names
print("Columns in sheet:", df.columns.tolist())
# Expect: ['impact type', 'percentile', 'read', 'write']

# 3) Specify which columns to augment
gt_cols = ['read', 'write']

# 4) How many synthetic samples per row, and noise level
n_aug = 5
noise_scale = 0.05  # 5% Gaussian noise

# 5) Build augmented rows
aug_rows = []
for _, row in df.iterrows():
    for _ in range(n_aug):
        new_row = row.copy()
        # apply independent noise to each gt_col
        noise = np.random.normal(loc=1.0, scale=noise_scale, size=len(gt_cols))
        new_row[gt_cols] = row[gt_cols] * noise
        aug_rows.append(new_row)

# 6) Concatenate originals + augmentations
aug_df = pd.DataFrame(aug_rows)
augmented_df = pd.concat([df, aug_df], ignore_index=True)

# 7) Save out
out_path = 'parallel_vibrations_data_points.xlsx'
augmented_df.to_excel(out_path, index=False)

