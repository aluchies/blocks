from itertools import product
import numbers




def find_blocks(array_shape, block_shape, step=1):
    """Select blocks.

    Keyword arguments:
    array_shape -- shape of the array being divided: tuple(array_shape_dim0,...)
    block_shape -- size of the blocks: tuple(block_shape_dim0,...)
    step -- step size between blocks: tuple(step_dim0, step_dim1,...)

    Return values:
    blocks -- list of tuples, where each tuple contains slices for a block that 
                can be used for numpy array indexing

    """

    array_shape = check_array_shape(array_shape)
    block_shape = check_block_shape(block_shape, array_shape)
    step = check_step(step, array_shape)

    ndim = len(array_shape)

    blocks = []
    for n in xrange(ndim):
        coords = range(array_shape[n] - block_shape[n] + 1)
        coords = coords[::step[n]]
        blocks.append([slice(coord_i, coord_i + block_shape[n]) for coord_i in coords])

    return list(product(*blocks))






def block_to_vertices(block):
    """Find vertices for a block. Return a list of lists. The ith item of the
    outer list is the ith vertex. The nth item of an inner list is the nth
    coordinate for that vertex: [[vertex1], [vertex2],...] also written as
    [[x0, y0,...], [x1, y1,...],...]
    """

    ndim = len(block)

    # list vertices by axis [[x0, x1,...], [y0, y1,...],...]
    va = []
    for n in xrange(0, ndim):
        dim_vertices = [ block[n].start, block[n].stop - 1 ]
        va.append( sorted(dim_vertices * 2 ** n ))
        # loop through previous dimensions
        for m in xrange(0, n):
            va[m] = va[m] + va[m][::-1]



    # list by vertex [[x0, y0,...], [x1, y1,...],...]
    vv = []
    for i in xrange(2 ** ndim):
        vv.append([va[0][i]])
        for n in xrange(1, ndim):
            vv[i].append(va[n][i])


    return vv



def blocks_to_vertices(blocks):
    """Find vertices for a list of blocks. Return a list of lists of lists.
    The kth item of the outer list is the kth block. The ith item of the
    middle list is the ith vertex. The nth item of an inner list is the nth
    coordinate for that vertex: [[[vertex1], [vertex2],...],...] also written as
    [[[x0, y0,...], [x1, y1,...],...],...]
    """
    return filter(block_to_vertices, blocks)






def check_array_shape(array_shape):
    """Helper function to verify array shape
    """
    if isinstance(array_shape, numbers.Number):
        array_shape = (array_shape,)
    elif isinstance(array_shape, list):
        array_shape = tuple(array_shape)

    if not isinstance(array_shape, tuple):
        raise ValueError('[Error] Encountered input error for array_shape. ' +
            'Acceptable input types include number, list, tuple, or 1D ndarray')

    if any([a <= 0 for a in array_shape]):
        raise ValueError('[Error] Encountered negative value for ' +
            'array_shape.')

    if not all([isinstance(a, int) for a in array_shape]):
        raise ValueError('[Error] Encountered non-integer values for ' +
            'array_shape.')

    return array_shape



def check_block_shape(block_shape, array_shape):
    """Helper function to verify block shape
    """
    array_shape = check_array_shape(array_shape)

    if isinstance(block_shape, numbers.Number):
        block_shape = (block_shape,) * len(array_shape)
    elif isinstance(block_shape, list):
        block_shape = tuple(block_shape)

    if not isinstance(block_shape, tuple):
        raise ValueError('[Error] Encountered input error for block_shape. ' +
            'Acceptable input types include number, list, tuple, or 1D ndarray')

    if len(block_shape) != len(array_shape):
        raise ValueError('[Error] Encountered input error for block_shape. ' +
            'Different number of dimensions for array_shape and block_shape.')

    if any([b <= 0 for b in block_shape]):
        raise ValueError('[Error] Encountered negative value for ' +
            'block_shape.')

    if any([a < b for a, b in zip(array_shape, block_shape)]):
        raise ValueError('[Error] Encountered block_shape larger than ' + 
            'block_shape.')

    if not all([isinstance(b, int) for b in array_shape]):
        raise ValueError('[Error] Encountered non-integer values for ' +
            'block_shape.')

    return block_shape



def check_step(step, array_shape):
    """Helper function to verify step
    """
    array_shape = check_array_shape(array_shape)
    if isinstance(step, numbers.Number):
        step = (step,) * len(array_shape)
    elif isinstance(step, list):
        step = tuple(step)

    if not isinstance(step, tuple):
        raise ValueError('[Error] Encountered input error for step. ' +
            'Acceptable input types include number, list, tuple, or 1D ndarray')

    if len(step) != len(array_shape):
        raise ValueError('[Error] Encountered input error for step. ' +
            'Different number of dimensions for array_shape and block_shape.')

    if any([s <= 0 for s in step]):
        raise ValueError('[Error] Encountered negative value for ' +
            'step.')

    if not all([isinstance(s, int) for s in step ]):
        raise ValueError('[Error] Encountered non-integer values for ' +
            'step.')

    return step