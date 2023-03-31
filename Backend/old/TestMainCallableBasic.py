import sys

sys.path.append("../")


import asyncio

from helpers import MainCallable, StringDefinitionsHelper

# File Properties
# file_names = ["../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx",
#               "../data/05SEP2019_600F-02min_BCS-1152.xlsx",
#               "../data/06NOV2019_Austemper-600defF-5min_BCS-1027.xlsx",
#               "../data/UMass Ta As-Sprayed #1 Map.xlsx",
#               "../data/UMass Ta As-Sprayed #2 Map.xlsx",
#               "../data/A365 CuCS T6 11-30-2018 1217.xlsx",
#               "../data/04SEP2019_600F-30min_BCS-RCS-1301.xlsx",
#               "../data/15JAN2020_Aust5min_BCS.xlsx",
#               "../data/15JAN2020_Aust30Min_BCS.xlsx",
#               "../data/19AUG2020_0515-2017-10601_Unprocessed_BCS-2118 MAP.xlsx"]
# file_formats = [StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO,
#                 StringDefinitionsHelper.FILE_FORMAT_TWO]

# file_name = "../data/UMass Ta As-Sprayed #1 Map.xlsx"
# file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

# file_name = "../data/A365 CuCS T6 11-30-2018 1217.xlsx"
# file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

# file_name = "../data/04SEP2019_600F-30min_BCS-RCS-1301.xlsx"
# file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

# file_name = "../data/06NOV2019_Austemper-600defF-5min_BCS-1027.xlsx"
# file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

# file_name = "../data/05SEP2019_600F-02min_BCS-1152.xlsx"
# file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

# file_name = "../data/05SEP2019_600F-02min_BCS-1152.xlsx"
# file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL
# property_to_cluster = StringDefinitionsHelper.MODULUS_LABEL

# clustering_method = StringDefinitionsHelper.AGGLOMERATIVE_LABEL
# clustering_details = {"num_clusters": "3", "linkage": "ward"}
# clustering_method = StringDefinitionsHelper.BIRCH_LABEL
# clustering_details = {"num_clusters": "3"}
# clustering_method = StringDefinitionsHelper.DBSCAN_LABEL
# clustering_details = {"esp": "0.75", "min_samples": "100", "algorithm": "auto"}
clustering_method = StringDefinitionsHelper.DECONVOLUTION_LABEL
clustering_details = {"m_val": "3", "max_iter": "1500", "limit": "0.000001", "label": "Hardness"}
# clustering_details = {"m_val": "3", "max_iter": "5000", "limit": "0.000001", "label": "Hardness"}
# clustering_details = {"m_val": "3", "max_iter": "1500", "limit": "0.000000001", "label": "Hardness"}
# clustering_details = {"m_val": "3", "max_iter": "1500", "limit": "0.01", "label": "Hardness"} # Crashes
# clustering_details = {"m_val": "3", "max_iter": "100", "limit": "0.000001", "label": "Hardness"}
# clustering_method = StringDefinitionsHelper.K_MEANS_LABEL
# clustering_details = {"num_clusters": "3", "random_state": "0"}
# clustering_method = StringDefinitionsHelper.K_MEDOIDS_LABEL
# clustering_details = {"num_clusters": "3", "init": "random", "random_state": "0"}
# clustering_method = StringDefinitionsHelper.OPTICS_LABEL
# clustering_details = {"esp": "999999999999999", "min_samples": "100", "algorithm": "auto"}
# TODO esp should be infinity, find a fix
# clustering_method = StringDefinitionsHelper.SPECTRAL_LABEL
# clustering_details = {"num_clusters": "3", "assign_labels": "discretize", "affinity": "rbf", "random_state": "0"}
# clustering_method = "Invalid Clustering Method"  # This will be invalid
# TODO Please change the clustering method immediately above this to change the clustering method

show_contour_clustered = True
show_contour_raw = True
show_bar_graph = True

remove_outliers = True
# remove_outliers = False


async def main_func():
    print(file_name, file_format)
    await MainCallable.execute(clustering_method=clustering_method, clustering_details=clustering_details,
                               clustered_column=property_to_cluster, show_contour_clustered=show_contour_clustered,
                               show_contour_raw=show_contour_raw, show_bar=show_bar_graph, file_name=file_name,
                               file_format=file_format, remove_outliers=remove_outliers)


if __name__ == "__main__":
    asyncio.run(main_func())
