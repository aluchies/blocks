import unittest 
from block import Block, find_vertices

class TestCode(unittest.TestCase):



    def test_Block(self):
        """
        """
        blk = Block([slice(0, 1)])
        self.assertEqual(blk, [slice(0, 1)])
        self.assertEqual(blk.vertices, [[0], [0]])




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





if __name__ == '__main__':
    print 'Running unit tests for block.py'
    unittest.main()