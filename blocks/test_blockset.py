import unittest 
from blockset import BlockSet, \
    check_array_shape, check_block_shape, check_step, check_overlap, \
    overlap_to_step, step_to_overlap, find_blocks, one_center_block
from block import Block, find_vertices

class TestCode(unittest.TestCase):




    def test_BlockSet(self):
        """
        """

        bs = BlockSet(initlist=[Block([slice(0, 2)])])
        self.assertTrue(isinstance(bs, BlockSet))
        self.assertEqual(bs.array_shape, None)
        self.assertEqual(bs.block_shape, None)
        self.assertEqual(bs.step, None)
        self.assertEqual(bs.overlap, None)


        bs = BlockSet(initlist=[Block([slice(0, 2), slice(0, 2)])])
        self.assertTrue(isinstance(bs, BlockSet))
        self.assertEqual(bs.array_shape, None)
        self.assertEqual(bs.block_shape, None)
        self.assertEqual(bs.step, None)
        self.assertEqual(bs.overlap, None)


        bs = BlockSet(array_shape=(2,2))
        self.assertTrue(isinstance(bs, BlockSet))
        self.assertEqual(bs.array_shape, (2, 2))
        self.assertEqual(bs.block_shape, (2, 2))
        self.assertEqual(bs.step, (2, 2))
        self.assertEqual(bs.overlap, (0, 0))
        self.assertEqual(bs, [ Block( [slice(0, 2, None), slice(0, 2, None)] ) ])

        bs0 = BlockSet(array_shape=(2,))
        self.assertTrue(isinstance(bs, BlockSet))
        polygon_vertices = find_vertices([slice(0, 4)])
        bs1 = bs0.filter_blocks(polygon_vertices)
        self.assertEqual(bs0, bs1)

        bs0 = BlockSet(array_shape=(2,))
        self.assertTrue(isinstance(bs, BlockSet))
        polygon_vertices = find_vertices([slice(0, 1)])
        bs1 = bs0.filter_blocks(polygon_vertices)
        self.assertTrue(bs0 != bs1)

        array_shape = (1000, 1000)
        block_shape = (600, 600)
        overlap = 0.
        bs = BlockSet(array_shape=array_shape, block_shape=block_shape, overlap=overlap,
                   coordinate_increments=2e-3, coordinate_offsets=0)









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
        bs_real = [slice(2, 4), slice(2, 4)]
        self.assertTrue(all([s == s_real for s, s_real in zip(bs[0], bs_real)]))

        array_shape = [5, 5]
        block_shape = [3, 3]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [slice(1, 4), slice(1, 4)]
        self.assertTrue(all([s == s_real for s, s_real in zip(bs[0], bs_real)]))

        array_shape = [6, 6]
        block_shape = [2, 2]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [slice(2, 4), slice(2, 4)]
        self.assertTrue(all([s == s_real for s, s_real in zip(bs[0], bs_real)]))

        array_shape = [6, 6]
        block_shape = [3, 3]
        bs = one_center_block(array_shape, block_shape)
        bs_real = [slice(2, 5), slice(2, 5)]
        self.assertTrue(all([s == s_real for s, s_real in zip(bs[0], bs_real)]))





if __name__ == '__main__':
    print 'Running unit tests for blocks.py'
    unittest.main()