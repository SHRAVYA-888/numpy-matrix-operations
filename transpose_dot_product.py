import numpy as np

C = np.array([[1, 2],
              [3, 4],
              [5, 6]])

C_T = C.T
dot_product = np.dot(C_T, C)

print("Transpose:")
print(C_T)

print("Dot product:")
print(dot_product)
