import unittest 
from blockset import BlockSet, \
    check_array_shape, check_block_shape, check_step, check_overlap, \
    overlap_to_step, step_to_overlap, one_center_block, spanning_blocks
from block import Block, find_vertices

class TestCode(unittest.TestCase):




    def test_BlockSet(self):
        """
        """

        bs = BlockSet(initlist=[Block([slice(0, 2)])])
        self.assertTrue(isinstance(bs, BlockSet))
        self.assertEqual(bs, [Block([slice(0, 2)])])

        bs = BlockSet(initlist=[Block([slice(0, 2), slice(0, 2)])])
        self.assertTrue(isinstance(bs, BlockSet))
        self.assertEqual(bs, [Block([slice(0, 2), slice(0, 2)])])

        bs0 = BlockSet(initlist=[Block([slice(0, 2)])])
        self.assertTrue(isinstance(bs, BlockSet))
        polygon_vertices = find_vertices([slice(0, 4)])
        bs1 = bs0.filter_blocks(polygon_vertices)
        self.assertEqual(bs0, bs1)

        bs0 = BlockSet(initlist=[Block([slice(0, 2)])])
        self.assertTrue(isinstance(bs, BlockSet))
        polygon_vertices = find_vertices([slice(0, 1)])
        bs1 = bs0.filter_blocks(polygon_vertices)
        self.assertTrue(bs0 != bs1)







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


    def test_one_center_block(self):
        """
        """

        array_shape = [5, 5]
        block_shape = [2, 2]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [[slice(2, 4), slice(2, 4)]]
        self.assertEqual(bs, bs_real)

        array_shape = [5, 5]
        block_shape = [3, 3]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [[slice(1, 4), slice(1, 4)]]
        self.assertEqual(bs, bs_real)

        array_shape = [6, 6]
        block_shape = [2, 2]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [[slice(2, 4), slice(2, 4)]]
        self.assertEqual(bs, bs_real)

        array_shape = [6, 6]
        block_shape = [3, 3]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [[slice(2, 5), slice(2, 5)]]
        self.assertEqual(bs, bs_real)


    def test_spanning_blocks(self):
        """
        """

        array_shape = (2, 2)
        block_shape = (2, 2)
        bs = spanning_blocks(array_shape, block_shape)
        bs_real = [[slice(0, 2), slice(0, 2)]]
        self.assertEqual(bs, bs_real)


        array_shape = (4, 4)
        block_shape = (2, 2)
        bs = spanning_blocks(array_shape, block_shape)
        bs_real = [[slice(0, 2, None), slice(0, 2, None)],
                   [slice(0, 2, None), slice(2, 4, None)],
                   [slice(2, 4, None), slice(0, 2, None)],
                   [slice(2, 4, None), slice(2, 4, None)]]
        self.assertEqual(bs, bs_real)





if __name__ == '__main__':
    print 'Running unit tests for blocks.py'
    unittest.main()