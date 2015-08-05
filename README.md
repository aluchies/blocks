blocks
======

simple n-dimensional array blocks
---------------------------------

Suppose you need to divide an n-dimensional numpy array into blocks. With blocks you can do the following:

```
blockset = BlockSet(array_shape, block_shape, step)

for b in blockset:
	numpy_array[b]
```

All you need to do is specify the array shape, block shape, and step size between blocks. 

Each `Block` is a list of `slice`s having length equal to the number of dimensions of the array. For example

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

A `BlockSet` is a list of `Block`s that includes a method for generating a collection of blocks given an `array_shape`, `block_shape`, and `step` size.

```
>>>blockset = BlockSet(array_shape=(3,3), block_shape=(2,2), step=1)

[[slice(0, 2, None), slice(0, 2, None)], [slice(0, 2, None), slice(1, 3, None)], 
 [slice(1, 3, None), slice(0, 2, None)], [slice(1, 3, None), slice(1, 3, None)]]
```




Installation
------------

```
python setup.py install
```


Notes
-----

1. Some of the functionality in blocks requires matplotlib, but blocks can be installed and used without a matplotlib installation.