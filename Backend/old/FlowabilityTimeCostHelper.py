import numpy as np

counter = 0

for pow1 in range(0, 31):
    for val1 in np.arange(0.2, 1, 0.2):
        for pow2 in range(pow1 + 1, 31):
            for val2 in np.arange(0.2, 1 - val1, 0.2):
                for pow3 in range(pow2 + 1, 31):
                    counter = counter + 1

print(counter)

exit(0)
