from UserList import UserList


class Block(UserList):
    """
    """

    def __init__(self, initlist):
        initlist = check_slice_list(initlist)
        UserList.__init__(self, initlist)

        # infer shape
        ndim = len(self)
        shape = []
        for n in xrange(ndim):
            shape.append( self[n].stop - self[n].start )

        self.ndim = ndim
        self.shape = tuple(shape)

        # find vertices
        self.vertices = find_vertices(self)




def check_slice_list(slice_list):
    """
    """

    if isinstance(slice_list, slice):
        slice_list = [slice_list]

    if not isinstance(slice_list, (tuple, list)):
        raise ValueError('[Error] Encountered input error for slice_list. ' +
            'Acceptable input types include list or tuple')

    if not all([isinstance(s, slice) for s in slice_list]):
        raise ValueError('[Error] Encountered non-slices in slice_list.')

    if not all([isinstance(s.start, int) for s in slice_list]):
        raise ValueError('[Error] Encountered non-integer values in slice_list.')

    if not all([isinstance(s.stop, int) for s in slice_list]):
        raise ValueError('[Error] Encountered non-integer values in slice_list.')

    if not all([s.start >= 0 for s in slice_list]):
        raise ValueError('[Error] Encountered negative values in slice_list.')

    if not all([s.stop >= 0 for s in slice_list]):
        raise ValueError('[Error] Encountered negative values in slice_list.')

    return slice_list





def find_vertices(block):
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

