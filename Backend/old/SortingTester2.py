import pandas as pd
import numpy as np


def order_clusters(data_df, clustered_data_df):
    """

    :param data_df: A DataFrame representation of all of the raw data we are reading
    :param clustered_data_df:A DataFrame representation of all of the clustered data we are reading
    :return: A new DataFrame which stores the new clustered values along with the original data

    """

    original_data_values = pd.DataFrame()
    original_data_values["Data"] = data_df["Data"].values
    original_data_values["Cluster"] = clustered_data_df["Data"].values

    # print("\nUnsorted:")
    # print(original_data_values)

    # https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
    # original_data_values = original_data_values.sort_values("Data")
    # print("\nSorted:")
    # print(original_data_values)

    unique_values = np.unique(original_data_values["Cluster"].values)
    num_clusters = len(unique_values)
    if -1 in unique_values:
        num_clusters = num_clusters - 1

    num_values = len(original_data_values["Cluster"].values)
    cluster_representations = pd.DataFrame()
    for i in range(num_clusters + 1):
        for j in range(num_values):
            cluster_value = original_data_values["Cluster"].values[j]
            if cluster_value == i:
                data_value = original_data_values["Data"].values[j]
                cluster_representations = cluster_representations.append(
                    pd.DataFrame({"Data": [data_value], "Cluster": [i]}))
                break

    # print("\nElement from each cluster")
    # print(cluster_representations)

    # print("\nElement from each cluster sorted")
    cluster_representations = cluster_representations.sort_values("Data")
    # print(cluster_representations)

    transformation_dictionary = {}
    for i in range(num_clusters):
        cluster_value = cluster_representations["Cluster"].values[i]
        transformation_dictionary[cluster_value] = i

    # print(transformation_dictionary)

    def transformation_function(orig_cluster):
        try:
            return transformation_dictionary[orig_cluster]
        except Exception:
            return orig_cluster

    # https://medium.com/dunder-data/select-a-single-column-of-a-pandas-dataframe-with-the-brackets-and-not-dot-notation-a5ec981cbae6
    # https://medium.com/@evelynli_30748/map-apply-applymap-with-the-lambda-function-5e83028be759
    # https://stackoverflow.com/questions/43520238/transform-dictionary-python
    # https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas
    # https://stackoverflow.com/questions/39475978/apply-function-to-each-cell-in-dataframe
    # http://chris35wills.github.io/apply_func_pandas/
    # df_new = pd.DataFrame({"Cluster": original_data_values["Cluster"].copy().values})
    # # df_new = [df_new["Clustered"] for item in df_new["Clustered"]]
    # df_new = df_new.applymap(transformation_function)
    # df_new["Data"] = original_data_values["Data"].copy()

    # print("\nThe transformed original data is:")
    # print(df_new)
    # print(original_data_values)
    df_new = pd.DataFrame({"Data": original_data_values["Cluster"].copy().values})
    # df_new = [df_new["Clustered"] for item in df_new["Clustered"]]
    # print(df_new)
    df_new = df_new.applymap(transformation_function)
    # print(df_new)
    # df_new["Data"] = original_data_values["Data"].copy().values
    return df_new


cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2]})
fixed_data = order_clusters(data_df=data_values, clustered_data_df=cluster_values)
print("\nFixed data for trial 1:")
print(fixed_data)

cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1, -1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2, 30]})
fixed_data = order_clusters(data_df=data_values, clustered_data_df=cluster_values)
print("\nFixed data for trial 2:")
print(fixed_data)

cluster_values = pd.DataFrame({"Data": [0, 1, 2, 2, 0, 2, 2, 1, -1]})
data_values = pd.DataFrame({"Data": [5, 4, -1, 0, 8, 0, -2, 2, -30]})
fixed_data = order_clusters(data_df=data_values, clustered_data_df=cluster_values)
print("\nFixed data for trial 3:")
print(fixed_data)

cluster_values = pd.DataFrame({"Data": [-1, 0, 1, 2, 2, 0, 2, 2, 1]})
data_values = pd.DataFrame({"Data": [-30, 5, 4, -1, 0, 8, 0, -2, 2]})
fixed_data = order_clusters(data_df=data_values, clustered_data_df=cluster_values)
print("\nFixed data for trial 4:")
print(fixed_data)

exit(0)
