import pandas as pd


input_file = "dataset/plank_dataset.csv"
output_file = "dataset/plank_dataset_with_header.csv"


# Read existing dataset
# header=None is important because first row is actual data
df = pd.read_csv(input_file, header=None)


# Create column names
columns = []
for i in range(33):
    columns.append(f"landmark{i}_x")
    columns.append(f"landmark{i}_y")
    columns.append(f"landmark{i}_z")
columns.append("angle")
columns.append("label")


# Assign header
df.columns = columns


# Save corrected dataset
df.to_csv(output_file, index=False)


print("Header added successfully")
print("Shape:", df.shape)
print("Saved to:", output_file)
