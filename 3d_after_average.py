import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = [0,0,1,2,2,2,2,4] #servo1 40 degree
data1 = [4,3,3,3,3,3,3,3,4] # 50 degree
data2 = [6,6,6,6,6,6,10,8,6] # 60 degree
data3 = [6,6,6,9,6,12,10,14,16] # 70 degree
data4 = [14,12,11,10,9,10,10,11,12] # 80 degree
data5 = [10,10,9,9,8,8,8,8,8] # 90 degree
data6 = [8,8,8,8,8,8,8,9,9] # 100 degree
data7 = [17,23,26,19,15,11,10,11,9] # 110 degree
data8 = [8,7,7,8,8,15,21,15,14] # 120 degree
data9 = [10,8,7,6,5,5,5,5,5] # 130 degree
data10 = [4,4,4,4,4,4,4,4,3] # 140 degree
data11 = [3,3,3,3,3,3,3,3,3] # 150 degree

rata_rata = sum(data) / len(data)
rata_rata1 = sum(data1) / len(data1)
rata_rata2 = sum(data2) / len(data2)
rata_rata3 = sum(data3) / len(data3)
rata_rata4 = sum(data4) / len(data4)
rata_rata7 = sum(data5) / len(data5)
rata_rata8 = sum(data6) / len(data6)
rata_rata5 = sum(data7) / len(data7)
rata_rata6 = sum(data8) / len(data8)
rata_rata9 = sum(data9) / len(data9)
rata_rata10 = sum(data10) / len(data10)
rata_rata11 = sum(data11) / len(data11)

# Data
data = [
    (0, 40, rata_rata), (5, 40, rata_rata), (10, 40, rata_rata), (15, 40, rata_rata), (20, 40, rata_rata), (25, 40, rata_rata), (30, 40, rata_rata), (35, 40, rata_rata),
    (0, 50, rata_rata1),(0, 50, rata_rata1),(5, 50, rata_rata1),(10, 50, rata_rata1),(15, 50, rata_rata1),(20, 50, rata_rata1),(25, 50, rata_rata1),(30, 50, rata_rata1),(35, 50, rata_rata1),
    (0, 60, rata_rata2), (0, 60, rata_rata2), (5, 60, rata_rata2), (10, 60, rata_rata2), (15, 60, rata_rata2), (20, 60, rata_rata2), (25, 60, rata_rata2), (30, 60, rata_rata2), (35, 60, rata_rata2),
    (0, 70, rata_rata3), (0, 70, rata_rata3), (5, 70, rata_rata3), (10, 70, rata_rata3), (15, 70, rata_rata3), (20, 70, rata_rata3), (25, 70, rata_rata3), (30, 70, rata_rata3), (35, 70, rata_rata3),
    (0, 80, rata_rata4), (0, 80, rata_rata4), (5, 80, rata_rata4), (10, 80, rata_rata4), (15, 80, rata_rata4), (20, 80, rata_rata4), (25, 80, rata_rata4), (30, 80, rata_rata4), (35, 80, rata_rata4),
    (0, 90, rata_rata5), (0, 90, rata_rata5), (5, 90, rata_rata5), (10, 90, rata_rata5), (15, 90, rata_rata5), (20, 90, rata_rata5), (25, 90, rata_rata5), (30, 90, rata_rata5), (35, 90, rata_rata5),
    (0, 100, rata_rata6), (0, 100, rata_rata6), (5, 100, rata_rata6), (10, 100, rata_rata6), (15, 100, rata_rata6), (20, 100, rata_rata6), (25, 100, rata_rata6), (30, 100, rata_rata6), (35, 100, rata_rata6),
    (0, 110, rata_rata7), (0, 110, rata_rata7), (5, 110, rata_rata7), (10, 110, rata_rata7), (15, 110, rata_rata7), (20, 110, rata_rata7), (25, 110, rata_rata7), (30, 110, rata_rata7), (35, 110, rata_rata7),
    (0, 120, rata_rata8), (0, 120, rata_rata8), (5, 120, rata_rata8), (10, 120, rata_rata8), (15, 120, rata_rata8), (20, 120, rata_rata8), (25, 120, rata_rata8), (30, 120, rata_rata8), (35, 120, rata_rata8),
    (0, 130, rata_rata9), (0, 130, rata_rata9), (5, 130, rata_rata9), (10, 130, rata_rata9), (15, 130, rata_rata9), (20, 130, rata_rata9), (25, 130, rata_rata9), (30, 130, rata_rata9), (35, 130, rata_rata9),
    (0, 140, rata_rata10), (0, 140, rata_rata10), (5, 140, rata_rata10), (10, 140, rata_rata10), (15, 140, rata_rata10), (20, 140, rata_rata10), (25, 140, rata_rata10), (30, 140, rata_rata10), (35, 140, rata_rata10),
    (0, 150, rata_rata11), (0, 150, rata_rata11), (5, 150, rata_rata11), (10, 150, rata_rata11), (15, 150, rata_rata11), (20, 150, rata_rata11), (25, 150, rata_rata11), (30, 150, rata_rata11), (35, 150, rata_rata11),
]

# Extracting x, y, and z values
x = [item[1] for item in data]
y = [item[0] for item in data]
z = [item[2] for item in data]

X, Y = np.meshgrid(np.unique(x), np.unique(y))
Z = np.zeros_like(X)

# Populate Z values based on the provided data
for i in range(len(data)):
    xi = data[i][1]
    yi = data[i][0]
    zi = data[i][2]
    idx_x = np.where(np.unique(x) == xi)[0][0]
    idx_y = np.where(np.unique(y) == yi)[0][0]
    Z[idx_y, idx_x] = zi

# Plotting the 3D contour plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D With Kalman Filter')

plt.show()
