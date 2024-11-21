# BTVN: các phép tính cơ bản của ma trận với số và của ma trận với ma trận
import numpy as np

# Tạo ma trận
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Các phép toán
C = A + B
D = A - B
E = 2 * A
F = np.dot(A, B)

# In kết quả
print("A + B = \n", C)
print("A - B = \n", D)
print("2 * A = \n", E)