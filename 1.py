# 1) Провести дисперсионный анализ для определения того, есть ли различия среднего 
# роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np 
import scipy.stats as stats
from scipy.stats import bartlett
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd


x = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
z = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

print(stats.shapiro(x))
print(stats.shapiro(y))
print(stats.shapiro(z))
#распределение нормальное (pvalio > a)

print(bartlett(x, y, z))
#дисперсия однородная (pvalio > a)

print(stats.f_oneway(x, y, z))
#есть статистические различия (pvalio < a)

max_1 = max(len(x), len(y), len(z))
if max_1 > len(x):
    while max_1 > len(x):
        k = max_1 - len(x)
        p = np.mean(x)
        x = np.append(x, p)
if max_1 > len(y):
    while max_1 > len(y):
        k = max_1 - len(y)
        p = np.mean(y)
        y = np.append(y, p)
else:
    while max_1 > len(z):
        k = max_1 - len(z)
        p = np.mean(z)
        z = np.append(z, p)
  
print('x =', len(x), 'y =', len(y), 'z =', len(z))
df = pd.DataFrame({'height': list(np.hstack([x, y, z])),'group': np.repeat(['x', 'y', 'z'], repeats=11)})
tukey=pairwise_tukeyhsd(df['height'], df['group'], alpha =0.05)
print(tukey)
# между футболистами и хоккеистами по росту нет различий
