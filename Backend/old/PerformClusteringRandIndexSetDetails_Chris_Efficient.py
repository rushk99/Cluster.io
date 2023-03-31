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
                    "K Means 3",
                    "K Means 4",
                    "K Means 5",
                    "Deconvolution 1",
                    "Deconvolution 2",
                    "Deconvolution 3",
                    "Deconvolution 4",
                    "K Medoids 1",
                    "K Medoids 2",
                    "K Medoids 3",
                    "K Medoids 4",
                    "K Medoids 5",
                    "K Medoids 6",
                    "K Medoids 7",
                    "K Medoids 8",
                    "K Medoids 9",
                    "Agglomerative 1",
                    "Agglomerative 2",
                    "Agglomerative 3",
                    "Agglomerative 4",
                    "Agglomerative 5",
                    "Agglomerative 6",
                    "Agglomerative 7",
                    "Agglomerative 8",
                    "Agglomerative 9",
                    "Agglomerative 10",
                    "Agglomerative 11",
                    "Agglomerative 12",
                    "Spectral 1",
                    "Spectral 2",
                    "Spectral 3",
                    "Spectral 4",
                    "Spectral 5",
                    "Spectral 6",
                    "Spectral 7",
                    "Spectral 8",
                    "Spectral 9",
                    "Spectral 10",
                    "Birch 1",
                    "Birch 2",
                    "Birch 3",
                    ]

clustering_methods_list = [
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.DECONVOLUTION_LABEL,
    StringDefinitionsHelper.DECONVOLUTION_LABEL,
    StringDefinitionsHelper.DECONVOLUTION_LABEL,
    StringDefinitionsHelper.DECONVOLUTION_LABEL,
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
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.BIRCH_LABEL,
    StringDefinitionsHelper.BIRCH_LABEL,
    StringDefinitionsHelper.BIRCH_LABEL

]

clustering_details_list = [
    {"num_clusters": "2", "random_state": "0"},
    {"num_clusters": "3", "random_state": "0"},
    {"num_clusters": "4", "random_state": "0"},
    {"num_clusters": "5", "random_state": "0"},
    {"num_clusters": "6", "random_state": "0"},
    {"m_val": "3", "max_iter": "1500", "limit": "0.000001", "label": "Hardness"},
    {"m_val": "3", "max_iter": "5000", "limit": "0.000001", "label": "Hardness"},
    {"m_val": "3", "max_iter": "1500", "limit": "0.000000001", "label": "Hardness"},
    {"m_val": "3", "max_iter": "100", "limit": "0.000001", "label": "Hardness"},
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
    {"num_clusters": "4", "linkage": "single"},
    {"num_clusters": "2", "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "3", "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "4", "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "5", "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "6", "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "2", "assign_labels": "kmeans", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "3", "assign_labels": "kmeans", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "4", "assign_labels": "kmeans", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "5", "assign_labels": "kmeans", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "6", "assign_labels": "kmeans", "affinity": "rbf", "random_state": "0"},
    {"num_clusters": "2"},
    {"num_clusters": "3"},
    {"num_clusters": "4"}

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
