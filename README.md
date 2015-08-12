blocks
======

simple n-dimensional array blocks
---------------------------------

Suppose you need to divide an n-dimensional numpy array into overlapping blocks. With blocks you can do the following:

```
blockset = spanning_blocks(array_shape, block_shape, step)

for b in blockset:
	numpy_array[b]
```

Instead of creating a list of numpy arrays for each block, keep the original numpy array intact, and use a `BlockSet` to record the indices of the `Block`s. Each `Block` is a list of `slice`s having length equal to the number of dimensions of the array. For example

```
>>>arr = np.asarray([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

>>>block = Block([slice(0, 2), slice(0, 2)])

[slice(0, 2, None), slice(0, 2, None)]

>>>arr[block]

array([[0, 1],
       [3, 4]])
```

The vertices of a `Block` are included 

```
>>>block.vertices

[(0, 0), (0, 1), (1, 1), (1, 0)]
```

For 1- and 2-dimensions a method to determine if the block is contained in an arbitrary polytope is provided

```
>>>block.in_polytope(polytope_vertices)

True
```

A `BlockSet` is a list of `Block`s. Several helper functions for creating `BlockSet`s are provided, including `spanning_blocks`

```
>>>blockset = spanning_blocks(array_shape=(3,3), block_shape=(2,2), step=1)

[[slice(0, 2, None), slice(0, 2, None)], [slice(0, 2, None), slice(1, 3, None)], 
 [slice(1, 3, None), slice(0, 2, None)], [slice(1, 3, None), slice(1, 3, None)]]
```

and `one_center_block`

```
>>>blockset = one_center_block(array_shape=(4,4), block_shape=(2,2))

[[slice(1, 3, None), slice(1, 3, None)]]
```


Installation
------------

```
python setup.py install
```


Notes
-----

1. Some of the functionality in blocks requires matplotlib, but blocks can be installed and used without a matplotlib installation.