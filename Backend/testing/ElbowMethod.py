import sys

sys.path.append("../")
from sklearn.cluster import AgglomerativeClustering, Birch, DBSCAN, KMeans, OPTICS, SpectralClustering
import matplotlib.pyplot as plt

from helpers import ClusteringHelper, DataAnalysisHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper
import asyncio
import math
import numpy as np
import pandas as pd

WAIT_TIME = 0.001

COLUMN_DEFAULT = StringDefinitionsHelper.HARDNESS_LABEL


async def execute(file_name, file_format, clustered_column=COLUMN_DEFAULT, k_min=1, k_max=10,
                  show_contour_clustered=True, show_contour_raw=True, show_bar=True, remove_outliers=False):
    """

    StringDefinitionsHelper
    :param file_name: The name of the file we are reading in relative to the folder of the executable
    :param file_format: The format of the file we are reading in, see StringDefinitionsHelper for options
    :param clustered_column: The name of the type of column we are clustering, default value of Hardness
    :param k_min The min amount of clusters to have
    :param k_max The max amount of clusters to have
    :param show_contour_clustered: A boolean of whether or not to show the final clustered data's contour plot
    :param show_contour_raw: A boolean of whether or not to show the raw data's contour plot
    :param show_bar: A boolean of whether or not to show the bar graph
    :param remove_outliers: A boolean of whether or not to remove outliers
    :return: Nothing at the moment

    Reads in all of the data and performs the necessary clustering. It performs the following steps: Reading in the
    data, preprocessing the data, clustering the data, an then analyzing the data. The the respective helper classes
    for more details as to how the processes work.
    """

    # Read in data
    print("Reading Data... ")
    data_df, x_df, y_df = DataCollectionHelper.get_data(file_name, file_format, clustered_column)

    # Pre process the data
    print("PreProcessing Data... ")
    data_df, x_df, y_df = PreProcessingHelper.preprocess_data(data_df=data_df, x_df=x_df, y_df=y_df,
                                                              remove_outliers=remove_outliers)

    clustered_data_sets = []
    clustered_data_centers = []
    k = k_min
    within_square_sum = []
    while k <= k_max:
        within_square_sum.append(0.0)
        print("Clustering Data with " + str(k) + " clusters ... ")
        k_means = KMeans(n_clusters=k, random_state=0).fit(data_df.copy()["Data"].values.reshape(-1, 1))
        cluster_means = []

        for item in k_means.cluster_centers_:
            cluster_means.append(item[0])

        cluster_means_arr = np.array(cluster_means)
        cluster_means_arr.sort()

        def closest(curr_val):
            within_square_sum[k - k_min] = within_square_sum[k - k_min] + min(np.abs(cluster_means_arr - curr_val))
            idx = (np.abs(cluster_means_arr - curr_val)).argmin()
            return idx

        k_means_results = []
        for i in range(data_df.copy()["Data"].values.size):
            # For every value add the cluster it belongs to into the k_means_results array
            k_means_results.append(closest(curr_val=data_df.copy()["Data"].values[i]))

        clustering_results_df = pd.DataFrame(k_means_results)
        clustering_results_df.columns = ["Data"]
        k = k + 1
        clustered_data_sets.append(clustering_results_df)
        clustered_data_centers.append(cluster_means_arr)

    # print(clustered_data_sets)
    # print(clustered_data_centers)

    # Provide Analysis
    print("Analyzing Data... ")
    k = k_min
    while k <= k_max:
        print("Analyzing Data with " + str(k) + " clusters ... ")
        clustered_data = clustered_data_sets[k - k_min]
        DataAnalysisHelper.perform_analysis(data_df=data_df, x_df=x_df, y_df=y_df, clustered_data=clustered_data,
                                            prop=clustered_column, show_contour_clustered=show_contour_clustered,
                                            show_contour_raw=show_contour_raw, show_bar=show_bar)
        k = k + 1

    # TODO Your clustering analysis method here
    print(within_square_sum)
    k_values = range(k_min, k_max + 1)
    # print(cluster_fractions)
    plt.plot(k_values, within_square_sum, '--ro')
    # TODO I would like to revisit how we are making this bar graph, I don't like the width being a set amount
    # TODO I would also like to see if it is possible to make the bar graph only use integer values for it's x values
    plt.title("Within-Cluster-Sum of Squared Errors (WSS) Vs Number of Clusters")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Within-Cluster-Sum of Squared Errors (WSS)")
    plt.show()
    exit(0)


if __name__ == "__main__":
    file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
    file_format = StringDefinitionsHelper.FILE_FORMAT_TWO
    asyncio.run(execute(file_name=file_name, file_format=file_format))
