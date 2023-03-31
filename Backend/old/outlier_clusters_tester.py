import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import interpolate
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import adjusted_rand_score
from helpers import ClusteringHelper

file_path = "../data/Bulk WAAM of Puck 1.xlsx"
# file_path = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444_small.xlsx"
sheet_name = "Test 1"
use_cols = "B:I"
hard_col_name = "HARDNESS"
x_col_name = "X Position"
y_col_name = "Y Position"
NUM_HIST_BINS = 200
nulls = True
skip_first_row = True

xls = pd.ExcelFile(file_path)

if nulls:
    test1_sheet = pd.read_excel(xls, sheet_name, usecols=use_cols)
else:
    test1_sheet = pd.read_excel(xls, sheet_name, usecols=use_cols).iloc[:-1].dropna()

print(test1_sheet)

# If skip_first_row then read every row after the first, otherwise read them all
if skip_first_row:
    # Remove the first row from every area due to it being a units label
    # The hardness values
    hardness_column = test1_sheet[hard_col_name].iloc[1:]
    # The x values
    x_column = test1_sheet[x_col_name].iloc[1:]
    # The y values
    y_column = test1_sheet[y_col_name].iloc[1:]
else:
    # The hardness values
    hardness_column = test1_sheet[hard_col_name].iloc[:]
    # The x values
    x_column = test1_sheet[x_col_name].iloc[:]
    # The y values
    y_column = test1_sheet[y_col_name].iloc[:]
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
# print("\nBelow are the hardness values... ")
# print(hard_df)
# print("\nBelow are the x values... ")
# print(x_df)
# print("\nBelow are the y values... ")
# print(y_df)

# r = random.random()
# b = random.random()
# g = random.random()
# color = (r, g, b)
#
# plt.hist(x_df["Data"].values, bins=NUM_HIST_BINS, color=color)  # "darkgoldenrod"
# plt.title("X Values vs Number of Occurrences")
# plt.xlabel("X Values")
# plt.ylabel("Number of Occurrences")
# plt.show()
#
# r = random.random()
# b = random.random()
# g = random.random()
# color = (r, g, b)
#
# plt.hist(y_df["Data"].values, bins=NUM_HIST_BINS, color=color)  # "forestgreen"
# plt.title("Y Values vs Number of Occurrences")
# plt.xlabel("Y Values")
# plt.ylabel("Number of Occurrences")
# plt.show()

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

# mean_val = np.mean(array)
# stddev_val = np.std(array)
# z_scores = 3
# # print("Mean value is " + str(mean_val))
# # print("Stddev value is " + str(stddev_val))
# array[abs(array - mean_val) > stddev_val * z_scores] = np.nan

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

# TODO This is different
# Remove outliers

cleaned_data = hard_df["Data"]

mean_val = np.mean(cleaned_data)
stddev_val = np.std(cleaned_data)
z_scores = 3
print("Mean value is " + str(mean_val))
print("Stddev value is " + str(stddev_val))
# cleaned_data[abs(cleaned_data - mean_val) > stddev_val * z_scores] = np.nan

print("Printing cleaned data...")
print(cleaned_data)

outliers_below = cleaned_data[cleaned_data - mean_val < -1 * stddev_val * z_scores]
outliers_below = pd.DataFrame(outliers_below)
# outliers_below = outliers_below.rename(columns=["Data"])
outliers_above = cleaned_data[cleaned_data - mean_val > stddev_val * z_scores]
outliers_above = pd.DataFrame(outliers_above)
no_outliers = cleaned_data[abs(cleaned_data - mean_val) <= stddev_val * z_scores]

num_outliers_below = len(outliers_below)
num_outliers_above = len(outliers_above)
num_non_outliers = len(no_outliers)
print("Below: \n" + str(outliers_below))
print("Above: \n" + str(outliers_above))
print("Non outliers: \n" + str(no_outliers))

print("Outliers below -3 Z Score: " + str(num_outliers_below))
print("Outliers above +3 Z Score: " + str(num_outliers_above))
print("Non outliers: " + str(num_non_outliers))

outliers_below_exist = num_outliers_below > 0
outliers_above_exist = num_outliers_above > 0

print("Outliers below: " + str(outliers_below_exist))
print("Outliers above: " + str(outliers_above_exist))

hard_df_no_outliers = pd.DataFrame()
hard_df_no_outliers["Data"] = no_outliers

k_means = KMeans(n_clusters=3, random_state=0).fit(hard_df_no_outliers.copy()["Data"].values.reshape(-1, 1))

