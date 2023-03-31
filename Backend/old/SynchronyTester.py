import collections
import sys

sys.path.append("../")

from helpers import ClusteringHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper, DataAnalysisHelper
import asyncio
import pandas as pd
import numpy as np

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL
remove_outliers = True
num_clusters = 3

# clustering_methods_list = [StringDefinitionsHelper.SPECTRAL_LABEL,
#                            StringDefinitionsHelper.SPECTRAL_LABEL]
# #
# clustering_details_list = [{"num_clusters": num_clusters, "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"},
#                            {"num_clusters": num_clusters, "assign_labels": "kmeans", "affinity": "rbf", "random_state": "0"}]

# clustering_methods_list = [StringDefinitionsHelper.DECONVOLUTION_LABEL,
#                            StringDefinitionsHelper.SPECTRAL_LABEL]
#
# clustering_details_list = [{"m_val": "3", "max_iter": "1500", "limit": "0.000001", "label": "Hardness"},
#                            {"num_clusters": num_clusters, "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"}]

# clustering_methods_list = [StringDefinitionsHelper.K_MEANS_LABEL,
#                            StringDefinitionsHelper.BIRCH_LABEL]
#
# clustering_details_list = [
#     {"num_clusters": num_clusters, "random_state": "0"},
#     {"num_clusters": num_clusters}]


clustering_methods_list = [StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.SPECTRAL_LABEL]
#
clustering_details_list = [{"num_clusters": num_clusters, "random_state": "0"},
                           {"num_clusters": num_clusters, "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"}]

async def main_func():
    print("Reading Data... ")
    data_df, x_df, y_df = DataCollectionHelper.get_data(file_name, file_format, property_to_cluster)

    # Pre process the data
    print("PreProcessing Data... ")
    data_df, x_df, y_df = PreProcessingHelper.preprocess_data(data_df=data_df, x_df=x_df, y_df=y_df,
                                                              remove_outliers=remove_outliers)

    print(file_name, file_format)

    clustered_data1 = ClusteringHelper.perform_clustering(data_df=data_df,
                                                          clustering_method=clustering_methods_list[0],
                                                          clustering_details=clustering_details_list[0])

    DataAnalysisHelper.plot_clustered_data(x_df, y_df, clustered_data1, property_to_cluster)
    clustered_data2 = ClusteringHelper.perform_clustering(data_df=data_df,
                                                          clustering_method=clustering_methods_list[1],
                                                          clustering_details=clustering_details_list[1])
    DataAnalysisHelper.plot_clustered_data(x_df, y_df, clustered_data2, property_to_cluster)

    data1 = clustered_data1.values.flatten()
    data2 = clustered_data2.values.flatten()
    overlap = []

    for idx, point in enumerate(data1):
        overlap.append((point, data2[idx]))

    counter = collections.Counter(overlap)

    clusters_acounted_for = set()
    conversions = []
    for count in counter.most_common():
        if count[0][0] not in clusters_acounted_for and count[0][1] not in clusters_acounted_for:
            clusters_acounted_for.add(count[0][0])
            clusters_acounted_for.add(count[0][1])
            conversions.append((count[0][0], count[0][1]))

    print(clusters_acounted_for, conversions)
    num_correct = 0
    for count in conversions:
        num_correct += count[1]
    print(num_correct / len(clustered_data1))

    synchrony = []
    for idx, point in enumerate(data1):
        for conversion in conversions:
            if point == conversion[0] and data2[idx] == conversion[1]:
                synchrony.append(1)
                break
        else:
            synchrony.append(0)

    df = pd.DataFrame(synchrony, columns=['Data'])
    DataAnalysisHelper.plot_clustered_data(x_df, y_df, df, property_to_cluster)
    print(np.count_nonzero(synchrony)/len(data1))



if __name__ == "__main__":
    asyncio.run(main_func())
    print("Clustering on all files completed")
    exit(0)
