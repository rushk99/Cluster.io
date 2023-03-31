import sys

sys.path.append("../")

from helpers import ClusteringHelper, DataAnalysisHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper
from server_files.store import queues
from sklearn.metrics import adjusted_rand_score
import asyncio

WAIT_TIME = 0.001

COLUMN_DEFAULT = StringDefinitionsHelper.HARDNESS_LABEL


async def execute(clustering_method_one, clustering_method_two, clustering_details_one, clustering_details_two,
                  file_name, file_format, clustered_column=COLUMN_DEFAULT, caller_id=None,
                  show_contour_clustered=True, show_contour_raw=True, show_bar=True, remove_outliers=False,
                  cluster_one_name="", cluster_two_name=""):
    """

    :param clustering_method_one: The clustering method we are using for our first clustering method,
    see StringDefinitionsHelper for options
    :param clustering_method_two: The clustering method we are using for our second clustering method,
    see StringDefinitionsHelper for options
    :param clustering_details_one: The details associated with the clustering method we are using for our
    first clustering method, see StringDefinitionsHelper.py and ClusteringHelper.py for details
    :param clustering_details_two: The details associated with the clustering method we are using for our
    second clustering method, see StringDefinitionsHelper.py and ClusteringHelper.py for details
    :param file_name: The name of the file we are reading in relative to the folder of the executable
    :param file_format: The format of the file we are reading in, see StringDefinitionsHelper for options
    :param clustered_column: The name of the type of column we are clustering, default value of Hardness
    :param caller_id: #TODO Eric describe this
    :param show_contour_clustered: A boolean of whether or not to show the final clustered data's contour plot
    :param show_contour_raw: A boolean of whether or not to show the raw data's contour plot
    :param show_bar: A boolean of whether or not to show the bar graph
    :param remove_outliers: A boolean of whether or not to remove outliers
    :param cluster_one_name: How to identify the first cluster for print reports
    :param cluster_two_name: How to identify the second cluster for print reports
    :return: Nothing at the moment

    Reads in all of the data and performs the necessary clustering. It performs the following steps: Reading in the
    data, preprocessing the data, clustering the data, an then analyzing the data. The the respective helper classes
    for more details as to how the processes work.
    """

    print("\n")
    print(str(cluster_one_name))
    print("Clustering Method: " + str(clustering_method_one))
    print("\tClustering Details: ")
    for cluster_param in clustering_details_one:
        print("\t\t" + str(cluster_param) + ": " + str(clustering_details_one[cluster_param]))
    print("\tFile Name: " + str(file_name))
    print("\tFile Format: " + str(file_format))
    print("\tClustering Column: " + str(clustered_column))
    print("\tShow Raw Data: " + str(show_contour_raw))
    print("\tShow Clustered Contour Plot: " + str(show_contour_clustered))
    print("\tShow Bar Graph: " + str(show_bar))
    print("\tRemove Outliers: " + str(remove_outliers))
    print("\n")

    print("\n")
    print(str(cluster_two_name))
    print("Clustering Method: " + str(clustering_method_two))
    print("\tClustering Details: ")
    for cluster_param in clustering_details_two:
        print("\t\t" + str(cluster_param) + ": " + str(clustering_details_two[cluster_param]))
    print("\tFile Name: " + str(file_name))
    print("\tFile Format: " + str(file_format))
    print("\tClustering Column: " + str(clustered_column))
    print("\tShow Raw Data: " + str(show_contour_raw))
    print("\tShow Clustered Contour Plot: " + str(show_contour_clustered))
    print("\tShow Bar Graph: " + str(show_bar))
    print("\tRemove Outliers: " + str(remove_outliers))
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
    clustered_data_one = ClusteringHelper.perform_clustering(data_df=data_df,
                                                             clustering_method=clustering_method_one,
                                                             clustering_details=clustering_details_one)
    clustered_data_two = ClusteringHelper.perform_clustering(data_df=data_df,
                                                             clustering_method=clustering_method_two,
                                                             clustering_details=clustering_details_two)

    # Provide Analysis
    for queue in queues: await queue.put("ANALYZING")
    await asyncio.sleep(WAIT_TIME)
    print("Analyzing Data... ")
    DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df, clustered_data=clustered_data_one,
                                        prop=clustered_column, show_contour_clustered=show_contour_clustered,
                                        show_contour_raw=show_contour_raw, show_bar=show_bar)
    DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df, clustered_data=clustered_data_two,
                                        prop=clustered_column, show_contour_clustered=show_contour_clustered,
                                        show_contour_raw=show_contour_raw, show_bar=show_bar)

    # Gathered from https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html

    cluster_method_one_list = clustered_data_one["Data"].values
    cluster_method_two_list = clustered_data_two["Data"].values
    rand_index = adjusted_rand_score(cluster_method_one_list, cluster_method_two_list)
    print("The rand index is " + str(rand_index) + " between " + str(cluster_one_name) + " and " + str(
        cluster_two_name) + ".")

    for queue in queues:
        await queue.put("COMPLETE")
        print(queue)
    print("Process complete")
    return rand_index
