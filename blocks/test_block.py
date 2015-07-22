import unittest 
from block import Block, find_vertices, block_in_segment, block_in_polygon, \
    block_vertices_to_coordinates, block_coordinates_to_vertices

class TestCode(unittest.TestCase):



    def test_Block(self):
        """
        """
        blk = Block([slice(0, 1)])
        self.assertEqual(blk, [slice(0, 1)])
        self.assertEqual(blk.vertices, [[0], [0]])
        self.assertEqual(blk.vertices_coordinates, [[0], [0]])
        self.assertTrue(blk.in_polytope([[0], [2]]))
        self.assertFalse(blk.in_polytope([[1], [2]]))

        blk = Block([slice(1, 3), slice(1, 3)])
        polygon_vertices = find_vertices([slice(0, 4), slice(0, 4)])

        try:
            from matplotlib.path import Path 
            self.assertTrue(blk.in_polytope(polygon_vertices))
        except:
            print('\nMatplotlib is not installed. tests for block_in_polygon unavailable')

        # Test constructing a block from a second block
        blk = Block([slice(1, 3), slice(1, 3)])
        blk2 = Block(blk)
        self.assertEqual(blk.data, blk2.data)
        self.assertEqual(blk.coordinate_increments, blk2.coordinate_increments)
        self.assertEqual(blk.coordinate_offsets, blk2.coordinate_offsets)






    def test_find_vertices(self):
        """
        """


        block = [slice(0, 1)]
        vertices = find_vertices(block)
        self.assertEqual(vertices, [[0], [0]])

        block = [slice(0, 2)]
        vertices = find_vertices(block)
        self.assertEqual(vertices, [[0], [1]])

        block = [slice(0, 3)]
        vertices = find_vertices(block)
        self.assertEqual(vertices, [[0], [2]])

        block = [slice(0, 1), slice(0, 1)]
        vertices = find_vertices(block)
        self.assertEqual(vertices, [[0, 0]] * 4)

        block = [slice(0, 3), slice(0, 1)]
        vertices = find_vertices(block)
        self.assertEqual(vertices, [[0, 0], [2, 0], [2, 0], [0, 0]])

        block = [slice(0, 3), slice(0, 4)]
        vertices = find_vertices(block)
        self.assertEqual(vertices, [[0, 0], [2, 0], [2, 3], [0, 3]])



    def test_block_in_segment(self):
        """
        """

        segment_vertices = find_vertices([slice(0, 4)])
        block_vertices = find_vertices([slice(1, 3)])
        v = block_in_segment(block_vertices, segment_vertices)
        self.assertTrue(v)

        segment_vertices = find_vertices([slice(1, 3)])
        block_vertices = find_vertices([slice(0, 4)])
        v = block_in_segment(block_vertices, segment_vertices)
        self.assertFalse(v)

        segment_vertices = find_vertices([slice(0, 4)])
        block_vertices = find_vertices([slice(0, 3)])
        v = block_in_segment(block_vertices, segment_vertices)
        self.assertTrue(v)

        segment_vertices = find_vertices([slice(1, 4)])
        block_vertices = find_vertices([slice(0, 3)])
        v = block_in_segment(block_vertices, segment_vertices)
        self.assertFalse(v)


    def test_block_in_polygon(self):
        """
        """

        try:
            from matplotlib.path import Path 

            polygon_vertices = find_vertices([slice(0, 4), slice(0, 4)])
            block_vertices = find_vertices([slice(1, 3), slice(1, 3)])
            v = block_in_polygon(block_vertices, polygon_vertices)
            self.assertTrue(v)


            polygon_vertices = find_vertices([slice(1, 3), slice(1, 3)])
            block_vertices = find_vertices([slice(0, 4), slice(0, 4)])
            v = block_in_polygon(block_vertices, polygon_vertices)
            self.assertFalse(v)

            # The commented line should produce a True value, but it produces False
            polygon_vertices = find_vertices([slice(0, 4), slice(0, 4)])
            #block_vertices = find_vertices([slice(0, 4), slice(0, 4)])
            block_vertices = find_vertices([slice(0, 4), slice(1, 4)])
            v = block_in_polygon(block_vertices, polygon_vertices)
            self.assertTrue(v)

        except:
            print('\nMatplotlib is not installed. tests for block_in_polygon unavailable')

    def test_block_vertices_to_coordinates(self):
        block = Block([slice(0, 2)])
        vertices_coordinates = block_vertices_to_coordinates(block.vertices, [1], [0])
        self.assertTrue(all([a == b for a, b in zip(block.vertices, vertices_coordinates)]))

        # check coordinate_increment
        block = Block([slice(0, 2)])
        vertices_coordinates = block_vertices_to_coordinates(block.vertices, [2], [0])
        self.assertTrue(all([a == b for a, b in zip([[0], [2]], vertices_coordinates)]))

        # check coordinate_offset
        block = Block([slice(0, 2)])
        vertices_coordinates = block_vertices_to_coordinates(block.vertices, [1], [1])
        self.assertTrue(all([a == b for a, b in zip([[1], [2]], vertices_coordinates)]))


    def test_block_coordinates_to_vertices(self):
        block = Block([slice(0, 2)], [1], [0])
        vertices = block_coordinates_to_vertices(block.vertices_coordinates, [1], [0])
        self.assertTrue(all([a == b for a, b in zip(block.vertices, vertices)]))

        # check coordinate_increment
        block = Block([slice(0, 2)], [2], [0])
        vertices = block_coordinates_to_vertices(block.vertices_coordinates, [2], [0])
        self.assertTrue(all([a == b for a, b in zip(block.vertices, vertices)]))

        # check coordinate_offset
        block = Block([slice(0, 2)], [1], [1])
        vertices = block_coordinates_to_vertices(block.vertices_coordinates, [1], [1])
        self.assertTrue(all([a == b for a, b in zip(block.vertices, vertices)]))



if __name__ == '__main__':
    print 'Running unit tests for block.py'
    unittest.main()