import sys

sys.path.append("../")

import asyncio

from helpers import StringDefinitionsHelper
from old import RandIndexEfficient

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL

clustering_names = ["K Means 1",
                    "K Means 2",
                    "K Means 3"
                    ]

clustering_methods_list = [
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL
]

clustering_details_list = [
    {"num_clusters": "2", "random_state": "0"},
    {"num_clusters": "3", "random_state": "0"},
    {"num_clusters": "4", "random_state": "0"}
]

# clustering_method = StringDefinitionsHelper.AGGLOMERATIVE_LABEL
# clustering_details = {"num_clusters": "3", "linkage": "ward"}
# clustering_method = StringDefinitionsHelper.BIRCH_LABEL
# clustering_details = {"num_clusters": "3"}
# clustering_method = StringDefinitionsHelper.DBSCAN_LABEL
# clustering_details = {"esp": "0.75", "min_samples": "100", "algorithm": "auto"}
# clustering_details = {"m_val": "3", "max_iter": "1500", "limit": "0.01", "label": "Hardness"} # Crashes
# clustering_method = StringDefinitionsHelper.K_MEDOIDS_LABEL
# clustering_details = {"num_clusters": "3", "init": "random", "random_state": "0"}

show_contour_clustered = True
show_contour_raw = False
show_bar_graph = False

# remove_outliers = False
remove_outliers = True
save_clustered_contour = True


async def main_func():
    print(file_name, file_format)
    await RandIndexEfficient.execute(clustering_methods_list=clustering_methods_list,
                                     clustering_details_list=clustering_details_list,
                                     clustered_column=property_to_cluster,
                                     show_contour_clustered=show_contour_clustered,
                                     show_contour_raw=show_contour_raw,
                                     show_bar=show_bar_graph, file_name=file_name, file_format=file_format,
                                     remove_outliers=remove_outliers, cluster_names_list=clustering_names,
                                     save_dir="rand_index/", save_contour_clustered=save_clustered_contour)


if __name__ == "__main__":
    asyncio.run(main_func())
    print("Clustering on all files completed")
    exit(0)
