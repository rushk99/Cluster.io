import pandas as pd
import numpy as np


def print_cluster_details(data_df, clustered_data_df, cluster_name):
    """

    :param data_df: A DataFrame representation of all of the raw data we are reading
    :param clustered_data_df: A DataFrame representation of all of the clustered data we are reading
    :param cluster_name: The name of the clustering configuration we are running
    :return: Nothing

    Print the mean, fractions, and standard deviations of each cluster
    Mean - Mean value of all elements in a cluster
    Standard Deviation - Standard deviation of all elements in a cluster
    Fraction - The fraction of the whole data set which is in this cluster

    """

    # Combine the data for filtering
    all_data_values = pd.DataFrame()
    all_data_values["Data"] = data_df["Data"].values
    all_data_values["Cluster"] = clustered_data_df["Data"].values

    # Find the unique clusters that exist and the size of the data
    unique_values = np.unique(all_data_values["Cluster"].values)
    num_clusters = len(unique_values)
    data_size = len(all_data_values["Data"].values)

    print("\nCluster Details for " + str(cluster_name) + ": ")
    # For every cluster, return the details
    for i in range(num_clusters):
        cluster = unique_values[i]
        data_set = all_data_values[all_data_values["Cluster"] == cluster]
        cluster_data = data_set["Data"].values
        cluster_mean = np.mean(cluster_data)
        cluster_stddev = np.std(cluster_data)
        cluster_fraction = len(cluster_data) / data_size
        cluster_min = min(cluster_data)
        cluster_max = max(cluster_data)
        print("\tCluster " + str(cluster) + " Details: ")
        print("\t\tCluster Mean: " + str(cluster_mean))
        print("\t\tCluster Standard Deviation: " + str(cluster_stddev))
        print("\t\tCluster Fraction: " + str(cluster_fraction))
        print("\t\tCluster Min: " + str(cluster_min))
        print("\t\tCluster Max: " + str(cluster_max))


cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2]})
cluster_name = "K Means 1"
print("\nTrial 1 Report:")
print_cluster_details(data_df=data_values, clustered_data_df=cluster_values, cluster_name=cluster_name)

cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1, -1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2, 30]})
cluster_name = "K Means 2"
print("\nTrial 2 Report:")
print_cluster_details(data_df=data_values, clustered_data_df=cluster_values, cluster_name=cluster_name)

cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1, -1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2, -30]})
cluster_name = "K Means 3"
print("\nTrial 3 Report:")
print_cluster_details(data_df=data_values, clustered_data_df=cluster_values, cluster_name=cluster_name)

cluster_values = pd.DataFrame({"Data": [-1, 0, 1, 2, 2, 0, 2, 2, 1]})
data_values = pd.DataFrame({"Data": [-30, 5, 4, -1, 0, 8, 0, -2, 2]})
cluster_name = "K Means 4"
print("\nTrial 4 Report:")
print_cluster_details(data_df=data_values, clustered_data_df=cluster_values, cluster_name=cluster_name)

exit(0)
