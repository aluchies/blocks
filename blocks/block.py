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

    def in_polytope(self, polytope_vertices):
        if self.ndim == 1:
            return block_in_segment(self.vertices, polytope_vertices)


        elif self.ndim == 2:

            return block_in_polygon(self.vertices, polytope_vertices)

        else:
            print('in_polytope() is undefined for ndim > 2')
            return None



def block_in_segment(block_vertices, segment_vertices):
    """
    """

    # verify segment_vertices
    if (len(segment_vertices) != 2) or (len(segment_vertices[0]) != 1) or (len(segment_vertices[1]) != 1):
        raise ValueError('[Error] Encountered input error for segment_vertices. '
            + 'vertices do not specify a segment')

    segment_max = max(segment_vertices)
    segment_min = min(segment_vertices)
    block_max = max(block_vertices)
    block_min = min(block_vertices)

    if (segment_max >= block_max) and (segment_min <= block_min):
        return True
    else:
        return False






def block_in_polygon(block_vertices, polygon_vertices):
    """

    Keyword arguments:
    vertices -- [[x0, y0], [x1, y1], ...]
    polygon_vertices -- [[x0, y0], [x1, y1], ...]

    Return values
    val -- True/False block is in polygon

    """

    try:
        from matplotlib.path import Path 
        #print('\nMatplotlib is installed.')

    except:
        print('\nMatplotlib is not installed. block_in_polygon() returns None')
        return None

    # verify polygon vertices
    if len(polygon_vertices) < 3:
        raise ValueError('[Error] Encountered input error for polygon_vertices. '
            + 'Three vertices needed to specify polygon.')

    if [len(v) for v in polygon_vertices] != [2, ] * len(polygon_vertices):
        raise ValueError('[Error] Encountered input error for polygon_vertices. '
            + 'Vertices do not have two coordinates.')

    # repeat first polygon vertex at end of list
    if not all([a == b for a, b in zip(polygon_vertices[0], polygon_vertices[-1])]):
        polygon_vertices = polygon_vertices + [polygon_vertices[0]]

    # create path object
    polygon_path = Path(polygon_vertices, closed=True)

    # repeat first block vertex at end of list
    if block_vertices[0] != block_vertices[-1]:
        block_vertices = block_vertices + [block_vertices[0]]

    block_path = Path(block_vertices, closed=True)


    # Note: there appears to be an error in contains_points(). For
    # example, reversing the direction of the vertices requires raidus=-0.01
    # to be specified. See the e-mails in the link below
    # http://matplotlib.1069221.n5.nabble.com/How-to-properly-use-path-Path-contains-point-tc40718.html#none
    return bool(polygon_path.contains_path(block_path))
    #return path.contains_points(block_vertices, radius=0.01).all()




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

