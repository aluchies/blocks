import unittest 
from blocks import check_array_shape, check_block_shape, check_step, \
    find_blocks

class TestCode(unittest.TestCase):
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

        block_shape = check_block_shape((2, 3), (2, 3))
        self.assertEqual(block_shape, (2, 3))

        block_shape = check_block_shape([3, 4, 2], (3, 4, 2))
        self.assertEqual(block_shape, (3, 4, 2))

        block_shape = check_block_shape(3, 5)
        self.assertEqual(block_shape, (3,))

    def test_check_step(self):
        """
        """

        step = check_step((2, 3), (2, 3))
        self.assertEqual(step, (2, 3))

        step = check_step([3, 4, 2], (3, 4, 2))
        self.assertEqual(step, (3, 4, 2))

        step = check_step(3, 5)
        self.assertEqual(step, (3,))


    def test_find_blocks(self):
        """
        """

        blocks = find_blocks((2, 2), (2, 2), 1)
        self.assertEqual(blocks, [(slice(0, 2, None), slice(0, 2, None))])

        blocks = find_blocks((2, 2), (1, 1), 2)
        self.assertEqual(blocks, [(slice(0, 1, None), slice(0, 1, None))])


if __name__ == '__main__':
    print 'Running unit tests for blocks.py'
    unittest.main()