import pandas as pd

df_to_save = pd.DataFrame(columns=["X", "Y"])

x_vals = list(range(1, 26))
y_vals = list(range(1, 26))
y_vals.reverse()

for x in x_vals:
    for y in y_vals:
        df_to_save = df_to_save.append({"X": x, "Y": y}, ignore_index=True)

print(df_to_save)

df_to_save.to_excel("x_and_y_6-30-2021.xlsx")


exit(0)
