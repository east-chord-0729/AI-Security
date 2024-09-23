"""
numpy 모듈 기초

numpy는 다차원 배열을 효과적으로 처리하는 모듈이다.
핵심은 축의 개념.
"""

import numpy as np
import numpy.random as npr

# create 1D array and reshape to 2D array
a = np.arange(15).reshape(3, 5)

print("\n=====")
print("array.......\n", a)
print("shape.......", a.shape)
print("dim.........", a.ndim)
print("itemsize....", a.itemsize)
print("size........", a.size)
print("data type...", a.dtype)

# create 1D array
a = np.array([1, 2, 3, 4, 5, 6])

print("\n=====")
print("array.......\n", a)
print("shape.......", a.shape)
print("dim.........", a.ndim)
print("itemsize....", a.itemsize)
print("size........", a.size)
print("data type...", a.dtype)

# initialize array
a = np.zeros((3, 4))
b = np.linspace(0, 50, 5)

print("\n=====")
print("zero array.........\n", a)
print("line space array...\n", b)

# generate random variable
a = np.random.randint(5)
a = np.random.rand(8)
a = np.random.rand(8, 2)
a = np.random.randn(6)
a = np.random.randn(3, 4)

print("\n=====")
print("randint...\n", a)

# compute arithmatic operation
a = np.array([1, 2, 3]) # first operand
b = np.array([1, 2, 3]) # second operand
c = np.add(a, b)
