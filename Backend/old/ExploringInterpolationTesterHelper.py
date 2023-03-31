import pandas as pd
import matplotlib.pyplot as plt
import random
from helpers import RemoveOutliers

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

RemoveOutliers.remove_data_from_outliers(data_df=hard_df, x_df=x_df, y_df=y_df, show_plots=True, show_extra_plots=True)

exit(0)
