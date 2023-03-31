import os
# import time
from datetime import datetime


def handle_dir_creation(dir_path):
    if os.path.isdir(dir_path):
        print("The directory " + dir_path +
              " already exists... this should not exist, check your directory structure.")
    else:
        print("The directory " + dir_path + " doesn't exist, creating it now.")
        os.mkdir(dir_path)


curr_dir = os.curdir

testing_cache_dir = curr_dir + "/TestingFilesCache"
handle_dir_creation(testing_cache_dir)

test_counter_tracker = "/TestTracker.txt"
test_counter_tracker_relative_path = testing_cache_dir + test_counter_tracker
print("Testing tracker file path: " + str(test_counter_tracker_relative_path))

if os.path.exists(test_counter_tracker_relative_path):
    test_number_file = open(test_counter_tracker_relative_path, "r")
    file_number = int(test_number_file.read())
    test_number_file.close()
else:
    file_number = 1

test_number_file = open(test_counter_tracker_relative_path, "w")
test_number_file.write(str(file_number + 1))
test_number_file.close()

test_name_dir = "/Test" + str(file_number) + "_" + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
cluster_results_dir = "/ClusterPlots"
rand_index_visualization_dir = "/RandIndexVisualization"
text_file_dir = "/TextFiles"
data_files_dir = "/ClusteredData"

print("Printing all directories to create")
print(curr_dir)
print(testing_cache_dir)
print(test_name_dir)
print(cluster_results_dir)
print(rand_index_visualization_dir)
print(text_file_dir)
print(data_files_dir)
print("")

test_name_dir_relative_path = testing_cache_dir + test_name_dir
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

handle_dir_creation(test_name_dir_relative_path)
handle_dir_creation(cluster_results_dir_relative_path)
handle_dir_creation(rand_index_visualization_dir_relative_path)
handle_dir_creation(text_file_dir_relative_path)
handle_dir_creation(data_files_dir_relative_path)

exit(0)
