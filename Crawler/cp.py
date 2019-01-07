#%%
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pandas as pd
import re
import csv

data=[]
with open('./DATA/cpu.csv', newline='') as csvfile:
    compare = csv.DictReader(csvfile)
    for i in compare:
        a=[i['price'],float(i['userbenchmark'])]
        data.append(a)

#%%
p = pd.DataFrame(columns=['price', 'userbenchmark'], data= data)
sns.lmplot(x='price', y='userbenchmark', data = p,fit_reg=False, size=15)
plt.savefig("filename.png")


#%%
