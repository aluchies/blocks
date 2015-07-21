import unittest 
from blocks import BlockSet, check_array_shape, check_block_shape, check_step, \
    find_blocks, block_to_vertices, overlap_to_step, step_to_overlap, \
    check_overlap

class TestCode(unittest.TestCase):



    def test_BlockSet(self):
        """
        """
        bs = BlockSet((2,2))
        self.assertEqual(bs.array_shape, (2, 2))
        self.assertEqual(bs.block_shape, (2, 2))
        self.assertEqual(bs.step, (2, 2))
        self.assertEqual(bs.overlap, (0, 0))
        self.assertEqual(bs.blocks, [(slice(0, 2, None), slice(0, 2, None))])
        self.assertEqual(bs.vertices, [[[0, 0], [1, 0], [1, 1], [0, 1]]])





    def test_check_array_shape(self):
        """
        """
        array_shape = check_array_shape((2, 3))
        self.assertEqual(array_shape, (2, 3))

        array_shape = check_array_shape([3, 4, 2])
        self.assertEqual(array_shape, (3, 4, 2))

        array_shape = check_array_shape(3)
        self.assertEqual(array_shape, (3,))

    def test_check_block_shape(self):
        """
        """

        block_shape = check_block_shape(None, (2, 3))
        self.assertEqual(block_shape, (2, 3))

        block_shape = check_block_shape((2, 3), (2, 3))
        self.assertEqual(block_shape, (2, 3))

        block_shape = check_block_shape([3, 4, 2], (3, 4, 2))
        self.assertEqual(block_shape, (3, 4, 2))

        block_shape = check_block_shape(3, (5,))
        self.assertEqual(block_shape, (3,))

    def test_check_step(self):
        """
        """

        step = check_step(None, (2, 3))
        self.assertEqual(step, (1, 1))

        step = check_step((2, 3), (2, 3))
        self.assertEqual(step, (2, 3))

        step = check_step([3, 4, 2], (3, 4, 2))
        self.assertEqual(step, (3, 4, 2))

        step = check_step(3, (5,))
        self.assertEqual(step, (3,))



    def test_check_overlap(self):
        """
        """

        overlap = check_overlap(None, (2, 3))
        self.assertEqual(overlap, None)

        overlap = check_overlap((0.5, ), (2, ))
        self.assertEqual(overlap, (0.5, ))

        overlap = check_overlap(0.5, (2, ))
        self.assertEqual(overlap, (0.5, ))

        overlap = check_overlap((0.0, ), (2, ))
        self.assertEqual(overlap, (0.0, ))

        overlap = check_overlap((0.5, 0.5), (2, 2))
        self.assertEqual(overlap, (0.5, 0.5))


    def test_find_blocks(self):
        """
        """

        blocks = find_blocks((2, 2), (2, 2), (1, 1))
        self.assertEqual(blocks, [(slice(0, 2, None), slice(0, 2, None))])

        blocks = find_blocks((2, 2), (1, 1), (2, 2))
        self.assertEqual(blocks, [(slice(0, 1, None), slice(0, 1, None))])


    def test_block_to_vertices(self):
        """
        """


        block = [slice(0, 1)]
        vertices = block_to_vertices(block)
        self.assertEqual(vertices, [[0], [0]])

        block = [slice(0, 2)]
        vertices = block_to_vertices(block)
        self.assertEqual(vertices, [[0], [1]])

        block = [slice(0, 3)]
        vertices = block_to_vertices(block)
        self.assertEqual(vertices, [[0], [2]])

        block = [slice(0, 1), slice(0, 1)]
        vertices = block_to_vertices(block)
        self.assertEqual(vertices, [[0, 0]] * 4)

        block = [slice(0, 3), slice(0, 1)]
        vertices = block_to_vertices(block)
        self.assertEqual(vertices, [[0, 0], [2, 0], [2, 0], [0, 0]])

        block = [slice(0, 3), slice(0, 4)]
        vertices = block_to_vertices(block)
        self.assertEqual(vertices, [[0, 0], [2, 0], [2, 3], [0, 3]])



    def test_overlap_to_step(self):
        """
        """

        step = overlap_to_step((0.5, ), (2, ))
        self.assertEqual(step, (1,))

        step = overlap_to_step((0.5, ), (4, ))
        self.assertEqual(step, (2,))

        step = overlap_to_step((0.5, 0.5), (4, 4))
        self.assertEqual(step, (2, 2))



    def test_step_to_overlap(self):
        """
        """

        overlap = step_to_overlap( (1,), (2,) )
        self.assertEqual(overlap, (0.5,))

        overlap = step_to_overlap( (2,), (4,) )
        self.assertEqual(overlap, (0.5,))

        overlap = step_to_overlap( (2, 2), (4, 4) )
        self.assertEqual(overlap, (0.5, 0.5))



if __name__ == '__main__':
    print 'Running unit tests for blocks.py'
    unittest.main()