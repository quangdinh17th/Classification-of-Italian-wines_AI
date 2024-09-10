# 3 giong ruou vang (3 class), class 1: 59, class 2: 71, class 3: 48
# Tong cong có 178 chai ruou, moi chai rouu có 13 đac trung khac nhau
# Chon 1/178 chai de test, 177 chai de train
# class 3: 13.84,4.12,2.38,19.5,89,1.8,.83,.48,1.56,9.01,.57,1.64,480

import pandas as pd
import numpy as np

columns = ['class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
           'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
           'Color intensity', 'Hue', 'OD280/OD315', 'Proline']

data_wine = pd.read_csv("Program/python/bai3/wine/wine.data", header=None, names=columns)

test_vector = np.array(list(map(float, input("Type input vector test: ").split(','))))

def manhattan_distance(row):
    return np.sum(np.abs(test_vector - row[1:]))  # Bỏ qua cột 'class'

# Tính khoảng cách Manhattan cho tất cả các hàng dữ liệu
data_wine['distance'] = data_wine.apply(manhattan_distance, axis=1)

# In ra tất cả khoảng cách
print("Khoảng cách từ vector test đến từng hàng:")
print(data_wine[['class', 'distance']])

# Tìm hàng có khoảng cách nhỏ nhất
nearest_row = data_wine.loc[data_wine['distance'].idxmin()]

# In kết quả
print(f"\nKết quả: Vector test thuộc class {nearest_row['class']} với khoảng cách nhỏ nhất là {nearest_row['distance']:.2f}")

