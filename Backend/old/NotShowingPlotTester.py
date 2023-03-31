import matplotlib.pyplot as plt
import numpy as np

# How to remove data from a file

x_data1 = np.random.uniform(0, 1, 100)
x_data2 = np.random.uniform(0, 1, 100)
# fig, axes = plt.subplots(17, 30, figsize=(360, 214))
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for axes_1d in axes:
    for ax in axes_1d:
        ax.hist(np.random.uniform(0, 1, 100))
        ax.set_title("Hi There")

# ax[0, 1].hist(x_data2)
# ax[1, 0].hist(x_data1)
# plt.close()
# ax[1, 1].hist(x_data2)
plt.show()
# plt.savefig("BigPlots3.png")

exit(0)
