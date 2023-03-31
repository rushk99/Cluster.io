import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

sys.path.append("../")
sys.path.append("../../")
sys.path.append("/ocean/projects/dmr200021p/cvieira")
sys.path.append("/ocean/projects/dmr200021p/cvieira/helpers")

# for item in sys.path:
#     print(item)

import asyncio

from helpers import StringDefinitionsHelper, AllClusteringAnalysisEfficientServer

# The cluster values to check for all plots
# CLUSTER_VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50)
CLUSTER_VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 50)

# The cluster values to check for spectral as spectral does not scale well with many more clusters
CLUSTER_VALUES_SPECTRAL = (2, 3, 4, 5, 6, 7, 8, 9, 10)
# CLUSTER_VALUES_SPECTRAL = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 30)

# The limits to use for Deconvolution
# DECON_LIMITS = ("0.000001", "0.1", "0.001", "0.0001")
DECON_LIMITS = ("0.000001", "0.000000001", "0.1", "0.001", "0.0001", "0.0000001")

# The iterations to use for Deconvolution
# DECON_ITERATIONS = ("100", "1500", "5000")
DECON_ITERATIONS = ("100", "1500", "5000", "10000", "30000")


# TODO Ocean
# TODO 14 18 26 Spectral

# file_name = "data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx" # 10000
# file_name = "data/04SEP2019_600F-30min_BCS-RCS-1301.xlsx" # 100
# file_name = "data/05SEP2019_600F-02min_BCS-1152.xlsx" # 10000
file_name = "data/06NOV2019_Austemper-600defF-5min_BCS-1027.xlsx" # 10000
# file_name = "data/15JAN2020_Aust5min_BCS.xlsx" # 625
# file_name = "data/15JAN2020_Aust30Min_BCS.xlsx" # 625
# file_name = "data/19AUG2020_0515-2017-10601_Unprocessed_BCS-2118 MAP.xlsx" # 62500
# file_name = "data/A365 CuCS T6 11-30-2018 1217.xlsx" # 10000
# file_name = "data/Bulk WAAM of Puck 1.xlsx" # 10000
# file_name = "data/UMass Ta As-Sprayed #1 Map.xlsx" # 10000
# file_name = "data/UMass Ta As-Sprayed #2 Map.xlsx" # 10000

file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

decon_show_plots = False
decon_save_plots = True

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL

clustering_names_small = [
    # "K Means 1",
    # "K Means 2",
    # "K Means 3",
    # "K Means 4",
    # "K Means 5",
    "K Means 6",
    "Decon 1",
    "K Means 7",
    # "K Medoids 1",
    # "K Medoids 2",
    # "K Medoids 3",

]

clustering_methods_list_small = [
    # StringDefinitionsHelper.K_MEANS_LABEL,
    # StringDefinitionsHelper.K_MEANS_LABEL,
    # StringDefinitionsHelper.K_MEANS_LABEL,
    # StringDefinitionsHelper.K_MEANS_LABEL,
    # StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,
    StringDefinitionsHelper.DECONVOLUTION_LABEL,
    # StringDefinitionsHelper.K_MEDOIDS_LABEL,
    # StringDefinitionsHelper.K_MEDOIDS_LABEL,
    # StringDefinitionsHelper.K_MEDOIDS_LABEL,
    StringDefinitionsHelper.K_MEANS_LABEL,

]

