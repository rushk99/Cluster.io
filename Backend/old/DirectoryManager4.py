import os
# import time
from datetime import datetime
from helpers import StringDefinitionsHelper


def create_necessary_directories(cluster_results_dir=StringDefinitionsHelper.CLUSTER_RESULTS_DIR,
                                 rand_index_visualization_dir=StringDefinitionsHelper.RAND_INDEX_VISUALIZATION_DIR,
                                 text_file_dir=StringDefinitionsHelper.TEXT_FILE_DIR,
                                 data_files_dir=StringDefinitionsHelper.DATA_FILES_DIR):
    """

    :param cluster_results_dir: The directory to save the clustering results in
    :param rand_index_visualization_dir: The directory to save the rand index visualization in
    :param text_file_dir: The directory to save any text files in
    :param data_files_dir: The directory to save any data files in
    :return: Nothing

    Sets up the directories necessary for saving information while completing the clustering.

    """

    # Find where we currently are
    curr_dir = os.curdir

    # Generate the absolute path for the testing files folder which stores all tests
    testing_cache_dir = curr_dir + "/TestingFilesCache"
    handle_dir_creation(testing_cache_dir)

    # Generate information for the file which is responsible for keeping track of the test number
    test_counter_tracker = "/TestTracker.txt"
    test_counter_tracker_relative_path = testing_cache_dir + test_counter_tracker
    print("Testing tracker file path: " + str(test_counter_tracker_relative_path))

    # Increase number by one if a text file exists, generate one if it doesn't
    if os.path.exists(test_counter_tracker_relative_path):
        test_number_file = open(test_counter_tracker_relative_path, "r")
        file_number = int(test_number_file.read())
        test_number_file.close()
    else:
        file_number = 1

    # Write over the file to increment
    test_number_file = open(test_counter_tracker_relative_path, "w")
    test_number_file.write(str(file_number + 1))
    test_number_file.close()

    # Generate a directory which stores a test number and a date to show when it was created
    test_name_dir = "/Test" + str(file_number) + "_" + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

    # Shows a list of all directories which are being used and created
    print("Printing all directories to create")
    print(curr_dir)
    print(testing_cache_dir)
    print(test_name_dir)
    print(cluster_results_dir)
    print(rand_index_visualization_dir)
    print(text_file_dir)
    print(data_files_dir)
    print("")

    # Generates all relative paths
    test_name_dir_relative_path = testing_cache_dir + test_name_dir
    cluster_results_dir_relative_path = test_name_dir_relative_path + cluster_results_dir
    rand_index_visualization_dir_relative_path = test_name_dir_relative_path + rand_index_visualization_dir
    text_file_dir_relative_path = test_name_dir_relative_path + text_file_dir
    data_files_dir_relative_path = test_name_dir_relative_path + data_files_dir

    # Displays relative paths
    print("Printing all directories to create from their relative path")
    print(test_name_dir_relative_path)
    print(cluster_results_dir_relative_path)
    print(rand_index_visualization_dir_relative_path)
    print(text_file_dir_relative_path)
    print(data_files_dir_relative_path)
    print("")

    # Creates the directories at the relative paths
    handle_dir_creation(test_name_dir_relative_path)
    handle_dir_creation(cluster_results_dir_relative_path)
    handle_dir_creation(rand_index_visualization_dir_relative_path)
    handle_dir_creation(text_file_dir_relative_path)
    handle_dir_creation(data_files_dir_relative_path)


def handle_dir_creation(dir_path):
    """
    :param dir_path: The directory path to create a directory for
    :return: Nothing

    Creates the specified directory. This serves as a helper function for create_necessary_directories

    """

    # If the path already exists...
    if os.path.isdir(dir_path):
        # Check to make sure it isn't TestingFilesCache as this is expected all but one times
        if dir_path != "./TestingFilesCache":
            print("The directory " + dir_path +
                  " already exists... this should not exist, check your directory structure.")
    else:
        if dir_path != "./TestingFilesCache":
            print("The directory " + dir_path + " doesn't exist, creating it now.")
        else:
            # Identifying this is the first setup, may be useful in the future
            print("The root testing data directory doesn't exist, creating it now.")
        # If it doesn't exist then make it
        os.mkdir(dir_path)


create_necessary_directories(cluster_results_dir=StringDefinitionsHelper.CLUSTER_RESULTS_DIR,
                             rand_index_visualization_dir=StringDefinitionsHelper.RAND_INDEX_VISUALIZATION_DIR,
                             text_file_dir=StringDefinitionsHelper.TEXT_FILE_DIR,
                             data_files_dir=StringDefinitionsHelper.DATA_FILES_DIR)

exit(0)
