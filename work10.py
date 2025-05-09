import pandas as pd
import numpy as np

# 1. Создать объект pandas Series из листа, объекта NumPy, и словаря

lst = pd.Series([1, 2, 3, 4, 5])
print(lst)

nmpy_arr = np.arange(5)
nmpy_series = pd.Series(nmpy_arr)
print(nmpy_series)

fname_dict = {'Egor': 493110130003,
              'Lev': 493110230002,
              'Masha': 493110130001,
              'Fedya': 493110130002,
              'Sasha': 493110230003}
fname = pd.Series(fname_dict)
print('fname:')
print(fname)

# 2. Получить не пересекающиеся элементы в двух объектах Series
sr1 = pd.Series([10, 20, 30, 40, 50])

sr2 = pd.Series([40, 50, 60, 70, 80])

s_union = pd.Series(np.union1d(sr1, sr2))

s_intersect = pd.Series(np.intersect1d(sr1, sr2))

ans = s_union[~s_union.isin(s_intersect)]

ans2 = np.setxor1d(sr1, sr2, assume_unique=False)

print(ans)

# 3. Узнать частоту уникальных элементов объекта Series (гистограмма)

data = 'абвгдеёжз'
len_sr = 40
sr = pd.Series(np.take(list(data), np.random.randint(len(data), size=len_sr)))

ans = sr.value_counts()

print(ans)

# 4. Объединить два объекта Series вертикально и горизонтально

sr1 = pd.Series(list('АБВГДЕЁЖЗИЙКЛМНОПРСТ'))
sr2 = pd.Series(np.arange(20))

df = pd.DataFrame({'буквы': sr1, 'расположение': sr2})

print(df)

# 5. Найти разность между объектом Series и смещением объекта Series на n
n = 2

sr = pd.Series([1, 3, 7, 14, 17, 21, 46, 12, 67, 98])

ans = sr.diff(periods=n)

print(ans)
