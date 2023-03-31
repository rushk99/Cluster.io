import sys

sys.path.append("../")

import asyncio

from helpers import MainCallable, StringDefinitionsHelper

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL

clustering_methods_list = [
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL
]
clustering_details_list = [
    {"num_clusters": "2", "init": "random", "random_state": "0"},
    {"num_clusters": "3", "init": "random", "random_state": "0"},
    {"num_clusters": "4", "init": "random", "random_state": "0"},
    {"num_clusters": "5", "init": "random", "random_state": "0"},
    {"num_clusters": "6", "init": "random", "random_state": "0"},
    {"num_clusters": "7", "init": "random", "random_state": "0"},
    {"num_clusters": "3", "init": "random", "random_state": "0"},
    {"num_clusters": "3", "init": "heuristic", "random_state": "0"},
    {"num_clusters": "3", "init": "k-medoids++", "random_state": "0"},
    {"num_clusters": "2", "linkage": "ward"},
    {"num_clusters": "2", "linkage": "complete"},
    {"num_clusters": "2", "linkage": "average"},
    {"num_clusters": "2", "linkage": "single"},
    {"num_clusters": "3", "linkage": "ward"},
    {"num_clusters": "3", "linkage": "complete"},
    {"num_clusters": "3", "linkage": "average"},
    {"num_clusters": "3", "linkage": "single"},
    {"num_clusters": "4", "linkage": "ward"},
    {"num_clusters": "4", "linkage": "complete"},
    {"num_clusters": "4", "linkage": "average"},
    {"num_clusters": "4", "linkage": "single"}
]

# clustering_method =
# clustering_details =
# clustering_method = StringDefinitionsHelper.BIRCH_LABEL
# clustering_details = {"num_clusters": "3"}
# clustering_method = StringDefinitionsHelper.DBSCAN_LABEL
# clustering_details = {"esp": "0.75", "min_samples": "100", "algorithm": "auto"}
# clustering_details = {"m_val": "3", "max_iter": "1500", "limit": "0.01", "label": "Hardness"} # Crashes
# clustering_method = StringDefinitionsHelper.K_MEDOIDS_LABEL
# clustering_details = {"num_clusters": "3", "init": "random", "random_state": "0"}

show_contour_clustered = True
show_contour_raw = False
show_bar_graph = True

remove_outliers = True


# remove_outliers = False


async def main_func():
    print(file_name, file_format)
    for i in range(len(clustering_methods_list)):
        await MainCallable.execute(clustering_method=clustering_methods_list[i],
                                   clustering_details=clustering_details_list[i], clustered_column=property_to_cluster,
                                   show_contour_clustered=show_contour_clustered, show_contour_raw=show_contour_raw,
                                   show_bar=show_bar_graph, file_name=file_name, file_format=file_format,
                                   remove_outliers=remove_outliers)


if __name__ == "__main__":
    asyncio.run(main_func())
    print("Clustering on all files completed")
    exit(0)
