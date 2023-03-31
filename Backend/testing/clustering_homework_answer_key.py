import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import interpolate
from sklearn.cluster import KMeans

file_path = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444_small.xlsx"
sheet_name = "Test 1"
use_cols = "A:C"
hard_col_name = "HARDNESS"
x_col_name = "X Position"
y_col_name = "Y Position"
NUM_HIST_BINS = 200
nulls = False


xls = pd.ExcelFile(file_path)

if nulls:
    test1_sheet = pd.read_excel(xls, sheet_name, usecols=use_cols).iloc[:-1]
else:
    test1_sheet = pd.read_excel(xls, sheet_name, usecols=use_cols).dropna()

print(test1_sheet)


# If skip_first_row then read every row after the first, otherwise read them all
# The hardness values
hardness_column = test1_sheet[hard_col_name]
# The x values
x_column = test1_sheet[x_col_name]
# The y values
y_column = test1_sheet[y_col_name]
# The stiffness column
# Asserts that the columns have values
assert hardness_column is not None
assert x_column is not None
assert y_column is not None

hard_df = pd.DataFrame(hardness_column)
x_df = pd.DataFrame(x_column)
y_df = pd.DataFrame(y_column)

# Renames columns of all read data for consistency
hard_df = hard_df.rename(columns={hard_col_name: "Data"})
x_df = x_df.rename(columns={x_col_name: "Data"})
y_df = y_df.rename(columns={y_col_name: "Data"})

# Makes all read data numeric
hard_df["Data"] = pd.to_numeric(hard_df["Data"], downcast="float")
x_df["Data"] = pd.to_numeric(x_df["Data"], downcast="float")
y_df["Data"] = pd.to_numeric(y_df["Data"], downcast="float")
print("\nBelow are the hardness values... ")
print(hard_df)
print("\nBelow are the x values... ")
print(x_df)
print("\nBelow are the y values... ")
print(y_df)

r = random.random()
b = random.random()
g = random.random()
color = (r, g, b)

plt.hist(x_df["Data"].values, bins=NUM_HIST_BINS, color=color)  # "darkgoldenrod"
plt.title("X Values vs Number of Occurrences")
plt.xlabel("X Values")
plt.ylabel("Number of Occurrences")
plt.show()

r = random.random()
b = random.random()
g = random.random()
color = (r, g, b)

plt.hist(y_df["Data"].values, bins=NUM_HIST_BINS, color=color)  # "forestgreen"
plt.title("Y Values vs Number of Occurrences")
plt.xlabel("Y Values")
plt.ylabel("Number of Occurrences")
plt.show()

r = random.random()
b = random.random()
g = random.random()
color = (r, g, b)

plt.hist(hard_df["Data"].values, bins=100, color=color)  # "darkred"
plt.title("Hardness Values vs Number of Occurrences")
plt.xlabel("Hardness Values")
plt.ylabel("Number of Occurrences")
plt.show()

array = hard_df.copy()["Data"].values

# Remove outliers
mean_val = np.mean(array)
stddev_val = np.std(array)
z_scores = 3
# print("Mean value is " + str(mean_val))
# print("Stddev value is " + str(stddev_val))
array[abs(array - mean_val) > stddev_val * z_scores] = np.nan

array = array.reshape(len(np.unique(x_df)), len(np.unique(y_df)))

x = np.arange(0, array.shape[1])
y = np.arange(0, array.shape[0])
# mask invalid values
array = np.ma.masked_invalid(array)
xx, yy = np.meshgrid(x, y)
# get only the valid values
x1 = xx[~array.mask]
y1 = yy[~array.mask]
newarr = array[~array.mask]

grid1 = interpolate.griddata((x1, y1), newarr.ravel(), (xx, yy), method='cubic')

# print(grid1)
plt.imshow(grid1, interpolation='nearest')
plt.show()

x = np.arange(0, grid1.shape[1])
y = np.arange(0, grid1.shape[0])
# mask invalid values
grid1 = np.ma.masked_invalid(grid1)
xx, yy = np.meshgrid(x, y)
# get only the valid values
x1 = xx[~grid1.mask]
y1 = yy[~grid1.mask]
newarr = grid1[~grid1.mask]

grid2 = interpolate.griddata((x1, y1), newarr.ravel(), (xx, yy), method='nearest')

# print(grid2)
plt.imshow(grid2, interpolation='nearest')
plt.show()

input_data = grid2.reshape(-1, 1)

hard_df = pd.DataFrame(input_data, columns=["Data"])

r = random.random()
b = random.random()
g = random.random()
color = (r, g, b)

plt.hist(hard_df["Data"].values, bins=100, color=color)  # "darkred"
plt.title("Cleaned Hardness Values vs Number of Occurrences")
plt.xlabel("Hardness Values")
plt.ylabel("Number of Occurrences")
plt.show()

k_means = KMeans(n_clusters=3, random_state=0).fit(hard_df.copy()["Data"].values.reshape(-1, 1))

k_means_results = k_means.labels_
clustered_df = pd.DataFrame(k_means_results)
clustered_df.columns = ["Data"]

num_clusters = len(np.unique(hard_df))
if num_clusters > 20:
    num_clusters = 20
x_values = np.unique(x_df["Data"].values)
y_values = np.unique(y_df["Data"].values)
grid_size_x = int(x_values.size)
grid_size_y = int(y_values.size)
z_values = np.rot90(hard_df["Data"].values.reshape(grid_size_x, grid_size_y))

fig, ax = plt.subplots(figsize=(10, 10))

ax.set_aspect('equal')
# Plots contour plot
cf = ax.contourf(x_values, y_values, z_values, num_clusters - 1, cmap="YlGn")
# Plots color bar
cb = fig.colorbar(cf, ax=ax)
# Labels being set
cb.set_label("Raw Hardness Values (GPA)")
plt.title("Hardness Raw Data VS Coordinate")
plt.xlabel("X Values (um)")
plt.ylabel("Y Values (um)")

plt.show()

num_clusters = len(np.unique(clustered_df))
if num_clusters > 20:
    num_clusters = 20
x_values = np.unique(x_df["Data"].values)
y_values = np.unique(y_df["Data"].values)
grid_size_x = int(x_values.size)
grid_size_y = int(y_values.size)
z_values = np.rot90(clustered_df["Data"].values.reshape(grid_size_x, grid_size_y))

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_aspect('equal')
# Plots contour plot
cf = ax.contourf(x_values, y_values, z_values, num_clusters - 1)
# Plots color bar
cb = fig.colorbar(cf, ax=ax)
# Labels being set
cb.set_label("Clustered Hardness Values (GPA)")
plt.title("Hardness Clustered Data VS Coordinate for " + str(num_clusters) + " Clusters")
plt.xlabel("X Values (um)")
plt.ylabel("Y Values (um)")

plt.show()

res_list = clustered_df["Data"].tolist()
cluster_fractions = []
cluster_num = []
unique_cluster_values = np.unique(clustered_df)
for i in unique_cluster_values:
    fraction = float(res_list.count(i)) / float(len(res_list))
    cluster_fractions.append(fraction)
    cluster_num.append(i + 1)
plt.bar(cluster_num, height=cluster_fractions, width=0.4)
plt.title("Distribution of Hardness Data After Clustering into " + str(len(cluster_num)) + " Clusters")
plt.xlabel("Cluster (" + str(len(cluster_num)) + " Clusters)")
plt.ylabel("Percentage of Data Contained Within Cluster")
plt.show()

exit(0)
