import sys

sys.path.append("../")

from helpers import ClusteringHelper, DataAnalysisHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper, CHI, DBI, SilhouetteCoefficient
from server_files.store import queues
from sklearn.metrics import adjusted_rand_score
import asyncio
from queue import PriorityQueue
import numpy as np

WAIT_TIME = 0.001

COLUMN_DEFAULT = StringDefinitionsHelper.HARDNESS_LABEL


async def execute(clustering_methods_list, clustering_details_list, cluster_names_list,
                  file_name, file_format, clustered_column=COLUMN_DEFAULT, caller_id=None,
                  show_contour_clustered=True, show_contour_raw=True, show_bar=True, remove_outliers=False,
                  save_contour_clustered=False, save_dir="", give_cluster_report=False,
                  print_to_console=False, print_to_text_file=False, text_file_name=""):
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
    :param give_cluster_report: A boolean of whether or not to print out a report of the clusters' details
    :param print_to_console: A boolean of whether or not to print out information to the console
    :param print_to_text_file: A boolean of whether or not to print out information to a text file
    :param text_file_name: The file path to save the text file to
    :return: Nothing at the moment

    Reads in all of the data and performs the necessary clustering. It performs the following steps: Reading in the
    data, preprocessing the data, clustering the data, an then analyzing the data. The the respective helper classes
    for more details as to how the processes work.
    """

    assert len(clustering_methods_list) == len(clustering_details_list) == len(cluster_names_list)

    if print_to_console:
        print("Starting analysis...")
        print("\tFile format: " + str(file_format))
        print("\tFile Name: " + str(file_name))
        print("\tFile Format: " + str(file_format))
        print("\tClustering Column: " + str(clustered_column))
        print("\tShow Raw Data: " + str(show_contour_raw))
        print("\tShow Clustered Contour Plot: " + str(show_contour_clustered))
        print("\tShow Bar Graph: " + str(show_bar))
        print("\tRemove Outliers: " + str(remove_outliers))
        print("\tSave Clustered Contour Plot: " + str(save_contour_clustered))
        print("\tSave Directory: " + str(save_dir))
        print("\tGive Cluster Report: " + str(give_cluster_report))
        print("\n")
        for i in range(len(clustering_methods_list)):
            print(str(cluster_names_list[i]))
            print("Clustering Method: " + str(clustering_methods_list[i]))
            print("\tClustering Details: ")
            for cluster_param in clustering_details_list[i]:
                print("\t\t" + str(cluster_param) + ": " + str(clustering_details_list[i][cluster_param]))
            print("\n")

    if print_to_text_file:
        f = open(text_file_name, "w")
        f.write("Starting analysis...")
        f.write("\n\tFile Name: " + str(file_name))
        f.write("\n\tFile Format: " + str(file_format))
        f.write("\n\tClustering Column: " + str(clustered_column))
        f.write("\n\tShow Raw Data: " + str(show_contour_raw))
        f.write("\n\tShow Clustered Contour Plot: " + str(show_contour_clustered))
        f.write("\n\tShow Bar Graph: " + str(show_bar))
        f.write("\n\tRemove Outliers: " + str(remove_outliers))
        f.write("\n\tSave Clustered Contour Plot: " + str(save_contour_clustered))
        f.write("\n\tSave Directory: " + str(save_dir))
        f.write("\n\tGive Cluster Report: " + str(give_cluster_report))
        f.write("\n")

        for i in range(len(clustering_methods_list)):
            f.write("\n\n")
            f.write(str(cluster_names_list[i]))
            f.write("\nClustering Method: " + str(clustering_methods_list[i]))
            f.write("\n\tClustering Details: ")
            for cluster_param in clustering_details_list[i]:
                f.write("\n\t\t" + str(cluster_param) + ": " + str(clustering_details_list[i][cluster_param]))
            f.write("\n")

    # TODO Specify different parameters to be used, clustering details need dictionary
    # TODO Fix project name in auto docs and readme
    # Read in data
    for queue in queues: await queue.put("READING")
    await asyncio.sleep(WAIT_TIME)
    if print_to_console:
        print("Reading Data... ")
    if print_to_text_file:
        f.write("\nReading Data... ")
    data_df, x_df, y_df = DataCollectionHelper.get_data(file_name, file_format, clustered_column)

    # Pre process the data
    for queue in queues: await queue.put("PREPROCESSING")
    await asyncio.sleep(WAIT_TIME)
    if print_to_console:
        print("PreProcessing Data... ")
    if print_to_text_file:
        f.write("\nPreProcessing Data... ")
    data_df, x_df, y_df = PreProcessingHelper.preprocess_data(data_df=data_df, x_df=x_df, y_df=y_df,
                                                              remove_outliers=remove_outliers)

    # Cluster the data
    for queue in queues: await queue.put("CLUSTERING")
    await asyncio.sleep(WAIT_TIME)
    if print_to_console:
        print("Clustering Data... ")
    if print_to_text_file:
        f.write("\nClustering Data... ")
    list_of_clustered_data = []
    for i in range(len(clustering_methods_list)):
        if print_to_console:
            print("Clustering Data with clustering method: " + str(cluster_names_list[i]))
        if print_to_text_file:
            f.write("\nClustering Data with clustering method: " + str(cluster_names_list[i]))
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

    for queue in queues: await queue.put("Visualizing")
    await asyncio.sleep(WAIT_TIME)
    if print_to_console:
        print("Visualizing Data... ")
    if print_to_text_file:
        f.write("\nVisualizing Data... ")
        f.close()
    for i in range(len(clustering_methods_list)):
        if print_to_console:
            print("\nVisualizing Data with clustering method: " + str(cluster_names_list[i]))
        if print_to_text_file:
            f = open(text_file_name, "a")
            f.write("\n\nVisualizing Data with clustering method: " + str(cluster_names_list[i]))
            f.close()

        DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df,
                                            clustered_data=list_of_clustered_data[i],
                                            prop=clustered_column, show_contour_clustered=show_contour_clustered,
                                            show_contour_raw=show_contour_raw, show_bar=show_bar,
                                            cluster_name=cluster_names_list[i], cluster_iter=i,
                                            save_clustered_contour=save_contour_clustered, save_dir=save_dir,
                                            give_cluster_report=give_cluster_report, print_to_console=print_to_console,
                                            print_to_text_file=print_to_text_file, text_file_name=text_file_name)

    # Setting up the priority queues to store all of the information and sort it
    rand_index_queue = PriorityQueue()
    chi_queue = PriorityQueue()
    dbi_queue = PriorityQueue()
    silhouette_queue = PriorityQueue()

    # For every cluster configuration, calculate the necessary information
    i = 0
    while i < len(clustering_methods_list):
        if len(np.unique(list_of_clustered_data[i]["Data"].values)) <= 1:
            chi_value = np.inf
            dbi_value = np.inf
            silhouette_value = np.inf
        else:
            chi_value = CHI.chi(data_df, list_of_clustered_data[i]["Data"].values)
            dbi_value = DBI.dbi(data_df, list_of_clustered_data[i]["Data"].values)
            silhouette_value = SilhouetteCoefficient.silhouetteCoefficient(data_df,
                                                                           list_of_clustered_data[i]["Data"].values)
        chi_queue.put((chi_value, cluster_names_list[i]))
        dbi_queue.put((dbi_value, cluster_names_list[i]))
        silhouette_queue.put((silhouette_value, cluster_names_list[i]))
        j = i
        # For every other clustering method pair we haven't gotten with this method, calculate the rand index
        while j < len(clustering_methods_list):
            if not i == j:
                cluster_method_one_list = list_of_clustered_data[i]["Data"].values
                cluster_method_two_list = list_of_clustered_data[j]["Data"].values
                rand_index = adjusted_rand_score(cluster_method_one_list, cluster_method_two_list)
                cluster_pair = str(cluster_names_list[i]) + " and " + str(cluster_names_list[j])
                rand_index_queue.put((rand_index, cluster_pair))
            j = j + 1
        i = i + 1

    # Make stacks to put everything in to reverse the order
    rand_index_stack = []
    chi_stack = []
    dbi_stack = []
    silhouette_stack = []

    # Put all the information in stacks
    while not rand_index_queue.empty():
        rand_index_stack.append(str(rand_index_queue.get()))

    while not chi_queue.empty():
        chi_stack.append(str(chi_queue.get()))

    while not dbi_queue.empty():
        dbi_stack.append(str(dbi_queue.get()))

    while not silhouette_queue.empty():
        silhouette_stack.append(str(silhouette_queue.get()))

    # Rand index initial print
    if print_to_text_file:
        f = open(text_file_name, "a")
        f.write("\n\n\nRand Index Values... ")
    if print_to_console:
        print("\n\nRand Index Values... ")

    # Rand index print loop
    while len(rand_index_stack) > 0:
        next_line = str(rand_index_stack.pop())
        if print_to_text_file:
            f.write("\n" + next_line)
        if print_to_console:
            print(next_line)

    # Chi initial print
    if print_to_text_file:
        f.write("\n\n\nCHI Values... ")
    if print_to_console:
        print("\n\nCHI Values... ")

    # Chi values print loop
    while len(chi_stack) > 0:
        next_line = str(chi_stack.pop())
        if print_to_text_file:
            f.write("\n" + next_line)
        if print_to_console:
            print(next_line)

    # DBI initial print
    if print_to_text_file:
        f.write("\n\n\nDBI Values... ")
    if print_to_console:
        print("\n\nDBI Values... ")

    # DBI values print loop
    while len(dbi_stack) > 0:
        next_line = str(dbi_stack.pop())
        if print_to_text_file:
            f.write("\n" + next_line)
        if print_to_console:
            print(next_line)

    # Silhouette initial print
    if print_to_text_file:
        f.write("\n\n\nSilhouette Values... ")
    if print_to_console:
        print("\n\nSilhouette Values... ")

    # Silhouette values print loop
    while len(silhouette_stack) > 0:
        next_line = str(silhouette_stack.pop())
        if print_to_text_file:
            f.write("\n" + next_line)
        if print_to_console:
            print(next_line)

    for queue in queues:
        await queue.put("COMPLETE")
        print(queue)

    # Finishing print
    if print_to_text_file:
        f.write("\nProcess complete")
        f.close()
    if print_to_console:
        print("\n\nProcess complete")
