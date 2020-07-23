# Numpy

[Cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)

## Basic Numpy

import numpy as np

### Create array

# empty array np.empty(<shape>)
np.empty((3,2))

# np.linspace(start, stop, len)
# similar to R: seq(from, to, by)
print(
    np.linspace(1, 5, 5),
    np.linspace(1, 5, 3),
    sep = '\n')

# np.arange(start, stop, step)
# equivalent to R: seq(from, to, by)
print(
    np.arange(5),        # stop
    np.arange(1, 5),     # start, stop
    np.arange(1, 6, 2),  # start, stop, step
    sep = '\n'
)

# random array
print(
    np.random.rand(),
    np.random.rand(3, 5),
    np.random.rand(3, 5, 1),
    sep = '\n\n'
)

# create array from tuple or list
a = np.array([(1,2,3), 
              (4,5,6)],
             dtype = float)
print(a)
print(type(a), type(a[0,0]))

#### Changing Shape

print(a.shape)
a.shape = (3, 2)
print(a.shape)
a

## Common Functions

### Arithmetic

a = np.array([1,2,3], dtype=float)
b = np.array([4,5,6], dtype=float)
print(
    a + b,
    a / b,
    a * 3,
    a.dot(b),  # dot product
    a @ b,     # dot product
    np.sin(a),
    sep = '\n\n')

### Logarithm & Exponential

Numpy doesn't have log function for arbitrary base, so use the rule: $log_b a = \frac{log_x a}{log_x b}$.

# log with base 2
np.isclose(
    np.log2(a), np.log(a)/np.log(2)
)

print(
    np.e,
    np.exp([0, 1, 2]),
    np.isclose(np.e, np.exp(1)),
    sep = '\n'
)

### Aggregate Functions

a = np.array([(1,2,3),
              (4,5,6)])

print(
    a.shape,
    a.sum(),        # all elements
    a.sum(axis=0),  # column wise
    a.sum(axis=1),  # row wise
    sep='\n'
)

print(
    np.median(a),
    np.median(a, axis=0),
    np.cumsum(a),
    sep = '\n'
)

### Modify Array

a = np.array([1, 2, 3, 1, 4])

idx, = np.where(a == 1)  # np.where returns a tuple when only condition provided
print(idx)

a = np.delete(a, idx)
a

a = np.array([1, 2, 3, 1, 4])

idx = np.where(a == 1, True, False)
print(idx)

b = a[~idx]
b

## Image processing with `matplotlib` & `numpy`

%matplotlib inline
from matplotlib.image import imread
import matplotlib.pyplot as plt

img = imread('/home/liao/img/bg/road-straight.jpg')
plt.imshow(img)

img.shape

img[::, ::, ::] == img

### Modify Image: Compression

Compress image by cutting the resolution to half, i.e. subset every two rows and every two columns in ndarray.

plt.imshow(img[::2, ::2, :])

### Modify Image: Color Mask

# np.where(<cond>, <value for True>, <value for False>)
img_mask = np.where(img > 180, 255, img)
plt.imshow(img_mask)

# np.where(<cond>, <value for True>, <value for False>)
img_mask = np.where(img < 80, 0, img)
plt.imshow(img_mask)