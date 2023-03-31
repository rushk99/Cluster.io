import sys

sys.path.append("../")

import asyncio

from helpers import StringDefinitionsHelper
from old import RandIndex
import numpy as np

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL

clustering_names = ["K Means 1",
                    "K Means 2",
                    "K Means 3",
                    "K Means 4",
                    "K Means 5",
                    "Deconvolution 1",
                    "Deconvolution 2",
                    "Deconvolution 3",
                    "Deconvolution 4"
                    ]

clustering_methods_list = [StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.DECONVOLUTION_LABEL,
                           StringDefinitionsHelper.DECONVOLUTION_LABEL,
                           StringDefinitionsHelper.DECONVOLUTION_LABEL,
                           StringDefinitionsHelper.DECONVOLUTION_LABEL]

clustering_details_list = [{"num_clusters": "2", "random_state": "0"},
                           {"num_clusters": "3", "random_state": "0"},
                           {"num_clusters": "4", "random_state": "0"},
                           {"num_clusters": "5", "random_state": "0"},
                           {"num_clusters": "6", "random_state": "0"},
                           {"m_val": "3", "max_iter": "1500", "limit": "0.000001", "label": "Hardness"},
                           {"m_val": "3", "max_iter": "5000", "limit": "0.000001", "label": "Hardness"},
                           {"m_val": "3", "max_iter": "1500", "limit": "0.000000001", "label": "Hardness"},
                           {"m_val": "3", "max_iter": "100", "limit": "0.000001", "label": "Hardness"}]

# clustering_method = StringDefinitionsHelper.AGGLOMERATIVE_LABEL
# clustering_details = {"num_clusters": "3", "linkage": "ward"}
# clustering_method = StringDefinitionsHelper.BIRCH_LABEL
# clustering_details = {"num_clusters": "3"}
# clustering_method = StringDefinitionsHelper.DBSCAN_LABEL
# clustering_details = {"esp": "0.75", "min_samples": "100", "algorithm": "auto"}
# clustering_details = {"m_val": "3", "max_iter": "1500", "limit": "0.01", "label": "Hardness"} # Crashes
# clustering_method = StringDefinitionsHelper.K_MEDOIDS_LABEL
# clustering_details = {"num_clusters": "3", "init": "random", "random_state": "0"}

show_contour_clustered = False
show_contour_raw = False
show_bar_graph = False

# remove_outliers = False
remove_outliers = True


async def main_func():
    print(file_name, file_format)
    rand_index_values = np.zeros((len(clustering_methods_list), len(clustering_methods_list)))
    for i in range(len(clustering_methods_list)):
        for j in range(len(clustering_methods_list)):
            rand_index = await RandIndex.execute(clustering_method_one=clustering_methods_list[i],
                                                 clustering_method_two=clustering_methods_list[j],
                                                 clustering_details_one=clustering_details_list[i],
                                                 clustering_details_two=clustering_details_list[j],
                                                 clustered_column=property_to_cluster,
                                                 show_contour_clustered=show_contour_clustered,
                                                 show_contour_raw=show_contour_raw,
                                                 show_bar=show_bar_graph, file_name=file_name, file_format=file_format,
                                                 remove_outliers=remove_outliers, cluster_one_name=clustering_names[i],
                                                 cluster_two_name=clustering_names[j])
            rand_index_values[i][j] = rand_index
    print("\n")
    for i in range(len(clustering_methods_list)):
        for j in range(len(clustering_methods_list)):
            print(str(clustering_names[i]) + " and " + str(clustering_names[j]) + " have a rand index of " + str(
                rand_index_values[i][j]))
        print("\n")


if __name__ == "__main__":
    asyncio.run(main_func())
    print("Clustering on all files completed")
    exit(0)
