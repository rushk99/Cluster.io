import sys

sys.path.append("../")

import asyncio

from helpers import StringDefinitionsHelper
from old import AllClusteringAnalysisEfficient

# The cluster values to check for all plots
CLUSTER_VALUES = (2, 3, 4, 5, 6, 7, 8, 15, 20, 30)
# The cluster values to check for spectral as spectral does not scale well with many more clusters
CLUSTER_VALUES_SPECTRAL = (2, 3, 4, 5, 6)

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL

clustering_names_small = [
    "K Means 1",
    "K Means 2",
    "K Means 3",
    "K Means 4",
    # "K Medoids 1",
    # "K Medoids 2",
    # "K Medoids 3",

]

clustering_methods_list_small = [
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    # StringDefinitionsHelper.K_MEDOIDS_LABEL,
    # StringDefinitionsHelper.K_MEDOIDS_LABEL,
    # StringDefinitionsHelper.K_MEDOIDS_LABEL,

]

clustering_details_list_small = [
    {"num_clusters": "2", "random_state": "0"},
    {"num_clusters": "3", "random_state": "0"},
    {"num_clusters": "4", "random_state": "0"},
    {"num_clusters": "5", "random_state": "0"},
    # {"num_clusters": "3", "init": "random", "random_state": "0"},
    # {"num_clusters": "3", "init": "heuristic", "random_state": "0"},
    # {"num_clusters": "3", "init": "k-medoids++", "random_state": "0"},

]

diff_clustering_methods = [
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.DECONVOLUTION_LABEL,
    StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.AGGLOMERATIVE_LABEL,
    StringDefinitionsHelper.SPECTRAL_LABEL,
    StringDefinitionsHelper.BIRCH_LABEL,
    StringDefinitionsHelper.HDBSCAN_LABEL,
    StringDefinitionsHelper.DBSCAN_LABEL,
    StringDefinitionsHelper.OPTICS_LABEL,
]

k_means_configs = [
]

# K Means config loop
for i in CLUSTER_VALUES:
    k_means_configs.append({"num_clusters": str(i), "random_state": "0"})

deconvolution_configs = [
]

# Deconvolution config loop
m_val = 3
label = "Hardness"
for i in range(2):
    for max_iter in ("100", "1500", "5000"):
        for limit in ("0.000001", "0.000000001"):
            deconvolution_configs.append({"m_val": m_val, "max_iter": max_iter, "limit": limit, "label": label})

k_medoids_configs = [
]

# K Medoids config loop
for i in CLUSTER_VALUES:
    for init in ("random", "heuristic", "k-medoids++"):
        k_medoids_configs.append({"num_clusters": str(i), "init": init, "random_state": "0"})

agglomerative_configs = [
]

# Agglomerative config loop
for i in CLUSTER_VALUES:
    for linkage in ("ward", "complete", "average", "single"):
        agglomerative_configs.append({"num_clusters": str(i), "linkage": linkage})

spectral_configs = [
]

# Spectral config loop
affinity = "rbf"
for i in CLUSTER_VALUES_SPECTRAL:
    for assign_labels in ("discretize", "kmeans"):
        spectral_configs.append({"num_clusters": str(i), "assign_labels": assign_labels,
                                 "affinity": affinity, "random_state": "0"})

birch_configs = [
]

# Birch config loop
for i in CLUSTER_VALUES:
    birch_configs.append({"num_clusters": str(i)})

hdbscan_configs = [
]

# HDBSCAN config loop
distance_metric = "euclidean"
for min_cluster_size in ("5", "10", "20"):
    for min_samples in ("100", "500", '1000'):
        hdbscan_configs.append({"distance_metric": distance_metric, "min_cluster_size": min_cluster_size,
                                "min_samples": min_samples})

dbscan_configs = [
]

# DBSCAN config loop
for eps_val in ("5", '0.25', "20"):
    for min_samples_val in ("10", "25", "100"):
        for db_method in ("auto", "ball_tree", 'kd_tree', "brute"):
            dbscan_configs.append({"eps": eps_val, "min_samples": min_samples_val, "algorithm": db_method})

optics_configs = [
]

# OPTICS config loop
for eps_val in ("5", '0.25', "20"):
    for min_samples_val in ("10", "25", "100"):
        for optics_method in ("auto", "ball_tree", 'kd_tree', "brute"):
            optics_configs.append({"eps": eps_val, "min_samples": min_samples_val, "algorithm": optics_method})

all_config_lists = [k_means_configs, deconvolution_configs, k_medoids_configs, agglomerative_configs, spectral_configs,
                    birch_configs, hdbscan_configs, dbscan_configs, optics_configs]

final_methods_list = []
final_names_list = []
final_config_list = []

for i in range(len(diff_clustering_methods)):
    current_config_list = all_config_lists[i]
    current_cluster_method = diff_clustering_methods[i]
    for j in range(len(current_config_list)):
        final_methods_list.append(current_cluster_method)
        final_names_list.append(str(current_cluster_method + " " + str(j)))
        final_config_list.append(current_config_list[j])

show_contour_clustered = True
show_contour_raw = False
show_bar_graph = False

remove_outliers = True
save_clustered_contour = True
give_cluster_report = True

print_to_console = True
print_to_text_file = True
text_file_name = "../old/text_file_output/6-4-21_Run2.txt"


async def main_func():
    # print(file_name, file_format)
    # await AllClusteringAnalysisEfficient.execute(clustering_methods_list=clustering_methods_list_small,
    #                                              clustering_details_list=clustering_details_list_small,
    #                                              clustered_column=property_to_cluster,
    #                                              show_contour_clustered=show_contour_clustered,
    #                                              show_contour_raw=show_contour_raw,
    #                                              show_bar=show_bar_graph, file_name=file_name,
    #                                              file_format=file_format, remove_outliers=remove_outliers,
    #                                              cluster_names_list=clustering_names_small, save_dir="rand_index/",
    #                                              save_contour_clustered=save_clustered_contour,
    #                                              give_cluster_report=give_cluster_report,
    #                                              print_to_console=print_to_console,
    #                                              print_to_text_file=print_to_text_file,
    #                                              text_file_name=text_file_name)
    await AllClusteringAnalysisEfficient.execute(clustering_methods_list=final_methods_list,
                                                 clustering_details_list=final_config_list,
                                                 clustered_column=property_to_cluster,
                                                 show_contour_clustered=show_contour_clustered,
                                                 show_contour_raw=show_contour_raw,
                                                 show_bar=show_bar_graph, file_name=file_name,
                                                 file_format=file_format, remove_outliers=remove_outliers,
                                                 cluster_names_list=final_names_list, save_dir="rand_index/",
                                                 save_contour_clustered=save_clustered_contour,
                                                 give_cluster_report=give_cluster_report,
                                                 print_to_console=print_to_console,
                                                 print_to_text_file=print_to_text_file,
                                                 text_file_name=text_file_name)
    # print(len(final_methods_list))
    # print(len(final_names_list))
    # print(len(final_config_list))
    # print(final_methods_list)
    # print(final_names_list)
    # print(final_config_list)


if __name__ == "__main__":
    asyncio.run(main_func())
    print("Clustering on all files completed")
    exit(0)
