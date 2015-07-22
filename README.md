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
>>>print(block)
[slice(x0, x1), slice(y0, y1), ...]
```

The corners of a `Block` are included 

```
>>>print(block.vertices)
[(0, 0), (0, 1), (1, 1), (1, 0)]
```

For 1- and 2-dimensions a method to determine if the block is contained in an arbitrary polytope is provided

```
>>>print(block.in_polytope(polytope_vertices))
True
```

A `BlockSet` is a list of `Block`s that includes a method for generating a collection of blocks given an `array_shape`, `block_shape`, and `step` size.



Installation
------------

```
python setup.py install
```


Notes
_____

Some of the functionality requires matplotlib, but blocks can be installed and used without a matplotlib installation.