import pandas as pd
import numpy as np

first_values = [1, 2, 3, 3, 1, 3, 3, 2]
second_values = [5, 4, -1, 0, 8, 0, -2, 2]

df = pd.DataFrame()
df["Data"] = second_values
df["Cluster"] = first_values

print("\nUnsorted:")
print(df)

# https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
# df = df.sort_values("Data")
print("\nSorted:")
print(df)

num_clusters = len(np.unique(df["Cluster"].values))
num_values = len(df["Cluster"].values)
cluster_representations = pd.DataFrame()
for i in range(num_clusters + 1):
    for j in range(num_values):
        cluster_value = df["Cluster"].values[j]
        if cluster_value == i:
            data_value = df["Data"].values[j]
            cluster_representations = cluster_representations.append(
                pd.DataFrame({"Data": [data_value], "Cluster": [i]}))
            break

print("\nElement from each cluster")
print(cluster_representations)

print("\nElement from each cluster sorted")
cluster_representations = cluster_representations.sort_values("Data")
print(cluster_representations)

transformation_dictionary = {}
for i in range(num_clusters):
    cluster_value = cluster_representations["Cluster"].values[i]
    transformation_dictionary[cluster_value] = i

print(transformation_dictionary)


def transformation_function(orig_cluster):
    # try:
    return transformation_dictionary[orig_cluster]
    # except Exception:
    #     return orig_cluster


# https://stackoverflow.com/questions/43520238/transform-dictionary-python
print(df)
df_new = pd.DataFrame({"Cluster": df["Cluster"].copy().values})
# df_new = [df_new["Clustered"] for item in df_new["Clustered"]]
print(df_new)
df_new = df_new.applymap(transformation_function)
print(df_new)
df_new["Data"] = df["Data"].copy().values

print("\nThe transformed original data is:")
print(df_new)

exit(0)
