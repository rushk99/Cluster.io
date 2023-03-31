import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import interpolate

file_path = "../data/01NOV2019_600degF-5min-Austempering_BCS-1444_small.xlsx"
sheet_name = "Test 1"
use_cols = "A:C"
hard_col_name = "HARDNESS"
x_col_name = "X Position"
y_col_name = "Y Position"
NUM_HIST_BINS = 200
nulls = False

xls = pd.ExcelFile(file_path)

if nulls:
    test1_sheet = pd.read_excel(xls, sheet_name, usecols=use_cols).iloc[:-1]
else:
    test1_sheet = pd.read_excel(xls, sheet_name, usecols=use_cols).dropna()

# If skip_first_row then read every row after the first, otherwise read them all
# The hardness values
hardness_column = test1_sheet[hard_col_name]
# The x values
x_column = test1_sheet[x_col_name]
# The y values
y_column = test1_sheet[y_col_name]
# The stiffness column
# Asserts that the columns have values
assert hardness_column is not None
assert x_column is not None
assert y_column is not None

hard_df = pd.DataFrame(hardness_column)
x_df = pd.DataFrame(x_column)
y_df = pd.DataFrame(y_column)

# Renames columns of all read data for consistency
hard_df = hard_df.rename(columns={hard_col_name: "Data"})
x_df = x_df.rename(columns={x_col_name: "Data"})
y_df = y_df.rename(columns={y_col_name: "Data"})

# Makes all read data numeric
hard_df["Data"] = pd.to_numeric(hard_df["Data"], downcast="float")
x_df["Data"] = pd.to_numeric(x_df["Data"], downcast="float")
y_df["Data"] = pd.to_numeric(y_df["Data"], downcast="float")

r = random.random()
b = random.random()
g = random.random()
color = (r, g, b)

plt.hist(hard_df["Data"].values, bins=100, color=color)  # "darkred"
plt.title("Hardness Values vs Number of Occurrences")
plt.xlabel("Hardness Values")
plt.ylabel("Number of Occurrences")
plt.show()


def complete_interpolation(data_list, x_df, y_df, method):

    """

    :param data_list: A list of data we are interpolating
    :param x_df: A DataFrame containing all x values
    :param y_df: A DataFrame containing all y values
    :param method: The method we are using to interpolate. This is based on the interpolate.griddata method so refer
        to their documentation. We typically use 'cubic' and then 'nearest'.

    :return: A 1D array of interpolated results

    This method will attempt to interpolate any and all null values in a list of data. It will then
    return the product of the interpolation process. This is not guaranteed to fill in all null values.

    """

    data_2d = data_list.reshape(len(np.unique(x_df)), len(np.unique(y_df)))

    # For every invalid value that exists, mark it as being invalid
    masked_data_2d = np.ma.masked_invalid(data_2d)

    # All possible points
    all_x_values = np.reshape(x_df["Data"].values, (100, 100))
    all_y_values = np.reshape(y_df["Data"].values, (100, 100))

    # This value will be false in every cell that needs to be replaced
    data_2d_mask = ~masked_data_2d.mask

    # Get only the valid values
    null_x_values = all_x_values[data_2d_mask]
    null_y_values = all_y_values[data_2d_mask]

    # Get all of the valid values
    unmasked_data_2d = masked_data_2d[data_2d_mask]

    # Complete the interpolation and get a grid result back
    interpolated_grid = interpolate.griddata((null_x_values, null_y_values), unmasked_data_2d,
                                             (all_x_values, all_y_values), method=method)

    # Return the grid reshaped into a 1D array
    return interpolated_grid.reshape(-1, 1)


data_1d = hard_df.copy()["Data"].values

# Remove outliers
mean_val = np.mean(data_1d)
stddev_val = np.std(data_1d)
z_scores = 3
data_1d[abs(data_1d - mean_val) > stddev_val * z_scores] = np.nan

grid_result_one = complete_interpolation(data_list=data_1d, x_df=x_df, y_df=y_df, method="cubic")
grid_result_two = complete_interpolation(data_list=grid_result_one, x_df=x_df, y_df=y_df, method="nearest")

hard_df = pd.DataFrame(grid_result_two, columns=["Data"])

r = random.random()
b = random.random()
g = random.random()
color = (r, g, b)

plt.hist(hard_df["Data"].values, bins=100, color=color)  # "darkred"
plt.title("Cleaned Hardness Values vs Number of Occurrences")
plt.xlabel("Hardness Values")
plt.ylabel("Number of Occurrences")
plt.show()

exit(0)
