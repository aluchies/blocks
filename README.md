blocks
======

simple n-dimensional array blocks
---------------------------------

Suppose you need to divide an n-dimensional numpy array into blocks. Imagine being able to do the following:

```
blocks = get_blocks(array_shape, block_shape, step)

for block in blocks:
	numpy_array[block]
```

All you need to do is specify the array shape, block shape, and step size between blocks. blocks takes care of the rest. Each block is a tuple of slices used to index a numpy array.


Installation
------------

```
python setup.py install
```