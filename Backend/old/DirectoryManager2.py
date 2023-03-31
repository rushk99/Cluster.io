import os
import sys

curr_dir = os.curdir
test_name_dir = "/Test01"
cluster_results_dir = "/ClusterPlots"
rand_index_visualization_dir = "/RandIndexVisualization"
text_file_dir = "/TextFiles"
data_files_dir = "/ClusteredData"

print("Printing all directories to create")
print(curr_dir)
print(test_name_dir)
print(cluster_results_dir)
print(rand_index_visualization_dir)
print(text_file_dir)
print(data_files_dir)
print("")

test_name_dir_relative_path = curr_dir + test_name_dir
cluster_results_dir_relative_path = test_name_dir_relative_path + cluster_results_dir
rand_index_visualization_dir_relative_path = test_name_dir_relative_path + rand_index_visualization_dir
text_file_dir_relative_path = test_name_dir_relative_path + text_file_dir
data_files_dir_relative_path = test_name_dir_relative_path + data_files_dir

print("Printing all directories to create from their relative path")
print(test_name_dir_relative_path)
print(cluster_results_dir_relative_path)
print(rand_index_visualization_dir_relative_path)
print(text_file_dir_relative_path)
print(data_files_dir_relative_path)
print("")

if os.path.isdir(test_name_dir_relative_path):
    print("The directory " + test_name_dir_relative_path +
          " already exists... this should not exist, check your directory structure.")
else:
    print("The directory " + test_name_dir_relative_path +  " doesn't exist, creating it now.")
    os.mkdir(test_name_dir_relative_path)


if os.path.isdir(cluster_results_dir_relative_path):
    print("The directory " + cluster_results_dir_relative_path +
          " already exists... this should not exist, check your directory structure.")
else:
    print("The directory " + cluster_results_dir_relative_path + " doesn't exist, creating it now.")
    os.mkdir(cluster_results_dir_relative_path)

if os.path.isdir(rand_index_visualization_dir_relative_path):
    print("The directory " + rand_index_visualization_dir_relative_path +
          " already exists... this should not exist, check your directory structure.")
else:
    print("The directory " + rand_index_visualization_dir_relative_path + " doesn't exist, creating it now.")
    os.mkdir(rand_index_visualization_dir_relative_path)

if os.path.isdir(text_file_dir_relative_path):
    print("The directory " + text_file_dir_relative_path +
          " already exists... this should not exist, check your directory structure.")
else:
    print("The directory " + text_file_dir_relative_path + " doesn't exist, creating it now.")
    os.mkdir(text_file_dir_relative_path)

if os.path.isdir(data_files_dir_relative_path):
    print("The directory " + data_files_dir_relative_path +
          " already exists... this should not exist, check your directory structure.")
else:
    print("The directory " + data_files_dir_relative_path + " doesn't exist, creating it now.")
    os.mkdir(data_files_dir_relative_path)

exit(0)