clustering_details_list_small = [
    # {"num_clusters": "2", "random_state": "0"},
    # {"num_clusters": "3", "random_state": "0"},
    # {"num_clusters": "3", "random_state": "10"},
    # {"num_clusters": "4", "random_state": "0"},
    # {"num_clusters": "5", "random_state": "0"},
    {"num_clusters": "5", "random_state": "60"},
    # {"num_clusters": "3", "init": "random", "random_state": "0"},
    # {"num_clusters": "3", "init": "heuristic", "random_state": "0"},
    # {"num_clusters": "3", "init": "k-medoids++", "random_state": "0"},
    {"m_val": 3, "max_iter": 1500, "limit": 1, "label": "Hardness", "show_plots": False, "save_plots": True},
    {"num_clusters": "5", "random_state": "60"},

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
    for possible_state in ("0", "50", "100", "1000"):
        k_means_configs.append({"num_clusters": str(i), "random_state": possible_state})

deconvolution_configs = [
]

# Deconvolution config loop
m_val = 3
label = "Hardness"
for i in range(3):
    for max_iter in DECON_ITERATIONS:
        for limit in DECON_LIMITS:
            deconvolution_configs.append({"m_val": m_val, "max_iter": max_iter, "limit": limit, "label": label,
                                          "show_plots": decon_show_plots, "save_plots": decon_save_plots})

k_medoids_configs = [
]

# K Medoids config loop
for i in CLUSTER_VALUES:
    for init in ("random", "heuristic", "k-medoids++"):
        for possible_state in ("0", "50", "100", "1000"):
            k_medoids_configs.append({"num_clusters": str(i), "init": init, "random_state": possible_state})

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
for min_cluster_size in ("5", "10", "20", "50", "75", "100"):
    for min_samples in ("10", "100", "500", "750", "1000"):
        hdbscan_configs.append({"distance_metric": distance_metric, "min_cluster_size": min_cluster_size,
                                "min_samples": min_samples})

dbscan_configs = [
]

# DBSCAN config loop
for eps_val in ("5", '0.25', "20", "100", "500"):
    for min_samples_val in ("10", "25", "100", "1000", "5"):
        for db_method in ("auto", "ball_tree", 'kd_tree', "brute"):
            dbscan_configs.append({"eps": eps_val, "min_samples": min_samples_val, "algorithm": db_method})

optics_configs = [
]

# OPTICS config loop
for eps_val in ("5", '0.25', "20", "100", "500"):
    for min_samples_val in ("10", "25", "100", "1000", "5"):
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

show_contour_clustered = False
show_contour_raw = False

remove_outliers = True
save_clustered_contour = True
give_cluster_report = True

print_to_console = True
print_to_text_file = True
text_report_name = "RunOutput.txt"

show_rand_index_plots = False
save_rand_index_visualizations = True

show_bar_graph = False
save_bar = True

save_clustered_data = True


async def main_func():
    # print(file_name, file_format)
    async def run_with_data(clustering_methods_list, clustering_details_list, cluster_names_list):
        await AllClusteringAnalysisEfficientServer.execute(clustering_methods_list=clustering_methods_list,
                                                           clustering_details_list=clustering_details_list,
                                                           clustered_column=property_to_cluster,
                                                           show_contour_clustered=show_contour_clustered,
                                                           show_contour_raw=show_contour_raw,
                                                           show_bar=show_bar_graph, file_name=file_name,
                                                           file_format=file_format, remove_outliers=remove_outliers,
                                                           cluster_names_list=cluster_names_list,
                                                           save_contour_clustered=save_clustered_contour,
                                                           give_cluster_report=give_cluster_report,
                                                           print_to_console=print_to_console,
                                                           print_to_text_file=print_to_text_file,
                                                           text_report_name=text_report_name,
                                                           show_rand_index_plots=show_rand_index_plots,
                                                           save_rand_index_visualizations=save_rand_index_visualizations,
                                                           save_cluster_histograms=save_bar,
                                                           save_clustered_data=save_clustered_data)

    # await run_with_data(clustering_methods_list=clustering_methods_list_small,
    #                     clustering_details_list=clustering_details_list_small,
    #                     cluster_names_list=clustering_names_small)
    await run_with_data(clustering_methods_list=final_methods_list,
                        clustering_details_list=final_config_list,
                        cluster_names_list=final_names_list)

    # await AllClusteringAnalysisEfficientServer.execute(clustering_methods_list=final_methods_list,
    #                                                    clustering_details_list=final_config_list,
    #                                                    clustered_column=property_to_cluster,
    #                                                    show_contour_clustered=show_contour_clustered,
    #                                                    show_contour_raw=show_contour_raw,
    #                                                    show_bar=show_bar_graph, file_name=file_name,
    #                                                    file_format=file_format, remove_outliers=remove_outliers,
    #                                                    cluster_names_list=final_names_list, save_dir="rand_index/",
    #                                                    save_contour_clustered=save_clustered_contour,
    #                                                    give_cluster_report=give_cluster_report,
    #                                                    print_to_console=print_to_console,
    #                                                    print_to_text_file=print_to_text_file,
    #                                                    text_file_name=text_file_name,
    #                                                    show_rand_index_plots=show_rand_index_plots)
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
