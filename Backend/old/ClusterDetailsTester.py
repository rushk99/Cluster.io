import pandas as pd
import numpy as np


def print_cluster_details(data_df, clustered_data_df):
    """

    :param data_df: A DataFrame representation of all of the raw data we are reading
    :param clustered_data_df:A DataFrame representation of all of the clustered data we are reading
    :return: Nothing

    Print the mean, fractions, and standard deviations of each cluster
    Mean - Mean value of all elements in a cluster
    Standard Deviation - Standard deviation of all elements in a cluster
    Fraction - The fraction of the whole data set which is in this cluster

    """

    all_data_values = pd.DataFrame()
    all_data_values["Data"] = data_df["Data"].values
    all_data_values["Cluster"] = clustered_data_df["Data"].values

    unique_values = np.unique(all_data_values["Cluster"].values)
    num_clusters = len(unique_values)
    data_size = len(all_data_values["Data"].values)

    print("\nOriginal Data: ")
    print(str(data_size) + " elements")
    print(all_data_values)

    print("\n\nCluster Details: ")
    for i in range(num_clusters):
        cluster = unique_values[i]
        print("\nCluster " + str(cluster) + " Details: ")
        data_set = all_data_values[all_data_values["Cluster"] == cluster]
        cluster_data = data_set["Data"].values
        print(data_set)
        print(cluster_data)
        cluster_mean = np.mean(cluster_data)
        cluster_stddev = np.std(cluster_data)
        cluster_fraction = len(cluster_data) / data_size
        print(cluster_mean)
        print(cluster_stddev)
        print(cluster_fraction)

    # num_values = len(all_data_values["Cluster"].values)
    # cluster_representations = pd.DataFrame()
    # for i in range(num_clusters + 1):
    #     for j in range(num_values):
    #         cluster_value = all_data_values["Cluster"].values[j]
    #         if cluster_value == i:
    #             data_value = all_data_values["Data"].values[j]
    #             cluster_representations = cluster_representations.append(
    #                 pd.DataFrame({"Data": [data_value], "Cluster": [i]}))
    #             break
    #
    # # print("\nElement from each cluster")
    # # print(cluster_representations)
    #
    # # print("\nElement from each cluster sorted")
    # cluster_representations = cluster_representations.sort_values("Data")
    # # print(cluster_representations)
    #
    # transformation_dictionary = {}
    # for i in range(num_clusters):
    #     cluster_value = cluster_representations["Cluster"].values[i]
    #     transformation_dictionary[cluster_value] = i
    #
    # # print(transformation_dictionary)
    #
    # def transformation_function(orig_cluster):
    #     try:
    #         return transformation_dictionary[orig_cluster]
    #     except Exception:
    #         return orig_cluster
    #
    # # https://medium.com/dunder-data/select-a-single-column-of-a-pandas-dataframe-with-the-brackets-and-not-dot-notation-a5ec981cbae6
    # # https://medium.com/@evelynli_30748/map-apply-applymap-with-the-lambda-function-5e83028be759
    # # https://stackoverflow.com/questions/43520238/transform-dictionary-python
    # # https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas
    # # https://stackoverflow.com/questions/39475978/apply-function-to-each-cell-in-dataframe
    # # http://chris35wills.github.io/apply_func_pandas/
    # # df_new = pd.DataFrame({"Cluster": all_data_values["Cluster"].copy().values})
    # # # df_new = [df_new["Clustered"] for item in df_new["Clustered"]]
    # # df_new = df_new.applymap(transformation_function)
    # # df_new["Data"] = all_data_values["Data"].copy()
    #
    # # print("\nThe transformed original data is:")
    # # print(df_new)
    # # print(all_data_values)
    # df_new = pd.DataFrame({"Data": all_data_values["Cluster"].copy().values})
    # # df_new = [df_new["Clustered"] for item in df_new["Clustered"]]
    # # print(df_new)
    # df_new = df_new.applymap(transformation_function)
    # # print(df_new)
    # # df_new["Data"] = all_data_values["Data"].copy().values


cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2]})
print("\nTrial 1 Report:")
print_cluster_details(data_df=data_values, clustered_data_df=cluster_values)

exit(0)
