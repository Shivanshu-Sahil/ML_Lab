import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

print("ML Lab Ready")

my_tuple = (10, 20, 30)
my_list = [10, 20, 30, 40]
my_set = {10, 20, 30, 30}
my_dict = {"A": 10, "B": 20, "C": 30}

print("Tuple:", my_tuple)
print("List:", my_list)
print("Set:", my_set)
print("Dictionary:", my_dict)

data = np.array(my_list)
print("\nNumPy Mean:", np.mean(data))

df = pd.DataFrame({
    "Values": data
})

print("\nPandas DataFrame:")
print(df)

mean = np.mean(data)
std = np.std(data)
z_scores = stats.zscore(data)

print("\nMean:", mean)
print("Standard Deviation:", std)
print("Z-Scores:", z_scores)

plt.plot(data)
plt.title("Simple Line Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
