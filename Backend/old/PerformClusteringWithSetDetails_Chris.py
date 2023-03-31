import sys

sys.path.append("../")

import asyncio

from helpers import MainCallable, StringDefinitionsHelper

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL

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
    StringDefinitionsHelper.BIRCH_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
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
    {"num_clusters": "4"},
    {"distance_metric": "euclidean", "min_cluster_size": "5", "min_samples": "100"},
    {"distance_metric": "euclidean", "min_cluster_size": "10", "min_samples": "100"},
    {"distance_metric": "euclidean", "min_cluster_size": "20", "min_samples": "100"},
    {"distance_metric": "euclidean", "min_cluster_size": "5", "min_samples": "500"},
    {"distance_metric": "euclidean", "min_cluster_size": "10", "min_samples": "500"},
    {"distance_metric": "euclidean", "min_cluster_size": "20", "min_samples": "500"},
    {"distance_metric": "euclidean", "min_cluster_size": "5", "min_samples": "1000"},
    {"distance_metric": "euclidean", "min_cluster_size": "10", "min_samples": "1000"},
    {"distance_metric": "euclidean", "min_cluster_size": "20", "min_samples": "1000"},
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