k_means_results = k_means.labels_
clustered_df = pd.DataFrame(k_means_results)
clustered_df.columns = ["Data"]
clustered_df = ClusteringHelper.order_clusters(hard_df_no_outliers.copy(), clustered_data_df=clustered_df.copy())

cluster_values = np.unique(clustered_df["Data"].values)
new_outlier_below_data = np.full(shape=num_outliers_below, fill_value=min(cluster_values) - 1)
print("Below outlier cluster list")
print(new_outlier_below_data)
print("Size")
print(len(new_outlier_below_data))
outliers_below["Data"] = new_outlier_below_data

outliers_above["Data"] = np.full(shape=num_outliers_above, fill_value=max(cluster_values) + 1)

print("Index")
no_outliers_index = hard_df_no_outliers.index
print(no_outliers_index)
# combined_clustered_initial = pd.DataFrame()
# # combined_clustered_initial = pd.DataFrame([], columns=["Data", "Clustered"])
# combined_clustered_initial["Data"] = hard_df_no_outliers["Data"]
# # combined_clustered_initial.insert(clustered_df["Data"])
# combined_clustered_initial["Clustered"].insert(clustered_df["Data"], ignore_index=True)
# print("Combined Clusters Initial")
# print(combined_clustered_initial)

combined_clusters = pd.DataFrame(clustered_df["Data"].values, index=no_outliers_index, columns=["Data"])
combined_clusters = combined_clusters.append(outliers_below)
combined_clusters = combined_clusters.append(outliers_above)
combined_clusters = combined_clusters.sort_index()
# combined_clusters.set_index(no_outliers_index)
# combined_clusters = combined_clusters.append(clustered_df)
print("Combined Clusters")
print(combined_clusters)

clustered_df = combined_clusters

# exit(0)

# cleaned_data[abs(cleaned_data - mean_val) > stddev_val * z_scores] = np.nan


num_clusters = len(np.unique(hard_df))
if num_clusters > 20:
    num_clusters = 20

x_values = np.unique(x_df["Data"].values)
y_values = np.unique(y_df["Data"].values)
grid_size_x = int(x_values.size)
grid_size_y = int(y_values.size)
z_values = np.rot90(hard_df["Data"].values.reshape(grid_size_x, grid_size_y))

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_aspect('equal')
# Plots contour plot
cf = ax.contourf(x_values, y_values, z_values, num_clusters - 1)
# Plots color bar
cb = fig.colorbar(cf, ax=ax)
# Labels being set
cb.set_label("Raw Hardness Values (GPA)")
plt.title("Hardness Raw Data VS Coordinate")
plt.xlabel("X Values (um)")
plt.ylabel("Y Values (um)")

plt.show()

unique_clustered_values = np.unique(clustered_df)
num_clusters1 = len(unique_clustered_values)
print("Unique Clustered Values")
print(unique_clustered_values)

if num_clusters1 > 20:
    num_clusters1 = 20

x_values = np.unique(x_df["Data"].values)
y_values = np.unique(y_df["Data"].values)
grid_size_x = int(x_values.size)
grid_size_y = int(y_values.size)
z_values = np.rot90(clustered_df["Data"].values.reshape(grid_size_x, grid_size_y))

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_aspect('equal')
# Plots contour plot
cf = ax.contourf(x_values, y_values, z_values, levels=[-1.5, -0.5, 0.5, 1.5, 2.5, 3.5])
# Plots color bar
cb = fig.colorbar(cf, ax=ax)
# Labels being set
cb.set_label("Cluster Values")
plt.suptitle("K Means 1")
plt.title("Hardness Clustered Data VS Coordinate for " + str(num_clusters1) + " Clusters")
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
plt.title("K Means 1 Distribution After Clustering into " + str(len(cluster_num)) + " Clusters")
plt.xlabel("Cluster (" + str(len(cluster_num)) + " Clusters)")
plt.ylabel("Percentage of Data Contained Within Cluster")
plt.show()

# Sanity Check Area

combined_clustered = pd.DataFrame(hard_df)
combined_clustered["Clustered"] = clustered_df["Data"]

data_df = combined_clustered
print("Clustering for clustering algo " + str(i))
for cluster_num in np.unique(data_df["Clustered"].values):
    current_data_values = data_df.loc[data_df["Clustered"] == cluster_num]
    current_data_values_hardness = current_data_values["Data"]
    min_val = min(current_data_values_hardness)
    max_val = max(current_data_values_hardness)
    print("\tCluster " + str(cluster_num))
    print("\t\tMin: " + str(min_val))
    print("\t\tMax: " + str(max_val))

exit(0)
