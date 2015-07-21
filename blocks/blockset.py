from UserList import UserList
from block import Block, block_in_polygon, block_in_segment
from itertools import product
import numbers





class BlockSet(UserList):
    """
    """

    def __init__(self, array_shape=None, block_shape=None, step=None, overlap=None, initlist=None):

        # There are two ways to construct a Blockset. Method 1 supercedes 2.
        # Method 1: provide a list of blocks via initlist
        if initlist != None:

            initlist = list(initlist)

            if not all([isinstance(b, Block) for b in initlist]):
                raise ValueError('[Error] Encountered input error for initlist. ' +
                    'initlist does not contain Blocks')

            self.array_shape = array_shape
            self.block_shape = block_shape
            self.step = step
            self.overlap = overlap

            if len(initlist) > 0:
                self.ndim = initlist[0].ndim
            else:
                self.ndim = 0

        # Method 2: specify array_shape, block_shape, step/overlap
        else:
            # check array_shape and block_shape
            self.array_shape = check_array_shape(array_shape)
            self.block_shape = check_block_shape(block_shape, array_shape)

            # step supercedes overlap, use zero overlap if neither specified
            if step != None:
                self.step = check_step(step, self.array_shape)
                self.overlap = step_to_overlap(step, self.block_shape)
            elif overlap != None:
                self.overlap = check_overlap(overlap, self.block_shape)
                self.step = overlap_to_step(self.overlap, self.block_shape)
            else:
                self.overlap = check_overlap(0.0, self.block_shape)
                self.step = overlap_to_step(self.overlap, self.block_shape)

            self.ndim = len(array_shape)

            initlist = find_blocks(self.array_shape, self.block_shape, self.step)


        UserList.__init__(self, initlist)


    def filter_blocks(self, polytope_vertices):
        initlist = filter(lambda x : filter_blocks(x, polytope_vertices), self)
        return BlockSet(self.array_shape, self.block_shape, self.step, self.overlap, initlist)






def filter_blocks(block, polytope_vertices):
    """
    """
    if block.ndim == 1:
        return block_in_segment(block.vertices, polytope_vertices)
    elif block.ndim == 2:
        return block_in_polygon(block.vertices, polytope_vertices)
    else:
        print('filter_blocks() is undefined for ndim > 2')
        return True












def overlap_to_step(overlap, block_shape):
    """
    """
    step = []
    ndim = len(overlap)

    for n in xrange(ndim):
        step.append(int( block_shape[n] * (1 -  overlap[n] ) ))

    return tuple(step)




def step_to_overlap(step, block_shape):
    """
    """
    overlap = []
    ndim = len(step)
    for n in xrange(ndim):
        overlap.append( 1 - float(step[n]) / block_shape[n] )

    return tuple(overlap)




def find_blocks(array_shape, block_shape, step):
    """Select blocks.

    Keyword arguments:
    array_shape -- shape of the array being divided: tuple(array_shape_dim0,...)
    block_shape -- size of the blocks: tuple(block_shape_dim0,...)
    step -- step size between blocks: tuple(step_dim0, step_dim1,...)

    Return values:
    blocks -- list of tuples, where each tuple contains slices for a block that 
                can be used for numpy array indexing

    """

    ndim = len(array_shape)

    blocks = []
    for n in xrange(ndim):
        coords = range(array_shape[n] - block_shape[n] + 1)
        coords = coords[::step[n]]
        blocks.append([slice(coord_i, coord_i + block_shape[n]) for coord_i in coords])


    return [Block(b) for b in list(product(*blocks))]















def check_array_shape(array_shape):
    """Helper function to verify array shape
    """
    if array_shape == None:
        raise ValueError('[Error] Encountered input error for array_shape. ' +
            'array_shape was not specified')

    if isinstance(array_shape, numbers.Number):
        array_shape = (array_shape,)
    elif isinstance(array_shape, list):
        array_shape = tuple(array_shape)

    if not isinstance(array_shape, tuple):
        raise ValueError('[Error] Encountered input error for array_shape. ' +
            'Acceptable input types include number, list, tuple')

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

    if block_shape == None:
        block_shape = array_shape

    if isinstance(block_shape, numbers.Number):
        block_shape = (block_shape,) * len(array_shape)
    elif isinstance(block_shape, list):
        block_shape = tuple(block_shape)

    if not isinstance(block_shape, tuple):
        raise ValueError('[Error] Encountered input error for block_shape. ' +
            'Acceptable input types include number, list, tuple')

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

    if step == None:
        step = (1,) * len(array_shape)

    if isinstance(step, numbers.Number):
        step = (step,) * len(array_shape)
    elif isinstance(step, list):
        step = tuple(step)

    if not isinstance(step, tuple):
        raise ValueError('[Error] Encountered input error for step. ' +
            'Acceptable input types include number, list, tuple')

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



def check_overlap(overlap, array_shape):
    """Helper function to verify overlap
    """
    if overlap == None:
        return None

    if isinstance(overlap, numbers.Number):
        overlap = (overlap,) * len(array_shape)
    elif isinstance(overlap, list):
        overlap = tuple(overlap)

    if not isinstance(overlap, tuple):
        raise ValueError('[Error] Encountered input error for overlap. ' +
            'Acceptable input types include number, list, or tuple')


    if len(overlap) != len(array_shape):
        raise ValueError('[Error] Encountered input error for overlap. ' +
            'Different number of dimensions for array_shape and block_shape.')

    if any([not isinstance(o, numbers.Number) for o in overlap]):
        raise ValueError('[Error] Encountered non-numeric values for overlap')

    if any([o < 0 for o in overlap]):
        raise ValueError('[Error] Encountered values <0 for overlap')

    if any([o >= 1 for o in overlap]):
        raise ValueError('[Error] Encountered values >= 1 for overlap')

    return overlap


