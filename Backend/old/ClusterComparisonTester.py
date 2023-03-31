import sys

sys.path.append("../")

from helpers import ClusteringHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper, DBI
import asyncio

file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
file_format = StringDefinitionsHelper.FILE_FORMAT_TWO

property_to_cluster = StringDefinitionsHelper.HARDNESS_LABEL
remove_outliers = True

clustering_names = ["K Means 1",
                    "K Means 2",
                    "K Means 3",
                    "K Means 4",
                    "K Means 5"
                    ]

clustering_methods_list = [StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL,
                           StringDefinitionsHelper.K_MEANS_LABEL]

clustering_details_list = [{"num_clusters": "2", "random_state": "0"},
                           {"num_clusters": "3", "random_state": "0"},
                           {"num_clusters": "4", "random_state": "0"},
                           {"num_clusters": "5", "random_state": "0"},
                           {"num_clusters": "6", "random_state": "0"}]


# clustering_names = [
#     "Deconvolution 1",
#     "Deconvolution 2",
#     "Deconvolution 3",
#     "Deconvolution 4"
# ]
#
# clustering_methods_list = [
#     StringDefinitionsHelper.DECONVOLUTION_LABEL,
#     StringDefinitionsHelper.DECONVOLUTION_LABEL,
#     StringDefinitionsHelper.DECONVOLUTION_LABEL,
#     StringDefinitionsHelper.DECONVOLUTION_LABEL]
#
# clustering_details_list = [
#     {"m_val": "3", "max_iter": "1500", "limit": "0.000001", "label": "Hardness"},
#     {"m_val": "3", "max_iter": "5000", "limit": "0.000001", "label": "Hardness"},
#     {"m_val": "3", "max_iter": "1500", "limit": "0.000000001", "label": "Hardness"},
#     {"m_val": "3", "max_iter": "100", "limit": "0.000001", "label": "Hardness"}]

# evaluation_method_function = SilhouetteCoefficient
# evaluation_method_name = "Silhouette Coefficient"
evaluation_method_function = DBI
evaluation_method_name = "Davies Bouldin Score"


async def main_func():
    print("Reading Data... ")
    data_df, x_df, y_df = DataCollectionHelper.get_data(file_name, file_format, property_to_cluster)

    # Pre process the data
    print("PreProcessing Data... ")
    data_df, x_df, y_df = PreProcessingHelper.preprocess_data(data_df=data_df, x_df=x_df, y_df=y_df,
                                                              remove_outliers=remove_outliers)

    print(file_name, file_format)
    clustered_data_list = []
    for i in range(len(clustering_methods_list)):
        print("Clustering Data... ")
        clustered_data = ClusteringHelper.perform_clustering(data_df=data_df,
                                                             clustering_method=clustering_methods_list[i],
                                                             clustering_details=clustering_details_list[i])
        clustered_data_list.append(clustered_data["Data"])

    # Find the best cluster using a method
    idx_of_best_cluster, score = evaluation_method_function.getBest(data_df, clustered_data_list)

    print(
        f'Using {evaluation_method_name}, {clustering_methods_list[idx_of_best_cluster]} with parameters '
        f'{clustering_details_list[idx_of_best_cluster]} has the best clusters with a score of {score}')


if __name__ == "__main__":
    asyncio.run(main_func())
    print("Clustering on all files completed")
    exit(0)
