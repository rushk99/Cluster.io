import pandas as pd
import numpy as np
import uuid

data = [1, 2, 3, 4, 5]
data_df = pd.DataFrame(data, columns=["Data"])
print(data_df)
data_df[data_df["Data"] > 3] = np.nan
print(data_df)

print(data_df["Data"].count())
print(data_df.count(numeric_only=True))
print(data_df.count(numeric_only=False))

print(np.linspace(1, 100, 100))

print(uuid.uuid4())

exit(0)
