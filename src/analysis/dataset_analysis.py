import pandas as pd 
df = pd.read_csv("dataset/plank_dataset.csv")
# check dimension 
print(df.shape) # o/p -->(927,101)

#colomn verification
print(df.columns.tolist())

# check null values
print(df.isnull().sum().sum()) # o/p --> 0 null values

# class distribution
print(df["label"].value_counts())

# calculate mean , min , max , standard deviation per group
grouped_stats = df.groupby("label")["angle"].agg(['mean','max','min','std'])
print(grouped_stats)
