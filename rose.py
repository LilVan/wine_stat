import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, spearmanr


wine = pd.read_csv('winestyle/Rose.csv')
wine = wine.drop(wine[wine.Year == 'N.V.'].index)

fig = plt.figure(figsize=(10, 6))
sns.barplot(y='Rating', x='Year', data=wine, errorbar=None)

years = len(wine['Year'].unique())
plt.xticks(np.arange(0, years, step=5))
plt.ylim(3, 5)

plt.show()

# statistics
# тест Пирсона
stat, p = pearsonr(wine.Year.astype(int), wine.Rating)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Переменные независимы')
else:
    print('Переменные зависимы')

# тест Спирмана
stat, p = spearmanr(wine.Year.astype(int), wine.Rating)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Переменные независимы')
else:
    print('Переменные зависимы')
