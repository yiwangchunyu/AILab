import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
res = pd.read_csv('data/performence.csv', index_col='N')
res['time'].plot()
plt.show()
print(res)
# x=np.arange(0,20,0.01)
# y=[math.sin(i) + 0.1*i for i in x]
# plt.plot(x,y)
# plt.show()