import sys

from matplotlib import pyplot as plt
import matplotlib.cm as cm
from sklearn.metrics import silhouette_score, silhouette_samples
from functools import reduce

sys.path.append("../")
from sklearn.cluster import AgglomerativeClustering, Birch, DBSCAN, KMeans, OPTICS, SpectralClustering

from helpers import ClusteringHelper, DataAnalysisHelper, DataCollectionHelper, PreProcessingHelper, \
    StringDefinitionsHelper
import asyncio
import math
import numpy as np
import pandas as pd

WAIT_TIME = 0.001

COLUMN_DEFAULT = StringDefinitionsHelper.HARDNESS_LABEL


async def execute(file_name, file_format, clustered_column=COLUMN_DEFAULT, k_min=2, k_max=5,
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
    cluster_labels_for_k = {}
    clusterer_for_k = {}
    k = k_min
    while k <= k_max:
        print("Clustering Data with " + str(k) + " clusters ... ")
        k_means = KMeans(n_clusters=k, random_state=0)
        fit = k_means.fit(data_df.copy()["Data"].values.reshape(-1, 1))
        cluster_labels = k_means.fit_predict(data_df.copy()["Data"].values.reshape(-1, 1))
        print(cluster_labels)
        # print(fit)
        cluster_labels_for_k[k] = cluster_labels
        clusterer_for_k[k] = k_means
        cluster_means = []

        for item in fit.cluster_centers_:
            cluster_means.append(item[0])

        cluster_means_arr = np.array(cluster_means)
        cluster_means_arr.sort()

        def closest(curr_val):
            idx = (np.abs(cluster_means_arr - curr_val)).argmin()
            return idx

        k_means_results = []
        for i in range(data_df.copy()["Data"].values.size):
            # For every value add the cluster it belongs to into the k_means_results array
            k_means_results.append(closest(curr_val=data_df.copy()["Data"].values[i]))

        clustering_results_df = pd.DataFrame(k_means_results)
        clustering_results_df.columns = ["Data"]
        k = k + 1
        print(clustering_results_df)
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
    k = k_min
    silhouette_avg_for_k = {}
    while k <= k_max:
        print("Performing Silhouette Method for " + str(k) + " clusters ... ")
        silhouette_avg = silhouette_score(data_df.copy()["Data"].values.reshape(-1, 1), cluster_labels_for_k.get(k))
        silhouette_avg_for_k[k] = silhouette_avg
        print("For n_clusters =", k,
              "The average silhouette_score is :", silhouette_avg)
        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(data_df.copy()["Data"].values.reshape(-1, 1), cluster_labels_for_k.get(k))

        fig, ax1 = plt.subplots(1, 1)
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, len(data_df.copy()["Data"].values.reshape(-1, 1)) + (k + 1) * 10])

        y_lower = 10
        for i in range(k):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[cluster_labels_for_k.get(k) == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / k)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                      "with n_clusters = %d" % k),
                     fontsize=14, fontweight='bold')
        plt.show()
        k = k + 1

    best_k = reduce(lambda key, max: key if silhouette_avg_for_k.get(key) > silhouette_avg_for_k.get(max) else max, silhouette_avg_for_k.keys())
    print("The optimal number of clusters based on their silhouette coefficients are", best_k)

    exit(0)


if __name__ == "__main__":
    file_name = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444.xlsx"
    file_format = StringDefinitionsHelper.FILE_FORMAT_TWO
    asyncio.run(execute(file_name=file_name, file_format=file_format))
