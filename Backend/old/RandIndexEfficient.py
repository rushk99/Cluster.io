import sys

sys.path.append("../")

from helpers import ClusteringHelper, DataAnalysisHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper
from server_files.store import queues
from sklearn.metrics import adjusted_rand_score
import asyncio

WAIT_TIME = 0.001

COLUMN_DEFAULT = StringDefinitionsHelper.HARDNESS_LABEL


async def execute(clustering_methods_list, clustering_details_list, cluster_names_list,
                  file_name, file_format, clustered_column=COLUMN_DEFAULT, caller_id=None,
                  show_contour_clustered=True, show_contour_raw=True, show_bar=True, remove_outliers=False,
                  save_contour_clustered=False, save_dir=""):
    """

    :param clustering_methods_list: The clustering methods we are using for our clustering,
    see StringDefinitionsHelper for options
    :param clustering_details_list: The details associated with the clustering methods we are using for our
    clustering methods, see StringDefinitionsHelper.py and ClusteringHelper.py for details
    :param cluster_names_list: How to identify the clusters for print reports
    :param file_name: The name of the file we are reading in relative to the folder of the executable
    :param file_format: The format of the file we are reading in, see StringDefinitionsHelper for options
    :param clustered_column: The name of the type of column we are clustering, default value of Hardness
    :param caller_id: #TODO Eric describe this
    :param show_contour_clustered: A boolean of whether or not to show the final clustered data's contour plot
    :param show_contour_raw: A boolean of whether or not to show the raw data's contour plot
    :param show_bar: A boolean of whether or not to show the bar graph
    :param remove_outliers: A boolean of whether or not to remove outliers
    :param save_contour_clustered: A boolean of whether or not save the clustered contour plot
    :param save_dir: The directory to save the figures to
    :return: Nothing at the moment

    Reads in all of the data and performs the necessary clustering. It performs the following steps: Reading in the
    data, preprocessing the data, clustering the data, an then analyzing the data. The the respective helper classes
    for more details as to how the processes work.
    """

    assert len(clustering_methods_list) == len(clustering_details_list) == len(cluster_names_list)
    for i in range(len(clustering_methods_list)):
        print("\n")
        print(str(cluster_names_list[i]))
        print("Clustering Method: " + str(clustering_methods_list[i]))
        print("\tClustering Details: ")
        for cluster_param in clustering_details_list[i]:
            print("\t\t" + str(cluster_param) + ": " + str(clustering_details_list[i][cluster_param]))
        print("\tFile Name: " + str(file_name))
        print("\tFile Format: " + str(file_format))
        print("\tClustering Column: " + str(clustered_column))
        print("\tShow Raw Data: " + str(show_contour_raw))
        print("\tShow Clustered Contour Plot: " + str(show_contour_clustered))
        print("\tShow Bar Graph: " + str(show_bar))
        print("\tRemove Outliers: " + str(remove_outliers))
        print("\tSave Clustered Contour Plot: " + str(save_contour_clustered))
        print("\tSave Directory: " + str(save_dir))
        print("\n")

    # TODO Specify different parameters to be used, clustering details need dictionary
    # TODO Fix project name in auto docs and readme
    # Read in data
    for queue in queues: await queue.put("READING")
    await asyncio.sleep(WAIT_TIME)
    print("Reading Data... ")
    data_df, x_df, y_df = DataCollectionHelper.get_data(file_name, file_format, clustered_column)

    # Pre process the data
    for queue in queues: await queue.put("PREPROCESSING")
    await asyncio.sleep(WAIT_TIME)
    print("PreProcessing Data... ")
    data_df, x_df, y_df = PreProcessingHelper.preprocess_data(data_df=data_df, x_df=x_df, y_df=y_df,
                                                              remove_outliers=remove_outliers)

    # Cluster the data
    for queue in queues: await queue.put("CLUSTERING")
    await asyncio.sleep(WAIT_TIME)
    print("Clustering Data... ")
    list_of_clustered_data = []
    for i in range(len(clustering_methods_list)):
        print("Clustering Data with clustering method: " + str(cluster_names_list[i]))
        clustered_data = ClusteringHelper.perform_clustering(data_df=data_df,
                                                             clustering_method=clustering_methods_list[i],
                                                             clustering_details=clustering_details_list[i])
        list_of_clustered_data.append(clustered_data)

    # # Provide Analysis
    # for queue in queues: await queue.put("ANALYZING")
    # await asyncio.sleep(WAIT_TIME)
    # print("Analyzing Data... ")
    # DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df, clustered_data=clustered_data_one,
    #                                     prop=clustered_column, show_contour_clustered=show_contour_clustered,
    #                                     show_contour_raw=show_contour_raw, show_bar=show_bar)
    # DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df, clustered_data=clustered_data_two,
    #                                     prop=clustered_column, show_contour_clustered=show_contour_clustered,
    #                                     show_contour_raw=show_contour_raw, show_bar=show_bar)

    # Gathered from https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html

    # Provide Visualization
    for queue in queues: await queue.put("Visualizing")
    await asyncio.sleep(WAIT_TIME)
    print("Visualizing Data... ")
    for i in range(len(clustering_methods_list)):
        print("Visualizing Data with clustering method: " + str(cluster_names_list[i]))
        DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df,
                                            clustered_data=list_of_clustered_data[i],
                                            prop=clustered_column, show_contour_clustered=show_contour_clustered,
                                            show_contour_raw=show_contour_raw, show_bar=show_bar,
                                            cluster_name=cluster_names_list[i], cluster_iter=i,
                                            save_clustered_contour=save_contour_clustered, save_dir=save_dir)

    for i in range(len(clustering_methods_list)):
        for j in range(len(clustering_methods_list)):
            cluster_method_one_list = list_of_clustered_data[i]["Data"].values
            cluster_method_two_list = list_of_clustered_data[j]["Data"].values
            rand_index = adjusted_rand_score(cluster_method_one_list, cluster_method_two_list)
            print(str(rand_index) + " is the rand index between clusters " + str(cluster_names_list[i]) + " and " + str(
                cluster_names_list[j]))
        print("\n\n")

    for queue in queues:
        await queue.put("COMPLETE")
        print(queue)
    print("Process complete")
