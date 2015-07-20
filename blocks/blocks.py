from itertools import product
import numbers




def check_array_shape(array_shape):
    if isinstance(array_shape, numbers.Number):
        array_shape = (array_shape,)
    elif isinstance(array_shape, list):
        array_shape = tuple(array_shape)

    if not isinstance(array_shape, tuple):
        raise ValueError('[Error] Encountered input error for array_shape. \
            Acceptable input types include number, list, tuple, or 1D ndarray')

    if any([a <= 0 for a in array_shape]):
        raise ValueError('[Error] Encountered negative value for \
            array_shape.')

    if any([isinstance(a, int) for a in array_shape]):
        raise ValueError('[Error] Encountered non-integer values for \
            array_shape.')

    return array_shape



def check_block_shape(block_shape, array_shape):
    if isinstance(block_shape, numbers.Number):
        block_shape = (block_shape,) * len(array_shape)
    elif isinstance(block_shape, list):
        block_shape = tuple(block_shape)

    if not isinstance(block_shape, tuple):
        raise ValueError('[Error] Encountered input error for array_shape. \
            Acceptable input types include number, list, tuple, or 1D ndarray')

    if len(block_shape) != len(array_shape):
        raise ValueError('[Error] Encountered input error for block_shape. \
            Different number of dimensions for array_shape and block_shape.')

    if any([b <= 0 for a in block_shape]):
        raise ValueError('[Error] Encountered negative value for \
            array_shape.')

    if any([a < b for a, b in zip(array_shape, block_shape)]):
        raise ValueError('[Error] Encountered block_shape larger than \
            array_shape.')

    if any([isinstance(b, int) for b in array_shape]):
        raise ValueError('[Error] Encountered non-integer values for \
            block_shape.')

    return block_shape



def check_step(step, array_shape):
    if isinstance(step, numbers.Number):
        step = (step,) * len(array_shape)
    elif isinstance(step, list):
        step = tuple(step)

    if not isinstance(step, tuple):
        raise ValueError('[Error] Encountered input error for step. \
            Acceptable input types include number, list, tuple, or 1D ndarray')

    if len(step) != len(array_shape):
        raise ValueError('[Error] Encountered input error for step. \
            Different number of dimensions for array_shape and block_shape.')

    if any([s <= 0 for s in step]):
        raise ValueError('[Error] Encountered negative value for \
            step.')

    if any([isinstance(s, int) for s in step_shape]):
        raise ValueError('[Error] Encountered non-integer values for \
            step.')

    return step




def find_block_coords(array_shape, block_shape, step=1):
    """Determine coordinates for overlapping blocks havine block_shape and step
    size.

    Keyword arguments:
    array_shape -- shape of the array being divided
    block_shape -- size of the blocks
    step -- step size between blocks

    Return values:
    origin_list -- list of origin points

    """

    array_shape = check_array_shape(array_shape)
    block_shape = check_block_shape(block_shape, array_shape)
    step = check_step(step, array_shape)

    ndim = len(array_shape)


    block_origin_list = []
    for n in xrange(ndim):
        block_origin_list.append(range(array_shape[n] - block_shape[n] + 1)[::step[n]])

    return list(product(*block_origin_list))