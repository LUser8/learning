import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]]])
print(a, a.ndim)
print(b, b.ndim)
print(c, c.ndim)
print(d, d.ndim)

# create n dim array
e = np.array([1, 2, 3, 4], ndmin=5)
print(e, e.ndim)